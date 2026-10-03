<!--

Canonical editable design master for Satisfactory - Early Locomotion.

Reconstructed from Early Locomotion Design Reference.docx on 14 September 2026.

Keep this file and the Word reference synchronized when approved design decisions change.

-->



# Early Locomotion Design Reference

Version 0.1 | 14 September 2026

Early Locomotion introduces affordable steam railways before Satisfactory's electric trains. Players gain early long distance bulk transport, then solve the operating demands of steam through locomotive choice, signalling, coal and water supply, servicing infrastructure and route planning. This reference records the project direction and keeps unresolved choices visible for future design work.

## Core concept

The mod is called Satisfactory Early Locomotion. Its core railway uses conventional two rail track, steam locomotives and period inspired infrastructure. A broad selection of locomotive and wagon variants is part of the long term ambition.

Steam must have a distinct operating identity rather than duplicate electric trains at an earlier unlock. Cheap construction and cheap rolling stock make early railway expansion attractive; lower speed, signalling constraints, finite supplies, large stations and servicing time constrain performance. Players should be able to engineer solutions to these limitations.

Status convention: Agreed identifies explicit user choices or earlier suggestions covered by the user's statement that unchallenged points were accepted. Proposed identifies subsequent assistant elaborations not expressly confirmed. Playtest target identifies illustrative values, even when their underlying principle is agreed. Superseded identifies an earlier idea replaced by a later correction. No numerical targets in this reference are final unless explicitly stated otherwise.

## Release scope and implementation order

Agreed: Core 1.0 / the first public release prioritises a complete, robust singleplayer experience. Multiplayer support is deferred to a post-release update and is not a Core release requirement or blocker. Listen-server, dedicated-server, client replication and multiplayer-specific UI/presentation validation are deferred.

Multiplayer validation requires additional accounts/machines and substantial replication, server and cross-client testing overhead. Singleplayer must work properly before significant multiplayer implementation/validation work.

Agreed implementation discipline: where reasonably cheap, maintain server-authoritative ownership of mutable gameplay state, use replication-friendly structures and avoid knowingly making future multiplayer unnecessarily difficult. Unverified multiplayer behaviour is labelled deferred; it must not block singleplayer development. This does not verify any networking mechanism.

Agreed: singleplayer persistence and save/load correctness remain Core requirements. Multiplayer replication and multiplayer save/session semantics are separate, deferred post-release questions; their technical answers remain Open Question.

Agreed development priority (grouping may adapt to verified technical dependencies; this order does not select final architecture):

1. Singleplayer locomotive architecture assessment and selection after Manager review.

2. Production steam readiness and traction.

3. Rolling stock.

4. Track.

5. Stations and servicing.

6. Signalling.

7. Progression recipes and unlocks.

8. UI presentation and tutorials as applicable.

9. Singleplayer save/load robustness.

10. Balance packaging and singleplayer release QA.

11. Core 1.0 singleplayer release.

12. Post-release multiplayer implementation and validation.

Multiplayer release timing is decided; replication mechanisms, client prediction, dedicated-server behaviour and exact multiplayer save/session semantics remain unresolved. OQ04/OQ06/OQ14/OQ27/OQ28 retain their multiplayer technical questions for post-release work; their singleplayer persistence/performance requirements remain active.

## Progression

Agreed direction: introduce the railway progressively and preserve electric rail's superior role in a mature factory. A simple first route should work without demanding extensive signalling expertise. More vehicles, junctions and throughput should create the need for more infrastructure.

The milestone outline remains a provisional implementation of that direction:

- Tier 3 Early Steam Railways: small locomotive, basic wagon, steam station, semaphore signal and basic signal box. The suggested prerequisites are Coal Power and Basic Steel Production.

- Later Tier 3 or early Tier 4 Railway Expansion: medium locomotive, more wagon types and improved signal box.

- Tier 4 or Tier 5 Heavy Steam Engineering: large locomotive, heavy freight wagons, auxiliary tenders and improved semaphore or interlocking technology.

- Tier 6 Monorail Train Technology: transition to the vanilla electric railway as the premier high capacity transport system.

The exact unlock for independent service points, prerequisites, recipes and milestone costs is open. The initial design discussion also placed water extraction availability at the heart of the Tier 3 rationale; actual game and mod API requirements need checking during implementation.

## Track design

Agreed: early rails use Iron Plates and Iron Rods. They look like conventional railway track, with two thin steel rails held together by transverse beams or sleepers. Both locomotives and wagons are cheaper than their vanilla equivalents; exact recipes are not yet set.

The original maximum placement length of half the vanilla rail length was superseded. The revised preference is for the cheaper track to allow longer individual placements than later railway, making infrastructure easier to build. The constraint should come from trains and their operation rather than repetitive placement clicks.

A 150 m maximum was proposed as an experiment, subject to spline feasibility. It is not an agreed specification. The earlier 50 m proposal and 100 m comparison remain historical discussion values only.

Agreed principle: track has a permitted speed, separate from signalling restrictions and locomotive capability. Proposed expression for automated operation: permitted speed equals the minimum of track limit, signalling limit and locomotive limit. Gradients, acceleration, braking and loading may reduce achieved speed further. Manual operation and enforcement still need a precise rule.

## Signalling

Agreed: semaphores divide the railway into blocks with a maximum permitted block length. Additional signals are required along longer lines. Early signalling also imposes a maximum operating speed. Signals must belong to a signal box with limited control capacity.

Start with conventional block signalling. Complex junctions should function less efficiently than a mature electronic network, preserving the value of later upgrades. An equivalent to vanilla path signalling should arrive late rather than in the starter package. A simple one train line between two stations should remain approachable.

Initial playtest targets from the accepted discussion are a 400 to 500 m maximum semaphore block and approximately 60 km/h automated speed. Proposed improved semaphore or interlocking examples were 90 km/h and an 800 m maximum block, followed by electronic signalling at vanilla capability. These values require route and braking tests.

The earlier manual driving example allowed a mechanically capable engine to exceed the automation cap on a private unsignalled line. This is a design example, not a completed safety or enforcement specification. Behaviour for invalid blocks, uncontrolled signals, failed control and conflicting routes remains open.

