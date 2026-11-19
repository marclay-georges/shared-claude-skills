# Valley Forge Capital Management: research log

Written 2026-11-19. All web access was through Exa (web_search_exa / web_fetch_exa). Some items below were read directly from the text Exa returned with a search result rather than from a separate fetch; those are marked "via search result".

## Oddities, read these first

- **Twelve quarters, all originals.** There are no 13F-HR/A amendments and no 13F-NT notices for Q4 2023 to Q3 2026. All filings were made on time, in mid-February, May, August and November.
- **Reconciliation.** Row counts match the cover page in all twelve quarters. Summed value matches the cover-page total exactly in ten quarters. In 2024-Q2 and 2025-Q2 the rows sum to $1 more than the cover total (3,867,718,196 vs 3,867,718,195, and 4,527,265,517 vs 4,527,265,516). This is filer rounding, and the CSVs keep the row values as filed.
- **Clean format.** Every row is SH (no PRN), investment discretion SOLE, voting SOLE, no put/call, other-managers count 0, and no confidential treatment in any quarter. Each CUSIP appears once per quarter, so no summing was needed. Values are in whole dollars.
- **Address and signer changes.**
  - Q4 2023 cover page: Wayne, PA. From Q1 2024: Miami, FL. The flagship fund's Form D header still showed Wayne, PA in 2026.
  - Signer title: "Managing Partner" through Q1 2026, "Manager of the General Partner" from Q2 2026. The 2025 Form D used "Sole Voting Member of the General Partner". Kantesaria still controls the firm per the March 2026 ADV.
- **Name and accession quirks.**
  - The ASML issuer name changed from "ASML HOLDING N V" to "ASML HLDG NV" from Q2 2026 (same CUSIP N07059210, NY registry shares). TSMC is the sponsored ADR (874039100).
  - The 2024 and 2025 N-PX filings carry a filing agent's accession prefix (0001214659), but sit in VF's own CIK folder. The 2026 N-PX is under VF's own prefix.
  - Form D for 2024 was filed under VF's prefix (0001697868-24-000006), and other years under the fund's own CIK 1473337.
- **Former names:** Valley Forge Advisors, LLC, then Valley Forge Advisors, L.P., then Valley Forge Capital Management, LP (2017). 13F file number 028-17727.
- **Exits and sizes.** Exits within the period: Aspen Technology (Q4 2024), Equifax and MSCI (Q1 2026), Intuit (Q3 2026). Q3 2026 has 10 positions, the most in the period.
- **No splits** affected the held names in the period. Share counts are continuous.

## 13F-HR filings read (oldest first)

All were fetched as full-submission .txt files from the archive folder https://www.sec.gov/Archives/edgar/data/1697868/ (listing fetched 2026-11-19).

| Period | Accession | URL | Entries | Cover total ($) |
|---|---|---|---|---|
| 2023-12-31 | 0001697868-24-000002 | https://www.sec.gov/Archives/edgar/data/1697868/000169786824000002/0001697868-24-000002.txt | 8 | 3,518,395,510 |
| 2024-03-31 | 0001697868-24-000005 | https://www.sec.gov/Archives/edgar/data/1697868/000169786824000005/0001697868-24-000005.txt | 8 | 3,666,608,140 |
| 2024-06-30 | 0001697868-24-000007 | https://www.sec.gov/Archives/edgar/data/1697868/000169786824000007/0001697868-24-000007.txt | 8 | 3,867,718,195 |
| 2024-09-30 | 0001697868-24-000008 | https://www.sec.gov/Archives/edgar/data/1697868/000169786824000008/0001697868-24-000008.txt | 8 | 4,500,146,048 |
| 2024-12-31 | 0001697868-25-000001 | https://www.sec.gov/Archives/edgar/data/1697868/000169786825000001/0001697868-25-000001.txt | 9 | 4,539,792,227 |
| 2025-03-31 | 0001697868-25-000004 | https://www.sec.gov/Archives/edgar/data/1697868/000169786825000004/0001697868-25-000004.txt | 9 | 4,388,954,111 |
| 2025-06-30 | 0001697868-25-000005 | https://www.sec.gov/Archives/edgar/data/1697868/000169786825000005/0001697868-25-000005.txt | 9 | 4,527,265,516 |
| 2025-09-30 | 0001697868-25-000006 | https://www.sec.gov/Archives/edgar/data/1697868/000169786825000006/0001697868-25-000006.txt | 9 | 4,156,989,872 |
| 2025-12-31 | 0001697868-26-000001 | https://www.sec.gov/Archives/edgar/data/1697868/000169786826000001/0001697868-26-000001.txt | 9 | 4,411,308,632 |
| 2026-03-31 | 0001697868-26-000003 | https://www.sec.gov/Archives/edgar/data/1697868/000169786826000003/0001697868-26-000003.txt | 7 | 3,375,637,687 |
| 2026-06-30 | 0001697868-26-000005 | https://www.sec.gov/Archives/edgar/data/1697868/000169786826000005/0001697868-26-000005.txt | 7 | 3,116,388,059 |
| 2026-09-30 | 0001697868-26-000007 | https://www.sec.gov/Archives/edgar/data/1697868/000169786826000007/0001697868-26-000007.txt | 10 | 2,527,376,800 |

