# AltaRock Partners (CIK 0001631014): research log

Written 2026-11-19. All web access through Exa (`web_fetch_exa`, `web_search_exa`); no Exa failures on anything that mattered.

## Odd things first

- **Filer entity changed mid-period.** AltaRock Partners, LLC (Beverly, MA; EIN 04-3607351) was succeeded by AltaRock Partners LP (West Palm Beach, FL; EIN 93-4288428). Same CIK, same 13F file number 028-16669, same CRD 161005. The 13Fs for Q4 2023 and Q1 2024 were filed by the LLC; everything from the Q1 2024 amendment on is the LP. The ADV brochure says there was "no change in personnel or control after the succession".
- **One amendment, harmless.** 13F-HR/A 0001104659-24-063732 (filed 2024-05-21) restates Q1 2024 ("RESTATEMENT", amendment no. 1) under the new LP name and Florida address. The holdings table is identical to the original (8 rows, $4,653,506,114, every row equal). I saved Q1 2024 from the original and treat the amendment as a name/address refiling.
- **Two filings landed one business day after the deadline.** Q4 2023 was accepted 2024-02-14 18:12 ET, after EDGAR's 5:30 pm cutoff, so its official filing date is 2024-02-15 (deadline was 02-14). Q2 2026 was signed 2026-08-14 (the deadline, a Friday) but accepted Monday 2026-08-17 07:00. Every other quarter was filed on or a day before its deadline. No 13F-NT notices in the folder.
- **Filing-agent accession prefix.** Every 13F in the period carries the agent prefix 0001104659 rather than AltaRock's own CIK. The 2026 N-PX was self-filed (0001631014-26-000002). Find filings by listing the CIK folder, not by guessing accession numbers.
- **All totals reconciled exactly.** For all 12 quarters (and the Q3 2023 comparison quarter) the parsed row count and value sum equal the cover page's entry total and value total to the dollar. Values are in whole dollars throughout. Every row is common stock (class "COMM"), SH not PRN, investment discretion SOLE, no put/call, no other managers (cover shows 0 other included managers), no confidential-treatment indication. No splits affected any holding in the period (Alphabet's and Amazon's 20-for-1 splits were in 2022).
- **Tiny residual "stub" positions.** After near-exits, AltaRock leaves small residues that persist for quarters: Charter 6,025 shares (Q2 2024 to Q4 2024, exited Q1 2025), Fair Isaac 670 shares (Q4 2024 to Q3 2025, exited Q4 2025), Hilton about 15,200 shares (Q1 2026 onward), Alphabet about 40,000 shares (Q1 2026 onward). They are kept in the CSVs as filed.
- **Non-13F holding found.** The 2024 N-PX shows a say-on-pay vote on 17,143 shares of Constellation Software (Toronto-listed, CUSIP 21037X100) in May 2024. It is not a 13F security, so it never appears in the 13F. Later N-PX filings show no Constellation vote; whether it is still held is unknown.
- **13F covers roughly 90% of reported assets.** Form ADV regulatory AUM: about $5.41B at 2024-12-31 and $5,663,773,000 at 2025-12-31, against 13F totals of $4.94B and $5.10B on the same dates.

## 13F filings read (CIK folder https://www.sec.gov/Archives/edgar/data/1631014/)

Full submission `.txt` fetched for each (cover page plus information table). Index pages fetched for all to confirm form type, period, acceptance time.

| Period | Form | Accession | Accepted (ET) | Deadline | Entries | Total value (USD) | Reconciled |
|---|---|---|---|---|---|---|---|
| 2023-09-30 (context only, not saved) | 13F-HR | 0001104659-23-117428 | 2023-11-13 19:59 (filed 11-14) | 11-14 | 8 | 3,992,658,987 | yes |
| 2023-12-31 | 13F-HR | 0001104659-24-024107 | 2024-02-14 18:12 (filed 02-15) | 02-14 | 8 | 4,483,273,009 | yes |
| 2024-03-31 | 13F-HR | 0001104659-24-061859 | 2024-05-15 15:30 | 05-15 | 8 | 4,653,506,114 | yes |
| 2024-03-31 | 13F-HR/A (restatement, identical) | 0001104659-24-063732 | 2024-05-21 11:50 | | 8 | 4,653,506,114 | yes |
| 2024-06-30 | 13F-HR | 0001104659-24-089560 | 2024-08-14 15:35 | 08-14 | 9 | 4,858,528,640 | yes |
| 2024-09-30 | 13F-HR | 0001104659-24-117526 | 2024-11-13 13:14 | 11-14 | 9 | 5,077,280,606 | yes |
| 2024-12-31 | 13F-HR | 0001104659-25-014306 | 2025-02-14 17:12 | 02-14 | 10 | 4,943,610,970 | yes |
| 2025-03-31 | 13F-HR | 0001104659-25-048610 | 2025-05-14 17:15 | 05-15 | 9 | 4,973,323,258 | yes |
| 2025-06-30 | 13F-HR | 0001104659-25-078208 | 2025-08-14 10:24 | 08-14 | 9 | 5,477,355,057 | yes |
| 2025-09-30 | 13F-HR | 0001104659-25-112002 | 2025-11-14 08:56 | 11-14 | 9 | 5,469,137,744 | yes |
| 2025-12-31 | 13F-HR | 0001104659-26-015359 | 2026-02-13 17:10 | 02-17 (weekend + holiday) | 8 | 5,100,067,772 | yes |
| 2026-03-31 | 13F-HR | 0001104659-26-062170 | 2026-05-15 12:34 | 05-15 | 8 | 4,126,337,614 | yes |
| 2026-06-30 | 13F-HR | 0001104659-26-097527 | 2026-08-17 07:00 (signed 08-14) | 08-14 | 8 | 4,239,761,490 | yes |
| 2026-09-30 | 13F-HR | 0001104659-26-127198 | 2026-11-13 17:00 | 11-16 (weekend) | 8 | 4,213,339,919 | yes |

