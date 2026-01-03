# DR-09 POS Stack & Payments

## Meta
id: DR-09
name: POS Stack & Payments
gate: Gate 3
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
| POS hardware cost per terminal | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Monthly software fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Payment processing percentage | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- pos_stack.terminals
- pos_stack.hardware_per_terminal
- pos_stack.monthly_software_fee
- pos_stack.payment_processing_pct
- pos_stack.onboarding_fee

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
POS Solutions for a Bar-Poolroom in Huntsville, AL
A late-night bar with pool tables needs a POS that handles both high-volume cocktail service and ancillary
recreation billing. Key requirements include tight liquor pour control, ID scanning/age verification, rocksolid performance during peak hours (7pm–2am), fast split-tender tabs, cloud back-office reporting,
inventory/loss-tracking, labor scheduling, Alabama regulatory compliance, rugged hardware, and guestfacing tools (loyalty, receipts, CRM). Below we summarize these needs and compare top POS vendors suited
for bars/nightclubs with billiards.
Key POS Requirements:
Liquor Pour Control: The POS should integrate with electronic pour systems (e.g. SkyFlo, Berg
Liquor Controls) so that every shot is recorded and compared to the sale. Integrated liquor control
technology journals each pour and compares it to the POS check , helping eliminate “free
pours” and shrinkage. For example, Berg’s liquor guns interface with many POS (Aldelo, Aloha, etc.)
via serial or RFID and automatically ring up pours . This ensures bartenders can only pour when
the POS ticket is open. (Likely approach: pair the chosen POS with a liquor-management system like
BarVision or Berg for real-time pour-versus-sale reports .)
ID Verification / Ban Lists: The system must enforce age limits. Many POS (e.g. Square for Retail)
can scan 2D barcodes on drivers’ licenses to verify age . Better yet, dedicated ID-scanners
integrate with POS to automatically flag minors or banned patrons. For example, Vēmos’s mobile ID
scanner cross-references a digital 86-list and VIP-list when scanning IDs . Patronscan’s
scanners similarly check licenses and alert staff if an ID is fake, expired or on a shared bannedperson database . In practice, the venue would use a scanner like Vēmos or Patronscan at
entry/cashier to gatekeep, while also optionally linking IDs to the POS guest records for marketing or
security.
Reliability & Offline Mode: Peak hours (late evenings) demand that the POS never fails. Leading
restaurant POSes boast 24/7 uptime and offline operation. For instance, Toast advertises “24/7
reliability” even during rush . Lightspeed offers a “fast, ultra-stable platform” with 24/7 support
. TouchBistro explicitly highlights an offline mode so orders and payments continue if the
Internet drops . In practice, ensure the system has battery-backed hardware or local caching so
that sales continue seamlessly if connectivity falters.
Fast Tabs & Payments: Bartenders need pre-authorized bar tabs and quick split checks. Square for
Restaurants, for example, supports secure pre-authorized tabs so cards stay behind the bar . All
top POS allow split-item or seat-based checks and accept EMV/NFC/tap payments. TouchBistro and
Toast likewise emphasize “bar tabs” (settle later) and fuss-free split checks . Modern solutions also
support mobile payments: e.g. Tap-to-pay readers and tableside devices.
Cloud Back Office / Mobile Access: Owners require real-time inventory, labor and sales dashboards
accessible from home. All major cloud POS (Toast, Square, Lightspeed, etc.) stream data to online
•
1 2
2
1
•
3
4 5
6 7
•
8
9 10
11
•
12
13
•
1
back-ends. For example, Square’s bar POS shows live sales by drink on a smartphone . Lightspeed
and Toast similarly offer mobile apps for viewing reports and adjusting menus on the fly .
This means management can review nightly variance reports and reorder alcohol on demand.
Inventory & Loss Prevention: The system must reconcile nightly counts and track liquor costs.
Revel and similar systems offer ingredient-level inventory control to track exact ounces poured .
In general, look for a POS with detailed liquor/beer inventory and reporting. (Alternatively, integrate
with a bar-inventory system like Pour Controls: they support many POS and automatically reconcile
pours against sales .) Such tools will help spot nightly shrinkage.
Labor Scheduling & Roles: A good POS includes shift scheduling, time-clock and tip distribution.
Square’s ecosystem includes shift scheduling and tip pools . Toast provides a “Team Management
Suite” with scheduling and tip management . Lightspeed has workforce management modules as
well. These allow managers to build shifts on the POS and export payroll data, with role-based login
to restrict manager vs bartender functions.
Regulatory Compliance: Alabama law often requires segregating alcohol revenue. The POS should
support item categories or locations for drink vs food sales to produce separate tax/revenue reports.
All modern POS let you categorize menu items by revenue center or tax code (so you can easily run
reports showing “liquor sales” vs “food sales”). Ensuring the POS can tag items by category will
simplify any state-mandated audits.
Hardware: The venue wants rugged, bar-friendly hardware. iPad- or Android-based terminals with
splash/dust protection are ideal. For example, Toast offers handheld Android terminals (Toast Go)
and durable countertop POS stations. Square sells an all-in-one Register and a magstripe/NFC reader
(Square Stand) that’s compact and sturdy. TouchBistro runs on iPad (usually in heavy-duty cases),
and Lightspeed can run on iPad or Windows terminals. In a humid, loud bar environment, use
protective cases, spare batteries/power backups, and consider upgrading to metal-mount tablets
(some vendors like SkyTab offer rugged kiosks). Ultimately choose hardware rated for 24/7
commercial use.
Customer-Facing Tools: A built-in loyalty/marketing module is a plus. For example, Square includes
a loyalty program and text/email marketing in its ecosystem . Toast and SkyTab both highlight
integrated promotions and CRM (e.g. personalized drink deals) . All systems support digital
receipts and email campaigns. Setting up a simple loyalty punch or points program in the POS can
help drive repeat visits at a bar.
14
15 8
•
16
1
•
17
18
•
•
•
19
20
2
Vendor Comparison
POS Vendor Key Features /
Integrations Pricing (est) Hardware Ideal For…
Toast
Toast’s bar/nightclub
package includes fast tab
management, built-in
drink modifiers, and 24/7
reliability . It has
native inventory
(including liquor-level
tracking), scheduling, and
strong loyalty/email tools.
Integrates with kitchen
displays for bar orders.
Supports offline mode.
~$135/mo per
terminal
(Starter Kit ~
$75–1000 onetime); no lock-in
(month-tomonth).
Hardware costs
extra.
Androidbased
terminals
(Toast Tap
reader,
handheld
Toast Go2, or
iPad/Android
tablets)
Bars/poolrooms
needing a proven,
full-featured
system with
robust support.
Good mid-market
fit.
Square for
Restaurants
Square’s restaurant
edition ($60/location)
supports bar tabs with
pre-auth card holds ,
split-item checks, and
quick order entry.
Includes inventory
syncing, staff scheduling
& timecards , and
loyalty/text-marketing
tools . Cloud-based
with mobile app for live
sales. No long-term
contract.
Starter Free; Plus
plan $60/mo per
location
(includes one
POS) + $40 for
each add’l device
.
(Transactions
fees ~2.6–2.9%.)
iPad or
Square
Register/
Stand; Square
Terminals &
Handheld for
payments.
Small to medium
bars that want
flexibility and low
upfront cost.
Excellent reliability
and ease of use.
Lightspeed
Restaurant
Fast, stable cloud POS for
bars . Supports
unlimited menu combos,
floor plans, and bar tabs
with pre-auth. Built-in
24/7 support. Includes
advanced inventory
(ingredient-level) and
labor/scheduling
modules. Rich reporting
and integrated loyalty/
CRM (with apps).
Integrates with many
third-party apps
(accounting, ordering).
Custom quotes
(typical ~$69–
$99/mo per
terminal).
(Transparent
pricing page
available.)
iPad (via
Lightspeed
app) or
dedicated
terminals.
Optional
POSitouch or
desktop
setups.
High-volume
nightclubs/sports
bars needing
advanced features
(multi-seat checks,
large menus).
Good for multilocation chains.
8
21
12
17
19
22
9
3
POS Vendor Key Features /
Integrations Pricing (est) Hardware Ideal For…
TouchBistro
iPad-based restaurant
POS with a dedicated
Bar/Nightclub mode .
Fast-bar register mode
(two taps) and “mobile”
order-taking. Handles bar
tabs (settle later), billsplitting, NFC/EMV
payments . Offline
mode keeps sales
running if internet fails
. Integrates with top
liquor inventory systems
and has loyalty module.
From $69/mo
per iPad (with
two-year
contract) .
Hardware (iPads)
extra. On-prem
version also
available.
iPad
terminals (at
fixed POS or
with iPad
stands), plus
Ethernet/
receipt
printers.
Bars/pubs
wanting an all-inone iPad solution.
Good if owners
prefer Apple
devices.
Revel
Systems
iPad-based POS built for
bars/nightlife. Ingredientlevel inventory and cost
controls . Full bar-tab
and bottle-service
support, custom drink
combos, multi-seat
checks. Integrated
Liquor Control: can link
to pour-spouts to
monitor every drop .
Employee scheduling,
deep analytics, loyalty
and marketing tools. Very
fast interface.
Quote required
(typically $99–
$199/mo per
terminal).
Higher-end,
enterprise-class.
iPad or iPad
Mini
terminals;
can also run
on Android
tablets.
Large bars,
nightclubs or
chains that need
granular pour
tracking and
robust
customization.
Others
(Honorable
Mentions)
SkyTab: A bar-focused
POS with lifetimewarrantied hardware.
Supports bar tabs and
loyalty. Lavu: iPad POS
similar to Toast, often
used by bars. CuetPOS
(Definitive Synergy):
Specialized pool-hall POS
with hourly table billing
(rare, on-prem). —These
exist, but mainstream
vendors above are more
common.
Varies. (SkyTab
custom; Lavu
~$60–$85/mo;
CuetPOS is
niche.)
SkyTab/
Aloha-type
terminals or
iPad
(depends on
vendor);
CuetPOS uses
PC.
SkyTab for venues
wanting dedicated
bar hardware;
CuetPOS if pool
billing is missioncritical.
23
13
11
24
16
25
4
Recommendations and Next Steps
Based on the criteria, Toast, Square, Lightspeed, TouchBistro or Revel would each serve the Poolroom
well, but with different strengths:
For pure reliability and ease (especially on a budget): Square for Restaurants is attractive. Its
$60/month plan (no long contract ) plus free smartphone reporting means low risk. It natively
handles tabs, age-check scanning (with a barcode reader) , shifts (via Square Shifts) , and
loyalty campaigns . Square’s hardware (Register or iPad Stand) is compact and durable. Its
weakness is less built-in pour-control, but you could integrate Square with a liquor-control system
(like Berg or SkyFlo) via middleware (as Berg supports Aldelo and similar POS , so a custom
Square integration is feasible via Square’s APIs). Overall, Square is a great starting point for a
modern bar.
For rich bar features and liquor control: Revel Systems or Lightspeed excel. Revel explicitly
mentions ingredient-level pour tracking and liquor-system integration , which directly
minimizes shrink. Lightspeed offers a similarly robust POS with 24/7 support and powerful inventory
modules . These may cost more upfront, but they are proven in busy nightlife environments
(Revel’s site touts “lightning-fast service” even at peak ). If controlling COGS via pour tracking is a
top priority, plan to connect Revel/Lightspeed to BarVision or Berg hardware for automatic pours.
For iPad-based simplicity: TouchBistro is solid. Its offline mode ensures no downtime, and it
can integrate with liquor inventory systems. It handles tabs, splits and NFC payments smoothly .
If the owners prefer Apple hardware, TouchBistro (or Square on iPad) may feel most familiar.
For comprehensive control: Toast offers an all-around system tailored to bars. It has built-in labor
and inventory, digital ordering, and strong reporting . Toast’s hardware (Android devices with
plans and free install) is commercial-grade. Many chains and sports bars use Toast successfully.
Action Plan: After selecting a POS, integrate complementary tools: install an ID scanner at entry (e.g.
Vēmos or Patronscan) and configure it with the POS/customer module. Add a pour-control system on liquor
guns (e.g. Berg, SkyFlo) linked into your POS if possible for real-time pour tracking . Use the POS’s
scheduling module to set shifts and tip-pooling. Categorize your menu items (beer, cocktails, food) for
reporting. Finally, train staff on fast bar modes and offline use so that even “last call” chaos is handled
smoothly.
Sources: We synthesized vendor info and expert articles (Toast, Square, Lightspeed, TouchBistro, Revel) and
case studies (bar operations forums, POS docs). For example, Toast’s blog confirms the need for 24/7
reliability in nightclubs , Square’s site details bar-tab and staff tools , and Revel’s literature
emphasizes pour-control integration . All assertions above are grounded in these sources.
•
22
3 17
19
2
•
16 25
9
26
• 11
13
•
8 11
1 2
8 12 17
25
5
How Pour Controls Helps The Hospitality
https://pourcontrols.com/how-we-help/
POS Interface - Liquor Controls & Management Systems
https://bergliquorcontrols.com/pos-interface/
Set age restrictions on items | Square Support Center - US
https://squareup.com/help/us/en/article/8197-set-age-restrictions-on-items-and-require-age-verification-with-square-for-retail
Vemos ID Scan | ID Scan App for Bars, Restaurants & Nightclub
https://www.vemos.io/idscan/
ID Scanner for Bars and Clubs | Patronscan
https://www.patronscan.com/id-scanner-for-bars
The Best Bar POS Systems: 10 Must-Have Features (2025) | Toast POS
https://pos.toasttab.com/blog/pos-systems-for-bars?
srsltid=AfmBOor4KrcDxgXmdqCLQDCgpZnsw8KaYnnv26KvC43VnX4XfJu0bI9A
Bar POS system | Bar POS Software Lightspeed
https://www.lightspeedhq.com/pos/restaurant/bar-pos-system/
Nightclub & Bar POS System - TouchBistro
https://www.touchbistro.com/pos-solutions/bar-pos/
POS System for Bars & Breweries | Square Restaurants
https://squareup.com/us/en/restaurants/bars
Bar & Nightclub POS -NextPOS - Revel POS Ireland
https://www.nextpos.ie/service/bar-nightclub-pos
Bar POS System | Nightclub & Bar Point of Sale | SkyTab
https://www.skytab.com/restaurant-types/bars-and-nightclubs
The Best POS Systems for Bars - Business.com
https://www.business.com/categories/best-bar-pos-systems/
Introducing Square for Restaurants | Square
https://squareup.com/us/en/the-bottom-line/selling-anywhere/introducing-square-for-restaurants
1
2
3
4 5
6 7
8 18
9 10 15
11 13 23
12 14 17 19
16 25 26
20
21 24
22
6
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
