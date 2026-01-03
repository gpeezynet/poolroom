# DR-17 Utilities & HVAC

## Meta
id: DR-17
name: Utilities & HVAC
gate: Gate 1
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
| HVAC service contract (annual) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Utility deposit months | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Seasonal utility variance | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- facility.utilities_per_month.low/mid/high
- facility.hvac.service_contract_per_year
- facility.utility_deposit_months
- facility.hvac.hvac_maintenance_reserve_per_year
- facility.hvac.filter_replacement_per_month

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
HVAC System Requirements
A 3600–5000 ft² bar with ~12–24 pool tables (group A‑2 occupancy) will need roughly 10–15 tons of cooling
(120,000–180,000 BTU/hr). A common rule of thumb in hot-humid climates is 300–400 ft² per ton . For
example, 3,000 ft² ≈10 tons (120 kBTU/hr) and 5,000 ft² ≈12.5–16.7 tons, as shown in the table below
(assuming 12,000 BTU/hr per ton). Sizing should be confirmed by Manual J load calculations, including
occupancy, lighting and equipment loads. Provide ample latent capacity for humidity/smoke removal
(especially if smoking is allowed) and include separate makeup air for any kitchen hood.
Typical commercial HVAC choices are rooftop packaged units or VRF multi-splits. Conventional RTUs
(packaged rooftop units) serve one large zone and have lower upfront cost and familiar maintenance ,
but they short‑cycle at part-load and run fans continuously. Variable-Refrigerant-Flow (VRF) systems use
inverter-driven compressors and individual heads for each zone . VRF excels at multi-zone control and
high part-load efficiency (the compressor modulates instead of cycling) , though it costs more and
requires specialized technicians. In a single, open bar area an RTU or single split might suffice, but VRF can
improve efficiency under varying loads (for example, cooling one room while heating another) .
Hybrid strategies (e.g. RTU for main hall plus VRF for back areas) are also feasible . In all cases use highefficiency equipment (≥14–16 SEER) and variable-speed compressors or EC fan motors to save energy.
Comfort Temp/RH: OSHA recommends ~68–76°F for indoor comfort . Relative humidity ~30–50%
is ideal (keep ≤60% to prevent musty air). A range of 40–60% RH is often cited to protect wood
(e.g. pool tables) from warping .
Ventilation: Bars typically require 20–30 air changes/hour for smoke/odor removal . Design
outdoor-air intake per ASHRAE 62.1: roughly 0.06–0.12 cfm/ft² plus 7.5–15 cfm per person
(depending on density). In practice, supplying ~15 cfm/person (plus area makeup) keeps CO₂
≲1,000 ppm . Locate intakes away from exhausts (IMC generally requires ≥10 ft clearance) to
avoid recirculation. If smoking is permitted, consider a dedicated smoke exhaust or high-volume
1
2
3
4
3 5
6
• 7
8
9
• 10
11
1
ventilation zone. If a commercial kitchen is present, install a Class I hood with makeup air per IMC/
NFPA 96 (keep cooking fumes out of the bar space).
Energy-Efficiency Strategies
Efficient Equipment: Specify high-SEER heat pumps or split systems. ENERGY STAR–rated units
and low-GWP refrigerants (e.g. R-410A/32) are recommended. Use variable-speed (inverter)
compressors and EC (electronically commutated) blower/fan motors to reduce part-load energy.
Consider ductless mini-splits for isolated areas.
Controls & Zoning: Install programmable smart thermostats (supporting scheduling and remote
control). Zone control (dampers or multi-thermostat VRF) lets you cool only occupied areas. Demandcontrol ventilation (CO₂ sensors) can modulate fresh air to occupancy. Duct sealing and wellinsulated attic/roof reduce waste.
Energy Recovery: In Zone 3A’s humid climate, use an energy-recovery ventilator (ERV) or enthalpy
wheel on the fresh-air intake. This pre-cools/dehumidifies outside air by exchanging heat/moisture
with exhaust air, cutting HVAC load in summer and reclaiming heat in winter.
Lighting & Extras: Though outside HVAC scope, switching all lighting (indoor, signage) to LEDs and
installing occupancy sensors cuts internal gains (lowering A/C load). Where allowed, evaporative
cooling on fresh-air intake can also pre-cool summer ventilation air.
Rebates & Guidelines: Huntville/TVA area offers efficiency incentives. TVA’s EnergyRight Commercial
program, for example, provides roughly $80–$250 per ton for high-efficiency HVAC (e.g. $250/ton for
VRF or dual-fuel heat pumps) , and $100 per horsepower for adding VFD fans .
ENERGY STAR’s programs encourage similar upgrades. Check Alabama/TVA programs or Alabama
Power for specific rebates (e.g. heat-pump rebates ). Ensure equipment selections meet
ENERGY STAR criteria (higher EER/SEER thresholds for Zone 3A).
Utility Loads and Monthly Costs
Based on industry data and Huntsville rates, a 3,000–5,000 ft² restaurant/bar will use on the order of
120,000–215,000 kWh/year (~10,000–18,000 kWh/month) and several hundred thousand cubic feet
of natural gas (if cooking or heating). For example, full-service eateries average ~40 kWh/ft²-yr . At
Huntsville’s rate (~$0.0985/kWh ), that implies on the order of $1,000–$2,000 per month for electricity
alone. HVAC (cooling) is typically the biggest share, especially in summer.
Natural gas usage depends on equipment. Huntsville’s small-business gas rate is $10.57 per 1,000 ft³ . A
bar kitchen with grills, fryers, or water heaters could use 20–60 MCF/month. For reference, if a bar used
~600 MCF/yr, gas would add ~\$6,300/yr (~\$525/mo). In winter, space heating (if any) adds to this; in
summer, gas usage falls to mostly kitchen loads. Altogether, budget \$300–\$600 per month for gas in peak
winter and less in summer.
Water costs are minor: Huntsville charges $2.65 per 1,000 gal . Even heavy usage (e.g. 20–40 kgal/mo
for restrooms, mop sinks, bar clean-up) costs only \$50–\$100/mo. Total water-sewer bills will be small
relative to electric/gas.
Seasonally, expect a summer peak in electricity. A hot summer month (e.g. July) might be ~1.5–2× the
electric use of a mild month . For example, a hypothetical breakdown might be:
•
•
•
•
•
12 13
14
15
15
16
17
18
19
2
Season/
Month
Electric
(kWh)
Gas
(MCF)
Water
(gal) Elec ($) Gas ($) Water ($) Total
Summer
(Jul) 18,000 20 25,000 18,000×0.0985≈\
$1,773
20×\
$10.57≈\
$211
25×\
$2.65≈\
$66
≈\
$2,050
Winter
(Jan)
8,000 50 20,000 8,000×0.0985≈\
$788
50×\
$10.57≈\
$529
20×\
$2.65≈\
$53
≈\
$1,370
Estimates use Huntsville Utilities rates: $0.0985/kWh for electricity, $10.57/MCF for gas, $2.65/1,000 gal
 for water. Seasonal swings (higher A/C in summer, some heating in winter) drive the variations .
