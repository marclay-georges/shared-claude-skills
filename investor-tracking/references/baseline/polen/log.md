# Polen Capital Management — research log

CIK 0001034524. Covers 13F-HR filings for Q4 2023 to Q3 2026. Written 2026-11-19.

## Oddities a future reader should know first

- **Q4 2023 has wrong values in the filing itself.** Several runs of consecutive rows repeat the value of the row that follows them. Wrongly valued: Eli Lilly, Goosehead, Helen of Troy, Illumina, iShares MSCI ACWI, Karooooo; Hamilton Lane, Houlihan Lokey, two iShares rows, Las Vegas Sands, MarketAxess; Globant, HDFC Bank, two iShares rows, LGI Homes. ICON is also wrong ($5.3M for about 1.19M shares). Share counts look right. The rows still sum exactly to the cover total, so the CSV keeps the filed values. Neither amendment fixed this. Estimated understatement is $0.7–0.8B; details are in `profile.md`. Do not compare Q4 2023 values for these names with Q1 2024.
- **Q4 2023 was filed three times.** The original (2024-02-13) labelled the Forum Energy convertible-note row as "FLOOR & DECOR". Amendment 1 (2024-02-20) has the same total. Amendment 2 (2024-05-10) corrects the label and is the version used.
- **Q3 2024 was amended** (2025-02). The total moved by +$269,142, which is immaterial. The amendment is the version used.
- **Units: every quarter is in whole dollars.** I checked this after the coordinator's correction that some filers report in thousands. Each quarter's summed rows equal its cover total exactly. The series runs smoothly from $41.5B to $9.2B, and single positions are in the billions (Amazon $5.5B in Q4 2023), which is impossible in thousands for a firm this size. No scaling was applied.
- **Q2 2025: the row count doubled,** from 117 to 240. This is the Cupps 5Perspectives team joining on June 30, 2025, not a change in Focus Growth.
- **Q4 2025: the only option rows.** Three PUTs (Bloom Energy, BWX Technologies, SoFi), each next to a long position. Kept as separate rows keyed by CUSIP plus put/call.
- **PRN rows** appear only in Q4 2023 and Q1 2024: Forum Energy Technologies 9% notes, CUSIP 34984VAC4, reported as principal amount. They are credit-side.
- **Splits inside the window:** ServiceNow (5-for-1, visible in Q4 2025) and Netflix (10-for-1, November 2025). In Q2 2026 the iShares Russell 1000 Growth and Vanguard Growth ETF per-share values change in a way that suggests splits; I did not verify this.
- **The 13F cannot show some Focus Growth trades.** Focus Growth's Q3 2026 purchase of Adyen (Amsterdam-listed) has no row.

## Reading order

The holdings were parsed first, then the letters were gathered. The method calls for a chronological read, so before writing the profile I went back through everything oldest-first: each quarter's commentary set against that quarter's 13F, with the ADV, fund reports and press slotted in by date. The arc in `profile.md` is written from that pass.

## 13F-HR filings read

Each holdings table is at `https://www.sec.gov/Archives/edgar/data/1034524/<accession without dashes>/infotable.xml`, read via Exa.

