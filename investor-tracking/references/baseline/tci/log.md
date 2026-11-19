# TCI Fund Management (CIK 1647251): research log

Written 2026-11-19 by a helper session. Draft for review.

## Anything odd, read this first

- **All twelve 13F-HRs found, no amendments, no NT filings.** Every quarter Q4 2023 to Q3 2026 has exactly one original 13F-HR, self-filed under TCI's own CIK prefix (0001647251-…). No 13F-HR/A and no 13F-NT exist in the archive folder for the window. The other accession numbers in the folder in this window are N-PX filings (late August each year, self-filed) and Schedule 13D/13G filings made by the filing agent Schulte Roth & Zabel (prefix 0000902664-).
- **Every quarter reconciled with its cover page** on both row count and total value. The one discrepancy is Q3 2025: rows sum to $52,699,548,226 against a cover total of $52,699,548,227, a $1 rounding difference.
- **All rows are SH** (no PRN), all SOLE investment discretion, all voting authority SOLE, no put/call rows, no "other managers" (cover reports 0 other included managers every quarter). No CUSIP needed aggregating (one row per CUSIP every quarter), so the CSVs are row-for-row the filings, sorted by value.
- **Two name changes on unchanged CUSIPs**, which some aggregator sites misread as an exit plus a new buy: GENERAL ELECTRIC CO became GE AEROSPACE in Q2 2024 (CUSIP 369604301), and FERROVIAL SE became FERROVIAL NV in Q2 2026 (CUSIP N3168P101). danielscrivner.com's Q2 2026 page shows Ferrovial as "Exited" and "Ferrovial NV" as "NEW"; that is wrong. Hedgefundalpha's Q1 2026 portfolio page also calls Ferrovial a new position in Q1 2026; it has been in every 13F since Q2 2024.
- **Corporate actions inside the window:** GE Vernova spin-off (April 2024, 1 GEV per 4 GE): no GEV row ever appears, so TCI sold the roughly 11.7M GEV shares it would have received within Q2 2024. Mobility Global spin-off from S&P Global (record date 2026-06-15, distributed 2026-07-01, 1 MBGL per SPGI share): TCI would have received about 14.08M MBGL shares and held only 623,651 at 2026-09-30, so it sold about 96% of the spin-off within the quarter. Source for the Mobility Global terms: S&P Global 8-K and press release (URLs below).
- **Ferrovial appears in Q2 2024 because Ferrovial's shares began trading in the US that quarter, not because TCI bought it then.** TCI has held Ferrovial since at least 2023 (Dutch AFM notification of July 2023: 1.53% direct shares plus 8.50% via swaps).
- **The 13F covers two TCI-managed vehicles**: The Children's Investment Master Fund (Cayman) and CIFF Capital UK LP (the investment vehicle of Hohn's foundation, the Children's Investment Fund Foundation). This is stated in Item 2 of TCI's 13G filings on Moody's and CPKC. The 2024 N-PX shows two voting rows per company whose share counts add to the 13F total (e.g. Visa 1,151,000 + 15,646,187 = 16,797,187), consistent with two vehicles; from 2025 the N-PX shows one row per company.
- **Price moves dominate quarter-to-quarter value changes.** Total 13F value fell 15.8% in Q1 2026 and 6.0% in Q3 2026 almost entirely through prices (GE implied price fell from $373.7 to $312.3 in Q3 2026).
- **Possible missing 13G amendment on CPKC (low confidence, flagged only for watching):** TCI's last CPKC 13G/A in its folder is February 2024 at 5.96% (55.5M shares of 931.8M). Holdings fell to 44.47M by 2026-09-30. If CPKC's share count is around 900M, that is just under 5%, which would normally prompt an exit amendment. I did not check CPKC's current share count, so this may simply not have crossed 5% yet.

## 13F filings read (all via Exa web_fetch of the full submission .txt)

Archive directory: https://www.sec.gov/Archives/edgar/data/1647251/ (fetched 2026-11-19; matches the brief's note that the browse page is stale and the archive is current).

