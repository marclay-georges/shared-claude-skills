"""Download every 13F submission (originals, amendments, notices) for investors and quarters.

Reads each 13F filer CIK from managers.yaml, finds its 13F filings in the SEC submissions
list, and saves each full submission to <cache>/filings/<cik>/<accession>.txt. Nothing is
parsed here; build13f.py does that. Already-downloaded filings are not fetched again.

If sec.gov can't be reached from where you are running, this stops with the error. Report it;
don't substitute copies from a web-reading tool, which may be cached or partial.

    python fetch13f.py akre berkshire-hathaway --from 2023-Q4 --to 2026-Q3 --cache ~/edgar-cache
    python fetch13f.py --all --from 2026-Q3 --to 2026-Q3 --cache ~/edgar-cache
"""
import argparse
import os
import sys

import edgar


def fetch_investor(slug, investor, first, last, cache, refresh=True):
    start, end = edgar.quarter_end(first), edgar.quarter_end(last)
    found = []
    for filer in investor['filers_13f']:
        name, rows = edgar.filings(filer['cik'], cache, since=start, refresh=refresh)
        for r in rows:
            if not r['form'].startswith('13F'):
                continue
            # reportDate is the period of report; fall back to filing date if blank
            period = r.get('reportDate') or ''
            if not (start <= period <= end):
                continue
            print(f'  {slug:<20} {filer["cik"]:>8} {r["form"]:<9} {period}  filed {r["filingDate"]}  {r["accessionNumber"]}')
            edgar.submission_text(filer['cik'], r['accessionNumber'], cache)
            found.append(r)
    if not found:
        print(f'  {slug:<20} no 13F filings for {first}..{last}')
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('investors', nargs='*', help='slugs from managers.yaml')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--from', dest='first', required=True, help='first quarter, e.g. 2023-Q4')
    parser.add_argument('--to', dest='last', required=True, help='last quarter, e.g. 2026-Q3')
    parser.add_argument('--cache', required=True, help='folder for downloaded filings')
    parser.add_argument('--config', help='managers.yaml path (default: next to this script)')
    args = parser.parse_args()

    investors, _ = edgar.load_investors(args.config)
    slugs = list(investors) if args.all else args.investors
    unknown = [s for s in slugs if s not in investors]
    if not slugs or unknown:
        sys.exit(f'name investors from managers.yaml (unknown: {unknown})' if unknown else 'name at least one investor, or --all')

    cache = os.path.expanduser(args.cache)
    for slug in slugs:
        print(f'Fetching 13F filings for {slug}...')
        fetch_investor(slug, investors[slug], args.first, args.last, cache)


if __name__ == '__main__':
    main()
