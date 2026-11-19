# Himalaya Capital Management (Li Lu): research log

Written 2026-11-19. Covers 13F filings for Q4 2023 through Q3 2026; CIK 0001709323. All web access was through Exa (web_search_exa and web_fetch_exa), and there were no Exa failures. Dates below are filing or publication dates. The 13F filing dates are the last-modified times shown in the EDGAR archive folder.

## Odd items, read these first

1. **Values in thousands in two quarters.** The Q4 2023 and Q1 2024 information tables report values in thousands of dollars, not whole dollars. The brief assumed whole dollars for all twelve quarters; that is wrong for this filer. Cover totals were 2,059,252 and 2,260,390, which only make sense in thousands. I rescaled both quarters ×1000 in the CSVs. Whole dollars start with Q2 2024.
2. **Q4 2025 amendment.** The original 13F-HR (0002043585-26-000011, 2026-02-17) had the share counts for Alphabet Class A (CUSIP 02079K305) and Class C (02079K107) swapped. The 13F-HR/A (0002043585-26-000012, 2026-02-18, amendmentType RESTATEMENT, amendmentNo 1) corrected them. `holdings/2025-Q4.csv` uses the amendment. Values and total are the same in both versions; only the class labels moved.
3. **Filer change of accession prefix.** From Q1 2025, the 13Fs were filed through an agent whose accession prefix is 0002043585. N-PX filings still use the firm's own 0001709323 prefix.
4. **Reconciliation.**
   - Eleven of twelve quarters match the cover-page total value and entry count exactly.
   - 2026-Q2 rows sum to $3,702,921,099 against a cover total of $3,702,921,098. That is a $1 rounding difference in the filing, and I left it as filed.
   - Every row is SH (no PRN). There are no put/call rows, no other-manager column (0 other included managers), and isConfidentialOmitted is false in every quarter.
5. **Late filings and missing quarters.** None. Q3 2026 was filed 2026-11-16 because November 14 fell on a Saturday. No 13F-NT was filed.
6. **Look-alike filer.** "Himalaya Capital Ltd," CIK 2094573, formerly NovumX Ltd, filed a Form D/A on 2026-11-10. It names Li Lu as director at "301 2nd Ave, Suite 2100, Seattle"; the real firm is at 1301 2nd Ave, Suite 2100. It reports $100K sold, a $10K minimum and every exemption ticked. A GlobeNewswire release of 2026-11-16 promotes it. I treated it as not the manager; see the profile.
7. **No 2025 N-PX** appears in the archive folder. N-PX filings exist for 2024 and 2026 only.

## 13F filings read (full submission .txt from the archive folder)

Archive folder: https://www.sec.gov/Archives/edgar/data/1709323/