| Period | Form | Accession | Filed | Cover entries / total | Parsed rows / total | URL |
|---|---|---|---|---|---|---|
| 2023-Q4 | 13F-HR | 0001647251-24-000002 | 2024-02-14 | 11 / $35,967,437,232 | 11 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725124000002/0001647251-24-000002.txt |
| 2024-Q1 | 13F-HR | 0001647251-24-000004 | 2024-05-15 | 10 / $39,659,032,698 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725124000004/0001647251-24-000004.txt |
| 2024-Q2 | 13F-HR | 0001647251-24-000007 | 2024-08-14 | 10 / $40,924,384,465 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725124000007/0001647251-24-000007.txt |
| 2024-Q3 | 13F-HR | 0001647251-24-000011 | 2024-11-14 | 10 / $44,020,529,632 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725124000011/0001647251-24-000011.txt |
| 2024-Q4 | 13F-HR | 0001647251-25-000003 | 2025-02-14 | 10 / $42,413,899,286 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725125000003/0001647251-25-000003.txt |
| 2025-Q1 | 13F-HR | 0001647251-25-000005 | 2025-05-15 | 10 / $43,372,530,344 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725125000005/0001647251-25-000005.txt |
| 2025-Q2 | 13F-HR | 0001647251-25-000009 | 2025-08-14 | 10 / $50,706,910,931 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725125000009/0001647251-25-000009.txt |
| 2025-Q3 | 13F-HR | 0001647251-25-000014 | 2025-11-14 | 9 / $52,699,548,227 | 9 / $52,699,548,226 ($1 rounding) | https://www.sec.gov/Archives/edgar/data/1647251/000164725125000014/0001647251-25-000014.txt |
| 2025-Q4 | 13F-HR | 0001647251-26-000002 | 2026-02-17 | 9 / $53,648,816,254 | 9 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725126000002/0001647251-26-000002.txt |
| 2026-Q1 | 13F-HR | 0001647251-26-000004 | 2026-05-15 | 10 / $45,170,870,798 | 10 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725126000004/0001647251-26-000004.txt |
| 2026-Q2 | 13F-HR | 0001647251-26-000007 | 2026-08-14 | 11 / $52,769,884,406 | 11 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725126000007/0001647251-26-000007.txt |
| 2026-Q3 | 13F-HR | 0001647251-26-000011 | 2026-11-16 | 12 / $49,583,884,496 | 12 / same | https://www.sec.gov/Archives/edgar/data/1647251/000164725126000011/0001647251-26-000011.txt |

Cover-page constants every quarter: report type 13F HOLDINGS REPORT; amendment flag false; 13F file number 028-16990; CRD 000269954; SEC file number 802-102468 (an exempt-reporting-adviser number); other included managers 0; signed by Angus Milne, Head of Compliance, London. Values are whole dollars (implied prices check out, e.g. GE $127.6 at 2023-12-31).

Parsing: values and shares were transcribed from the fetched text into a small Python data file in the session scratchpad, and totals were checked against the covers (the value checksums all matched, which also validates the value transcription; share counts are not covered by that checksum, but implied prices are all plausible).

## Other SEC filings (scope addition of 2026-11-19)

Schedule 13D / 13G (all filed via Schulte Roth & Zabel, accession prefix 0000902664):

