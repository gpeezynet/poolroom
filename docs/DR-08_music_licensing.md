# DR-08 Music Licensing (ASCAP/BMI/SESAC/GMR)

## Meta
id: DR-08
name: Music Licensing (ASCAP/BMI/SESAC/GMR)
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
| ASCAP annual license fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| BMI annual license fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| SESAC/GMR annual license fees | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- music_licensing.ascap_per_year
- music_licensing.bmi_per_year
- music_licensing.sesac_per_year
- music_licensing.gmr_per_year
- music_licensing.total_music_licenses_per_year

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
Music Licensing Overview
In the U.S., any music played publicly outside a private home requires a license from the rights holders.
This applies to recorded background music (e.g. radio, streaming, CDs, jukebox) as well as live
performances (bands, DJs, karaoke) . The major U.S. Performing Rights Organizations (PROs) –
ASCAP, BMI, SESAC, and GMR – license public performances of songs in their repertoires. Each PRO
represents different songwriters/publishers, so a blanket license from one (e.g. ASCAP) covers only its
catalog . In practice a bar must obtain licenses from all applicable PROs whose music is played
(many songwriters belong to multiple PROs) . (For example, ASCAP and BMI are large nonprofit
PROs, while SESAC and GMR are smaller, invitation-only/licensing-focused PROs covering select artists.)
Venues typically obtain blanket licenses (annual contracts) for unlimited uses in a given period. Some PROs
also offer one-time or special-event licenses (for concerts or festivals), but these are uncommon for regular
bar use. Failure to license any public performance is infringement: PROs can sue or demand payment per
song played without permission, with statutory penalties of \$750–\$30,000 per song (up to \$150,000 if
willful) . PROs routinely audit or investigate bars (e.g. “sending reps to listen to your music” ) and
pursue unpaid fees. In short, any non-exempt music use in the bar (background playlists, live/DJ sets,
karaoke tracks, televised music, etc.) requires licensing from the relevant PROs .
2. Licensing Costs and Coverage
Typical Fees (ASCAP, BMI, SESAC, GMR): Annual blanket fees vary by venue size, capacity, and music usage.
For a 5,000–10,000 sq.ft. bar with ~100–150 patrons, estimates are on the order of hundreds of dollars per
PRO. For example, ASCAP’s baseline fee is roughly \$390/year (for very small bars it can be as low as \$1/
day ). BMI licensing usually runs \$250–\$400+ annually for a venue of this size (note
1 2
3 4
5 6
7 8 9
1 10
11
12 13 14
1
SoundMachine estimates \$250–\$2,000 depending on factors ). SESAC often averages around \$700/
year , and GMR is not publicly priced (often negotiated at a premium since it covers major hit writers)
. Combined, a multi-PRO license bill can easily reach \$1,000+ per year (Jukeboxy cites ~\$1,000+
for all PROs on a 5,000 ft² site ). Some hospitality associations offer discounts (e.g. Alabama Restaurant
Assoc. has ~20% off BMI) to lower this cost.
PRO Typical Annual Fee Notes
ASCAP ~\$300–\$400 (baseline for small bar) Covers ASCAP catalog only.
BMI
~\$250–\$2,000 (wide range; ~$400 typical) Covers BMI catalog.
SESAC ~\$700+ (often similar to BMI) Invite-only PRO; separate license needed.
GMR Negotiated (often >\$1,000) Covers top artists (Rihanna, etc.); inviteonly.
Pricing Models: Most bars use blanket licenses (annual flat fees). Some PROs allow single-event licenses
or “festival” licenses for one-day concerts (but these are rarely used for bars). There is no practical “persong” license for a bar; per-song fees apply only to infringement penalties.
Background vs. Live/DJ/Karaoke: License fees rise when you add live or interactive elements. PROs
categorize uses differently – for example, ASCAP’s rate sheets charge extra per-occupant fees if you host DJs,
karaoke, dancing, or games in addition to background music . In practice, bars without live music might
pay at the lower end (e.g. \$500–\$1,500/PRE-year per PRO ), while adding regular live bands, DJs or
karaoke nights increases costs. (One example: on a 5,000 ft² site, ASCAP might base ~\$298/year, plus
surcharges for extra speakers or live acts .) Karaoke typically counts as a special category (like a DJ) and
may have a small extra fee, and often requires licensing the karaoke tracks themselves (see §4). In all cases,
a single blanket license usually covers unlimited uses during its term, so you won’t pay “per song” under a
lawful license – only fixed annual or periodic fees.
3. Enforcement and Risks
Playing unlicensed music poses severe legal and financial risks. Statutory damages for copyright
infringement can reach \$750–\$30,000 per song (and up to \$150,000 per song if willful) , plus the
venue may owe the PROs’ legal fees. Courts have fined small businesses tens of thousands in such cases.
PROs actively enforce compliance: investigators often pose as customers, note what songs play, then bill
non-licensed venues for thousands of dollars worth of songs . (Bar owners report cases where PROs
demanded \$750 per song played without a license .)
In Alabama specifically, there have been recent enforcement actions. For example, BMI sued Moe’s BBQ in
Cullman, AL (2022) for “willful” infringement of nine songs played without permission . That case
highlights the risk: BMI sought damages after attempts to educate the owners failed. Elsewhere, ASCAP
recently filed dozens of lawsuits against bars and restaurants nationwide (including one Illinois pub),
showing that no region is exempt. (As one bar owner noted, ASCAP asserts an average cost of about \$2/
day for full coverage – far below potential fines.) In short, if unlicensed music use is discovered (through
14
14
11 11 15
15
11 15
13
14
14
16
17
15
8 7
9
18
19 20
21
6
2
audits, sting inspections, or follow-up to complaint calls), expect cease-and-desist demands and lawsuits.
Worst-case, repeated infringement can even force a business to shut down under legal pressure .
4. Jukebox and Streaming Services
Commercial jukeboxes (e.g. AMI, TouchTunes): Standard coin-operated jukeboxes pay their own licensing
fees. For instance, TouchTunes states that performances on its machines are licensed by ASCAP, BMI, SESAC,
and GMR . In practice, if your bar installs a commercial jukebox provider like TouchTunes or AMI, you do
not need separate PRO licenses for music played through that jukebox system. The jukebox company holds
the blanket rights for its music catalog (much as a subscription service does). However, music played
elsewhere (house playlist, karaoke, etc.) still needs licensing.
Consumer streaming (Spotify, Apple Music, YouTube, etc.): Personal streaming accounts cannot be used
legally in a bar. Spotify’s own policy explicitly forbids “broadcast[ing] or play[ing] Spotify publicly from a
business” , and this applies to any personal subscription service (Apple Music, Amazon Music, Pandora,
YouTube, etc.). Using a free radio stream (internet or broadcast) in a bar without paying the proper license is
also infringement (it’s a public performance). In short, a regular Spotify/Premium/Family account – or the
free tier – is only licensed for private, home use .
Licensed business music services: To stay compliant, use a service designed for commercial use. These
bundled services pay PROs (and sometimes record labels) on your behalf. Examples include Pandora Cloud
Cover, Soundtrack Your Brand (formerly Spotify’s business arm), SoundMachine, Cloud Cover Music,
Rockbot, TouchTunes Jukebox, and others. These subscriptions typically cost on the order of \$20–\$40/
month per location (often under \$25/mo if prepaid annually), and they promise “all licensing included.” For
instance, Pandora Cloud Cover advertises that its \$16.95/mo plan “covers all music rights and licensing
fees” (ASCAP, BMI, SESAC, etc.) for business use . Likewise, SoundMachine and similar platforms handle
PRO licenses as part of the service . Using one of these ensures you can play built-in playlists or your
own songs legally. (Even then, if you have live bands, confirm whether the plan covers those performances.)
22
23
24
24 25
14
26 2
3
5. Bundled Licensing Options
Because each PRO is separate, it can be tedious to get four licenses. There are a few ways to streamline
compliance:
All-in-one music subscriptions: As noted, some business streaming services (Cloud Cover,
Soundtrack, SoundMachine, etc.) bundle all PRO fees into one monthly charge . For example,
SoundMachine advertises a single package (currently about \$323/yr) that covers ASCAP, BMI, SESAC
and GMR . This can be more affordable and easier than dealing with each PRO separately.
Commercial jukebox or background music providers: If you use an on-site jukebox (TouchTunes/
AMI) or a licensed BGM solution (like Jukeboxy, Cloud Cover, Mood Media, etc.), those providers may
handle some or all licenses. As above, a jukebox covers its own music. Some BGM vendors integrate
PRO licensing in their fee. Always verify what’s included.
“One-stop” licenses: There is no U.S. single-license covering all PROs beyond these subscription
services. PROs do not issue a combined ASCAP+BMI+SESAC+GMR license themselves. (Some
countries have “one license” schemes, but not in the U.S.) However, some local businesses use
umbrella associations (e.g. state hospitality associations) to purchase multiple licenses at once; for
example, BMI and ASCAP offer discounts through restaurant associations in some states.
In summary, the easiest compliance path is often to subscribe to a licensed music service that explicitly
covers PROs. If you choose to license directly, expect roughly \$300–\$700 per PRO per year as a ballpark
(subject to occupancy and music type) .
6. Integration with the Business Plan
Integrating music legally into your bar’s strategy involves both planning and budgeting:
Entertainment schedule: Use music to attract customers strategically. For example, karaoke on
slower weeknights and live bands or DJs on busier weekends can boost traffic. Plan a calendar
(e.g. DJ on Fridays, acoustic on Sundays). Make sure your licenses account for these events: some
PRO license forms ask how many events/nights per week you host live or karaoke.
Playlist and ambiance: Even when no live acts are booked, curated background playlists keep the
vibe alive. A licensed streaming service lets you schedule different music by time of day (lounge
music earlier, dance hits later) with confidence of compliance .
Budgeting for licensing: Treat music licensing as a fixed overhead (roughly \$100–\$200/month for
all PROs, by one estimate ). Include this in your financial plan. Some operators add a small cover
charge or “entertainment fee” for special nights to offset costs. For instance, charging \$1–\$5 cover
on live band nights can recoup licensing and talent fees. Promoting drink specials or packages tied to
events (e.g. “Karaoke Tuesday: $10 pitchers”) can also boost revenue on those nights.
Legal compliance as business insurance: Emphasize to stakeholders that licensing is not optional.
It’s like insurance – paying, say, \$1–\$2 per day keeps you out of danger. Many composers point out
•
14 27
28
•
•
28 15
•
•
29
•
30
•
4
that a licensed business actually helps artists earn (bars distribute music indirectly) . This
perspective can justify the expense.
In practice, successful bar operators plan entertainment around licensing. For example, if weekday nights
are slow, schedule karaoke or open-mic nights then (since costs are fixed, filling seats can improve profit
with minimal extra licensing). On peak nights, a DJ or band justifies a cover charge. Keep meticulous records
(dates, performers, playlists) in case a PRO ever audits you. Finally, negotiate with providers: joining a
hospitality association can net discounts on BMI/ASCAP fees, and shopping around for a licensed music
service (SoundMachine, Pandora Cloud Cover, etc.) can yield bundled deals.
Summary: A Huntsville poolroom bar must obtain public performance licenses from ASCAP, BMI, SESAC,
and GMR (or use a service that covers them) to play any copyrighted music – whether background playlists,
live bands, DJ sets, or karaoke . Budget roughly \$1,000+ per year in licensing (all PROs combined)
depending on size and usage . Ensure live events and karaoke are accounted for, as they can add
fees. Using a licensed streaming/jukebox service will automate compliance, whereas self-curated music
requires securing each PRO license. Integrate these costs into your business model (e.g. via event cover
charges or promotions). With proper licensing, you avoid expensive lawsuits and can focus on the ambiance
that music adds to your bar .
Sources: Official PRO FAQs and licensing guides ; industry publications ; expert blogs ;
and news reports of enforcement cases . (All figures and examples are specific to U.S. law and the
hospitality context.)
Music Licensing for Bars, Restaurants, Breweries, Wineries and other Eating and Drinking
Establishments | BMI.com
https://www.bmi.com/licensing/entry/bars_and_restaurants
Background Music for Business Made Easy | SoundMachine
https://sound-machine.com/
BMI Licensing for Businesses | Complete Guide, Cost (Updated 2021)
https://www.jukeboxy.com/blog/bmi-licensing-for-businesses/
SESAC Music Licensing for Business | SoundMachine
https://sound-machine.com/licensing/sesac
Music Licensing for Bars and Restaurants: What You Need to Know | Bar Marketing - Bar
Business - Opening a Bar - Bar Owner
https://www.barbusinessowner.com/public/Music-Licensing-for-Bars-and-Restaurants.cfm
Poison Ivy Pub in Roscoe is being sued over music licensing fees
https://roscoenews.com/poison-ivy-pub-roscoe-among-13-venues-nationwide-being-sued-not-paying-ascap/
Can you play Spotify in your business? | Soundtrack
https://www.soundtrack.io/blog/can-you-play-spotify-in-a-business/
Music Licensing Insights | Everything You Need to Know
https://cloudcovermusic.com/music-licensing-guide
31
1 2
15 28
8 1
1 2 17 15 28 14
19 8
1 12
2
3 7 13 15
4 11 22 26 27 28 30
5 9 10 17 18
6 21
8 25 29 31
14
5
[PDF] Music Type Rate Per Occupant Fee 1. Live Music (check ... - ASCAP
https://www.ascap.com/~/media/files/pdf/licensing/classes/2021-license-rates-reports/bgt-2021.pdf
Alabama restaurant sued for copyright infringement of 9 classic songs – Action News Jax
https://www.actionnewsjax.com/news/trending/alabama-restaurant-sued-copyright-infringement-9-classic-songs/
O7WDZBBZBNA25JJF454VAYUTAY/
Licenses | TouchTunes
https://www.touchtunes.com/licenses
Spotify for public or commercial use - Spotify
https://support.spotify.com/us/article/spotify-public-commercial-use/
16
19 20
23
24
6
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