## Signal boxes

Agreed: each steam station includes a signal box. Dedicated boxes extend control as the network grows, so a new player does not need extra standalone control buildings merely to start a basic route.

Control should be assigned automatically through connected railway territory rather than require individual cables to every signal. The box interface should show controlled signals, their current states, capacity usage and controlled distance. The visual direction is a substantial period building with windows, visible levers and rod or cable conduits; animated lever banks were suggested.

Playtest targets: 6 to 8 signals per station box, 12 to 16 per dedicated box, and approximately 1 to 1.5 km of connected railway territory. A 1,200 m display example illustrated the interface rather than adding another fixed limit.

Open implementation details include how distance is measured across junctions, territory overlap, assignment priority, reassignment after track edits and the relationship between signal count and distance limits.

### Mechanical signal-box linkage visuals — Agreed

Agreed: when a semaphore becomes assigned to or controlled by a signal box, automatically generated mechanical-looking line-side rods/wires/linkages represent that relationship. Where technically practical, they originate from or visibly connect to the controlling box area, follow the railway formation believably, and head toward controlled equipment. They regenerate/update when assignments change. This is primarily a presentation/readability layer; it does not replace automatic territory/control assignment.

Agreed: players do not manually place, route or wire signalling equipment. There is no manual wiring minigame. Full physical simulation of mechanical rod/cable travel over hundreds of metres is excluded. When controlled equipment changes state, linkage may twitch/jolt/vibrate slightly and appropriate mechanical click/clack/tension audio may play. The semaphore arm, signal-box lever and relevant machine supply the primary readable movement; line-side motion remains secondary environmental detail.

The design principle is perceptual plausibility, visual communication and mechanical atmosphere, not museum-grade simulation. This builds on mechanical semaphores, limited box capacity/territory, connected-territory assignment and the rod/cable conduit visual language.

Open Question / technical: rod versus wire appearance, spline/path generation, junction branching, continuity over long runs, overlapping territories, linkage to points/switch equipment, regeneration after track edits or reassignment, clutter, LOD/culling/performance and multiplayer presentation remain unresolved under OQ04. TECHNICAL VERIFICATION NEEDED; no implementation architecture or API is established.

## Locomotives

Agreed: Small, Medium and Large are the three primary Core gameplay roles. Every supported Core regional style ultimately provides one Small, one Medium and one Large locomotive; exact supported launch regions remain open. Each locomotive may have individual statistics. Core simplicity comes from a small roster, broad roles and accessible UX, not identical hidden physics. They should retain useful roles rather than form a ladder in which every larger engine invalidates the last. Purchase cost, traction, acceleration, speed, supply capacity, consumption and footprint must be considered together.

Small British reference: LMS Fowler Dock Tank. It is a tank locomotive with onboard coal and water and no normal tender. It is the weakest class, suited to short industrial trains and local branches. Low cost and economical operation should keep it useful later. An auxiliary tender is possible but adds a significant burden to its limited hauling ability.

Medium British reference: Merchant Navy Class. It includes a normal tender with substantially increased coal and water capacity, but also consumes more. This makes an auxiliary tender a more practical option. The later proposed role is the fastest steam class, serving lighter long distance or mixed freight with good rather than maximum traction.

Large British reference: BR Standard Class 9F. It is the most powerful of the selected British gameplay examples and includes a normal tender. It suits heavy freight, with high coal and water demand. An auxiliary tender may be appropriate on especially long routes. The later proposed role prioritises traction over the Medium class's top speed.

Earlier playtest suggestions were Small at 50 to 55 km/h with 1 to 3 wagons, Medium at 70 to 75 km/h with 3 to 6, and Large at 85 to 90 km/h with 6 to 10 or more. The later fastest Medium proposal conflicts with the original ascending speed ladder; do not implement both. Wagon counts are role illustrations, not hard consist caps.

Proposed operating character: the Small should start a few loaded wagons confidently but struggle with long heavy trains and hills. The Medium offers speed and range at higher consumption. The Large offers heavy haul capability with greater servicing demand and slower acceleration. Actual curves and relative values remain to be chosen.

## Locomotive identity and running numbers — Core feature

### Normal locomotives and permanent Fleet Identity — Agreed

Visible running numbers are a Core feature for both Core and expansion normal locomotives. Normal locomotives represent class members, receive generated historically plausible numbers and normally have no individual names. A number is assigned after successful placement; the build hologram does not need a permanent final number. The lifecycle hook/event remains TECHNICAL VERIFICATION NEEDED.

Every normal locomotive receives a permanent hidden Fleet Identity, distinct from its visible running number. It survives repainting, livery changes, regional transformations and renumbering. Dismantling/deletion destroys that identity; a new placement receives a new identity. Exact persistence/storage remains OQ28. The word registry/database does not require SQL or an external database.

### Regional number mappings — Agreed

One Fleet Identity may store separate visible-number mappings for its regional identities. British → North American → British restores the previous British number rather than generating a fresh one each round trip. Manual renumbering within a region updates that region's stored mapping: a player changing 47298 to 47111 returns to Britain with 47111. These numbers illustrate persistence, not verified class-number datasets.

A genuine Core regional transformation uses the destination region's stored/generated number and retains Fleet Identity and previous mappings. If an expansion locomotive cannot transform because no valid corresponding owned destination locomotive is available, it retains its existing regional identity, presentation and number; no new destination number is allocated. Livery changes alone never assign a new number. Explicit numbering-mode changes, region/class transformations and manual renumbering are number-change events; their technical implementation remains open.

### World numbering modes — Agreed

Core provides a world-level choice between **Standardised** and **Historical Operator** numbering. Standardised uses a consistent later/common scheme appropriate to that region; BR-style standardisation is a likely British reference baseline, not an approved dataset. Historical Operator uses researched operator/class-specific rules; GWR, LMS, LNER, Southern and BR are British examples, not complete data. The setting affects eligible locomotives across the world, rather than giving each normal engine an independent regime by default. The railway assistant should explain the choice when introduced; exact dialogue remains future writing work.