- 0000902664-23-005905, SC 13G/A on Moody's, filed 2023-12-18 (just before the window; read index only). https://www.sec.gov/Archives/edgar/data/1647251/000090266423005905/0000902664-23-005905-index.html
- 0000902664-24-001652, SC 13G/A Amendment 2 on Moody's, filed 2024-02-14: 12,049,611 shares, 6.58%, Rule 13d-1(c) (passive). Item 2 names the Master Fund and CIFF Capital UK LP as holders. https://www.sec.gov/Archives/edgar/data/1647251/000090266424001652/p24-0514sc13ga.htm
- 0000902664-24-001653, SC 13G/A Amendment 5 on Canadian Pacific Kansas City, filed 2024-02-14: 55,514,385 shares, 5.96%, Rule 13d-1(c). https://www.sec.gov/Archives/edgar/data/1647251/000090266424001653/p24-0512sc13ga.htm
- 0000902664-24-006201, SC 13D/A Amendment 9 on Canadian National, filed 2024-11-04: 32,719,677 shares, 5.2% at 2024-11-01, aggregate cost ~$3.28bn; Schedule A lists daily sales from 2024-09-18 to 2024-11-01 (all sales, in both USD and CAD). Item 4 not amended (the activist purpose is in the 2021 amendments). https://www.sec.gov/Archives/edgar/data/16868/000090266424006201/p24-3188sc13da.htm
- 0000902664-25-002033, SCHEDULE 13D/A Amendment 10 on Canadian National, filed 2025-04-30: 26,166,798 shares, 4.2% at 2025-04-29; date of ceasing to be a 5% holder given as 2024-12-11, so this is the exit amendment and later CN trades are visible only in 13Fs. Schedule A shows TCI bought about 468K shares on 2025-04-01 to 04-03 (C$139-143) and then sold about 1.2M from 04-08 to 04-29 (C$131-136): two-way trading around a position being run down. https://www.sec.gov/Archives/edgar/data/1647251/000090266425002033/0000902664-25-002033.txt
- 0000902664-26-002468, SCHEDULE 13G/A Amendment 3 on Moody's, filed 2026-05-15, event date 2026-03-31: 14,334,027 shares, 8.21%. https://www.sec.gov/Archives/edgar/data/1647251/000090266426002468/0000902664-26-002468.txt
- Earlier context read: CN 13D/A of 2021-08-31 with the TCI letter demanding withdrawal from the KCS bid and a CEO change (Item 4). https://www.sec.gov/Archives/edgar/data/16868/000090266421004084/p21-2054sc13da.htm
- Not found: any 13D or 13G on Ferrovial, Visa, S&P Global, GE Aerospace, Alphabet, Microsoft, Martin Marietta or Vulcan in the window. For Ferrovial the direct shareholding (~3%) is below 5% and the rest is cash-settled swaps, which is consistent with no filing.

