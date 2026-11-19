"""Set up a working copy of the investor baselines from the snapshot bundled with the skill.

The skill ships each investor's holdings as one combined file, `holdings.csv`, with `book` and
`quarter` columns (a skill can hold at most 200 files, and one file per quarter would exceed
that). The scripts work on one file per quarter, so this unpacks the snapshot into the layout
they expect:

    <work>/managers.yaml
    <work>/investors/<slug>/profile.md, log.md
    <work>/investors/<slug>/holdings/YYYY-QN.csv and sources.csv
    <work>/investors/<slug>/holdings/<book>/...        (a second filer kept apart, e.g. fisl)

It never overwrites a file that already exists in the working copy, since that copy is where
reviewed updates live; it lists what it skipped instead.

    python seed_baseline.py --to /path/to/working/folder
"""
import argparse
import csv
import os
import shutil

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(SKILL, 'references', 'baseline')
HOLDINGS_COLUMNS = ['issuer', 'cusip', 'class', 'shares', 'value_usd', 'put_call', 'pct_of_portfolio']


def write_new(path, write, skipped):
    """Create a file only if it doesn't exist yet."""
    if os.path.exists(path):
        skipped.append(path)
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write(path)


def split_csv(source, folder, filename_for, columns, skipped):
    """Write one file per (book, key) group from a combined CSV."""
    groups = {}
    with open(source, newline='') as f:
        for row in csv.DictReader(f):
            book = row.get('book') or ''
            groups.setdefault((book, filename_for(row)), []).append(row)
    for (book, name), rows in groups.items():
        path = os.path.join(folder, book, name) if book else os.path.join(folder, name)

        def write(p, rows=rows):
            with open(p, 'w', newline='') as out:
                writer = csv.DictWriter(out, fieldnames=columns, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(rows)
        write_new(path, write, skipped)
    return len(groups)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--to', required=True, help='working folder to create or fill')
    args = parser.parse_args()
    work = os.path.expanduser(args.to)
    skipped = []

    write_new(os.path.join(work, 'managers.yaml'),
              lambda p: shutil.copy(os.path.join(SKILL, 'scripts', 'managers.yaml'), p), skipped)

    for slug in sorted(os.listdir(BASELINE)):
        src = os.path.join(BASELINE, slug)
        if not os.path.isdir(src):
            continue
        dst = os.path.join(work, 'investors', slug)
        for name in ('profile.md', 'log.md'):
            if os.path.exists(os.path.join(src, name)):
                write_new(os.path.join(dst, name), lambda p, n=name: shutil.copy(os.path.join(src, n), p), skipped)

        quarters = 0
        if os.path.exists(os.path.join(src, 'holdings.csv')):
            quarters = split_csv(os.path.join(src, 'holdings.csv'), os.path.join(dst, 'holdings'),
                                 lambda r: f'{r["quarter"]}.csv', HOLDINGS_COLUMNS, skipped)
        if os.path.exists(os.path.join(src, 'sources.csv')):
            with open(os.path.join(src, 'sources.csv'), newline='') as f:
                source_columns = [c for c in csv.DictReader(f).fieldnames if c != 'book']
            split_csv(os.path.join(src, 'sources.csv'), os.path.join(dst, 'holdings'),
                      lambda r: 'sources.csv', source_columns, skipped)
        print(f'  {slug}: {quarters} quarter file(s)')

    if skipped:
        print(f'Left {len(skipped)} existing file(s) untouched, e.g. {skipped[0]}')
    print(f'Working copy ready at {work}')


if __name__ == '__main__':
    main()
