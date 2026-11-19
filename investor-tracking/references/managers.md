# The tracked investors at a glance

One card per investor in the bundled baseline (as of 2026-11-19). Each card gives who decides, the
filer entities, how much of the book the 13F shows, and the quirks that trip up a reading. The full
understanding is in `baseline/<slug>/profile.md`; the sources and problems are in `log.md`. CIKs
and configuration are in `scripts/managers.yaml`, which is the version the scripts use; if the two
disagree, the YAML is the one to fix.

**Akre Capital Management** (`akre`). John Neff, sole PM since September 2023; Chuck Akre owns the
firm. 13F filer CIK 1112520; its Braddock private-fund vehicle files a 13F-NT pointing to it. The
13F shows about 80% of the flagship fund: Constellation Software, Topicus and LVMH are off it. The
fund became an ETF in October 2025 and has had heavy outflows since; redemptions are met in kind
with shares Neff chooses. Compute the flow rate first; the ETF's N-PORT (trust CIK 811030, series
S000089351) gives monthly flows. Splits in the window: O'Reilly 15:1 (2025-Q2), Brookfield 3:2
(2025-Q4). The Q1 2024 amendment re-files the whole table under a "new holdings" label.

**AltaRock Partners** (`altarock`). Mark Massey, founder and sole PM; almost no public record since
2014, so the profile leans on filings and the ADV. CIK 1631014; filings carry an agent's accession
prefix. About 90% of the book is on the 13F; Constellation Software was found through an N-PX vote.
A Brown Brothers Harriman feeder fund sits behind part of the assets, so trims can be client money.
Moved headquarters to West Palm Beach in 2024; an unexplained $833M jump in its Form D.

**Altimeter Capital** (`altimeter`). Brad Gerstner. CIK 1541617. The 13F is most of the public
book; the private and venture book is separate. Uses options occasionally (a QQQ put whose put/call
field was left blank, an SMH put in Q3 2026). Filer errors: Q2 2024 swapped Amazon's and Astera
Labs' names (corrected in `managers.yaml`); Q3 2026 rows sum $344,388 below the cover (accepted,
the filer's own gap). Grab warrants changed CUSIP in Q2 2026 (alias in the YAML). An Anthropic
position is expected from Q4 2026.

**Berkshire Hathaway** (`berkshire-hathaway`). Greg Abel, CEO since 2026; Warren Buffett, chairman;
Ted Weschler runs a book of just under $20B. CIK 1067983. The 13F is only the US stock portfolio;
the Japanese trading houses (~$50B), cash and the operating businesses are off it. Reports one
issuer across many rows (sum by CUSIP). Uses confidential treatment, revealed later by "new
holdings" amendments (Chubb, Q4 2023; four positions, Q1 2025). Form 4s on 10%-owned companies
(Lennar, DaVita, SiriusXM) preview the next 13F; the 10-K letter and 10-Q equity tables are the
richest Said and Filed sources.

**Dorsey Asset Management** (`dorsey`). Pat Dorsey. CIK 1671657; agent accession prefix. About
80–90% of the book; non-US listings are off it. Nine client accounts move in step, so the most
common percentage change is the flow rate. Booking 25:1 split (2026-Q2); Ashtead became Sunbelt
Rentals in March 2026 (a conversion, not a new buy).

**Fundsmith** (`fundsmith`). Terry Smith. Two 13F filers: Fundsmith LLP (CIK 1569205) and its
sister firm FISL (CIK 1868537), kept as a separate book (`fisl`). The LLP filing holds
about 74–78% of the group's US positions and blends several vehicles; Europe-listed holdings are
off both. Smithson's liquidation shows as a near-uniform 58% cut in 2026-Q1. Read FISL whenever a
name appears or disappears at only one of the two. The Fundsmith Equity ETF (ALPS Series Trust,
CIK 1558107, series S000097194) launched December 2025.

**Greenlea Lane Capital** (`greenlea-lane`). Josh Tarasoff, founder and sole PM; essays on his site
are his only public channel. CIK 1766504. About 75% of the book; the rest is assumed to be T-bills
or cash (unconfirmed). Q2 2025 was restated the same day to fix Brookfield's CUSIP.

**Himalaya Capital** (`himalaya`). Li Lu. CIK 1709323. Only about 14–17% of the book is on the 13F:
BYD and other Hong Kong and China listings are off it. Q4 2023 and Q1 2024 were filed in thousands
(scaled up by the build). Q4 2025 was restated the next day after swapping Alphabet A and C share
counts. A look-alike, "Himalaya Capital Ltd" (CIK 2094573), is not Li Lu's firm.

**Pershing Square** (`pershing-square`). Bill Ackman. The 13F filer was Pershing Square Capital
Management (CIK 1336528) through Q1 2026 and is Pershing Square Inc. (CIK 2026053) from Q2 2026;
the old entity now files a 13F-NT. Most longs are on the 13F; Fannie Mae and Freddie Mac, Nike via
options, Hertz via swaps and PSUS forwards are not. From 2026 the filing includes about $10.3B of
Pershing Square Inc.'s own stock (CUSIP 71531U102), excluded from weights by `diff13f.py`. A
Q4 2024 amendment revealed Hertz. PSUS (CIK 2002660) files N-PORT and N-CSR. Proxy-fight material
and letters carry the reasoning.

**Polen Capital** (`polen`). Dan Davidowitz and Damon Ficklin run Focus Growth; Drew Cupps's
5Perspectives team joined in June 2025 and doubled the row count. CIK 1034524. About 70% of firm
assets; ~$9.3B of model and UMA assets are not discretionary. The 13F total fell from $41.5B to
$9.2B over the window: read the median change first. Q4 2023 was filed three times and still holds
about 17 values shifted by one row (never fixed). Polen Growth Fund: FundVantage Trust CIK 1388485,
series S000029264.

**Scion Asset Management** (`scion`). Michael Burry. CIK 1649339. Deregistered 2025-11-10; the
baseline covers its last 12 filings (2022-Q4 to 2025-Q3), then his public Substack, which is
partly paywalled. Misleading even when it filed: option notional dominated the total in five
quarters. Watch for a new entity, not new 13Fs.

**TCI Fund Management** (`tci`). Chris Hohn. CIK 1647251. About 60–65% of the book: Safran, Airbus,
Aena, Vinci and Cellnex are off it, and Ferrovial is partly held through swaps. The filing covers
the master fund and the foundation's vehicle. Letters are paywalled, so Hohn's words are
second-hand. Name changes on unchanged CUSIPs (GE Aerospace, Ferrovial NV) are not trades.

**Valley Forge Capital** (`valley-forge`). Devang Kantesaria, sole PM. CIK 1697868. Nearly all of
the book is on the 13F. A Brown Brothers Harriman feeder sits behind part of the assets. Its
Q3 2026 rotation into Amazon, Broadcom, Nvidia and TSMC, away from payments and ratings, reversed
his 2024 statements and is unexplained.
