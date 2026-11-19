# The bundled baselines: overview

Written 2026-11-19, when the baseline was built. It is a snapshot: the investors' own folders, once copied into a working location, are where later updates go.

This folder holds a three-year baseline (Q4 2023 to Q3 2026) for each of the 13 managers the quarterly 13F routine watches. The point is to give a later session something to reason against when a new filing lands. How to read a 13F, what it leaves out and how much of each book it shows are in `SKILL.md` and `managers.md`; this file holds what the baseline work found. Before you read a share change as a decision, the profile tells you what is usually noise for that manager (fund flows, splits, a second book in the same filing, hedges reported at notional), and what has historically been signal. Each profile labels claims as **Said** (the manager's own words, linked), **Filed** (a 13F or other SEC filing) or **Inferred** (the writer's reading, with confidence and what would change it). Trust them in that order.

## What is here

Each manager has a folder:

- `holdings/YYYY-QN.csv`, one per quarter. Columns: `issuer, cusip, class, shares, value_usd, put_call, pct_of_portfolio`. Rows are summed by CUSIP plus put/call, so Berkshire's many rows per issuer collapse to one. Built by `scripts/build13f.py` from the SEC's own filings and reconciled to each cover page; `sources.csv` names the accessions behind each quarter. Values are whole dollars; two Himalaya quarters (Q4 2023, Q1 2024) were filed in thousands and were multiplied up.
- `profile.md`, the brief: who runs the money, how they say they invest, the arc across the 12 quarters read oldest first, how to separate flows from views, what the 13F does not show, and what to watch next.
- `log.md`, every filing and source read, in order, with what failed and why.

Two folders differ. `scion/` covers Q4 2022 to Q3 2025, Burry's last 12 filings before Scion deregistered on 2025-11-10, then his public Substack. `fundsmith/holdings/fisl/` holds the 13Fs of Fundsmith's sister firm (see below).

## Themes across managers

**Most share changes in this window are flows, not decisions.** Akre (outflows, then an ETF conversion in Oct 2025 where Neff picks which shares leave in kind), Polen (13F total fell from $41.5B to $9.2B), Fundsmith (flagship roughly halved) and Dorsey (nine client accounts moving in step) all show near-uniform percentage changes across names. AltaRock and Valley Forge both sit behind large Brown Brothers Harriman wealth-platform feeder funds, so their trims can be client money too. The working method that most profiles arrive at: find that quarter's median share change across the core names, then read each name against it. Only the deviation is the manager's view.

**Quality-growth managers changed their minds about AI in 2025–26.** Polen avoided semiconductors, then bought NVIDIA and Broadcom in August 2025 and moved into AI-infrastructure and industrial names in 2026. Valley Forge rotated about a quarter of its book into Amazon, Broadcom, Nvidia and TSMC in Q3 2026 while cutting Mastercard, Visa and Moody's, reversing what Kantesaria said in 2024; no stated reason was found. Fundsmith went the other way: it halved Microsoft, Meta and Alphabet on AI capex worries, and Smith now talks about being "more active". TCI exited Microsoft quickly. Turnover rose at several of these managers, so older profiles of them as patient compounders are less reliable than they were.

**FICO fell in Q3 2026 across its holders.** The value roughly halved on price after the FHFA and VantageScore moves in September 2026, with near-flat share counts at Valley Forge and Fundsmith; Akre added to it.

**Splits and name changes trap anyone comparing share counts.** The ones in this window: Brookfield 3:2 (Oct 2025), O'Reilly 15:1 (Jun 2025), Booking 25:1 (Apr 2026), ServiceNow and Netflix (see Polen). Aggregator sites often misread these as purchases.

**Filers' own data is sometimes wrong.** Polen's Q4 2023 filing has about 17 values shifted by one row (Eli Lilly shows $81M, really about $347M) and no amendment fixed it. Altimeter swapped CUSIPs in Q2 2024, and Himalaya swapped Alphabet A and C in Q4 2025 and amended the next day. Each case is in the relevant log.

## Quality and gaps

All 13 profiles were reviewed as a cold reader. Five were sent back once for missing filings or sources: Akre, Pershing, Fundsmith, Berkshire and Altimeter. All are now sourced. Thinner spots, and why:

- **AltaRock and Greenlea Lane** have almost no public record. AltaRock has said nothing in public since 2014, so its 2026 ADV brochure is the main source. Their profiles lean more on Inferred.
- **TCI** letters are paywalled (FT, Bloomberg), so Hohn's words are second-hand.
- **Scion's** 2026 positions come from paywalled Substack summaries, marked as secondary.
- **Akre's** Feb 2026 letter was seen only as a paywalled preview.
- **Altimeter's** Q3 2026 rows are $344,388 short of the cover total. The gap is unexplained and immaterial.
- **Pershing:** the explanation for its Q3 2026 Microsoft and Restaurant Brands cuts is medium-high confidence, until PSUS's Q3 N-PORT (due about late November) confirms it.

## Open items at the time of writing

- **A look-alike entity.** "Himalaya Capital Ltd" (CIK 2094573) filed a Form D in November 2026. The profile treats it as not Li Lu's firm; worth a glance.
- **AltaRock** moved its headquarters to West Palm Beach in 2024, and its Form D shows an $833M jump that nothing explains.
- **Valley Forge's** Q3 2026 rotation is the biggest unexplained change in the set.
- **Q4 2026 filings (due mid-February) should show:**
  - an Anthropic row at Altimeter;
  - Lennar, SiriusXM and DaVita changes at Berkshire.
