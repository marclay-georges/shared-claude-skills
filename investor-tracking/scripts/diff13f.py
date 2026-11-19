"""Compare two quarters of one investor's holdings and separate flows from decisions.

What it reports, and why each piece is there:

- share changes adjusted for splits (managers.yaml corporate_actions) and CUSIP aliases, so a
  15-for-1 split doesn't read as a 1,400% purchase;
- new positions and full exits, the clearest decisions a 13F shows;
- the flow rate: the median and the most common percentage share change across the core
  names (held in both quarters, no options, at least --core-min-weight of the earlier book).
  When clients add or withdraw money, most names move by about the same percentage, and that
  shared move says nothing about the manager's view. Each name's deviation from the median is
  where the view shows;
- a value-versus-shares check: when shares jump while the implied price falls by the same
  factor, it is probably a split nobody listed, and it is flagged rather than read as a trade;
- an estimated buy/sell amount per name (share change times the average of the two implied
  prices), which is rough: it assumes trades happened at mid-quarter prices.

CUSIPs listed under exclude_from_weights (Pershing Square Inc.'s stake in itself) are left
out of weights, totals and the flow rate, and shown separately.

    python diff13f.py PREV.csv CUR.csv --investor akre [--core-min-weight 1.0] [--json out.json]

The quarter of each file is read from its name (YYYY-QN.csv) unless --prev-quarter and
--cur-quarter are given.
"""
import argparse
import collections
import csv
import json
import os
import re
import statistics
import sys

import edgar

SPLIT_LIKE = [1.5, 2, 3, 4, 5, 8, 10, 15, 20, 25, 50]


def read_holdings(path):
    rows = {}
    with open(path, newline='') as f:
        for r in csv.DictReader(f):
            key = (r['cusip'].upper(), r.get('put_call') or '')
            rows[key] = {'issuer': r['issuer'], 'class': r['class'], 'shares': float(r['shares']),
                         'value': float(r['value_usd'])}
    return rows


def quarter_from_name(path):
    m = re.search(r'(\d{4}-Q[1-4])', os.path.basename(path))
    return m.group(1) if m else None


def adjust_previous(prev, investor, actions, prev_q, cur_q):
    """Rename aliased CUSIPs and restate the earlier share counts in post-split units."""
    aliases = investor.get('cusip_aliases') or {}
    renamed = {}
    for (cusip, pc), row in prev.items():
        renamed[(aliases.get(cusip, cusip), pc)] = row

    notes = []
    for action in actions:
        effective = str(action['quarter'])
        if action.get('type') != 'split' or not (prev_q < effective <= cur_q):
            continue
        for (cusip, pc), row in renamed.items():
            if cusip == action['cusip'].upper():
                row['shares'] = row['shares'] * float(action['ratio'])
                notes.append(f'{action["issuer"]}: earlier shares x{action["ratio"]} for the split in {effective}')
    return renamed, notes


def describe(prev, cur, excluded, core_min_weight):
    prev_total = sum(r['value'] for k, r in prev.items() if k[0] not in excluded)
    cur_total = sum(r['value'] for k, r in cur.items() if k[0] not in excluded)

    lines = []
    for key in set(prev) | set(cur):
        p, c = prev.get(key), cur.get(key)
        row = c or p
        line = {'cusip': key[0], 'put_call': key[1], 'issuer': row['issuer'], 'class': row['class'],
                'prev_shares': p['shares'] if p else 0, 'cur_shares': c['shares'] if c else 0,
                'prev_value': p['value'] if p else 0, 'cur_value': c['value'] if c else 0,
                'excluded': key[0] in excluded}
        line['prev_weight'] = 100 * line['prev_value'] / prev_total if prev_total and not line['excluded'] else 0
        line['cur_weight'] = 100 * line['cur_value'] / cur_total if cur_total and not line['excluded'] else 0

        if not p:
            line['status'] = 'new'
        elif not c:
            line['status'] = 'exit'
        else:
            change = (c['shares'] / p['shares'] - 1) * 100 if p['shares'] else None
            line['share_change_pct'] = change
            line['status'] = 'held'
            ### implied prices: a split nobody listed shows as shares up, price down by the same factor
            if p['shares'] and c['shares'] and p['value'] and c['value']:
                price_ratio = (c['value'] / c['shares']) / (p['value'] / p['shares'])
                share_ratio = c['shares'] / p['shares']
                line['price_change_pct'] = (price_ratio - 1) * 100
                for k in SPLIT_LIKE:
                    if abs(share_ratio / k - 1) < 0.12 and abs(price_ratio * k - 1) < 0.15:
                        line['possible_split'] = k
                        break

        ### rough dollars traded: share change at the average of the two implied prices
        prices = []
        if p and p['shares']:
            prices.append(p['value'] / p['shares'])
        if c and c['shares']:
            prices.append(c['value'] / c['shares'])
        line['est_traded_usd'] = (line['cur_shares'] - line['prev_shares']) * (sum(prices) / len(prices)) if prices else 0
        lines.append(line)

    ### flow rate across the core names
    core = [l for l in lines if l['status'] == 'held' and not l['put_call'] and not l['excluded']
            and l['prev_weight'] >= core_min_weight and l.get('share_change_pct') is not None
            and 'possible_split' not in l]
    changes = [l['share_change_pct'] for l in core]
    flow = {'core_names': len(core)}
    if changes:
        flow['median_pct'] = statistics.median(changes)
        buckets = collections.Counter(round(x) for x in changes)
        mode, count = buckets.most_common(1)[0]
        flow['modal_pct'] = mode
        flow['modal_count'] = count
        for l in lines:
            if l.get('share_change_pct') is not None:
                l['deviation_pct'] = l['share_change_pct'] - flow['median_pct']

    summary = {'prev_total': prev_total, 'cur_total': cur_total,
               'prev_lines': len(prev), 'cur_lines': len(cur),
               'net_est_traded_usd': sum(l['est_traded_usd'] for l in lines if not l['excluded']),
               'flow': flow}
    return summary, lines


