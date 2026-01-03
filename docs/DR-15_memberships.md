# DR-15 Memberships Program

## Meta
id: DR-15
name: Memberships Program
gate: Gate 5
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
| Membership annual fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Membership discount percentage | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Target member count | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- memberships.annual_fee
- memberships.monthly_fee
- memberships.discount_pct
- memberships.target_member_count

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
Membership Model Strategy for Huntsville
Poolroom Bar
To engage customers and unlock recurring revenue, we propose a multi‑tier membership program. For
example:
Casual Tier: A low-cost entry level (e.g. $10/month or $100/year). Benefits might include a small
drink or table fee discount (say 5%), one complimentary off-peak play session per month, and early
notification of special events. This appeals to occasional players who want some perks without heavy
commitment.
Regular Tier: Mid-level membership (e.g. $20/month or $200/year) with stronger benefits. Offer
~10–15% off drinks and table rentals, two free off-peak play hours each month, and priority
reservations on busy nights. Regular members could also receive one complimentary guest pass or
birthday drink. The expected value (e.g. 15% off a ~$25 average check twice a month plus free plays)
should exceed the fee for frequent patrons.
VIP Tier: Premium membership (e.g. $30–35/month or ~$300/year). Benefits include ~20% discounts
on all purchases, unlimited free off-peak play, guaranteed prime-time table reservations, invitationonly tournaments or social nights, and special welcome swag (branded cue, T-shirt, etc.). This tier
targets league players and enthusiast groups, providing a “mini-club” experience.
Each tier should explicitly state its value. For instance, a $20/month membership that includes two free $8
covers and ~$5–10 in drink discounts per month yields roughly $21–26 of value in an average month (using
core hour spends ). Setting prices slightly below the break-even point for heavy users encourages
adoption. A summary table might compare tiers:
Tier Price (Mo/Year) Core Benefits
Casual \$10 / \$100 5% drink discount; 1 free off-peak play/month.
Regular \$20 / \$200 10% discount; 2 free off-peak plays; priority booking.
VIP \$35 / \$300 20% discount; unlimited off-peak play; member events and swag.
Figure: An upscale pool hall interior – membership perks (discounts, free play, priority booking) should make
customers feel catered-to in such a setting.
Value Proposition: The tiered pricing aligns with local usage patterns and competitor benchmarks. In
Huntsville, nightlife demand is moderate; Bumpers Billiards charges a flat $8 per person for all-night play
, and Chips & Salsa uses a $5 cover for unlimited pool . A membership program should let frequent
players pay less per visit. For example, a member saving even $2 per outing on drinks or play fees
accumulates value quickly. Our unit-economics data shows an average core‐hour spend of ~$25 per
customer ; a 10–20% discount on this for members yields $3–5 in net savings per visit. Over a month,
that covers much of a $20 membership fee.
•
•
•
1 2
2 3
4
1
Furthermore, league and peak/off-peak trends support the model. Huntsville has ~320 league players in
APA teams ; these players often get free or waived table fees on league nights in exchange for buying
drinks . Extending similar perks to members (e.g. free league-night tables or discounted league entry)
can draw this core group. On weekends and evenings (the busiest times ), members could reserve tables
in advance. During slower hours (e.g. weekdays 11am–4pm), members might get extra discounts or hourly
deals, incentivizing them to play when the hall would otherwise be quiet. In short, membership perks
should be tied to both high-value (late-night) usage and demand-fillers (weekday afternoons).
Revenue Impact Modeling: We estimate membership revenue based on plausible adoption. Huntsville’s
metro has ~492,000 people, and ~40–50k are interested in billiards; a few thousand may frequent a new hall
. Assuming a 3,000-person core base for modeling, even modest adoption yields sizable recurring
revenue:
Adoption Rate Members (of 3,000) Monthly Revenue (at \$20/mo)
5% 150 $3,000
10% 300 $6,000
20% 600 $12,000
Even at 5% take rate, $3,000/month in predictable income is notable for a local bar. These figures can be
scaled if the actual membership price differs or if more members sign up for higher tiers. (The base
assumes ~3,000 engaged customers ; a higher TAM would amplify revenue.) This recurring stream
improves cash flow and justifies marketing and benefits investment.
Operational Integration
Implement the membership program via the POS and staff processes:
- POS Setup: Use your point-of-sale system’s loyalty or membership features. Many systems allow creating
membership or prepaid cards. For example, one hall uses a card that holds a stored balance and grants a
flat 20% discount whenever customers use it . Setup is straightforward: equip the host stand/bar with a
card reader or enable phone-number lookup. When members pay, staff select the member or scan the card
to automatically apply discounts and track play hours .
- Check-in & Discounts: Train staff to verify membership at entry or point of sale. Members might flash a
card/QR code or give a PIN, triggering the POS to apply the correct discounts to table or drink charges.
Have clear signage and screens prompting for member status. For table rentals, configure both hourly rates
and packages; members could have a lower hourly rate or free hours automatically added by the system.
- Loyalty Events & Promotions: Use the membership database to email or text members about exclusive
events. For instance, hold a members-only tournament or “members happy hour” where participation is
reserved for cardholders. Staff should check membership status at the door for such events. When running
drink specials or contests, simply target “members” in the POS or reservation system to ensure only
members get the deal. Integrating membership into the existing reservation system (or using popular tools
like FiveStars) helps automate perks. As one owner notes, modern loyalty programs let you award points
per dollar spent, redeemable for free plays or merch .
By merging membership logic into the POS, the program flows through existing workflows: bartenders and
hosts follow familiar checkout steps, just with a new discount code or account ID for members.
5
6
7
8
8
9
10
11
2
Legal & Regulatory Alignment
The membership program must fully comply with Alabama/Huntsville law. Key points:
- Optional Membership: Alabama does not require customers to join a club to play pool or drink; in fact,
memberships are purely optional benefits . You should not make membership mandatory for entry or
alcohol purchase (that could imply a “private club” and violate ABC rules). Instead, sell memberships as addons.
- Licensing & Fees: All usual licenses still apply. The venue needs its ABC liquor license (Class I lounge, onpremises) with city approval , and the annual privilege licenses (e.g. beer/wine licenses). It also must buy
a pool room license for each table ($38.50/table/year) and post a $1,000 bond – this enforces no gambling
and no minors . Membership does not exempt any of these requirements.
- Business Taxes: Alabama law considers any revenues (including membership dues or cover fees) as
taxable income. In Huntsville, a general business license covers “other revenues (cover charges, table fees,
etc.)” . Membership fees would fall under this category. Plan to declare and pay the appropriate city
privilege tax on all membership receipts just as with cover charges.
- Age & Conduct: By law, no one under 21 may loiter or play at a licensed pool hall . Members must still
abide by these rules; a membership card doesn’t override the “No Minors” requirement. Similarly, all
patrons (including members) must follow standard liquor laws (e.g. no drinking after 2 AM). Huntsville
strictly forbids any alcohol consumption after 2 AM even in “members-only” areas . If you hold private
late-night events for members (e.g. an after-hours tournament), you cannot serve alcohol – only soft
drinks are allowed .
In summary, treat the membership like any other revenue line: collect dues through the POS, remit taxes on
them, and maintain full liquor/pool licensing. Use memberships only as a marketing benefit, not a legal
workaround. All safety and occupancy rules still apply to members.
Best Practices & Differentiators
Tiered loyalty is common in successful pool venues. For instance, one hall runs a 3-tier VIP program where
each tier automatically gets 20% off purchases as long as they have a prepaid balance on their account .
They even give sign-up bonuses (e.g. \$20, \$100, \$200 in credits) to higher tiers . Another switched
from hours-based rewards to a points system: players earn points per dollar spent and redeem them for
free table time, drinks or merch . These ideas can inspire our program.
To make membership feel premium yet welcoming: give tangible perks and a sense of exclusivity without
shutting out casuals. Possible ideas include: branded membership cards or T-shirts, a reserved “Members’
Section” with a special high-top table, and periodic members-only events (tournaments, “game nights,” etc.).
Gift new members a useful sign-up package (e.g. a cue chalk gift, drink tokens, or voucher) to reinforce
value . Keep tier names catchy (e.g. “Silver/Gold/Platinum Shooters” or pool-themed names) and cap the
number of VIP spots so that high tiers feel exclusive.
Balance these with accessibility: ensure non-members can still enter, play, and enjoy the bar easily. For
example, advertise “Casual membership from \$10/mo” clearly (so it’s inviting, not mandatory). Offer a mix
of free or community events (like open tournaments) so everyone feels welcome, with members simply
getting priority or extras. National best practices emphasize experiential perks: “priority reservations” and
1
12
13
14
13
15
15
9
16
11
16
3
“members-only happy hours” can make members feel special. By combining competitive pricing with
genuine added value (discounts, freebies, convenience), the membership becomes a loyalty driver.
Figure: A well-lit pool table in a friendly venue – adding exclusive perks and decor (e.g. a “VIP” section or club card)
can make members feel part of a select community without alienating others.
Recommendations: Implement the program gradually. Start with 2 tiers and adjust pricing based on
uptake. Track member usage: if Regular members visit 2× more than non-members, the model is working.
Collect feedback and iterate – perhaps adjusting off-peak benefits or discounts. Monitor legal compliance
closely (especially cut-off times). With the right mix of perks and pricing, a membership strategy can boost
customer loyalty and add steady revenue, giving this Huntsville poolroom an edge in a modest but growing
market.
Sources: Huntsville market and unit-economics data ; competitor pricing ; legal requirements
; and industry examples .
dr-05_unit_econ.md
file://file-AofkwNHPzZZrDNRhu3iof9
dr-01_market.md
file://file-UAvg9DPv5Qjc6ukH83rPeB
Pool Hall Rewards Program | AzBilliards Forums
https://forums.azbilliards.com/threads/pool-hall-rewards-program.390387/
dr-02_legal.md
file://file-NR7NHTkFEEVPwYrbfDmQ4m
1 8 2 3
13 15 9 16
1 4 6
2 3 5 7 8
9 10 11 16
12 13 14 15
4
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
