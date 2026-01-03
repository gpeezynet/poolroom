# DR-12 Labor Wages & Staffing

## Meta
id: DR-12
name: Labor Wages & Staffing
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
| Manager hourly wage | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Cook hourly wage | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Server hourly wage | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- labor.wages.manager_hourly
- labor.wages.cook_hourly
- labor.wages.server_hourly
- labor.wages.cleaner_hourly

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
Alcohol COGS Benchmarks
Bars typically target beverage COGS in the low‐20% range for spirits and cocktails, and mid‐20s for beer. For
example, industry data show draft beer pours at ~20% cost (80% margin) , bottled beer around 25% ,
spirits about 18–20% , and wine higher (30–40%) . (Cocktails combine spirits plus mixers, so their
cost is higher by ingredient, but still often managed to ~25–30%.) In practice, a half‑barrel (15.5 gal)
domestic lager keg runs roughly $79–$139 and a craft keg can be $100–$200 (plus deposit). For
example, Bud Light half‑kegs around $130 and Dos Equis Amber ~$158 . At $150 per keg, a 20% pour
cost implies charging ~$6/pint . Liquor bottle costs vary by brand: operators use the ABC price list (spirits
sold via Alabama ABC stores) but typically pay wholesale $20–$30 per 750 mL for mid‑range vodka or
bourbon, yielding ~$0.50/oz cost. Table below summarizes typical COGS targets by drink type (and example
pricing):
Figure: Beer on draft delivers high margins when keg costs are managed. Draft beer can achieve ~80% gross
margin , but bars can lose ~8–10% of each keg to foam/overpour without controls .
Beverage
Category
Target COGS %
(approx.)
Notes / Pricing Examples
Draft Beer ~20–22% Domestic keg (15.5 gal) ~$80–$140 (~124 pints); craft kegs
$100–200 . Aim for 80% margin (20% pour cost) .
Bottled/
Canned Beer
~23–25% 24‑packs of domestic beer ~$16–$24 wholesale ; markup to
price accordingly.
Spirits
(Liquor) ~18–20%
Industry standard spirits cost 18–20% . A 750 mL bottle of
mid‑tier vodka (~$22 retail) might be ~$15 wholesale (1.5 oz pour
~$0.48 cost).
1 2
3 4 5
6
6
7
1 8
1
5
6
6 1
2
5
9
3
3
1
Beverage
Category
Target COGS %
(approx.)
Notes / Pricing Examples
Cocktails/
Mixed
~25–30%
(varies)
Includes liquor + mixers + garnish. Cost depends on recipe;
higher than straight liquor, but managed by portioning and
pricing.
Wine (by
bottle) ~30–40%
Fine wines often target higher COGS. Bottles are typically marked
~2.5–3× wholesale .
In aggregate, bars often see beverage COGS of 18–24% . Most profitable bars keep total beverage cost in
the low-20s (80% gross margin). (By comparison, food COGS are typically higher – ~28–35% – so
beverage programs lift overall margin.) In the Southeast region, distributors offer similar pricing: Alabama
Crown, Supreme Beverage and others supply kegs at broadly the above rates. Volume discounts apply (e.g.
case and keg pricing tiers); many distributors require minimum orders (often a few hundred dollars) and set
delivery schedules (e.g. weekly or biweekly). The Alabama ABC “Direct Delivery Store” (DDS) program even
offers twice‑weekly beverage delivery for large accounts, but only for big orders (50‑case minimum per
delivery) .
Food COGS Benchmarks
If the pool hall serves bar snacks or platters (wings, fries, nachos, etc.), budget roughly 30–35% food cost.
Bulk wings, a common bar item, run about $8–$9 per pound from broadline distributors like Sysco .
(A 10 lb case of Sysco Classic seasoned wings is ~$80–90 .) Fries or nacho chips are cheaper (frozen
fries often ~$0.60–$1.00/lb in quantity). For example, Sysco lists 2.5 kg fries ~ $7.30 on a reseller site (≈
$1.30/lb), and bulk tortilla chips ~$1–2/lb (depending on type). Plan to sell menu prices at about 3×
ingredient cost. Expect some spoilage: restaurants typically waste ~4–10% of food inventory . Food
spoilage (improper storage, over‐prep) and plate waste (customers leaving extras) drive this loss.
Minimizing waste by cooking-to-order, using FIFO inventory, and tracking expiry can shave points off COGS.
Notably, for every $1 spent on waste prevention, studies show ~$7 gain in profit (about 600% ROI).
Vendor pricing (Sysco, US Foods) varies by region. For a Huntsville account, one would sign with the local
Sysco branch or US Foods and meet their order minimum (often ~$250–$300/month). Both deliver 1–3
times per week depending on order. Large chains like Sysco offer loyalty discounts, but even independents
can negotiate volume pricing. Sample food item costs (approx.): chicken tenders 10 lb ~$80–$120, frozen
fries 10 lb ~$10–$15, frozen mozzarella sticks 2.5 kg (about 5.5 lb) ~$10–$12. These prices imply, e.g., a 20-
piece wing order (about 1.5 lb raw) costs <$12. Managing food COGS involves tight portioning, training
kitchen staff, and often using a recipe/inventory system to track usage.
Distribution Logistics & Fees
Alabama’s three-tier system means beer is sold through licensed distributors, while wine/spirits move via
state ABC warehouses. Key distributors in Huntsville include Supreme Beverage, Alabama Crown, and
smaller craft suppliers. Typical distributor rules: many require a weekly or monthly minimum (often a few
hundred dollars per delivery). Delivery fees may apply for small orders; larger accounts (e.g. weekly $1,000+
spend) often get free delivery. Beer distributors typically deliver on fixed days (e.g. one or two weekdays per
4
10
11
12
13 14
15 16
15 16
17
18
2
week). The ABC’s DDS program (for large-volume spirit accounts) requires 50-case minimums and delivers
twice weekly . Otherwise, bars buy spirits either by ordering through ABC’s online shop or picking up at
Wholesale ABC stores.
Local sourcing: Huntsville has several craft breweries (Yellowhammer Brewing, Straight to Ale, etc.) and
distilleries (Irons One, Guajana Rum). However, Alabama law prohibits distilleries from selling directly to
bars . Brewers also must distribute through wholesalers (self-distribution is generally not allowed). Bars
can stock local brands by ordering them from the distributor network. Some bars tap local beers on draft,
often under similar pricing (e.g. Yellowhammer kegs roughly in the $150–$180 range). No local craft
exemption means all alcohol (even in-state) follows the same 3-tier margins.
Inventory control systems (like Bar-i, Sculpture Hospitality, Partender) can significantly trim COGS. By
automating liquor counts and linking to POS, these systems detect over-pours, theft, and free-drink comps
in real time. For example, data from Bar-i shows many bars lose about 8–10% of each keg to foam, overpouring and line issues . Tight pour spouts, portioned jiggers, and training reduce these losses. Software
also flags fast-moving vs dead stock, enabling smarter ordering and lower spoilage. Bars using digital
inventory report often recover 5–15% in cost savings within a year, as waste is identified and eliminated.
Operational COGS Drivers
Key factors driving beverage COGS include pour control and training: consistent 1.5‑oz pours (or
controlling double/rocks pours) is critical. Underpouring hurts guest experience, while overpouring directly
raises costs. Free drinks (comps) and unauthorized discounts also cut into margins. Theft (employee
consumption) is a hidden COGS driver – diligent inventories and restricted access to bottles help mitigate
this. Tools like POS modifiers (to upcharge doubles) and inventory audits discourage cutting corners. Welltrained staff who know drink recipes and measure pours are essential: studies show that without controls,
even a 0.1 oz overpour per drink can raise spirit costs by several points.
Equipment maintenance is another driver: for draft beer, poorly cleaned or imbalanced lines can waste beer.
As noted above, bars often lose up to 10% of draught volume to foam or line problems . Keeping taps
calibrated and glassware pre-chilled can recoup that loss. Even routine tasks (like counting bottles nightly)
translate directly to saved dollars: regular inventory is the first defense against unnoticed waste.
Proven systems with ROI: many operators report that implementing bar-control software pays for itself. For
example, one analysis found that linking recipes and inventory data can cut liquor waste 5–10% and pay
back the system cost within 6–12 months. (By contrast, focusing on curbside and food waste can yield ~7×
ROI .) In short, disciplined stock audits, portion-control tools, and theft prevention can shave beverage
COGS by several percentage points over a year.
Comparative Data
In similar Southern markets, on-premise beverage costs cluster around the national norms. Industry
benchmarks (NRA, Provi, hospitality firms) put full-bar liquor & beer COGS at roughly 18–24% of beverage
sales . Pool halls or beer bars – which sell mostly drinks – tend to hit the lower end (around 20%),
since their “menu” has higher-margin items. By contrast, fast-casual or full-service restaurants (which sell
13
19
8
8
18
11 5
3
more food) usually see higher total COGS: typical food COGS run 28–35% of food sales. In fact, studies
show food costs average ~10 points higher than liquor costs . Overall restaurant COGS (food + beverage)
have climbed above 40% recently , driven by inflation, whereas a drinks-focused operation can stay near
25%.
For benchmarking: a fast-casual concept might budget ~35% food COGS and 6–10% for soft drinks
(beverage share ~5–10% of revenue) . A bar/pool hall, however, might see food only 10–20% of sales and
beverage ~80–90%. Thus total COGS may still be ~30–35%, but heavily weighted to alcohol. National data
(pre-2025) for bars/taverns show liquor/drinks holding ~20% COGS, with high gross margins (80%) on drinks
being a major profit engine. Even in pandemic‐recovery times (2023–25), beverage sales grew moderately
(~4%/year in bar/taverns ) despite cost pressures, indicating effective cost controls in place.
Sources: Distributor pricing and industry benchmarks are drawn from Alabama ABC and distributor
websites and publications (e.g. Alabama Select Spirits price lists, local supplier catalogs), plus hospitality
industry guides . National cost percentages come from POS and inventory systems
literature , and recent bar/restaurant reports . Local regulations (ABC/DDS) and
Alabama law are cited from official sources .
Keg Costs 101: What You Need to Know Before You Buy
https://pos.toasttab.com/blog/on-the-line/keg-costs?
srsltid=AfmBOorK7z76qmJJWb3saaDk0Zmg5KAn0i7v8HMv9zMkncH3LmzY8rBH
Liquor Cost Guide for Bars and Restaurants
https://www.getbackbar.com/liquor-cost-bars-restaurants
What Is the Average Liquor Cost for a Bar? | Bar Profit Guide
https://www.sculpturehospitality.com/blog/what-is-the-average-liquor-cost-for-a-bar
Beverage Costing Guide: Calculating Cost Percentage for Pricing
https://www.bernicks.com/blog/beverage-costing-guide
Stat Sheet: COGS-to-Revenue Ratio for Restaurants (Sep 2024)
https://www.supplyve.com/post/cogs-to-revenue-ratio-for-restaurants
DDS Registration | Alabama ABC Board
https://alabcboard.gov/stores/DDS-Registration
Chicken Wings Of Fire Cooked 1&2 Joints Small -Sysco Classic 1 Case, 2
https://easylunches.com/products/sysco-classic-chicken-wings-fire-cooked-1-2-joints-small-1-case-2-bags-10-pounds-total?
srsltid=AfmBOorCdgoKUW9HC40vUnvWMOR3dl2s_AdqG9y9ndbscuavu53Hj5Ht
How to Calculate Restaurant Food Waste
https://upkeep.com/learning/how-to-calculate-restaurant-food-waste/
New Alabama law mixes spirits with education starting in October - Yellowhammer News
https://yellowhammernews.com/new-alabama-law-mixes-spirits-with-education-starting-october-1/
12
12
20
5
9
6 15 1 3 5
1 3 11 12 20 5
13 14 19
1 2 6 7 8
3 10 11 12
4
5
9 20
13 14
15 16
17 18
19
4
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