Changing mode alters only system-controlled/class-specific structure as required and preserves player-selected digits wherever valid. If a destination scheme cannot support the prior structure, adjust/remove incompatible scheme-controlled structure while preserving user-controlled content where possible. A controlled portion need not literally be a prefix. The system must protect class/scheme structure. Exact conversions and datasets remain OQ29.

### Unique allocation, release and overflow — Agreed

Normal numbers must be historically plausible, not one-to-one recreations of real individual machines. Generation follows researched class blocks, operator ranges, controlled portions, formats and meaningful ordering rules. Produce a valid candidate, check the active registry, reject/retry a reserved candidate and reserve a valid number. Two active normal locomotives cannot share a visible number in the relevant numbering pool/domain; whether that domain is class, operator, region or a broader scheme remains OQ29.

Dismantling/deletion releases the active reservation, allowing later reuse; the save does not permanently retire every allocated number. Exhausting a plausible historical pool must not block placement: use explicit, unique, visibly non-historical overflow allocation. X-00001 / X-00002 are examples only; the final prefix/format remains open.

Construction order, a save-local sequence or another internal ordering mechanism may inform schemes where historical age/order matters. This remains Open Question OQ29; Satisfactory playtime is not currently a historical calendar. Per-class research determines whether ordering matters.

### Manual renumbering — Agreed

Manual renumbering is a customisation feature enabled by a cheap AWESOME Shop-style unlock. Afterwards the player may edit permitted number portions; duplicates are rejected and scheme-controlled portions enforced. A manual value is retained in its regional mapping, including through return visits to that region. Later numbering-scheme changes preserve player-controlled digits where valid. Exact unlock cost, UI and technical integration remain OQ30.

### Number presentation and fleet search — Agreed direction

Display numbers in historically appropriate/canonical locations defined per locomotive class/model: possible surfaces include smokebox/front, tanks, cab, tender or bunker. Do not use a universal decal/socket transform or visually impossible placements. Painted/displayed numbering is the consistent simplification; reproducing physical brass/cast-plate manufacture is not a universal requirement. Exact locations/transforms belong in model asset data and require research.

The visible number forms part of player-facing identity; [Class] — No. [Running Number] is an example format only. Fleet management, train/timetable identity, map search and locomotive lists are possible uses; the hidden Fleet Identity remains internal. Players should be able to search/filter locomotives/trains by running number and class. Desired map behaviour keeps matches prominent and dulls non-matches; list/sidebar behaviour filters non-matching entries out. 92214 and 9F illustrate specific-engine versus class searches, not a fixed UI specification. Exact UI integration remains OQ30, TECHNICAL VERIFICATION NEEDED.

### Historical numbering research and cards

Agreed research discipline: each supported region requires its own verified conventions. Do not transpose British logic onto North American, German/Central European, French, Japanese or other future regions; these examples do not approve a launch-region list. Do not force every operator into one arithmetic rule. On selecting each production class, research and record historical ranges, operator conventions, nationalisation/renumbering treatment, blocks/controlled portions, construction-order significance, number placement, livery compatibility and exceptions in a structured per-locomotive definition suitable for later implementation. LNER/GWR and others may need bespoke logic. User screenshots are supporting references until independently verified, not sufficient hardcoding evidence.

Proposed: historical build cards may show a small secondary numbering note covering typical series, operator convention or class-range structure. Normal cards should not become full historical registries. Exact per-class data and algorithms remain OQ29.

## Regional variants

### Core regional presentation — Agreed

Regional presentation is a world/save-level setting, not a per-player visual preference: conflicting infrastructure styles would confuse multiplayer. Normal Core regional selection follows the world style; connected wagon presentation follows the controlling locomotive rule below. Cross-region mixing is not the normal Core design. Do not duplicate equivalent buildables merely to offer separate British/American/etc. versions of the same freight wagon.

Changing the selected Core region is intended to affect existing and future Core/basic infrastructure, Core locomotives, Core wagons and other presentation covered by the regional system, not just newly built objects. Runtime implementation is unverified. The earlier language-derived automatic default remains a possible default-selection idea, not a replacement for world/save-level selection.

Each supported Core style ultimately includes one Small, Medium and Large locomotive serving broad roles, with individual definitions/statistics. British, North American and Continental European styles have been discussed repeatedly, but none of these examples establishes the final launch list. Exact launch regions and references remain OQ06.

Agreed architectural constraint: standardise software/data contracts, not physical chassis. Wheel arrangements, wheelbases, proportions, tenders, rigs and animations may differ substantially. The shared collision box/wheel-layout proposal remains Superseded. Big Boy was an illustration of chassis differences, not the ordinary American Large selection. Santa Fe-type 2-10-2, Mikado 2-8-2, heavy 4-8-2 and 2-8-4 suggestions remain unselected examples.

### Consist regional presentation — Agreed

A connected consist derives wagon regional presentation from its controlling / lead locomotive's regional identity. A British controlling locomotive gives its wagons British presentation; a North American controlling locomotive gives North American presentation. An unconnected wagon follows the global world regional style. This supports coherent consists and regional rolling-stock mass/balance without duplicate regional wagon buildables.

Do not define the controlling / lead locomotive solely by front-most mesh order. Determination for multiple locomotives, double-heading, banking, coupling/uncoupling, timetable ownership and multiple-unit operation remains technically unverified. Live reskin updates, cargo/resource preservation, regional wagon mass/data migration, save/load, replication and performance remain OQ06/OQ27. TECHNICAL VERIFICATION NEEDED; this presentation rule does not select a runtime implementation.

### Regional performance — Agreed

Regional locomotive traditions may have meaningfully different absolute physical/performance characteristics. A North American locomotive may be heavier/more powerful while its corresponding rolling stock is also heavier; a British locomotive may have lower absolute power and lighter stock. These are illustrative principles, not selected classes or numeric specifications.

The objective is broadly comparable useful gameplay performance for representative regional trains while preserving regional mechanical character, not identical displayed numbers. Wagon tare/mass may be an internal balancing parameter. No numeric balance values or final curves are approved.