Code Compliance and Permitting
All HVAC work must comply with Huntsville’s adopted codes. The City follows the 2018 International
Mechanical Code (IMC) and 2015 International Energy Conservation Code (IECC) , and the 2021
International Fire Code (IFC) for fire-safety systems . A mechanical permit is required for new or modified
HVAC. Inspections include a rough‑in check (before walls/ceilings are closed) to verify ductwork, gas piping
and vents , and a final inspection after equipment installation . All gas appliances and combustion
equipment must also pass fire-department clearance and CO-safety checks per IMC.
Key code points for A-2 occupancy (bars/restaurants):
Ventilation: Design per ASHRAE 62.1 (often required by IMC). Provide the calculated outdoor airflow
(cfm/person + cfm/ft²) to keep indoor CO₂ ≲1,000 ppm . Fresh-air inlets must be sited per IMC
(typically ≥10 ft from building exhausts or pollutant sources) to avoid intake of contaminated air. If
smoking is allowed, comply with any local smoking-zone rules and ensure very high exhaust
ventilation.
Kitchen exhaust: Commercial cooking requires a UL-listed Type I hood with fire suppression
(NFPA 96) and makeup air per IMC Chapter 5. Kitchen air must be exhausted separately; do not mix
heavy grease/smoke into the dining HVAC system.
Fire safety: By code, a large assembly (A-2) generally requires an automatic sprinkler system (IFC).
Smoke detectors and fire dampers (in ductwork) are required where ducts penetrate fire barriers.
HVAC riser diagrams and equipment layouts are typically needed for plan review.
Energy code: All new equipment must meet Alabama’s energy code (2015 IECC) – e.g. minimum EER/
SEER and efficiency for AHUs. Commissioning or refrigerant charge verification may be mandated
for commercial units.
Permitting steps: Typically submit HVAC plans with load calcs and equipment specs to Huntsville’s
Building Department. After permit issuance, schedule a rough‑in (ducts/gas) inspection and final
inspection as noted above . Also coordinate with the Fire Marshal for any life-safety reviews
(duct smoke detectors, CO monitors if required, fresh-air interlocks, etc.).
16 17
18 19
20
21
22 23
•
11
•
•
•
•
22 23
3
Maintenance and Service Contracts
For reliability, establish a professional HVAC service contract with a qualified commercial HVAC firm. Best
practices include: biannual preventive tune-ups (spring and fall), which cover filter changes, blower/coil
cleaning, refrigerant leak checks, belt inspections, thermostat calibration, and safety controls testing.
Replace filters (often monthly or per equipment spec) and keep condensate drains clear. Verify refrigerant
charge and fan speeds to ensure efficient dehumidification (e.g. ~350 cfm/ton on coils).
In the contract, require emergency response (24–48h) and priority service clauses. Maintain a record of all
maintenance and repairs (date, findings, actions taken). Vendors should be licensed, insured, and familiar
with commercial systems (including any VRF or specialized equipment chosen).
Costs: Commercial HVAC service contracts typically run on the order of \$500–\$2,000 per year for one or
two rooftop units . (Actual cost depends on system size, service frequency, and inclusions.) Budget
around \$1,000–\$1,500 annually for routine HVAC maintenance on a mid-sized bar facility. Note that
diligent maintenance pays off: ENERGY STAR notes that a well-maintained system can save energy and
avoid major repairs . Ensure the contract covers major tune-up tasks; some include consumables (filters,
belts) and a parts discount.
Overall, a structured HVAC maintenance plan and service agreement will maximize uptime and efficiency,
which supports operational readiness for the bar.
Sources: Technical guidance above is drawn from HVAC sizing and code references (IMC/ASHRAE) and
industry data . All utility rates are from Huntsville Utilities. The zone climate is
ASHRAE 3A (hot-humid, e.g. dewpoints ~70°F ).
24
24
1 7 10 12 16 17 22 24
25
4
Is a 12.5 Ton AC the Right Size for Your Building? Sizing Guidance for
https://thefurnaceoutlet.com/blogs/hvac-tips/is-a-12-5-ton-ac-the-right-size-for-your-building-sizing-guidance-for-lightcommercial-spaces?srsltid=AfmBOopUA1J2K2qkDbC7fjbpJ2k217jjBWy8nSJQaKy8-SmvDoAjj1Lc
Conventional Rooftop vs. VRF Systems: Which Saves the Most Energy?
https://www.haroldbros.com/blog/vrf-vs-rtu-hvac-energy-savings
What can I do if my indoor workplace is too hot or cold? | Occupational Safety and Health
Administration
http://www.osha.gov/node/57113
Restaurant Humidity Control: How to Reach Appropriate Levels — GWT2Energy
https://www.gwt2energy.com/blog/restaurant-humidity-control-how-to-reach-appropriate-levels
How To Protect Your Pool Table From Humidity | All Pro Billiards
https://nineballbilliards.com/blog/2024/04/how-to-protect-your-pool-table-from-humidity/
Recommended Air Change Rates for Different Room Types
https://www.engineeringtoolbox.com/air-change-rate-room-d_867.html
Carbon Dioxide Levels Chart – CO2 Meter
https://www.co2meter.com/blogs/news/carbon-dioxide-indoor-levels-chart?
srsltid=AfmBOoqOMnVbd7Wym_sbwzDUBd2PWryCrcMwCfmnMolE549tsoqRuglm
Incentives - Business & Industry - energy incentives - TVA EnergyRight
https://energyright.com/business-industry/incentives/
From TVA: Rolling Out The Rebates
https://www.hsvutil.org/news_detail_T15_R223.php
What is the Average Restaurant Electricity Bill in 2025?
https://pos.toasttab.com/blog/on-the-line/average-restaurant-electricity-bill?
srsltid=AfmBOoqFUWVFjhnPAJVAlPlLYCjCkmHMR0kqdlIcGulduKXgmuQWdptw
Commercial Account Rates
https://www.hsvutil.org/business__commercial_services_/business__commercial_rates.php
Commercial Building Inspection Requirements - City of Huntsville
https://www.huntsvilleal.gov/development/building-construction/inspections/requirements/
Average Commercial HVAC Maintenance Cost - Evolution Mechanics
https://evolutionmechanical.net/blog/average-commercial-hvac-maintenance-cost/
Climate Zone 3A Warm-Humid Efficiency: Smart Fixes for Comfort and Low
https://thefurnaceoutlet.com/blogs/hvac-tips/climate-zone-3a-warm-humid-efficiency-smart-fixes-for-comfort-and-lower-bills?
srsltid=AfmBOopxH3Ak6-v3L967aMsGJ-1Oy7lfuwJZRXPjoEFlSloEdntoL8n2
1
2 3 4 5 6
7
8
9
10
11
12 13
14
15 19
16 17 18
20 21 22 23
24
25
5
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