URLs follow the pattern `https://www.sec.gov/Archives/edgar/data/1631014/<accession without dashes>/<accession>.txt` and `.../<accession>-index.html`.

Older 13Fs read for holding-period context only (not saved as CSVs): Q4 2015 (0001144204-16-079521, values in thousands), Q4 2019 (0001104659-20-020035, thousands), Q4 2021 (0001104659-22-022401, thousands), Q4 2022 (0001104659-23-019687), Q2 2023 (0001104659-23-091497).

## Other SEC filings (scope addition, 2026-11-19)

- **Form N-PX** (institutional-manager say-on-pay votes), all read in full:
  - 0001104659-24-096204, filed 2024-09-03, year to 2024-06-30. Votes on MSFT, GOOGL, AMZN, Constellation Software (17,143 sh, 2024-05-13), MA, MCO, TDG, V. All with management.
  - 0001104659-25-082925, filed 2025-08-26, year to 2025-06-30. MSFT, V, FICO (670 sh), TDG, MCO, HLT, AMZN, MA. All with management.
  - 0001631014-26-000002, filed 2026-08-21, year to 2026-06-30. MSFT, V, TDG, MCO (897,036 sh at the 2026-04-14 meeting), HLT, AMZN (7,900,514 sh at the 2026-05-20 meeting), GOOGL (43,391 sh), MA. One vote against management: Alphabet say-on-pay, 2026-06-05. Everything else with management.
  - N-PX share counts are as of each meeting's record date, so they give intra-quarter position sizes.
