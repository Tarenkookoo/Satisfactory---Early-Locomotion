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

## Locomotives

Agreed: Small, Medium and Large are the three initial gameplay classes. They should retain useful roles rather than form a ladder in which every larger engine invalidates the last. Purchase cost, traction, acceleration, speed, supply capacity, consumption and footprint must be considered together.

Small British reference: LMS Fowler Dock Tank. It is a tank locomotive with onboard coal and water and no normal tender. It is the weakest class, suited to short industrial trains and local branches. Low cost and economical operation should keep it useful later. An auxiliary tender is possible but adds a significant burden to its limited hauling ability.

Medium British reference: Merchant Navy Class. It includes a normal tender with substantially increased coal and water capacity, but also consumes more. This makes an auxiliary tender a more practical option. The later proposed role is the fastest steam class, serving lighter long distance or mixed freight with good rather than maximum traction.

Large British reference: BR Standard Class 9F. It is the most powerful of the selected British gameplay examples and includes a normal tender. It suits heavy freight, with high coal and water demand. An auxiliary tender may be appropriate on especially long routes. The later proposed role prioritises traction over the Medium class's top speed.

Earlier playtest suggestions were Small at 50 to 55 km/h with 1 to 3 wagons, Medium at 70 to 75 km/h with 3 to 6, and Large at 85 to 90 km/h with 6 to 10 or more. The later fastest Medium proposal conflicts with the original ascending speed ladder; do not implement both. Wagon counts are role illustrations, not hard consist caps.

Proposed operating character: the Small should start a few loaded wagons confidently but struggle with long heavy trains and hills. The Medium offers speed and range at higher consumption. The Large offers heavy haul capability with greater servicing demand and slower acceleration. Actual curves and relative values remain to be chosen.

## Regional variants

Agreed ambition: regional models apply to locomotives and wagons. Automatic selection may use the game's language as a default, but players should be able to override it through a Regional Rolling Stock Style option. Language alone does not identify a country or railway preference.

Suggested style entries include Automatic, British, North American, German or Central European, French and Japanese. This is an example menu, not a committed launch roster. The user is willing to invest in research and modelling; release scope remains open.

Agreed correction: do not force all regional locomotives onto one physical chassis. Different wheel arrangements, wheelbases, proportions and motion require their own models, rigs and animations. Standardise software behaviour and interfaces instead. The earlier shared collision box and wheel layout proposal must not be treated as a settled requirement.

The user used Big Boy as an extreme illustration of chassis differences, then chose a smaller but still impressive American steam freighter for the ordinary Large role. Big Boy is not the baseline selection. The conversation corrected its wheel arrangement to 4 8 8 4; that correction is background context rather than a gameplay specification.

Later candidate suggestions included a Santa Fe type 2 10 2, a large Mikado 2 8 2, or a heavy 4 8 2 or 2 8 4. No American class has been selected. Regional equivalents should be comparable in role and visual stature, while remaining recognisably distinct.

Open balance decision: the accepted initial recommendation used identical statistics within each regional gameplay class. A later assistant proposal allowed different statistics within an equivalent overall performance and cost budget. This later proposal was not confirmed. Use identical class statistics as the earlier baseline pending an explicit decision; do not quietly introduce regional advantages.

Specialist or articulated locomotives outside the three class baseline were suggested for distant future expansion. They are not a core launch commitment.

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

Proposed architecture: a shared SteamLocomotiveBase owns common fuel, water, traction, steam state, signalling and interface behaviour. Definitions hold performance values; model specific presentation supplies mesh, wheel configuration, rig, animation, steam emitters and audio. Wagon families share common behaviour with cargo, fluid and possible specialist variants.

The earlier workflow discussion suggested AI assisted coding with independent review, Blender for final locomotive geometry, generated props or concepts as starting points, material authoring for coherent wear and soot, and layered sound effects driven by operating state. These are workflow proposals rather than installed tools or development commitments.

Locomotive geometry, rods and wheel motion require deliberate modelling. Servicing targets must match each model. Keep complex state logic separate from presentation and verify any Satisfactory or mod loader API against the actual chosen development version. The archived tool and engine version recommendations must be rechecked before implementation.

## Open questions

- OQ01 Progression: approve exact milestones, prerequisites and service point unlocks.

- OQ02 Track: choose maximum segment length, speed cap, recipe quantities and geometry rules after spline tests.

- OQ03 Signalling: choose block lengths, speed caps, path or interlocking progression, and invalid or uncontrolled block behaviour.

- OQ04 Signal boxes: settle capacity, territory measurement, overlap and reassignment rules.

- OQ05 Locomotives: confirm whether Medium is the fastest steam class, then define traction, acceleration, mass, capacities and consumption curves.

- OQ06 Regions: select launch packs, American references, fallback style and identical statistics versus regional tradeoffs; define multiplayer selection and save behaviour.

- OQ07 Wagons: establish item and fluid roster, capacities, dimensions, costs and platform compatibility.

- OQ08 Supplies: define fuel support, depleted supply behaviour, range estimation, station buffers and transfer rates.

- OQ09 Stations: specify dimensions, animations, service reach, multiple locomotive servicing and how freight loading overlaps with replenishment.

- OQ10 Tenders: select types, entity model, coupling rules, refill order and resource distribution.

- OQ11 Service points: choose separate facilities, timetable controls, departure conditions and signal box requirements.

- OQ12 Conversion: validate geometry preservation and replacement, protect occupied lines, determine costs and retain station or timetable references where possible.

- OQ13 Scope: decide whether interchange buildings, specialist engines and faster servicing equipment belong in later releases.

- OQ14 Implementation: choose and verify game, mod loader and editor versions, then establish multiplayer, save and load, performance and build validation requirements.

## Revision record

Version 0.1 created on 14 September 2026. Consolidates the initial concept, detailed balance discussion, user corrections on rail length and tenders, the regional chassis correction, animated servicing requirements and the final conventional rail versus monorail distinction.

Future revisions should update the relevant section, change its status where appropriate, record the reason and source in CHANGELOG.md, and resolve the corresponding open question. Preserve superseded decisions in the change history rather than leave conflicting instructions active.
