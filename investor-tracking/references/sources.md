# Where to find each source

Reached for when building a baseline or chasing a specific document. Everything on EDGAR is free;
the SEC asks automated clients to send a User-Agent naming the requester with a contact email
(see `SKILL.md` for where the scripts read it from).

## EDGAR

- **Filing list for any CIK** (every form, newest first, reliable):
  `https://data.sec.gov/submissions/CIK##########.json` (CIK padded to ten digits). The main file
  holds about the last thousand filings; older ones are in the extra files it lists under
  `filings.files`. The EDGAR browse pages and some archive folder listings have been stale; this
  JSON has not.
- **A filing's folder**: `https://www.sec.gov/Archives/edgar/data/<cik>/<accession without dashes>/`
- **The full submission** (SGML header plus every document, the input `parse13f.py` reads):
  `https://www.sec.gov/Archives/edgar/data/<cik>/<accession without dashes>/<accession>.txt`
- **Just the header** (names fund series and the subject company of a 13D/G or Form 4):
  the same path with `.hdr.sgml`.
- **Full-text search** across filing text: `https://efts.sec.gov/LATEST/search-index?q="phrase"`,
  narrowed with `&forms=N-CSR` or `&ciks=0001112520` (both checked 2026-11-19; it returns JSON). The
  browsable version is the "Full-Text Search" page on sec.gov. Useful for finding which funds
  mention a name, or a manager's 13D purpose language.
- **Accession prefixes are not a guide to the filer.** Many investors file through agents whose
  CIK becomes the accession prefix, and the agent can change from year to year. Find filings by the
  investor's CIK, never by guessing an accession number.

## Off EDGAR

- **Form ADV** (assets, clients, fees, strategy brochure): `https://adviserinfo.sec.gov/firm/summary/<CRD>`;
  the brochure (Part 2A) is the strategy in the adviser's words. The CRD number is in each profile.
- **ETF daily holdings**: the manager's or fund's own site (Akre: akrefund.com).
- **UK notices** (Pershing Square Holdings, Fundsmith's UK funds): the London Stock Exchange's
  regulatory news service and the companies' own investor pages. **Dutch, French and other
  European holdings notices** (TCI's stakes): the national regulators' disclosure registers, e.g.
  the AFM register for the Netherlands.
- **Letters, meetings and interviews**: the manager's site first, then reposts (Seeking Alpha,
  hedge-fund letter aggregators, podcasts with transcripts). Where only a paywalled summary exists,
  record it as second-hand Said, with the source.

## When sec.gov is blocked

Report it rather than working around it. A web-reading tool pointed at a filing's `.txt` URL returns
the submission with its tags stripped, and `build13f.py --raw-dir` can build from saved copies, but a
web reader may serve a cached or partial page, so holdings built that way are unverified. Use them
only when the user asks, and label them as such.