| Quarter | Accession | Filed | Rows | Cover total ($) | Reconciled |
|---|---|---|---|---|---|
| Q4 2023 (original) | 0001172661-24-000776 | 2024-02-13 | — | 41,488,412,793 | superseded |
| Q4 2023 (amendment 1) | 0001172661-24-001616 | 2024-02-20 | — | 41,488,412,793 | superseded |
| **Q4 2023 (amendment 2, used)** | 0001172661-24-002148 | 2024-05-10 | 107 | 41,490,887,814 | yes, exact |
| Q1 2024 | 0001172661-24-002149 | 2024-05 | 104 | 43,317,845,975 | yes, exact |
| Q2 2024 | 0001172661-24-003233 | 2024-08 | 110 | 39,855,562,577 | yes, exact |
| Q3 2024 (original) | 0001172661-24-004624 | 2024-11 | — | 38,739,331,264 | superseded |
| **Q3 2024 (amendment, used)** | 0001172661-25-000622 | 2025-02 | 118 | 38,739,600,406 | yes, exact |
| Q4 2024 | 0001172661-25-000623 | 2025-02 | 124 | 37,010,355,943 | yes, exact |
| Q1 2025 | 0001172661-25-001713 | 2025-05 | 117 | 31,845,099,652 | yes, exact |
| Q2 2025 | 0001172661-25-003133 | 2025-08 | 240 | 32,586,427,255 | yes, exact |
| Q3 2025 | 0001172661-25-004691 | 2025-11 | 232 | 30,802,400,951 | yes, exact |
| Q4 2025 | 0001172661-26-000654 | 2026-02 | 234 | 23,420,875,210 | yes, exact |
| Q1 2026 | 0001172661-26-001911 | 2026-05 | 221 | 14,456,164,077 | yes, exact |
| Q2 2026 | 0001172661-26-003035 | 2026-08 | 219 | 11,610,786,601 | yes, exact |
| Q3 2026 | 0001172661-26-005017 | 2026-11 | 256 | 9,210,349,857 | yes, exact |

"Reconciled" means two checks against the cover page: the row count matches the cover's entry total, and the summed values match the cover's value total. Rows were then aggregated by CUSIP plus put/call to build the CSVs.

Cover-page facts, the same in every quarter: other included managers 0; file number 028-03687; no confidential-treatment request seen. The signer changed over time:
- Brian D. Goldberg (CCO);
- Lauren Walsh (CCO, from the May 2024 filings);
- Goldberg (General Counsel and CCO, February 2026);
- Richard J. Simek (CCO, Q3 2026).

## Other SEC filings

