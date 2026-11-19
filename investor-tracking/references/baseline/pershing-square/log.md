# Pershing Square: research log (written 2026-11-19)

## Oddities

- **Filer change.**
  - Through Q1 2026 the 13F-HR came from Pershing Square Capital Management, L.P. (CIK 1336528, 028-11694).
  - For Q2 2026 and Q3 2026, PSCM filed a 13F-NT naming Pershing Square Inc. (CIK 2026053, 028-25746): "Holdings of this reporting manager are now included in the report of its public parent company."
  - CIK 2026053 was Pershing Square Holdco, L.P. until the April 2026 IPO, when it became Pershing Square Inc. (Nevada).
  - From Q2 2025 through Q1 2026 Holdco/PS Inc. filed separate one-row "13F COMBINATION REPORT"s listing PSCM as another manager. Each covered the 9,000,000 HHH shares Holdco bought directly on 2025-05-05.
- **How the quarterly CSVs were combined.**
  - Each quarterly CSV sums every filer and amendment covering that quarter, by CUSIP:
    - Q4 2024: original plus 13F-HR/A.
    - Q2 2025 through Q1 2026: PSCM plus Holdco/PS Inc.
    - Q2 2026: original plus 13F-HR/A.
  - Each filing was reconciled to its own cover page separately; see below.
- **Amendments.**
  - **Q4 2024 13F-HR/A (0001172661-25-001497, filed 2025-04-16).** Reveals a position omitted under confidential treatment from the original (whose cover flag isConfidentialOmitted = true): Hertz, 12,713,963 shares, $46,533,105.
  - **Q2 2026 13F-HR/A (0001172661-26-005426, filed 2026-11-16, amendment type "NEW HOLDINGS").**
    - Adds Pershing Square Inc. COM (CUSIP 71531U102), 184,289,699 shares, $6,055,759,509, other managers 3 and 4 (Pershing Square Partner Group, Pershing Square Management).
    - This is PS Inc.'s own stock held by insiders and management vehicles. It is not a portfolio investment.
    - The same row is in the Q3 2026 original at $10,309,165,762.
    - Interpretation: likely a correction once PS Inc. common became a listed 13(f) security. See profile.md.
- **Totals inflated by non-portfolio rows from Q2 2026.** The PS Inc. self-stake, PS Inc.'s directly held 9M HHH shares and its 4M-share PSUS seed are all included. pct_of_portfolio in the CSVs is computed against the full filed total, self-stake included, so it matches the raw filing. Ex-self totals:
  - Q2 2026: $19,465,692,772.
  - Q3 2026: $20,487,384,364.
- **Reconciliation.** All 20 filings reconciled exactly (row count and total value) to their cover pages. No mismatches.
- **Row types.** All rows in all quarters are SH. There are no PRN rows and no put/call rows.
- **Value scale.** Prompted by the coordinator's correction of 2026-11-19, I checked each quarter's implied per-share prices. Examples: Chipotle $2,287 at Q4 2023 (pre-split), Hilton $182, Restaurant Brands $78, Microsoft $513 at Q3 2026. All are real prices, so every quarter is in whole dollars and nothing was rescaled. The cover totals also match the summed rows exactly in every filing.
- **Splits and timing.**
  - Chipotle's 50-for-1 split (June 2024) shows as 743,984 shares in Q1 2024 becoming 28,815,165 in Q2 2024.
  - Brookfield Corp: shares go from 41,020,231 (Q3 2025) to 61,403,089 (Q4 2025), a ratio of 1.497. The implied price goes from $68.58 to $45.89. This is a 3-for-2 stock split (October 2025, from my prior knowledge; the ratio confirms it), net of a small trim, not a purchase.
  - No late filings: Q4 2025 (filed 2026-02-17) and Q3 2026 (filed 2026-11-16) landed on the next business day after a weekend or holiday deadline.
- **Other-manager column quirk in Q3 2026.** RBI is tagged "3,4,5" and the PSUS seed "1,2,3,4", the reverse of Q2's pattern. Probably a filing error.
- **Seaport rows.** Q3 2024 carries two Seaport rows: rights (812215101) and common (812215200). Both came from the HHH spin-off and the rights-offering backstop.
- **Cover flag.** "provideInfoForInstruction5" is Y from Q4 2023 through Q2 2024 and N afterwards.