Superseded: the earlier requirement for identical locomotive class statistics between regional variants. It is retained here and in CHANGELOG history only, not as an active requirement.

Open Question OQ06: whether a world-region change dynamically changes existing locomotive/wagon mass or performance, whether values are fixed at construction, save/load migration, already-running trains, total train mass display, transient/exploit states, coherent migration and visual fallback. Do not choose a migration rule in implementation without approval. TECHNICAL VERIFICATION NEEDED.

## Fuel and water servicing

Agreed: steam locomotives need coal and water, loaded at a supplied station. Range should emerge from actual onboard capacities and consumption rather than an arbitrary distance countdown. Heavy loads, acceleration and climbing should increase demand; coasting should use less. A remaining range estimate was accepted as a useful interface direction.

Water should generally be the tighter operating limit. Earlier normal load playtest targets were Small water range 2 to 3 km and coal range 4 to 5 km; Medium water 4 to 5 km and coal about 7 km; Large water 6 to 7 km and coal about 10 km. These are route dependent targets, not guaranteed distances or tank sizes.

Compacted Coal should be more efficient than ordinary coal. The agreed recommendation is to derive this from the game's fuel energy system rather than hard code a separate arbitrary multiplier. Water savings from fuel choice were not established and should not be assumed.

Servicing adds dwell time. The initial example was 5 to 15 extra seconds depending on depletion. A later proposal refines this into actual water and coal transfer rates, with a small top up taking less time than an empty refill. Transfer rates, animation overhead, station buffers and departure conditions are still open.

## Stations

Agreed: the steam station is substantially larger than a vanilla station, incorporating a water tower, coal conveyor or loading equipment and its signal box. It has coal and water inputs; the accepted interface suggestion is one conveyor fuel input and one pipe water input.

The servicing sequence is a defining feature. The locomotive approaches slowly, settles into its dock and releases a long hiss. Coal is chuted into its storage while the water equipment swings around. The machinery moves and adjusts to find the actual water hatch and coal bunker or tender on the arriving model. Servicing occupies a visible period of time.

Proposed animation completion: retract both mechanisms before departure. Standard model specific targets can guide common machinery without forcing locomotive geometry to match. Suggested target names are WaterFillSocket, CoalFillSocket, SteamExhaustSocket, FrontCouplerSocket, RearCouplerSocket and CabInteractionSocket. These are interface proposals, not verified existing game APIs.

Large station size is part of balance: early technology is affordable in advanced materials but costs land and supporting infrastructure. Exact dimensions, clearances, approach speed, servicing reach, simultaneous coal and water transfer, freight platform behaviour and handling multiple locomotives need definition.

## Auxiliary tenders

Agreed distinction: a normal tender comes with the larger locomotive and belongs in its base capacity and balance. An auxiliary tender is an additional vehicle that trades train length and hauling capacity for more range. The Small tank engine has no normal tender.

Water only and combined coal and water auxiliary tenders were suggested. Their exact launch selection is open. They carry no freight, add mass and reduce the cargo that an otherwise comparable consist can haul. They should solve range limitations without becoming a free upgrade.

The Small may accept one, but the extra weight can worsen its main weakness. The Medium has enough capability to make the trade attractive on longer work. The Large can use one for especially long journeys.

Proposed entity model: treat locomotive plus normal tender as one game vehicle if feasible, while the auxiliary tender is a true separate wagon. Entity structure, refill order, resource sharing, placement rules and how station machinery reaches auxiliary storage remain technical questions.

## Service points

Agreed: separate trackside coal and water facilities enable journeys beyond a locomotive's ordinary range. Trains stop to replenish supplies, paying a time cost. A full cargo station should not be necessary for every service stop.

Proposed facility set: Water Tower for water, Coaling Stage for coal, combined Steam Service Point for both, and full Station for cargo operations plus both supplies and an integrated signal box. A combined service point's signal box is undecided. The exact number of separate buildables is open to avoid unnecessary menu clutter.

The later preferred timetable proposal makes service stops explicit, for example a water only stop with departure when full. Automatic opportunistic servicing was also mentioned but not selected. Scheduling, reservation, bypass behaviour, insufficient supply and starvation recovery need design.

Range can be solved by adding an auxiliary tender, inserting a water stop, building a combined service point or choosing a locomotive with greater capacity. Service sidings and higher flow water or coal machinery were suggested as later optimisation options.

## Mk1 to monorail conversion

Agreed user interaction: select the higher tier railway, point it at existing early track and replace it in place, in the familiar manner of upgrading conveyors or miners. Preserve route planning rather than require players to rebuild their entire network from scratch.

The latest physical constraint is decisive: conventional steam running gear and the vanilla beam hugging monorail system are different constructions. The latest design response therefore treats steam and monorail rolling stock as incompatible. The earlier proposal that upgraded monorail should still support steam is superseded. This incompatibility is the working conversion design following the user's correction.

Proposed conversion behaviour: retain the spline path and, where feasible, supports and junction geometry. Show an upgrade hologram and an explicit warning that steam rolling stock cannot use the converted section. Spline lengths, curvature, gradients, clearances and connection compatibility require feasibility checks before promising exact preservation.

Proposed station conversion uses aligned replacement rather than a literal visual morph of a sprawling steam complex into a compact vanilla station. Preserve name and timetable references where technically possible, and remove obsolete coal and water equipment. Signalling upgrades and replacement of mechanical control by electronic interlocking are related proposals, not yet specified systems.

Proposed long term network: retain conventional steam branches alongside a converted electric trunk route. Freight can move through an interchange between the networks. A dedicated Transfer Station building was suggested as a future possibility; it is not an agreed launch feature. Steam cannot move directly between the two track systems.

Open conversion safeguards include occupied track, stranded trains, mixed networks, junction boundaries, conversion costs and refunds, partial upgrades, undo or recovery, and the maximum lengths accepted by vanilla rail.

## Balance philosophy

Agreed: make early rail cheap and convenient to deploy, then balance it through meaningful operating demands. Do not use additional clicks as the main cost. Early steam should excel at long distance bulk movement while tractors retain flexibility and low route infrastructure requirements. Belts retain their role for permanent short and medium connections; electric rail should lead in mature speed, throughput, density and convenience.