## Other SEC filings

**Form N-PX.** Three filings, all say-on-pay only.
- 0001214659-24-015524, filed 2024-08-29, year to 2024-06-30. https://www.sec.gov/Archives/edgar/data/1697868/000121465924015524/0001214659-24-015524.txt
- 0001214659-25-012972, filed 2025-08-28, year to 2025-06-30. https://www.sec.gov/Archives/edgar/data/1697868/000121465925012972/0001214659-25-012972.txt
- 0001697868-26-000006, filed 2026-08-27, year to 2026-06-30. https://www.sec.gov/Archives/edgar/data/1697868/000169786826000006/0001697868-26-000006.txt

Votes and shares voted are summarised in profile.md. The share counts are as of each meeting's record date, which gives intra-quarter checkpoints: FICO 780,172 in early 2025; Mastercard 1,282,808 for the 2026-06-16 meeting.

**Form ADV.**
- Part 1, annual amendment filed 2026-03-30, data at 2025-12-31. Fetched 2026-11-19 at https://reports.adviserinfo.sec.gov/reports/ADV/162953/PDF/162953.pdf. CRD 162953, SEC 801-110956. It gives RAUM of $4,447,808,128 in four pooled vehicles, with Schedule D 7.B.(1) private fund details. The first fetch at 60k characters cut off before the firm's own funds, so I re-fetched at 250k.
- Part 2A brochure dated 2026-03-30, via search result: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1032470. It covers fees, the sub-advisory relationship with a large financial institution, and the permitted instruments.
- Earlier ADVs were not read directly. The March 2024 BBH master figures come secondhand from https://ppli.com/hedge-funds/bbh-valley-forge-master-fund/ (via search result).

**Form D, Valley Forge Capital, L.P. (CIK 0001473337).** Read via search results.
- 0001473337-23-000002, 2023-08-21: cumulative sold $758.1M. https://www.sec.gov/Archives/edgar/data/1473337/000147333723000002/0001473337-23-000002.txt
- 0001697868-24-000006, 2024-07-18: $805.2M, 125 investors. Listed at https://13f.info/form-d/0001473337-valley-forge-capital-l-p
- 0001473337-25-000002, 2025-07-16: $935.7M, 142 investors, exemption now 3(c)(7). https://www.sec.gov/Archives/edgar/data/1473337/000147333725000002/0001473337-25-000002.txt
- 0001473337-26-000001, 2026-07-14: $1,156.1M, 147 investors. https://www.sec.gov/Archives/edgar/data/1473337/000147333726000001/0001473337-26-000001.txt; also https://capedge.com/filing/1473337/0001473337-26-000001/D-A

**Not read: the Form D for BBH Valley Forge Master Fund** (Form D file no. 021-1838264 per ADV). A search did not surface it, and I did not chase it further.