## Reconciliation by filing

| Quarter | Filing | Rows (parsed/cover) | Total (parsed = cover) | Combined CSV rows / total |
|---|---|---|---|---|
| 2023-Q4 | PSCM HR | 8/8 | $10,396,017,618 | 8 / $10,396,017,618 |
| 2024-Q1 | PSCM HR | 7/7 | $10,761,092,093 | 7 / $10,761,092,093 |
| 2024-Q2 | PSCM HR | 9/9 | $10,411,823,523 | 9 / $10,411,823,523 |
| 2024-Q3 | PSCM HR | 11/11 | $12,916,077,581 | 11 / $12,916,077,581 |
| 2024-Q4 | PSCM HR + HR/A | 10/10 + 1/1 | $12,614,560,346 + $46,533,105 | 11 / $12,661,093,451 |
| 2025-Q1 | PSCM HR | 11/11 | $11,930,893,008 | 11 / $11,930,893,008 |
| 2025-Q2 | PSCM HR + Holdco | 11/11 + 1/1 | $13,729,120,533 + $607,500,000 | 11 / $14,336,620,533 (HHH summed) |
| 2025-Q3 | PSCM HR + Holdco | 11/11 + 1/1 | $14,643,293,767 + $739,530,000 | 11 / $15,382,823,767 |
| 2025-Q4 | PSCM HR + Holdco | 11/11 + 1/1 | $15,526,737,802 + $717,930,000 | 11 / $16,244,667,802 |
| 2026-Q1 | PSCM HR + PS Inc | 11/11 + 1/1 | $13,714,299,861 + $569,340,000 | 11 / $14,283,639,861 |
| 2026-Q2 | PS Inc HR + HR/A | 15/15 + 1/1 | $19,465,692,772 + $6,055,759,509 | 15 / $25,521,452,281 (two HHH rows summed) |
| 2026-Q3 | PS Inc HR | 17/17 | $30,796,550,126 | 16 / $30,796,550,126 (two HHH rows summed) |

The parsing script is at /tmp/claude-0/-home-user/e63fcd6d-0599-5972-896a-3d4b7157bae9/scratchpad/build_csv.py (scratch). Rows were transcribed from the parsed information tables.

## 13F filings read (index pages; the full .txt submission was read for each)

| Quarter | Filing | Accession | Filed | URL |
|---|---|---|---|---|
| 2023-Q4 | PSCM 13F-HR | 0001172661-24-001556 | 2024-02-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266124001556/0001172661-24-001556-index.html |
| 2024-Q1 | PSCM 13F-HR | 0001172661-24-002519 | 2024-05-15 | https://www.sec.gov/Archives/edgar/data/1336528/000117266124002519/0001172661-24-002519-index.html |
| 2024-Q2 | PSCM 13F-HR | 0001172661-24-003511 | 2024-08-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266124003511/0001172661-24-003511-index.html |
| 2024-Q3 | PSCM 13F-HR | 0001172661-24-005218 | 2024-11-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266124005218/0001172661-24-005218-index.html |
| 2024-Q4 | PSCM 13F-HR | 0001172661-25-001119 | 2025-02-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266125001119/0001172661-25-001119-index.html |
| 2024-Q4 | PSCM 13F-HR/A | 0001172661-25-001497 | 2025-04-16 | https://www.sec.gov/Archives/edgar/data/1336528/000117266125001497/0001172661-25-001497-index.html |
| 2025-Q1 | PSCM 13F-HR | 0001172661-25-002315 | 2025-05-15 | https://www.sec.gov/Archives/edgar/data/1336528/000117266125002315/0001172661-25-002315-index.html |
| 2025-Q2 | PSCM 13F-HR | 0001172661-25-003509 | 2025-08-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266125003509/0001172661-25-003509-index.html |
| 2025-Q2 | Holdco 13F-HR (combination) | 0001172661-25-003512 | 2025-08-14 | https://www.sec.gov/Archives/edgar/data/2026053/000117266125003512/0001172661-25-003512-index.html |
| 2025-Q3 | PSCM 13F-HR | 0001172661-25-005039 | 2025-11-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266125005039/0001172661-25-005039-index.html |
| 2025-Q3 | Holdco 13F-HR (combination) | 0001172661-25-005115 | same period, date not recorded | https://www.sec.gov/Archives/edgar/data/2026053/000117266125005115/0001172661-25-005115-index.html |
| 2025-Q4 | PSCM 13F-HR | 0001172661-26-001091 | 2026-02-17 | https://www.sec.gov/Archives/edgar/data/1336528/000117266126001091/0001172661-26-001091-index.html |
| 2025-Q4 | Holdco 13F-HR (combination) | 0001172661-26-001095 | same period, date not recorded | https://www.sec.gov/Archives/edgar/data/2026053/000117266126001095/0001172661-26-001095-index.html |
| 2026-Q1 | PSCM 13F-HR | 0001172661-26-002336 | 2026-05-15 | https://www.sec.gov/Archives/edgar/data/1336528/000117266126002336/0001172661-26-002336-index.html |
| 2026-Q1 | PS Inc 13F-HR (combination) | 0001172661-26-002339 | same period, date not recorded | https://www.sec.gov/Archives/edgar/data/2026053/000117266126002339/0001172661-26-002339-index.html |
| 2026-Q2 | PSCM 13F-NT | 0001172661-26-003777 | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1336528/000117266126003777/0001172661-26-003777-index.html |
| 2026-Q2 | PS Inc 13F-HR | 0001172661-26-003790 | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/2026053/000117266126003790/0001172661-26-003790-index.html |
| 2026-Q2 | PS Inc 13F-HR/A | 0001172661-26-005426 | 2026-11-16 | https://www.sec.gov/Archives/edgar/data/2026053/000117266126005426/0001172661-26-005426-index.html |
| 2026-Q3 | PS Inc 13F-HR | 0001172661-26-005427 | 2026-11-16 | https://www.sec.gov/Archives/edgar/data/2026053/000117266126005427/0001172661-26-005427-index.html |
| 2026-Q3 | PSCM 13F-NT | 0001172661-26-005462 | 2026-11-16 | https://www.sec.gov/Archives/edgar/data/1336528/000117266126005462/0001172661-26-005462-index.html |

