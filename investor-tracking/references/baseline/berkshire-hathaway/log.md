# Berkshire Hathaway (CIK 0001067983): research log

Written 2026-11-19. This log covers the 13F baseline for Q4 2023 through Q3 2026 and the profile in this folder.

## Oddities to know first

- **Two quarters were filed with positions held back under confidential treatment. The CSVs show those quarters as amended.**
  - Q4 2023: the original 13F-HR (0000950123-24-002518) answered "true" to confidential omission. Chubb was the hidden position. Berkshire revealed it on 2024-05-15 in two single-row 13F-HR/As:
    - Q3 2023: 8,143,530 sh, $1,695,320,075 (0000950123-24-005653).
    - Q4 2023: 20,100,000 sh, $4,542,600,000 (0000950123-24-005664).
    - The amendments say confidential treatment ended because the holding was reported in the 2024-03-31 13F.
  - Q1 2025: the original (0000950123-25-005701) answered "true" again. Amendment 0000950123-25-008361, filed 2025-08-14, revealed four rows totalling $1,106,550,356:
    - D R Horton 1,512,371 sh
    - Lennar A 1,929,972 sh
    - Lennar B 202 sh
    - Nucor 5,756,510 sh
  - `holdings/2023-Q4.csv` adds the Chubb row. Its total is $351,900,674,461 against $347,358,074,461 filed.
  - `holdings/2025-Q1.csv` adds the four rows. Its total is $259,807,694,872 against $258,701,144,516 filed.
  - The `pct_of_portfolio` column in both files uses the amended total.
  - The Q3 2023 amendment falls outside the period. It was read but not saved as a CSV.
- **Every one of the 12 originals reconciles exactly with its cover page, on both entry count and total value.** The table is under "13F filings read".
- **Units: every quarter is in whole dollars. Nothing was rescaled.** I checked this after the coordinator's 2026-11-19 correction about filers that still reported in thousands. For every quarter, the summed rows equal the cover-page total, and the values imply quarter-end prices: Apple $192.53 at 2023-12-31, $171.48 at 2024-03-31, and $333.02 at 2026-09-30, with Coca-Cola similarly matching. A filing in thousands would imply prices 1,000 times too small.
- No 13F-NT. No late filings.
  - Q4 2025 was filed 2026-02-17, because Feb 14 was a Saturday and Feb 16 a holiday.
  - Q3 2026 was filed 2026-11-16, because Nov 14 was a Saturday.
- **All rows are SH. No PRN, no puts or calls. Every row's discretion is DFND (shared-defined).**
- **Large multi-row reporting.** Each filing has 89 to 138 rows but only 29 to 42 CUSIP positions. One stock can appear in up to 12 rows, one per chain of subsidiaries.
  - Every row carries other-manager "4" (Warren E. Buffett).
  - Fourteen other included managers appear on every full filing:
    - 1 BH Homestate
    - 2 BH Life of Nebraska
    - 3 BH Finance
    - 4 Buffett Warren E
    - 5 Columbia Insurance
    - 6 Cypress
    - 7 General Re
    - 8 GEICO Corp
    - 9 Medical Protective
    - 10 National Fire & Marine
    - 11 National Indemnity
    - 12 National Liability & Fire
    - 13 Nebraska Furniture Mart
    - 14 U.S. Investment Corp
  - The CSVs sum the rows by CUSIP plus put/call.