- **Schedule 13D / 13G**: none. The CIK folder lists only 13F-HR, 13F-HR/A and N-PX accessions from 2015 to now. AltaRock's stakes are far below 5% of these mega-caps (largest proportionally is TransDigm, roughly 1.5% of shares by my estimate), so none would be required.
- **Forms 3/4/5**: none. AltaRock is not a 10% holder of anything.
- **Form ADV Part 1**: https://reports.adviserinfo.sec.gov/reports/ADV/161005/PDF/161005.pdf (other-than-annual amendment filed 2026-04-24, read 2026-11-19). RAUM $5,663,773,000, 2 accounts, 7 employees, 3 in investment functions; principal office West Palm Beach plus a Boston office (399 Boylston St) with 3 investment staff. Schedule A: Mark T. Massey, Founder & CIO, ownership 75%+, since 02/2002; Shannon T. Cabot, CCO, since 09/2014; Big Mound Partners LLC (Massey managing member) GP since 01/2024. Private funds: AltaRock Fund, LP (Delaware, gross assets $2,412,275,000, 90 beneficial owners, $5M minimum, 16% owned by adviser and related persons, administrator NAV Consulting, prime broker Jefferies, custodians Jefferies and Pershing) and BBH AltaRock Partners Master Fund, LP (Cayman master; feeders BBH Wealth Strategies LLC AltaRock Partners Series and BBH Wealth Strategies Unit Trust AltaRock Sub-Trust; gross assets $3,251,498,000, about 2,100 beneficial owners, $100K minimum, 5% owned by adviser and related persons, 9% non-US, BBH administrator and custodian, Jefferies prime broker). Non-US client RAUM $3,251,498,000 (the Cayman master counts as a non-US client).
- **Form ADV Part 2A brochure** dated 2026-03-23: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1024091 (read 2026-11-19). The best primary statement of current strategy found. Key points: 1% management fee, 10% performance allocation over high-water mark; "The Funds managed by AltaRock follow the same strategy and have the same holdings"; "Mark Massey is the portfolio manager for the Funds and makes all investment decisions"; leverage, shorts and options permitted by fund documents. Prior brochure dated 2025-03-27 was not found as a document; its RAUM figure (about $5.4B at 2024-12-31) comes from secondary ADV-data sites (unbiased.com, specstream.ai, hedgethink.com), which agree with each other.
- **Form D**:
  - AltaRock Fund LP, CIK 0001172921, D/A 0000919574-26-000159 filed 2026-01-09 (https://www.sec.gov/Archives/edgar/data/1172921/000091957426000159/0000919574-26-000159.txt): cumulative amount sold $1,282,618,369, 121 investors, first sale 2002-04-01, $5M minimum. Earlier amendments' figures taken from formds.com's history (https://www.formds.com/issuers/altarock-fund-lp): $381.6M at 2024-01-11, $1,214.8M at 2025-01-10. The +$833M jump during 2024 is unexplained; it could be new subscriptions or a transfer between vehicles. Form D shows gross money in, never redemptions.
  - BBH Wealth Strategies LLC – AltaRock Partners Series, CIK 0001630718: D/A 0001630718-26-000001 (2026-01-22): cumulative $2,056,016,266, 2,395 investors; D/A 0001630718-25-000001 (2025-01-23): $1,850,222,090, 2,219 investors. History from https://www.formds.com/issuers/bbh-wealth-strategies-llc-altarock-partners-series: $1,672.5M at 2024-01-25, first offering January 2015.
  - BBH Wealth Strategies Unit Trust AltaRock Sub-Trust: not looked up separately (Cayman feeder).
- **N-CSR / N-PORT**: not applicable (no registered funds).

## Manager's own words and other sources (by date of the material)

- 2010-08-09, Market Folly, AltaRock mid-2010 letter to partners (excerpt, cash quote): https://www.marketfolly.com/2010/08/hedge-fund-altarocks-investing.html. The embedded letter PDF itself was not fetched.
- 2011-09-20, Market Folly, AltaRock mid-2011 letter (Domino's, Mohawk, Carter's): https://www.marketfolly.com/2011/09/mark-masseys-hedge-fund-altarock-on.html. The Scribd copy (https://www.scribd.com/document/78780537/AltaRock-Mid-2011-Letter) gave a browser-challenge page; not pursued.
- 2014-07, The Manual of Ideas interview with Mark Massey. The PDF hosted by Dorsey Asset (https://dorseyasset.com/wp-content/uploads/2016/08/Manual_Ideas_Interview_July-2014.pdf) came back via search highlights only (Massey's section not in the excerpt); the full Massey Q&A text was read at https://stockmarketeers.blogspot.com/2015/06/mark-massey-and-wide-moat-investing.html (2015-06-03 repost). GuruFocus commentary on the same interview: https://www.gurufocus.com/news/338960/a-name-worth-knowing-mark-massey-of-altarock.
- 2024-12-22, MOI/Latticework compilation reusing the 2014 quote (paywalled beyond excerpt): https://www.latticework.com/p/how-successful-investors-find-winning. No new material.
- 2025-10-14, Old Well Labs profile: https://newsletter.oldwell-labs.com/p/owl-s-low-turnover-club. Source for Massey's pre-AltaRock career (Fidelity analyst, Eureka Capital, Massey Capital Management), Scott Bradford leaving in 2017, the BBH vehicle, and a quoted BBH strategy description dated 2023-12-31 ("15% gross (12.5% net) return over at least the next 10 years"). The original BBH material was not found.
- https://www.altarockpartners.com/: a one-line holding page, no content.
- 2022 Palm Beach property articles (bizjournals, Palm Beach Daily News via rabideauklein.com): personal real estate, not used in the profile.
- Secondary 13F trackers read for cross-checking only (no new facts used): danielscrivner.com Q3/Q4 2025, insiderset.com Q3/Q4 2025, portfoliosavvy.com GOOGL history, valuesider.com GOOGL history, gigainvestors.com, investortracks.com, hedgethink.com, insidermonkey.com, ppli.com (BBH master fund page; its returns are model estimates, not reported), privatefunddata.com, fundvendors.com, 41investments Substack (2026-02-20), nasdaq.com/TipRanks (2024-06-12), valuesense.io (2025-08-27).
- **Unreliable secondary claims, flagged:** danielscrivner.com / turos.app say Massey worked at Baupost and that Scott Bradford still co-runs AltaRock. Massey's own 2014 account says Fidelity, and OWL says Bradford left in 2017; the ADV names Massey as sole decision maker. valuesense.io presents quotes ("I don't like deep value because...") that read as paraphrases of the 2014 interview, not verbatim; not used.

## Looked for and not found

- Any AltaRock letter to partners dated 2012 or later. None circulates publicly as far as Exa could find.
- Any interview, podcast, conference talk or press quote from Mark Massey after the 2014 MOI interview. None found.
- Any stated reason for any position change in 2023-2026 (Charter exit, Alphabet exit, Moody's exit, Fair Isaac and Hilton round trips, Visa/Mastercard rebuild, Microsoft/Amazon swings). None found; every explanation in the profile is my inference and is marked as such.
- The BBH 2023-12-31 fact sheet quoted by OWL.
- RAUM as of 2023-12-31 (2024 annual ADV).
- Whether Constellation Software is still held.

## Parsing notes

Exa returns EDGAR XML with tags stripped, so the information tables were transcribed field by field (name, class, CUSIP, value, shares, SH, SOLE, voting) into a small Python data file in my scratch directory, then summed and checked against each cover page before writing `holdings/<YYYY>-Q<N>.csv`. Every filing had at most 10 rows, so a transcription error would show up in the reconciliation, and none did. `pct_of_portfolio` is value / filed total.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