**Schedule 13D/13G: none.** VF's archive folder (2017–2026) lists only 13F-HR, N-PX and the one 2024 Form D, with no 13D or 13G. This is consistent with position sizes: the largest stake relative to shares outstanding is FICO at roughly 3–4% (my estimate), below the 5% threshold.

**Forms 3/4/5: do not apply.** VF is not a 10% holder of any issuer, and none were found.

**N-CSR/N-PORT: do not apply.** There is no registered fund.

## Manager's own words (oldest first)

- Value Investor Insight, "Standing Out", October 2019 (free). Via search result. https://valueinvestorinsight.com/Content_Free/investor-insight-standing-out-october-2019.aspx
- The Investor's Podcast, "Buffett's Core Principles", October 2021. Via search result; episode page only. https://www.theinvestorspodcast.com/episodes/buffetts-core-principles-w-dev-kantesaria/
- Good Investing Talks, interview recorded 2022, published 2023-01-26. Via search result. https://www.good-investing.net/2023/01/26/dev-kantesaria-what-is-your-formula-for-quality-investing/
- Grant's Current Yield, "Growth and Profitability", 2024-11-20. The episode page https://grantpub.libsyn.com/growth-and-profitability was fetched but has no transcript. The transcript was fetched from https://exa.ai/library/podcast/36jbmdd91r3/episode/920ykxmrzfb (also listed at https://podcasts.apple.com/za/podcast/growth-and-profitability/id1207583745?i=1000677675179). **This is the key source for his AI, ASML, Nvidia and TSMC views and his cash policy.**
- The Investor's Podcast TIP680, 2024-12-05. The page https://www.theinvestorspodcast.com/episodes/investing-in-exceptional-businesses-for-the-long-run-dev-kantesaria/ was fetched but truncated. The full transcript was fetched from https://exa.ai/library/podcast/9n0n4fg4c6z/episode/d84mjqxkgsk.
- University of Miami event, 2025-02-12. Event page only, no recording found. https://events.miami.edu/event/insights-from-the-hedge-fund-frontier-a-conversation-with-dev-kantesaria
- Firm website https://www.valleyforgecapital.com/ has contact details only.

## Secondary sources and news context (by date of event)

