# DR-18 Code, ADA, and Egress

## Meta
id: DR-18
name: Code, ADA, and Egress
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
| Occupant load limit | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Exit count requirement | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| ADA upgrade costs | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- code_ada.occupant_load_limit
- code_ada.exit_count_required
- code_ada.ada_restroom_upgrades_cost
- code_ada.sprinkler_requirement
- code_ada.egress_upgrade_cost

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
Americans with Disabilities Act (ADA)
Requirements
Accessible Entrance & Path: The primary entrance and all public areas must be on an accessible
route. Walking surfaces (incl. sidewalks and entry ramps) must have running slopes ≤1:20 (5%) and
cross slopes ≤1:48 . At least one public entrance must be fully accessible (ADA 206.4), and if
altering a front entrance or other primary area, an accessible path to that area must be provided
unless it exceeds 20% of the project cost .
Doors & Thresholds: All doorways on the accessible route must provide ≥32″ clear width .
Thresholds at doors are limited to ½″ high maximum (beveled if >¼″) . Maneuvering clearances
(space to open doors) must meet ADA 404.2.4 (e.g. 48″ clear space perpendicular to pull side, 60″ on
push side). Hardware (handles, locks) should be operable with ≤5 lbf.
Restrooms (ADA-Compliant Stall, Counters): At least one unisex or multi-user restroom must be
accessible. A wheelchair-accessible stall requires 60″×56″ clear floor space (for wall-hung toilet)
with side-wall grab bar (42″ long minimum) and rear grab bar . Sinks and mirrors must allow 27″
clearance under the sink (toekick 9″ high), and be no higher than 34″. Fixtures (toilet, sink, dispenser
heights) must meet ADA specs. For example, a typical accessible bathroom remodel (widen door,
install grab bars, etc.) costs on average ~$8,400 .
Figure: A typical wheelchair-accessible restroom stall meets ADA dimensions and grab-bar layout .
Interior Layout & Seating: A clear aisle of ≥36″ must run through the bar area (32″ min allowed
only very short segments). Provide a 60″ diameter turning space where needed (e.g. between tables)
. In assembly areas (pool tables/bar seating), ADA requires wheelchair spaces and companion
seating. For ~100 occupants (assembly), a minimum of 4 wheelchair spaces are needed (Table
221.2.1.1) , each with adjacent companion seats (one per wheel space ). Dining surfaces
•
1
2
• 3
4
•
5
6
7
5 6
• 8
9
10 11
1
(including bar tops and tables) must be 28–34″ high ; at least 5% of seating/standing spaces at
the bar must have this accessible height with knee clearance (e.g. one lowered bar section for ~20
seats).
Signage and Wayfinding: All permanent rooms (restrooms, exits, etc.) must have ADA-compliant
signs: tactile characters (uppercase, Braille) per ADA 703.2-703.5 . Restroom doors must have
pictogram with raised letters “Men”/“Women”/“Accessible” and Braille. If not all entrances are
accessible, non-accessible entries must be signed with the International Symbol of Accessibility
pointing to the accessible entrance (ADA 216.6) and directional signs provided. Exit doors along the
accessible egress path must bear tactile “EXIT” signs (ADA 216.4.1) . All signage should be highcontrast and 5/8″ min raised text with Grade-2 Braille.
Alterations & Grandfathering: In existing bars, many features can be grandfathered until major
alterations. However, if you alter a primary function area (like the bar or pool room) or entrance, the
accessible path to it must be upgraded (unless it exceeds 20% of project cost) . Changing the
occupancy or floor area may trigger full compliance (see egress below). If an alteration includes a
restroom or drinking fountain, at least 5% of each type of fixture must be made accessible. Thus, a
partial remodel often triggers broader ADA upgrades (new ramp/door or accessible restroom) to
maintain an accessible route to the remodeled area.
Egress and Emergency Exiting
Exit Signage & Lighting: All exits must be clearly marked. Illuminated “EXIT” signs are required at
each egress doorway, plus emergency lighting with 90-minute battery backup . Exit signs must
remain lit (e.g. LEDs) and be free of obstructions (no drapes or signs covering them). Under ADA, exit
doors must also have tactile signage (the word “EXIT” in raised letters and Braille) . In practice,
any exit door (even if unlocked) should be clearly signed and illuminated so occupants with
disabilities can find egress routes easily.
Number & Width of Exits: A-2 occupancies must provide two exits if occupant load exceeds 50 (for
100+ persons, use at least 2 exits). Exit widths must accommodate the occupant load: by code, the
total egress width (in inches) ≥ total occupants×0.3″ for stairways, or ×0.2″ for other egress
12
•
13
14
•
2
•
15
14
•
2
components . For 100 people, that is ~30″ (stair) or 20″ (corridor) total per exit. In practice, each
exit doorway is typically ≥32″–36″ wide to meet clearance and maneuvering requirements. Exits
(doors, corridors, stairways) must remain unobstructed at all times.
Panic/Fire Exit Hardware: Because this is a public bar (Assembly occupancy) with >50 persons, any
locked or latched egress door must have panic hardware (push bar) . In other words, doors in the
means-of-egress from the bar to the outside must unlatch with one forceful push. This is a strict IBC/
IFC requirement for A-2 occupancies. Fire exits and interior stair doors serving the path of egress
must likewise swing in the direction of travel and have panic or fire-exit hardware.
Sprinkler Systems: Modern building codes require automatic sprinklers in most new A-2 bars. Per
IBC 903.2.1.2, any new or significantly altered A-2 area with an occupant load ≥100 must be fully
sprinkled . (Many jurisdictions enforce the 2021 IBC rule: “occupant ≥100→sprinkler.”) For
existing older bars, IFC 1103.5.1 would retroactively require sprinklers only if the load is ≥300 (due to
alcohol) . Thus an older unsprinklered bar (100 people) can often remain as-is unless you expand
or renovate enough to meet the new-code threshold. Bear in mind that adding sprinklers (including
piping, heads, and often a fire pump) is costly, so this is a major renovation trigger.
Unobstructed Egress: All egress paths – including aisles between pool tables, chairs, and the bar –
must remain clear. No storage or furniture may block an exit path. Ramps (if needed) must have
slopes ≤1:12 and landings. Exit discharge to public way must be continuous. Emergency egress
lighting (battery-backed) must illuminate any stairs or changes in level in the path. In short, fire code
requires a continuous, accessible path from any point in the bar to the exterior. Violations like blocked
exits or non-functioning exit lights are common inspection failures .
Local Code Overlays (Huntsville, AL)
Adopted Codes: Huntsville follows Alabama’s adopted building codes (generally a version of the IBC/
IFC with local amendments). For commercial assembly, this means requirements largely mirror the
IBC/IFC above. (Consult the City’s Building Dept. or municipal code for the exact adopted edition and
any Alabama amendments.) Local amendments may adjust fire separation, parking, or licensing
rules.
Zoning & Alcohol Licenses: The bar must be in a properly zoned district for assembly/nightlife.
Huntsville’s Alcoholic Beverages Code requires a “Late Hours Permit” (Mixed Beverage Permit) to
serve alcohol between midnight–2:00 a.m.; without it, service must stop at midnight. City noise
ordinances also apply (e.g. decibel limits after 10 p.m.). While not strictly building code, these affect
operating hours.
Certificate of Occupancy: The CO inspection will check code compliance. Inspectors typically verify:
accessible parking and entry, ADA routes, restroom accessibility, exit sign/lighting, fire extinguishers,
alarm systems, and that the occupancy load does not exceed the stamped certificate. Common CO
holds include missing or noncompliant exit signage, blocked egress, lack of required sprinklers (if
triggered), or lack of an accessible route. In practice, having all ADA features (ramps/clearances/etc.)
and full egress systems is required before a CO is issued. (In Huntsville, as elsewhere, the CO cannot
be granted if life-safety or ADA violations are found.)
Renovation Impacts
Triggering Full Compliance: Major remodels often trigger broader code upgrades. For example, a
change of use to A-2 or a large expansion would invoke current code: sprinklers, accessible entrance,
16
•
17
•
18
19
•
20 15
•
•
•
•
3
etc. Even without changing use, altering >50% of the space or structural elements can require
compliance with current codes (see IBC 3403 “Change of Occupancy” and NFPA/IFC retrofit rules).
ADA specifically: altering a “primary function” area (like the bar floor) mandates an accessible path to
it (per the 20% rule) , so one might need to install a ramp or lift even if not doing it initially.
Cost of Compliance: Retrofitting an older bar can be expensive. ADA ramp installation can run
$5,000–$20,000 (materials, labor). Converting a restroom (widen door, install grab bars,
accessible fixtures) averages $2,700–$16,000 (around $8–$10K typical). Adding a sprinkler system
can be tens of thousands. These costs mean owners often postpone renovations to delay upgrades.
However, piecemeal fixes (e.g. one accessible restroom but not others) still expose liability, and at
some point full compliance will be required by law. In summary: renovation triggers = code
triggers – more scope often forces ADA and egress fixes.
Financial Planning: Owners should budget for these upgrades when renovating. For example,
making restrooms fully ADA might cost ~$8K , and adding a full wheelchair ramp and lift could be
another $10K–$30K . Not budgeting for this can derail a project if inspectors demand compliance
before occupancy.
Enforcement Patterns and Inspections
Fire Marshal Priorities: In assembly venues, fire marshals focus on exit access and suppression.
Common violations include blocked egress paths, missing or non-illuminated exit signs/emergency
lights, and obstructed fire doors . They check that extinguishers are present and alarms/
strobes are working. Panic hardware absence is a fast citation (IBC mandates it for A-2≥50). Any
change of occupancy or major renovation may prompt a sprinkler review.
Building Inspector Focus: During CO inspections, building officials verify occupant load signage,
handrail design (stair rail heights), ADA compliance of restrooms and entrances, and that a
continuous accessible route exists. Typical ADA citations include: ramp or elevator missing, doorways
<32″ clear, improper restroom stall dimensions or missing grab bars. Inspectors also check ADA
parking count and signage if the site has parking. Failure to address these issues can delay the CO.
Legal Risks & Insurance: Operating a bar that fails ADA or fire codes carries liability. ADA “drive-by”
lawsuits (for instance, patrons checking restrooms) are common; insurance articles note first-time
settlement averages around $75,000 for ADA violations . Non-compliance can void insurance
coverage for certain claims and result in fines or legal judgments. Courts have held that ignorance of
ADA is no defense. In practice, even aside from lawsuits, many insurance carriers require certain lifesafety features (like sprinklers) for coverage. Thus, meeting ADA and egress codes is not just
regulatory – it’s essential risk management.
Sources: 2010 ADA Standards (DOJ) ; 2021 IBC/IFC excerpts
; insurance and safety industry guidance . (Local Huntsville code: City ordinances for
late-hours permits and zoning.)
2010 ADA Standards for Accessible Design | ADA.gov
https://www.ada.gov/law-and-regs/design-standards/2010-stds/
Chapter 4: Entrances, Doors, and Gates
https://www.access-board.gov/ada/guides/chapter-4-entrances-doors-and-gates/
2
•
21
7
•
7
21
•
20 15
•
•
22
3 4 1 5 6 9 10 12 2 13 14 18
19 16 17 20 15 22
1 3 4 5 6 8 9 10 11 12 13 14
2
4
How Much Does Building an Accessible Bathroom Cost? [2025 Data]
https://www.homeadvisor.com/cost/additions-and-remodels/accessible-bathroom/
11 Most Common Building Fire Code Violations: Fire Safety Fails | AIE
https://aiefire.com/fire-safety-fail-reasons-most-common-fire-code-violations-businesses/
Microsoft Word - BU_09_06_11.doc
https://www3.iccsafe.org/cs/committeeArea/pdf_file/BU_09_06_11.pdf
Panic Hardware Requirements – Follow-Up – I Dig Hardware – Answers to your door, hardware, and code
questions from Allegion's Lori Greene.
https://idighardware.com/2022/12/panic-hardware-requirements-follow-up/
2024 Building Areas, Fire Areas and Mixed Occupancies
https://bsd.dli.mt.gov/_docs/Training/2024-IBC-Full-day-Bldg-Areas-Fire-Areas-and-Mixed-Occupancies.pdf
nfsa.org
https://nfsa.org/wp-content/uploads/2023/01/2021.10-Retrofit-Guide-4th-Ed.pdf
ADA Accessibility & Compliance for Medical Office Construction
https://stryker-construction.com/2018/04/20/ada-accessibility-dental-medical-office-construction/
The Hidden Liabilities Lurking in Every Restaurant and Bar - Gonzalez Insurance
https://gonzalezinsurance.com/the-hidden-liabilities-lurking-in-every-restaurant-and-bar/
7
15 20
16
17
18
19
21
22
5
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