Keep locomotive roles distinct. A Large engine pulling one wagon should be inefficient; a Small hauling a very long loaded train should struggle. Small industrial engines should remain useful after the heavier classes arrive.

Early wagons should be cheaper and lower capacity than vanilla freight cars. An accepted initial playtest range is 16 to 24 item stacks. The discussion used 20 stacks per steam wagon against 32 per vanilla wagon as an illustrative comparison. No exact cargo capacities, fluid capacities or wagon catalogue have been finalised.

Evaluate a route as a whole: purchase cost, cargo moved per trip, travel time, fuel and water logistics, time stopped, track occupancy, extra tender mass and station footprint. Numerical comparisons from the original conversation are historical design context, not a current validation of game data.

Every limitation should support a player choice: range can be extended with supplies or tenders; capacity with suitable locomotives and consists; traffic with signals and boxes; and mature throughput with monorail conversion. Frequent service stops trade time for reliability. Whether frequent top ups actually improve throughput depends on approach and animation overhead as well as transfer rates and must be tested.

## Development and asset direction

Agreed design constraint: Core and expansions share expressive locomotive gameplay/simulation with individual definitions; expansions must not delay current Core work. The class/inheritance decision remains unresolved. Proposed architecture: a shared SteamLocomotiveBase owns common fuel, water, traction, steam state, signalling and interface behaviour. Definitions hold performance values; model specific presentation supplies mesh, wheel configuration, rig, animation, steam emitters and audio. Wagon families share common behaviour with cargo, fluid and possible specialist variants.

The earlier workflow discussion suggested AI assisted coding with independent review, Blender for final locomotive geometry, generated props or concepts as starting points, material authoring for coherent wear and soot, and layered sound effects driven by operating state. These are workflow proposals rather than installed tools or development commitments.

Locomotive geometry, rods and wheel motion require deliberate modelling. Servicing targets must match each model. Keep complex state logic separate from presentation and verify any Satisfactory or mod loader API against the actual chosen development version. The archived tool and engine version recommendations must be rechecked before implementation.

## Railway Assistant & Animated Tutorial System

The 20 September 2026 addition is reconciled with the Manager-approved 1 October dispositions below. Concept approval does not establish API feasibility.

### Confirmed / Agreed

#### Railway assistant character and scope

Early Locomotion has its own scripted railway-focused assistant, distinct from ADA and voiced by the user/project creator. She is warm, bubbly, enthusiastic, expressive and competent as a teacher, strongly interested in railways, signalling, locomotives and engineering. Her warmer support-oriented presentation contrasts with ADA/FICSIT's colder corporate tone. She handles Early Locomotion narrative/voice presentation and supports integrated railway education.

She is not actual generative AI, a live railway-management/diagnostic system, a route calculator, a network inspector, an automatic signal placer or an automatic railway fixer. She does not diagnose or operate the player's live network. Tutorials teach principles and preserve player problem-solving.

#### Animated teaching and reference library

The assistant includes an always-accessible animated railway teaching/reference system. Lessons remain optional and replayable and become available progressively alongside relevant technology. The library remains accessible; individual lessons respect progression. Miniature demonstrations animate concepts, pause at important moments, highlight relevant objects/behaviour and use short explanatory captions. Avoid giant text walls.

Agreed presentation direction: a clean white miniature model-railway/showroom/IKEA-like table with miniature Early Locomotion trains, track, stations, semaphores, signal boxes and servicing structures. Create's Ponder system may inspire visual interaction, but its assets/presentation must not be copied literally. This is not an implementation dependency.

Agreed library UI direction: recognisably older FICSIT visual language, instructional, cleaner, older/prototype and less aggressively corporate. This visual direction does not establish historical lore. Desired controls where practical are pause, replay, previous step and next step; exact UI and playback/control implementation remain open under OQ15/OQ18.

#### Release audio requirement

Windows XP audio is not intended release content. Use an original legally distinct retro-computer startup jingle; no third-party sound rights are assumed.

### Proposed

#### First unlock introduction and apparent ADA takeover

On the first applicable Early Locomotion technology unlock, expected ADA-style presentation may begin, followed by interface glitches/interference, an apparent railway-assistant takeover, an original retro startup jingle and her introduction. The intended humour is surprising rather than sinister. Exact animation, sequence, dialogue, timing and trigger remain Proposed/Open; no ADA interception or independent recreation mechanism is selected.

#### Legacy FICSIT flavour

Older UI language, warmer support tone, obsolete/prototype styling, less productivity-obsessed wording and strange persistence in the modern system may imply an earlier FICSIT era. Do not canonise “FICSIT used to be good and was later corrupted.” Exact historical origin remains open.

#### Expanded teaching and character content

Specialised/common-mistakes lessons, advanced junction/passing-loop/signalling demonstrations, additional flavour dialogue/animations and milestone narration remain Proposed beyond the concept. A vertical subject/category list is one Proposed layout, not the final library UI.

### Open Questions

- **OQ15 — Character and presentation:** Exact assistant name, introductory dialogue, avatar/visual design, palette and final library/UI layout remain open.
- **OQ16 — Historical origin and lore:** Exact deeper lore/origin; whether history is explained or implied, and whether older-FICSIT styling represents lore or visual implication only.
- **OQ17 — Tutorial content and narration:** Exact subject/launch roster, unlock mapping and milestone voice-line structure.
- **OQ18 — Tutorial and assistant implementation:** Exact playback controls, first-unlock trigger, announcement UI, ADA-style illusion/interception versus independent recreation, animated demonstration scenes, lesson tracking and voice/audio integration. TECHNICAL VERIFICATION NEEDED against the actual environment; no API, hook, Blueprint or architecture is approved.

## Build menu UX

Proposed: Early Locomotion eventually has its own top-level build category rather than placing the entire system in vanilla Transport. Possible groups are Railway Infrastructure, Stations / Servicing, Signalling and Rolling Stock. Exact hierarchy/nesting remains OQ19. TECHNICAL VERIFICATION NEEDED for Satisfactory build-menu support; no API or implementation is established.

