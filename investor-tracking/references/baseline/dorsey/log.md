# Dorsey Asset Management: research log

Manager: Dorsey Asset Management, LLC. CIK 0001671657. Slug: dorsey. Log written 2026-11-19.

## Oddities first

- **Every quarter reconciles exactly, in whole dollars.** All 12 quarters from Q4 2023 to Q3 2026 match their cover page on both row count and total value. The Q3 2023 filing, read for context only, also matches.
  - The coordinator later warned that some filers still reported in thousands. I checked Dorsey's scale independently through implied prices, value ÷ shares. Two examples: Meta was $354.0 at Q4 2023 and $485.6 at Q1 2024. Both are real per-share prices, so no quarter here is in thousands and no rescaling was applied.
- **No amendments or notices.** There is no 13F-HR/A or 13F-NT in the period. The amendment flag is false on every filing. There are no confidential-treatment requests, no options (put_call is blank throughout), and no other-included managers (count 0).
- **All rows are SH, none PRN, and all are SOLE discretion.** Each quarter has one row per CUSIP, so no aggregation was needed.
- **A filing agent submits the 13Fs.** Accession numbers carry the agent prefix 0001398344, not Dorsey's CIK. Michael Harriett (CCO/CFO/COO) signs.
- **Filing dates that look late but aren't.** Q4 2025 was filed 2026-02-17: day 45 was Saturday 2026-02-14, and Monday was Presidents' Day. Q3 2026 was filed 2026-11-16: day 45 was Saturday 2026-11-14. Both were filed on the next business day.
- **Booking Holdings 25:1 split.** It took effect after the close on 2026-04-02, and split-adjusted trading began 2026-04-06. Shares went from 16,444 at Q1 2026 to 741,500 at Q2 2026. Split-adjusted, that is an +80% buy, not +4,409%. The N-PX record-date count of 411,100 is exactly 16,444 × 25.
- **Ashtead redomiciled as Sunbelt Rentals Holdings.** The scheme took effect 2026-02-27, with a 1:1 exchange, and NYSE trading began 2026-03-02 (CUSIP 866966104). Sunbelt first appears in the Q1 2026 13F at 11.4%. I treat this as the likely conversion of an existing LSE holding, not a new buy. See profile.md.
- **Smartsheet was taken private** by Blackstone and Vista at $56.50. The deal was announced 2024-09-24 and closed 2025-01-22. The Q1 2025 "exit" is the deal closing.
- **Third-party trackers miss these corporate actions.** Some show Booking and Sunbelt changes as raw trades. Use the split and redomicile adjustments above.
- **ADV 2A date label.** The brochure dated 2026-03-24 gives AUM of $1,445,270,658 "as of February 28, 2025". ADV Part 1, filed the same day, shows the same figure, and Part 1 must be computed within 90 days of filing. So the label is probably a typo for 2026, though it might really be stale. Treat that AUM date as uncertain.
- **Q3 2026 includes an ETF row**, the iShares MSCI ACWI ETF (CUSIP 464288257), at 1%. It is the first fund row in the period.

## 13F filings read

All were read via Exa from the full-submission .txt, which holds the cover page, summary and information table. The URL pattern is `https://www.sec.gov/Archives/edgar/data/1671657/<accession without dashes>/<accession>.txt`. The folder listing was read at https://www.sec.gov/Archives/edgar/data/1671657/

| Period | Form | Accession | Filed | Entries | Total value ($) | Reconciled |
|---|---|---|---|---|---|---|
| 2023-09-30 (context) | 13F-HR | 0001398344-23-020605 | 2023-11-14 | 10 | 765,870,304 | yes |
| 2023-12-31 | 13F-HR | 0001398344-24-002904 | 2024-02-14 | 9 | 777,953,675 | yes |
| 2024-03-31 | 13F-HR | 0001398344-24-009633 | 2024-05-15 | 10 | 860,167,415 | yes |
| 2024-06-30 | 13F-HR | 0001398344-24-014603 | 2024-08-14 | 11 | 839,404,708 | yes |
| 2024-09-30 | 13F-HR | 0001398344-24-020708 | 2024-11-14 | 12 | 927,641,584 | yes |
| 2024-12-31 | 13F-HR | 0001398344-25-002824 | 2025-02-14 | 11 | 970,037,173 | yes |
| 2025-03-31 | 13F-HR | 0001398344-25-009457 | 2025-05-15 | 11 | 943,610,993 | yes |
| 2025-06-30 | 13F-HR | 0001398344-25-015394 | 2025-08-14 | 10 | 1,115,187,507 | yes |
| 2025-09-30 | 13F-HR | 0001398344-25-020887 | 2025-11-14 | 9 | 1,112,595,766 | yes |
| 2025-12-31 | 13F-HR | 0001398344-26-003214 | 2026-02-17 | 10 | 1,150,397,601 | yes |
| 2026-03-31 | 13F-HR | 0001398344-26-009218 | 2026-05-15 | 11 | 1,255,861,264 | yes |
| 2026-06-30 | 13F-HR | 0001398344-26-014470 | 2026-08-14 | 11 | 1,561,408,466 | yes |
| 2026-09-30 | 13F-HR | 0001398344-26-020103 | 2026-11-16 | 13 | 1,712,548,933 | yes |