Archive listings used: https://www.sec.gov/Archives/edgar/data/1336528/ and https://www.sec.gov/Archives/edgar/data/2026053/. The 2026053 listing was stale; its latest entry was 2026-08-25. The November 2026 accessions given in the brief still resolved by direct URL.

## Other SEC filings (per the 2026-11-19 addition)

**Schedule 13D/A.** These are filed under PSCM's CIK 1336528. I read the ones marked "read"; the others I saw only as index entries.
- Restaurant Brands (QSR)
  - Amendment 2, 0000950170-24-050065, event 2024-04-29, **read**. A percentage-only change from the share count, with no trades. 23,348,135 shares plus exchangeable units; 7.5% for the funds, 8.5% including Ackman. https://www.sec.gov/Archives/edgar/data/1336528/000095017024050065/form_13da_qsr_04.29.24.htm
  - Amendment 5, 0001140361-26-020328, event 2026-05-06, filed about 2026-05-08, **read**. Adds PSUS and PS Inc. as reporting persons. 24,126,097 common, plus 2,652,778 shares under forward purchase contracts (PSUS), plus 357,841 exchangeable units: 27,136,716 shares, 7.8%. PSUS directly holds 1,860,000 common plus the forwards. https://www.sec.gov/Archives/edgar/data/1336528/000114036126020328/xslSCHEDULE_13D_X01/primary_doc.xml
- Howard Hughes (HHH)
  - 0000950170-24-001844 (Jan 2024), 0001193125-24-147209, 0001193125-24-181173 (July 2024, exhibits 99.19/99.20), 0000930413-24-002192, 0000930413-24-002260: index pages seen, not read in full.
  - 0000930413-25-000067 (2025-01-13): **read** exhibit 99.22, the $85/share proposal and the "modern-day Berkshire Hathaway" letter. https://www.sec.gov/Archives/edgar/data/1336528/000093041325000067/c111204_ex99-22.htm
  - 0001140361-25-005030, -006650, -008430, -012557, -013876, -016521: 2025 HHH 13D/As, index only.
  - Amendment 29, 0001140361-25-017784, event around 2025-05-05: **read**. Item 4 covers the $900M purchase of 9M shares at $100, the Services Agreement ($3.75M a quarter plus a variable fee), the 47% ownership cap and 40% voting cap, and board arrangements. https://www.sec.gov/Archives/edgar/data/1336528/000114036125017784/xslSCHEDULE_13D_X01/primary_doc.xml
  - 0001140361-25-029622 and 0001140361-25-046218 (late 2025; the latter is probably the Vantage announcement and equity commitment letter, Exhibit 99.39): index only.
  - Amendment 33, 0001140361-26-024479, event 2026-06-04: **read**. The Vantage acquisition closed (about $2.1B), with $1.0B of Series A non-voting exchangeable perpetual preferred bought by PSH. 27,852,064 shares = 46.7%. PS HHH Holdings LLC holds the 9M (15.1%). https://www.sec.gov/Archives/edgar/data/1336528/000114036126024479/xslSCHEDULE_13D_X01/primary_doc.xml