Forms 3/4/5: none in TCI's folder in the window. TCI's large stakes are either in foreign private issuers (CN, CPKC, Ferrovial), which are exempt from Section 16, or below 10% (Moody's 8.21%). Does not apply.

Form N-PX (self-filed, "Institutional Manager Voting Report", say-on-pay votes only):
- 0001647251-24-000009, period to 2024-06-30, filed 2024-08-29: FOR on every say-on-pay (Ferguson, Visa, Moody's, S&P Global, GE, Thermo Fisher); two rows per company. https://www.sec.gov/Archives/edgar/data/1647251/000164725124000009/0001647251-24-000009.txt
- 0001647251-25-000012, period to 2025-06-30, filed 2025-08-29: FOR on Microsoft, Visa, Moody's, GE Aerospace, S&P Global. https://www.sec.gov/Archives/edgar/data/1647251/000164725125000012/0001647251-25-000012.txt
- 0001647251-26-000009, period to 2026-06-30, filed 2026-08-27: FOR on Microsoft (two rows, one of only 843 shares), Visa, Moody's, GE Aerospace, S&P Global, Alphabet (class A only). https://www.sec.gov/Archives/edgar/data/1647251/000164725126000009/0001647251-26-000009.txt
- Note: the institutional-manager N-PX covers only say-on-pay, so TCI's climate votes and director votes, which matter more for this manager, are not visible here.

Form ADV: TCI is an exempt reporting adviser (file 802-102468, CRD 269954), so it files only parts of Form ADV Part 1 and no Part 2A brochure. Read the latest annual amendment dated 2026-06-29: https://reports.adviserinfo.sec.gov/reports/ADV/269954/PDF/269954.pdf (fetched to 90,000 characters; the document is longer and was cut off). What it shows: UK FCA registration; fiscal year end March; related persons include TCI Advisory Services LLP and The Children's Investment Fund Management (GP) Ltd; Section 7.B lists the TCI Real Estate Partners lending funds with gross asset values of about $1.10bn (Fund I), $1.90bn (Fund II), $2.02bn (Fund III), $1.89bn (Fund IV), plus a Parallel Fund IV (cut off). I did not reach an entry for the equity master fund in the portion fetched, so ADV gave no equity AUM figure. The IAPD summary page (https://adviserinfo.sec.gov/firm/summary/269954) returned only a shell.

Form D: found for the real-estate lending funds (e.g. TCI Real Estate Partners Fund IV LP, Fund IV Ltd and Parallel Fund IV, first sales May 2023, amended 2024-05-16; $732.1M + $676.5M + $470.2M sold). Sources: https://www.sec.gov/Archives/edgar/data/1975683/000090266423003178/0000902664-23-003178.txt and summary at https://altstreet.investments/edgar/1975508. No Form D found for The Children's Investment Master Fund (offshore; presumably not offered in the US under Reg D). These real-estate funds are separate from the equity book and do not touch the 13F.

## Other sources read (chronological by publication date)

- 2021-05-18 Reuters, TCI urges CN to drop voting trust: https://www.reuters.com/business/canadian-national-railway-shareholder-urges-board-amend-kansas-city-deal-2021-05-18/ (search highlight only)
- 2021-09-27 Globe and Mail, Hohn on CN's "weak CEO and weak board": https://www.theglobeandmail.com/business/article-a-weak-ceo-and-a-weak-board-meet-the-hedge-fund-manager-aiming-to/ (highlight)
- 2022-01-25 Trains.com / Globe and Mail / FreightWaves, CN settlement with TCI, Tracy Robinson named CEO: https://www.trains.com/trn/news-reviews/news-wire/cn-names-former-cp-official-tracy-robinson-as-its-next-ceo/
- 2020-07-27 and 2020-10-09 TCI letters on Aena climate plan, and 2021-03-25 letter to Union Pacific (Say on Climate), on tcifund.com: https://www.tcifund.com/Files/esg/Aena%20AGM%20-%20Letter%20to%20Spanish%20Environment%20Minister.pdf ; https://www.tcifund.com/Files/esg/Letter%20to%20AENA%2009.10.20.pdf ; https://www.tcifund.com/files/esg/Union%20Pacific%20Railroad%20-%20Letter%20to%20Union%20Pacific%2025.03.2021.pdf
- TCI ESG policy (dated March 2023) and ESG engagement page: https://www.tcifund.com/ESG ; https://www.tcifund.com/ESGEngagements
- TCI home page (strategy statement): https://www.tcifund.com/
- 2024-01-05 Bloomberg, TCI +33% in 2023 (paywalled, headline and summary only): https://www.bloomberg.com/news/articles/2024-01-05/chris-hohn-s-hedge-fund-bounces-back-with-33-gain-in-2023
- 2024-01-22 Reuters, LCH ranking, TCI $12.9bn 2023 gains: https://www.reuters.com/business/finance/top-global-hedge-funds-tripled-gains-clients-2023-lch-finds-2024-01-22/
- 2025-01-19 24/7 Wall St on CN trims and the 13D/A: https://247wallst.com/investing/2025/01/19/billionaire-investor-trims-railway-holdings-and-puts-it-all-on-this-magnificent-7-stock/
- 2025-01-21 LCH table via Morningstar/Dow Jones (TCI end-2024 AUM $57.6bn, 2024 gains $8.2bn): https://tools.morningstar.co.uk/uk/stockreport/newsItem.aspx?id=TDJNMW_2025012111
- 2025-01-30 Institutional Investor, TCI +15% in 2024 (highlight only): https://www.institutionalinvestor.com/article/2ecrz2s6w3g2k4h9soo3k/hedge-funds/how-chris-hohns-concentrated-portfolio-fared-last-year
- 2025-05-13/14 In Good Company with Nicolai Tangen (Norges Bank), Hohn interview; transcript excerpts via Exa podcast library: https://exa.ai/library/podcast/fdv4tvl897t/episode/wt08ppqg9ws (also https://www.youtube.com/watch?v=M01NZc2QlDk). Full transcripts exist at https://librariancapital.substack.com/p/chris-hohn-interview-by-nicolai-tangen and https://www.icemancapital.com/p/sir-chris-hohn-transcript-from-in (not fetched).
- 2025-08-08 and 2025-08-13 Hedge Fund Alpha, TCI Q1 2025 letter summaries (master fund $61bn; sector gross exposure; contributors): https://hedgefundalpha.com/investor-letters/sir-christopher-hohn-tci-2025/ ; https://hedgefundalpha.com/investor-letters/christopher-hohn-tci-q1-2025/ (rest behind free login; did not register)
- 2025-09-25 TCI letter to Aena board (TCI holds 6%): https://www.tcifund.com/files/corporateengageement/aena/Aena%20Letter%20to%20the%20Board%2025%20September%202025.pdf (highlight only)
- 2025-11-14 Hedge Fund Alpha write-up of Hohn at the Money Maze Allocator Summit: https://hedgefundalpha.com/news/chris-hohn-good-companies-stay-good/ (fetched; rest behind free login)
- 2026-01-18/19 Forbes, WSJ, Institutional Investor, MarketWatch on TCI's record $18.9bn 2025 gain, 27.8% return, $77bn AUM: https://www.forbes.com/sites/hanktucker/2026/01/18/hedge-fund-billionaire-chris-hohns-tci-profited-by-a-record-189-billion-in-2025/ ; https://www.institutionalinvestor.com/article/chris-hohns-tci-tops-hedge-fund-gains-2025
- 2026-04-14 Institutional Investor, TCI -11.9% in March 2026, -9.4% Q1 2026: https://www.institutionalinvestor.com/article/after-record-year-tci-hits-speed-bump
- 2026-05-08 TipRanks/TheFly summarising FT (Costas Mourselas) on the Microsoft cut, with letter quotes: https://www.tipranks.com/news/the-fly/christopher-hohns-tci-slashes-stake-in-microsoft-ft-reports-thefly-news ; Techzine 2026-05-11: https://www.techzine.eu/news/applications/141193/tci-sells-off-billions-in-microsoft-stake-due-to-ai-concerns/ . FT original paywalled: https://www.ft.com/content/ac5d90a9-b010-4529-9616-706420920681
- 2026-07-01 S&P Global press release and 8-K on the Mobility Global spin-off: https://investor.spglobal.com/news-releases/news-details/2026/SP-GLOBAL-INC--COMPLETES-SEPARATION-OF-MOBILITY-GLOBAL-INC-/default.aspx ; https://www.sec.gov/Archives/edgar/data/64040/000110465926080005/tm2619099d1_8k.htm
- 2026-07-03 Alpha-File substack, TCI portfolio stitched from 13F plus European regulator filings (~$27bn of European stakes; Safran 7.1%, Airbus 5%, Aena 6.26%, Cellnex 10.15%, plus Deutsche Börse and LSEG), with sourced Hohn quotes: https://alphafile.substack.com/p/tci-a-73-billion-portfolio-of-monopolies ; and https://alpha-file.com/manager/0001647251-tci-fund-management-ltd (highlight only)
- 2026-10-20 Forbes España / Demócrata, AFM notification: TCI 13% of Ferrovial (3.07% shares, 9.97% swaps): https://forbes.es/ultima-hora/1049407/el-fondo-britanico-tci-eleva-su-participacion-en-ferrovial-al-13-y-se-afianza-como-segundo-mayor-accionista/ ; https://www.democrata.es/en/economy/the-british-fund-tci-increases-its-stake-in-ferrovial-to-13-and-consolidates-its-position-as-the-second-largest-shareholder/
- 2026-11-09 Institutional Investor, TCI -2% YTD after October: https://www.institutionalinvestor.com/article/after-record-2025-chris-hohn-still-digging-out-slump
- 2026-11-17 Alternative Fund Insight on MLM/VMC adds: https://alternativefundinsight.com/chris-hohn-builds-1-5bn-us-construction-materials-position-at-tci/ (highlight only)
- Aggregator pages used only for cross-checks, never for reasons: valuesider.com, holdingsintel.com, 13f.finance, filingspy.com, danielscrivner.com, 13fholding.com, seekingalpha.com (summaries).

## Problems and gaps

- FT, Bloomberg and WSJ originals are paywalled; used only via headlines and secondary summaries (TipRanks/TheFly, Techzine). Not subscribed, per the brief.
- Hedge Fund Alpha letter summaries are behind a free registration; did not register. Only the public lead paragraphs were used.
- No primary TCI investor letter found anywhere freely (TCI does not publish them; they circulate privately).
- No stated reason found for: the Canadian National sell-down (2024 to 2026), the Thermo Fisher exit (Q1 to Q2 2024), the Visa near-doubling (Q2 2025 to Q1 2026), the Alphabet halving in 2025, the Martin Marietta and Vulcan entries (Q2 2026). The profile marks every explanation for these as inference.
- Form ADV PDF was cut off at 90,000 characters; the equity master fund's Section 7.B entry (if listed) was not reached.
- Paywall/sign-in walls hit: FT, Bloomberg, WSJ, Hedge Fund Alpha (free login), Seeking Alpha, substack paid sections, Telegram-gated blog (filosofaresuimercati.eu). None was bypassed.
- Exa itself worked throughout; no fallback to other search tools.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
