# OUTLINE — "Early Locomotion, Explained" (42 slides)

Stage 1 deliverable, 18 October 2026. Read with `RESEARCH_NOTES.md` (diagram specs), `ASSET_MANIFEST.md` (images) and `STAGE2_CLOUD_BRIEF.md` (build rules). This is a **read-alone deck**: no presenter, no speaker notes. Design statuses come from `Design/GAME_DESIGN.md`. No status was changed and no Open Question was resolved.

## Narrative arc

The reader starts knowing nothing. Slides 1–3 say what the mod is and how to read the tags. Slides 4–13 are primers: what Satisfactory is, then how real steam railways work (track, engine, coal, water, tenders, why signals exist) and a glossary. Slides 14–17 explain the mod's idea: steam rail is not "vanilla trains, but earlier", every limit has an answer, and electric rail still wins in the end. Slides 18–24 cover the locomotives, wagons, range and tenders. Slides 25–27 cover stations and servicing. Slides 28–34 are the signalling chapter (blocks, semaphores, signal box, the whole system, limits, automatic control, later signals). Slides 35–36 look ahead to the monorail upgrade and optional post-launch packs. Slides 37–38 cover regional styles, running numbers and the railway guide. Slides 39–40 say plainly where the project is and what is still undecided. Slides 41–42 credit every image.

## Style tokens (proposed; reused from the accepted Reporting templates where noted)

Reused: Arial throughout, dark background, native shapes for diagrams, restrained layouts (`Reporting/ACCEPTED_PRESENTATION_TEMPLATES.md`). Changed: the templates' blue-charcoal and brass accent become charcoal and Satisfactory-style orange.

```yaml
canvas: 13.333 x 7.5 in (16:9)
font: Arial (all text)
language: en-GB
colours:
  background: "#1E2126"
  panel: "#2B2F36"
  panel_alt: "#343A43"
  line: "#4A515B"
  text: "#F2F2F2"
  muted: "#A9B0B8"
  accent_orange: "#F28C28"
  stop_red: "#E5484D"
  clear_green: "#3FB950"
  caution_amber: "#F2C14E"
  water_blue: "#4DA3FF"
  electric_blue: "#6CA0DC"
  coal: "#1B1D21"
  steel: "#9AA0A6"
  sleeper_brown: "#6B5B4B"
tag_chips:   # 1.5 x 0.4 in, 14 pt bold, upper case, rounded, top-right at (11.2, 0.5)
  Agreed:      {fill: "#3FB950", text: "#101418"}
  Proposed:    {fill: "#B084F5", text: "#101418"}
  Provisional: {fill: "#4DA3FF", text: "#101418"}
  Undecided:   {fill: none, outline: "#A9B0B8 2pt", text: "#F2F2F2"}
  Background:  {fill: "#4A515B", text: "#F2F2F2"}   # real-world fact, not a design status
  inline_chip: 1.1 x 0.3 in, 12 pt, same colours (used beside a single statement)
type_scale:
  title: 36 pt bold, at (0.6, 0.45), height 0.8
  section_label: 12 pt caps, muted, at (0.6, 0.18)
  caption: 20 pt (never below 18 pt), inside a panel bar at (0.6, 6.4) 12.13 x 0.6 with an orange 0.08 in left rule
  diagram_labels: 14-18 pt (14 pt is the minimum anywhere on a diagram)
  credit_lines: 10 pt muted at (0.6, 7.1)  (legal credits are the only text below 14 pt; credit tables on slides 41-42 use 11 pt)
  slide_number: 12 pt muted, bottom right
layout:
  margins: 0.6 in left and right
  content_area: y 1.4 to 6.3
  corner_radius: 0.08 in on panels and images
  stroke: 1.5 pt; connectors 2.25 pt
```