- Seaport Entertainment: 0000950170-24-109381 and 0000950170-24-116421 (2024), index only.
- **Schedule 13G:** none found in PSCM's folder for the period. That is consistent with Pershing holding large stakes as 13D filers.

**Forms 3/4/5.**
- Form 3, 0000950170-24-084732 (2024-07-18, HHH-related): index only.
- Form 4, 0001140361-26-016494, transaction 2026-04-21: **read**. The issuer is Pershing Square SPARC Holdings, Ltd. A J-code transfer of about 1.8% of SPARC Sponsor membership interests from Pershing Square, L.P. to PS Redemption, L.P., tied to a special redemption on 2026-04-21. No change in aggregate holdings. Not a portfolio trade. https://www.sec.gov/Archives/edgar/data/1336528/000114036126016494/xslF345X05/form4.xml
- Form 3, 0001140361-26-017583 (2026-04-28): PSCM as insider of PSUS, index only.
- No Form 5s seen.
- No Form 4s for open-market trades in portfolio names were found. Pershing is a 10% holder only of HHH, and that block did not trade.

**Form N-PX.**
- 0001438934-24-001199 (PSCM, filed 2024-08-29, 12 months to 2024-06-30): **read**. Say-on-pay votes FOR at Chipotle, Hilton, HHH, RBI Inc. and the RBI LP units (381,005 units). https://www.sec.gov/Archives/edgar/data/1336528/000143893424001199/votetable.xml
- 0001438934-25-001297 (PSCM, filed 2025-08-21, 12 months to 2025-06-30): **read**. https://www.sec.gov/Archives/edgar/data/1336528/000143893425001297/0001438934-25-001297.txt
  - FOR at Brookfield, CP, Chipotle, Hertz, Hilton, RBI (shares and LP units), Uber and UMG (83,348,648 shares).
  - **AGAINST Nike** say-on-pay (meeting 2024-09-10, 3,040,132 shares). This is the only AGAINST in three years.
- 0001438934-26-001601 (PSCM, filed 2026-08-25, 12 months to 2026-06-30, PS Inc. listed as another manager): **read**. https://www.sec.gov/Archives/edgar/data/1336528/000143893426001601/0001438934-26-001601.txt
  - FOR at Alphabet, Amazon, Hertz, HHH, RBI and Uber; Uber's say-on-pay frequency set to 1 year.
  - AGAINST a Meta shareholder proposal for annual say-on-pay, i.e. with management.
  - PS Inc.'s 9M HHH shares were voted partly in proportion to other holders under the 40% voting cap; the footnote cites a Voting Proxy Agreement dated 2025-08-05.
  - Vote counts equal record-date holdings, e.g. Amazon 11,451,981 and Uber 29,958,771, the same as the Q1 2026 13F.
- 0001438934-26-001592 (PS Inc., filed 2026-08-25): **read**. A notice report only; its votes are reported by PSCM (028-11694).
- 0001438934-26-001590 (PSUS, filed 2026-08-25): **read**. A fund notice report with no votes reported.

**Form ADV.**
- Part 1 PDF (other-than-annual amendment, 2026-06-03), **read**: https://reports.adviserinfo.sec.gov/reports/ADV/132982/PDF/132982.pdf
  - RAUM $25,061,606,673 across 5 discretionary accounts, about $18.2B attributable to non-US persons.
  - 48 employees, 11 in investment functions.
  - Private funds: PSH, gross assets $17.88B, 527 beneficial owners, 28% owned by related persons; Pershing Square International $346.8M; Pershing Square, L.P. $1.13B; PS Redemption, L.P. $25.4M.
  - Lists the @BillAckman, @PershingSquare and @pscmnews X accounts and pershingsquareinc.com.