def money(x):
    sign = '-' if x < 0 else ''
    x = abs(x)
    if x >= 1e9:
        return f'{sign}${x / 1e9:.2f}B'
    if x >= 1e6:
        return f'{sign}${x / 1e6:.1f}M'
    return f'{sign}${x / 1e3:.0f}K'


def print_report(investor_slug, prev_q, cur_q, summary, lines, notes, top):
    flow = summary['flow']
    print(f'## {investor_slug}: {prev_q} -> {cur_q}\n')
    print(f'Total {money(summary["prev_total"])} -> {money(summary["cur_total"])}; lines {summary["prev_lines"]} -> {summary["cur_lines"]}; estimated net trading {money(summary["net_est_traded_usd"])}.')
    if 'median_pct' in flow:
        print(f'Flow rate across {flow["core_names"]} core names: median {flow["median_pct"]:+.1f}%, most common {flow["modal_pct"]:+d}% ({flow["modal_count"]} names).')
    for n in notes:
        print(f'Adjusted: {n}')
    print()

    new = sorted([l for l in lines if l['status'] == 'new'], key=lambda l: -l['cur_value'])
    exits = sorted([l for l in lines if l['status'] == 'exit'], key=lambda l: -l['prev_value'])
    held = [l for l in lines if l['status'] == 'held']
    splits = [l for l in held if 'possible_split' in l]
    held = [l for l in held if 'possible_split' not in l]

    if new:
        print('### New')
        for l in new[:top]:
            pc = f' {l["put_call"]}' if l['put_call'] else ''
            print(f'- {l["issuer"]}{pc} ({l["cusip"]}): {l["cur_shares"]:,.0f} sh, {money(l["cur_value"])}, {l["cur_weight"]:.2f}%')
    if exits:
        print('### Exits')
        for l in exits[:top]:
            pc = f' {l["put_call"]}' if l['put_call'] else ''
            print(f'- {l["issuer"]}{pc} ({l["cusip"]}): was {l["prev_shares"]:,.0f} sh, {money(l["prev_value"])}, {l["prev_weight"]:.2f}%')
    if splits:
        print('### Share jumps that look like unlisted splits (check before reading as trades)')
        for l in splits:
            print(f'- {l["issuer"]} ({l["cusip"]}): shares {l["share_change_pct"]:+.0f}%, implied price {l["price_change_pct"]:+.0f}%, about {l["possible_split"]}-for-1')

    print('### Held names, largest deviation from the flow rate first')
    print('| issuer | weight | shares chg | vs median | price chg | est. traded |')
    print('|---|---|---|---|---|---|')
    held.sort(key=lambda l: -abs(l.get('deviation_pct', 0)) * max(l['prev_weight'], l['cur_weight'], 0.01))
    for l in held[:top]:
        pc = f' {l["put_call"]}' if l['put_call'] else ''
        excl = ' (excluded)' if l['excluded'] else ''
        dev = f'{l["deviation_pct"]:+.1f}' if 'deviation_pct' in l else ''
        price = f'{l["price_change_pct"]:+.0f}%' if 'price_change_pct' in l else ''
        print(f'| {l["issuer"]}{pc}{excl} | {l["prev_weight"]:.1f}% -> {l["cur_weight"]:.1f}% | {l["share_change_pct"]:+.1f}% | {dev} | {price} | {money(l["est_traded_usd"])} |')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('prev')
    parser.add_argument('cur')
    parser.add_argument('--investor', required=True)
    parser.add_argument('--prev-quarter')
    parser.add_argument('--cur-quarter')
    parser.add_argument('--core-min-weight', type=float, default=1.0, help='minimum earlier weight, in percent, for a core name')
    parser.add_argument('--top', type=int, default=25)
    parser.add_argument('--json', help='also write the full comparison here')
    parser.add_argument('--config')
    args = parser.parse_args()

    investors, actions = edgar.load_investors(args.config)
    investor = investors.get(args.investor)
    if investor is None:
        sys.exit(f'unknown investor {args.investor}')
    prev_q = args.prev_quarter or quarter_from_name(args.prev)
    cur_q = args.cur_quarter or quarter_from_name(args.cur)
    if not (prev_q and cur_q):
        sys.exit('name the quarters with --prev-quarter and --cur-quarter')

    excluded = {e['cusip'].upper() for e in investor.get('exclude_from_weights') or []}
    prev, notes = adjust_previous(read_holdings(args.prev), investor, actions, prev_q, cur_q)
    cur = read_holdings(args.cur)
    summary, lines = describe(prev, cur, excluded, args.core_min_weight)
    print_report(args.investor, prev_q, cur_q, summary, lines, notes, args.top)

    if args.json:
        with open(args.json, 'w') as f:
            json.dump({'investor': args.investor, 'prev_quarter': prev_q, 'cur_quarter': cur_q,
                       'adjustments': notes, 'summary': summary, 'lines': lines}, f, indent=1)


if __name__ == '__main__':
    main()