- Luis Pazmino substack, 2024-10-13 (2023 trades: Amazon, Adobe and Autodesk sold; ASML bought). Via search result. https://luisepazmino.substack.com/p/super-investor-series-dev-kantesaria
- Reuters, 2024-11-05, Emerson proposes $240/share for Aspen Tech. Via search result. https://www.reuters.com/markets/deals/emerson-proposes-acquire-remaining-shares-aspentech-2024-11-05/
- Chit Chat Stocks podcast profile, 2025-08-27 (secondary; about him, not with him). Via search result. https://podcasts.apple.com/us/podcast/dev-kantesaria-great-compounding-machines-that-crush/id1437766060?i=1000723692098
- Reuters, 2026-01-12, rate-cap call. https://www.reuters.com/business/finance/us-financial-stocks-fall-after-trump-calls-credit-card-rate-cap-2026-01-12/ — Investing.com, 2026-01-13. https://www.investing.com/news/stock-market-news/visa-and-mastercard-stock-falls-as-trump-doubles-down-on-fee-crackdown-4445207. Both via search result.
- WSJ live coverage, 2026-02-03 (Claude Cowork selloff). https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-02-03-2026/card/C97KvtPTsT9H3joFwS7C — Reuters, 2026-02-04. https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/ — Both via search result.
- Reuters, 2026-02-10, S&P Global guidance. Via search result. https://www.reuters.com/business/sp-global-forecasts-2026-profit-below-estimates-shares-plunge-2026-02-10/
- CoinCentral, March 2026, V/MA and stablecoins. Via search result. https://coincentral.com/how-visa-and-mastercard-are-responding-to-the-stablecoin-threat-in-2026/
- Economic Times (Reuters), 2026-04-22, GSEs accept VantageScore. Via search result. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-fico-shares-slide-as-freddie-mac-fannie-mae-begin-accepting-rival-vantagescore/articleshow/130450555.cms
- Alpha-File, "Valley Forge Capital: The Monopoly...", 2026-08-11. Fetched 2026-11-19. https://alpha-file.com/blog/valley-forge-capital-the-monopoly. This is the source of the −2.8% (2025) and −23% (Q1 2026) performance figures, with no primary source cited.
- Joseph Carlson summaries: Q2 2026 (redemption reading), https://reducer.xgoose.org/items/4167; Q3 2026, https://reducer.xgoose.org/items/14313. Both via search result.
- TIKR, September 2026, FICO −17% on the FHFA move. Via search result. https://www.tikr.com/blog/is-fair-isaac-stock-a-buy-after-its-17-mortgage-score-selloff
- Motley Fool, 2026-09-29. https://www.fool.com/investing/2026/09/29/why-fair-isaac-corporation-plunged-today/ — Kalkine. https://kalkine.com/news/financial/why-did-fair-isaac-nysefico-stock-plunge-as-fannie-mae-and-freddie-mac-move-to-one-pricing-grid — Yahoo. https://finance.yahoo.com/markets/stocks/article/fair-isaac-stock-plunges-20-after-fannie-and-freddie-open-door-to-fico-credit-score-rival-142841650.html — All via search result.
- Yahoo, October 2026, FICO Preferred Program. https://finance.yahoo.com/markets/stocks/articles/why-fair-isaac-corporation-fico-010247962.html — TradingView/StockStory, November 2026, FICO pauses buybacks. https://www.tradingview.com/news/stockstory:98a133676094b:0-fico-q3-cy2026-deep-dive-margin-compression-and-pricing-strategy-transition-overshadow-revenue-growth/ — Investing.com RBC downgrade. https://www.investing.com/news/analyst-ratings/rbc-capital-downgrades-fair-isaac-stock-rating-on-pricing-concerns-93CH-5002449 — All via search result.
- Traders Agency, November 2026, Q3 rotation commentary. https://tradersagency.com/blog/13f-season-reveals-a-major-portfolio-rotation-at-valley-forge-capital-while-other-super-investors-stay-the-course — Valuesider buys/sells page (post-quarter price moves, as seen mid-November 2026). https://valuesider.com/guru/dev-kantesaria-valley-forge-capital-management/buys-sells — Both via search result.

## Problems and gaps

- **No partnership letters found.** Searched for annual and quarterly letters, 2023–2026. Letters are referred to in interviews but none circulate publicly that Exa could find.
- **No primary statement on the 2026 trades.** I searched for 2025–2026 interviews, talks and letters explaining the Visa cut, the Q2 selling, or the Q3 AI-hardware buys and the Mastercard sale. I found none, so every stated reason for those trades in circulation is from commentators.
- **Paywalls and sign-ins.**
  - Value Investor Insight, "No Compromises", September 2024: premium, paywalled. Only the free summary was seen. https://valueinvestorinsight.com/Content_Premium/investor-insight-no-compromises-september-2024.aspx
  - Hedge Fund Alpha interview: sign-in required, not read. https://hedgefundalpha.com/profiles/interview-with-dev-kantesaria-valley-forge-capital-management/
  - FT article on Kantesaria (search result only): paywalled, not read. https://www.ft.com/content/48ec5657-c2e7-4111-a236-24a96a8d49e7
  - The Barron's May 2024 profile is known only from secondary citations and was not read.
- **Pages that didn't give the content.**
  - The TIP680 episode page was truncated, so the Exa library transcript was used.
  - The Grant's libsyn page has no transcript, so the Exa library transcript was used.
  - The ADV PDF was too large for one tool response, so the output was saved to a tool-results file and parsed locally with python3 -I.
- **Not read.**
  - The BBH Valley Forge Master Fund Form D.
  - ADV filings before March 2026, other than the secondhand PPLI figure.
  - The 2021 TIP episode and the 2019 VII piece were read only from search-result text, not fully fetched.
- **EDGAR.** The browse pages were not relied on; the archive folder was used. Direct curl to sec.gov is blocked by the proxy, as expected.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
