"""Parse a 13F submission into one record: cover facts plus information-table rows.

Input is the full submission text (`<accession>.txt` from the EDGAR archive). It comes in
two shapes and both give the same record:

- the real thing, fetched from sec.gov, where the cover and the information table are XML
  documents inside the SGML wrapper;
- a tag-stripped copy, which is what a web-reading tool returns for the same URL: the XML
  tags are gone and every value sits on its own line. Such copies may be cached or partial, so
  holdings built from them are unverified; this path exists for checking, not for routine use.

The stripped parser leans on the information table's fixed column order (issuer, class,
CUSIP, optional FIGI, value, amount, SH/PRN, optional put/call, discretion, ...). Every
record carries its own reconciliation against the cover page, so a parsing slip shows up
as a mismatch rather than as a quietly wrong number.

    python parse13f.py FILE.txt [FILE.txt ...] [--json OUT.json]
"""
import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET

REPORT_TYPES = ('13F HOLDINGS REPORT', '13F NOTICE', '13F COMBINATION REPORT')
CUSIP_RE = re.compile(r'[0-9A-Za-z]{9}')
FIGI_RE = re.compile(r'BBG[0-9A-Za-z]{9}', re.I)
INT_RE = re.compile(r'\d+')
DATE_RE = re.compile(r'\d{2}-\d{2}-\d{4}')


def _header_field(text, label):
    m = re.search(label + r':\s*(\S+)', text)
    return m.group(1) if m else None


def _strip_namespaces(root):
    for el in root.iter():
        if isinstance(el.tag, str) and '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    return root


def _text(el, path, default=None):
    found = el.find(path)
    if found is None or found.text is None:
        return default
    return found.text.strip()


def _to_int(s):
    return int(round(float(s.replace(',', ''))))


def _xml_blocks(text):
    """Every XML document embedded in the submission, parsed, namespaces removed."""
    docs = []
    for block in re.findall(r'<XML>(.*?)</XML>', text, flags=re.S | re.I):
        try:
            docs.append(_strip_namespaces(ET.fromstring(block.strip())))
        except ET.ParseError:
            continue
    return docs


def _base_record(text):
    form = _header_field(text, 'CONFORMED SUBMISSION TYPE')
    period = _header_field(text, 'CONFORMED PERIOD OF REPORT')
    filed = _header_field(text, 'FILED AS OF DATE')
    return {
        'accession': _header_field(text, 'ACCESSION NUMBER'),
        'filer_cik': _header_field(text, 'CENTRAL INDEX KEY'),
        'filer_name': (re.search(r'COMPANY CONFORMED NAME:\s*(.+)', text) or [None, None])[1],
        'form': form,
        'period': f'{period[:4]}-{period[4:6]}-{period[6:]}' if period else None,
        'filed': f'{filed[:4]}-{filed[4:6]}-{filed[6:]}' if filed else None,
        'source': (re.search(r'^SOURCE:\s*(.+)$', text, flags=re.M) or [None, 'sec.gov'])[1].strip(),
    }


def parse_xml(text):
    record = _base_record(text)
    docs = _xml_blocks(text)
    cover = next((d for d in docs if d.tag == 'edgarSubmission'), None)
    table = next((d for d in docs if d.tag == 'informationTable'), None)
    if cover is None:
        return None

    cover_page = cover.find('formData/coverPage')
    summary = cover.find('formData/summaryPage')
    record['report_type'] = _text(cover_page, 'reportType')
    record['is_amendment'] = _text(cover_page, 'isAmendment', 'false').lower() == 'true'
    record['amendment_type'] = _text(cover_page, 'amendmentInfo/amendmentType')
    record['amendment_no'] = _text(cover_page, 'amendmentNo')
    record['manager_name'] = _text(cover_page, 'filingManager/name')

    ### who else is in this filing, or (for a notice) who files for this manager
    included = []
    if summary is not None:
        for m in summary.iter('otherManager'):
            name = _text(m, 'name')
            if name:
                included.append({'name': name, 'cik': _text(m, 'cik'), 'file_no': _text(m, 'form13FFileNumber')})
    reporting_for_us = []
    for m in cover_page.iter('otherManager'):
        name = _text(m, 'name')
        if name:
            reporting_for_us.append({'name': name, 'cik': _text(m, 'cik'), 'file_no': _text(m, 'form13FFileNumber')})
    record['other_included_managers'] = included
    record['other_managers_reporting'] = reporting_for_us

    record['entries'] = int(_text(summary, 'tableEntryTotal', '0')) if summary is not None else 0
    record['total'] = _to_int(_text(summary, 'tableValueTotal', '0')) if summary is not None else 0
    record['confidential_omitted'] = (_text(summary, 'isConfidentialOmitted', 'false') or 'false').lower() == 'true' if summary is not None else False

    rows = []
    if table is not None:
        for it in table.findall('infoTable'):
            rows.append({
                'issuer': _text(it, 'nameOfIssuer', ''),
                'class': _text(it, 'titleOfClass', ''),
                'cusip': _text(it, 'cusip', '').upper(),
                'value': _to_int(_text(it, 'value', '0')),
                'shares': _to_int(_text(it, 'shrsOrPrnAmt/sshPrnamt', '0')),
                'sh_prn': _text(it, 'shrsOrPrnAmt/sshPrnamtType', ''),
                'put_call': (_text(it, 'putCall', '') or '').capitalize(),
                'discretion': _text(it, 'investmentDiscretion', ''),
                'other_manager': _text(it, 'otherManager', ''),
            })
    record['rows'] = rows
    record['format'] = 'xml'
    return record


