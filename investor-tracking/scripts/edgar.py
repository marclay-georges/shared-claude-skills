"""Shared EDGAR access: a polite, cached HTTP client and the filing list for a CIK.

The SEC asks every automated client to name itself in the User-Agent header (a name and a
contact email) and to stay under 10 requests a second. There is no API key. Each person
running these scripts supplies their own, never inside the shared skill: see user_agent().

Filings never change once accepted, so they are cached on disk forever. The submissions
list does change, so it is refetched unless the caller asks for the cached copy.
"""
import gzip
import json
import os
import sys
import time
import urllib.error
import urllib.request

SECONDS_BETWEEN_REQUESTS = 0.15
_last_request_at = [0.0]

# set by scripts run with --offline: read only what is cached, never touch the network
OFFLINE = [False]


class NotCached(Exception):
    """Raised in offline mode when something was never saved to the cache."""


# where load_investors() found managers.yaml; a user-agent file can sit beside it
CONFIG_DIR = [None]
USER_AGENT_FILE = 'sec_user_agent.txt'


def _user_agent_candidates():
    """Places the contact line can live, outside the shared skill, in the order they are tried."""
    paths = []
    if os.environ.get('SEC_USER_AGENT_FILE'):
        paths.append(os.path.expanduser(os.environ['SEC_USER_AGENT_FILE']))
    if CONFIG_DIR[0]:
        paths.append(os.path.join(CONFIG_DIR[0], USER_AGENT_FILE))
    paths.append(os.path.expanduser(os.path.join('~', '.config', 'investor-tracking', USER_AGENT_FILE)))
    return paths


def user_agent():
    """The SEC contact line: a name and an email, set by whoever runs the scripts.

    Read from the SEC_USER_AGENT environment variable, or from a one-line file: the path in
    SEC_USER_AGENT_FILE, sec_user_agent.txt beside the managers.yaml in use (the working copy,
    not the shared skill), or ~/.config/investor-tracking/sec_user_agent.txt.
    """
    ua = os.environ.get('SEC_USER_AGENT', '').strip()
    if '@' in ua:
        return ua
    for path in _user_agent_candidates():
        if os.path.exists(path):
            with open(path) as f:
                ua = f.read().strip()
            if '@' in ua:
                return ua
    places = '; '.join(_user_agent_candidates())
    sys.exit(f'No SEC contact found. The SEC asks every automated client for a name and email (there is no API key). Set SEC_USER_AGENT="Jane Doe jane@example.com", or put that one line in a file at one of: {places}')


def get(url, cache_path=None, refresh=False):
    """Fetch a URL politely; read from and write to cache_path when one is given."""
    if cache_path and os.path.exists(cache_path) and not refresh:
        with open(cache_path, 'rb') as f:
            return f.read()
    if OFFLINE[0]:
        raise NotCached(f'offline and not cached: {url}')

    headers = {'User-Agent': user_agent(), 'Accept-Encoding': 'gzip'}
    for attempt in range(4):
        ### stay under the SEC's rate limit
        wait = SECONDS_BETWEEN_REQUESTS - (time.time() - _last_request_at[0])
        if wait > 0:
            time.sleep(wait)
        _last_request_at[0] = time.time()

        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
                if response.headers.get('Content-Encoding') == 'gzip':
                    body = gzip.decompress(body)
            break
        except urllib.error.HTTPError as e:
            # 429 is the SEC asking us to slow down; 5xx gateway errors are usually brief
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt * 5)
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < 3:
                time.sleep(2 ** attempt * 5)
                continue
            raise

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, 'wb') as f:
            f.write(body)
    return body


def load_investors(path=None):
    """The investors table and corporate actions from managers.yaml (next to this file by default)."""
    import yaml  # the one dependency outside the standard library
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'managers.yaml')
    CONFIG_DIR[0] = os.path.dirname(os.path.abspath(path))
    with open(path) as f:
        config = yaml.safe_load(f)
    return config['investors'], config.get('corporate_actions', [])


def quarter_label(period):
    """'2026-09-30' -> '2026-Q3'."""
    return f'{period[:4]}-Q{(int(period[5:7]) - 1) // 3 + 1}'


def quarter_end(label):
    """'2026-Q3' -> '2026-09-30'."""
    year, q = label.split('-Q')
    return {'1': f'{year}-03-31', '2': f'{year}-06-30', '3': f'{year}-09-30', '4': f'{year}-12-31'}[q]


def cik10(cik):
    return f'{int(cik):010d}'


def _columns_to_rows(block):
    """The submissions JSON stores filings column-wise; turn it into one dict per filing."""
    keys = list(block.keys())
    rows = []
    for i in range(len(block['accessionNumber'])):
        rows.append({k: block[k][i] for k in keys})
    return rows


def filings(cik, cache_dir, since=None, refresh=True):
    """Every filing EDGAR lists for a CIK, newest first: (entity name, list of filing dicts).

    The main JSON holds only the most recent ~1,000 filings. Older ones sit in extra
    files, which are read only when `since` reaches back into them.
    """
    url = f'https://data.sec.gov/submissions/CIK{cik10(cik)}.json'
    cache_path = os.path.join(cache_dir, 'submissions', f'CIK{cik10(cik)}.json')
    data = json.loads(get(url, cache_path, refresh=refresh))
    rows = _columns_to_rows(data['filings']['recent'])

    for extra in data['filings'].get('files', []):
        if since and extra.get('filingTo', '9999') < since:
            continue
        extra_url = f'https://data.sec.gov/submissions/{extra["name"]}'
        extra_cache = os.path.join(cache_dir, 'submissions', extra['name'])
        older = json.loads(get(extra_url, extra_cache, refresh=refresh))
        rows += _columns_to_rows(older)

    if since:
        rows = [r for r in rows if r['filingDate'] >= since]
    rows.sort(key=lambda r: r['filingDate'], reverse=True)
    return data.get('name', ''), rows


def submission_url(cik, accession):
    folder = accession.replace('-', '')
    return f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{folder}/{accession}.txt'


def index_url(cik, accession):
    folder = accession.replace('-', '')
    return f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{folder}/'


def submission_text(cik, accession, cache_dir):
    """The full submission (.txt): SGML header plus every document, cached for good."""
    cache_path = os.path.join(cache_dir, 'filings', str(int(cik)), f'{accession}.txt')
    body = get(submission_url(cik, accession), cache_path)
    return body.decode('utf-8', errors='replace')


def header(cik, accession, cache_dir):
    """A filing's SGML header: small, and it names the series and the subject company."""
    folder = accession.replace('-', '')
    url = f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{folder}/{accession}.hdr.sgml'
    cache_path = os.path.join(cache_dir, 'headers', str(int(cik)), f'{accession}.hdr.sgml')
    return get(url, cache_path).decode('utf-8', errors='replace')
