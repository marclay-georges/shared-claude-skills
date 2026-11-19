"""Read a fund's N-PORT filings: monthly flows and full holdings, including non-US names.

For an investor whose 13F is mostly one public fund (Akre's ETF, Polen's Growth Fund),
the fund's own flows explain most quarter-to-quarter share changes in the 13F. N-PORT gives
them month by month (sales, reinvested distributions, redemptions) along with the fund's
total and net assets, and it lists every holding, including the Canadian, European and
Asian names a 13F never shows. Public N-PORTs appear about 60 days after the fund's
quarter end, and fund quarters often end a month off the calendar quarters.

    python nport.py --investor akre --since 2024-01-01 --cache ~/edgar-cache --out ~/investors/akre/nport
    python nport.py --cik 811030 --series S000089351 --since 2025-10-01 --cache ~/edgar-cache --out out/

Writes flows.csv (one row per month) and holdings/<period end>.csv (one per filing).
"""
import argparse
import csv
import os
import re
import sys
import xml.etree.ElementTree as ET

import edgar
from parse13f import _strip_namespaces, _text


def parse_nport(text):
    """Flows, assets and holdings from one N-PORT submission."""
    block = re.search(r'<XML>(.*?)</XML>', text, flags=re.S | re.I)
    if not block:
        return None
    root = _strip_namespaces(ET.fromstring(block.group(1).strip()))
    form = root.find('formData')
    gen, fund = form.find('genInfo'), form.find('fundInfo')

    record = {
        'series_id': _text(gen, 'seriesId'),
        'series_name': _text(gen, 'seriesName'),
        'period_end': _text(gen, 'repPdDate'),
        'fiscal_year_end': _text(gen, 'repPdEnd'),
        'total_assets': float(_text(fund, 'totAssets', '0') or 0),
        'net_assets': float(_text(fund, 'netAssets', '0') or 0),
        'flows': [],
        'holdings': [],
    }

    ### three months of flows, oldest first; amounts are attributes on mon1Flow..mon3Flow
    for i in (1, 2, 3):
        flow = fund.find(f'mon{i}Flow')
        if flow is None:
            continue
        sales = float(flow.get('sales', 0) or 0)
        reinvest = float(flow.get('reinvestment', 0) or 0)
        redemptions = float(flow.get('redemption', 0) or 0)
        record['flows'].append({'month_of_quarter': i, 'sales': sales, 'reinvestment': reinvest,
                                'redemptions': redemptions, 'net': sales + reinvest - redemptions})

    for sec in form.iter('invstOrSec'):
        isin = sec.find('identifiers/isin')
        ticker = sec.find('identifiers/ticker')
        record['holdings'].append({
            'name': _text(sec, 'name', ''),
            'title': _text(sec, 'title', ''),
            'cusip': _text(sec, 'cusip', ''),
            'isin': isin.get('value') if isin is not None else '',
            'ticker': ticker.get('value') if ticker is not None else '',
            'balance': _text(sec, 'balance', ''),
            'units': _text(sec, 'units', ''),
            'currency': _text(sec, 'curCd', ''),
            'value_usd': _text(sec, 'valUSD', ''),
            'pct_of_net_assets': _text(sec, 'pctVal', ''),
            'asset_category': _text(sec, 'assetCat', ''),
            'country': _text(sec, 'invCountry', ''),
        })
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--investor', help='slug; uses its related entities that carry a series id')
    parser.add_argument('--cik')
    parser.add_argument('--series')
    parser.add_argument('--since', required=True, help='filing date, YYYY-MM-DD')
    parser.add_argument('--cache', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--config')
    args = parser.parse_args()

    if args.investor:
        investors, _ = edgar.load_investors(args.config)
        funds = [(e['cik'], e.get('series')) for e in investors[args.investor].get('related') or [] if e.get('series') or e.get('nport')]
    elif args.cik:
        funds = [(args.cik, args.series)]  # no series: a single-fund filer such as a closed-end fund
    else:
        sys.exit('give --investor, or --cik (with --series for a trust that files for many funds)')
    if not funds:
        sys.exit('no fund series recorded for this investor in managers.yaml')

    cache, out = os.path.expanduser(args.cache), os.path.expanduser(args.out)
    flow_rows = []
    for cik, series in funds:
        print(f'Reading N-PORT filings for {cik} {series or "(single fund)"}...')
        _, rows = edgar.filings(cik, cache, since=args.since)
        for r in sorted(rows, key=lambda r: r['filingDate']):
            if not r['form'].startswith('NPORT-P'):
                continue
            ### a trust files one N-PORT per fund; the small header says which fund
            try:
                if series and series not in edgar.header(cik, r['accessionNumber'], cache):
                    continue
                text = edgar.submission_text(cik, r['accessionNumber'], cache)
            except Exception as e:
                print(f'  SKIPPED {r["accessionNumber"]} ({r["filingDate"]}): could not download ({e}); rerun later')
                continue
            record = parse_nport(text)
            if record is None or (series and record['series_id'] != series):
                continue
            period = record['period_end']
            print(f'  {period} {r["form"]} {r["accessionNumber"]}: net assets ${record["net_assets"]:,.0f}, {len(record["holdings"])} holdings')

            ### holdings file per period end
            path = os.path.join(out, 'holdings', f'{period}.csv')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=list(record['holdings'][0].keys()) if record['holdings'] else ['name'])
                writer.writeheader()
                writer.writerows(record['holdings'])

            for flow in record['flows']:
                flow_rows.append({'series': series or record['series_id'] or '', 'period_end': period, 'accession': r['accessionNumber'],
                                  'form': r['form'], 'net_assets_at_period_end': record['net_assets'], **flow})

    if flow_rows:
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'flows.csv'), 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(flow_rows[0].keys()))
            writer.writeheader()
            writer.writerows(flow_rows)
        print(f'Wrote {len(flow_rows)} monthly flow rows to {os.path.join(out, "flows.csv")}')


if __name__ == '__main__':
    main()