## Post-release enthusiast expansion programme

### Core boundary and shared foundation — Agreed

The expansion programme is a Proposed long-term post-Core direction. Agreed constraint: it must not delay Core, first playable implementation or Core 1.0. Core must be complete, polished and satisfying; do not deliberately weaken or leave Core locomotives incomplete to sell expansions. Core retains its identity as Satisfactory with a distinct early steam railway system. Expansion value would come from breadth, historical variety, specialisation, enthusiast depth, advanced operation and infrastructure.

Agreed: Core and expansion locomotives share one sufficiently expressive underlying gameplay/simulation foundation, with individual data-driven definitions. Expansions add definitions, nuanced characteristics and optional deeper driving interactions. Do not create an expansion-only physics engine where the common foundation can support both. Standardise software/data contracts, not physical locomotive chassis. This is a design constraint, not a choice of Unreal inheritance or implementation type.

### Regional packs and updates — Proposed

Separate regional enthusiast packs may add expanded fleets, region-specific advanced infrastructure presentation, enthusiast systems and historical/livery content. Approximately £10 GBP per pack is a Proposed planning target only; exact price is open. Pricing, storefront, entitlement, distribution and commercial permission are not technically or legally settled.

Proposed update model: launch with a smaller meaningful roster, then add locomotives/content through updates supplied to existing owners without charging per locomotive. Exact roster and release strategy remain open. Do not canonise early adopters paying more for incomplete content; early-access pricing remains open.

### Expanded locomotive catalogue — Agreed direction

Without expansions, Small / Medium / Large remains the simple primary Core selection. With a substantially expanded enthusiast roster, browsing should move to historical/operational role categories. Core locomotives remain available and are reclassified into that catalogue. Shunters, Mixed Traffic, Express Freight / Fast Freight and Heavy Freight are candidate names only. A category explains a locomotive family/role; its individual card explains that machine's strengths and duties. Exact category names remain open.

Satisfactory has no normal passenger economy. A gameplay Express category primarily means express/fast freight or high-speed logistics, not a passenger-service requirement. Passenger-oriented historical classes may appear for broader real-world use, enthusiast significance or cameo/prestige content. Historical descriptions must state their real purpose honestly even if gameplay adapts it.

Each expansion locomotive may meaningfully differ in tractive effort, speed, mass, acceleration, braking, coal/water capacity and consumption, gradient behaviour and hauling character. They are not cosmetic skins of Small/Medium/Large; same-category locomotives need not behave identically. No final values are approved. Real railway research informs relative character, role, identity and plausible differences; do not copy all engineering values literally into Satisfactory. The aim is historically knowledgeable gameplay, not exact engineering simulation.

Agreed: the eventual roster has a deliberate cap to avoid overwhelming players. Substantial variety is a Proposed aspiration; earlier examples of roughly four shunters, five–six mixed-traffic and up to ten each fast/heavy freight machines are not committed counts or requirements. Exact expansion names, roster, count and role categories remain OQ20.

### Historical cards and Golden Era scope

Agreed: expansion locomotive cards separate HISTORY / CHARACTER from EARLY LOCOMOTION GAMEPLAY. History gives a short researched introduction covering class, designer/builder/operator, introduction era/year, intended historical purpose and useful reputation/story. Gameplay states duties, strengths, weaknesses and practical role. Research class-specific history when developing rosters; no roster is approved here.

Proposed: regional fleets primarily draw from steam's mature/Golden Era period. British examples may include suitable GWR, LNER, LMS, SR, British Railways and other relevant operators. Operators inform history, livery and identity; they are not build-menu categories. Exact chronological boundaries remain OQ21.

### Late steam and advanced infrastructure

Agreed: vanilla electric monorail remains technically superior overall even with expansions. High-end steam may remain late-game viable in specialised roles through physical scale: large terminals, many tracks/trains, substantial signalling/servicing and large railway complexes. Electric remains compact, efficient, convenient and high-density; steam's scale/volume ambition does not make it objectively better.

Agreed: advanced late-game steam infrastructure is expansion-only and serves enthusiasts intentionally retaining steam after electric unlocks. Larger terminals, higher-capacity servicing, larger signal boxes/capacity/territories, improved interlocking, greater practical signal spacing and large-network systems remain Proposed/Open. Do not give steam vanilla electronic capability with semaphore visuals. Exact catalogue remains OQ22.

Proposed regional asset direction: Core provides BASIC regional infrastructure presentation; matching regional packs provide ADVANCED expansion presentation. Owned matching assets may supply the selected visual set; unowned regional assets must not be provided magically. Fallback for existing advanced infrastructure when a matching pack is unavailable remains OQ23.

### Expansion locomotive region switching — Agreed fallback

If no valid corresponding owned expansion locomotive is available in the newly selected world region, the existing expansion locomotive does not transform: it retains regional/national identity, presentation and running number. Core locomotives and other stock with valid regional replacements may still transform normally. “No nationality change → no new VISA” is design shorthand only, not required UI text. The high-level fallback is now resolved; valid correspondence, transformations when available, advanced-asset fallback and technical migration remain OQ23.

Agreed: regional expansion rosters need not have identical role counts or class-to-class symmetry. Do not force equal shunter, Mixed Traffic or Heavy Freight counts or artificial equivalents merely to enable switching. Each region should represent plausible/useful locomotives from its tradition; final rosters remain future research/design work (OQ20).

### Expansion progression

Agreed philosophy: ownership does not immediately grant advanced/endgame steam content. Expansions progress alongside Core: early/small expansion machines unlock around comparable Core stages; more capable machines and infrastructure unlock around Heavy Steam or later progression. Exact unlocks remain open.

Proposed implementation preference: integrate unlocks into existing Early Locomotion milestones where practical. If technically awkward, use parallel/additional clearly labelled expansion milestones. Exact milestone integration/API remains OQ20, TECHNICAL VERIFICATION NEEDED.

### Advanced manual driving — refined Agreed scope

Advanced manual steam driving remains expansion-only, optional/toggleable. Simple remains available, default and preselected. First relevant use presents Simple versus Advanced with notice that settings can change later; the assistant may explain it. Technical configuration/input APIs remain unverified.