| Period | Form | Accession | Filed | Total value (cover) | Entries | URL |
|---|---|---|---|---|---|---|
| 2022-12-31 (context) | 13F-HR | 0001709323-23-000001 | 2023-02-14 | 1,927,217 (thousands) | – | https://www.sec.gov/Archives/edgar/data/1709323/000170932323000001/0001709323-23-000001.txt |
| 2023-09-30 (context) | 13F-HR | 0001709323-23-000006 | 2023-11-14 | 1,820,102 (thousands) | 6 | https://www.sec.gov/Archives/edgar/data/1709323/000170932323000006/0001709323-23-000006.txt |
| 2023-12-31 | 13F-HR | 0001709323-24-000001 | 2024-02-14 | 2,059,252 (thousands) | 6 | https://www.sec.gov/Archives/edgar/data/1709323/000170932324000001/0001709323-24-000001.txt |
| 2024-03-31 | 13F-HR | 0001709323-24-000004 | 2024-05-15 | 2,260,390 (thousands) | 6 | https://www.sec.gov/Archives/edgar/data/1709323/000170932324000004/0001709323-24-000004.txt |
| 2024-06-30 | 13F-HR | 0001709323-24-000005 | 2024-08-14 | 2,561,616,158 | 7 | https://www.sec.gov/Archives/edgar/data/1709323/000170932324000005/0001709323-24-000005.txt |
| 2024-09-30 | 13F-HR | 0001709323-24-000009 | 2024-11-14 | 2,472,447,859 | 8 | https://www.sec.gov/Archives/edgar/data/1709323/000170932324000009/0001709323-24-000009.txt |
| 2024-12-31 | 13F-HR | 0001709323-25-000001 | 2025-02-14 | 2,711,379,783 | 8 | https://www.sec.gov/Archives/edgar/data/1709323/000170932325000001/0001709323-25-000001.txt |
| 2025-03-31 | 13F-HR | 0002043585-25-000004 | 2025-05-15 | 2,212,436,862 | 8 | https://www.sec.gov/Archives/edgar/data/1709323/000204358525000004/0002043585-25-000004.txt |
| 2025-06-30 | 13F-HR | 0002043585-25-000010 | 2025-08-14 | 2,689,202,442 | 9 | https://www.sec.gov/Archives/edgar/data/1709323/000204358525000010/0002043585-25-000010.txt |
| 2025-09-30 | 13F-HR | 0002043585-25-000015 | 2025-11-12 | 3,230,264,839 | 9 | https://www.sec.gov/Archives/edgar/data/1709323/000204358525000015/0002043585-25-000015.txt |
| 2025-12-31 | 13F-HR (superseded) | 0002043585-26-000011 | 2026-02-17 | 3,568,876,223 | 9 | https://www.sec.gov/Archives/edgar/data/1709323/000204358526000011/0002043585-26-000011.txt |
| 2025-12-31 | 13F-HR/A, restatement (used) | 0002043585-26-000012 | 2026-02-18 | 3,568,876,223 | 9 | https://www.sec.gov/Archives/edgar/data/1709323/000204358526000012/0002043585-26-000012.txt |
| 2026-03-31 | 13F-HR | 0002043585-26-000013 | 2026-05-15 | 3,201,226,867 | 14 | https://www.sec.gov/Archives/edgar/data/1709323/000204358526000013/0002043585-26-000013.txt |
| 2026-06-30 | 13F-HR | 0002043585-26-000022 | 2026-08-14 | 3,702,921,098 | 8 | https://www.sec.gov/Archives/edgar/data/1709323/000204358526000022/0002043585-26-000022.txt |
| 2026-09-30 | 13F-HR | 0002043585-26-000030 | 2026-11-16 | 3,781,431,260 | 8 | https://www.sec.gov/Archives/edgar/data/1709323/000204358526000030/0002043585-26-000030.txt |

Every cover page reads: report type 13F HOLDINGS REPORT; 13F file number 028-18090; signer Paul Teng, CCO. From Q1 2025 the cover also carries CRD 000157594 and SEC file 801-72763. I did not use the EDGAR browse page.

## Other SEC filings

- **Form N-PX.**
  - 2024: 0001709323-24-000006, filed 2024-08-26. Institutional manager notice report; the reporting person did not exercise voting. The text says the firm "felt no proxy voting matters were material" and abstained. https://www.sec.gov/Archives/edgar/data/1709323/000170932324000006/0001709323-24-000006.txt
  - 2026: 0001709323-26-000001, filed 2026-08-31, of the same type. https://www.sec.gov/Archives/edgar/data/1709323/000170932326000001/0001709323-26-000001.txt
  - 2025: none found in the archive folder.
- **Schedule 13D and 13G.** I looked in the CIK 1709323 archive folder for the period and found none. That is expected, since no US position comes near 5% of its issuer; Sable Offshore, at about 1.25%, was the largest.
- **Forms 3, 4 and 5.** None in the period. They don't apply, because Himalaya is not a 10% holder of any US issuer.
- **Form ADV.**
  - Part 1: https://reports.adviserinfo.sec.gov/reports/ADV/157594/PDF/157594.pdf, the current version, read 2026-11-19. It gives:
    - RAUM of $21,392,207,523 at 2025-12-31, of which about $4.76B is for non-US clients
    - 21 employees, 15 of them advisory
    - fund gross assets of about $21.4B and 638 beneficial owners
    - HedgeServ as administrator
  - Part 2A brochure, dated 2026-03-31: https://files.adviserinfo.sec.gov/IAPD/Content/Common/crd_iapd_Brochure.aspx?BRCHR_VRSN_ID=1034902. It gives the fees (no management fee; expenses capped at 0.375%; 25% of gains over a 6% compounded hurdle), a $25M minimum, the geographic focus with the "better opportunities in Asia… especially in Greater China" sentence, leverage and borrowing for redemptions, the 40% private-company limit, two discretionary accounts and semiannual LP reports.
  - Earlier RAUM figures came from IAPD snapshots and search results: about $14.17B (2022-12-31), $14.99B (2023-12-31) and $17.18B (2024-12-31). I did not open every historical ADV PDF; earlier brochure versions were not fetched.