Example full URL: https://www.sec.gov/Archives/edgar/data/1671657/000139834426020103/0001398344-26-020103.txt

The CSVs in `holdings/` cover Q4 2023 through Q3 2026. Q3 2023 was used only to identify Q4 2023 entries and exits (Disney and Dollar General were sold; Danaher was new), and no CSV was saved for it.

## Other SEC filing types checked

- **Form N-PX: applies. Three filings read.**

  | Covers | Accession | Filed |
  |---|---|---|
  | Jul 2023 – Jun 2024 | 0001398344-24-016945 | 2024-08-30 |
  | Jul 2024 – Jun 2025 | 0001398344-25-017096 | 2025-08-29 |
  | Jul 2025 – Jun 2026 | 0001398344-26-014586 | 2026-08-14 |

  - These are say-on-pay votes only. Every vote was FOR management except an AGAINST on Sprout Social's say-on-pay on 2025-05-22.
  - Record-date share counts are useful as intra-quarter snapshots. Examples: Herc 477,676 (May 2024); AutoZone 29,458 (Dec 2024) and 28,722 (Dec 2025); Danaher 602,177 (May 2025); AppLovin 341,541 (June 2026); Booking 411,100.
  - URLs follow the same pattern, e.g. https://www.sec.gov/Archives/edgar/data/1671657/000139834426014586/0001398344-26-014586.txt
- **Schedule 13D / 13G: none found.** The CIK folder lists none in the period. Positions are far below 5% of any issuer, so none is expected.
- **Forms 3, 4 and 5: none found, and they don't apply.** Dorsey is not a 10% holder of anything it owns.
- **13F-HR/A and 13F-NT: none in the period.**
- **Form ADV Part 1: applies. Read.**
  - Filed 2026-03-24. CRD 169056, SEC 801-96175.
  - RAUM $1,445,270,658, all discretionary, across 9 accounts.
  - Clients: 3 pooled vehicles ($860,894,458), 5 charitable organisations ($569,241,670), 1 high-net-worth individual ($15,134,530).
  - 10 employees, 8 in investment roles.
  - $23.4M of RAUM belongs to non-US persons.
  - Separate-account mix: 99% exchange-traded equity, 1% cash.
  - Custodians and administrators: Northern Trust and BNY Mellon.
  - https://reports.adviserinfo.sec.gov/reports/ADV/169056/PDF/169056.pdf
  - Summary page: https://adviserinfo.sec.gov/firm/summary/169056
- **Form ADV Part 2A brochure: applies. Read.**
  - Dated 2026-03-24. Funds: Global Moat Fund LP, Global Moat Offshore Fund LP, DAM SIF I LP. Strategy of 10–15 global positions, separate accounts run pari passu with the funds.
  - Fees 1.00–1.25%, no performance fee, currency generally unhedged. AUM date label: see oddities.
  - https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1024609
- **Earlier ADV AUM.** The 2024 brochure's figure ("As of February 29, 2024 … $1,113,609,479") comes via the third-party aggregator https://www.9at.com/Adviser/801-96175, read 2026-11-19. I did not read the 2024 brochure itself on IAPD, because historical brochure versions weren't reachable via Exa.
- **Form D: applies. Read.**
  - **Global Moat Fund LP** (CIK 1636453):
    - D/A 0000950123-24-012172, filed 2024-12-04: cumulative sold $323,373,106, 51 investors. https://www.sec.gov/Archives/edgar/data/1636453/000095012324012172/0000950123-24-012172.txt
    - D/A 0001213900-25-118054, filed 2025-12-04: $323,378,106. https://www.sec.gov/Archives/edgar/data/1636453/000121390025118054/0001213900-25-118054.txt
    - Folder: https://www.sec.gov/Archives/edgar/data/1636453/
    - The April 2023 figure of about $321.9M comes via https://ledger.svi.solutions/filings/469459-global-moat-fund-lp
    - The fund raised essentially no new money in 2023–25.
  - **Global Moat Offshore Fund:** $20M (Dec 2024), via https://www.formds.com/investment-advisers/dorsey-asset-management. I did not locate the EDGAR filing itself.
  - **DAM SIF I LP** (CIK 1661112): the last Form D found is from 2017, at $176.1M. There is none in the period. ADV shows $614M in gross assets and 3 beneficial owners. Index pages: https://www.sec.gov/Archives/edgar/data/1661112/000139834417002699/0001398344-17-002699-index.html and https://13f.info/form-d/0001661112-dam-sif-i-lp
- **N-CSR and N-PORT: don't apply.** Dorsey runs no registered fund.

## The manager's own words and other sources

Listed in date order. All were read 2026-11-19 via Exa unless noted.

