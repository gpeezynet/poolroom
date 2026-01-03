# DR-20 Ops Binder & SOPs

## Meta
id: DR-20
name: Ops Binder & SOPs
gate: Gate 4
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
| Training hours per role | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| SOP update cadence (months) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Compliance audit frequency | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- ops_binder.training_hours_per_role
- ops_binder.sop_update_cadence_months
- ops_binder.compliance_audit_frequency_per_year
- ops_binder.checklist_count

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
DR-20 Operations Binder: Huntsville Poolroom Bar
1. Opening and Closing Procedures
Opening (12pm–5pm): Staff should systematically prepare the bar and poolroom for service. Bartender:
Unlock and power on the POS, lights, music and TVs; wipe down bar counters and stools; set up menus,
napkins and garnishes; fill ice wells and stock mixers; verify starting cash float. Barback: Restock beer
kegs, wine and liquor; polish glassware; fill ice bins and supply clean shakers/utensils; sweep floors and
replenish bar napkins/utensils. Security/Bouncer: Test cameras, turn off alarms, secure entrance doors,
post signage (“No Minors”); confirm emergency exits are clear. Manager: Hold a quick pre-shift briefing
(assign roles, review house specials, occupancy limits and any events); inspect the premises for readiness;
update reservation/waitlist if any; complete a quick safety check (fire extinguishers, first-aid).
Evening Peak (5pm–10pm): During busy hours, maintain role focus. Bartender: Follow standard-pour
SOPs (1.25 oz shots) and cocktail recipes exactly; pace service to meet drink goals; alert barback to replenish
low-stock liquor and glassware immediately. Barback: Continually refill beer/wine on tap, restock garnishes,
ice and glassware; clean up spills promptly; remove empty bottles and trash. Security: Check IDs at the
door (see Section 4); patrol the poolroom and bar area to deter trouble; seat guests or manage a waitlist
(log names/time, estimate wait). Floorman: Greet guests, manage pool table assignments, enforce “no
outside food/drinks” and sportsmanship rules. Manager: Float to assist guests or staff, take deliveries,
verify schedules for the next shift; handle any staff substitutions.
Late-Night Closeout (10pm–2am): Last call is at 1:45am (service ends by 2:00am per state law ). After
service ends, follow a closing checklist. Bartender: Make final drink runs, close out tabs and print out sales
reports; “burn” extra ice and sanitize ice bins; turn off beer taps or cappers. Barback: Empty and replace
trash liners; clear and sanitize tables and pool accessories (cues, balls); stack stools and mop floors.
Security: Ensure all patrons leave calmly; secure loose chairs/tables outside; walk-through to check no one
loitering. Manager: Oversee last call announcement and exit; count the cash drawer and reconcile with POS
receipts ; store cash in safe/deposit bag; verify that all customers have vacated and lock main doors; arm
alarms. All Staff: Wipe down all surfaces (bar top, tables, pool tables), sweep/mop floors, clean toilets, and
restock for the next day. Closing tasks include ensuring all guests leave, cleaning the service area,
restocking supplies, and securing the premises .
Cash Reconciliation: At shift end, the shift lead should follow the “cashout” steps: count register and tips,
verify totals match POS reports, log any over/short, prepare bank deposit, and fill out a cash report form. A
sample checklist might include: tallying cash, verifying card tips, reconciling gift cards/comp vouchers, and
filing the deposit slip for the safe. (For example: “Count cash drawer and calculate tips” is a standard closing
duty .)
1
2
3
4
3
1
2. Staff Scheduling Guidelines
Staggered Shifts: Tailor staffing levels by day and time. Schedule lighter crews mid-week and
heavier on weekends. Peak times (Friday/Saturday nights, major sports events) require extra
bartenders and barbacks, while weekdays may need minimal overlap. Adjust start times so that
peaks are fully staffed (e.g., second bartender from 5–6pm rather than all starting at 5pm). Use parttimers or split shifts to cover lunch/afternoon lulls. Build flexibility for no-shows or last-minute
bookings.
Labor Cost Targets: Aim for a labor cost of ~20–25% of sales . Schedule around projected sales
(e.g. use forecasting to match “covers” to FTE hours). Implement cross-training so servers can back
up each other. Review sales daily/weekly and adjust scheduling to hit the 20–25% range .
Late-Night Enhancements: From 10pm onward, include at least one extra security guard (or
bouncer) per entrance, and designate a dedicated closing crew (possibly 1 bartender + 1 barback) to
finalize tasks. Closing crew should arrive by 10–11pm to start pre-close duties. Ensure managers or
supervisors work late to oversee security and final checks.
Shift Coverage: Maintain a small on-call list in case of unexpected absences. Stagger breaks (don’t
have all servers off simultaneously) to maintain coverage. A rotating schedule helps meet
compliance with overtime rules while keeping coverage. (Using scheduling software or templates
can help visualize staffing by day; many restaurant guides target 20–25% labor by aligning staff to
busy hours .)
3. Bar and Floor Operations
Beverage SOPs: Enforce strict pouring and recipe rules. Use bar jiggers or electronic pourers
(SkyFlo, etc.) so drinks are consistent. Standard pours (1.25 oz for liquor shots) maximize profit and
control alcohol use. Maintain laminated recipe cards at the bar and train bartenders to follow them
verbatim. Regularly spot-check pours or use POS modifiers for “double” vs “single” to track variance.
Keep a daily inventory (ending bottle counts) and compare with sales to catch over-pours or
shrinkage. Conduct weekly or monthly physical counts of liquor, beer and wine by category.
Preparation (“Mise en Place”): Bartenders should prep bar-side mise en place before busy periods
 – e.g. fill well buckets with mixers, pre-cut garnishes, ensure shakers and glassware are ready.