- **Form D: Himalaya Capital Investors, L.P.** (onshore master; CIK 1576745; folder https://www.sec.gov/Archives/edgar/data/1576745/). Amounts are cumulative gross amounts sold since the first sale, not net of redemptions.
  - 0001576745-23-000001 (Sep 2023): $8,007,837,441 sold; 440 investors; minimum $100M. https://www.sec.gov/Archives/edgar/data/1576745/000157674523000001/0001576745-23-000001.txt
  - 0001576745-24-000001 (Sep 2024): $8,195,339,409; 448 investors. From the folder listing and formds.com.
  - 0001193125-25-205154 (Sep 2025): $8,533,920,871; 464 investors. https://www.sec.gov/Archives/edgar/data/1576745/000119312525205154/0001193125-25-205154.txt
  - 0001193125-26-386645 (Sep 2026): $9,238,800,390; 503 investors. Via https://www.formds.com/issuers/himalaya-capital-investors-l-p
- **Form D: Himalaya Capital Investors (Offshore), L.P.** (CIK 1747706)
  - Sep 2023: $700.5M sold; 133 investors. Via formds.com.
  - 0001747706-24-000001 (Sep 2024): $726.75M; 133 investors. https://www.sec.gov/Archives/edgar/data/1747706/000174770624000001/xslFormDX01/primary_doc.xml
  - 0001193125-26-386632 (Sep 2026): $1,710,788,137; 187 investors. https://capedge.com/filing/1747706/0001193125-26-386632/D-A (also https://www.formds.com/issuers/himalaya-capital-investors-offshore-l-p)
  - No 2025 amendment was seen.
- **Form D: iCapital-Himalaya Capital Investors feeder** (CIK 2078361; folder https://www.sec.gov/Archives/edgar/data/2078361/)
  - 0002033548-25-000075 (Jul 2025): first sale 2025-07-01; $18.05M sold; 39 investors. https://www.sec.gov/Archives/edgar/data/2078361/0002033548-25-000075.txt
  - 0002078361-26-000001 (Jul 2026): $42.335M; 79 investors. https://www.sec.gov/Archives/edgar/data/2078361/000207836126000001/0002078361-26-000001.txt
- **Look-alike, not the manager:** Himalaya Capital Ltd, CIK 2094573. Folder https://www.sec.gov/Archives/edgar/data/2094573/; Form D/A of 2026-11-10 at https://www.sec.gov/Archives/edgar/data/2094573/000209457326000002/xslFormDX01/primary_doc.xml
- **N-CSR and N-PORT:** not applicable, since Himalaya runs no registered fund.

## HKEX disclosure of interests (positions invisible on a 13F)

- **BYD H-shares, Li Lu notice of July 2021** (sale to 62,879,100 shares, 6.00%): https://di.hkex.com.hk/di/NSForm1.aspx?fn=IS20210714E00253&lang=EN&pn=li+lu&sa1=pl&sa2=np&sced=17%2F08%2F2021&scpid1=35238&scpid2=2508&scpid3=2&scsd=17%2F08%2F2020
- **BYD H-shares, November 2021** (fell below 5%, to 4.97%, through dilution; no notices since): https://di.hkex.com.hk/di/NSForm1.aspx?corpn=BYD+Co.+Ltd.++-+H+Shares&ed=04%2F09%2F2022&fn=IS20211111E00105&g_lang=en&lang=EN&sa1=cl&sa2=ns&sc=1211&sced=04%2F09%2F2022&scsd=04%2F08%2F2021
- **Postal Savings Bank of China H-shares, January 2021** (stake built to 6.42%): https://di.hkex.com.hk/di/NSForm1.aspx?fn=IS20210120E00328&lang=EN&pn=li+lu&sa1=pl&sa2=np&sced=27%2F01%2F2024&scpid1=35238&scpid2=142788&scpid3=2&scsd=27%2F01%2F2018
- **PSBC, sale on 2024-12-06** (20M shares; 6.03%→5.93%): https://di.hkex.com.hk/di/NSForm1.aspx?fn=IS20241211E00055&g_lang=zh-HK&lang=ZH
- **PSBC, sale on 2025-05-08** (10.387M shares; 5.02%→4.96%, below the disclosure threshold): seen in HKEX search results. I did not keep a separate URL for this form.
- A BYD Form 3A director notice (DA20250311E00316) came up in search. It is a BYD director's filing, not Himalaya's, and I did not use it.

## The manager's own words, oldest first

| Date | Source | URL | Notes |
|---|---|---|---|
| Undated, older | himcap.com publications list | https://www.himcap.com/publications | Lists the 2010 *Poor Charlie's Almanack* foreword, the 2013 Graham & Doddsville interview, the 2015 and 2018/2019 PKU and modernization talks, and the 2023 Munger remembrance. Older items are used only as background. |
| 2023-11-30 | "Remembering My Teacher Charlie Munger" | listed at https://www.himcap.com/publications | Only the listing and summary were read; I did not read the full text. |
| 2024-11-28 | Zhenghe Island online interview for the Munger anniversary (Chinese) | English versions: https://medium.com/@iamalexcarter/latest-interview-transcripts-li-lu-on-value-investing-charlie-munger-and-the-ai-revolution-34f3605a124f (2024-12-16) and https://www.hermitresearch.com/p/oij-24-li-lu-interviews (2025-03-11) | Source of the four reasons for selling, the BYD holding-period remarks, and the 1998 redemption episode. These are translations by third parties. |
| 2024-12-07 | PKU Guanghua 10th-anniversary keynote, "Global Value Investing in Our Era" | https://offpisteinvesting.com/wp-content/uploads/2025/01/Global-Value-Investing-in-Our-Era.pdf (English translation, Jan 2025; also listed on himcap.com) | The six principles, purchasing power, macro versus micro, the China "perplexity," and the middle-income trap. |
| 2026-04-03 | BYD official 《有请》 dialogue with BYD's company secretary and CIO, Li Qian (Chinese) | https://finance.sina.com.cn/stock/stockzmt/2026-04-04/doc-inhtipvz7969350.shtml ; https://finance.sina.com.cn/wm/2026-04-05/doc-inhtmhff7183424.shtml ; https://finance.sina.com.cn/wm/2026-04-05/doc-inhtmhff7191215.shtml ; https://finance.sina.com.cn/wm/2026-04-07/doc-inhtsrqu3446939.shtml ; https://finance.sina.com.cn/wm/2026-04-08/doc-inhttxki6567127.shtml ; https://caifuhao.eastmoney.com/news/1689532726 (2026-04-05) ; https://news.qq.com/rain/a/20260423A03U1G00 (2026-04-23) ; https://www.xueqiu.com/4506124050/384299776 (2026-04-17, presented as a full transcript "authorised by Li Lu") | Says all BYD shares bought in 2002 are still held, and that the initial position was about 10% of the fund. |
| 2026-10-05 | Columbia 36th Annual Graham & Dodd Luncheon, keynote and Q&A | https://business.columbia.edu/sites/default/files-efs/imce-uploads/36th%20Annual%20Graham%20&%20Dodd%20Luncheon%20Transcript%20%2820261005%29%20CBS.pdf | AI as "tool versus creature," market bifurcation, China's "objective or cost," "build that church in Asia," and crypto as "fundamentally bogus." This is the most recent and most important source. |

## Third-party sources (commentary only; none is a source of Li Lu's reasons)

- Eagle Point Capital, "What Does Li Lu See in a Pre-Revenue SPAC?", 2024-12-14: https://eaglepointcapital.substack.com/p/what-does-li-lu-see-in-a-pre-revenue. Paywalled; the free part only.
- Xueqiu post, 2025-07-03, on the PSBC sale of 2024-12-06 (about 1.178B H-shares left afterwards): https://www.xueqiu.com/1676777498/341050266
- Margin of Sanity, 2025-08-31, on offshore drillers and Sable: https://marginofsanity.substack.com/p/a-bet-on-offshore-drillers-deep-value. Paywalled.
- Seeking Alpha, "Sable Offshore: Risky, But Deeply Discounted", 2025-09-11: https://seekingalpha.com/article/4822167-sable-offshore-risky-but-deeply-discounted. Snippet only.
- Sina / 六里投资报, 2026-02-24, on the Q4 2025 13Fs of Duan Yongping and Li Lu: https://finance.sina.com.cn/money/fund/jjyj/2026-02-24/doc-inhnxxka8492695.shtml
- Valuesider, BAC exit in Q2 2026 ("held for ~6 years"), 2026-08-14: https://valuesider.com/insights/2026-q2/li-lu-bac-position-exited. Also the SOC history: https://valuesider.com/guru/li-lu-himalaya-capital-management/history/SOC
- 163.com / 证券之星, 2026-08-19, on the Q2 2026 changes: https://www.163.com/dy/article/L4NADU4J051984TV.html
- Compound with René, "Li Lu Sold Three Compounder Darlings to Double Down on This Stock", 2026-08-20: https://www.compoundwithrene.com/p/unorthodox-ideas-from-13-f-season-1bc. Paywalled. It mentions the earlier 2020–21 PDD holding.
- InvestorLens, 2026-10-04, on the Q2 2026 PDD buy: https://www.investorlens.capital/blog/2026-10-04-li-lu-himalaya-q2-2026-pdd
- tradingjournl, Q2 2026, 2026-10-09/10: https://www.tradingjournl.io/blog/himalaya-capital-13f-2026-q2/en. Also the source of the old Ilsung Pharmaceuticals (Korea, 2015) item.
- DeepValues, Q3 2026, 2026-11-17: https://research.deepvalues.ai/insights/2026-11-17-li-lu-q3-2026-13f-portfolio-research/. It is AI-drafted and notes that Himalaya gives no commentary on 13F changes.
- StockCircle, SOC transactions (exit near $9 against a reported $23.63 entry): https://stockcircle.com/portfolio/himalaya-capital/soc/transactions
- Dataroma activity and SOC history: https://www.dataroma.com/m/m_activity.php?m=HC&typ=a ; https://www.dataroma.com/m/hist/hist.php?f=HC&s=SOC
- GlobeNewswire release on the look-alike "Himalaya Capital" entity, 2026-11-16: https://www.globenewswire.com/news-release/2026/11/16/3403992/0/en/himalaya-capital-the-evolution-of-a-u-s-value-investment-firm-and-related-sec-and-fincen-public-registration-records-draw-attention.html
- I set aside one 163.com article (https://www.163.com/dy/article/JK4015H705568YYS.html). Its figures for a reduction from 9.03% to 7.96% describe a different shareholder, not Himalaya.
- Hermit Research, cited above, gives 17.5% gross and 14.1% net annual returns for 1998–2022. These are unverified secondary figures and are not used in the profile.

## Problems and gaps

- **Paywalls:** Eagle Point Capital, Compound with René and Margin of Sanity. I used only the free highlights, and did not subscribe or sign in.
- **Not found:**
  - Any statement by Li Lu explaining a specific 13F trade in 2023–26, including Alphabet, BAC, PDD, the info-services basket and Berkshire. Searches in English and Chinese found only third-party commentary.
  - Himalaya LP letters. They are semiannual and not public.
  - A 2025 N-PX.
  - The offshore feeder's 2025 Form D/A.
  - Any current Korea or Japan holding disclosures.
  - A current BYD share count. Nothing has been disclosed since it fell below 5% in 2021.
- **Not read in full:** the 2023-11-30 Munger remembrance (only the listing was seen) and older ADV brochure versions.
- **Tools:** I used the EDGAR archive folder listings instead of the browse page, as the brief advised. Direct sec.gov access through curl was not attempted, since it is blocked.
- **Scripts:** the parsing and build script lives in the scratch directory, not the shared folder: /tmp/claude-0/-home-user/e63fcd6d-0599-5972-896a-3d4b7157bae9/scratchpad/himalaya/build.py. The holdings data were hand-transcribed from the fetched filing text, because Exa strips the XML tags, and checked against the cover totals.


## 2026-11-19: holdings rebuilt from SEC filings

The holdings CSVs were regenerated by `scripts/build13f.py` from the information-table XML fetched directly from sec.gov, and compared row by row (CUSIP plus put/call) with the hand-built CSVs. Shares and values were identical in every quarter, so no transcription error was found. Differences are cosmetic: issuer and class text is now as filed rather than normalised by hand, and `pct_of_portfolio` has four decimals. Each holdings folder now has `sources.csv`, listing the accessions behind each quarter and how amendments were applied. Filer errors that were never amended are fixed in `managers.yaml` (`corrections`, `accepted_gaps`) rather than by hand.
