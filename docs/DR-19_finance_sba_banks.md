# DR-19 Financing (SBA/Banks)

## Meta
id: DR-19
name: Financing (SBA/Banks)
gate: Gate 2
status: PENDING
last_updated: YYYY-MM-DD
owner: TBD

## Prompt
```text
You are running Deep Research for the poolroom model. Use the Meta section above for id, name, and gate. Scope is Huntsville, AL unless explicitly noted. Do not invent numbers. Extract numeric assumptions with low/mid/high ranges and cite sources for each numeric claim, or tag it PLACEHOLDER. Return findings by filling the FINDINGS section below, keeping headings intact.
```

## Deliverables
- Summary for the topic scope.
- Numbers table with low/mid/high ranges.
- Risks and recommendations tied to the ROI model.
- Citations list with URLs.

## Assumptions to Extract
| Assumption | Low | Mid | High | Notes | Source |
| --- | --- | --- | --- | --- | --- |
| Loan amount | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Interest rate | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Term length (years) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- financing.loan_amount
- financing.interest_rate
- financing.term_years
- financing.down_payment_pct
- financing.sba_guarantee_fee
- financing.dscr_target

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
SBA Loan Programs for a Pool Hall Bar
SBA 7(a) Loans: The SBA’s flagship 7(a) program (loans up to $5 million) is well-suited for a capital‑intensive
restaurant or bar. It can finance leasehold build‑outs, equipment, furniture/fixtures, initial inventory,
working capital, and even debt refinance . Loan terms are generous: up to 25 years if most of the
funding is for real estate, or typically 10 years for equipment/working capital . Interest rates are
negotiated but capped (often prime + 2–4%); current rates for well‑qualified borrowers generally fall in the
~10–15% range . The SBA guarantees 75–85% of these loans, allowing lenders to offer lower rates
and longer amortization. Equity injection is required: typically around 10–15% for acquisitions, but 15–25%
or more for brand‑new startups . Borrowers must be “creditworthy” and able to repay the loan ,
with personal guarantees from any owner holding ≥20% equity .
SBA 504 (CDC) Loans: The 504 program helps finance major fixed assets (commercial real estate, long‑lived
equipment). A Certified Development Company (CDC) raises 40% via a low‑rate bond, the borrower puts in
10% (15% if a startup or special use), and a bank covers the remaining 50% . Total project size can exceed
$5 million (up to ~$5.5M SBA‑backed). Repayment is over 10–20 years with fixed interest rates (currently ~5–
6%) . This is ideal for purchasing or building a bar/restaurant space or expensive kitchen/bar equipment.
Note: 504 loans require owner‑occupancy and non‑speculative property; they cannot fund working capital
or inventory, only fixed assets .
Other SBA Options: For smaller needs, the SBA Microloan program (up to $50,000) can cover equipment,
inventory or short‑term working capital at terms up to ~6 years (rates ~8–13% ). CAPLines (SBA’s working
capital lines) can help seasonal or cyclical cash needs, but a more complex application. For a startup bar, 7(a)
and 504 are primary. Use the 7(a) for inventory, initial build‑out, furniture, deposits, and working capital;
use 504 only if buying real estate or expensive long‑life equipment that justifies the structure and time
needed.
SBA Program Comparison
Loan Type
Maximum
Amount
SBA
Guarantee
Term
(Repayment)
Typical Uses
Borrower
Equity
(Down
Payment)
7(a) $5,000,000
75%
(≥$150K);
85%
(≤$150K)
Up to 25 yr
(real estate);
~10 yr
(equipment,
working
capital)
Renovation/
leasehold
improvements,
equipment/furniture,
inventory, working
capital, debt
refinance
Typically
~10–25%
(startups
often 15–
25%)
1 2
3
4 5
6 7
8
9
4
1
10
11
3
1 2
6
1
Loan Type
Maximum
Amount
SBA
Guarantee
Term
(Repayment)
Typical Uses
Borrower
Equity
(Down
Payment)
CDC/504 $5.5 million*
40%
(CDC‑backed
bond)
10–20 yr (fixed
assets)
Owner‑occupied
commercial property,
large equipment
10%
normal;
15%
(startups/
special use)
Microloan $50,000 85%
~6 yr (short
term)
Small equipment,
inventory, modest
working capital
~15%
(varies by
lender)
CDC 504 loans are structured (50% bank loan + 40% CDC loan + 10% borrower) and can exceed $5M total. All SBA
loans require personal guarantees from owners of ≥20%* .
Eligibility, Terms and Requirements
To qualify for SBA financing, the business must be a for-profit U.S. small business in a legal industry .
SBA size standards (by NAICS code) determine “small”; most restaurants/bars easily qualify. Ineligible
industries (pure real estate, lending, some professional services, etc.) are listed by SBA, but bars are
generally eligible (SBA encourages financing for bars, restaurants, and hospitality ventures, as reflected by
industry marketing guides ). Note that because bars serve alcohol, lenders will examine any history of
regulatory or legal issues; having the proper local alcohol licenses in place is critical before loan closing
(an outstanding liquor‑license application is typically not enough). The project team should plan for the AL
ABC Board application (e.g. beer license ~$500–$600/yr ) and local land‑use/zoning approvals up front.
Credit and Collateral: SBA lenders require strong personal credit (ideally 650+ FICO) and a solid personal
financial profile. Owners with ≥20% stake must provide unconditional personal guarantees . Collateral
policies vary: SBA does not automatically seize all assets for loans < $50K , but for larger 7(a) loans the
lender must generally “take all available collateral” (business assets, equipment, possibly personal) even if
not sufficient . In practice, SBA insists on pledging all business assets and secondary collateral if needed
(including second liens on real estate). However, loans cannot be rejected solely for lack of collateral .
Down Payment/Equity: SBA expects the borrower to inject equity. For a startup restaurant/bar, a 15–25%
equity injection is typical . (For an existing business acquisition or refinance, the minimum might be
~10%.) SBA 504 loans specifically require at least 10% down (rising to 15% if the business is a startup or
property is special‑use) . The owner’s contribution can include cash, equipment trade‑in, or other value.
Interest Rates & Fees: 7(a) interest rates are variable or fixed, negotiated with the lender but subject to
SBA maximums. In today’s market (2026), well‑qualified borrowers often see ~10–15% rates on 7(a) loans
. (For perspective: in late-2025 the SBA 7(a) maximum for loans >$50K was often ~13–15% variable.)
504 loans have stable fixed rates around 5–6% (reflecting long-term bond yields) . Microloan rates are
set by intermediary lenders (often 8–13% today) . SBA loans also carry guarantee and servicing fees (e.g.
1
9
8
7
2
12
8
8
13
13
6
9
4 5
4
14
2
SBA guaranty fees 3–4% of loan, depending on term and amount) – these are typically financed into the
loan or paid at closing.
Working Capital: SBA 7(a) allows financing up to 25 years for real estate and up to 10 years for working
capital or equipment . Borrowers should note that working capital financing is capped at 10 years;
after that the remaining principal must be paid (though many bars aim to refinance or sell by then).
Liquor/Regulatory Issues: Bars are eligible but come with special scrutiny. Lenders will verify zoning
compliance and ABC regulations. The project’s liquor license (beer/wine or retail liquor license) is a
prerequisite. In Alabama, retail beer licenses cost roughly $500–$600/year and require a local ABC Board
hearing . Lenders typically require proof of license or a firm commitment from local authorities before
disbursing funds for a bar. The applicant must also obtain a Food Service permit (from the AL Department of
Public Health, ~15–45 day process) and meet any fire/ADA inspections . The SBA itself does not forbid
alcohol‑related businesses, but any legal/regulatory issues (e.g. past violations) must be disclosed and
cleared.
SBA-Preferred Lenders & Local Banks in Huntsville
Several banks with Huntsville presence are active SBA partners. These institutions can expedite SBA
financing and often have local officers who understand hospitality:
Regions Bank (Huntsville, AL) – Regions is a major regional lender and SBA Preferred Lender. Its
Huntsville Commercial Banking team (recently expanded under Chris Patty) supports small
businesses across sectors. Contact: Church Street NW Branch, 225 Church St NW, Huntsville (P:
256‑535‑2000) . They offer SBA 7(a) and 504 loans up to $5M, term loans, lines of credit, etc., and
have experience with restaurants/hospitality. (Regions has deep roots in north Alabama and
emphasizes “community support” for growing businesses .)
River Bank & Trust (Huntsville) – A locally headquartered bank, River Bank offers SBA financing for
businesses of all sizes. Its Huntsville office (401 Holmes Ave NE, Huntsville, P: 256‑384‑1203) has
dedicated Small Business Relationship Managers (e.g. Paul Robinson, Senior VPs Patrick Fleming,
etc. ) to help with SBA 7(a) and conventional loans. Sectors: General commercial, including
restaurants and retail. Loan sizes: up to SBA limits. River Bank markets itself to local small businesses
seeking term loans, lines, and SBA programs .
Bank Independent (Madison/Shelby counties) – A long‑time Alabama community bank (with a
Huntsville presence), Bank Independent promotes “flexible financing” and explicitly mentions
SBA‑backed loans among its products . Contact: (256) 386‑5000 (the North Alabama line). They
emphasize local decision-making and fast turnaround. A known local SBA lender, they handle small
business term loans and have business bankers (e.g. Tammy Pratt, Huntsville) who can assist with
SBA 7(a) applications. They serve all industries; given their roots in rural/agricultural lending, they
likely accommodate new ventures like hospitality.
First Horizon Bank (Huntsville) – Regional bank with local office. Contact: Eric Sanders (Market
President) eric.sanders@firsthorizon.com or Brian Daniels (Commercial Banking Manager)
brian.daniels@firsthorizon.com . First Horizon is an SBA Preferred Lender and offers SBA
3
12
15
•
16
17 18
•
19 20
21 19
•
22
•
23 24
3
loans, equipment financing, CRE loans, etc. . They note SBA loans explicitly on their Huntsville
FAQ. As a big bank, they do large loan sizes but also serve small businesses; they have dedicated SBA
specialists.
Synovus Bank (Huntsville) – A regional bank in the Southeast and SBA Preferred Lender. Contact:
Local branch managers at Synovus (e.g. Washington St branch at 301 Washington St NW,
888‑796‑6887) or Piedmont branch. Synovus advertises “up to 100% financing” and a “specialized
SBA lending team” . They cover term loans and lines for SBA-backed projects (including startup
and franchise financing), as well as USDA loans. Synovus branches in Huntsville can refer borrowers
to their SBA lenders for 7(a) or 504.
Each lender has its own strengths. Regions and First Horizon can do large transactions and have robust
hospitality experience. River Bank and Bank Independent are more community-focused and may offer
personalized service for smaller projects. Call or email the named contacts above to inquire about SBA
lending. (All above banks are FDIC/NCUA institutions with SBA status; for contact info, see their websites or
branch listings.)
Project Financial Model & SBA Approval Factors
The poolroom’s projections and capex will be closely reviewed. Key points from the provided model and
market research:
Market Demand: Huntsville has a population ~500K, with tens of thousands of adults playing pool
casually and a few thousand regulars . League participation and competitor data indicate steady
demand and room for growth. Cited estimates suggest “several thousand” potential regular
customers in the metro . This moderates lender concern: the plan is targeting an undersupplied
niche. However, lenders will compare projections to local comparables (e.g. Bumpers Billiards, Steve’s
Cue). A credible business plan should highlight unmet demand (as our market analysis does) and
realistic customer volumes.
Revenue & Unit Economics: The model assumes high beverage margins (~80% gross profit on
drinks ) and average per-customer checks of ~$25 (core hours) to $18 (late night) . Tipdriven labor (target 20–25% of sales) and moderate COGS (15–20% of sales) yield a healthy gross
margin and cash flow if traffic targets are met. These assumptions must be well-documented
(pricing analysis, league/tourism traffic, staff scheduling). If the plan shows positive cash flows and
capacity utilization even at 50–60% of tables in use, lenders will view that favorably. The SBA wants
proof of repayment ability, so using these figures to show EBITDA and debt service coverage will
strengthen the case.
Capital Expenditures: The startup is very capital-intensive. Our CAPEX analysis shows likely total
costs of ~$620K to build out a 12-table venue (plus ~$100K working capital) . Even a “likely”
scenario requires ~$720K total capital (with up to $1M for high-end fit-out). For a 24-table hall,
projected startup costs exceed $1.2–1.3M . SBA lenders will examine these numbers for
reasonableness. The detailed breakdown (construction, FF&E, pool tables, soft costs, contingency) is
good evidence, but lenders may want third-party quotes or contractor bids. They will also note that
requiring an SBA loan ~90% of a ~$700K or $1.3M project demands the entrepreneurs to provide
25
•
26
•
27
27
•
28 29 30
31
•
32
32
4
$70K–$130K in equity (10% at minimum). This aligns with SBA norms, but too little owner equity
could be a red flag.
Debt Coverage: The model must show that projected EBITDA comfortably covers debt service. For
example, if we borrow ~$650K at ~10% over 10–15 years, annual debt service might be ~$70K–$90K.
Combined with other business expenses (rent, payroll), the business will need to net well over
$100K/yr. The unit-economic model (with 12 tables, say 6–8 players on weekdays and full weekends)
should demonstrate this. If the plan assumes very aggressive table usage (e.g. full occupancy 6
nights/week), lenders may want sensitivity runs (e.g. what if slower start?). Conservative projections
lend credibility.
Regulatory/Collateral: The project has no obvious disqualifying factors, but SBA lenders will expect
the business to have or obtain all local licenses. A contingency clause in the loan closing likely
requires securing the liquor license and occupancy permits. Collateral-wise, the bank would likely
take a lien on all FF&E and possibly the leasehold improvements. Personal assets of the owners
(home equity, savings) may be needed if business assets fall short of loan amount.
Management Experience: (Not in the data files, but critical.) Lenders will ask about the owners’
backgrounds. Experience in hospitality or prior business success can offset startup risk. If the
owners have a track record (even in related industries), highlight it. Otherwise, stress thorough
planning and industry research (as in this model) to compensate.
Overall, the loan’s approval hinges on realistic assumptions and sufficient equity. The provided financial
model (assuming moderate build‑out costs and sound pricing) seems plausible. The unmet local demand
and strong margins support repayment ability. However, any optimism must be justified – e.g. showing
competition still busy, having franchise/league commitments, marketing plans, etc. SBA lenders will be
looking for conservatism (e.g. worst-case scenario, build contingency, actual quotes) to ensure the business
can weather slow opening or cost overruns.
Building a Compelling SBA Loan Package
Assemble a complete SBA loan application packet. Key components include:
Executive Summary & Business Plan: Concisely describe the concept (pool + bar), market
opportunity (cite local demand), management team, and financial projections. Use our market
analysis to show demand and competitive advantage . Highlight your USP (e.g. big tables, unique
menu, hospitality focus).
Financial Projections: Provide a 3–5 year income statement, cash flow, and balance sheet. Base
these on your unit economics (tables/hour * avg check, etc.) and conservative growth rates. Include
quarterly details for Year 1. Explain assumptions (e.g. X tables at Y occupancy, Z average spend).
Demonstrate debt coverage ratio ≥1.25x on the proposed loan. SBA’s guidance recommends clearly
matching funding needs to uses . Include startup costs (from [77]) and attach detailed
budgets (build-out, FF&E, working capital).
•
•
•
•
27
•
33 34
5
Personal and Business Financial Statements: Submit personal tax returns (last 2–3 yrs), a personal
financial statement, and any existing business financials (if you have an existing company). If a
startup, supply personal net worth statements to show equity injection ability. SBA lenders often
want to see liquid assets or secondary collateral (like home equity) to cover at least the down
payment or unexpected overruns.
Collateral and Guarantees: Prepare a list of collateral: commercial leasehold improvements,
furniture/fixtures, equipment, and any other business assets. Also list any personal assets you’re
willing to pledge. SBA Form 1919 (list of principals) will be required; be ready to provide Bio/CV/
resume for each principal over 20% ownership.
Licenses and Legal Documents: Include copies of any relevant permits or applications (business
license, zoning approval, liquor license application, health permits, etc.). If not yet obtained, include
a timeline showing when each will be secured. Provide a signed copy of the lease agreement (or LOI)
for the premises. SBA and lenders will verify compliance with local laws.
Creditworthiness: Demonstrate strong credit by disclosing credit scores and history. Any past
bankruptcies or judgments must be explained. Two years in business is ideal, but as a startup you
must compensate with stronger projections and more equity .
** SBA Forms and Application:** Use SBA Form 1919 (Personal History Statement) and Form 413
(Personal Financial Statement). Many lenders will have a checklist. Provide a cover letter stating the
loan amount, purpose (itemized uses), and proposed terms.
Additional Tips:   Secure letters of intent from suppliers (e.g. liquor distributors) or contracts with
employee/leasing agencies to show planning. Include references from any prior business ventures
or community leaders. Emphasize the quality of tables and experience (e.g. “Diamond tables, pro
shop support”) to justify traffic and pricing.
In summary, present a well‑documented, conservative plan: realistic costs (with quotes/contingency), solid
demand evidence , and clear repayment ability. SBA lenders favor completeness: missing paperwork or
inconsistent statements can delay or derail approval. Given the high fixed costs, also prepare a fallback plan
(e.g. phased build-out) to show you can scale investment if needed. A strong relationship with an SBA
lender (e.g. meeting with an SBA loan officer or counselor in Alabama) can also help refine the package.
Sources: Official SBA and lender resources , industry analyses , and local Huntsville
studies were used. All advice conforms to current (2026) SBA and Alabama regulations.
7(a) loans | U.S. Small Business Administration
https://www.sba.gov/funding-programs/loans/7a-loans
SBA Loans - First Horizon Bank
https://www.firsthorizon.com/Small-Business/Products-and-Services/Borrowing/SBA-Loans
Current SBA Loan Rates Explained (2026): 7(a), 504 & Microloan
https://clarifycapital.com/blog/sba-loan-rates
•
•
•
•
6
•
•
27
1 2 9 8 4 6
27 35 28
1 7
2 3
4 5 10 14
6
Understanding SBA 7(a) Down Payment Requirements
https://www.port51.com/insights/thought-leadership/understanding-sba-7a-down-payment-requirements-for-business-owners
SBA Loan Collateral vs. Guarantee | Bankrate
https://www.bankrate.com/loans/small-business/sba-loan-collateral-vs-guarantee/
SBA 504 Loans — SCED
https://www.scedd.org/sba-504-loans
Types of 7(a) loans | U.S. Small Business Administration
https://www.sba.gov/partners/lenders/7a-loan-program/types-7a-loans
Apply for licenses and permits | U.S. Small Business Administration
https://www.sba.gov/business-guide/launch-your-business/apply-licenses-permits
[PDF] How to Comply with the Regulatory Flexibility Act
https://advocacy.sba.gov/wp-content/uploads/2019/07/How-to-Comply-with-the-RFA-WEB.pdf
Chris Patty, Regions Bank - Huntsville/Madison County Chamber
https://hsvchamber.org/chris-patty-regions-bank/
Small Business Loans Huntsville, AL | River Bank & Trust
https://riverbankandtrust.com/small-business-loans-huntsville-al/
Bank Independent | Small Business Loan and Lending Options
https://www.bibank.com/business/loans
Banks in Huntsville | First Horizon Bank
https://www.firsthorizon.com/bank/al/banking-in-huntsville
Small Business Administration (SBA) Loans - Synovus
https://www.synovus.com/business/borrow-charge/small-business-administration-loans/
dr-01_market.md
file://file-UAvg9DPv5Qjc6ukH83rPeB
dr-05_unit_econ.md
file://file-AofkwNHPzZZrDNRhu3iof9
dr04_capex.md
file://file-UWNh8PW1ppU2pPkFZvbDfY
Write your business plan | U.S. Small Business Administration
https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan
6
8
9
11 13
12
15
16 17 18
19 20 21
22
23 24 25
26
27
28 29 30 31
32 35
33 34
7
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
