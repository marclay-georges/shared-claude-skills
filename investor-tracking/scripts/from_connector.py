"""Save filings fetched through the Beat and Raise connector into the filing cache, untouched.

Where sec.gov is blocked (a sandbox whose proxy allows only listed hosts), the filings still
arrive through the Beat and Raise MCP connector, which runs outside the sandbox. But a connector
is a tool the model calls, so its results land in the session, not on disk. Every tool result
is also written word for word into the session's transcript file, and this script copies them
from there. Nothing passes through the model's own output, so nothing can be mistyped.

What it reads from the transcript:
- get_filings results: each filing's form, filing date, CIK and document list;
- get_document results, called with get_markdown=false: each document's raw XML.

For every accession with both, it writes <cache>/filings/<cik>/<accession>.txt in the same
shape as the SEC's own submission file (a short header, then each XML document), so
build13f.py and nport.py read it exactly as they read a direct download. An accession whose
documents are incomplete is reported and skipped.

Several sessions or helpers may fetch at once, each writing its own transcript, so by default it
reads every transcript written in the last day rather than guessing which one is this session's.
That is safe: a filing never changes, so the same accession found twice gives the same file, and a
filing is written only when its metadata and every one of its XML documents were found.

    python from_connector.py --cache /path/to/cache                    # transcripts from the last 24 hours
    python from_connector.py --cache /path/to/cache --transcript FILE.jsonl [--transcript ...]
"""
import argparse
import glob
import json
import os
import re
import sys
import time


def recent_transcripts(hours):
    """Every session transcript (helpers' included) under ~/.claude/projects written in the last `hours`."""
    cutoff = time.time() - hours * 3600
    candidates = glob.glob(os.path.expanduser('~/.claude/projects/**/*.jsonl'), recursive=True)
    recent = [p for p in candidates if os.path.getmtime(p) >= cutoff]
    if not recent:
        sys.exit(f'no transcript written in the last {hours} hours under ~/.claude/projects; pass --transcript')
    return recent


def result_text(content):
    """A tool result's text, following the harness's pointer when a large result was saved aside."""
    if isinstance(content, list):
        content = ''.join(c.get('text', '') for c in content if isinstance(c, dict))
    if not isinstance(content, str):
        return ''
    saved = re.search(r'(?:saved to|Full output saved to):\s*(\S+)', content)
    if saved and os.path.exists(saved.group(1)):
        with open(saved.group(1), encoding='utf-8', errors='replace') as f:
            content = f.read()
    return content


def unwrap(text):
    """Connector results arrive as {"result": "..."} JSON or as plain text."""
    try:
        data = json.loads(text)
    except ValueError:
        return text
    if isinstance(data, dict) and isinstance(data.get('result'), str):
        return data['result']
    return data


def read_transcript(path):
    """Tool calls and their results, paired by id, for the connector tools this script uses."""
    calls, results = {}, {}
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            try:
                record = json.loads(line)
            except ValueError:
                continue
            message = record.get('message')
            if not isinstance(message, dict) or not isinstance(message.get('content'), list):
                continue
            for block in message['content']:
                if block.get('type') == 'tool_use':
                    name = block.get('name', '')
                    if name.endswith('get_filings') or name.endswith('get_document') or name.endswith('get_filing_detail'):
                        calls[block['id']] = (name, block.get('input') or {})
                elif block.get('type') == 'tool_result' and block.get('tool_use_id') in calls:
                    results[block['tool_use_id']] = result_text(block.get('content'))
    return calls, results


def xml_block(text):
    """One raw document as an <XML> block, without the connector's source comment."""
    text = re.sub(r'^\s*<!--.*?-->\s*', '', text, flags=re.S)
    if '<XML>' not in text:
        text = f'<XML>\n{text}\n</XML>'
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cache', required=True, help='filing cache; files go to <cache>/filings/<cik>/')
    parser.add_argument('--transcript', action='append', help='a session transcript (.jsonl); repeatable. Default: all from the last --hours')
    parser.add_argument('--hours', type=float, default=24, help='how far back to look for transcripts (default 24)')
    args = parser.parse_args()

    transcripts = args.transcript or recent_transcripts(args.hours)
    calls, results = {}, {}
    for transcript in transcripts:
        more_calls, more_results = read_transcript(transcript)
        calls.update(more_calls)
        results.update(more_results)
    print(f'Read {len(transcripts)} transcript(s): {len(results)} connector results')

    ### filing metadata from get_filings and get_filing_detail
    filings = {}
    for call_id, (name, _) in calls.items():
        if call_id not in results or name.endswith('get_document'):
            continue
        data = unwrap(results[call_id])
        if not isinstance(data, dict):
            continue
        for f in data.get('filings', [data] if 'accession_number' in data else []):
            if f.get('accession_number') and f.get('content_object'):
                filings[f['accession_number']] = f

    ### raw documents from get_document
    documents = {}
    for call_id, (name, given) in calls.items():
        if not name.endswith('get_document') or call_id not in results:
            continue
        if given.get('get_markdown', True):
            continue  # markdown is a rendering, not the filing
        text = unwrap(results[call_id])
        if isinstance(text, str) and given.get('accession_number') and given.get('filename'):
            documents.setdefault(given['accession_number'], {})[given['filename']] = text

    written = 0
    for accession, docs in sorted(documents.items()):
        meta = filings.get(accession)
        if not meta:
            print(f'  SKIPPED {accession}: no get_filings or get_filing_detail result names its form and date')
            continue
        wanted = [d['filename'] for d in meta['content_object'] if d['filename'].lower().endswith('.xml')]
        missing = [w for w in wanted if w not in docs]
        if missing:
            print(f'  SKIPPED {accession}: documents not fetched yet: {", ".join(missing)}')
            continue

        body = '\n'.join(xml_block(docs[w]) for w in wanted)
        period = re.search(r'<(?:\w+:)?(?:reportCalendarOrQuarter|periodOfReport)>(\d{2})-(\d{2})-(\d{4})<', body)
        period = f'{period.group(3)}{period.group(1)}{period.group(2)}' if period else ''
        cik = int(meta['cik'])
        header = '\n'.join([
            f'ACCESSION NUMBER: {accession}',
            f'CONFORMED SUBMISSION TYPE: {meta["form"]}',
            f'CONFORMED PERIOD OF REPORT: {period}',
            f'FILED AS OF DATE: {meta["filing_date"][:10].replace("-", "")}',
            f'CENTRAL INDEX KEY: {cik:010d}',
            'SOURCE: beatandraise.com via connector',
        ])
        path = os.path.join(os.path.expanduser(args.cache), 'filings', str(cik), f'{accession}.txt')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(header + '\n' + body)
        written += 1
        print(f'  {meta["form"]:<9} {accession}  cik {cik}  -> {path}')
    print(f'Wrote {written} filing(s).')


if __name__ == '__main__':
    main()
