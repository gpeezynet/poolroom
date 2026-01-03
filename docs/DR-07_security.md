# DR-07 Security Staffing & Controls

## Meta
id: DR-07
name: Security Staffing & Controls
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
| Security guard hourly rate | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| CCTV system upfront cost | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| ID scanner monthly fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- security.hourly_rate.low/high/default
- security.camera_system.upfront_cost
- security.camera_system.monthly_monitoring
- security.id_scanner.upfront_cost
- security.id_scanner.monthly_service
- security.staffing_ratio_per_100_patrons

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
Security & Compliance Plan – Huntsville Poolroom
Bar
Overview: This security plan outlines the measures to maintain a safe, compliant poolroom bar in
Huntsville, AL (approx. 100-person capacity, 21+ patrons, alcohol-focused with limited food). It covers
physical security, staffing protocols, late-night operations, legal compliance, and cost considerations. A onepage Security Compliance Checklist is included at the end for quick staff reference.
1. Physical Security Plan
ID Scanning & Entry Control: The bar will enforce 100% ID checks at the entrance for all patrons to ensure
21+ only at all times . A dedicated doorman will verify government-issued photo IDs. Implementing
an electronic ID scanner at the door is highly recommended – modern scanners (e.g. PatronScan,
VeriScan) can quickly validate ID authenticity and detect fakes, while logging entry data . Scanning IDs
creates a record of patrons (useful if an incident occurs later) and flags any banned individuals attempting
re-entry . Alabama law is strict about underage drinking, and the pool hall license explicitly forbids
minors from loitering, so rigorous ID enforcement is non-negotiable . The doorman will also refuse
entry to visibly intoxicated persons to prevent problems at the door . Management will post clear
signage at the entrance: “21+ Only – IDs Required” and “No Underage, No Gambling,” as required by
Alabama’s billiard hall regulations .
Surveillance (CCTV) Coverage: A comprehensive camera system will cover all key areas of the venue for
both deterrence and incident documentation . Cameras should monitor the main entrance (capturing
each patron’s face on entry), the bar service area (to observe any service issues or disputes), the gaming
areas around pool tables, any secluded or “dark” corners, and the exits. Exterior cameras covering the front
door and parking lot are advisable for after-hour crowd dispersal and parking lot safety. All cameras will
record to a secure DVR/NVR with timestamps. Data retention will be set to at least 30 days of footage
storage , consistent with industry best practices for bars (to allow for delayed incident reports or
claims). Higher-risk periods (e.g. weekends) may warrant 60–90 day retention if storage allows .
Recorded footage provides critical evidence in the event of accidents, fights, or false liability claims . It
can also lead to insurance benefits, as some insurers offer premium discounts or even require cameras for
liquor liability coverage . Signage will be posted (as per legal requirements and deterrence best practice)
stating “Premises under 24/7 Video Surveillance” .
Access Points & Emergency Exits: The bar will utilize a single controlled entry point (the main front door)
for patrons. All other public access points (side or back doors) will be either locked or closely monitored
during business hours to prevent unauthorized entry or bypassing of the ID check. Emergency exits will
always remain unlocked from the inside for life safety, but will be equipped with audible alarms and
signage “Emergency Exit Only – Alarm Will Sound.” This ensures they are used only when truly needed. Staff
will conduct regular checks to confirm exits are closed (no door-propping) and not obscured or blocked by
any objects . Clearly illuminated EXIT signs and backup emergency lighting will be maintained per fire
code. During operating hours, the doorman or a roving security staff should keep an eye on exit doors
1 2
3
4
5 6
7
8 9
10
11 12
13
11
14
15
16
1
(either via direct line of sight or via camera monitor) to deter patrons from sneaking out with drinks or
propping doors open. At closing time, management will lock all entrances once the bar is cleared of
customers (no after-hours lingerers) to comply with Alabama’s prohibition on after-hours alcohol
consumption on the premises . The floor plan will be arranged so that security staff have a clear view of
all areas and there are no blind spots – mirrors or additional cameras will be added if necessary to cover any
hidden corners or hallways.
2. Staffing and Security Protocols
Security Roles & Staffing by Shift: A layered security staffing plan will be used to cover entry control,
internal monitoring, and managerial oversight, scaled to the time of day and crowd size. On typical busy
nights (e.g. weekends), the security team will consist of at least: - Doorman/Bouncer (Front Door):
Stationed at opening and through the night to check IDs, manage the entry line and capacity count, enforce
dress code or patron sobriety at entry, and refuse entry to underage or visibly intoxicated persons. This
person also stamps hands or provides wristbands if needed to indicate age-verified entry. - Roving Floor
Security: At least one guard circulating inside the bar, monitoring patron behavior in the pool table areas,
near the bar, and in any seating or patio areas. Their role is to preempt conflicts – keeping an eye on
competitive games that might turn heated, watching for signs of over-intoxication or harassment, and deescalating arguments. They are trained to intervene early with a polite warning or chat, and to break up any
physical altercations swiftly (using minimal force as appropriate) . On high-traffic nights (100 or near
capacity), a second roving guard should be added so one can cover the pool area while the other covers the
bar and other zones . - Manager on Duty (MOD): A manager or senior staff member will always be
on-site during operating hours, with specific responsibility for security oversight. The MOD (who could be
the owner or a trained shift manager) stays until closing and lock-up is complete . They coordinate
the security team’s actions, make judgment calls (e.g. whether to involve police in an incident), and ensure
all policies (ID checks, cut-offs, etc.) are consistently enforced. The manager also handles sensitive issues
like customer ejections or complaints, and will secure cash at close. Notably, the manager remains sober
and alert at all times during the shift.
Staffing levels will be adjusted based on crowd size and day of week. For instance, on a slow Monday or
Tuesday, the bar might only need one doorman (or even just the bartender checking IDs if very quiet) and
no dedicated floor guard after 10pm if only a handful of patrons are present . Conversely on a packed
Friday night, two security staff plus a manager are essential. It’s better to err on the side of overstaffing
security on uncertain nights – the cost of one extra guard is small compared to the potential cost of an
incident if understaffed . The security team will have clear shift schedules, including staggered start
times; e.g. one guard starting earlier in the evening and an additional guard coming in at 10pm when the
crowd grows . All security staff (and managers) should meet briefly before each weekend shift to review
assignments, discuss any known issues (e.g. banned patron descriptions, planned large parties, etc.), and
refresh on protocols .
Hiring & Training Guidelines: When hiring security personnel, the bar will prioritize professionalism,
training, and where appropriate, proper licensing: - Qualifications: Security staff should ideally have prior
experience in nightclub/bar security or law enforcement. Alabama does not require a special license for inhouse “bouncers” employed directly by the bar, as they are not contract security guards . However,
they must abide by the same legal limits on use of force and detention as any citizen (reasonable force only
in self-defense or to stop a crime) . All hires will undergo background checks. Any history of violent
offenses is disqualifying. - Training: All security staff (and bartenders) will be trained in responsible alcohol
17
18 7
19 20
21 22
23
24
23
25
26 18
27 28
2
service and conflict de-escalation. Participation in Alabama’s Responsible Vendor Program or equivalent
training (e.g. TIPS certification) will be required, as it both educates staff on state laws and can mitigate
penalties in case of a violation . Security employees will also receive in-house training on the bar’s
specific protocols: ID verification techniques, how to calmly refuse service or entry, proper communication
with patrons, and incident report writing. Regular refresher sessions (e.g. quarterly) will keep skills sharp
. We will maintain a training log signed by each employee, which demonstrates our due diligence to
regulators and insurers . - Off-Duty Police: For higher-risk times (holiday weekends, major events, or if a
pattern of late-night incidents emerges), management will consider hiring off-duty Huntsville police
officers as supplemental security. Off-duty officers (in uniform) have full arrest powers and bring
authoritative presence. They are especially useful at closing time to ensure everyone disperses peacefully.
The cost is higher (often ~$40–50/hour ), but their presence can deter weapons and serious altercations.
Any off-duty officers would be coordinated through the local police detail program, ensuring they are
properly approved to work security. This approach will be used as needed, in addition to the regular inhouse team – not as a substitute for a solid everyday security staff. Whether using in-house or off-duty
personnel, the bar will ensure adequate insurance coverage for security operations (including workers’
comp and liability coverage for any security staff actions – see Section 4).
Crowd Control & Intoxicated Guests: Maintaining a safe atmosphere means proactively managing crowd
behavior and patron intoxication: - Capacity & Floor Management: The doorman will track the headcount
to never exceed the fire code capacity (~100 persons). Overcrowding not only violates fire regulations but
also increases risk of fights and accidents. If the venue reaches capacity, entry becomes “one-in, one-out.”
Inside, security (and other staff) should circulate regularly. Key areas to watch are the pool tables –
competitive games or bets can spark disputes. Staff will enforce house rules (e.g. sign-up lists for tables,
no holding tables without playing, etc.) to reduce conflict triggers. If a crowd is gathering around a
particular contentious game, security will maintain a visible presence to remind patrons to keep it friendly.
The bar will also maintain a comfortable environment – not overly dark or loud – so staff can see and
communicate with patrons easily. If parts of the bar become congested, staff may politely disperse people
to other areas or outside patio (if available) to relieve crowding. The goal is to prevent any “hot spots” where
tempers could flare unchecked. - Managing Intoxicated Patrons: Bartenders and security will work
together to identify signs of intoxication early (slurred speech, stumbling, aggressive behavior, etc.). All
service staff are trained to slow or stop alcohol service in accordance with TIPS techniques. When a patron is
reaching their limit, bartenders will cut off service tactfully (e.g. offer a water or soda instead, state that per
policy they cannot serve more alcohol). Security or the manager will support the bartender if backup is
needed – a “buddy system” is used where one staff member notifying another before approaching an
impaired patron . The patron will be treated with respect and discretion: e.g. “For your safety, we
have to call it for the night on alcohol, but we’ll get you some water.” Free water, coffee, and light snacks
(e.g. pretzels) will be easily available, especially after midnight, to help slow down consumption and keep
guests composed . If a guest becomes highly intoxicated or ill, staff will ensure they are not left
alone – a staff member may escort them outside for fresh air, call a friend or rideshare to pick them up, or
as a last resort call medical help if needed. Under no circumstances will an intoxicated person be allowed to
drive; security will assist in arranging a taxi or rideshare and encourage them to wait in a safe area. If an
intoxicated patron must be removed (for causing disturbances), security will do so calmly by guiding them
out – never using force unless absolutely necessary. The incident will be documented and the person may
be refused entry on future occasions if they posed a serious problem . These measures not only
protect patrons, but also reduce our dram shop liability exposure (preventing a potential DUI incident
after leaving) .
29 30
31
32
33
34 35
36 37
38 39
40 41
3
3. Late-Night Operations & Risk Mitigation
The period after 10:00 PM, especially the last hour before closing (1:00–2:00 AM), is the highest-risk time for
bar security. The bar will implement special late-night policies to mitigate risks when patrons are most
intoxicated and incidents are most likely:
No Re-entry Policy: After a certain late hour (commonly 12:30 or 1:00 AM), the bar will enforce a no
re-entry rule . This means patrons stepping outside (e.g. to smoke or go to their car) after that
time will not be allowed back in. By doing this, we prevent the common issues of people “chugging”
alcohol outside or retrieving weapons/contraband from vehicles and returning . Security will
clearly inform patrons who exit after the cutoff that they cannot come back that night (“Last entry is
at 1 AM – if you leave, thanks for coming and have a good night.”). We will post a sign at the door
after the cutoff time as a reminder. This also helps us gradually thin out the crowd as closing
approaches.
Last Call & Closing Routine: “Last call” for alcohol will be announced at 1:30 AM (30 minutes
before the 2:00 AM closing time) . At last call, lights may be briefly flashed or subtly raised and
music volume lowered to signal the winding down . No new drink orders will be taken after this
announcement. Bartenders will make a final round of drink preparation and encourage patrons to
finalize tabs. By Alabama law, no alcohol can be served or consumed after 2:00 AM – all drinks
must be out of customers’ hands by that time . To ensure compliance, staff will begin collecting
remaining beverages shortly before 2:00. The DJ or jukebox (if present) will be turned off by 1:45–
1:50 AM, and the house lights brought fully up at 2:00 AM to prompt a smooth clearing of the bar
. Given the billiards focus, staff might announce “final game” warnings around 1:45 AM – e.g. no
new pool games to start after that time – so that players can wrap up ongoing games by closing .
Orderly Exit and Dispersal: Starting at last call, security and management will take an active role in
promoting an orderly exit. One security guard (or the manager) will station near the main door
around closing to gently remind departing patrons to take care and head home. Inside, as soon as
2:00 AM hits, security will sweep through the venue to usher any stragglers out, using polite but
firm reminders that the bar is now closed. Staff will be trained to never use aggressive language;
instead, they’ll say things like “We’re closed for the night, let’s get you home safe.” Importantly, a
security staffer will monitor the parking lot for a short period after close (around 2:00–2:15 AM)
. This outside presence can discourage fights or loitering in the parking area. If groups of
patrons are congregating outside, security will encourage them to disperse quietly (mindful of
neighbors). The goal is to avoid any altercations once people leave the controlled environment of the
bar. Many local police departments increase patrols at closing time, and we aim to have our crowd
dispersed on time to avoid police attention . All patrons should ideally be off premises by ~2:15
AM, aligning with common municipal expectations for bars.
Transportation for Patrons: As part of our commitment to safety, the bar will facilitate safe rides
for those who shouldn’t drive. Near closing, staff will proactively offer to call taxis or assist with
rideshare apps for any patron who appears too intoxicated to drive . We will post contact
information for local taxi companies and display signage for Uber/Lyft services inside the venue .
Management will explore partnerships with rideshare companies (e.g. promo codes for first-time
users or a discount for rides from our location) . By moving drinkers off the road, we reduce DUI
risks in the community and protect the bar from potential dram shop liability . We will also
•
42
42
•
43
44
45
44
46
•
22
47
48
•
49
49
49
40
4
encourage designated drivers in groups by offering free sodas or water to those who identify as
the DD.
Lighting and Music Adjustments: As mentioned, the ambiance of the bar will shift in the final
minutes to naturally cue patrons that the night is ending. From about 1:45 AM onward, music will
switch to calmer, lower-tempo selections or be turned off entirely by 2:00 AM . House lights will
be gradually brightened. These changes tend to subdue rowdy behavior and make it clear that it’s
time to leave, without staff needing to shout or herd people. Security staff will use a friendly but
direct approach – for example, lightly clapping and saying “Alright folks, that’s it for tonight. Thank
you for coming!” – to move people along.
Post-Closing Lockdown: Immediately after the last patron exits, the doors will be locked. Staff
(including at least one security or manager) will remain on site for a brief period (usually 30–60
minutes) to clean up and secure the premises . During this time, they will not allow any patrons
back in (even if someone forgot a jacket, a staff member can retrieve it rather than letting the person
re-enter). The MOD will verify that security alarm systems are armed and all entry points are secured
before the final staff leave. By around 3:00 AM, the venue should be empty of all persons and fully
locked, in compliance with Alabama’s expectation that licensed premises be closed after hours .
By implementing these late-night strategies, the bar minimizes potential fights, noise complaints, and legal
violations during closing time – protecting both the patrons and the business.
4. Legal Compliance & Liability Coverage
Staying in strict compliance with all alcohol, safety, and pool hall regulations is a core part of the security
plan. Below is a summary of relevant Huntsville and Alabama requirements and how the bar will adhere to
them:
Hours of Sale & Closing Time: In Huntsville (Madison County), 2:00 AM is the latest permissible closing
time for bars with alcohol service . All alcohol service will cease by 2:00 AM sharp (last call at 1:30 AM
as noted). Alabama law prohibits any consumption of alcohol on premises after legal service hours – by 2:00
AM no patron may possess or consume a drink . The staff’s closing routine ensures this (clearing drinks
at 2:00). Additionally, local ordinances often require patrons to vacate shortly after closing (commonly by
2:15 AM), so our policy of clearing the building by ~2:15 aligns with that . We will incorporate any specific
City of Huntsville stipulations that might apply (for example, if a special late-night permit or exception is
needed for operation until 2 AM, we will secure it – the business will not operate past midnight unless
properly permitted ). There will be no after-hours “bottle club” activity – the establishment will not
allow patrons to remain drinking (even their own alcohol) after closing, which is illegal .
Age Restrictions (Underage Patrons): Because this is an alcohol-forward venue, no minors are allowed
on premises at any time during operating hours . Even though Alabama’s old law banning
under-19 in pool halls was repealed, a newer provision effectively bans underage customers when alcohol is
being sold during extended hours . In practice, we will enforce 21+ only at all times. The front-door
ID check policy (Section 1) is the first line of defense. All staff serving alcohol will additionally be instructed
to card anyone who appears under 30 years old at point of sale . If a minor (under 21) somehow
gains entry or if any patron is found using a fake ID, they will be escorted out immediately, and the incident
will be documented. The bar will also prominently post the required signage about age restrictions – for
•
44
•
22
17
45 50
45
50
51 52
17
53 2
5 1
54 55
5
example, a sign stating “Must be 21 to Enter – Minors Prohibited” as suggested by Alabama Code .
We will stay current with Alabama ABC’s Responsible Vendor Program and ensure all servers and door
staff complete this training, as it reinforces ID checking and can provide some relief in penalties if a
violation occurs . Random internal compliance checks will be done (e.g. owners sending in a 21-yearold who looks young to ensure IDs are checked). The consequence for any staff found to have served a
minor is immediate termination – the risk to our license is that critical. Law enforcement (ABC or local
police) does conduct stings; our goal is to never fail a compliance check .
No Gambling Policy: Alabama law explicitly forbids gambling or betting in billiard rooms . The bar
will enforce a zero-tolerance policy on any form of gambling on-site. This includes obvious activities like card
games or dice, but also extends to informal betting on pool games or sports, tournament side-pots, or
any device that could be construed as a game of chance . Common prohibited games (mentioned in
statute) include things like “Kelly pool,” “keno,” or any scheme of wagering on game outcomes . As a
preventative measure, we will not allow dice, playing cards, or other gambling paraphernalia to be
brought out by patrons . Coin-operated machines that resemble gambling (e.g. video poker) will not be
installed, as those are illegal in Alabama . Our pool leagues or tournaments will be structured in
compliance with ABC rules (entry fees and prizes will be token and pre-announced to avoid any illegal pools
). We’ll also post signage per the law: for example, “No Gambling Allowed – Violators will be
Prosecuted” . Any patron caught attempting to gamble (e.g. two guests exchanging money over a
pool game) will receive a warning and be monitored closely; repeat or egregious behavior will result in
ejection and potentially a report to authorities. Management understands that gambling violations are
serious – a first offense is a misdemeanor, and a second offense can escalate to a felony and endanger our
business license and the $1,000 pool hall surety bond . We are committed to a clean, law-abiding
entertainment environment.
Incident Reporting & Record-Keeping: In the event of any notable security incident (fight, physical
altercation, accident/injury, ejection, theft, etc.), staff will follow an incident reporting protocol. The
manager on duty will ensure that an Incident Report Form is filled out promptly (ideally immediately after
the situation is under control, before memories fade). The report will capture date, time, parties involved
(including witness contacts if possible), description of what happened, actions taken by staff, and outcome
(whether anyone was removed, injured, whether police were called, etc.). These reports will be kept in an
incident log binder on-site and reviewed by upper management weekly. For serious incidents – e.g. a patron
injury requiring EMS, a large fight or any situation involving law enforcement – the ownership will selfreport to the Alabama ABC Board or local police as appropriate . It is better for regulators to hear of an
incident from us (along with an explanation of how we responded responsibly) than through a third party or
lawsuit . Alabama ABC expects incident transparency, and prompt reporting can demonstrate our
good-faith intent to operate safely. Additionally, our liquor liability insurance may require notification of
certain incidents. The bar will cooperate fully with law enforcement or ABC investigators if they follow up on
any incident. Surveillance footage of incidents will be preserved and provided to authorities if requested, in
line with privacy laws. By diligently documenting incidents, we create a paper trail showing we take
problems seriously and address them – this can be invaluable if there are later legal claims or licensing
reviews .
Other Local Regulations: We will adhere to all relevant city ordinances (e.g. noise ordinances, waste
disposal, etc.) and specific Huntsville codes for pool halls or bars: - The Fire Marshal’s occupancy limit (once
set during permitting) will be posted and never exceeded, as discussed. - Smoking rules: If smoking is
allowed by local law (Madison County allows it in bars unless otherwise regulated), we will ensure proper
56 8
29 57
54 55
58
58 59
58
60
61
62
63 64
65 66
67
67
68 69
6
ventilation and designated areas, but also be mindful of any future local smoking bans that could affect
indoor policy. - Health and sanitation: Even with minimal food service, we will keep the premises sanitary.
Alabama’s pool hall provisions require maintaining a clean establishment (unsanitary conditions can violate
the pool hall license) . Restrooms will be cleaned frequently and stocked; the play areas will be kept
free of debris to prevent slips. A nightly cleaning checklist will be followed. - Posting of Licenses and Signs:
All required licenses (liquor license, business license, pool table licenses, health permit if any) will be framed
and displayed as required by law. We will also display any mandatory signage (e.g. the Alabama ABC
warning signs about pregnancy and alcohol, the pooling of certain laws like underage and gambling rules
as mentioned in §34-6-12) . - Cooperation with Authorities: The management will maintain a good
working relationship with Huntsville Police and Alabama ABC enforcement. We will invite local police
officers to do a “walk-through” on busy nights from time to time (showing we have nothing to hide) or even
hire them as noted . Any ABC inspection or law enforcement visit will be treated with full cooperation
and immediate corrective action on any issue noted.
Insurance Requirements: Alongside legal compliance, carrying proper insurance is mandatory and a
critical risk mitigation measure: - Liquor Liability Insurance: Alabama state law requires liquor-serving
establishments to carry at least $100,000 in liquor liability coverage . The bar will secure a
comprehensive liquor liability insurance policy with at least a $1 million per occurrence limit, which is
common for bars and provides a higher safety net . This protects the business in case of alcohol-related
injuries or lawsuits (e.g. a dram shop claim if an overserved patron causes an accident). We note that
Alabama’s 2019 Dram Shop Act reform has made insurance more available and affordable (historically
premiums were extremely high, sometimes ~$30k/year, but have come down since) . - General Liability
Insurance: A general commercial liability policy will cover non-alcohol incidents (slip-and-fall, property
damage, etc.). We will carry at least $1M in general liability coverage as well, in line with industry standards
. Many insurers offer package deals (BOPs) that include both GL and property coverage for bars. -
Assault & Battery Coverage: Because we have bouncers and the risk of fights, we will ensure our liability
insurance includes Assault & Battery coverage (this is often an add-on rider to bar insurance) . A&B
coverage is crucial; some basic policies exclude fights or ejections from coverage. Our insurer will be
informed of our security procedures (ID checks, training, etc.), and we will comply with any conditions they
require for A&B coverage (such as all security staff to be trained, incident logs kept – which we are doing
). - Property Insurance: The bar will have property insurance covering fire, theft, vandalism, and so on
for the building (if owned) or the contents/improvements (if leased). This includes coverage for our pool
tables and equipment, which are valuable assets. Security measures like an alarm system, CCTV, and proper
locks can help lower property insurance premiums due to reduced theft risk. - Workers’ Compensation: All
employees, including security staff, will be covered by workers’ comp insurance as required by law. This
protects the business if staff are injured (for instance, a bouncer hurt while breaking up a fight). - Insurance
Compliance: We will keep all insurance policies current and in-force, and copies of insurance certificates
will be maintained on site. Additionally, as part of our risk management, we plan to maintain a good claims
record. By preventing incidents, we can avoid claims that would drive up premiums. Some insurers conduct
inspections or require checklists of best practices – we will embrace those, as many align with this plan (for
example, an insurer may require video cameras or written policies; we have those in place) . A safe
track record and cooperation with insurer recommendations can even lead to premium reductions over
time .
70 71
64 8
72
73
74
73
75
76
39
77 78
79
7
5. Operational Controls and Procedures
Beyond staffing and hardware, the bar will implement operational controls that promote security and
prevent losses. These include policies on alcohol service, measurement of drinks, record-keeping, and
escalation protocols:
Responsible Alcohol Service Training: All bartenders, servers, and managers will be certified in
responsible alcohol service (e.g. through TIPS or ServSafe Alcohol programs) . This formal training
teaches staff how to identify intoxication, how to refuse service diplomatically, and the legal obligations in
Alabama (such as not serving minors or overserving adults). Having trained staff is viewed favorably by both
regulators and insurance underwriters . In fact, Alabama’s ABC offers the Responsible Vendor Program
which, upon completion, provides some protection (reduced penalties) if a trained staff member
inadvertently serves a minor . We will ensure all new hires complete training within their first 30
days, and maintain documentation of their certificates . Periodically (at least annually, and as part of
staff meetings), we will conduct in-house refresher sessions – for example, a quarterly quiz on ID checking
procedures or how to cut someone off – to keep knowledge fresh . The emphasis is that every staff
member is part of the security team when it comes to preventing drunk driving and underage sales.
Portion Control & Bar Procedures: To minimize over-service and protect profit margins, the bar will
institute pour controls for all alcoholic drinks: - All spirits will be poured using either measured jiggers or
controlled-pour spouts to ensure standard servings (the standard shot in Alabama is 1.25 oz of liquor ).
Free-pouring will be discouraged except by very experienced bartenders who have demonstrated accuracy
(and even then, spot-checks will be done). - For high-volume times or for certain products, we’ll consider
technology like electronic flow meters or an automated dispensing system (e.g. Berg or SkyFlo) that tracks
each pour . Even without high-tech systems, measured pourers on bottles will be used to prevent
accidental over-pouring . - A recipe guide will be provided for all cocktails, specifying exact ingredients
and measures. Bartenders are expected to stick to those recipes – this ensures consistency for customers
and prevents “heavy handed” drinks that could over-intoxicate patrons or waste product . Management
will occasionally do a pour test (pouring water as a “shot” and measuring it) to recalibrate staff’s pouring
habits . - Shots or multi-liquor drinks that encourage rapid intoxication will be monitored. The bar’s
policy is to avoid any irresponsible promotions (like “buy one get one free shots” or large “fishbowl”
cocktails) especially late at night . We want to serve drinks in standard portions at a reasonable pace.
This not only promotes safety but also keeps us in good standing with insurers and regulators who frown
on high-risk drink specials . (For example, we will not offer extreme happy hour deals after 10 PM). -
Serving protocols: All alcohol service will stop at last call (no exceptions). Servers will be instructed to
remove unattended drinks during cleanup to prevent someone chugging multiple drinks at closing. No
open containers leave the premises – door security will enforce that no one walks out with a drink in hand
.
Inventory and Cash Controls: Sound operational controls indirectly enhance security by reducing internal
theft (shrinkage) and cash mishandling: - The manager will conduct nightly inventory counts for highvalue liquor bottles (e.g. count of top-shelf spirits at close) and track beer keg volumes, to catch any
significant discrepancies . A full inventory of all alcohol will be done weekly. This deters employee theft
or over-pouring because usage is being monitored. - A robust POS (Point-of-Sale) system will be used for
all transactions – no sales will be done “off the books.” Each drink sale will be entered, and the POS will be
set up to flag any missing transactions vs. inventory usage . All cash tips from the jar are to be
declared and rung in (or at least accounted for in closing reports) to avoid underreporting. - At shift end, the
80
81
82 83
32
31
84
85
86
87
88
89 90
91 90
19
92
92 93
8
closing manager/bartender will reconcile the register: match cash against reported sales, count credit card
receipts, and note any variances. Any comped drinks or spillage must be logged in the Manager Log
Book (with reasons) . This log book will also include a section for incidents or notable events (e.g. “broke
up a fight at 12:30 AM, two patrons were removed” as noted earlier) . Maintaining such a log
demonstrates diligent oversight and can be crucial documentation if an insurance claim or legal issue arises
later . - The safe and cash drawers will be secured. Only the manager and authorized personnel have
safe access. Nightly bank deposits will be done discretely (preferably by two people together, for safety). -
These operational controls, while focused on financial integrity, complement the security plan by fostering a
culture of accountability and allowing management to quickly spot irregularities that could indicate a
problem (like a staff member giving out free drinks or a patron sneaking in their own liquor).
Incident Response & Escalation Protocols: We have outlined preventive measures, but when incidents do
happen, a clear escalation procedure is key: - Minor Altercations: If a shouting match or minor scuffle
occurs, security will intervene immediately to separate the individuals. They will be moved apart to opposite
sides of the room or outside. The MOD will assess the situation. Often, simply ejecting one or both parties
involved for the night resolves the issue. The individuals will be told to leave and not return until a later day.
Security will escort them out one at a time to ensure they don’t re-engage outside. The incident will be
logged and those patrons may be added to a “do not admit” list at the door if the behavior was egregious. -
Serious Fights or Violence: If a full fight (multiple punches thrown) breaks out, security will follow training
to break up the fight with reasonable force and remove the combatants from the premises as quickly as
possible . If weapons are involved or it’s beyond staff control, 911 will be called immediately. Generally,
our protocol is: break it up, secure the area, then call police if anyone was injured or if perpetrators are not
cooperative. The manager makes the call on involving police; however, staff are encouraged to call 911
without delay if there is any immediate danger. Once the situation is safe, staff will attend to any injured
patrons with basic first aid (we will keep a first aid kit on site). Police reports will be filed for any assaults.
All staff involved will write an incident report. - Medical Emergencies: For any patron who is unconscious,
not breathing, or seriously injured (e.g. a seizure, head injury from a fall, etc.), staff will call for EMS (911)
right away. At least one staff member on duty will be CPR/first-aid certified if possible. We will render what
aid we can (within our training) until paramedics arrive. The manager will ensure crowd control (other
patrons should give space). We will document what happened and how we responded. - Escalation
Decision-Making: The general rule is to err on the side of over-escalating to authorities when in doubt. We
prefer to have police assistance and not need it, rather than need it and delay calling. The MOD will not
hesitate to call law enforcement to handle situations like aggressive patrons who refuse to leave, criminal
activity (assault, theft), or any threat to life/safety. Our security staff, as noted, are not police and will not
restrain patrons except as allowed in a citizen’s arrest for a witnessed crime . Thus, if someone is
committing a crime (e.g. a patron punches someone and continues to be violent), the protocol is to detain
only if absolutely necessary to protect others, and get police on site ASAP to take over. - Post-Incident
Review: After any incident, management will review how it was handled. This helps refine our protocols and
can identify any gaps in training or coverage. For example, if a fight broke out in a camera blind spot, we
may add a camera. If a staff member hesitated to call police, we’ll reiterate the escalation policy. These
reviews also feed into our insurance and legal strategy: we learn from each event to reduce recurrence.
All these operational controls are documented in our internal SOPs. By enforcing them consistently, the bar
not only runs efficiently but also demonstrates to investors, insurers, and authorities that it is proactively
managed with risk in mind. This reduces the likelihood of costly incidents and ensures any that do occur
are handled properly.
94
68
68
95
7
9
6. Cost Planning and ROI of Security Measures
Investing in security yields returns not just in safety but also in financial stability. Below we outline the
expected costs of our security program and the offsetting benefits:
Security Staffing Costs: For a venue of this size (100 patrons max), we anticipate the following typical labor
costs for security: - On weekend nights (peak business), we’ll schedule 2 security staff from ~8 PM to 2 AM
(6 hours each). Assuming an average wage of $15/hour (the local market rate for bar security is in the
~$13–17 range) , that’s about $180 per weekend night (12 total hours). In addition, the manager (or
a dedicated security supervisor) is on salary or a higher hourly rate, but that role overlaps with operational
management duties. - On weeknight evenings, we might have 1 security staff for 6 hours. That’s ~$90 per
night. - Summed up, we’re looking at roughly $300–$500 per week in security labor for a consistent
schedule (one guard on weekdays, two on Fri/Sat). This translates to roughly $15,000–$25,000 per year
in dedicated security wages. We consider this a necessary expense. As noted in our unit economics,
allocating ~5% of revenue to security staffing is worthwhile to prevent incidents and ensure smooth
operations . - If we augment with off-duty police on a few high-risk nights (say, 4 hours at $40/hour),
that might add another ~$160 for those nights. We will budget for occasional use of police details, but not
as a regular nightly cost.
These labor costs will be built into our operating budget. The trade-off for safety is clear: for example, $100
in security pay on a busy night is far cheaper than the consequences of a bar fight that could lead to
lawsuits or lost business .
Technology and Equipment Costs: Upfront, we will invest in the ID scanner device (~$1,000 for a quality
scanner or tablet setup) and a CCTV system. A 8-12 camera CCTV setup with recorder might cost on the
order of $5,000 installed. These are one-time or infrequent costs. Their ROI comes in both preventing theft
(catching a staff pocketing cash, for instance) and providing evidence to swiftly resolve any liability claims.
Often just having cameras visible deters theft and bad behavior, preserving revenue (this is hard to
quantify, but industry experience validates it).
Insurance Premiums: The insurance policies (liquor liability, general liability, property, etc.) are significant
fixed costs. For a bar of our profile, we estimate insurance will cost a few thousand dollars per year in total
. Notably, Alabama’s recent reforms have lowered liquor liability premiums; we anticipate maybe
~$1,000 annually for a $1M liquor liability policy for our small venue , plus perhaps another $1,000
for general liability and property. By implementing strong security measures, we make ourselves a better
risk to insurers. Many insurers explicitly ask about security: Do you have bouncers? Cameras? ID scanners?
Training programs? Answering “yes” to these can either qualify us for better rates or at least ensure
coverage is not denied. Some insurance carriers might offer a discount or lower deductible if we, for
example, show all staff are TIPS certified or that we keep video for 30 days – we will leverage these where
possible . Over time, if we maintain a clean claims record (no alcohol liability claims, no big fights
leading to lawsuits), we may see premiums hold steady or even decrease relative to the market. Conversely,
one bad claim can skyrocket our costs or make insurance renewal difficult. Thus, the “return” on investment
in security is partly avoiding huge insurance hikes. For instance, a single overserving lawsuit could carry a
$10,000 legal defense cost and then double our premiums next year. Preventing that incident saves that
$10k and keeps our ~$2k/year insurance cost in check.
96 97
98
99 98
98 100
75 101
102 75
103 77
10
Liability and Legal Savings: The most significant ROI from a robust security plan is in avoided liability: -
Avoiding Fines/License Suspensions: A violation for serving a minor in Alabama can lead to hefty fines
and possibly a license suspension or revocation on repeat offense . By strictly enforcing ID checks
and training, we aim to never incur these penalties. Saving even one $5,000 fine justifies a lot of ID scanning
hours. Similarly, not getting our liquor license suspended (which would shut down revenue) is priceless –
our security diligence makes that scenario far less likely. - Preventing Lawsuits: Bars commonly face
lawsuits from patron fights, injuries, or DUI accidents. With good security, the frequency of such incidents
drops dramatically. And if an incident does occur, having proper procedures can provide a defense. For
example, if a patron sues claiming we overserved them, we can show our camera footage and logs that the
person was cut off and given water, etc., potentially nullifying the claim. Avoiding just one major lawsuit
(which could cost tens of thousands in damages or settlements) pays back years of security expense.
Alabama’s dram shop law historically had unlimited liability for bars (hence those $30k premiums) –
while it’s been moderated, liability is still a real financial threat. We view every night with no incidents as
protecting the company’s financial health. - Theft and Shrinkage Reduction: Internal theft (bartenders
giving away free drinks or stealing cash) can significantly erode profits. A vigilant manager, solid inventory
controls, and cameras act as deterrents. By tracking pours and sales closely, we might save 1-2% of alcohol
inventory from shrinkage compared to a lax operation. For a bar doing say $500,000 annual sales, that’s
$5,000–$10,000 saved per year – again a payback on having those controls. The use of tools like jiggers and
inventory reconciliation each night directly preserves revenue that might otherwise leak out. - Reputation
and Repeat Business: Although harder to quantify, a safe environment means patrons feel comfortable
returning, and we avoid the revenue loss that comes if the bar gets a reputation for fights or crime. In the
long run, consistency in security can thus drive stable or increased patronage, which is an indirect ROI
through higher sales.
Insurance and Licensing Risk Mitigation: A well-implemented security plan is also an investment in
license protection. Regulators and law enforcement are aware of which bars are “trouble spots” and which
are well-managed . By being firmly in the latter category, we reduce the risk of targeted inspections,
undercover operations, or objections during license renewals. If we ever do come up for a license review or
need city council approval for something (like an extension or special permit), having had zero violations
and full compliance will make that process smooth. In contrast, a bar with multiple police calls can face
community opposition or stricter conditions on their license. This plan ensures we remain in good standing,
which protects our ability to operate and generate revenue without interruption.
In summary, while the security measures do incur ongoing costs (staff wages, equipment maintenance,
training expenses), they are an essential investment. They pay for themselves by preventing losses –
whether financial (theft, lawsuits, fines) or intangible (reputation damage, staff turnover due to unsafe
conditions). For our investors, this means less volatility and more reliable returns. A single serious incident
could cost more than our entire annual security budget, so we consider this plan as insurance in action.
Moreover, a safe and controlled environment is likely to attract a better clientele and reduce property
damage, further adding to long-term savings.
7. Security Compliance Checklist (Addendum)
Below is a one-page Security Compliance Checklist for quick reference by staff and management. This list
highlights the key daily/weekly steps to maintain safety and compliance in the poolroom bar:
82 104
73
105
11
✔ ID Verification for All Entrants: Door staff checks every patron’s ID with an electronic scanner – no
exceptions (21+ only) . Verify ID authenticity and photograph if needed. Refuse entry to minors or
anyone without valid ID. Post “Must be 21 to Enter” signage.
✔ Controlled Entry & Capacity: Keep only the front door as public entrance. Monitor occupancy count –
do not exceed 100 persons (post the official capacity sign). Use clicker or POS counter for entries/exits.
Enforce any “one-in, one-out” when at capacity.
✔ Surveillance Cameras Operational: Ensure CCTV covers all key areas (entrances, bar, pool tables, exits,
parking lot) and is recording properly . Check that cameras are unobstructed and recording device has
~30 days storage . Surveillance On signs are posted.
✔ Security Staff on Duty: Schedule at least 1–2 security personnel during peak hours (especially after
10pm) in addition to the manager . Confirm guards are in position: one at door, one roaming. All
staff know who the MOD (Manager on Duty) is each shift.
✔ Incident Response Plan Review: Before weekend shifts, do a brief team huddle to review protocols –
e.g. how to handle fights, when to call 911, etc. . Verify each staff member understands their role if an
incident occurs (who breaks up altercations, who calls police, who documents events).
✔ Alcohol Service & Training Compliance: All bartenders/servers have current TIPS/ServSafe Alcohol
training certification on file . Staff can recite the basic steps for refusing service. Bartenders use
standard pour tools (jiggers or measured spouts) for every drink – no free-pouring unless tested. No
extreme drink specials after 10pm that encourage bingeing .
✔ Intoxicated Patron Management: Cut off any patron exhibiting signs of intoxication (slurred speech,
etc.). Offer water or food, involve a manager if needed. Document any cut-offs in the log (time, person,
reason). Use a buddy system – never let one staff member deal with a very drunk person alone . If
someone must be removed for intoxication or behavior, do so calmly with two staff escorting.
✔ No Underage or Gambling Enforcement: Verify that no minors are on premises. Check that “No one
under 21, No Gambling Allowed” signs are posted . Staff to monitor pool games – no betting or
exchange of money should occur on game outcomes. Remove any cards, dice, or unapproved gaming
activity immediately.
✔ Late-Night Procedures: After 12:30/1:00 AM, enforce no re-entry – stamp hands or use wristbands to
identify who can’t return if they step out . Announce last call by 1:30 AM, stop music and raise lights at
1:45 AM to calm atmosphere . At 2:00 AM sharp, cease alcohol service and clear all drinks . Gently
clear patrons out, ensuring no one sneaks out with a drink. Lock doors once all patrons are out.
✔ Safe Departure: Encourage patrons to use taxis/rideshare if impaired – have phone numbers and Uber/
Lyft info readily available at the bar . Security or staff should visibly remain near the exit/parking for a
short time to supervise dispersal. Do not allow loitering outside after close (politely ask groups to head
home).
3 53
10
11
19 20
25
80
86
89
34
64 8
42
44 45
49
12
✔ Emergency Exits & Safety Equipment: Check that all emergency exits are unobstructed and lit (daily
walk-through) . Exits should be closed (not propped open) and alarmed. Test panic bar alarms
periodically. Also verify emergency lights and exit signs are functioning (test weekly).
✔ Lighting and Audio: Maintain adequate lighting in all areas, including the parking lot (replace burnt
bulbs promptly) . Keep music at a reasonable volume so staff can communicate (especially near
closing).
✔ Incident Log & Reporting: After any incident (fight, injury, ejection, property damage), write an
incident report in the log book immediately with full details . Include date, time, people involved,
actions taken. If serious (injury, major fight, any police involvement), notify upper management and prepare
to inform ABC or police proactively . Preserve any camera footage of incidents.
✔ Cash/Inventory Check: End of night, the manager/bartender team performs cash reconciliation and
basic inventory count. Log any discrepancies or comped items in the manager log . Secure cash in safe.
Ensure CCTV recorded properly during the night (no interruptions).
✔ Insurance & License Compliance: Ensure all licenses (liquor license, business license, pool table license)
are current and visibly posted . Keep a copy of the liquor liability insurance certificate on site and note
expiration dates to renew on time. Maintain required minimum insurance coverages (Liquor, GL, A&B rider,
property). Any time a policy is updated, put the new certificate in the bar’s compliance binder. Noncompliance can jeopardize operations, so review this checklist regularly.
This checklist should be reviewed by the general manager weekly and by on-duty managers nightly. By
following these steps, the Huntsville Poolroom Bar will create a safe, secure environment that complies with
all laws and protects the business’s longevity . Each item is designed to reduce risk and ensure that
security is an integral part of our operations and culture.
dr-02_legal.md
file://file-NR7NHTkFEEVPwYrbfDmQ4m
dr-05_unit_econ.md
file://file-AofkwNHPzZZrDNRhu3iof9
Bouncer Laws: What They Can (And Can’t) Do Legally? | LegalMatch
https://www.legalmatch.com/law-library/article/what-are-bouncers-legally-allowed-to-do.html
Video Retention: How Long Should You Keep Security Camera Footage? - Hospitality Insurance
Group
https://hmic.com/video-retention-how-long-should-you-keep-security-camera-footage/
16
106 25
68
67
94
107
77 105
1 2 5 6 8 9 17 29 32 33 40 41 42 43 44 45 46 48 49 50 51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 70 71 82 83 103 104 105
3 4 10 11 14 15 16 19 20 21 22 23 24 25 30 31 34 35 36 37 38 39 47 68 69 72 73 74 75 76
77 78 79 80 81 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 106 107
7 18 26 27 28
12 13
13
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