This speeds service during rushes. Use colored labels or shots glasses to pre-measure frequently
used mixes (like simple syrup, juice, soda).
Pool Table Rental Operations: Set clear hourly rates and group pricing. Common practice is a perplayer rate that decreases with larger groups (e.g. $3/hr per person for 1–2 players, $2.50 each for 3–
4 players). Post the table fee structure visibly and in menus. Maintain a reservations or league
schedule: hold weekly leagues/tournaments (e.g. Monday nights), and post a league roster with
times/fees. Enforce rules: allow only chalk near tables, require cue-rack returns, forbid food/drink
spills on tables, and set a maximum time per rack to ensure turnover. Log table use hourly; a simple
sign-up sheet or digital app can track who plays when and how long, to reconcile with payments
collected.
Guest Management & Etiquette: Greet guests promptly and manage any wait-list fairly (e.g. list
names with arrival times, offer a pager or text alert). Enforce “courtesy of the house” etiquette: no
foul language, no obstructing walkways, avoid bullshitting or sexist remarks, and respect others’
games. Inform patrons of rules if needed (e.g. “please no slam shots” or “keep voices reasonable”).
Host staff should de-escalate minor disputes politely. Instruct staff to check customers’ IDs and
understanding of rules upon entry to avoid issues later.
•
• 5
5
•
•
5
•
•
1
•
•
2
4. Security and Safety Protocols
ID Check and Refusal: Scan or visually check ID of anyone who looks under 30. Keep a basic refusal
script posted at the bar (e.g. “I’m sorry, but I cannot serve you” when ID fails or if person is visibly
intoxicated). Know state rules: never serve alcohol to minors or visibly intoxicated persons.
Alabama law prohibits under-21 from serving alcohol . Train staff on these protocols, and post
“No Minors” signs at entrances.
Camera Coverage: Install surveillance to cover all key areas: entry/exit points, bar counter, pool
tables, and parking lot if possible. Recommended mounting: at least one high-angle camera
covering the bar and tables, and another covering the main entrance. Label camera zones (Front
Door, Back Door, Bar, Pool Area) on a facility map. Regularly test cameras and sign a weekly log to
verify systems are on and recording.
Incident Response: Establish clear steps for altercations or medical issues. For fights or unruly
patrons: security should first attempt de-escalation (calm voice, create distance). If aggression
continues or weapons are involved, call 911 immediately. If someone is too intoxicated, move them
to a safe area, offer water, and arrange a ride-share or taxi home. In all cases, notify the on-duty
manager at first sign of trouble. Document every incident in an incident log (time, individuals
involved, action taken). Provide staff an emergency contact sheet (local police, fire, ambulance,
poison control) behind the bar.
Weekly Security Briefing: Hold a brief meeting or huddle before each busy shift to cover any recent
issues. Review upcoming events, watch-list individuals (e.g. banned patrons), and any maintenance
concerns (e.g. a broken door lock). Use a checklist: door security functional, cameras recording, code
words for emergencies (e.g. manager says “Code Yellow” if bartender needs help). This ensures every
team member knows their role in maintaining a safe environment.
5. Legal and Compliance Framework
State ABC Laws: Alabama law sets an alcohol service cutoff at 2:00 AM (with on-premise sales
ending by that time). No sales of alcohol may occur after 2am. Happy Hour: Alabama prohibits price
discounts or multi-drink deals before 10am or after 9pm . Thus all promotions must end by 9pm.
It is also illegal to serve multiple drinks for one price or require customers to buy two to get a special
price . (These rules help enforce the 2am cutoff and responsible service.)
Alcohol Licensing: Obtain a state ABC liquor license (Class I Lounge Retail for on-premises) from
the Alabama ABC Board . The state license fee is \$300/year . Alabama requires you to first
apply with the ABC Board and be approved before receiving local approval . Next, file a City of
Huntsville Alcohol Beverage License application (with City Finance) . Huntsville also imposes a
local liquor privilege license tax on sales (a percentage of alcohol sales) and a general business license
for other revenue . Expect to provide city auditors with your Articles of Organization, lease, and a
health department letter of intent (even if no food is served) . Local zoning and community
approval apply (nearby residents are notified, public hearing possible). All licenses (state and city)
must be posted conspicuously behind the bar.
Other Licenses & Permits:
Pool Table License & Bond: Alabama law (§40-12-146) requires a license per pool table in public
billiard halls . The combined state+county fee is about \$38.50/table/year . You must also post
a \$1,000 Pool Room Operator’s bond (approx \$100/year cost) with the county probate judge .
This bond guarantees compliance with pool hall rules (no gambling, no underage loitering).
•
6
•
•
•
• 2
7
7
•
8 8
9
9
10
9 11
•
•
12 12
12
3
County Beer/Wine Licenses: Besides the ABC license, you need county licenses to sell beer and
wine (even for on-premise consumption). This typically means a county beer license and table-wine
license (often ~$112.50 each annual total) . These are obtained through the probate office after
your ABC license is approved.
Food Service Permit: If you serve any food (even pre-packaged snacks), obtain a health permit from
Madison County. Even without food, the health department usually issues a “letter of intent” or
inspector note confirming status . Display all health inspection certificates prominently (usually at
the host stand).
Occupancy Permit: Post the maximum occupancy (from the fire marshal) near the exit. Obtain an
Alabama Department of Labor poster and all required labor law/employment posters (minimum
wage, anti-discrimination, etc.) on a break-room bulletin board. Common signage includes: “No
Minors,” “No Credit,” “Spirits Only Sold In Interior,” and your ABC license.
6. Cash Handling & Inventory Controls
End-of-Day Cashout Checklist: The closing manager or lead should complete a formal cash-out.
Typical steps: close out all open tabs in the POS, run a sales report, count the cash drawer (as noted
above), compare to POS receipts, log any discrepancies, prepare the deposit (store surplus in safe,
take tip jar). Record voids/comps separately. Check that all credit card receipts are collected, tips
allocated, and that the register is balanced. (E.g. Toast POS recommends counting the cash drawer
and tips as a final closing task .)
Inventory Audits: Maintain daily logs for key items. Each morning or nightly, have someone tally onhand counts for liquor (by bottle count or ounces), draft kegs (volume), wine bottles, and packaged
mixers. Enter these into a daily inventory form. Once per week, do a full physical inventory and
compare to sales to detect over-pours or theft. Create standard templates (physical spreadsheet or
POS inventory module) for these audits. Track wastage: require staff to log any spills or cracked
liquor bottles (include date, item, quantity, reason) on a waste/spill log. Similarly, log all comped
drinks with the reason (on staff form or POS note) to monitor abuse.
Controls & Technology: Use an itemized POS to record every sale and comp. Implement portion
control: use measured pourers or jiggers on bottles, and weigh beer kegs when tapped/drained to
check waste. A tool like SkyFlo (electronic metering) or enforced jigger use prevents free-pours. Keep
a single par-stock of liquor so reordering is predictable. Reconcile receipts to deliveries weekly to
ensure nothing was lost.
7. Customer Experience Enhancements
Service Goals: Set clear targets for drink service. During peak hours, bartenders should serve at
least 2 drinks per guest per hour on average; during slower late-night hours, target ~1.5 drinks per
guest. These goals can be tracked via POS sales per server per hour. Encourage suggestive selling
(e.g. “Would you like another?” or pairing drinks with snack deals).
Menu Design: Create an easy-to-read drink menu. Group items logically (e.g. Domestic Beer, Import
Beer, House Spirits, Specialty Cocktails, Non-Alcoholic). Balance beer vs. liquor offerings (e.g. 50%
local/specialty beers and 50% classic cocktails). Include a few “house specials” or combos (e.g. “Shot
& Beer” deal) to encourage add-on sales. Price drinks to meet a target beverage COGS (e.g. 20–25%)
and a standard beverage margin. Keep menus concise (avoid overwhelming choices late at night)
and prominently feature any ongoing specials (within legal hours).
•
13
•
11
•
•
3
•
•
•
•
4
Pricing & Combos: Use premium pricing for late-night hours (just before last call) since demand is
high. Consider offering a “bucket” special (e.g. 4 beers + 2 shots) on weekend nights. Happy hour
pricing is allowed between 10am–9pm ; after 9pm you may not reduce prices or serve multi-drink
discounts . Promote non-alcoholic combo deals (e.g. free popcorn with a pitcher) if allowed.
Atmosphere & Service: Train staff to be attentive – refill waters, clear empty glasses quickly, and
maintain smiles even late at night. The goal is to maximize check value with quality service while
keeping lines moving. Rotate drink specials weekly to give customers variety, and solicit feedback on
new cocktails.
8. Emergency and Contingency Planning
Utility Failures: If power goes out, safely move all open flames (e.g. light candles if needed for
ambiance, extinguish any fire hazards), use emergency lighting, and serve only bottled/non-open
foods as needed. For plumbing failures (e.g. no water), suspend bar service if ice machines or sinks
are out; notify maintenance and use bottled ice/water as stop-gap. If the refrigerator/freezer fails,
immediately relocate perishable stock (beer kegs to a backup cooler, liquor to cold storage) and use
dry ice if available. In all cases, post a notice for customers and consider offering partial refunds or
closing if necessary.
Fire Evacuation: Post a fire exit map behind the bar showing primary exits and the assembly point.
Assign staff specific duties: one person escorts customers out calmly, another retrieves the register/
cash (if safe to do so), a manager calls 911 and checks stockrooms for stranded staff. Conduct at
least an annual drill. Keep fire extinguishers accessible (know locations: bar, kitchen, near pool
tables) and ensure staff know how to use them.
Injury or Incident: In case of customer injury (fall, altercation) or other incident, call 911 if needed.
Provide first aid if safe. Document the incident in detail (date/time, people involved, what occurred).
Keep a basic incident report form and have staff note witness names/contact info. For any legal
complaint (e.g. accident or false claim), preserve evidence: save video footage, police reports, and
copies of the incident log. Notify owners and your insurance broker about any serious incident.
Additional Contingencies: Prepare for other emergencies: have a generator or battery lights for
extended outage, keep a plunger and basic tool kit for minor maintenance, and stock a small cash
reserve in case banks are closed. In all emergencies, prioritize customer and staff safety and
communicate clearly.
Sources: This binder’s procedures are informed by industry best practices and Alabama regulations
. Each checklist and policy aligns with Alabama ABC rules and
Huntsville codes for a compliant, efficient operation.
How to Make an Opening and Closing Checklists for Bars (Free Template)
https://pos.toasttab.com/blog/on-the-line/bar-opening-and-closing-checklists?
srsltid=AfmBOooxHWAeCpHUEU1dlemSBtjodscanoGHaszhvYV_0rn-p1d4VJsb
Last Call for Alcohol Time by State [Map Updated for 2025]
https://pos.toasttab.com/blog/on-the-line/last-call-for-alcohol-by-state?
srsltid=AfmBOoo7qTalgIe9TO86qXW5nGepPgTCSzDKNyUjgsk8g-ouL_b-1H_M
A Complete Guide on Restaurant Closing Checklist
https://www.exceedinsurance.com/blog/restaurant-night-closing-checklist/
•
7
7
•
•
•
•
•
4 1
14 3 5 6 2 7 8 9 11 10 12 13
1 3 14
2
4
5
7 Poke Bowl Restaurant KPIs: Track Costs and Break-Even;
https://financialmodelslab.com/blogs/kpi-metrics/poke-bowl-restaurant?
srsltid=AfmBOorIPr86cAn3YUS_tU7OGw20UPsll0N3v6a7Jsln8wz3gjrIz0Hz
Responsible Vendor Program (RVP) | Alabama ABC Board
https://alabcboard.gov/licensing-compliance/responsible-vendor-program
Ala. Admin. Code r. 20-X-6-.13 - Limitations On Happy Hour And Similar Price Reductions | State
Regulations | US Law | LII / Legal Information Institute
https://www.law.cornell.edu/regulations/alabama/Ala-Admin-Code-r-20-X-6-.13
dr-02_legal.md
file://file-NR7NHTkFEEVPwYrbfDmQ4m
5
6
7
8 9 10 11 12 13
6
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