- **Manual of Ideas interview, July 2014** (launch-era philosophy): https://dorseyasset.com/wp-content/uploads/2016/08/Manual_Ideas_Interview_July-2014.pdf. A July 2012 interview is at the same path with "2012". I only skimmed both through search highlights.
- **Talks at Google, 2015:** https://www.youtube.com/watch?v=YFS5JBgz1Xc. Used for enduring philosophy only, via search highlights.
- **Website:** https://dorseyasset.com/, https://dorseyasset.com/what-we-do/, https://dorseyasset.com/who-we-are/ (undated pages).
- **LinkedIn company page** ("do not short, use leverage, or hedge currency exposure"): https://www.linkedin.com/company/dorsey-asset-management/. Read via search highlight without signing in.
- **Chit Chat Stocks, about 2024-09-25** (third-party discussion of the 13F; its "low turnover" claim is now outdated): https://pod.wave.co/podcast/chit-chat-stocks/what-10-super-investors-bought-and-sold-last-quarter-uber-msft-spot-and
- **Morningstar, *The Long View*, 2026-03-31.** Full transcript read and quotes re-verified. https://www.morningstar.com/podcasts/the-long-view/pat-dorsey-economic-moats-more
  - It covers PayPal "wrong-footed", the "too hard" bucket and mission-critical software, ASML "sat on it", "rebuy your portfolio every morning", and "bulk of our investors are nontaxable".
- **"Ten Lessons from Ten Years," 2026-05-31:** https://dorseyasset.com/wp-content/uploads/2026/06/ten-lessons-from-ten-years_pat-dorsey_good-investing_20260531.pdf
- **"Maximizing Moats" deck, June 2026** (about $1.7B at 2026-06-01; "Twelve positions currently, with 59% of capital in top five"): https://dorseyasset.com/wp-content/uploads/2026/06/maximizing-moats_reinvestment-runways-capital-allocation_june-2026.pdf
- **Capital Allocators EP.509, "The Nuances of Investing in Moats," published around early July 2026.**
  - Video: https://www.youtube.com/watch?v=P25Ahug2-eQ
  - Transcript read in full: https://www.usetranscribe.io/yt/P25Ahug2-eQ/investing-in-moats
  - Saved copy in my scratch directory.
  - It covers the 15% max and the 15-name hard cap, 6–7% starting sizes, sales mostly being errors, about 30–40% historically non-US, local common shares, ASML as largest position, Safran and Rolls work, Meta held since 2015, and about $1.5B with 12 stocks.

**Corporate-action and deal confirmations:**
- Booking split: 8-K via https://www.stocktitan.net/sec-filings/BKNG/8-k-booking-holdings-inc-reports-material-event-e738c601b9d7.html and https://www.sec.gov/Archives/edgar/data/1075531/000095015726000465/ex3-1.htm
- Sunbelt scheme effective: https://ir.sunbeltrentals.com/news-events/press-releases/detail/111/sunbelt-rentals-holdings-inc---effectiveness-of-the-scheme-of-arrangement
- Sunbelt NYSE trading start: https://ir.sunbeltrentals.com/news-events/press-releases/detail/96/sunbelt-rentals-shares-begin-trading-on-new-york-stock-exchange
- Smartsheet close: https://www.smartsheet.com/content-center/news/blackstone-and-vista-equity-partners-complete-acquisition-smartsheet
- Enovis still independent in 2026: https://ir.enovis.com/news-releases/news-release-details/enovis-announces-first-quarter-2026-results
- Herc/H&E deal, 2025-02-18: https://www.investing.com/news/stock-market-news/herc-stock-tumbles-after-overthetop-bid-for-he-93CH-3875296
- Adobe/Semrush, 2025-11-19, $12 cash: https://news.adobe.com/news/2025/11/adobe-to-acquire-semrush

**Third-party 13F trackers.** I looked at these but did not rely on them for any number. Some misread Booking and Sunbelt.
- https://dataroma.com/m/hist/p_hist.php?f=DA
- https://13f.info/manager/0001671657-dorsey-asset-management-llc
- https://valuesider.com/guru/pat-dorsey-dorsey-asset-management/history

## Looked for, not found

- **Dorsey client letters, 2023–26.** Several searches found none. They exist, since Morningstar quotes "your most recent letter", but they don't circulate publicly. This is the biggest gap: most trades have no stated reason.
- **Any Dorsey statement on:**
  - the AppLovin round trip in 2024, or the re-entry in 2026;
  - Ashtead or Sunbelt;
  - AerCap, Booking, Uber, S&P Global, Live Nation, Royalty Pharma, Veeva, Tyler or Axon specifically;
  - the exits of Herc, Upwork, Wix, Semrush, Sprout, Alphabet, AutoZone, Enovis and Danaher.
- **Identity of the non-13F holding(s).** Mid-2026 Dorsey cited 12 positions while the 13F showed 11.

## Problems hit

- **Large fetch saved to file.** The Capital Allocators transcript fetch (about 84KB) came back as a file. I parsed it locally, with no data loss.
- **No Exa failures, paywalls, sign-in walls or human-verification checks.** None was encountered or attempted.
- **EDGAR browse page avoided.** I worked from the archive folder listing instead, as the brief advised.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