- Part 2A brochure (June 3, 2026): **read in targeted sections** (Items 2, 4, 5 on RAUM, allocation, rebalancing and cross-trades, and the derivatives and strategy text), not every page. https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1047158
  - PSLP, PS International and PSH: "typically 8 to 12 core investments". PSUS: "12 to 15 core investments", because of 1940-Act and RIC diversification rules.
  - Allocation targets count equity forwards and other delta-one derivatives. Holdings may be "in different proportions between PSUS and the other Core Funds".
  - The 1940 Act restricts PSUS cross-trades and joint transactions with affiliates. The legacy funds rebalance among themselves.
  - Total return swaps are used "to manage regulatory, tax, legal or other issues", not for leverage.
  - Total AUM including HHH: $33.7B as of 2026-05-01, of which $9.5B is HHH, non-discretionary. Ackman owns 25–50% of PS shares, with voting capped below 25%.
  - Part 2B names Ackman, Ryan Israel and Ben Hakim (not read in full).
- adviserinfo.sec.gov/firm/summary/132982 returned an empty JavaScript shell through Exa.

**Form D.** Pershing Square International, Ltd. (CIK 1324919, file 021-105156) files an annual D/A. The 2026-06-16 (0001324919-26-000001) and 2025-06-09 (0001324919-25-000003) amendments both show $2,901,321,627 cumulative sold since 2005 and 200 investors, unchanged. That means no new private-fund raising. Read via the EDGAR company page and FilingFlow summaries, not the primary XML. The Pershing Square, L.P. Form D (021-190142) was not read. Form Ds do not explain any flows in this period.

**PSUS (CIK 2002660) N-PORT and N-CSRS.**
- NPORT-P 0001410368-26-088161 (period 2026-06-30, filed 2026-08-28): **read**. https://www.sec.gov/Archives/edgar/data/2002660/000141036826088161/0001410368-26-088161.txt
  - Net assets $4.59B. Direct shares: AMZN 1,589,900; BN 4,870,093; META 374,541; MSFT 549,096; QSR 1,860,000; UBER 3,141,090; NFLX 3,156,394; V 749,323; MA 495,000; SPGI 578,128; FNMA 12,263,177; FMCC 8,980,793.
  - Plus 35.8% in a BlackRock Treasury money-market fund, a Goldman Treasury fund, and $600M of T-bills (13.0%).
  - Equity forwards ("equity-performance leg", expiring May 2029): META $328.6M notional (Nomura), MSFT $401.9M (UBS), QSR $248.5M (Nomura), UBER $334.1M (UBS), BN $276.4M (UBS).