Agreed: meaningful steam-engine operation without full professional locomotive simulation. Primary player-managed systems are coal/firebox management, regulator/throttle and reverser/cutoff; braking remains part of driving where required. Manual injectors, detailed boiler-water management, blower/damper simulation, dozens of cab valves and engineering-procedure simulation are not currently required features. The earlier broader exploratory loop is narrowed by this approval. Steam and Steel may later be researched as a conceptual interaction reference only; do not copy formulas without verification/design review.

Agreed: poor operation produces natural performance consequences rather than arbitrary punishment. Unsuitable regulator/reverser use reduces effective hauling; excessive power/cutoff combinations may cause wheel slip; insufficient steam pressure reduces available power; weak fire/steam management reduces performance. Boiler explosions, permanent boiler damage, locomotive destruction and catastrophic punishment are not required. Exact formulas, pressure/reverser behaviour and wheel-slip model remain OQ24.

Agreed: Simple behaves like a competent automatic crew / automatic transmission: the player provides basic movement intent and the game handles detailed steam operation. Advanced is manual operation, allowing a skilled player to prepare for gradients, hold power, trade efficiency for short-term output and manage immediate needs. Simple must remain competent and useful. Advanced may offer a modest skill ceiling and potentially somewhat better useful performance; the exact amount/shape of that advantage remains OQ24. Do not intentionally cripple Simple.

### Liveries and cameo content

Agreed expansion principle: historical liveries are prominent, with an appropriate/default historical presentation where feasible and possible additional historical liveries. FICSIT/custom corporate styles remain possible. Historical liveries must not become separate real-money microtransactions within an owned expansion proposal. Customizer/AWESOME Shop integration is Proposed and technically unverified; exact livery integration and relevant licensing remain OQ25.

Proposed flavour: occasional, first-time/context-sensitive, non-spammy assistant reactions may express railway-nerd pleasure at historical liveries and playful disappointment at corporate/FICSIT styling. Exact dialogue remains future writing work.

### VIP / Prestige locomotive framework — Agreed

VIP / Prestige locomotives are extremely expensive enthusiast/show-off rewards for display, collection, screenshots and bragging rights, analogous in spirit to Golden Nut / Golden FICSIT Cup prestige rewards. They are not superior logistics upgrades. Exact prices remain OQ25.

Expansion VIPs represent specific famous historical machines with fixed historical identity, name and number, no procedural fleet number, one-per-world/save where appropriate, and extremely expensive prestige/AWESOME-style unlocks. Practical freight utility is deliberately poor; high speed must not make them logistics-meta. Mallard and Flying Scotsman remain examples only, not an approved roster. Name/trademark/livery licensing review remains required.

Core prestige normally selects a special historical individual from an existing Core locomotive class rather than an unrelated celebrity engine, keeping it understandable to non-enthusiasts. It has fixed identity/name/number, special livery/presentation, prestige treatment and one-per-world where appropriate. If 9F remains British Large/Core, Evening Star is an example only; it is not approved here.

Normal locomotives are generated, normally unnamed class members; VIPs are fixed historical individuals. VIPs ignore procedural numbering and retain fixed name, number and identity through rerolls, global numbering-mode changes, manual renumbering and procedural regional replacement.

Proposed: suitable prestige/historical passenger stock may accompany expansion VIPs for appearance, display and showpiece consists. Exact coach roster remains OQ25; this adds no normal passenger economy, and full passenger simulation is outside scope unless separately approved.

Proposed flavour: the assistant may recognise VIPs and react enthusiastically to purchase or first placement, briefly losing professional composure. Avoid repeated lengthy dialogue on every placement. Exact dialogue remains future writing work.

### Multiplayer and compatibility

Agreed desired outcome: friends should ideally not need a separate enthusiast-content purchase simply to join/play with an owner, if technically, legally and commercially viable. This is not verified server-side DLC. Client installation/asset requirements and commercial entitlement are distinct. Client assets, mod loading, server dependencies, entitlement, save compatibility and differing pack availability remain OQ27.

Agreed: regional packs depend on Core, should coexist and be mutually compatible. Multiple packs should not duplicate underlying mechanical systems. Share gameplay systems/data contracts where practical and vary content/presentation; different regional buildings do not justify separate gameplay implementations.

### Commercial delivery — Open Question

Exact pack pricing, early-access pricing, paid distribution/storefront and commercial/platform permission remain OQ26. Patreon, external purchases and manual installation are unapproved ideas, not implementation plans. Investigation must cover Coffee Stain and Satisfactory Modding policies, SML/SMR rules, redistribution, commercial permissions, platform terms, entitlement, updates, dependencies and licensing. TECHNICAL VERIFICATION NEEDED, plus legal/commercial verification; no promise of sale or distribution mechanism is established.

## Open questions

- OQ01 Progression: approve exact milestones, prerequisites and service point unlocks.

- OQ02 Track: choose maximum segment length, speed cap, recipe quantities and geometry rules after spline tests.

- OQ03 Signalling: choose block lengths, speed caps, path or interlocking progression, and invalid or uncontrolled block behaviour.

- OQ04 Signal boxes: settle capacity, territory measurement, overlap and reassignment; generated linkage appearance, routing/branching, continuity, equipment coverage including points, regeneration, clutter, LOD/performance and multiplayer presentation. Multiplayer-specific validation is deferred post-release; applicable singleplayer requirements remain Core.

- OQ05 Locomotives: confirm whether Medium is the fastest steam class, then define traction, acceleration, mass, capacities and consumption curves.

- OQ06 Regions: select exact supported Core launch regions/references and world/save selection; verify existing/future switching, controlling/parent locomotive determination for multi-locomotive consists, live wagon reskin updates, cargo/resource preservation, regional wagon mass/data migration, dynamic versus construction-fixed performance, already-running trains, total mass display, save/load, replication, performance and transient/exploit safeguards. The controlling-locomotive presentation rule is Agreed; its implementation is not. Identical statistics are Superseded; balance values remain unset. Multiplayer-specific validation is deferred post-release; applicable singleplayer requirements remain Core.