def parse_stripped(text):
    """Parse a copy whose XML tags were stripped, leaving one value per line."""
    record = _base_record(text)
    tokens = [t.strip() for t in text.split('\n') if t.strip()]

    ### cover: report type, amendment type, then after the signature date the summary's
    ### other-manager count, entry total and value total (and, when present, true/false
    ### for confidential omission)
    type_at = next((i for i, t in enumerate(tokens) if t in REPORT_TYPES), None)
    if type_at is None:
        return None
    record['report_type'] = tokens[type_at]
    record['amendment_type'] = next((t for t in tokens[:type_at + 40] if t in ('RESTATEMENT', 'NEW HOLDINGS')), None)
    record['is_amendment'] = record['form'].endswith('/A') if record['form'] else False
    record['amendment_no'] = None
    record['manager_name'] = None
    record['other_included_managers'] = []
    record['other_managers_reporting'] = []

    record['entries'] = 0
    record['total'] = 0
    record['confidential_omitted'] = False
    summary_end = type_at
    for k in range(type_at, len(tokens) - 3):
        if not DATE_RE.fullmatch(tokens[k]):
            continue
        window = tokens[k + 1:k + 4]
        if all(INT_RE.fullmatch(t) for t in window):
            record['entries'] = int(window[1])
            record['total'] = int(window[2])
            summary_end = k + 4
            if summary_end < len(tokens) and tokens[summary_end] in ('true', 'false'):
                record['confidential_omitted'] = tokens[summary_end] == 'true'
                summary_end += 1
            break

    ### information table: anchor on each CUSIP followed by value, amount and SH/PRN
    rows = []
    body = tokens[summary_end:]
    for k, t in enumerate(body):
        if k < 2 or not CUSIP_RE.fullmatch(t):
            continue
        j = k + 1
        if j < len(body) and FIGI_RE.fullmatch(body[j]):
            j += 1
        if j + 2 >= len(body):
            continue
        value, amount, sh_prn = body[j], body[j + 1], body[j + 2]
        if not (INT_RE.fullmatch(value.replace(',', '')) and INT_RE.fullmatch(amount.replace(',', '')) and sh_prn in ('SH', 'PRN')):
            continue
        after = body[j + 3] if j + 3 < len(body) else ''
        put_call = after.capitalize() if after.upper() in ('PUT', 'CALL') else ''
        discretion = body[j + 4] if put_call and j + 4 < len(body) else after
        rows.append({
            'issuer': body[k - 2],
            'class': body[k - 1],
            'cusip': t.upper(),
            'value': _to_int(value),
            'shares': _to_int(amount),
            'sh_prn': sh_prn,
            'put_call': put_call,
            'discretion': discretion,
            'other_manager': '',
        })
    record['rows'] = rows
    record['format'] = 'stripped'
    return record


def parse_submission(text):
    record = parse_xml(text) if re.search(r'<XML>', text, flags=re.I) else None
    if record is None:
        record = parse_stripped(text)
    if record is None:
        raise ValueError('not a 13F submission this parser understands')

    ### an option row whose put/call field was left blank but whose class says PUT or CALL
    for r in record['rows']:
        r['issuer'] = ' '.join(html.unescape(r['issuer']).split())
        r['class'] = ' '.join(html.unescape(r['class']).split())
        if not r['put_call'] and r['class'].strip().upper() in ('PUT', 'CALL'):
            r['put_call'] = r['class'].strip().capitalize()

    record['reconciled'] = reconcile(record)
    return record


def reconcile(record):
    """Do the rows add up to the cover page? A notice has no rows and nothing to check.

    Each row's value is rounded to the dollar and so is the cover total, so a sum can miss
    the total by up to half a dollar per row; anything beyond that is a real gap.
    """
    if record['report_type'] == '13F NOTICE':
        return {'ok': True, 'row_gap': 0, 'value_gap': 0}
    row_gap = len(record['rows']) - record['entries']
    value_gap = sum(r['value'] for r in record['rows']) - record['total']
    rounding = len(record['rows']) // 2 + 1
    return {'ok': row_gap == 0 and abs(value_gap) <= rounding, 'row_gap': row_gap, 'value_gap': value_gap}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='+')
    parser.add_argument('--json', help='write all parsed records to this file')
    args = parser.parse_args()

    records = []
    for path in args.files:
        with open(path, encoding='utf-8', errors='replace') as f:
            record = parse_submission(f.read())
        records.append(record)
        rec = record['reconciled']
        status = 'OK' if rec['ok'] else f'MISMATCH rows {rec["row_gap"]:+d} value {rec["value_gap"]:+,d}'
        print(f'{record["accession"]}  {record["form"]:<9} {record["period"]}  {record["format"]:<8} {record["report_type"]:<22} {record["amendment_type"] or "":<12} rows {len(record["rows"]):>4}/{record["entries"]:<4} {status}')

    if args.json:
        with open(args.json, 'w') as f:
            json.dump(records, f, indent=1)
    return 0 if all(r['reconciled']['ok'] for r in records) else 1


if __name__ == '__main__':
    sys.exit(main())
