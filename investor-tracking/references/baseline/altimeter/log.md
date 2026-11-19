# Altimeter Capital Management: research log

Manager: Altimeter Capital Management, LP (Brad Gerstner). CIK 0001541617. Written 2026-11-19. All web access was through Exa search/fetch; direct requests to sec.gov were not used.

## Oddities a future reader should know first

- **Q3 2026 does not reconcile exactly.** The 17 information-table values sum to $10,308,735,663; the cover page says $10,309,080,051, a gap of $344,388 (0.003%). I re-checked all 17 values against the filing text and the transcription is faithful. The cause is unknown, possibly a rounding or late edit on the filer's side. The other eleven quarters match on both row count and total.
- **Value scale checked: whole dollars in all twelve quarters, no x1,000 adjustment needed.** Every cover total is $5B-$10B in whole dollars and matches the row sum. Implied prices match the market at each quarter end, e.g. Q4 2023: Snowflake $199.00, Meta $353.96, Microsoft $376.04; Q1 2024: Nvidia $903.56 (pre-split). Q2 2024 Nvidia is $123.54 after the split.
- **Q2 2024 name swap.** The filing pairs the issuer names "AMAZON COM INC" and "ASTERA LABS INC" with each other's CUSIPs. The CSV uses the issuer that matches the CUSIP (023135106 = Amazon, 04626A103 = Astera).
- **Q3 2024 misnamed issuer.** CUSIP 53566V106 is filed as "LINEAGE CELL THERAPUTICS IN" but is Lineage, Inc. (the cold-storage REIT that IPO'd in July 2024). The CSV uses "LINEAGE INC".
- **Q1 2025 QQQ put has an empty put/call field.** Title of class reads "PUT" but the putCall element is blank. The CSV records it as `Put`. Aggregators disagree on this row; at least one later called the Q3 2026 SMH put Altimeter's "first option since 2019", which is wrong.
- **Q2 2026 lowercase CUSIP** on the Cerebras row; normalized to upper case.
- **Grab warrant CUSIP changed** from G0370L116 to G4124C117 in Q2 2026 (same 3,502,000 warrants, class "W EXP 12/1/202", truncated in the filing). Treat as one continuous position.
- **NVIDIA 10-for-1 split** (June 2024) makes Q2 2024 shares jump from 0.79M to 7.74M; not a purchase.
- **Voting authority:** from Q2 2025 many rows split voting authority between Sole and None (e.g. Nvidia Q3 2026: 8,093,046 sole, 1,913,023 none). The filing does not say which account the "none" slice is. My guess, low confidence: a client account that keeps its own votes, maybe the sovereign-wealth SMA.
- **Address change:** the filer address moved from Boston, MA to Menlo Park, CA starting with the Q1 2026 filing. The Q2 2026 cover page newly carries CRD 000160017 and SEC file 801-73411.
- **Signers:** Mara Davis (CCO) through Q3 2024; Kate Karustis (Compliance Associate) Q4 2024 and Q1 2025; Annie Hancock (CCO and Deputy General Counsel) from Q2 2025.
- **No amendments or late notices:** no 13F-HR/A or 13F-NT in the period. All rows are SH (none PRN); no other included managers; no confidential treatment requested.
- **The EDGAR folder listing was stale.** https://www.sec.gov/Archives/edgar/data/1541617/ as fetched omitted 0001541617-25-000003, -26-000010 and -26-000011; I found them by probing accession folders directly.
- **Implied prices in Q3 2026** look very high for Micron (~$1,065) and SanDisk (~$1,740), straight from value/shares. Recorded as filed; not independently verified.

## 13F-HR filings read (holdings CSVs built from these)

Each URL is the full submission text file. Rows were transcribed, summed by CUSIP and put/call, and checked against the cover page.

| Quarter | Accession | Filed | Cover rows / rows read | Cover total / sum | Result |
|---|---|---|---|---|---|
| 2023-Q4 | 0001541617-24-000004 | 2024-02-14 | 11 / 11 | 6,022,792,261 / same | OK |
| 2024-Q1 | 0001541617-24-000006 | 2024-05-15 | 17 / 17 | 6,509,261,366 / same | OK |
| 2024-Q2 | 0001541617-24-000007 | 2024-08-14 | 20 / 20 | 6,731,598,776 / same | OK |
| 2024-Q3 | 0001541617-24-000009 | 2024-11-14 | 23 / 23 | 6,753,620,788 / same | OK |
| 2024-Q4 | 0001541617-25-000002 | 2025-02-14 | 24 / 24 | 5,545,911,561 / same | OK |
| 2025-Q1 | 0001541617-25-000005 | 2025-05-15 | 22 / 22 | 4,971,096,519 / same | OK |
| 2025-Q2 | 0001541617-25-000009 | 2025-08-14 | 18 / 18 | 6,930,626,980 / same | OK |
| 2025-Q3 | 0001541617-25-000013 | 2025-11-14 | 23 / 23 | 7,581,939,536 / same | OK |
| 2025-Q4 | 0001541617-26-000002 | 2026-02-17 | 18 / 18 | 6,661,973,445 / same | OK |
| 2026-Q1 | 0001541617-26-000006 | 2026-05-15 | 13 / 13 | 5,699,287,719 / same | OK |
| 2026-Q2 | 0001541617-26-000008 | 2026-08-14 | 20 / 20 | 9,829,676,383 / same | OK |
| 2026-Q3 | 0001541617-26-000010 | 2026-11-16 | 17 / 17 | 10,309,080,051 / 10,308,735,663 | Off by $344,388 |

URLs, in the same order:
- https://www.sec.gov/Archives/edgar/data/1541617/000154161724000004/0001541617-24-000004.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161724000006/0001541617-24-000006.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161724000007/0001541617-24-000007.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161724000009/0001541617-24-000009.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161725000002/0001541617-25-000002.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161725000005/0001541617-25-000005.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161725000009/0001541617-25-000009.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161725000013/0001541617-25-000013.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161726000002/0001541617-26-000002.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161726000006/0001541617-26-000006.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161726000008/0001541617-26-000008.txt
- https://www.sec.gov/Archives/edgar/data/1541617/000154161726000010/0001541617-26-000010.txt

Raw transcriptions and the build/analysis scripts are in the helper's scratch folder (not kept): raw/<quarter>.txt, scripts/build.py, scripts/analyze.py.

## Other SEC filings, by type

**Schedule 13G / 13G-A (read).** All are passive filings; there is no Schedule 13D in the period.
- SC 13G/A, Confluent, 0001541617-24-000002, filed 2024-02-14. Above 5% at 2023-12-31. https://www.sec.gov/Archives/edgar/data/1541617/000154161724000002/
- SC 13G/A, Snowflake, Amendment No. 5, 0001541617-24-000003, filed 2024-02-14. Altimeter 12,424,944 shares (4.71%); Gerstner 15,503,498 including shares "held directly", so about 3.08M personal shares sit outside the 13F. https://www.sec.gov/Archives/edgar/data/1541617/000154161724000003/
- SCHEDULE 13G/A, Confluent, Amendment 4, 0001541617-25-000008, filed 2025-08-14, Rule 13d-1(c). 13,122,150 shares (4.5%) at 2025-08-14; 15,552,976 (5.3%) at 2025-06-30; 13,626,464 (5.5%) at 2024-09-30. https://www.sec.gov/Archives/edgar/data/1541617/000154161725000008/
- SCHEDULE 13G, Cerebras Systems, 0001541617-26-000009, filed 2026-08-14, Rule 13d-1(b). 7,160,181 shares (6.2%) at 2026-08-14; 7,225,037 (7.3%) at 2026-06-30; 7,707,909 (18.3% of Class A) at 2026-05-31. Shares "held of record by several private funds". Joint filing agreement in altimeterjfa.pdf. https://www.sec.gov/Archives/edgar/data/1541617/000154161726000009/
- SCHEDULE 13G/A, Cerebras Systems, 0001541617-26-000011, filed 2026-11-16, Rule 13d-1(d). 5,953,504 shares (3.7%) at 2026-09-30; Gerstner personally 360,097 more. https://www.sec.gov/Archives/edgar/data/1541617/000154161726000011/
- Looked for and not found: any 13G/13G-A for Coupang, CoreWeave, SpaceX, Uber, Meta or Nvidia (none expected given position sizes against shares outstanding, but CoreWeave and SpaceX were worth checking).

**Forms 3, 4, 5.** None found filed by Altimeter Capital or Brad Gerstner as a reporting owner in the period. Searches for Cerebras insider filings returned only other insiders (for example Andrew Feldman and a director, Vassallo). Gerstner says he sat on Cerebras's board, so a Form 3/4 might be expected; I could not find one through Exa and log it as looked-for, not found, not as proof none exists. The Cerebras lock-up was reported to end around 2026-11-09.

**Form N-PX (proxy votes).**
- 0001541617-24-000008, filed 2024-08-30 (12 months to 2024-06-30). https://www.sec.gov/Archives/edgar/data/1541617/000154161724000008/
- 0002073679-25-000037, filed 2025-09-02 (proxytable.xml read). Filed under a filing agent's prefix. Say-on-pay votes only; FOR management on every one (Amazon, Confluent, Coupang, Flutter, Maplebear, Meta including three-year frequency, Micron, Microsoft, Nvidia, Robinhood, Snowflake, Uber). Small separate blocks recorded as abstain or against-management: Confluent 666 shares, Maplebear 326,814, Nvidia 66,600.
- 0002073679-26-000153, filed 2026-08-31. Located but not read in detail; skimmed only for type.

**Form ADV.**
- Part 2A brochure, March 2026: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1038994 (strategies, the four fund families, the sovereign-wealth SMA, Menlo Park and Boston offices).
- Part 1: https://reports.adviserinfo.sec.gov/reports/ADV/160017/PDF/160017.pdf (RAUM $18,753,715,687 at 2025-12-31, 36 accounts, 33 private funds of which 31 venture and 2 hedge, 35 employees of whom 13 give investment advice).
- AUM history (secondary, aggregated from ADV): https://specstream.ai/data/investment-advisers/firm/altimeter-capital-management-lp-160017, read 2026-11-18/19. Prior-year RAUM $12.69B.

**Form D / D-A.**
- Altimeter Partners Fund LP (the hedge fund), CIK 1452343, cumulative amount sold: 0001452343-23-000001 (2023-04-28) $3,462,619,888, 364 investors; 0001452343-24-000001 (2024-04-25) $3,470,268,581, 369; 0001541617-25-000003 (2025-04-29, filed under Altimeter's prefix) $3,544,297,644, 379; 0001814554-26-000086 (2026-04-30) $3,703,885,893, 386. Minimum investment $100,000; first sale 2008-11-01. These are cumulative gross sales; redemptions are not reported.
- Venture and co-investment vehicles found by search: Altimeter Growth Olympic Fund II (CIK 2064415, 2025-04-21, $250M, 13 investors); Olympic IV (CIK 2085849, 2025-09-12, $27.25M sold); Olympic VIII (CIK 2134726, 2026-05-15, $40M offering); Altimeter Growth Co-Invest VI (CIK 1915734, 2025-08-08, $15M); Venture Partners VII ($1B, 2023-06-29). Older Growth Partners IV, V and Castle entities appeared too.
- Looked for and not found: a Form D for the Long Opportunities Fund.

## Gerstner's own words and other web sources (chronological)

Dates are publication dates; all read 2026-11-17 to 2026-11-19 via Exa.
- 2022-10-24, "Time to Get Fit" open letter to Meta (Medium, Altimeter's account): https://medium.com/@alt.cap/time-to-get-fit-an-open-letter-from-altimeter-to-mark-zuckerberg-and-the-meta-board-of-392d94e80a18
- 2024-05-07, CNBC, exposure cut 10-20 points: https://www.cnbc.com/2024/05/07/altimeters-brad-gerstner-says-he-trimmed-positions-across-portfolio-after-2024s-strong-tech-run.html
- 2024-06-02 and 2024-10-01, Motley Fool on Snowflake (secondary): https://www.fool.com/investing/2024/06/02/ and https://www.fool.com/investing/2024/10/01/ (article slugs truncated in my notes)
- 2024-11-21, CNBC Trade Tracker, Uber to Tesla: https://www.cnbc.com/video/2024/11/21/trade-tracker-brad-gerstner-sells-uber.html; quotes via https://www.teslarati.com/tesla-tsla-acts-as-replacement-for-uber-in-legendary-investors-portfolio/ and https://www.matterfact.com/newsletter/2026-09-23-track-record-gerstner-tesla-uber-robotaxi
- 2025-01-11, BG2 podcast on net exposure and the 10-year: https://www.youtube.com/watch?v=yPD1qEbeyac; figures from a third-party summary https://finance.biggo.com/podcast/4cbbdaa4dbd491d5 (secondary; not checked against the audio)
- 2025-03-02, 24/7 Wall St on the KWEB position (secondary): https://247wallst.com/investing/2025/03/02/
- 2025-04-03, CNBC, "bomb shelter": https://www.cnbc.com/2025/04/03/nvidia-positioned-to-weather-trump-tariffs-says-altimeters-gerstner.html; fuller quote https://finviz.com/news/38283/brad-gerstner-says-hes-buying-nvidia-nvda-amid-off-the-charts-gpu-demand-secular-growth; tariffs https://www.cnbc.com/2025/04/03/ceos-think-trumps-tariff-plan-is-a-huge-mistake-says-altimeters-brad-gerstner.html; Tesla segment https://www.cnbc.com/video/2025/04/03/brad-gerstner-explains-his-tesla-position.html
- 2025-04-28, Yahoo Finance, Tesla "has to execute": https://finance.yahoo.com/news/brad-gerstner-says-no-market-212542879.html
- 2025-10 (mid-October), BG2 on circular revenue: https://www.youtube.com/watch?v=KX6q6lvoYtM
- 2025-11-07, CNBC, Nvidia position "as large as it had ever been": https://www.cnbc.com/2025/11/07/altimeters-brad-gerstner-says-market-pullback-is-healthy-sees-no-bubble-in-tech.html
- 2025-12, "wall of worry" (secondary write-up): https://www.capitalaidaily.com/ai-boom-climbing-wall-of-worry-that-stops-a-bubble-from-forming-says-altimeters-brad-gerstner/
- 2026-03-17, IBM completes Confluent acquisition: https://newsroom.ibm.com/2026-03-17-ibm-completes-acquisition-of-confluent,-making-real-time-data-the-engine-of-enterprise-ai-and-agents; Confluent 8-K https://www.sec.gov/Archives/edgar/data/1699838/000110465926029071/tm268826d6_8k.htm
- 2026-05-04, Milken conference interview (Altimeter's YouTube upload): https://www.youtube.com/watch?v=T3Stli61soU; https://www.benzinga.com/markets/tech/26/05/52311247/nvidia-10-trillion-valuation-altimeter-brad-gerstner-forecast-market-concerns
- 2026-05-14, CNBC at the Cerebras IPO: https://www.youtube.com/watch?v=q8tjCXs3xvA
- 2026-06-12, SpaceX IPO (company IR and MarketWatch; URLs truncated in my notes) and an Altimeter LinkedIn post noting participation.
- 2026-09-24, CNBC full interview: https://www.youtube.com/watch?v=8dND0Pj7PA0; https://www.cnbc.com/video/2026/09/24/cnbc-full-interview-altimeter-capital-brad-gerstner.html
- 2026-10-15, CNBC, "lowest they've been in three years" (transcript): https://ceointerviews.ai/interview/3067810/; video https://www.youtube.com/watch?v=s-h4NpYmVBU
- 2026-10-21, CNBC Squawk Box on a SpaceX-Tesla combination: https://www.cnbc.com/video/2026/10/21/brad-gerstner-cheaper-capital-may-be-key-to-spacex-tesla-merger.html
- 2026-11-12, Nvidia CEO change, confirmed in primary sources. The board accepted Huang's resignation on 11 Nov, effective immediately; Colette Kress named interim CEO and Harvey Jones chair. Nvidia 8-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm; press release: https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition. Earlier board statement on its investigation (2026-11-08): https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/
- 2026-11-13 (letter posted on X) and 2026-11-14 (coverage), Gerstner and Gavin Baker's joint letter to Nvidia's board. It asks for a slow, deliberate succession process that keeps Huang's possible return open. CNBC: https://www.cnbc.com/2026/11/14/nvidia-investors-jensen-huang-return-board-letter.html. On 2026-11-16 Gerstner said it was not a call for immediate reinstatement. Semafor: https://www.semafor.com/article/11/16/2026/altimeters-gerstner-urges-nvidias-board-to-reconsider-huangs-ouster-to-get-this-right; CNBC video: https://www.cnbc.com/video/2026/11/16/brad-gerstner-on-his-letter-to-nvidia-board-suggesting-potential-return-of-huang.html. The same day a source told CNBC the board was not considering Huang's return: https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html
- 2026-11-16, CNBC, $5B Anthropic IPO order: https://www.cnbc.com/2026/11/16/altimeters-brad-gerstner-investing-5-billion-in-anthropic-ipo.html; excerpts https://www.cnbc.com/2026/11/16/cnbc-exclusive-excerpts-altimeter-capital-founder-ceo-brad-gerstner-speaks-with-cnbcs-scott-wapner-on-halftime-report-today.html
- 2026-11-16/17, secondary takes on the Q3 2026 13F: https://thefilingsreport.substack.com/p/the-ai-bull-sold-the-equipment-makers; https://mlq.ai/news/altimeter-sells-its-chip-equipment-stocks-and-qualcomm-buys-a-put-on-a-chip-etf-and-a-tesla-stake-13f-shows/; https://chipdispatch.com/articles/altimeter-exits-qualcomm-chip-equipment-adds-tesla-and-etf-put

## Problems and gaps

- Exa fetch of the 0001541617-25-000003 full .txt returned CRAWL_NOT_FOUND; the index page and primary_doc.xml under CIK 1452343 worked instead.
- The EDGAR browse page for CIK 1452343 timed out (CRAWL_LIVECRAWL_TIMEOUT).
- Probes of accession numbers 24-000001, 24-000005, 25-000001, 25-000004, 25-000006, 25-000007, 25-000010 to 25-000012, 26-000001, 26-000003 to 26-000005, 26-000007 and 26-000012 under CIK 1541617 returned CRAWL_NOT_FOUND. They either do not exist or were filed under an agent's CIK; I cannot rule out an unseen filing.
- No Forms 3/4/5 found (see above). No Long Opportunities Fund Form D found. The 2026 N-PX was not read in detail.
- Gerstner's posts on X were not read directly; quotes come from video, CNBC text and transcripts. The Jan 2025 BG2 exposure figures come from a third-party summary, not the audio.
- I found no public LP letter from Altimeter for the period.
- Reasons for the Snowflake sell-down, the China trades and the Q3 2026 Tesla purchase were not found in any Gerstner statement; the profile marks these as inference.
- I didn't read the full text of the Gerstner/Baker letter on X. Its quotes come from CNBC and the Economic Times (ANI). The Nvidia CEO change is confirmed by Nvidia's own 8-K and press release.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