| Type | Accession / location | Date | What it is |
|---|---|---|---|
| SC 13G/A | 0001172661-24-000261 | 2024-01-18 | Forum Energy Technologies, credit-side |
| SC 13G | 0001829126-24-000915 | 2024-02-13 | Polen Credit Opportunities Fund filing |
| 40-APP/A | 0001829126-24-001488 | 2024-03-08 | Co-investment exemptive relief with Polen Capital Credit (CIK 1010422) |
| N-PX | 0001172661-24-003684 | 2024-08-23 | Proxy votes. Located, content not analysed |
| SC 13G | 0001172661-24-004486 | 2024-11-06 | Paycom, 3,485,664 shares, 6.1%, event date 9/30/2024 |
| SCHEDULE 13G/A | 0001829126-25-000921 | 2025-02-13 | Polen Credit Opportunities Fund |
| SCHEDULE 13G/A | 0001010422-25-000004 | 2025-07-22 | Polen Credit Opportunities Fund, filed by Polen Capital Credit |
| SCHEDULE 13G/A | 0001172661-25-002704 | 2025-07-24 | Paycom, 2,846,113 shares, 4.92% at 6/30/2025, signed by Walsh. Below 5%, so reporting ends |
| N-PX | 0001172661-25-003850 | 2025-08-27 | Located, not analysed |
| N-PX | 0001172661-26-003271 | 2026-08-11 | Located, not analysed |
| Form ADV Part 2A | [Combined Form ADV, March 2026](https://www.polencapital.com/hubfs/_web/Disclosures/Combined_Form_ADV.pdf); also IAPD brochure version 1032050 | March 2026 | RAUM $24,061,099,864 discretionary plus $9,285,497,035 advised (12/31/2025). Control persons; 5Perspectives team; Polen International Equity LLC |
| Form ADV Part 1 data | specstream, RIA Monitor (third-party) | ADV filed 2026-09-30 and 2025-05-06 | $24.06B, 1,607 accounts, 168 employees with 22 investment staff, 2 private funds ($108.6M). Prior RAUM $37.70B |
| N-PORT-P, Polen Growth Fund (FundVantage Trust, CIK 1388485, series S000029264) | 0000940400-26-011374, https://www.sec.gov/Archives/edgar/data/1388485/000094040026011374/0000940400-26-011374.txt | period 2026-01-30 | Net assets $3.64B, 25 stocks, plus 70,000 Vanguard Growth ETF shares |
| Schedule of investments (same fund) | https://www.sec.gov/Archives/edgar/data/1388485/000094040026011370/MB50FV013126.htm | 1/31/2026 | Readable version of the above |
| Schedule of investments (same fund) | https://www.sec.gov/Archives/edgar/data/1388485/000175272424212313/MB45FV073124.htm | 7/31/2024 | Earlier example, used to confirm the overlap with Focus Growth |

**Types searched for and not found in the adviser's EDGAR folder:**
- Schedule 13D: none. Polen is not an activist.
- Forms 3, 4 and 5: none. Polen has not been a 10% holder or insider.
- Form D: none, although the ADV lists 2 private funds.
- Confidential-treatment 13F filings: none.

**N-CSR for FundVantage** was not pulled from EDGAR directly. Fund size figures for 4/30/2026 and later came from Polen's annual report PDF, CapEdge and the factsheet; see the next section. The EDGAR archive listing I could read looked stale after 2026-08-11, so a filing made after that date could have been missed. The Q3 2026 13F and the September 2026 ADV were found by direct accession or through aggregators.

## Other sources (manager's words, press, aggregators)

Focus Growth commentaries and talks, the main source for what the manager said:

| Source | Date published or read |
|---|---|
| [Focus Growth presentation, Q4 2023 data](https://advisorintelligence.com/files/1719852992_Polen-Focus-Growth-Presentation.pdf) | read 2026-11 |
| [Q2 2024 letter (fiscal.ai)](https://fiscal.ai/fund-letters/polen-capital-q2-2024-fscl_document_7BWD3BFM707/) | Q2 2024 |
| [Q2 2024 Davidowitz fireside chat](https://www.polencapital.com/q2-2024-focus-growth-fireside-chat) | July 2024 |
| [Q3 2024 commentary (Seeking Alpha 4736847)](https://seekingalpha.com/article/4736847-polen-focus-growth-portfolio-q3-2024-commentary) | 2024-11-13 |
| [Q4 2024 commentary (advisorintelligence)](https://advisorintelligence.com/files/Polen-Focus-Growth-Commentary-Q4-24.pdf); also reprinted by buysidedigest | Jan 2025 |
| [Q1 2025 commentary (Seeking Alpha 4777163)](https://seekingalpha.com/article/4777163-polen-focus-growth-portfolio-q1-2025-commentary) | April 2025 |
| [Q2 2025 commentary (Seeking Alpha 4803243)](https://seekingalpha.com/article/4803243-polen-focus-growth-portfolio-q2-2025-commentary) | July 2025 |
| [Q3 2025 commentary (advisorintelligence)](https://advisorintelligence.com/files/Polen-Focus-Growth-Commentary-Q3-25.pdf); also on fiscal.ai | October 2025 |
| Q3 2025 fireside chat (pantheon.polencapital.com) | 2025-10-15 |
| [Yahoo Finance: NVIDIA initiated in August](https://finance.yahoo.com/news/polen-focus-growth-strategy-initiated-130637898.html) | 2025-10-14 |
| [Q4 2025 commentary (Seeking Alpha 4861364, also 4861367)](https://seekingalpha.com/article/4861364-polen-focus-growth-portfolio-q4-2025-commentary); also on fiscal.ai | 2026-01-21 |
| [Q1 2026 portfolio update (Seeking Alpha 4898017)](https://seekingalpha.com/article/4898017-polen-focus-growth-portfolio-q1-2026-portfolio-update); also on fiscal.ai | 2026-05-04 |
| [Q2 2026 letter (fiscal.ai)](https://fiscal.ai/fund-letters/polen-capital-q2-2026-fscl_document_5KBH8KUR503/); also a whitecliff-hosted PDF | July 2026 |
| [Current Focus Growth commentary, Q3 2026](https://www.polencapital.com/hubfs/_web/Quality%20Growth%20Franchise/Focus%20Growth/ad-hoc/Polen_Focus_Growth_Commentary.pdf) | read 2026-11 |

Firm, team and fund pages:
- 5Perspectives Growth: [franchise page](https://www.polencapital.com/franchises/5perspectives-growth), [SMA page](https://www.polencapital.com/smas/5perspectives-growth-opportunities-sma) (transition date June 30, 2025), [ETF launch news](https://www.polencapital.com/insights/news/5perspectives-etf-launch) (2026-05-18).
- [InvestmentNews on the ETF launch](https://www.investmentnews.com/etfs/polen-capital-aims-to-boost-advisor-choice-with-active-growth-equity-etfs/266698) (2026-05-21).
- [Polen Focus Growth ETF 497K](https://www.polencapital.com/hubfs/_web/Quality%20Growth%20Franchise/Focus%20Growth/ETF/e146393_Polen%20Focus%20Growth%20ETF%20-%20497K_WebReady.pdf): firm AUM about $22.76B at 6/30/2026.
- Polen Growth Fund: [annual report](https://www.polencapital.com/hubfs/_web/Quality%20Growth%20Franchise/Focus%20Growth/MF/Polen%20Growth%20Fund%20-%20Institutional%20Class.pdf) ($2.16B at 4/30/2026); [factsheet and top ten](https://www.polencapital.com/mutual-funds/focus-growth-mutual-fund) (9/30/2026); [CapEdge](https://capedge.com/fund/S000029264/holdings) ($1.64B at 7/31/2026).
- [Morningstar firm page](https://www.morningstar.com/asset-management-companies/polen-capital-BN00000OKL).

Press and aggregators:
- [Insurance Journal reprint of Bloomberg](https://www.insurancejournal.com/news/southeast/2026/06/17/874134.htm), 2026-06-17 ([Bloomberg original](https://www.bloomberg.com/news/articles/2026-06-17/wrong-way-ai-trade-costs-boca-raton-stock-picker-50-billion) is paywalled; I read the reprint). Covers AUM history, job cuts, departures and the NVIDIA quotes.
- [Financial Standard](https://www.financialstandard.com.au/news/severe-underperformance-sees-polen-capital-funds-wound-up-179811977), 2026-03-24: Montgomery winds up its Polen funds.
- [briefglance](https://briefglance.com/articles/polen-capital-bets-on-autonomy-with-new-12b-international-equity-team), 2026-08-04: Polen International Equity and the CastleArk team.
- [13finsight](https://13finsight.com/research/polen-capital-q1-2026-growth-book-cut-in-half), 2026-05-23: Q1 2026 13F commentary. Used as a cross-check only.
- [specstream](https://specstream.ai/data/investment-advisers/firm/polen-capital-management-llc-106093) (checked 2026-11-10) and [RIA Monitor](https://www.riamonitor.com/firms/106093): ADV Part 1 data.

## Problems and how they were handled

- **Direct curl to sec.gov was denied** by the environment's auto-mode classifier. I did not retry, and used Exa for all EDGAR reads.
- **Exa fetches that failed:**
  - `infotable.html` returned CRAWL_NOT_FOUND. I used `infotable.xml` instead.
  - The whitecliff Q1 2026 PDF returned CRAWL_NOT_FOUND. I used the Seeking Alpha and fiscal.ai versions.
  - The advisorintelligence Q1 2025 commentary returned CRAWL_NOT_FOUND. I used Seeking Alpha 4777163.
  - The 0001172661-24-004486 filing directory returned CRAWL_LIVECRAWL_TIMEOUT. I used the full-text .txt file.
- **The Q4 2023 commentary** was read only through excerpts in search results and the presentation deck, not as a full PDF.
- **Not done:**
  - N-PX voting records were located but not analysed.
  - FundVantage N-CSR was not read from EDGAR; I used Polen-hosted reports instead.
  - Bloomberg was paywalled, so I read the reprint.
- **Paywalls and sign-ins:** none were entered. Bloomberg was the only paywalled source.
- **Q4 2023 values:** the filing's own errors were documented, not corrected, in the CSV.

## Working files

The scratch scripts (`check.py` for reconciliation, `build.py` for CUSIP aggregation, `analyze.py` for concentration and median-flow stats) are in the session scratch directory and are not kept. The method is described in `profile.md` under "Flows versus decisions".


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