- OQ07 Wagons: establish item and fluid roster, capacities, dimensions, costs and platform compatibility.

- OQ08 Supplies: define fuel support, depleted supply behaviour, range estimation, station buffers and transfer rates.

- OQ09 Stations: specify dimensions, animations, service reach, multiple locomotive servicing and how freight loading overlaps with replenishment.

- OQ10 Tenders: select types, entity model, coupling rules, refill order and resource distribution.

- OQ11 Service points: choose separate facilities, timetable controls, departure conditions and signal box requirements.

- OQ12 Conversion: validate geometry preservation and replacement, protect occupied lines, determine costs and retain station or timetable references where possible.

- OQ13 Scope: determine Core/post-launch non-expansion scope for interchange buildings and specialist content. Advanced late-game steam infrastructure belongs to expansions; its exact catalogue remains OQ22.

- OQ14 Implementation: verify toolchain, singleplayer architecture, singleplayer persistence/save-load correctness, performance and build/release validation. Core 1.0 is singleplayer; multiplayer implementation/validation is post-release. Replication mechanisms, listen/dedicated-server behaviour, client prediction and multiplayer save/session semantics remain unresolved, not Core blockers.

- OQ15–OQ18 Railway assistant and animated tutorials: see the dedicated section above for character/presentation, lore, tutorial content/narration, and technically unverified implementation questions.

- OQ19 Build menu: verify top-level category support and select exact hierarchy/nesting.

- OQ20 Expansion catalogue and progression: exact pack names, release/update roster/strategy, deliberate total cap, role-category names and unlock stages; verify existing-milestone integration API versus Proposed parallel/additional labelled milestones. Symmetric regional role counts/equivalents are not required. No suggested roster counts are commitments.

- OQ21 Golden Era: exact chronological start/end and regional/operator coverage.

- OQ22 Advanced infrastructure: exact expansion-only catalogue, capabilities, capacity/territory/interlocking limits and balancing against electric superiority.

- OQ23 Expansion regional migration: valid owned correspondence and transformation handling when available, missing/multiple-pack technical migration and advanced regional-asset fallback. High-level locomotive fallback is resolved: no valid corresponding owned destination locomotive means retain current identity/presentation/number. No technical mapping, storage or migration mechanism is chosen.

- OQ24 Advanced driving: exact firebox/pressure/regulator/reverser formulas, wheel-slip model, natural performance consequences and amount/shape of a modest potential Advanced advantage. Simple is competent automatic operation; injectors, detailed boiler-water/blower/damper/cab-valve simulation and catastrophic damage are not current required features. Configuration/input implementation needs verification.

- OQ25 Liveries and VIP/prestige content: exact livery integration, Customizer/AWESOME support, Core/expansion VIP rosters and prices, one-per-world applicability, prestige passenger coach roster, dialogue and name/trademark/livery licensing. Named examples are not approved selections; the Agreed prestige framework is not a logistics upgrade or passenger economy.

- OQ26 Commercial programme: exact regional pack price, early-access pricing, paid distribution/storefront, permissions/policies, redistribution, updates/dependencies and licensing. No delivery plan approved.

- OQ27 Multiplayer expansions: client assets/install/mod loading, server dependencies, entitlement, save compatibility, differing pack availability and feasibility of joining without extra purchase; replication/save/performance implications of consist regional updates. No entitlement or runtime mechanism is verified. Multiplayer implementation/validation is deferred post-release; no technical answer or entitlement mechanism is selected, and singleplayer save/load remains a Core requirement.

- OQ28 Fleet Identity: verify placement lifecycle hooks, permanent identity persistence/storage, regional mapping save/load, dismantling/deletion lifecycle and replication. No SQL/external database requirement or API is chosen. Multiplayer-specific validation is deferred post-release; applicable singleplayer requirements remain Core.

- OQ29 Numbering rules/data: define collision pool/domain, independently verified per-class/operator/regional algorithms and datasets, construction-order relevance, scheme conversion, controlled/player-controlled portions, manual-value validity and overflow prefix/format. Do not treat playtime as a historical calendar or screenshots as verified data.

- OQ30 Numbering customisation/UI: exact cheap renumber-unlock price, AWESOME-style integration, editing/duplicate validation, player-facing number locations in UI and fleet search/filter integration. Map prominence/dulling and list filtering are Agreed desired behaviour; APIs and final UI remain unverified.

## Revision record

Version 0.1 created on 14 September 2026. Consolidates the initial concept, detailed balance discussion, user corrections on rail length and tenders, the regional chassis correction, animated servicing requirements and the final conventional rail versus monorail distinction.

20 September 2026: added the approved Railway Assistant & Animated Tutorial System, preserving the Confirmed / Agreed, Proposed, and Open Questions split; added OQ15–OQ18 without resolving existing questions.

1 October 2026: reconciled Manager-approved assistant/tutorial, generated linkage, world-region and regional-performance direction; identical regional statistics are Superseded. Added a clearly post-Core Proposed enthusiast programme, agreed scope/foundation/compatibility constraints, OQ19–OQ27 and revised OQ04/OQ06/OQ13/OQ15–OQ18. No implementation or remaining Open Question is resolved.

2 October 2026: applied Manager-approved numbering/Advanced Driving/VIP refinements. Resolved high-level expansion locomotive retention fallback; agreed controlling-locomotive wagon presentation and asymmetric regional rosters. Added Core identity/numbering/search family, refined Advanced scope/Simple relationship, expansion progression and Core/expansion prestige framework. Revised OQ06/OQ20/OQ23–OQ25/OQ27; added OQ28–OQ30. Technical mechanisms, exact values, roster, licensing and Proposed details remain open. No gameplay implementation is claimed.

Future revisions should update the relevant section, change its status where appropriate, record the reason and source in CHANGELOG.md, and resolve the corresponding open question. Preserve superseded decisions in the change history rather than leave conflicting instructions active.

2026-10-03: Manager/user-approved singleplayer-first Core 1.0 scope; multiplayer support and validation deferred post-release. Singleplayer save/load remains required. Multiplayer technical questions stay open; no production architecture selected.
