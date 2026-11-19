"""List every new SEC filing by or about the investors you follow, of any form type.

The 13F is one quarterly snapshot. Between snapshots, an investor's other filings often
say more and say it sooner: a 13D states the purpose of a stake, a Form 4 shows a trade
within two business days, a fund's N-CSR carries the manager's discussion of the year, an
N-PORT shows a fund's holdings and monthly flows. This lists all of them, for each 13F
filer and each related entity in managers.yaml, with a note on what each form can tell you.

For fund trusts that hold many funds, fund-level forms (N-PORT, N-CSR, prospectuses) are
kept only when their header names the investor's series. That costs one small request per
filing the first time and is cached after.

    python watch.py --all --since 2026-08-15 --cache ~/edgar-cache
    python watch.py akre pershing-square --days 30 --cache ~/edgar-cache
"""
import argparse
import datetime
import os
import re
import sys

import edgar

### what each form can tell you, and which kind of evidence it is
FORM_NOTES = [
    ('13F-NT', 'Filed: notice that another filer reports these holdings; follow it'),
    ('13F-HR/A', 'Filed: 13F amendment; new holdings (often confidential positions) or a restatement'),
    ('13F-HR', 'Filed: quarterly long US positions, 45 days after quarter end'),
    ('SCHEDULE 13D', 'Filed + Said: stake over 5% with intent to influence; Item 4 states the purpose'),
    ('SC 13D', 'Filed + Said: stake over 5% with intent to influence; Item 4 states the purpose'),
    ('SCHEDULE 13G', 'Filed: passive stake over 5%'),
    ('SC 13G', 'Filed: passive stake over 5%'),
    ('3', 'Filed: became a 10% owner or insider'),
    ('4', 'Filed: insider or 10%-owner trade, within two business days'),
    ('5', 'Filed: annual catch-up of insider trades'),
    ('N-PX', 'Filed: proxy votes with share counts, which reveal non-US holdings'),
    ('NPORT-P', 'Filed: fund holdings and monthly flows (creations, redemptions)'),
    ('N-CSRS', 'Said + Filed: fund semi-annual report; holdings, sometimes a letter'),
    ('N-CSR', 'Said + Filed: fund annual report; management discussion of performance'),
    ('497', 'Said: fund prospectus or supplement; strategy, manager changes'),
    ('485', 'Said: fund registration update; strategy, manager changes'),
    ('DFAN14A', 'Said: proxy-fight material from a non-management holder; the activist case'),
    ('DEFA14A', 'Said: additional proxy material'),
    ('PX14A6G', 'Said: exempt solicitation; a holder campaigning on a vote'),
    ('D', 'Filed: private fund raising (cumulative amount sold, investor count)'),
    ('10-K', 'Said + Filed: annual report (Berkshire: the shareholder letter and equity table)'),
    ('10-Q', 'Filed: quarterly report (Berkshire: equity cost and value by sector)'),
    ('8-K', 'Filed: material event'),
    ('DEF 14A', 'Said: proxy statement'),
    ('40-APP', 'Filed: application for exemptive relief'),
]
FUND_LEVEL = ('NPORT', 'N-CSR', '497', '485', 'N-1A', 'N-14', '24F', 'N-CEN', 'N-PX')
OWNERSHIP = ('SCHEDULE 13', 'SC 13', '3', '4', '5', '3/A', '4/A', '5/A')


def note_for(form):
    for prefix, note in FORM_NOTES:
        if form == prefix or form.startswith(prefix + '/') or (len(prefix) > 2 and form.startswith(prefix)):
            return note
    return ''


def subject_of(text):
    """The company an ownership filing is about (SUBJECT COMPANY for 13D/G, ISSUER for Forms 3/4/5)."""
    m = re.search(r'<?(?:SUBJECT-COMPANY|ISSUER)>?.*?CONFORMED-NAME>([^\n<]+)', text, flags=re.S) or \
        re.search(r'(?:SUBJECT COMPANY|ISSUER):\s*\n\s*COMPANY DATA:\s*\n\s*COMPANY CONFORMED NAME:\s*([^\n]+)', text)
    return m.group(1).strip() if m else ''


def watch_investor(slug, investor, since, cache, forms, refresh=True):
    entities = [dict(e, role='13F filer') for e in investor['filers_13f']]
    entities += [dict(e, role='related') for e in investor.get('related') or [] if not e.get('ignore')]
    found = {}
    for entity in entities:
        try:
            _, rows = edgar.filings(entity['cik'], cache, since=since, refresh=refresh)
        except edgar.NotCached:
            print(f'  (skipped {entity["label"]}: no saved filing list for CIK {entity["cik"]})')
            continue
        for r in rows:
            form = r['form']
            if forms and not any(form.startswith(f) for f in forms):
                continue
            accession = r['accessionNumber']
            if entity.get('series') and form.startswith(FUND_LEVEL):
                try:
                    series_ids = set(re.findall(r'S0000\d{5}', edgar.header(entity['cik'], accession, cache)))
                except edgar.NotCached:
                    series_ids = {entity['series']}  # can't tell offline; keep it rather than drop it
                if entity['series'] not in series_ids:
                    continue
            ### one line per filing, even when several of the investor's entities are on it
            if accession in found:
                found[accession]['labels'].append(entity['label'])
                continue
            subject = ''
            if form.startswith(OWNERSHIP) and form != '40-APP':
                try:
                    subject = subject_of(edgar.header(entity['cik'], accession, cache))
                except edgar.NotCached:
                    subject = ''
            found[accession] = {'date': r['filingDate'], 'form': form, 'labels': [entity['label']],
                                'subject': subject, 'url': edgar.index_url(entity['cik'], accession),
                                'note': note_for(form)}
    return sorted(found.values(), key=lambda f: f['date'], reverse=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('investors', nargs='*')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--since', help='YYYY-MM-DD; default is --days ago')
    parser.add_argument('--days', type=int, default=100)
    parser.add_argument('--forms', nargs='*', help='only these form prefixes, e.g. 13F SCHEDULE 4')
    parser.add_argument('--cache', required=True)
    parser.add_argument('--offline', action='store_true', help='read only saved filing lists (cache/submissions/CIK##########.json); fetch nothing')
    parser.add_argument('--config')
    args = parser.parse_args()

    investors, _ = edgar.load_investors(args.config)
    slugs = list(investors) if args.all else args.investors
    if not slugs:
        sys.exit('name investors from managers.yaml, or --all')
    since = args.since or (datetime.date.today() - datetime.timedelta(days=args.days)).isoformat()
    cache = os.path.expanduser(args.cache)
    edgar.OFFLINE[0] = args.offline

    for slug in slugs:
        investor = investors[slug]
        print(f'\n## {investor["name"]} ({slug}), filings since {since}')
        if investor.get('status'):
            print(f'Status: {investor["status"]}')
        found = watch_investor(slug, investor, since, cache, args.forms, refresh=not args.offline)
        if not found:
            print('None.')
        for f in found:
            subject = f' on {f["subject"]}' if f['subject'] else ''
            print(f'- {f["date"]} {f["form"]}{subject} | {"; ".join(f["labels"])} | {f["note"]} | {f["url"]}')


if __name__ == '__main__':
    main()
