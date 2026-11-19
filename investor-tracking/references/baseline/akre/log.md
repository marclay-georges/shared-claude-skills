# Akre Capital Management — research log

Manager: Akre Capital Management LLC, CIK 0001112520, 13F file no. 028-06599, CRD 109242, Middleburg, VA.
Period covered: 13F-HR for Q4 2023 through Q3 2026 (12 quarters).
Written 2026-11-19 by a helper subagent. All EDGAR material was read through Exa (direct sec.gov access is blocked here).

## Odd things first

1. **Q1 2024 was amended.** Original 13F-HR 0001112520-24-000010 (filed 2024-05-13) had 20 rows, $12,087,745,994. A 13F-HR/A, 0001112520-24-000012 (filed 2024-05-23, "Amendment No. 1", amendment type NEW HOLDINGS), re-filed the full table with 21 rows, $12,089,164,350. The only addition is SOPHiA Genetics (CUSIP H82027105), 287,699 sh, $1,418,356. `holdings/2024-Q1.csv` uses the amended table. No other amendments in the period.
2. **All 12 quarters reconcile exactly** to the cover-page row count and total value (difference $0 every quarter). Values are whole dollars in every quarter, including 2023-Q4 and 2024-Q1 (checked after the coordinator's 2026-11-19 note that some filers still reported in thousands then): cover totals run $11.9B → $4.4B with no 1,000x break between adjacent quarters, and value ÷ shares gives real market prices in each quarter (e.g. Mastercard $426.5 in 2023-Q4, $481.6 in 2024-Q1, $551.5 in 2026-Q3). No scaling applied. Every row is SH (no PRN). One option line exists: Salesforce CALL, 100,000 underlying shares, in Q1, Q2 and Q3 2026. It is kept as its own row (put_call = Call) and its value counts in the total, as the filing reports it. No duplicate CUSIP rows needed summing except where noted in the CSV build (none affected totals).

   | Quarter | Accession | Filed | Rows | Total value |
   |---|---|---|---|---|
   | 2023-Q4 | 0001112520-24-000006 | 2024-02-09 | 18 | $11,884,542,493 |
   | 2024-Q1 | 0001112520-24-000012 (13F-HR/A; original -24-000010) | 2024-05-23 (orig. 05-13) | 21 | $12,089,164,350 |
   | 2024-Q2 | 0001112520-24-000014 | 2024-08-13 | 19 | $11,366,082,231 |
   | 2024-Q3 | 0001112520-24-000025 | 2024-11-13 | 18 | $12,017,990,024 |
   | 2024-Q4 | 0001112520-25-000003 | 2025-02-13 | 18 | $11,561,087,092 |
   | 2025-Q1 | 0001112520-25-000015 | 2025-05-13 | 18 | $10,400,552,669 |
   | 2025-Q2 | 0001112520-25-000019 | 2025-08-14 | 19 | $10,210,810,464 |
   | 2025-Q3 | 0001112520-25-000029 | 2025-11-13 | 19 | $10,030,655,183 |
   | 2025-Q4 | 0001112520-26-000008 | 2026-02-13 | 18 | $9,120,742,965 |
   | 2026-Q1 | 0001112520-26-000009 | 2026-05-14 | 20 | $6,134,537,825 |
   | 2026-Q2 | 0001112520-26-000014 | 2026-08-14 | 20 | $5,122,536,308 |
   | 2026-Q3 | 0001112520-26-000022 | 2026-11-13 | 21 | $4,424,875,808 |

3. **Stock splits inside the period (share counts jump, not trades):**
   - O'Reilly Automotive 15-for-1, record 2025-06-02, trading post-split 2025-06-10. Falls between the Q1 2025 (864,262 sh) and Q2 2025 (9,411,330 sh) filings. Split-adjusted, Q1 2025 = 12.96M, so Q2 2025 was a cut of about 27%, not a ten-fold purchase. Source: https://corporate.oreillyauto.com/investor-relations-information/stock-split-history/ and the company's split FAQ PDF (read 2026-11-19).
   - Brookfield Corporation 3-for-2 (stock dividend), record 2025-10-03, post-split trading 2025-10-10. Falls between Q3 2025 (19.22M sh) and Q4 2025 (26.84M sh). Split-adjusted Q3 2025 = 28.82M, so Q4 2025 was a cut of about 7%, not a 40% add. Source: Brookfield security history PDF, https://bn.brookfield.com/sites/brookfield-bn-v2/files/BN-IR-Master/Brookfield-Security-History/brookfield-security-history-2025.pdf, and press release of 2025-10-09 (read 2026-11-19).
   - ServiceNow's 5-for-1 split (late 2025) came before Akre's first purchase (Q1 2026), so it does not affect the series.
4. **Filer structure did not change, but the main client did.** The Akre Focus Fund (mutual fund, AKREX/AKRIX/AKRSX) converted into the Akre Focus ETF (ticker AKRE) on 2025-10-24/27. Same adviser, same CIK, same 13F filer. Retail and Supra classes were merged into Institutional on 2025-10-10 first. See profile for why this changes how to read share-count changes.
5. **"Other included manager" listed but not used.** Every cover page in the period lists one other included manager, Braddock Partners Offshore, LP (028-17748, CIK 0001697927), yet the other-manager column is blank on every holdings row. The Braddock private funds' holdings are therefore inside these numbers without being tagged. The June 2025 Schedule 13G on SOPHiA confirms Braddock vehicles hold at least that name.
6. **Format change:** a FIGI column appears in the information table from Q1 2024 on. No effect on the data.
7. **Timeliness:** every 13F filed on day 40–45 after quarter end. No 13F-NT, no confidential-treatment requests seen (cover pages show no confidential omission), no missing quarters. Signer on every 13F: Carolyn S. Hylton, Head Trader – Client Service Director.
8. **Adviser N-PX data quirk:** in the 2026 N-PX, the "shares voted" figure for CCC (frequency and say-on-pay) and Perimeter Solutions is 2,237,504, the same number as SOPHiA's voted shares in 2025, while the "shares on loan/held" column shows 4,980,004 and 250,000. Looks like a copy error in the filing. Not used for anything.

## Filings read — SEC, adviser CIK 0001112520

Folder listing: https://www.sec.gov/Archives/edgar/data/1112520/ (read 2026-11-19).

13F-HR / 13F-HR/A: the twelve accessions in the table above. For each I read the XSL-rendered information table and cover page, e.g. https://www.sec.gov/Archives/edgar/data/1112520/000111252026000022/xslForm13F_X02/infotable.xml and .../xslForm13F_X02/primary_doc.xml (same pattern for every accession folder: https://www.sec.gov/Archives/edgar/data/1112520/<accession without dashes>/). For 2023-Q4 through 2024-Q2 I read the full submission .txt files (e.g. https://www.sec.gov/Archives/edgar/data/1112520/000111252024000006/0001112520-24-000006.txt) and the index pages (e.g. https://www.sec.gov/Archives/edgar/data/1112520/000111252024000012/0001112520-24-000012-index.html).

Schedule 13G (the adviser files these; no 13D in the period):
- 0000919574-25-003801, filed 2025-06-27, SOPHiA Genetics SA, event date 2025-06-20, 3,719,140 sh = 5.6%. Filers: Akre Capital Management, Braddock Partners Offshore LP, Braddock Capital Offshore LLC; shared voting and dispositive power. https://www.sec.gov/Archives/edgar/data/1112520/000091957425003801/xslSCHEDULE_13G_X01/primary_doc.xml
- 0000919574-26-003207, filed 2026-05-15, CCC Intelligent Solutions Holdings, event date 2026-03-31, 30,313,000 sh = 5.2%, held for advisory clients, no single client over 5%. https://www.sec.gov/Archives/edgar/data/1112520/000091957426003207/xslSCHEDULE_13G_X01/primary_doc.xml
- No Schedule 13D found in the folder for the period. No 13G amendments found.

Forms 3/4/5: none found in the adviser's folder for the period. Akre is not a 10% holder of anything it reports (largest stake seen is 5.6% of SOPHiA). Not applicable.

Form N-PX (adviser's own say-on-pay report, institutional manager voting report):
- 0001112520-24-000019, filed 2024-08-27, year to 2024-06-30. https://www.sec.gov/Archives/edgar/data/1112520/000111252024000019/0001112520-24-000019.txt — Voted FOR on most; ABSTAIN (recorded as against management's recommendation) on American Tower (6.19M sh, 2024-05-22), DigitalBridge and Uber. Signed by Quinn Morris, Business Risk Manager.
- 0001112520-25-000024, filed 2025-08-28, year to 2025-06-30. https://www.sec.gov/Archives/edgar/data/1112520/000111252025000024/0001112520-25-000024.txt — FOR on all items, including American Tower, Constellation Software (43,120 sh), SOPHiA (Swiss pay votes), Airbnb, Brookfield. Signed Quinn Morris, Chief Compliance Officer.
- 0001112520-26-000019, filed 2026-08-26, year to 2026-06-30. https://www.sec.gov/Archives/edgar/data/1112520/000111252026000019/0001112520-26-000019.txt — FOR on all items (Copart, Visa, FICO, Moody's, Goosehead, Danaher 400 sh, O'Reilly, Constellation 54,418 sh, Roper, Verisk 273 sh, American Tower, CCC, Perimeter, Airbnb, Mastercard, CoStar during its activist fight); ABSTAIN on Berkshire Hathaway's two pay items.
- The share counts voted here are far below 13F totals (e.g. Visa 28,740), so this report covers only accounts where the adviser itself votes; the fund's votes are in the trust's N-PX (see below). The voted Danaher (400 sh) and Verisk (273 sh) in May 2026 suggest small residual holdings in client accounts after the 13F lines disappeared (13F threshold is not per-account, so this is consistent with de minimis leftovers; low importance).
- Proxy-table HTML pages (proxytable.html) returned "not found" through Exa; the .txt submissions were readable.

Form 40-APP (exemptive application filed by the trust with Akre as co-applicant, in the adviser's folder):
- 0000894189-25-001634, filed 2025-03-04 (application for an ETF share class of the mutual fund) and 40-APP/A 0000894189-25-002502, filed 2025-04-16. Index pages read: https://www.sec.gov/Archives/edgar/data/1112520/000089418925001634/0000894189-25-001634-index.html. Akre later dropped the share-class route in favour of a full conversion (etf.com, 2025-06-05; Bloomberg newsletter 2025-09-26, headline only).

Form 13F-NT, 13F-CTR: none in the period.

## Filings read — Akre Focus Fund / Akre Focus ETF (trust: Professionally Managed Portfolios, CIK 0000811030)

- N-CSR (annual, FY to 2023-07-31), 0000898531-23-000415: https://www.sec.gov/Archives/edgar/data/811030/000089853123000415/akre-ncsra.htm — annual letter (exited Salesforce, added Brookfield, trimmed CarMax; AMT at lowest valuation since 2017).
- N-CSR (FY to 2024-07-31), 0001133228-24-009298: https://www.sec.gov/Archives/edgar/data/811030/000113322824009298/affaf-efp9716_ncsr.htm — net assets $12.98B, 17 holdings, turnover 5%; eliminated Adobe and Lumine; Uber "exploratory position… pivoted to Airbnb"; Veralto spin-off shares sold.
- N-CSRS (half-year to 2025-01-31), 0001133228-25-003473: https://www.sec.gov/Archives/edgar/data/811030/000113322825003473/afff-efp14732_ncsrs.htm — redemption-in-kind sales of $942.7M in six months; fund holdings by name (including LVMH 154,617 sh, Topicus, Constellation).
- N-CSRS (half-year to 2026-01-31, first ETF report), 0001133228-26-004864, filed 2026-04-08: https://www.sec.gov/Archives/edgar/data/811030/000113322826004864/afe-efp23113_ncsrs.htm — net assets $8.48B, turnover 1%, full schedule (BN 21.16M, MA 2.05M, CSU 416,720, LVMH 429,539 = 3.3%, CRM 405k, NOW 720k, etc.), cash 2.9%.
- N-CSR (FY to 2026-07-31), 0001133228-26-013166, filed 2026-10-06: https://www.sec.gov/Archives/edgar/data/811030/000113322826013166/afe-efp27312_ncsr.htm — net assets $5.24B (from $12.48B); 1-yr −20.13% vs S&P +19.56%; ETF creations $417M vs redemptions $4.41B; in-kind realized gains $3.62B; turnover 5% ex in-kind; full schedule at 2026-07-31; no options held in the fund.
- Conversion documents (read in part): N-14/reorganization strategy doc https://www.sec.gov/Archives/edgar/data/811030/000089418925011387/akrefocusstrategyetf.htm; tax opinion https://www.sec.gov/Archives/edgar/data/811030/000089418925012778/a42akrefreorgtaxopinion.htm. Older context only: 497 supplements on PM changes, https://www.sec.gov/Archives/edgar/data/811030/000089418919008770/akre497knewpm.htm (2019) and https://www.sec.gov/Archives/edgar/data/811030/000089418914003388/akre_497e.htm (2014).
- **N-PORT-P (added 2026-11-19 at the coordinator's request).** The mutual fund is series S000026760 (classes AKREX C000080286, AKRIX C000080287, AKRSX C000159797). The ETF is a new series, S000089351 (class C000255872, AKRE). Both are under trust CIK 811030. I read Part B (net assets, monthly returns, monthly flow Item B.6) through the XSL view, e.g. https://www.sec.gov/Archives/edgar/data/811030/000119312526406412/xslFormNPORT-P_X01/primary_doc.xml. Holdings came from the .txt or the NPORT-EX schedule where noted:
  - 0001145549-24-019775 (period 2024-01-31, filed 2024-03-28): net assets $12.94B. Flows Nov–Jan: sold $0.90B, redeemed $1.76B, reinvested $0.35B.
  - 0001145549-24-040507 (2024-04-30, filed 2024-06-27): $12.13B; sold $0.66B, redeemed $1.26B. Schedule: https://www.sec.gov/Archives/edgar/data/811030/000114554924040507/pmp-akre2_nport.htm (seen in search only).
  - 0001145549-24-061728 (2024-07-31, filed 2024-09-27): $12.98B; sold $0.80B, redeemed $1.57B.
  - 0001145549-24-082738 and NPORT-P/A 0001145549-24-083415 (2024-10-31, both filed 2024-12-30): read the amendment. $12.66B; sold $0.51B, redeemed $1.01B.
  - 0001145549-25-023186 (2025-01-31, filed 2025-03-31): $12.69B; sold $0.69B, redeemed $1.54B, reinvested $0.47B.
  - 0001145549-25-045210 (2025-04-30, filed 2025-06-30): $11.90B; sold $0.75B, redeemed $1.18B.
  - 0000894189-25-009200 (2025-07-31, filed 2025-09-26; last mutual-fund N-PORT): $12.47B; sold $0.94B, redeemed $1.24B. Holdings read from the .txt, including CSU 433,400, Topicus 5.97M, LVMH 429,539, Airbnb 3,255,674, Danaher 1.61M, FICO 21,578, Copart 2.6M and AMT 200,987. Off-13F names were 20.4% of net assets; cash 6.1%.
  - 0000894189-25-019248 (2025-10-31, filed 2025-12-29; first ETF N-PORT): $10.41B. Aug–Oct: sold $5.67B, redeemed $6.49B (October includes the share-class merger), reinvested $0.39B. Schedule: https://www.sec.gov/Archives/edgar/data/811030/000089418925019248/akre.htm (CSU 416,720, Topicus 5.97M, LVMH 429,539 = 19.1% off-13F; Airbnb 3,255,674; Danaher 577,081; BN 25.58M; cash 4.3%).
  - 0000894189-26-009778 (2026-01-31, filed 2026-03-30): $8.54B; no creations; redemptions $1.14B.
  - 0001193125-26-287657 (2026-04-30, filed 2026-06-29): $6.41B; creations $0.29B, redemptions $1.60B. Schedule: https://www.sec.gov/Archives/edgar/data/811030/000119312526287657/akre2.htm (CSU 416,720, Topicus 5.97M, LVMH 206,922 = 20.0% off-13F; Airbnb 1,165,060; FICO 300,187; O'Reilly 1,619,099; cash 8.4%).
  - 0001193125-26-406412 (2026-07-31, filed 2026-09-29): $5.25B; creations $0.13B, redemptions $1.57B. Holdings from the .txt: CSU 310,679, Topicus 5,289,600, LVMH 242,964 = 22.5% off-13F; Airbnb 1,005,494; O'Reilly 699,156; cash 0.7%. Monthly returns: +1.52%, −3.47%, +7.97%.
  - Cross-check: November 2025–July 2026 ETF creations ($0.42B) and redemptions (about $4.3B plus late October) match the N-CSR's $417M and $4.41B.
  - The October 2023 and earlier N-PORTs were not read (before the period).
  - Filing list: https://www.sec.gov/cgi-bin/browse-edgar?CIK=S000026760&action=getcompany and https://www.sec.gov/cgi-bin/browse-edgar?CIK=C000255872&action=getcompany ; also https://capedge.com/fund/S000089351/filings (log-in wall past the first rows).
- Trust 497 supplement 0000894189-26-014273 (2026-05-01, "akreofficerupdate.htm"): changes to trust officers at the administrator (U.S. Bank). No change to the Akre portfolio manager. Read to rule out a PM change.
- Daily ETF holdings on akrefund.com were not read.
- **Fund N-PX (trust CIK 811030): not read.** Only the adviser's N-PX was read.

## Form ADV and Form D

- Form ADV Part 2A brochure dated 2026-03-30: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1034720 (read 2026-11-19). Key facts used: RAUM about $11.8B at 2025-12-31; fees (SMA 1.50%, $5M minimum; private funds 1.25% plus 20% incentive over a hurdle; ETF unitary 0.98%); strategy "focused / non-diversified", buy and hold.
- Form ADV Part 1, other-than-annual amendment dated 2026-06-04, read on the SEC adviser site: https://reports.adviserinfo.sec.gov/reports/ADV/109242/PDF/109242.pdf (read 2026-11-19). SEC file 801-57156; organized in Delaware.
  - RAUM $11,821,915,481 across 218 discretionary accounts; $290M for non-US clients.
  - Clients: 1 investment company $9.85B; 3 pooled vehicles $1.25B; 15 corporations $428M; 89 high-net-worth individuals $233M; 105 other individuals $38M; 6 charities $18M; 1 pension plan $1.3M.
  - 12 employees, 3 in investment functions.
  - Private funds (Section 7.B.(1)): a master-feeder. Braddock Partners LP (Delaware feeder; GAV $1,180,984,891; about 100 beneficial owners; $5M minimum; Form D file 021-106166) and Braddock Partners Offshore Ltd feed the master, Braddock Partners Offshore, LP (Cayman; GAV $1,251,944,781; about 107 owners; no Form D). Akre and related persons own about 47% of each.
  - Correction to my first pass: the aggregator figures summed GAVs across master and feeders (about $2.47B). The real private-fund pool is about $1.25B.
  - The Exa fetch truncated at about 75k characters, so Schedule A/B (owners) and the Offshore Ltd page were not reached. Ownership by Charles T. Akre Jr. (revocable trust) still rests on the aggregators and the brochure.
  - Aggregators first used: https://hedgemountain.com/firm/akre-capital-management-llc-109242/ and https://altstreet.investments/advisers/109242
- Form D on EDGAR (read 2026-11-19):
  - Braddock Partners, LP (CIK 0001406947, file 021-106166). D/A 0000919574-26-000556 (2026-01-30): first sale 1993-10-01; cumulative $343,930,893 sold; 198 investors; $5M minimum; 3(c)(7); signed by Charles T. Akre, Jr. as Managing Member of the GP (Braddock Capital Offshore, LLC). https://www.sec.gov/Archives/edgar/data/1406947/000091957426000556/0000919574-26-000556.txt. Prior in-period amendments: 0000919574-25-000753 (2025-01-31; $342.9M, 197 investors) and 0000919574-24-000612 (2024-02-01; $342.9M, 197). Filing list: https://www.sec.gov/cgi-bin/browse-edgar?CIK=1406947&action=getcompany&type=D
  - Braddock Partners Offshore, Ltd. (CIK 0001407066, file 021-106191). D/A 0000919574-26-000552 (2026-01-30): https://www.sec.gov/Archives/edgar/data/1407066/000091957426000552/0000919574-26-000552-index.html (index read). Amount series from https://13f.info/form-d/0001407066-braddock-partners-offshore-ltd: cumulative $85.9M (2024-02-01) → $98.4M (2025-01-31) → $100.9M (2026-01-30); first sale 2004-01-01.
  - Braddock Partners Offshore, LP (master, CIK 0001697927): the ADV says no Form D.
  - Use for the 13F: the private funds took in little new money (about $15M of cumulative sales across 2024–2025), so they are not a source of the flows; the ETF is.

## Manager's own words — read in date order

| Date | Source | URL |
|---|---|---|
| Sept 2023 | Annual letter in N-CSR | https://www.sec.gov/Archives/edgar/data/811030/000089853123000415/akre-ncsra.htm (also https://scuttlebutt.co/letters/akre-focus-fund-annual-report-fiscal-year-ended-july-31-2023-ffd332) |
| Jan 2024 | Q4 2023 commentary | https://seekingalpha.com/article/4663865-akre-focus-fund-q4-2023-commentary |
| Apr 2024 | Q1 2024 commentary (PDF) | https://www.akrefund.com/wp-content/uploads/2024/04/Akre-Focus-Fund-Quarterly-Commentary-2024-Q1.pdf |
| Jul 2024 | Q2 2024 commentary | https://hedgefundalpha.com/investor-letters/akre-focus-fund-2q24-commentary/ |
| Oct 2024 | Q3 2024 commentary (review) | https://finance.yahoo.com/news/akre-capitals-akre-focused-fund-195605166.html |
| Jan 2025 | Q4 2024 commentary | https://seekingalpha.com/article/4749930-akre-focus-fund-q4-2024-commentary |
| Apr 2025 | Q1 2025 commentary "Gravity's Rainbow" | https://seekingalpha.com/article/4774427-akre-focus-fund-q1-2025-commentary |
| Jun 2025 | Conversion announcement coverage | https://www.etf.com/sections/news/akre-capital-seeks-122b-mutual-fund-etf-conversion |
| Jul 2025 | Q2 2025 commentary | https://bsdpdfapi-production.up.railway.app/letters/file/ac7c81f9-cb26-494c-a879-a16b29f8e761/ ; review https://www.gurufocus.com/news/3002513/akre-capitals-akre-focus-fund-2ndquarter-2025-letter-a-review |
| Sept 2025 | "Why We Are Converting to an ETF" | https://seekingalpha.com/article/4831706-why-we-are-converting-to-an-etf |
| Oct 2025 | Q3 2025 commentary | https://bsdpdfapi-production.up.railway.app/letters/file/3fe6ba48-4494-47ad-aec7-93570081a51f/ |
| Oct 27 2025 | Conversion completed (press release) | https://www.globenewswire.com/news-release/2025/10/27/3174739/0/en/Akre-Capital-Completes-One-of-the-Industry-s-Largest-Mutual-Fund-to-ETF-Conversions.html |
| Dec 2025 | Animal Spirits "Talk Your Book: The Anti-AI Portfolio" (Neff; via show notes) | https://notescast.com/animal-spirits/episodes/talk-your-book-the-anti-ai-portfolio |
| Jan 15 2026 | Q4 2025 commentary | https://seekingalpha.com/article/4860088-akre-focus-fund-q4-2025-commentary |
| Apr 2026 | etf.com feature on Neff and AI | https://www.etf.com/sections/features/akre-etf-betting-market-wrong-ai |
| Apr 29 2026 | Q1 2026 commentary | https://seekingalpha.com/article/4896233-akre-focus-etf-q1-2026-commentary (summary also https://stonerecord.wang/detail/akre_capital_2026q1) |
| Aug 2026 | Q2 2026 commentary | https://seekingalpha.com/article/4953686-akre-focus-etf-q2-2026-commentary ; https://stonerecord.wang/en/detail/akre_capital_akre_focus_etf_quarterly_commentary_2026_q2 ; https://thehiddenvaluelab.substack.com/p/everyone-says-this-portfolio-is-an |
| Oct 20 2026 | Q3 2026 commentary | https://seekingalpha.com/article/4955395-akre-focus-etf-q3-2026-commentary (summary https://stonerecord.wang/detail/akre_capital_2026q3) |

Seeking Alpha pages were read as far as the free view shows; in most cases that was the full letter text or most of it.

## People and firm history sources

- Morningstar firm page and fund articles: https://www.morningstar.com/asset-management-companies/akre-BN00000BWH ; https://www.morningstar.com/funds/this-large-growth-fund-isnt-afraid-go-its-own-way ; https://www.morningstar.com/funds/active-asset-management-isnt-easy (read 2026-11-19). Used for: Neff sole PM since Sept 2023, Cerrone's departure, analysts Andrew Millette and Trey Tickner taking firm equity in January 2025, Parent rating Average (2025-11-17).
- Citywire, Oct 2023 downgrade on team turnover: https://citywire.com/ria/news/ratings-roundup-akre-and-blackrock-funds-downgraded-following-team-turnover/a2428978
- Trust 497 supplements (2014, 2019) for co-PM history (Neff and Saberhagen from 2014; Cerrone added 2019/2020).

## Market-event sources (for causes of price moves)

- Fair Isaac, Q3 2026: Bloomberg 2026-09-04 "FICO plunges 21%…" https://www.bloomberg.com/news/articles/2026-09-04/fico-plunges-21-credit-bureaus-fall-as-pulte-renews-criticism (headline/summary); WSJ live coverage 2026-09-29 https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-09-29-2026/card/CaKe2ib4EWs7jrmCWj71 ; Forbes 2026-09-30 https://www.forbes.com/sites/jimosman/2026/09/30/fico-stock-crashed-27-a-mortgage-price-war-could-send-it-lower/ ; Motley Fool 2026-09-29 https://www.fool.com/investing/2026/09/29/why-fair-isaac-corporation-plunged-today/ ; Yahoo https://finance.yahoo.com/markets/stocks/article/fair-isaac-stock-plunges-20-after-fannie-and-freddie-open-door-to-fico-credit-score-rival-142841650.html and https://finance.yahoo.com/markets/stocks/articles/fair-isaac-fico-stock-dropped-101121370.html ; Benzinga https://www.benzinga.com/trading-ideas/movers/26/09/62052695/fico-stock-hits-multi-year-low-whats-happening ; Proactive https://www.proactiveinvestors.com/companies/news/1099315/fair-isaac-drops-26-as-vantagescore-gains-mortgage-pricing-parity-1099315.html (all read 2026-11-19).
- Splits: O'Reilly and Brookfield pages cited in "Odd things" above.

## Third-party 13F trackers (cross-checks only, not used as facts)

- Seeking Alpha "Tracking Akre Capital Management Portfolio" updates: https://seekingalpha.com/article/4908149-tracking-akre-capital-management-portfolio-q1-2026-update ; https://seekingalpha.com/article/4871193-tracking-akre-capital-management-portfolio-q4-2025-update ; https://seekingalpha.com/article/4816936-akre-capital-management-portfolio-q2-2025-update ; https://kr.seekingalpha.com/article/4786878-tracking-akre-capital-management-portfolio-q1-2025-update ; https://kr.seekingalpha.com/article/4739155-tracking-akre-capital-management-portfolio-q3-2024-update
- GuruFocus on the AMT cut: https://www.gurufocus.com/news/2859594/american-tower-corp-sees-significant-reduction-in-akre-capital-managements-portfolio
- https://www.thevalueinvestor.org/p/transactions-of-chuck-akre-q1-2025 ; https://finance.yahoo.com/news/chuck-akre-adjusts-portfolio-major-003607094.html (note: these label the 13F "Chuck Akre's" portfolio; he has not been PM since end-2020).

## Problems and gaps

- **Paywall:** fiscal.ai letter pages (e.g. https://fiscal.ai/fund-letters/investors/akre-capital-management-llc-fscl_investor_7TTC4HMS788/) show previews only. Logged and skipped; other copies of the same letters were used.
- **Not read in full:** "A Letter from the Investment Team – February 6, 2026". Its title is listed on https://www.akrefund.com/ and on https://www.mazvantage.com/research/letters, but I found no free copy and did not guess the akrefund.com address. The only content seen is a paywalled preview, https://fiscal.ai/fund-letters/akre-capital-management-llc-q1-2026-fscl_document_7ENB8DWJ692/ ("Akre Focus ETF Update - February 2026"). Its third-party tags list Roper, Constellation, Topicus and CCC as "Added", with the argument that their vertical software costs customers only 50–100 basis points of revenue, so replacing it with AI in-house is unlikely. Checked against N-PORT: Roper and CCC rose in the fund November–April, while Constellation and Topicus share counts were unchanged. Treat the preview as secondary. Semi-annual investor call replays (May 14 2026, Nov 18 2026; https://www.akrefund.com/semi-annual-investor-call-replay-may-2026/ and https://www.akrefund.com/semi-annual-investor-call-replay-november-2026/) are audio/video, not read. Barron's piece on the conversion reposted on akrefund.com not read.
- **Not found:** an explicit manager statement on why Airbnb was sold out. N-PORT timing: the fund held 3.26M shares at 2025-10-31, 2.40M at 2026-01-31, 1.17M at 2026-04-30 and 1.01M at 2026-07-31; the 13F shows none at 2026-09-30, so the last shares went in August–September 2026 (it was a top contributor in the FY to July 2026; the Q3 2026 letter text available did not explain the exit). Also no stated reason for selling the last of Danaher (Q4 2025–Q1 2026) or CarMax (Q1 2026) beyond the Q4 2024 letter's rate-sensitivity remarks for CarMax.
- **Not read:** Fund N-PX (trust); ADV Schedule A/B (fetch truncated). N-PORT, Form D and ADV Part 1 were read on 2026-11-19 (see above).
- **Estimated flows** in the profile (net buying/selling per quarter) are my own calculation: change in shares times the average of the two quarter-end implied prices, split-adjusted. They are approximations, not reported figures.
- Exa returned "not found" for the N-PX proxytable.html views; the .txt submissions worked.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