**Rules for every slide**
- One idea per slide. Aim for 25 words or fewer in total (caption plus labels). Exempt: slides 2, 13, 32, 41, 42.
- Quoted text in the table below is exact on-slide wording. Text in the visual-spec column that is in quotation marks is a diagram label and also goes on the slide.
- Every slide except 1, 2, 41 and 42 carries the status chip named in the **Tag** column. A second inline chip appears next to any single statement with a different status (Proposed or Provisional). Never rely on colour alone: every state is also written in words.
- No speaker notes. No animations or transitions. Alt text on every picture and diagram group (use the "What it shows" text in `ASSET_MANIFEST.md`; for diagrams, one sentence describing the idea). Reading order: title, chip, visual, caption.
- Never show Superseded ideas. Never state a Playtest Target as fact: it carries a Provisional chip or is left out.
- Photos go in unmodified except for resizing, with the credit line directly under the picture (10 pt). A picture of a real locomotive never claims to be the mod's model.

## Slide table

Spec shortcuts: **SIG-28 to SIG-31** are the signalling specs in `RESEARCH_NOTES.md` ("FULL SIGNALLING DIAGRAM SPEC"). **SPEC-A to SPEC-I** are in the same file under "OTHER DIAGRAM SPECS".

| # | Section | Title | Caption (exact) | Visual spec | Tag | GAME_DESIGN.md ref | Images |
|---|---------|-------|-----------------|-------------|-----|--------------------|--------|
| 1 | Welcome | Early Locomotion | "A steam railway mod for Satisfactory, explained for newcomers. Everything here is a plan, not a finished mod." | Title slide, no chip. Left 55%: title in 54 pt bold, orange rule under it, caption below. Right 45%: R01 full height, cropped, rounded. Credit line: "Early test model. Not final art." | — | Core concept | R01 |
| 2 | Welcome | How to read this guide | "Every idea carries a tag in the top-right corner." | Legend of five rows, each a real chip plus a 20 pt meaning: Agreed "Decided." Proposed "Suggested, not confirmed." Provisional "A test number that may change." Undecided "Still an open question." Background "A real-world fact." | — | Core concept (status convention) | — |
| 3 | Welcome | The idea in one picture | "Cheap track and trains. Real limits. You solve them with coal, water, signals and planning." | Four boxes (2.6 x 1.6 in) left to right, orange arrows: "Cheap to build" → "Real limits: speed, range, signals, stations" → "Your answers: tenders, service stops, signal boxes" → "Later: electric monorail". R01 small inset (2.6 x 1.5 in) bottom right. | Agreed | Core concept; Balance philosophy | R01 |
| 4 | The game | What is Satisfactory? | "A first-person game about building factories. You mine, make and move materials until it all runs itself." | Factory strip from shapes, left to right: miner (square plus drill triangle), conveyor belt (long dark bar with chevrons), smelter (box plus chimney), constructor (box), storage crate. A small player figure on a platform labelled "You". Definition box (18 pt): "Vanilla = the game without mods." Muted 14 pt footer: "By Coffee Stain Studios. Full release 2024." | Background | — (see RESEARCH_NOTES §7) | — |
| 5 | The game | Where the mod fits | "Technology unlocks in tiers. The mod adds steam railways early, before the game's electric trains." | Four-step staircase rising left to right. Step labels: "Tier 3: Early Steam Railways" (small engine, basic wagon, steam station, semaphore, signal box); "Tier 3 to 4: Railway Expansion" (medium engine, more wagons, better box); "Tier 4 to 5: Heavy Steam" (large engine, heavy wagons, auxiliary tenders, better signals); "Tier 6: Monorail" in electric blue (the game's electric trains). Footer chip: "Tiers and prerequisites: provisional. Undecided (OQ01)." | Provisional | Progression; OQ01 | — |
| 6 | Steam railways | Track | "Two steel rails sit on sleepers over stone ballast. The sleepers keep the rails the right distance apart." | Left: P01 (4.2 x 3.1 in) with credit. Right: end-on cross-section from shapes: grey ballast trapezoid (4.2 x 0.9 in), three brown sleepers, two steel rails. Labels "Rail", "Sleeper", "Ballast". Double-headed arrow between the rails: "Gauge: 1,435 mm on most railways". | Background | — | P01 |
| 7 | Steam railways | How a steam engine works | "Coal heats water. Steam pushes pistons. Rods turn the wheels." | Side cutaway from shapes, 8 in wide: orange firebox at the rear, long boiler (rounded rectangle, blue inside), chimney at the front, cylinder with piston, connecting rod and coupling rod over three wheels. Orange badges 1 "Fire", 2 "Steam", 3 "Piston", 4 "Wheels". Curved arrow from cylinder to chimney: "Exhaust". P03 inset at right (3.6 x 2.4 in) with credit. | Background | — | P03 |
| 8 | Steam railways | Coal, water and steam | "Steam is used once and lost. So water runs out first. Coal lasts longer." | SPEC-A. | Agreed | Fuel and water servicing | — |
| 9 | Steam railways | Tender or tank? | "A tender engine pulls a coal and water wagon. A tank engine carries both itself." | Two photo cards (5.8 x 3.9 in): P04 "Tender engine", P05 "Tank engine". Orange leader lines with labels: "Tender: coal and water behind the cab"; "Side tanks: water. Bunker: coal." | Background | Locomotives; Auxiliary tenders | P04, P05 |
| 10 | Steam railways | Taking on water | "A water crane swings over the engine. Water flows down from a tank above." | SPEC-B. | Background | Fuel and water servicing | P06, P07 |
| 11 | Steam railways | Taking on coal | "Coal starts higher than the tender. A ramp or tower lets gravity fill it." | SPEC-C. | Background | Fuel and water servicing | P08, P09 |
| 12 | Steam railways | Why trains need signals | "Trains cannot swerve. They need a long way to stop. Signals keep them apart." | Two stacked tracks. Top: one track, two trains nose to nose, red cross between them, label "No warning: crash". Bottom: the same track split into three blocks by two signals, one train per block (a small copy of SIG-28 objects), plus a braking-distance bar under the lead train from its nose to a dashed line, label "Long stopping distance". | Background | Signalling | — |
| 13 | Steam railways | Words you will meet | "Short meanings for the words in this guide." | 2 x 4 grid of cards (2.9 x 1.3 in), term in 20 pt bold orange, meaning in 18 pt: "Vanilla: the game without mods." "Tier: a step of unlocks." "Wagon: a vehicle that carries cargo." "Tender: a coal and water wagon behind an engine." "Block: a stretch of track that holds one train." "Semaphore: a signal with a moving arm." "Signal box: where a signaller works the signals." "Service stop: a stop to refill coal and water." | Background | — | — |
| 14 | The mod's idea | Not "trains, but earlier" | "Steam rail is not electric trains with an early unlock. It works in its own way." | Two-column comparison, five rows with simple shape icons. Headers "Vanilla electric (later)" in electric blue and "Early steam (this mod)" in orange. Rows: Track "Monorail beam" / "Two-rail track"; Power "Electricity" / "Coal and water"; Stops "No refuelling" / "Service stops"; Signals "Block and path" / "Semaphores and boxes"; Station "Compact" / "Large". | Agreed | Core concept; Stations | — |
| 15 | The mod's idea | Every limit has an answer | "Short range, small loads, a busy line, slow trips: each has a fix." | Four rows, each a grey limit chip with orange arrows to answer chips. "Short range" → "Auxiliary tender", "Service stop", "Bigger engine". "Small loads" → "A suitable engine and train length". "Busy line" → "More signals and boxes". "Slow overall" → "Convert to monorail later". | Agreed | Balance philosophy; Service points | — |
| 16 | The mod's idea | Why steam stays behind electric | "Steam is cheap and early. Electric wins on speed, throughput, traffic and convenience." | SPEC-G. | Agreed | Balance philosophy; Late steam and advanced infrastructure | — |
| 17 | The mod's idea | The mod's track | "Two thin rails on sleepers, built from iron plates and rods. Speed is the lowest of three limits." | Left: R02 (5.6 x 3.15 in). Below it: R05 (2.6 x 1.95 in) labelled "Close-up: chairs and rails". Right: P02 (3.6 x 2.7 in) labelled "A real railway, for comparison". Bottom band: rounded box "Speed = lowest of: track limit, signal limit, engine limit" with an inline Proposed chip. Footer: "Longest piece of track: undecided (OQ02)." | Agreed | Track design; OQ02 | R02, R05, P02 |
| 18 | Locomotives | Three roles | "Small, Medium and Large each have a job. Bigger is not simply better." | SPEC-F. | Agreed | Locomotives; OQ05 | — |
| 19 | Locomotives | Small: the branch-line tank | "Small carries its own coal and water. It is cheap, light and best on short branches." | Left: P10 (5.6 x 3.7 in) with note under it: "A related Fowler tank engine (a Jinty). The design's reference, the Dock Tank, has no survivor to photograph." Right: three icon rows: "No tender", "Weakest hauler", "Cheap to run". Inline Proposed chip on "Struggles with long trains and hills". | Agreed | Locomotives | P10 |
| 20 | Locomotives | Medium: the long-range runner | "Medium has a tender and more range. It uses more coal and water. It may be the fastest class." | Left: P11 (5.6 x 3.5 in), credit "Reference: Merchant Navy class". Right: rows "Normal tender: more coal and water", "Burns more", "Auxiliary tender: a practical extra". Inline Proposed chip on "Fastest class", with "Undecided (OQ05)" beside it. | Agreed | Locomotives; OQ05 | P11 |
| 21 | Locomotives | Large: the heavy hauler | "Large pulls the heaviest trains. It is thirsty and slow to speed up. It suits heavy freight." | Left: P12 (5.6 x 3.7 in), credit "Reference: BR Standard 9F". Right: rows "Most powerful", "High coal and water demand", "Auxiliary tender for very long routes". Inline Proposed chip on "Slower to speed up". | Agreed | Locomotives | P12 |
| 22 | Locomotives | Wagons | "Steam wagons are cheaper and hold less. About 20 item stacks, against 32 in a vanilla wagon." | Two side-view wagons (3.4 x 1.4 in, wheels drawn). Orange wagon holds a 4 x 5 grid of small squares (20). Blue wagon holds a 4 x 8 grid (32). Labels "Steam wagon: about 20 stacks", "Vanilla wagon: 32 stacks". Legend: "Stack = a pile of one item." Inline Provisional chip. Footer: "Wagon catalogue: undecided." | Provisional | Balance philosophy | — |
| 23 | Locomotives | How far can an engine go? | "Range comes from real tank sizes and real use. Hills and heavy loads use more. Coasting uses less." | Left: coal and water gauges for one engine and a mock readout card "Range left" (dial icon, no number) with inline chip "Range estimate: Agreed direction". Right: table, Provisional chip, header "Route-dependent targets": rows Small / Medium / Large; columns Water, Coal: Small 2 to 3 km, 4 to 5 km; Medium 4 to 5 km, about 7 km; Large 6 to 7 km, about 10 km. Bottom: "Compacted Coal burns more efficiently." (Agreed). | Agreed | Fuel and water servicing | — |
| 24 | Locomotives | Tenders | "A normal tender belongs to the engine. An auxiliary tender is an extra wagon: more range, less pulling power." | Train strip at y 2.4: engine plus normal tender joined by a bracket "One vehicle" (inline Proposed chip); a gap; a hatched wagon "Auxiliary tender: a separate wagon"; then three cargo wagons. Under the hatched wagon two Proposed chips "Water only" and "Coal and water". Two downside icons: "Carries no freight", "Adds weight". P18 (3.4 x 2.3 in) bottom left, credit "A real tender, for illustration". | Agreed | Auxiliary tenders | P18 |
| 25 | Stations | A steam station | "A steam station is big. It has a water tower, coal loading, a signal box and a platform." | SPEC-D. | Agreed | Stations | P17 |
| 26 | Stations | Servicing takes time | "The machinery finds each engine's hatches. Servicing takes visible time. Then it folds away." | SPEC-E. | Agreed | Stations; Fuel and water servicing | — |
| 27 | Stations | Service points | "Separate coal and water stops make long routes possible. Not every stop needs a full station." | SPEC-I. | Proposed | Service points | — |
| 28 | Signals | Blocks: one train at a time | "Signals split the track into blocks. Only one train may be in a block. The next train waits." | SIG-28. | Agreed | Signalling | — |
| 29 | Signals | Semaphore signals | "Arm flat means stop. Arm raised means go. On real railways, a broken wire drops the arm to stop." | SIG-29. Corner chip "Arm style: undecided". Pictures R03 (STOP), R04 (CLEAR), inset P13. | Agreed | Signalling; Signal boxes | R03, R04, P13 |
| 30 | Signals | The signal box | "A signaller pulls levers. Rods and wires carry the movement out to the signals." | SIG-30. | Agreed | Signal boxes | P14, P15 |
| 31 | Signals | How it works together | "The signaller watches the blocks, sets the signals and keeps trains apart." | SIG-31. | Agreed | Signalling; Signal boxes; Mechanical signal-box linkage visuals | — |
| 32 | Signals | Early limits | "Early signals have limits: short blocks, a speed cap and a limited number per box. Numbers are provisional." | Four tiles (2.8 x 2.2 in), each with an inline Provisional chip: "Block length: about 400 to 500 m"; "Speed cap: about 60 km/h"; "Signals per box: 6 to 8 (station box), 12 to 16 (dedicated box)"; "Box reach: about 1 to 1.5 km of track". Under the tiles: ruler strip with a signal every 450 m (small copies of the SIG-28 post). Footer: "Block lengths and speed caps: undecided (OQ03)." | Provisional | Signalling; Signal boxes; OQ03 | — |
| 33 | Signals | No wiring for you | "Boxes take control of connected signals automatically. Rods and wires are drawn for you, as a visual layer." | Left: P16 (5.2 x 3.5 in). Right: three numbered steps: 1 "Place a signal on connected track"; 2 "A box with room takes control"; 3 "Rods and wires draw themselves and update". Under them: "The box screen lists its signals, their state, capacity and reach." Corner chip: "Rod or wire look: undecided (OQ04)". | Agreed | Signal boxes; Mechanical signal-box linkage visuals; OQ04 | P16 |
| 34 | Signals | Later signals and manual control | "Better signals come later. Drivers can also set points from a simple track diagram." | Left: timeline of three nodes: "Start: semaphore blocks" (Agreed); "Later: better semaphore or interlocking" (Proposed chip); "Mature: electronic signals like vanilla" (Proposed chip). Right: dark rounded panel (4.4 x 3.6 in) with a track diagram of circle nodes and lines, the active route bright orange, alternatives grey; three mode pills across the top "AUTO", "YARD", "MAINLINE". Under the panel: "Pick a destination and let the game set points: Proposed." | Agreed | Manual Railway Operations Diagram; Signalling; Progression | — |
| 35 | Later | Upgrading to the monorail | "Upgrade steam track in place. The route stays. Steam trains cannot use the converted part." | SPEC-H. | Agreed | Mk1 to monorail conversion | — |
| 36 | Later | After launch | "After launch, optional packs could add locomotives, regional looks and deeper driving. The core game stays complete." | Stack of blocks: solid orange base "Core 1.0: a complete game" (Agreed chip); above it four dashed blocks with Proposed chips: "Regional packs", "More locomotives", "Late-steam infrastructure", "Advanced manual driving (optional)". P19 at right (3.8 x 2.5 in), credit line "Real British locomotives like this could appear." Footer: "Which locomotives: undecided (OQ20)." | Proposed | Post-release enthusiast expansion programme; OQ20 | P19 |
| 37 | Extras | Regions and running numbers | "The world picks a regional style. Each engine has a hidden permanent ID and a number you can change." | Left: three pills "British", "North American", "Continental European" with the note "Examples only. Launch regions undecided (OQ06)." Right: nameplate card, large "No. 1234" labelled "Visible number: you can change it", small "Fleet ID: hidden, never changes". Footer: "Changing region restyles existing Core stock. How values migrate: undecided." | Agreed | Regional variants; Locomotive identity and running numbers; OQ06 | — |
| 38 | Extras | Your railway guide | "A friendly railway guide teaches with short animated lessons. Lessons are optional and can be replayed." | White rounded table top (miniature scene) with an oval of track, a tiny train, a semaphore and a signal box from shapes; a speech bubble "Short caption here"; four control icons: pause, replay, back, next. Inline Proposed chip: "A playful takeover when you first unlock rail". | Agreed | Railway Assistant & Animated Tutorial System | — |
| 39 | Status | Where we are | "A test engine runs on the game's real rails. Next come the other railway pieces. Singleplayer first. Multiplayer after release." | Horizontal roadmap line with eight circles: "Engine", "Rolling stock", "Track", "Stations", "Signals", "Unlocks", "Tutorials", "Release 1.0: singleplayer", then a dashed "Later: multiplayer". Engine and Track filled orange with the label "Under way"; the rest grey, "Planned". R01 thumbnail above Engine and R02 above Track (2.0 x 1.3 in each). Inline Provisional chip: "Plans can change." No technical test detail. | Provisional | Release scope and implementation order | R01, R02 |
| 40 | Status | Still undecided | "These questions are open. Nothing here has been chosen yet." | 4 x 2 grid of cards (2.9 x 1.6 in), each with an outline Undecided chip: "Exact unlock tiers (OQ01)"; "Longest track piece (OQ02)"; "Block lengths and speed caps (OQ03)"; "How boxes measure their reach (OQ04)"; "Is Medium the fastest? (OQ05)"; "Which regions at launch? (OQ06)"; "Which extra locomotives? (OQ20)"; "Pricing and release of packs (OQ26)". | Undecided | Open questions | — |
| 41 | Credits | Image credits (1 of 2) | "Photographs come from Wikimedia Commons under Creative Commons licences." | Table (11 pt): Slot, Slide, Author, Licence, Source link (hyperlinked). Rows P01 to P12 from `ASSET_MANIFEST.md`. Note under the table: "CC BY-SA photos are shown unmodified except for resizing." | — | — | P01–P12 |
| 42 | Credits | Image credits (2 of 2) | "Mod renders belong to the project. They show early test models." | Table (11 pt) continuing with P13 to P19, then R01 to R05 with the credit "Early Locomotion project (test model, not final art)". Same note and hyperlinks. | — | — | P13–P19, R01–R05 |

## Status counts and checks
- Agreed 23, Proposed 2, Provisional 4, Undecided 1, Background 8, no chip 4 (slides 1, 2, 41, 42). Slide 17, 19–21, 23, 24, 29, 33, 34 and 36 also carry inline Proposed, Provisional or Undecided chips.
- Every Proposed item on the deck has a visible Proposed chip: the speed-minimum rule (17), Small's weakness (19), Medium as fastest (20), Large's slow acceleration (21), one-vehicle model and tender types (24), the service-point set (27), later signals (34), destination routing (34), the upgrade hologram and warning, mixed networks and interchange (35, SPEC-H), post-launch packs (36), the takeover intro (38).
- Superseded ideas excluded: identical regional stats, shared collision box or wheel layout, steam on upgraded monorail, original half-length track limit, 50 m and 100 m track values.
- Slide 19 note (Jinty photo) and slide 29 wording ("On real railways") are deliberate accuracy fixes. Slide 39 deliberately leaves out the test-engine technical detail.