- **Share classes are separate CUSIPs and separate CSV rows.** These are Alphabet A and C, Lennar A and B, and Liberty Live A and C. Q3 2026 has 30 CUSIP positions across 27 issuers.
- **Filing agent changed.** Accession prefixes are 0000950123 up to Q2 2025 and 0001193125 from Q3 2025. Same filer CIK and same signer.
- **Signer.** Every filing is signed by Marc D. Hamburg (SVP), including Q2 and Q3 2026. That is after he handed CFO duties to Chuck Chang on 2026-06-01; he retires 2027-06-01. Expect a new signer in 2027.
- **Corporate actions, not trades** (don't read them as buys or sells):
  - Q3 2024: Liberty SiriusXM tracking stock became SiriusXM Holdings, with new CUSIP 829933100.
  - Q4 2025: Liberty Live split off into Liberty Live Holdings (new CUSIPs). The Formula One tracking stock was renamed, then sold in Q1 2026.
  - Issuer names drift between filings, for example "BANK AMERICA CORP" vs "BANK OF AMER CORP", "CHUBB LIMITED" vs "CHUBB LTD SWITZ", and "CHEVRON CORP NEW" vs "CHEVRON CORPORATION". Match on CUSIP, not name.
- **A non-US issuer appears on the 13F.** Bending Spoons SpA (Italian CUSIP T19377109, Nasdaq BSP) shows up in Q3 2026. It is on the 13F because its shares are US-listed. The Japanese trading houses are not on any 13F.
- **Small stub rows to ignore.** D R Horton 3,564 sh appears again from Q2 2026 after the position was sold in Q3 2025. NVR (11,112 sh) and Jefferies (433,558 sh) have sat unchanged for years.
- **Morningstar's Q2 2026 note gets Lennar wrong.** It says Berkshire "sold 9.3 million shares of Lennar Class A" and bought "12.4 million additional shares of Lennar Class B". The filings show Lennar A rising from 10.10M to 13.11M and Lennar B from 0.24M to 0.30M. The CSVs follow the filings.

## 13F filings read (full submission .txt, via Exa)

| Form | Period | Filed | Accession | Entries | Total ($) | Conf. omitted | Reconciles | URL |
|---|---|---|---|---|---|---|---|---|
| 13F-HR | 2023-12-31 | 2024-02-14 | 0000950123-24-002518 | 138 | 347,358,074,461 | true | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324002518/0000950123-24-002518.txt |
| 13F-HR | 2024-03-31 | 2024-05-15 | 0000950123-24-005622 | 133 | 331,680,406,332 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324005622/0000950123-24-005622.txt |
| 13F-HR/A | 2023-09-30 | 2024-05-15 | 0000950123-24-005653 | 1 | 1,695,320,075 | n/a | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324005653/0000950123-24-005653.txt |
| 13F-HR/A | 2023-12-31 | 2024-05-15 | 0000950123-24-005664 | 1 | 4,542,600,000 | n/a | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324005664/0000950123-24-005664.txt |
| 13F-HR | 2024-06-30 | 2024-08-14 | 0000950123-24-008740 | 129 | 279,969,062,343 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324008740/0000950123-24-008740.txt |
| 13F-HR | 2024-09-30 | 2024-11-14 | 0000950123-24-011775 | 121 | 266,378,900,503 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012324011775/0000950123-24-011775.txt |
| 13F-HR | 2024-12-31 | 2025-02-14 | 0000950123-25-002701 | 112 | 267,175,474,249 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012325002701/0000950123-25-002701.txt |
| 13F-HR | 2025-03-31 | 2025-05-15 | 0000950123-25-005701 | 110 | 258,701,144,516 | true | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012325005701/0000950123-25-005701.txt |
| 13F-HR | 2025-06-30 | 2025-08-14 | 0000950123-25-008343 | 114 | 257,521,776,925 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012325008343/0000950123-25-008343.txt |
| 13F-HR/A | 2025-03-31 | 2025-08-14 | 0000950123-25-008361 | 4 | 1,106,550,356 | n/a | yes | https://www.sec.gov/Archives/edgar/data/1067983/000095012325008361/0000950123-25-008361.txt |
| 13F-HR | 2025-09-30 | 2025-11-14 | 0001193125-25-282901 | 115 | 267,334,501,955 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000119312525282901/0001193125-25-282901.txt |
| 13F-HR | 2025-12-31 | 2026-02-17 | 0001193125-26-054580 | 110 | 274,160,086,701 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000119312526054580/0001193125-26-054580.txt |
| 13F-HR | 2026-03-31 | 2026-05-15 | 0001193125-26-226661 | 90 | 263,095,703,570 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000119312526226661/0001193125-26-226661.txt |
| 13F-HR | 2026-06-30 | 2026-08-14 | 0001193125-26-352200 | 89 | 299,253,556,246 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000119312526352200/0001193125-26-352200.txt |
| 13F-HR | 2026-09-30 | 2026-11-16 | 0001193125-26-463399 | 89 | 304,196,581,325 | false | yes | https://www.sec.gov/Archives/edgar/data/1067983/000119312526463399/0001193125-26-463399.txt |

Position counts by CUSIP, Q4 2023 to Q3 2026: 42, 41, 41, 40, 38, 39, 41, 41, 42, 29, 29, 30.

I found the accessions from the archive folder listing https://www.sec.gov/Archives/edgar/data/1067983/ and the browse-edgar 13F list. The 13F browse list happened to be current.

## Other SEC filings, by type

**10-K, 10-Q and earnings releases.** Read these for cash, buybacks, and equity purchases and sales from the cash-flow statement:
- 10-K FY2023: 0000950170-24-019719 (2024-02-26).
- 10-K FY2024: 0000950170-25-025210 (2025-02-24).
- 10-K FY2025: 0001193125-26-083899 (2026-03-02).
- 10-Q Q2 2024 cash flows: https://www.berkshirehathaway.com/qtrly/2ndqtr24.pdf
- 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm
- 10-Q Q3 2026: https://www.berkshirehathaway.com/qtrly/3rdqtr26.pdf (SEC accession 0001193125-26-452412, filed 2026-11-09)
  - Nine-month 2026 equity purchases $41,771M, sales $30,572M.
  - The buyback rule now reads: the CEO, "after consultation with the Chairman", decides; repurchases stop if cash would fall below $30B.
- Earnings release, 2026-11-07: https://berkshirehathaway.com/news/nov0726.pdf
- Other 10-Qs: 0000950170-24-053185, 0000950170-24-090305, 0000950170-24-120241, 0000950170-25-063112, 0000950170-25-101578, 0001193125-25-261548, 0001193125-26-202243. I did not open their documents. Their equity purchase and sale figures came from SEC's XBRL API instead, which carries the tagged values from every 10-Q and 10-K:
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0001067983/us-gaap/PaymentsToAcquireEquitySecuritiesFvNi.json
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0001067983/us-gaap/ProceedsFromSaleOfEquitySecuritiesFvNi.json
  - Year-to-date purchases ($M; Q1, H1, 9M, FY): 2023 2,873 / 7,442 / 9,142 / 16,462; 2024 2,691 / 4,306 / 5,809 / 9,237; 2025 3,183 / 7,092 / 13,447 / 16,923; 2026 15,938 / 39,405 / 41,771.
  - Year-to-date sales ($M): 2023 13,283 / 25,833 / 32,786 / 40,631; 2024 19,972 / 97,123 / 133,218 / 143,359; 2025 4,677 / 11,592 / 24,046 / 30,686; 2026 24,087 / 27,780 / 30,572.
  - Each Q4 figure is the 10-K full year minus the nine-month 10-Q. I checked the 9M figures for 2023, 2024 and 2025 against the third-quarter 10-Q PDFs (https://www.berkshirehathaway.com/qtrly/3rdqtr23.pdf, 3rdqtr24.pdf, 3rdqtr25.pdf), and they match.

**8-K.** Index pages read:
- 0001193125-25-229405 (2025-10-03): item 5.03, bylaws.
- 0001193125-25-314935 (2025-12-11): item 5.02. Its EX-99.1 is the 2025-12-08 release on Combs leaving, Pierce becoming GEICO CEO and Abel becoming CEO; I read that release at berkshirehathaway.com.
- 0001193125-25-115695 (2025-05-08): item 5.02. Its EX-99.1 says the board voted unanimously on 2025-05-04 to make Abel President and CEO from 2026-01-01, with Buffett remaining Chairman.
- 0001193125-26-004727 (2026-01-06, 8-K/A): item 5.02. Read. Abel became President and CEO on 2026-01-01, at a $25M salary.
- 0001193125-26-212148 (2026-05-07): items 2.02, 5.02, 5.03 and 5.07. Read (https://www.sec.gov/Archives/edgar/data/1067983/000119312526212148/d74313d8k.htm).
  - Chang succeeds Hamburg as CFO on 2026-06-01.
  - The board amended the by-laws on 2026-05-03 "to update the officer roles and responsibilities to conform to Berkshire's current operating structure" (Sections 4, 6 and 10). I did not read the by-law exhibit itself.
  - All 13 directors were re-elected; nothing in it concerns the investment portfolio.
- Other 8-Ks with item 5.07 (meeting votes only): 0001193125-24-133049 (2024-05-07), 0001193125-25-113900 (2025-05-06). Not opened.

**DEF 14A (proxy).** Read: 0001193125-24-069107 (2024-03-15), 0001193125-25-054877 (2025-03-14) and 0001193125-26-106253 (2026-03-13), via the main documents in each SEC folder.
- None of the three mentions Weschler, Combs or who manages the stock portfolio.
- Buffett's voting interest is 31.0%, 30.3% and 30.0%; his economic interest is 15.0%, 14.3% and 13.7%. A voting agreement caps his votes at 49.9%.
- 2024 and 2025: after Buffett, no family member would manage Berkshire, but the family would help the board pick and oversee the CEO, and a family member should be non-executive Chairman.
- 2026: Abel CEO since 2026-01-01, Buffett Chairman; only the family non-executive-chairman sentence remains. The compensation committee "will be working with Mr. Abel… to evaluate what, if any, changes" the CEO change requires.

**Schedule 13D/13G and amendments.** Berkshire files many of these, under its own CIK and the subject's. The browse page https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067983&type=SC+13 came back stale, ending 2024-11-25. Resolved: the SEC submissions file https://data.sec.gov/submissions/CIK0001067983.json, fetched through Exa, lists every filing under Berkshire's CIK with its form type (356 filings, 2023-10-02 to 2026-11-17). The archive folder https://www.sec.gov/Archives/edgar/data/1067983/ also loads, but it lists accession folders without form types. Index pages read:
- SC 13G, Liberty Media, 2024-02-14: 0001193125-24-036540 and 0001193125-24-036510. Group members include R. Ted Weschler, GEICO, NICO, and the BH, BNSF, PCC and Scott Fetzer pension trusts.
- SC 13G/A, Liberty Media: 0001193125-24-089047 (2024-04-08), 0001193125-24-226916 and 0001193125-24-226917 (2024-09-26). Weschler is a group member.
- SC 13G, Chubb, 2024-11-14: 0001193125-24-258561. Group members are NICO and Buffett only.
- SC 13D/A, DaVita: 0001193125-24-038549 (2024-02-16) and 0001193125-24-197170 (2024-08-08). Group members include Weschler and the pension trusts. The DaVita sales are made under an agreement that keeps Berkshire at or below 45%.
- SC 13D/A by Buffett on Berkshire itself (his gifts; not portfolio): 0001193125-23-283406, 0001193125-24-172349, 0001193125-24-265100.
- After the December 2024 form rename ("SCHEDULE 13G/A"), I found only through search and listing:
  - SCHEDULE 13G/A, Domino's: 0001193125-26-054571 (2026-02-17).
  - SCHEDULE 13G/A, Pool: 0001193125-26-054609 (2026-02-17).
  - SCHEDULE 13G, Constellation Brands: 0000950170-25-072565 (2025-05-15).
  - From the submissions file plus index pages, new Schedule 13G subjects in the period are: Chubb (0001193125-24-258561, 2024-11-14), Domino's (0000950170-25-021164, 2025-02-14), Constellation Brands (0000950170-25-072565, 2025-05-15), Pool (0000950170-25-108858, 2025-08-14), Liberty Live Holdings (0001193125-26-054685, 2026-02-17), Delta (0001193125-26-227087, 2026-05-15), New York Times (0001193125-26-227126, 2026-05-15), Lennar (0001193125-26-352904, 2026-08-14, before it crossed 10% in September) and Bending Spoons (0001193125-26-464218, 2026-11-16).
  - SCHEDULE 13D/A, DaVita: 0000950170-25-020183 (2025-02-13).
  - SCHEDULE 13D/A by Buffett on Berkshire itself (gifts, not portfolio): 0000950170-25-091802, 0001193125-25-277436, 0001193125-26-304838, 0001193125-26-465884.
  - Unopened 13G/As, subjects unknown: 0000950170-25-021166, -021167 (2025-02-14); 0000950170-25-108857 (2025-08-14); 0001193125-25-283602, -283604, -283606, -283610, -283617, -283631 (2025-11-14); 0001193125-26-227100, -227102, -227107, -227122, -227203 (2026-05-15); 0001193125-26-352910 (2026-08-14); 0001193125-26-417254 (2026-10-07); 0001193125-26-464189, -464211, -464214, -464219 (2026-11-16).
  - Three 13G/As under Berkshire's CIK are by other holders of Berkshire stock, not by Berkshire: 0000315066-26-000368, 0000102909-26-000775 and 0002100119-26-000227.

**Forms 3 and 4 (Berkshire as a 10% owner).**
- Form 3 and Form 4, Lennar, filed 2026-09-21. Form 4: https://www.sec.gov/Archives/edgar/data/920760/000119312526397059/xslF345X06/ownership.xml. Purchases 9/17 to 9/21/2026. Holders are AZGUARD, BHG Life, Medical Protective, NICO, NorGUARD and WestGUARD.
- Form 4, Lennar, 0001193125-26-403089 (accepted 2026-09-25), via https://portfoliosavvy.com/report/000119312526403089-berkshire-hathaway-inc-2026-09-23
- Form 4, SiriusXM, 0001193125-26-445930 (filed 2026-11-03): https://www.sec.gov/Archives/edgar/data/1067983/000119312526445930/0001193125-26-445930.txt
  - Purchases 10/30 to 11/3/2026, bringing the holding to 125,731,398 sh.
  - GEICO holds 109,746,508 sh.
  - Pension plans hold 15,984,890 sh: BH Consolidated 10,556,408, BNSF 3,308,255, PCC 1,952,727, Scott Fetzer 167,500.
  - The holding before these purchases, 124,807,117 sh, equals the Q3 2026 13F figure exactly. So the 13F includes the subsidiary pension-plan holdings.
- Form 4 by Ajit Jain (0001728451-24-000002): his own holdings, not portfolio.
- The browse page for type=4 timed out on Exa (CRAWL_LIVECRAWL_TIMEOUT). Resolved with the submissions file (144 Forms 3, 4 and 4/A in the period, heaviest in 2024 for the BofA sales and OXY buys) and the owner page https://www.sec.gov/cgi-bin/own-disp?action=getowner&CIK=0001067983, which lists the transactions by issuer. Points that matter:
  - Lennar: buys 2026-09-17 to 10-02 took Class A to 28,438,045 sh and Class B to 568,028.
  - DaVita: quarterly sales continue; the latest, 2026-10-27, sold 382,563 sh, leaving 28,314,666.
  - Liberty Live C: sales 2026-01-06 to 01-16, leaving 10,587,143. Form 3 0001193125-26-054931 (2026-02-17).
  - VeriSign: 4.3M sold 2025-07-30, leaving 8,989,880.
  - SiriusXM: buys 2025-07-31 to 08-04 to 124,807,117, then 2026-10-30 to 11-03 to 125,731,398.
  - Form 3s 0001193125-26-206348 (2026-05-05) and 0001193125-26-265894 (2026-06-10) are Berkshire officers, not portfolio: General Counsel Michael O'Sullivan and CFO Charles Chang.
  - Form 3s 0000950170-24-108005 and 0000950170-24-115313 (2024) were not opened.

**Form N-PX.** None filed under Berkshire's CIK from 2023-10-02 to 2026-11-17, per the SEC submissions file (which lists every form type in that span; N-PX does not appear).
- The browse page type=N-PX timed out on Exa.
- Searches returned only N-PX votes by others at Berkshire's meetings: https://votescores.com/company/berkshire-hathaway-inc/ (28% of reporting filers voted against Berkshire's say-on-pay in 2026) and https://proxyvotesnow.com/company/berkshire-hathaway-inc/2025
- A 13F manager should file N-PX for say-on-pay votes from mid-2024. None appears under Berkshire's CIK. Whether one is filed under another entity, such as an insurance subsidiary or a joint filing, I did not check.

**Form ADV.** Not applicable. Berkshire is an insurance holding company, not a registered investment adviser; its 13F lists insurers and Buffett as managers. I did not search IAPD separately. This is low priority, but the absence is unverified.

**Form D.** Not applicable as a filer (Berkshire raises no private funds). The browse page type=D timed out. Related: Bending Spoons' October 2026 private placement to GEICO relied on Reg D Rule 506 (per the issuer's 6-K), and the issuer would be the one filing any Form D.

**Issuer filings read.**
- Alphabet 8-K EX-99.2, 2026-06-02 (the $10B Berkshire private placement): https://www.sec.gov/Archives/edgar/data/1652044/000119312526257724/d83560dex992.htm
- Bending Spoons 6-K, October 2026 (subscriber is Government Employees Insurance Company): https://bendingspoons.com/documents/financials/2026/Bending%20Spoons%E2%80%94Form%206-K%E2%80%94Berkshire%20Hathaway%20Investment%E2%80%94October%202026.pdf

## Other sources (in reading order, with date)

- 2023 annual letter, 2024-02-24: https://www.berkshirehathaway.com/letters/2023ltr.pdf
- 2024 AGM, 2024-05-04:
  - CNBC archive https://buffett.cnbc.com/video/2024/05/06/morning-session---2024-meeting.html
  - Transcript at steadycompounding.com/transcript/brk-2024/
  - Moneycontrol live blog, for the Paramount and Abel quotes
- Reuters, 2024-08-03 (Q2 2024: net equity sales $75.5B, cash $276.9B): https://www.reuters.com/business/finance/berkshires-cash-hits-277-bln-buffett-slashes-apple-stake-operating-profit-sets-2024-08-03/
- 2024 annual letter, 2025-02-22: https://www.berkshirehathaway.com/letters/2024ltr.pdf
- CNBC, 2025-02-22 (net equity sales of $134B in 2024): https://www.cnbc.com/2025/02/22/warren-buffett-amasses-more-cash-and-sells-more-stock-but-doesnt-explain-why-in-annual-letter.html
- Business Insider, 2025-02-24 (2024: about $9B bought, $143B sold; buybacks $2.6B in Q1 2024, $0.3B in Q2 2024, none after): https://www.businessinsider.com/warren-buffett-berkshire-hathaway-cash-pile-stock-sales-tax-record-2025-2
- 2025 AGM, 2025-05-03: transcript at alpha-file.com/content/21605, plus Reuters and AP coverage.
- 2025-08-14:
  - CNBC on UNH: https://www.cnbc.com/2025/08/14/warren-buffetts-berkshire-hathaway-unh.html
  - Morningstar: https://www.morningstar.com/stocks/berkshire-hathaway-buys-unitedhealth-reveals-mystery-stocks
- Thanksgiving letter, 2025-11-10: https://www.berkshirehathaway.com/news/nov1025.pdf
- CNBC on Alphabet, 2025-11-15: https://www.cnbc.com/2025/11/15/berkshire-hathaways-surprising-new-tech-stake.html
- Combs leaves, 2025-12-08:
  - Berkshire release https://berkshirehathaway.com/news/dec0825.pdf
  - JPMorgan release https://www.jpmorganchase.com/newsroom/press-releases/2025/jpmorganchase-names-todd-combs-to-head-strategic-investment-group
  - Morningstar https://www.morningstar.com/stocks/berkshire-hathaway-combs-departure-leaves-investment-portfolio-duties-hands-abel-others
- CNBC on Q4 2025, 2026-02-21: https://www.cnbc.com/2026/02/21/berkshire-was-a-net-seller-of-stocks-in-buffetts-final-quarter-as-ceo.html
- 2025 annual letter (Abel's first), 2026-02-28: https://www.berkshirehathaway.com/letters/2025ltr.pdf
- Reuters, 2026-02-28 (YE2025 cash $373.3B; 13th straight quarter as a net seller; sixth with no buybacks): https://www.reuters.com/sustainability/boards-policy-regulation/berkshire-hathaway-profit-falls-writedowns-lower-insurance-income-2026-02-28/
- Business Insider, 2026-02-28: https://www.businessinsider.com/warren-buffett-berkshire-ceo-stock-sales-cash-pile-buybacks-earnings-2026-2
- 2026 AGM, 2026-05-02:
  - Transcript https://www.good-investing.net/berkshire-hathaway-annual-meeting/transcripts/2026-transcript/
  - CNBC video https://www.youtube.com/watch?v=mGbVNMchrmQ
  - CNBC live blog https://www.cnbc.com/2026/05/02/warren-buffett-berkshire-hathaway-annual-meeting-2026-live-updates.html
  - Reuters https://www.reuters.com/sustainability/boards-policy-regulation/berkshire-shareholders-head-greg-abels-first-annual-meeting-with-buffett-2026-05-02/
  - CNBC excerpts, 2026-05-01: https://www.cnbc.com/2026/05/01/cnbc-excerpts-berkshire-hathaway-ceo-greg-abel-speaks-with-cnbcs-becky-quick-on-squawk-box-today.html (snippet only)
  - Bridges Trust commentary, 2026-05-06: https://bridgestrust.com/2026-berkshire-commentary/
- Q1 2026 13F coverage, 2026-05-15 to 05-19:
  - Morningstar https://www.morningstar.com/stocks/berkshire-hathaway-13f-abel-takes-hard-look-portfolio-sales-outweigh-purchases
  - Investopedia https://www.investopedia.com/berkshire-hathaway-13f-q1-2026-stocks-greg-abel-warren-buffett-11976563
  - S&P Global https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/5/berkshire-exits-unitedhealth-aon-visa-mastercard-in-1st-quarter-with-new-ceo-101770246
  - AP via Yahoo https://finance.yahoo.com/markets/stocks/articles/berkshire-hathaway-triples-alphabet-stake-224426821.html
  - Barchart https://www.barchart.com/story/news/2011500/warren-buffetts-berkshire-hathaway-dumped-16-stocks-in-q1-but-the-chevron-sale-was-the-largest
  - FilingSpy https://filingspy.com/investors/warren-buffett/q/2026q1
- Alphabet private placement and Taylor Morrison, 2026-06-01 and 06-02:
  - CNBC https://www.cnbc.com/2026/06/01/berkshire-hathaway-alphabet-investment.html
  - Reuters https://www.reuters.com/legal/transactional/berkshire-under-new-ceo-greg-abel-invests-168-billion-two-days-2026-06-01/
  - CNBC https://www.cnbc.com/2026/06/02/greg-abel-channels-buffetts-dealmaking-style-in-17-billion-deal-spree.html
  - AP https://apnews.com/article/berkshire-hathaway-warren-buffett-abel-taylor-morrison-b7bf3c0c23cbe5e4e9d2f2bd184eb06a
- Q2 2026 13F and 10-Q coverage, 2026-08-14 to 08-17:
  - Morningstar https://www.morningstar.com/stocks/berkshire-hathaway-13f-purchases-outweighed-sales-alphabet-most-traded-q2 (contains the Lennar error noted above)
  - CNBC https://www.cnbc.com/2026/08/15/berkshire-adds-17-billion-to-alphabet-stake.html
  - Forbes https://www.forbes.com/sites/bill_stone/2026/08/15/berkshire-hathaway-turns-buyer-as-buffett-backs-alphabet/
  - AP https://apnews.com/article/berkshire-hathaway-warren-buffett-greg-abel-portfolio-fd9d6750d34f208c338e305759bcf6c9
  - GestorLens https://www.gestorlens.com/en/inversor/warren-buffett/2026-t2
- Lennar, September and October 2026:
  - CNBC https://www.cnbc.com/2026/09/22/lennar-shares-pop-as-berkshire-builds-almost-a-10percent-stake-in-beleaguered-homebuilder.html
  - Realtywire https://realtywire.com/berkshire-lennar-10-percent-owner/
  - CNBC https://www.cnbc.com/2026/10/03/berkshire-buys-more-lennar-shares-but-pace-of-purchases-slows.html
- Bending Spoons, 2026-10-14 to 10-17:
  - Issuer release https://investors.bendingspoons.com/newsroom/berkshire-hathaway-invests-further-in-bending-spoons
  - CNBC https://www.cnbc.com/2026/10/14/berkshire-hathaway-investment-bending-spoons.html
  - Axios https://www.axios.com/2026/10/15/bending-spoons-aol-berkshire-hathaway
  - Motley Fool https://www.fool.com/investing/2026/10/17/berkshire-hathaway-million-in-ipo-invest-bsp/
- Q3 2026 results, 2026-11-07 to 11-09:
  - CNBC https://www.cnbc.com/2026/11/07/berkshire-hathaway-q3-2026-earnings-buybacks.html
  - Reuters via Investing.com https://au.investing.com/news/stock-market-news/berkshire-hathaway-speeds-up-stock-buybacks-though-profit-falls-4753716
  - Fortune https://fortune.com/2026/11/07/berkshire-hathaway-stock-brk-q3-earnings-investment-portfolio-buybacks/
  - CrowdfundedWealth 10-Q breakdown https://www.crowdfundedwealth.com/articles/berkshire-hathaway-10-q-q3-2026-cash-buybacks-stock-sales
- Q3 2026 13F coverage, 2026-11-16 and 11-17:
  - Morningstar https://www.morningstar.com/stocks/berkshire-hathaway-13f-sales-outweighed-purchases-swapping-bank-america-stock-lennar
  - Investor Data Digest https://www.investordatadigest.com/news/berkshire-hathaway-q3-2026-13f-trims-bank-of-america-doubles-lennar-adds-bending-spoons-nov-2026
  - Kiplinger https://www.kiplinger.com/investing/stocks/stocks-berkshire-hathaway-bought-sold-q3-2026
  - StockAnalysis https://stockanalysis.com/news/berkshire-q3-2026-13f-delta-bank-of-america/
  - Benzinga https://www.benzinga.com/trading-ideas/long-ideas/26/11/63324690/berkshire-hathaway-takes-stake-in-aol-owner-bending-spoons-nearly-doubles-lennar-holding
  - Quiver https://www.quiverquant.com/news/Berkshire+Hathaway+Discloses+New+Bending+Spoons+Stake%2C+Nearly+Doubles+Lennar+Holdings

## Problems hit

- **Exa returned the 13F XML with its tags stripped.** I parsed the values by their position instead (fixed field order). Every quarter still reconciled exactly with its cover page.
- **The Exa fetch results were inline rather than saved to disk.** I recovered them from my own session transcript.
- **Exa returned CRAWL_LIVECRAWL_TIMEOUT for several EDGAR browse pages:**
  - browse-edgar type=SCHEDULE 13D
  - SCHEDULE%2013D and SCHEDULE%2013G
  - type=4
  - type=N-PX
  - type=D
- **The browse page for type=SC 13 loaded but was stale.** It ends 2024-11-25.
- **Resolved later:** the SEC submissions file and owner page (both via Exa) replaced the timed-out and stale browse pages for the 13D/G, Form 3/4 and N-PX checks. The archive folder listing also loaded but carries no form types.
- **The browse list "10-" looked stale.** At first I took 0001193125-26-445930 (2026-11-03) for the Q3 2026 10-Q. It is a SiriusXM Form 4. I read the Q3 2026 10-Q at berkshirehathaway.com instead.
- **Paywalled or truncated sources, used only as headlines or snippets:**
  - Bloomberg, 2024-08-03 and 2026-08-14
  - Seeking Alpha, 2026-05-15 and 2026-11-16
  - The CNBC Squawk Box excerpts
- **No sign-in, purchase or human-verification check was met.**
- **Sources I looked for and couldn't find:**
  - Any Berkshire statement on who (Abel, Buffett or Weschler) made a specific 2026 purchase, such as Delta, Macy's, NYT, Bending Spoons or the Lennar add.
  - (Resolved) The Q4 2023, Q4 2024 and Q4 2025 equity purchases and sales, now derived as 10-K minus nine-month 10-Q from SEC's XBRL API; see "10-K, 10-Q and earnings releases" above.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
