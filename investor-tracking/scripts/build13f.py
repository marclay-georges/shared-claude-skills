"""Build one holdings file per quarter from an investor's 13F submissions.

For each quarter it takes every 13F the investor's filers made for that period and:

1. checks each filing against its own cover page (row count and total value). A filing
   that doesn't reconcile stops its quarter: nothing is written, and the gap is printed;
2. merges amendments. A RESTATEMENT amendment replaces what that filer reported before it;
   a NEW HOLDINGS amendment adds rows, usually positions that were under confidential
   treatment when the original was filed. A 13F-NT has no rows and only says who reports
   instead;
3. multiplies values by 1,000 for quarters listed in thousands_quarters, and warns when a
   quarter's total is about 1,000 times off its neighbours (a unit slip nobody listed);
4. sums rows by CUSIP plus put/call (Berkshire, for one, reports an issuer across many
   rows) and writes issuer, cusip, class, shares, value_usd, put_call, pct_of_portfolio.

Filers with a `book` in managers.yaml are written to their own subfolder. A sources file
records which accessions made each quarter.

    python build13f.py akre --from 2023-Q4 --to 2026-Q3 --cache ~/edgar-cache --out ~/investors/akre/holdings
    python build13f.py akre ... --raw-dir saved/   # saved copies instead of the cache; treat the result as unverified
"""
import argparse
import csv
import glob
import os
import re
import statistics
import sys

import edgar
from parse13f import parse_submission


def load_filings(filer_cik, folder, first, last):
    """Parse every 13F submission saved for one filer and keep those inside the quarter range."""
    start, end = edgar.quarter_end(first), edgar.quarter_end(last)
    records = []
    for path in sorted(glob.glob(os.path.join(folder, '*.txt'))):
        with open(path, encoding='utf-8', errors='replace') as f:
            text = f.read()
        if not re.search(r'CONFORMED SUBMISSION TYPE:\s*13F', text):
            continue
        record = parse_submission(text)
        if record['filer_cik'] and int(record['filer_cik']) != int(filer_cik):
            continue
        if start <= record['period'] <= end:
            records.append(record)
    return records


def _refiles_everything(amendment_rows, earlier_rows):
    """True when most of the earlier rows reappear, unchanged, in the amendment."""
    if not earlier_rows:
        return False
    amended = {(r['cusip'], r['shares'], r['value']) for r in amendment_rows}
    repeated = sum(1 for r in earlier_rows if (r['cusip'], r['shares'], r['value']) in amended)
    return repeated / len(earlier_rows) > 0.5


def merge_quarter(filings):
    """Apply each filer's amendments in filing order.

    Returns the merged rows, the filings whose rows survive (only these need to reconcile;
    an original replaced by a restatement may be wrong, which is why it was restated), and
    a note on how each filing was used.
    """
    state = {}
    used = []
    for f in sorted(filings, key=lambda r: (r['filed'], r['accession'])):
        current = state.setdefault(f['filer_cik'], {'rows': [], 'filings': []})
        if f['report_type'] == '13F NOTICE':
            reporters = ', '.join(m['name'] for m in f['other_managers_reporting']) or 'another filer'
            used.append((f, f'notice: holdings reported by {reporters}'))
            continue
        if not f['is_amendment']:
            state[f['filer_cik']] = {'rows': list(f['rows']), 'filings': [f]}
            used.append((f, 'original'))
        elif f['amendment_type'] == 'RESTATEMENT':
            state[f['filer_cik']] = {'rows': list(f['rows']), 'filings': [f]}
            used.append((f, 'restatement, replaces earlier rows'))
        elif _refiles_everything(f['rows'], current['rows']):
            # some filers label a complete re-filed table NEW HOLDINGS (Akre, Q1 2024);
            # adding it would count every position twice
            state[f['filer_cik']] = {'rows': list(f['rows']), 'filings': [f]}
            used.append((f, 'labelled new holdings but re-files the full table; replaces earlier rows'))
        else:
            current['rows'].extend(f['rows'])
            current['filings'].append(f)
            used.append((f, 'new holdings, added'))

    merged, contributing = [], []
    for filer_state in state.values():
        merged.extend(filer_state['rows'])
        contributing.extend(filer_state['filings'])
    return merged, contributing, used


def aggregate(rows, multiplier):
    """Sum shares and value by CUSIP plus put/call; name each line after its largest row."""
    groups = {}
    for r in rows:
        key = (r['cusip'], r['put_call'])
        g = groups.setdefault(key, {'shares': 0, 'value': 0, 'largest': r})
        g['shares'] += r['shares']
        g['value'] += r['value'] * multiplier
        if r['value'] > g['largest']['value']:
            g['largest'] = r

    total = sum(g['value'] for g in groups.values())
    lines = []
    for (cusip, put_call), g in groups.items():
        pct = round(100 * g['value'] / total, 4) if total else 0
        lines.append({
            'issuer': g['largest']['issuer'],
            'cusip': cusip,
            'class': g['largest']['class'],
            'shares': g['shares'],
            'value_usd': g['value'],
            'put_call': put_call,
            'pct_of_portfolio': f'{pct:.4f}',
        })
    lines.sort(key=lambda x: x['value_usd'], reverse=True)
    return lines, total


def write_csv(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['issuer', 'cusip', 'class', 'shares', 'value_usd', 'put_call', 'pct_of_portfolio'])
        writer.writeheader()
        writer.writerows(lines)