- N-CSRS 0001193125-26-360100 (semi-annual to 2026-06-30, filed 2026-08-21): **read** (manager's report, exposure table, forwards schedule, derivatives notes). https://www.sec.gov/Archives/edgar/data/2002660/000119312526360100/d87027dncsrs.htm
  - Exposure table, shares plus forwards: MSFT 1,521,596 (12.4%), UBER 7,634,090, META 913,501, BN 10,813,093, AMZN 1,589,900, QSR 5,040,478 and others; total exposure 85.9%.
  - Forwards total $1.59B notional with $122.7M unrealized loss; $502M of T-bills pledged as collateral.
- The PSUS Q3 2026 N-PORT (period 2026-09-30) was not yet in the archive listing (latest entry 2026-10-06); it is likely due around late November 2026.
- Other PSUS entries seen but not read: 0001193125-26-415861 (2026-10-06, a Section 16 ownership form), and the April–May 2026 IPO and registration filings.

**PSH 2026 interim report (H1 2026, primary).** **Read** (manager's report, exits, attribution, fair-value note, subsidiaries). https://assets.pershingsquareholdings.com/wp-content/uploads/2026/08/13002306/Pershing-Square-Holdings-Ltd.-June-2026-Interim.pdf
- NAV −12.6% for H1 2026 against the S&P +10.2%.
- "We exited our investments in Universal Music Group and Alphabet during the six-month period ended June 30, 2026, and exited Hertz in July 2026."
- Cash $201M at June 30, 2026, down from $1.14B.
- Derivative liabilities $94.6M: total return swaps $93.1M and currency forwards $1.5M. The TRS underlyings are not named in the parts I read.
- The HHH preferred ($1.02B) is held through 14 Cayman subsidiaries.
- H1 attribution: UMG −2.6%, Fannie −2.8%, Freddie −2.7%, Hertz −1.1% (through August 11).

**Prospectus and 10-Q (PS Inc.).**
- 424B4: https://www.sec.gov/Archives/edgar/data/2026053/000114036126018103/ny20040230x30_424b4.htm. Management owned 63.93% of PS Inc. and ManagementCo held 74.73% of the vote; about 400M shares outstanding.
- S-1/A: https://www.sec.gov/Archives/edgar/data/2026053/000114036126016419/ny20040230x28_s1a.htm
- PS Inc. 10-Q for 2026-06-30: https://www.sec.gov/Archives/edgar/data/2026053/000119312526349628/ps-20260630.htm (skimmed)
- PSUS FWP: https://www.sec.gov/Archives/edgar/data/2002660/000114036126008625/ny20064799x2_fwp.htm

## Manager's own words (in date order)

- PSH 2023 Annual Report (March 2024): https://assets.pershingsquareholdings.com/2024/03/22201541/Pershing-Square-Holdings-Ltd.-2023-Annual-Report.pdf
- PSH H1 2024 interim letter (August 2024), via Seeking Alpha: https://seekingalpha.com/article/4716465-pershing-square-holdings-h1-2024-letter-to-shareholders. A PDF copy is hosted by MBW: https://www.musicbusinessworldwide.com/files/2024/08/Pershing-Square-Holdings-Ltd.-June-2024-Interim-1.pdf
- BusinessWire, 10% Holdco stake sale (2024-06-03): https://www.businesswire.com/news/home/20240603875090/en/Pershing-Square-Capital-Management-L.P.-Announces-Sale-of-10-Common-Equity-Interest-for-1.05-Billion-to-Strategic-Investors
- PSH 2024 Annual Report (March 2025), the main source for Brookfield, Uber, the Nike call-option conversion, UMG and the competitive-advantage passage: https://assets.pershingsquareholdings.com/2025/03/14150847/Pershing-Square-Holdings-Ltd.-2024-Annual-Report.pdf
- Ackman's Hertz post (2025-04-16/17), via Bloomberg https://www.bloomberg.com/news/articles/2025-04-17/ackman-says-pershing-has-amassed-a-19-8-stake-in-hertz and CNBC https://www.cnbc.com/2025/04/16/-hertz-surges-after-bill-ackman-takes-big-stake-in-the-rental-car-firm.html. I did not open the X post itself.
- Q3 2025 PSH call transcript (November 2025), the source for the Chipotle and Nike post-mortems and the Meta entry: https://seekingalpha.com/article/4846231-pershing-square-holdings-ltd-pshzf-q3-2025-earnings-call-transcript. Also https://finance.yahoo.com/quote/PSH.L/earnings/PSH.L-Q3-2025-earnings_call-383321.html/
- PSH 2025 Annual Report (February 2026), covering the Hilton exit, 2025 attribution, and Fannie/Freddie: https://assets.pershingsquareholdings.com/wp-content/uploads/2026/02/18175039/Pershing-Square-Holdings-Ltd.-2025-Annual-Report.pdf
- 2026 Annual Investor Presentation (February 2026): https://assets.pershingsquareholdings.com/wp-content/uploads/2026/02/11144917/2026-Annual-Investor-Presentation.pdf
- PS Inc. Q2 2026 letter (2026-08-12): https://pershingsquareinc.com/wp-content/uploads/2026/08/PS-Inc.-2Q26-Letter-to-Shareholders.pdf
- PS Inc. Q3 2026 letter (2026-11-02): https://www.pershingsquareinc.com/wp-content/uploads/2026/11/Q3-26-PS-Inc-Letter-to-Shareholders.pdf
- PSUS Q3 2026 portfolio summary (November 2026): https://pershingsquareusa.com/wp-content/uploads/2026/11/PSUS-Portfolio-Summary.pdf
- IPO press releases: https://pershingsquareinc.com/pershing-square-announces-pricing-of-the-combined-ipo-of-pershing-square-usa-and-pershing-square-inc/ and https://pershingsquareinc.com/pershing-square-announces-the-closing-of-the-combined-ipo-of-pershing-square-usa-and-pershing-square-inc/

## Secondary sources (dated as published)

- Reuters 2024-08-14 (Nike, Brookfield): https://www.reuters.com/business/retail-consumer/ackmans-pershing-square-made-new-investments-nike-brookfield-filing-2024-08-14/
- Reuters 2025-05-22 (Amazon in, CP out): https://www.reuters.com/sustainability/sustainable-finance-reporting/ackmans-hedge-fund-pershing-square-bets-amazon-exits-canadian-pacific-2025-05-22/
- Institutional Investor (Chipotle and Nike exits, late 2025): https://www.institutionalinvestor.com/article/facing-losses-ackman-exits-chipotle-and-nike
- Reuters 2026-02-11 (Meta, Hilton exit): https://www.reuters.com/sustainability/sustainable-finance-reporting/ackmans-hedge-fund-pershing-square-bets-meta-exits-hilton-2026-02-11/
- Reuters 2026-04-29 (IPO, $5B): https://www.reuters.com/business/bill-ackmans-pershing-square-raises-5-billion-new-us-fund-2026-04-29/
- CNBC 2026-05-15 (Microsoft built in Q1): https://www.cnbc.com/2026/05/15/bill-ackman-says-he-built-microsoft-position-in-first-quarter.html
- Reuters 2026-05-16 (Ackman X post on the Alphabet sale): https://www.reuters.com/business/bill-ackman-says-alphabet-stake-sale-not-bet-against-company-2026-05-16/
- WSJ (Microsoft stake): https://www.wsj.com/finance/investing/ackman-says-pershing-square-has-taken-new-stake-in-microsoft-b68120d9. Paywalled; headline only.
- Reuters 2026-08-13 (six new investments, H1 2026): https://www.reuters.com/business/media-telecom/ackman-unveils-six-new-investments-including-netflix-visa-mastercard-biggest-2026-08-13/
- Music Business Worldwide (UMG bid and exit): https://www.musicbusinessworldwide.com/bill-ackman-who-called-universal-music-one-of-the-best-businesses-we-have-ever-owned-steers-clear-of-music-in-pershing-square-stock-buying-splurge/
- Stocktwits (Hertz exit, "bungled equity offering", July 2026): https://stocktwits.com/news-articles/markets/equity/htz-stock-hit-hard-as-bill-ackman-s-pershing-square-walks-away-citing-bungled-equity-offering/cZoqmqsRJLt
- Seeking Alpha news (Q3 2026: Alcon added, Netflix up, Hertz out): https://seekingalpha.com/news/4673371-pershing-square-adds-alcon-increases-netflix-exits-hertz-among-q3-moves
- TipRanks/TheFly (Q3 2026 13F coverage, which reads the PS Inc. self-stake as a buy): https://www.tipranks.com/news/the-fly/pershing-boosts-stake-in-netflix-exits-hertz-position-thefly-news

## Problems and gaps

- The PSH 2026 interim report was read later (see above). It confirms the H1 figures previously taken from Reuters and the PS Inc. Q2 letter.
- I did not open Ackman's X posts directly. Quotes are as reported by Reuters, Bloomberg and CNBC. That includes the November 2025 Fannie/Freddie plan, which I know of only from press summaries.
- The Q2 2026 (August 13) call transcript was not located and read in full. The Hertz "asymmetric" characterisation is from secondary reporting.
- The Q2-to-Q3 2026 Microsoft and RBI share cuts are now largely reconciled. PSUS's economic exposure was unchanged, so the cuts came from the legacy funds, and in dollars they match the new ICE and Alcon buys. See profile.md section 5. Still unconfirmed: whether part moved into PSH total return swaps. No manager statement addresses it.
- I could not confirm the exact UMG exit mechanics from a primary source; MBW is secondary.
- Since closed: ADV Part 2A (read in targeted sections), the Form D (via summaries), PSUS N-PORT and N-CSRS (June 30), and the 2025 and 2026 N-PX. Still open: the Pershing Square, L.P. Form D, Part 2B in full, and the PSUS Q3 N-PORT (not yet filed or listed).
- WSJ was paywalled, so I used the headline only. No sign-ins or paywalls were attempted.
- Large Exa fetches persisted to local JSON and were read by slicing. No sec.gov fetch failed except the stale 2026053 archive listing noted above.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
