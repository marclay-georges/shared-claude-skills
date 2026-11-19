# Fundsmith LLP (CIK 0001569205): research log

Written 2026-11-19 by a helper session building the three-year baseline. Companion files: `profile.md` (the brief), `holdings/*.csv` (LLP, one file per quarter, 2023-Q4 to 2026-Q3) and `holdings/fisl/*.csv` (sister filer FISL, same quarters, added later on 2026-11-19).

## Odd things, read these first

- **All twelve quarters reconcile exactly** with their cover pages on both entry count and total value. There are no 13F-HR/A amendments and no 13F-NT notices in the folder for this period, and no confidential-treatment omissions were found (no amendment later revealed a position).
- **Accession prefixes change over the period.** Q4 2023 to Q1 2025 were filed by an agent with prefix 0001520023; Q2 2025 by a different agent, prefix 0001801547; from Q3 2025 the filer uses its own CIK prefix 0001569205. Look in the CIK folder, don't guess from a prefix.
- **There is a sister 13F filer.** Fundsmith Investment Services Ltd (FISL, Mauritius), CIK 0001868537, file 028-21328, files its own 13F. It holds the same large-cap strategy stocks. All twelve of its quarters are now saved in `holdings/fisl/` and reconcile with their covers (table below). The LLP is 74.4–77.5% of combined LLP+FISL value in every quarter, and 69–82% of each shared large-cap name. The 13G group totals below agree. The two filers list no other included managers, so nothing in the LLP filing points at FISL.
- **The LLP 13F mixes several vehicles.** Fundsmith Equity Fund (UK OEIC), the Fundsmith SICAV sub-funds, Fundsmith Stewardship Fund (renamed from Sustainable Equity on 24 March 2025), the Delaware LPs, and Smithson (investment trust until February 2026, then Smithson Equity Fund OEIC). The 20-odd small and mid caps under 0.6% weight are Smithson's.
- **Smithson Investment Trust was liquidated** (effective 27 February 2026) with 58.6% of holders taking cash. This shows in the 2026-Q1 13F as a near-uniform ~58% cut across the Smithson names.
- **2026-Q1 to 2026-Q3 is a regime change**, not noise: H1 2026 turnover was 51.8% after a stated change of process (see profile).
- **All rows are SH (shares), SOLE discretion, common stock or ADR.** No PRN rows, no options or put/call rows, no other-manager column entries. Values are whole dollars in all twelve quarters, including 2023-Q4 and 2024-Q1 (checked after the coordinator's 2026-11-19 correction about filers still reporting in thousands): each cover total matches the summed rows, totals run $12.8bn to $25.6bn without a 1,000x jump, and implied prices match market prices (e.g. Microsoft $376.04 at 2023-12-31, $420.72 at 2024-03-31). No rescaling was applied. Voting authority: through 2024-Q1 small amounts sat in the "None" column; from 2024-Q2 "None" is zero except McCormick non-voting shares (all "None", correctly, as non-voting stock).
- **Signer and place:** Tom Armstrong, Director, signing for Fundsmith LLP from Grand Baie, Mauritius (2025 covers) and Beaux Songes, Mauritius (2026 covers; FISL moved office there on 7 April 2026). The 13F is signed from Mauritius although the filer is the London LLP.
- **Third-party tracker error found.** investortracks.com's Q3 2026 page says Veeva was "adjusted for a 1-for-2 reverse split". Veeva has no split on record (stockanalysis.com, roic.ai and alphaspread all show none, checked 2026-11-19). The raw change is 816,785 to 2,705,345 shares (+231%). Do not import that site's split adjustments.
- **Scratchpad collision (my process, not the data).** The shared scratchpad held another helper's `raw/` files with a different header format, which broke my first parse. I moved my own files into `scratchpad/fundsmith/` and reparsed; the saved CSVs come only from my own raw files.

## 13F filings read (all from the CIK folder https://www.sec.gov/Archives/edgar/data/1569205/)

Columns: period, form, accession, filed, entries on cover, total value on cover (USD), parsed rows and total match cover, URL of full submission.

| Period | Form | Accession | Filed | Entries | Total value | Reconciles | URL |
|---|---|---|---|---|---|---|---|
| 2023-Q4 | 13F-HR | 0001520023-24-000014 | 2024-02-14 | 40 | 23,888,150,521 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000014/0001520023-24-000014.txt |
| 2024-Q1 | 13F-HR | 0001520023-24-000020 | 2024-05-15 | 40 | 25,550,406,404 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000020/0001520023-24-000020.txt |
| 2024-Q2 | 13F-HR | 0001520023-24-000030 | 2024-08-14 | 40 | 24,539,466,801 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000030/0001520023-24-000030.txt |
| 2024-Q3 | 13F-HR | 0001520023-24-000040 | 2024-11-14 | 40 | 25,278,411,425 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000040/0001520023-24-000040.txt |
| 2024-Q4 | 13F-HR | 0001520023-25-000002 | 2025-02-14 | 38 | 23,458,177,867 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002325000002/0001520023-25-000002.txt |
| 2025-Q1 | 13F-HR | 0001520023-25-000003 | 2025-05-15 | 38 | 21,974,626,595 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000152002325000003/0001520023-25-000003.txt |
| 2025-Q2 | 13F-HR | 0001801547-25-000008 | 2025-08-14 | 39 | 23,016,527,870 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000180154725000008/0001801547-25-000008.txt |
| 2025-Q3 | 13F-HR | 0001569205-25-000004 | 2025-11-14 | 35 | 19,795,225,546 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000156920525000004/0001569205-25-000004.txt |
| 2025-Q4 | 13F-HR | 0001569205-26-000002 | 2026-02-17 | 37 | 17,116,090,918 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000002/0001569205-26-000002.txt |
| 2026-Q1 | 13F-HR | 0001569205-26-000005 | 2026-05-15 | 34 | 12,827,766,987 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000005/0001569205-26-000005.txt |
| 2026-Q2 | 13F-HR | 0001569205-26-000012 | 2026-08-14 | 41 | 13,648,923,682 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000012/0001569205-26-000012.txt |
| 2026-Q3 | 13F-HR | 0001569205-26-000014 | 2026-11-16 | 42 | 12,922,460,889 | yes | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000014/0001569205-26-000014.txt |

Amendments (13F-HR/A): none in the folder for these periods. Notices (13F-NT): none. Each row in every filing was a distinct CUSIP, so summing by CUSIP plus put/call changed nothing.

## FISL 13F filings read (sister filer, CIK 0001868537, folder https://www.sec.gov/Archives/edgar/data/1868537/), saved to `holdings/fisl/`

Added 2026-11-19 at the coordinator's request.
- Parsed from the full-submission .txt files, fetched in one Exa call; the oversized result was saved to a local tool-results file and parsed with Python.
- All twelve reconcile exactly on entry count and total.
- No amendments, no 13F-NT, and no other included managers.
- All rows are SH, with no put/call.
- Values are whole dollars; implied Microsoft price is $376.04 at 2023-12-31, the same as the LLP's.
- Signed by Tom Armstrong. FISL's 13F file number is 028-21328.

| Period | Accession | Filed | Entries | Total value | URL |
|---|---|---|---|---|---|
| 2023-Q4 | 0001868537-24-000002 | 2024-02-14 | 26 | 6,923,866,161 | https://www.sec.gov/Archives/edgar/data/1868537/000186853724000002/0001868537-24-000002.txt |
| 2024-Q1 | 0001868537-24-000005 | 2024-05-15 | 27 | 7,524,417,426 | https://www.sec.gov/Archives/edgar/data/1868537/000186853724000005/0001868537-24-000005.txt |
| 2024-Q2 | 0001868537-24-000009 | 2024-08-14 | 28 | 7,750,041,584 | https://www.sec.gov/Archives/edgar/data/1868537/000186853724000009/0001868537-24-000009.txt |
| 2024-Q3 | 0001520023-24-000041 | 2024-11-14 | 28 | 8,040,017,687 | https://www.sec.gov/Archives/edgar/data/1868537/000152002324000041/0001520023-24-000041.txt |
| 2024-Q4 | 0001868537-25-000008 | 2025-02-14 | 31 | 7,688,519,723 | https://www.sec.gov/Archives/edgar/data/1868537/000186853725000008/0001868537-25-000008.txt |
| 2025-Q1 | 0001868537-25-000009 | 2025-05-15 | 27 | 7,086,192,124 | https://www.sec.gov/Archives/edgar/data/1868537/000186853725000009/0001868537-25-000009.txt |
| 2025-Q2 | 0001801547-25-000007 | 2025-08-14 | 26 | 7,385,809,681 | https://www.sec.gov/Archives/edgar/data/1868537/000180154725000007/0001801547-25-000007.txt |
| 2025-Q3 | 0001868537-25-000015 | 2025-11-14 | 23 | 6,416,583,977 | https://www.sec.gov/Archives/edgar/data/1868537/000186853725000015/0001868537-25-000015.txt |
| 2025-Q4 | 0001868537-26-000002 | 2026-02-17 | 26 | 5,466,028,851 | https://www.sec.gov/Archives/edgar/data/1868537/000186853726000002/0001868537-26-000002.txt |
| 2026-Q1 | 0001868537-26-000003 | 2026-05-15 | 24 | 4,405,319,613 | https://www.sec.gov/Archives/edgar/data/1868537/000186853726000003/0001868537-26-000003.txt |
| 2026-Q2 | 0001868537-26-000007 | 2026-08-14 | 27 | 4,518,917,743 | https://www.sec.gov/Archives/edgar/data/1868537/000186853726000007/0001868537-26-000007.txt |
| 2026-Q3 | 0001868537-26-000009 | 2026-11-16 | 26 | 4,149,841,980 | https://www.sec.gov/Archives/edgar/data/1868537/000186853726000009/0001868537-26-000009.txt |

FISL quirks:
- **Agent prefixes.** Two accessions carry agent prefixes: 0001520023 for 2024-Q3 and 0001801547 for 2025-Q2, the same agents and quarters as the LLP.
- **ETF lines from 2025-Q4.** FISL's 13F includes tiny lines that are the Fundsmith Equity ETF's holdings: Apple 605, Amazon 715, TJX 1,155 and TSMC 605 shares, matching the ETF's December 2025 N-PORT exactly.
- **FISL-only names.** First Citizens, Nvidia, Reddit, Shopify, Coupang, IES Holdings, Waste Management and Paychex are not in the LLP filing. Each is under 0.6% of FISL. I take them to be a separate sub-advised mandate (inference; FISL's ADV lists unaffiliated US funds).
- **Divergence from the LLP.** Comparing quarter-on-quarter by CUSIP, the LLP's change in a large name differed from the combined change by 8 points or more only four times: Zoetis 2025-Q1, P&G 2026-Q2, Veeva 2026-Q3 and Yum 2026-Q3.
- **Scripts.** The parse and comparison scripts are `fisl_parse.py` and `combine.py` in the scratchpad's `fundsmith/scripts/`.

## Other SEC filings (Q4 2023 to Q3 2026)

### Schedule 13G and 13G/A (all Rule 13d-1(b), type IA, group filings, signed by Tom Armstrong)

Exhibit / Item 8 on each: "Fundsmith LLP is a Securities Affiliate of Fundsmith Investment Services Ltd, an Investment Manager incorporated in Mauritius… 8.34% owned by Mr Mark Laurence, 13.83% by Mr Julian Robins and 77.83% by Eighth Wonder Limited which is 100% owned by THE EIGHTH WONDER FOUNDATION."

| Filed | Accession | Issuer | Event date | Group shares | % class | LLP 13F shares same date | LLP share of group | URL |
|---|---|---|---|---|---|---|---|---|
| 2024-02-14 | 0001868537-24-000003 | Brown-Forman B (Amendment No. 2) | 2023-12-31 | 15,666,962 | 5.10% | 11.65M | ~74% | https://www.sec.gov/Archives/edgar/data/1569205/ (file fundsmith_brown2023.txt) |
| 2024-02-14 | 0001520023-24-000016 | Waters (Amendment No. 6) | 2023-12-31 | 4,935,371 | 8.30% | 3,800,688 | 77% | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000016/ |
| 2024-02-14 | 0001520023-24-000017 | Sabre (Amendment No. 3) | 2023-12-31 | 22,261,537 | 5.90% | 22.26M | 100% (Smithson only) | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000017/ |
| 2024-02-14 | 0001520023-24-000018 | McCormick non-voting (Amendment No. 5) | 2023-12-31 | 19,165,971 | 7.60% | 15,090,383 | 79% | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000018/ |
| 2024-11-14 | 0001520023-24-000038 | McCormick non-voting (13G/A, XML) | 2024-09-30 | 1,813,404 | 0.8% | 1,728,157 | 95% | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000038/primary_doc.xml |
| 2024-11-14 | 0001520023-24-000050 | Brown-Forman B (labelled Amendment No. 2 again) | 2024-09-30 | 12,909,622 | 4.40%, ceased >5% box ticked | not compared | | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000050/fundsmith_brown2024.txt |
| 2026-05-15 | 0001569205-26-000007 | Waters (Amendment No. 6 per XML) | 2026-03-31 | 4,308,930 | 4.4% | 3,212,075 | 75% | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000007/primary_doc.xml |
| 2026-05-15 | 0001569205-26-000008 | Sabre (Amendment No. 3 per XML) | 2026-03-31 | 9,013,783 | 2.3% | 9,013,783 | 100% (Smithson only) | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000008/primary_doc.xml |

Quirks: amendment numbers repeat (Brown-Forman "No. 2" twice; Waters "No. 6" in 2024 and 2026), and the 2024 McCormick XML cites a 2023 accession as its predecessor. Treat the numbering as unreliable; dates and share counts are what matter.

### Schedule 13D
None in the folder for the period. Fundsmith is a passive 13G filer throughout.

### Forms 3, 4, 5
None. Fundsmith is not a 10% holder of any issuer in the period (largest stake seen is 8.3% of Waters at group level in Dec 2023), so Section 16 does not apply.

### Form N-PX (institutional manager say-on-pay votes)

| Filed | Accession | Filer | Period | Read? | URL |
|---|---|---|---|---|---|
| 2024-08-28 | 0001520023-24-000031 | Fundsmith LLP | year to 2024-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000031/0001520023-24-000031.txt |
| 2024-09-04 | 0001520023-24-000032 | Fundsmith LLP (N-PX/A, restatement) | year to 2024-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1569205/000152002324000032/0001520023-24-000032.txt |
| 2024-08-30 | 0001868537-24-000010 | FISL | year to 2024-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1868537/000186853724000010/0001868537-24-000010.txt |
| 2025-08-22 | 0001520023-25-000007 | Fundsmith LLP | year to 2025-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1569205/000152002325000007/0001520023-25-000007.txt |
| 2025-08-22 | 0001868537-25-000013 | FISL | year to 2025-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1868537/000186853725000013/0001868537-25-000013.txt |
| 2026-08-21 | 0001569205-26-000013 | Fundsmith LLP | year to 2026-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1569205/000156920526000013/proxyvotetable.xml |
| 2026-08-21 | 0001868537-26-000008 | FISL (sister) | year to 2026-06-30 | read in full | https://www.sec.gov/Archives/edgar/data/1868537/000186853726000008/proxyvotetable.xml |

What the 2026 tables show: the LLP's N-PX covers only small and mid caps (ADMA, Badger Meter, Doximity, Manhattan Associates, Medpace, MSCI, Paycom, Rollins, Sabre, Clorox, Verisign, Vertiv): 7 votes against say-on-pay, 5 for. FISL's N-PX covers the large caps (Alphabet, ADP, Church & Dwight, Fortinet, IDEXX, Intuit, Marriott, Mettler, Microsoft, Nike, Otis, PMI, Stryker, TI, P&G, Visa, Waters, Zoetis, plus Badger Meter and small Amazon, Home Depot, TJX, Waste Management lines): against on 20 of 23 say-on-pay items, for only IDEXX, Home Depot and TJX. FISL's share counts are group-level (Waters 4,296,350 against the 13G group figure of 4,308,930). Earlier years:
- **LLP, 2024.** Against 9 of 12 say-on-pay items: MSCI, Graco, Paycom, Cognex, Equifax, IDEX, Verisk, Choice and Verisign. For: Sabre, Exponent and Qualys, plus Sabre's director equity plan. The N-PX/A of 2024-09-04 restated only Paycom, from FOR to AGAINST.
- **LLP, 2025.** Against 9 of 13. For: Clorox, Sabre, Exponent and Qualys.
- **FISL, 2024.** Against 17 of 21 say-on-pay items. For: First Citizens, IDEXX, Home Depot and McDonald's. Group-level counts include Microsoft 11,298,966 and PMI 19,412,206.
- **FISL, 2025.** Against 20 of 24. For: IDEXX, Home Depot, Coupang and Shopify.

IDEXX was voted FOR by FISL in all three years. Preparer: Addition Compliance Limited, London. N-PX cover gives LLP's identifiers: 13F file 028-15226, CRD 160365, SEC 801-79120.

### Form ADV
- Fundsmith LLP Part 2A brochure dated 26 June 2026: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1049668 (read). Regulatory AUM $18.51bn at 31 March 2026; advises Fundsmith Equity Fund L.P. and Fundsmith Sustainable Equity Fund L.P. (Delaware) plus non-US funds; FISL is sub-adviser; owner International Value Investments Ltd under the Eighth Wonder Foundation (Seychelles) set up by Terry Smith; fees 1.0% / 0.9%; no derivatives.
- FISL Part 2A brochure dated 29 June 2026: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1049828 (read). Regulatory AUM $23.8bn discretionary; sub-advises the Delaware LPs, the Fundsmith Equity ETF (ALPS Series Trust, NYSE Arca, 1.00% unitary fee), unaffiliated US funds, non-US funds and Fundsmith Reserve Master Fund (Cayman); office moved to Beaux Songes 7 April 2026.
- Fundsmith LLP Form ADV Part 1, annual amendment of 26 June 2026: https://reports.adviserinfo.sec.gov/reports/ADV/160365/PDF/160365.pdf. Fetched via Exa; the oversized output was saved locally and searched with Python for Items 5 and 7.B rather than read line by line. What it says:
  - regulatory AUM $18,508,143,977, all discretionary, across 5 accounts
  - $17,899,700,479 attributable to non-US persons
  - 43 employees, 5 performing investment advisory functions
  - two private funds: Fundsmith Equity Fund, LP (Delaware, long-only equity, gross assets $504,522,962, minimum $250,000) and a second LP with gross assets $103,920,536
- FISL Form ADV Part 1: not fetched.

### Form D
None found in the LLP's CIK folder for the period. Private vehicles (Delaware LPs, the Cayman Reserve fund) may file under their own CIKs; not searched.

### N-CSR / N-PORT
Read on 2026-11-19 at the coordinator's request, to put numbers on the non-US share. The Fundsmith Equity ETF (ticker ETFT) is series S000097194 of ALPS Series Trust (CIK 0001558107). It launched on 1 December 2025 and FISL is its adviser.

| Period | Form | Accession | Filed | Net assets | Non-US-listed share of equities | URL |
|---|---|---|---|---|---|---|
| 2025-12-31 | NPORT-P | 0001049169-26-000387 | 2026-02-27 | $5.46m | 35.5% (12 of 32 names) | https://www.sec.gov/Archives/edgar/data/1558107/000104916926000387/0001049169-26-000387.txt |
| 2026-03-31 | NPORT-P | 0001049169-26-001468 | 2026-05-29 | $13.67m | 31.8% | https://www.sec.gov/Archives/edgar/data/1558107/000104916926001468/0001049169-26-001468.txt |
| 2026-06-30 | NPORT-P | 0001049169-26-002147 | 2026-08-28 | $7.76m | 15.0% (Amadeus, L'Oréal, Legrand, Sage) | https://www.sec.gov/Archives/edgar/data/1558107/000104916926002147/0001049169-26-002147.txt |

How the figures were computed and what they leave out:
- **Method.** Each share is non-US-listed equity value divided by total common stock. TSMC is counted as US because it is held as the US ADR, though N-PORT codes the issuer as TW.
- **ETF ≠ FEF.** The ETF is not identical to FEF. It held Apple, Amazon and Danone, and its weights were near-equal at launch.
- **Oct 2026 website split.** The ETF's own website, read 2026-11-19, gives country of listing at 30 October 2026 as US 76.0%, France 9.6%, Spain 5.1%, UK 4.5% and cash 4.8%. https://www.fundsmithetf.us/
- **Not read.** The Sept 2026 N-PORT was not found; it is due around 29 November 2026. The March 2026 semi-annual report (N-CSRS 0001398344-26-010363) and the ETF's N-PX (0001398344-26-015882) were not read.
- **Third-party lists.** Secondary holdings lists for the ETF (stockanalysis.com, equibles, stillhousedata) were seen in search results only. Stillhousedata's percentages are visibly mis-scaled.

## Manager's own words and other sources, in the order read for the narrative (oldest first)

| Date of source | Source | URL |
|---|---|---|
| enduring | Fundsmith Owner's Manual and fund documents | https://www.fundsmith.co.uk/documents/ |
| Jan 2024 | FEF annual letter for 2023 | https://www.fundsmith.co.uk/media/31plodnq/2023-fef-annual-letter-to-shareholders.pdf |
| Jul 2024 | FEF semi-annual letter H1 2024 | https://www.fundsmith.co.uk/media/uznnt5w2/2024-fef-semi-annual-letter-to-shareholders.pdf |
| Jan 2025 | FEF annual letter for 2024 | https://www.fundsmith.co.uk/media/pirmvyly/annual-letter-to-shareholders-2024.pdf |
| Jan 2025 | FEF short-form report 2024 (largest purchases and sales in £, share count) | https://www.fundsmith.co.uk/media/2l1p53ou/2024-short-form-report-for-the-twelve-months-ended-31-december-2024.pdf |
| 2025-01-28 | Morningstar: underperforms fourth year | https://global.morningstar.com/en-eu/funds/fundsmith-equity-underperforms-fourth-year |
| 2025-03-24 | Fundsmith news: Sustainable Equity renamed Stewardship Fund | https://www.fundsmith.co.uk/news/2025/6043-fundsmith-renames-fundsmith-sustainable-equity-fund-to-fundsmith-stewardship-fund |
| Jul 2025 | FEF semi-annual letter H1 2025 | https://www.fundsmith.co.uk/media/bvgden5v/2025-fef-semi-annual-letter-to-shareholders.pdf |
| 2025-07-22 | Citywire / Morningstar on H1 2025 outflows (£1.9bn) | seen via Exa search results (no stable URL kept) |
| 2025-11-12 | Smithson RNS: restructure proposals | https://www.londonstockexchange.com/en/news/article/restructure-proposals/6b21-87-31-8a-55-410191 |
| 2025-11-20 | interactive investor note (fund ~£17bn, peak >£25bn) | seen via Exa search results |
| Jan 2026 | FEF annual letter for 2025 | https://www.fundsmith.co.uk/media/4hcfd1pg/2025-fef-annual-letter-web.pdf |
| Jan 2026 | FEF short-form report 2025 | https://www.fundsmith.co.uk/media/uxvf5sjz/2025-short-form-report-for-the-twelve-months-ended-31-december-2025.pdf |
| Jan 2026 | Stewardship Fund annual letter 2025 (SICAV version) | https://www.fundsmith.eu/media/qvkearfi/2025-annual-letter.pdf |
| Jan 2026 | Stewardship Fund UK short-form report 2025 | https://www.fundsmith.co.uk/media/minaphkq/2025-short-form-report-for-the-twelve-months-ended-31-december-2025.pdf |
| 2026-01-08 | Citywire: 2025 outflows ~£6.5bn | seen via Exa search results |
| 2026-01-22 | FTAdviser: peak £26bn | seen via Exa search results |
| Jan 2026 | Calastone: record UK equity fund outflows 2025; Investment Week / Trustnet coverage | seen via Exa search results |
| Feb 2026 (posted 2026-03-17) | Fundsmith Annual Shareholders' Meeting, February 2026, Fundsmith's own YouTube channel (transcript extract via Exa) | https://www.youtube.com/watch?v=W8vYeazBox4 |
| 2026-03-18 | Librarian Capital full AGM transcript (secondary, not opened; noted as a fuller text) | https://librariancapital.substack.com/p/fundsmith-2026-agm-full-transcript |
| 2026-02-23/24 | AIC: over half of Smithson holders opt for cash exit | https://www.theaic.co.uk/aic/news/industry-news/over-half-of-smithson-shareholders-opt-for-cash-exit |
| Jul 2026 | FEF semi-annual letter H1 2026 (strategy change; Appendix 2 trade reasons) | https://www.fundsmith.co.uk/media/lfhpxi1x/fundsmith-equity-fund-semi-annual-letter-to-shareholders-2026.pdf |
| 31 Jul 2026 | FEF factsheet July 2026 ("A number of portfolio changes were implemented in July") | https://www.fundsmith.co.uk/media/yshdfb44/july.pdf |
| 2026-08-06 (republished) | Morningstar analyst report on FEF | https://www.fundsmith.co.uk/media/jbsni1u0/morningstar-fundsmith-report-2025.pdf |
| 2026-08-13 | Fidelity UK: Important changes at Fundsmith Equity | https://www.fidelity.co.uk/markets-insights/investing-ideas/funds/important-changes-at-fundsmith-equity/ |
| 2026-08-17 | Hargreaves Lansdown fund update | https://www.hl.co.uk/funds/research-and-news/fundsmith-equity-august-2026-fund-update |
| 28 Aug 2026 | FEF factsheet August 2026 (no outright sales or purchases) | https://www.fundsmith.co.uk/media/rs5hmxd0/august.pdf |
| 2026-09-14 | Smithson portfolio manager change letter (Barnard to Imlah, Fundsmith Partners US LLC) | https://www.fundsmith.co.uk/media/xjwpufit/portfolio-manager-change-september-2026.pdf |
| 2026-09-21 | ABC Money on factsheet limits and H1 trades | https://www.abcmoney.co.uk/2026/09/fundsmith-equity-fund-holdings-reveal-more-than-the-top-10/ |
| 30 Sep 2026 | FEF factsheet September 2026 (no outright sales or purchases; US 82.3%) | https://www.fundsmith.co.uk/media/n4hdflc1/september.pdf |
| 30 Oct 2026 | FEF factsheet October 2026 (live page) | https://www.fundsmith.co.uk/factsheet |
| 2026-10-30 | Copio Capital blog on Fundsmith portfolio (secondary) | https://copiocapital.com/blog/terry-smith-fundsmith-portfolio-strategy |
| 2026-11-16 | investortracks Fundsmith Q3 2026 page (secondary; contains the Veeva split error) | https://investortracks.com/investors/fundsmith/ |
| 2026-11-19 | Veeva split check: stockanalysis.com, roic.ai, alphaspread | https://stockanalysis.com/stocks/veev/statistics/ |

## Problems and gaps

- **Exa output limit:** fetching the 2024 short-form report exceeded the tool's output size; the result was saved to a local tool-results file and the relevant passages were extracted with Python. No content lost.
- **EDGAR browse page:** not used (known to be stale); all filings were taken from the archive folder listings.
- **Not read:** the 2024 and 2025 Annual Shareholders' Meetings (Fundsmith publishes video and Q&A each year; only the February 2026 meeting was read, from a transcript extract); the H2 2023 period's semi-annual letter (July 2023, before the window); Terry Smith's newspaper columns; monthly factsheets before July 2026; FISL's Form ADV Part 1; the ETF's N-CSR/N-CSRS and its September 2026 N-PORT; FEF's UK long-form annual and half-year reports (full holdings). The earlier N-PX tables, FISL's 13Fs, three ETF N-PORTs and the LLP's ADV Part 1 were added later the same day.
- **No paywalls, sign-ins or human checks were met.** None were attempted.
- **Not established:** the exact split of each 13F row between FEF, the SICAV, Stewardship, the Delaware LPs and Smithson. The vehicle attributions in the profile are inferences from size, overlap with the published fund portfolios and timing.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