def unit_warnings(totals):
    """Quarters whose total is roughly 1,000 times off the median of the others."""
    warnings = []
    for quarter, total in totals.items():
        others = [t for q, t in totals.items() if q != quarter and t]
        if not others or not total:
            continue
        ratio = statistics.median(others) / total
        if ratio > 300 or ratio < 1 / 300:
            warnings.append(f'{quarter}: total ${total:,} is {ratio:,.0f}x off the other quarters; check whether it was filed in thousands')
    return warnings


def build(slug, investor, first, last, cache, out, raw_dir=None):
    thousands = set(investor.get('thousands_quarters') or [])
    books = {}
    for filer in investor['filers_13f']:
        folder = raw_dir or os.path.join(cache, 'filings', str(int(filer['cik'])))
        filings = load_filings(filer['cik'], folder, first, last)
        books.setdefault(filer.get('book', ''), []).extend(filings)

    ok = True
    for book, filings in books.items():
        book_out = os.path.join(out, book) if book else out
        by_quarter = {}
        for f in filings:
            by_quarter.setdefault(edgar.quarter_label(f['period']), []).append(f)

        totals = {}
        source_lines = []
        for quarter in sorted(by_quarter):
            quarter_filings = by_quarter[quarter]
            rows, contributing, used = merge_quarter(quarter_filings)

            ### every filing whose rows we keep must add up to its own cover page
            accepted = {str(g['accession']): g for g in investor.get('accepted_gaps') or []}
            for f in contributing:
                if not f['reconciled']['ok'] and f['accession'] in accepted:
                    gap = f['reconciled']
                    print(f'  {slug} {book or "main"} {quarter}: accepted known gap in {f["accession"]} (value {gap["value_gap"]:+,d}): {accepted[f["accession"]]["why"]}')
            for f in contributing:
                gap = f['reconciled']
                if gap['ok'] and gap['value_gap']:
                    print(f'  {slug} {book or "main"} {quarter}: {f["accession"]} rows differ from the cover by ${gap["value_gap"]:+,d}, within per-row rounding')
            bad = [f for f in contributing if not f['reconciled']['ok'] and f['accession'] not in accepted]
            superseded = [f for f in quarter_filings if f not in contributing and not f['reconciled']['ok']
                          and f['report_type'] != '13F NOTICE']
            for f in superseded:
                gap = f['reconciled']
                print(f'  {slug} {book or "main"} {quarter}: note, superseded {f["accession"]} did not reconcile (rows {gap["row_gap"]:+d}, value {gap["value_gap"]:+,d}); a later amendment replaced it')
            if bad:
                ok = False
                for f in bad:
                    gap = f['reconciled']
                    print(f'  {slug} {book or "main"} {quarter}: NOT WRITTEN. {f["accession"]} does not reconcile (rows {gap["row_gap"]:+d}, value {gap["value_gap"]:+,d} against the cover)')
                continue
            if not rows:
                print(f'  {slug} {book or "main"} {quarter}: no holdings rows (' + '; '.join(u for _, u in used) + ')')
                for f, how in used:
                    source_lines.append([quarter, f['accession'], f['form'], f['filed'], f['filer_cik'], how, f['source']])
                continue
            for fix in investor.get('corrections') or []:
                if fix['quarter'] != quarter:
                    continue
                for r in rows:
                    if r['cusip'] == fix['cusip'].upper() and 'issuer' in fix:
                        r['issuer'] = fix['issuer']
                print(f'  {slug} {book or "main"} {quarter}: corrected {fix["cusip"]}: {fix["why"]}')
            multiplier = 1000 if quarter in thousands else 1
            lines, total = aggregate(rows, multiplier)
            totals[quarter] = total
            write_csv(os.path.join(book_out, f'{quarter}.csv'), lines)
            for f, how in used:
                source_lines.append([quarter, f['accession'], f['form'], f['filed'], f['filer_cik'], how, f['source']])
            note = ' (values x1000)' if multiplier > 1 else ''
            print(f'  {slug} {book or "main"} {quarter}: {len(lines)} lines, ${total:,}{note}, from {len(used)} filing(s)')

        for warning in unit_warnings(totals):
            print(f'  WARNING {slug} {book or "main"} {warning}')

        if source_lines:
            os.makedirs(book_out, exist_ok=True)
            with open(os.path.join(book_out, 'sources.csv'), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['quarter', 'accession', 'form', 'filed', 'filer_cik', 'how_used', 'source'])
                writer.writerows(source_lines)
    return ok


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('investor', help='slug from managers.yaml')
    parser.add_argument('--from', dest='first', required=True)
    parser.add_argument('--to', dest='last', required=True)
    parser.add_argument('--cache', help='folder fetch13f.py saved filings into')
    parser.add_argument('--raw-dir', help='folder of saved submission texts to read instead of the cache')
    parser.add_argument('--out', required=True, help='holdings folder to write YYYY-QN.csv files into')
    parser.add_argument('--config')
    args = parser.parse_args()

    investors, _ = edgar.load_investors(args.config)
    if args.investor not in investors:
        sys.exit(f'unknown investor {args.investor}')
    if not (args.cache or args.raw_dir):
        sys.exit('give --cache or --raw-dir')
    print(f'Building {args.investor} {args.first}..{args.last}...')
    ok = build(args.investor, investors[args.investor], args.first, args.last,
               os.path.expanduser(args.cache or ''), os.path.expanduser(args.out), args.raw_dir)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
