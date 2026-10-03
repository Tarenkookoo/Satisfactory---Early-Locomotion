# Satisfactory - Early Locomotion
## Project Index

**Last updated:** 3 October 2026
**Project phase:** Design finalisation + Probe 2a power/timetable diagnostics complete; Probe 2b power-gate isolation next
**Primary local project path:** `C:\Users\a156b\Documents\Satisfactory - Early Locomotion`

---

## 1. Project Goal

**Satisfactory - Early Locomotion** is a Satisfactory mod that introduces conventional steam railways before the base game's electric monorail trains.

The mod must **not** feel like “vanilla trains, but unlocked earlier.”

Its identity is:

- cheap and easy-to-build conventional railway infrastructure;
- cheaper locomotives and wagons than vanilla trains;
- lower speeds and lower network efficiency;
- steam locomotives requiring coal and water;
- visible servicing and meaningful servicing delays;
- mechanical semaphore signalling controlled by signal boxes;
- locomotive classes with different operational roles;
- conventional steam rail eventually giving way to the superior vanilla electric monorail system.

The player should gain powerful early long-distance bulk transport, but have to engineer around the operating limitations of steam.

### Railway assistant and animated education — Agreed

Early Locomotion has a warm, bubbly, expressive scripted railway assistant, distinct from ADA and voiced by the creator, with optional/replayable animated miniature teaching on a clean white model-railway table. The always-accessible library uses older/prototype FICSIT visual language; lessons unlock progressively. Live network diagnosis/operation, route calculation, automatic fixes/signal placement and generative AI are excluded.

The first-unlock ADA-style takeover and legacy-FICSIT lore flavour remain Proposed; name, dialogue, lore, tutorial roster, final UI and implementation remain Open Questions OQ15–OQ18. TECHNICAL VERIFICATION NEEDED.

---

## 2. Core Balance Philosophy

Early rail should be attractive because the **track and rolling stock are affordable**, not because the system is equal to vanilla electric rail.

Balance should come mainly from:

- locomotive performance;
- signalling limits;
- coal and water logistics;
- servicing time;
- station footprint;
- train weight;
- acceleration and traction;
- lower wagon capacity;
- lower network density;
- more complicated operation.

Avoid using extra clicks or deliberately awkward construction as the main balancing mechanism.

Every limitation should ideally create a player choice.

Examples:

- insufficient range → add an auxiliary tender, add a service stop, or use a larger locomotive;
- insufficient hauling power → use a larger locomotive, fewer wagons, or improve route gradients;
- too many trains → add signals and signal boxes;
- too much congestion → improve signalling or transition to electric rail;
- long servicing delays → redesign the network or later improve service infrastructure.

---

## 3. Track Design

### Agreed

- Early railway uses **conventional two-rail track**.
- Visual style should resemble real railway track: two narrow rails with sleepers/ties between them.
- Construction materials should primarily use:
  - Iron Plates
  - Iron Rods
- Early railway is physically different from the vanilla FICSIT monorail.
- Steam locomotives cannot run on the FICSIT monorail.
- FICSIT electric locomotives cannot run on the conventional steam railway.
- Track itself should be inexpensive and convenient to construct.
- The earlier idea of giving early track a shorter placement length than vanilla track is **superseded**.

### Current direction

Early track may actually permit **longer individual placement lengths** than vanilla rail, making the initial infrastructure easier to establish.

The main disadvantages should come from the trains and railway operation rather than from track placement.

### Open

- final maximum rail segment length;
- track speed limit;
- exact Iron Plate / Iron Rod cost;
- curvature and gradient limits;
- how much existing spline geometry can be preserved during later monorail conversion.

---

## 4. Signalling

### Agreed

Steam-era signalling uses mechanical **semaphore signals**.

Semaphore signalling has limitations that vanilla electronic signalling does not:

- maximum signal block length;
- maximum permitted operating speed;
- signals must be controlled by a signal box;
- signal boxes have limited capacity and territory.

Stations include an integrated signal box so a simple first railway does not require extra buildings.

Dedicated signal boxes are needed for larger networks.

Signal assignment should preferably be based on connected railway territory rather than requiring the player to manually wire every signal.

### Initial playtest ideas — not final

- semaphore block length: roughly 400–500 m;
- early automatic signalling speed: roughly 60 km/h;
- station signal box: roughly 6–8 controlled signals;
- dedicated signal box: roughly 12–16 signals;
- signal-box territory: roughly 1–1.5 km of connected railway.

### Desired progression

Basic block signalling first.

Later steam-era improvements may introduce better interlocking / improved semaphore systems.

Anything equivalent to vanilla path signalling should arrive late or remain part of the vanilla electric railway advantage.

---

## 5. Signal Boxes

Signal boxes are a major part of the mod's visual and mechanical identity.

Desired visual direction:

- substantial period-style building;
- visible lever frames;
- windows;
- cable/rod conduits;
- mechanical operation;
- animated levers when routes/signals change.

Desired UI information:

- controlled signals;
- signal state;
- used/available capacity;
- control territory.

### Mechanical linkage visuals — Agreed

Automatic rods/wires represent semaphore-to-box control, following the formation and updating assignments where practical. No manual wiring or full mechanical transmission simulation. Twitch/clack ambience is secondary to arms/levers; routing, equipment coverage, continuity, regeneration, clutter, performance and multiplayer remain OQ04. TECHNICAL VERIFICATION NEEDED.

Open questions include:

- exact signal capacity;
- how distance is measured through junctions;
- overlapping signal-box territories;
- reassignment after track changes;
- invalid/uncontrolled signal behaviour.

---

## 6. Locomotive Classes

Three main gameplay classes are currently planned:

### Small

British visual reference: **LMS Fowler Dock Tank**

Role:

- tank engine;
- no normal tender;
- inexpensive;
- economical;
- suited to local work, industrial branches, and short trains;
- good usefulness at low speeds;
- limited coal/water capacity;
- weakest long-distance/heavy-haul capability.

An auxiliary tender may be possible, but its extra mass should be a significant tradeoff for the weakest locomotive class.

### Medium

British visual reference: **SR Merchant Navy Class**

Role direction:

- tender locomotive;
- significantly larger coal/water capacity;
- higher consumption;
- good long-distance capability;
- likely the **fastest steam class**;
- useful for lighter long-distance and mixed freight;
- enough power for an auxiliary tender to become a practical option.

Whether Medium is definitively the fastest steam class remains an open balance decision.

### Large

British visual reference: **BR Standard Class 9F**

Role:

- tender locomotive;
- strongest heavy freight capability;
- high traction;
- large coal/water demand;
- intended for long/heavy trains;
- slower acceleration than lighter classes;
- auxiliary tender useful on especially long routes.

Large must not simply make Small and Medium obsolete.

---

### Core locomotive identity and numbering — Agreed

Normal locomotives are normally unnamed class members with automatic visible running numbers and a distinct permanent hidden Fleet Identity. Core provides world-level Standardised / Historical Operator modes, remembered regional numbers, a cheap renumber-unlock direction and class/number fleet search. VIPs retain fixed historical names/numbers. Historical datasets, uniqueness domain, storage, hooks, unlock cost and UI remain OQ28–OQ30; no implementation/API is verified.

## 7. Regional Locomotive Variants

Agreed: regional style is world/save-level, not per-player, and is intended to update existing and future Core/basic infrastructure and rolling stock. Normal Core uses one world style rather than duplicate regional buildables or routine cross-region mixing. Connected wagon presentation follows its controlling locomotive; disconnected wagons follow the world style. Controlling-locomotive determination and live mass/presentation migration remain technically unverified. Each supported Core style ultimately provides one Small, Medium and Large locomotive with individual definitions. Exact launch regions remain open; discussed British/North American/Continental examples are not launch commitments.

Standardise software/data contracts, not physical chassis. Regional power, mass and rolling-stock tare may differ while representative regional trains offer broadly comparable useful performance. **Superseded:** identical regional class statistics. Exact values, regional-switch stat/presentation migration and save/runtime safeguards remain OQ06; feasibility is unverified.

Post-Core enthusiast packs remain **Proposed**, with agreed Core-priority/shared-foundation/compatibility constraints. Role-based catalogues, historical cards/liveries and optional Advanced driving are expansion directions, not current prototype tasks. Agreed fallback: an expansion locomotive without a valid owned destination counterpart retains its region, presentation and number; symmetric regional rosters are not required. Advanced driving focuses on firebox, regulator and reverser/cutoff, with competent default Simple controls; formulas/advantage remain open. Core/expansion VIPs are prestige rewards with fixed historical identity, not logistics upgrades; no named roster is approved. Expansion progression accompanies Core; milestone integration remains Proposed/unverified. Pricing (~£10 planning target), roster, chronology, infrastructure, technical migration, distribution and entitlement remain open. See GAME_DESIGN OQ19–OQ30 and ROADMAP.docx.

---

## 8. Fuel and Water

### Agreed

Steam locomotives require:

- coal;
- water.

Range should emerge from actual:

- storage capacity;
- consumption;
- train load;
- operating conditions;

rather than from an arbitrary kilometre countdown.

Water should generally be the tighter range limitation.

Compacted Coal should be more efficient.

Preferred implementation principle: use the game's fuel-energy values where possible instead of hardcoding a special Compacted Coal multiplier.

The locomotive UI should ideally provide an estimated remaining range.

---

## 9. Stations

Steam stations should be **significantly larger** than vanilla stations.

A full steam station includes:

- locomotive stopping area;
- cargo interfaces;
- integrated signal box;
- water tower;
- coal-loading equipment;
- servicing machinery.

### Desired servicing sequence

When a locomotive arrives:

1. it approaches slowly;
2. docks into position;
3. releases a long steam hiss;
4. water equipment moves toward the locomotive;
5. coal-loading equipment moves toward the bunker/tender;
6. both systems mechanically align with the locomotive's service points;
7. coal and water are transferred;
8. equipment retracts;
9. locomotive departs.

Servicing should be visually intricate and become part of the mod's identity.

### Preferred technical concept

Each locomotive exposes model-specific servicing targets such as:

- water fill target;
- coal fill target;
- steam exhaust locations;
- coupler positions;
- cab interaction point.

These are design-interface concepts only until verified against the actual Unreal/Satisfactory implementation.

### Servicing time

Servicing should not simply add a fixed timer.

Preferred design:

- water crane has a transfer rate;
- coal chute has a transfer rate;
- lightly depleted locomotives receive a short top-up;
- heavily depleted locomotives take substantially longer.

---

## 10. Auxiliary Tenders

Distinguish between:

### Normal tender

Part of the locomotive's standard design.

Examples:

- Merchant Navy tender;
- 9F tender.

If technically practical, locomotive + normal tender should behave as one locomotive entity for gameplay/scheduling purposes.

### Auxiliary tender

A separate vehicle added by the player.

Purpose:

- increase water and/or coal capacity;
- extend range.

Tradeoffs:

- extra mass;
- consumes train length;
- reduces effective freight capacity;
- worsens performance on weaker locomotives.

Potential types:

- water-only tender;
- combined coal/water tender.

Exact launch set is not final.

---

## 11. Trackside Service Facilities

Long routes should not require a full cargo station just to replenish steam locomotives.

Planned/possible service buildings:

- Water Tower
- Coaling Stage
- Combined Steam Service Point
- Full Steam Station

A locomotive can stop mid-route to refuel/rewater, making extremely long steam journeys possible at the cost of journey time.

Preferred scheduling direction:

service points should appear explicitly in train timetables, for example:

- stop at water tower;
- service water;
- depart when full.

Automatic opportunistic servicing has been discussed but is not currently the preferred default.

---

## 12. Wagons

Steam wagons should be:

- cheaper than vanilla freight cars;
- lower capacity;
- visually appropriate to conventional rail;
- available in multiple variants.

Initial illustrative item capacity discussed:

- roughly 16–24 stacks;
- 20 stacks used as an example versus vanilla's 32.

No final wagon capacities are approved yet.

Future wagon categories may include:

- item freight;
- fluid;
- specialist/support wagons;
- auxiliary tenders.

---

## 13. Transition to Vanilla Electric Rail

The steam railway and vanilla monorail are physically incompatible.

The old idea that steam locomotives could continue running on upgraded monorail track is **superseded**.

### Preferred conversion UX

Treat the transition similarly to upgrading belts/buildings:

1. select the higher-tier FICSIT railway;
2. point it over existing conventional track;
3. show an upgrade/replacement hologram;
4. preserve the route/spline geometry where technically feasible;
5. replace the conventional line with vanilla-style monorail.

The system should warn the player if converting a section would strand steam rolling stock.

The goal is to preserve the player's **route-planning work**, not physical interoperability.

Mixed mature networks may contain:

- retained steam branches;
- electric mainlines.

A future transfer/interchange building has been suggested but is not confirmed for initial release.

---

## 14. Development Architecture Direction

Current proposed architecture:

- shared steam-locomotive gameplay logic;
- data-driven locomotive definitions;
- model-specific presentation and animation;
- shared wagon families;
- hybrid Unreal C++ + Blueprint.

Gameplay systems should be separated from presentation.

Data-driven parameters should cover things like:

- locomotive class;
- mass;
- maximum speed;
- traction;
- acceleration/braking;
- coal capacity;
- water capacity;
- consumption;
- servicing targets;
- regional model;
- wagon capacity/type.

The exact Unreal implementation pattern is **not yet decided** and must be based on verified SML/engine APIs.

---

## 15. Current Verified Development Environment

Technical reconnaissance began on 14 September 2026. The current setup checkpoint below includes verified relocation and probe packaging on 2 October 2026.

### Verified target

- **Satisfactory:** 1.2
- **Satisfactory Mod Loader:** SML 3.12.0
- **Coffee Stain Unreal Engine:** 5.6.1-CSS

Current pairing:

`Satisfactory 1.2 ↔ SML 3.12.x ↔ Unreal 5.6.1-CSS`

Older UE 5.3 / SML 3.11 material must be treated as potentially outdated.

### Current setup checkpoint

Completed and verified:

- Coffee Stain Unreal Engine 5.6.1-CSS installed;
- `SatisfactoryModLoader` repository cloned;
- `FactoryGame.uproject` associated with 5.6.1-CSS;
- Wwise 2023.1.14.8770 and required deployment targets installed;
- Wwise Unreal integration 2023.1.14.8770.3555 completed;
- companion Wwise project created;
- SoundBanks generated successfully;
- Visual Studio Community 2022 17.14.x installed with the required workloads/components selected;
- Windows restarted after Visual Studio installation;
- Visual Studio project generation succeeded on 20 September 2026; `FactoryGame.sln` created in the SML repository;
- first FactoryGame **Development Editor / Win64** build succeeded in Visual Studio 2022 on 20 September 2026 (12 succeeded, 0 failed);
- first usable Unreal Editor launch and FactoryGame environment load succeeded on 26 September 2026 in 5.6.1-CSS; SML 3.12.0 initialization completed.

Wwise Windows metadata/platform and Init resource-loading errors are resolved after enabling Object GUID, Object Path, Max Attenuation, and Estimated Duration metadata and regenerating SoundBanks. The all-banks metadata efficiency message is advisory.

Turnkey/System.Windows.Forms, Version=6.0.2.0 remains unresolved but deferred because it has not blocked project generation, the FactoryGame build, or editor launch. No dependency/toolchain versions changed.

SML now uses `C:\SML`. On 2 October 2026, project regeneration, Development Editor / Win64 build and editor/probe Blueprint loading succeeded after relocation; Wwise remained functional. `EL_ArchitectureProbe` implementation and Blueprint preparation are complete, and its Windows Shipping package deployed successfully to `D:\Steam\steamapps\common\Satisfactory` (AutomationTool ExitCode 0). The 260-character Shipping path blocker is resolved. Alpakit did not launch retail Satisfactory during packaging. The later retail Runtime Probe 1 is completed: AFGLocomotive subclassing is runtime-verified viable for construction, rail attachment, input, braking and unpowered movement. Within the currently tested implementation, `SetTractivePowerFactor(1.f)` is necessary for producing unpowered traction; the no-op `UpdatePower()` alone is insufficient. This does not establish the final production locomotive architecture. The working probe is restored; AFGLocomotive-derived probe integration with vanilla rolling stock is runtime-verified for normal construction-time consist formation, forward/reverse movement and braking while electrically unpowered. Final production architecture remains unresolved.

### Important current traps

- Visual Studio installer may encourage a newer VS release; Satisfactory tooling currently expects VS 2022.
- SML 3.12 uses newer build settings and full include paths.
- Satisfactory 1.2 migration includes increased use of `TObjectPtr<>`.
- `FGGameFeatureData` requirements changed.
- Enhanced Input usage changed.
- Old compiled 1.1 / SML 3.11 mods are not compatible with the current environment.

---

## 16. Relevant Verified Satisfactory Rail Classes

Claude's reconnaissance found current public headers for:

- `AFGRailroadVehicle`
- `AFGLocomotive`
- `AFGBuildableRailroadTrack`
- `AFGBuildableRailroadSignal`
- `AFGBuildableRailroadStation`
- `AFGRailroadSubsystem`

These strongly suggest Early Locomotion can potentially reuse parts of Satisfactory's existing railroad graph and vehicle systems.

However:

`AFGLocomotive` is designed around the vanilla electric/third-rail power model.

The project has **not yet decided** whether steam locomotives should:

- subclass/extend vanilla locomotive classes and replace the power model;
- extend a more generic railroad-vehicle layer;
- or use another architecture.

Read-only local railway header/API reconnaissance is complete. Local FactoryGame Private `.cpp` implementations are generated stubs; runtime baseline experiments are required before choosing the locomotive/track architecture.

Railway header/system reference areas include:

- railroad vehicle movement components;
- locomotive movement components;
- train/timetable composition classes;
- railroad attachments;
- switches;
- train platforms;
- cargo platforms.

---

## 17. AI / Tooling Roles

### ChatGPT project chats

- **The Manager:** project coordination, setup guidance, decisions, approvals, debugging triage, delegation, ordinary research, and review of specialist output.
- **Ideas Lab:** brainstorming and speculative design; ideas return to The Manager before becoming canonical.
- **Project Operations:** Work-mode project-file maintenance, artifacts, reconciliation, conversion, and substantial research deliverables; it does not independently make game-design decisions.

### Claude Code

Primary role:

- lead implementation engineer;
- Unreal/SML C++;
- repository work;
- debugging;
- API/header investigation;
- build diagnosis;
- Blueprint handoff documentation.

Claude has a root `CLAUDE.md` defining project rules.

### Codex

Planned role:

- independent code reviewer;
- second implementation opinion;
- debugging;
- refactoring;
- QA;
- alternative implementation review.

### Blender

Primary final 3D modelling tool.

AI may assist through Python scripting for repetitive modelling tasks.

### Meshy

Potential supporting role:

- props;
- rough blockouts;
- secondary environmental assets.

Not intended as the final source for precision locomotive geometry.

### Substance 3D

Preferred material/texturing workflow.

### ElevenLabs

Potential source for layered steam locomotive sound effects.

---

## 18. Claude Project Rules

The project root contains `CLAUDE.md`.

Important principles:

- Claude is implementation lead, not final game designer.
- `Design/GAME_DESIGN.md` is design authority.
- Agreed/Proposed/Playtest/Superseded/Open Question statuses must be respected.
- Claude must not invent Satisfactory/SML APIs.
- unfamiliar APIs must be verified;
- no silent design decisions;
- multiplayer and save/load implications must be considered;
- binary Unreal assets should not be casually modified;
- major changes should remain Git-reviewable.

Initial Claude onboarding has been completed successfully.

Claude correctly identified:

- project goal;
- design status hierarchy;
- major agreed systems;
- superseded ideas;
- OQ01–OQ14;
- technical verification requirements.

---

## 19. Git Status / Project Storage

Primary project folder:

`C:\Users\a156b\Documents\Satisfactory - Early Locomotion`

Git has been initialised.

Baseline commit created before Claude development work.

Claude project instructions were added separately.

The local Documents folder is the **master project location**.

ChatGPT, Claude, Codex, Unreal, Blender, and other tools should all work from the same project rather than maintaining separate competing copies.

---

## 20. Current Development Status

Completed:

- concept established;
- core balance philosophy established;
- track/signalling/station/locomotive direction documented;
- project folder created;
- Git repository initialised;
- `CLAUDE.md` created;
- Claude Code installed and working;
- Claude onboarding completed;
- current technical environment researched;
- Coffee Stain Unreal Engine 5.6.1-CSS installed;
- SML starter repository cloned and `FactoryGame.uproject` associated with 5.6.1-CSS;
- Wwise 2023.1.14.8770 installed and integrated, companion project created, and SoundBanks generated;
- Visual Studio Community 2022 17.14.x installed with required selections;
- Windows restarted after Visual Studio installation;
- Visual Studio project generation succeeded on 20 September 2026; `FactoryGame.sln` created in the SML repository;
- first FactoryGame **Development Editor / Win64** build succeeded in Visual Studio 2022 on 20 September 2026 (12 succeeded, 0 failed);
- first usable Unreal Editor launch and FactoryGame environment load succeeded on 26 September 2026 in 5.6.1-CSS; SML 3.12.0 initialization completed.

Documentation reconciliation and repository cleanup are complete; INDEX.md is restored and reconciled files are in place. Project Operations (Local) is established inside the ChatGPT Project with local access verified; Project Operations (Cloud) remains available for cloud/project-source work.

Read-only railway header/API reconnaissance is complete (Manager/user confirmed 26 September 2026).

SML now uses `C:\SML`. On 2 October 2026, project regeneration, Development Editor / Win64 build and editor/probe Blueprint loading succeeded after relocation; Wwise remained functional. `EL_ArchitectureProbe` implementation and Blueprint preparation are complete, and its Windows Shipping package deployed successfully to `D:\Steam\steamapps\common\Satisfactory` (AutomationTool ExitCode 0). The 260-character Shipping path blocker is resolved. Alpakit did not launch retail Satisfactory during packaging. The later retail Runtime Probe 1 is completed: AFGLocomotive subclassing is runtime-verified viable for construction, rail attachment, input, braking and unpowered movement. Within the currently tested implementation, `SetTractivePowerFactor(1.f)` is necessary for producing unpowered traction; the no-op `UpdatePower()` alone is insufficient. This does not establish the final production locomotive architecture. The working probe is restored; AFGLocomotive-derived probe integration with vanilla rolling stock is runtime-verified for normal construction-time consist formation, forward/reverse movement and braking while electrically unpowered. Final production architecture remains unresolved.

Not yet completed:

- Probe 2b exact power-gate isolation, successful station/timetable operation and broader integration before final architecture selection;
- production Early Locomotion gameplay implementation and first playable railway;
- production packaging/runtime verification.

---

## 21. Immediate Next Steps

### Current next task

Probe 2b: set only the inherited locomotive `mHasPower` state true via verified Unreal property reflection while leaving `PowerInfoHasPower` unchanged, then test self-driving. This is the next planned test, not a verified outcome; do not select final production architecture.

Runtime Probe 1 is completed and analysed. Two separately placed probes moved from rest with HasPower=false and retained train/rail integration, normal input response and working air/dynamic braking. Construction-time vanilla Freight Wagon formation, forward/reverse movement and clean braking are now verified without derailment/separation in normal operation on unpowered railway. The temporary probe coupling node/position is visibly misaligned. Driving the probe into an independently placed loose wagon made the train unresponsive to commands. Whether collision-coupling independently placed rail vehicles is a supported vanilla workflow has not been established; this observation is not classified as an architecture failure. Earlier camera, normal locomotive UI and exit-placement residuals remain unresolved. Production implementation and broader runtime integration remain unverified.

Probe 2a recorded 1,069 samples with both locomotive power flags false. Powered shoe contact allowed manual traction, but self-driving produced SDLE_NoPower one tick after activation and suppressed traction; disabling it restored manual driving. The timetable/self-driving No Power condition is locomotive-level rather than simply lack of powered third rail. The exact gate remains unresolved because `HasPower` and `PowerInfoHasPower` were always identical in this run. The earlier powering-related manual-drive failure did not reproduce and remains unverified.

The Probe 1 and Probe 2a results, limits and other untested areas are recorded in Development/TECHNICAL_ENVIRONMENT.md. Turnkey remains unresolved/deferred; no final architecture decision has been made.

Do not begin major gameplay implementation before the runtime evidence and architecture review establish a viable approach.

---

## 22. First Technical Prototype Goal

The first prototype should be deliberately small.

Goal:

**Prove that a custom conventional railway / steam rolling-stock approach can integrate correctly with Satisfactory's railroad systems.**

Initial prototype should focus on:

- basic custom rail representation;
- one minimal locomotive;
- one wagon;
- one simple line;
- basic movement;
- existing railroad graph compatibility.

Do not initially build:

- full coal/water simulation;
- large animated steam station;
- semaphore network;
- regional variants;
- 9F production model;
- complex tenders;
- final balance.

The purpose is to validate the fundamental architecture before substantial content work begins.

---

## 23. Current Open Questions

### OQ01 — Progression
Exact milestones, prerequisites, and service-point unlock timing.

### OQ02 — Track
Maximum segment length, speed cap, recipe quantities, curvature/gradient rules.

### OQ03 — Signalling
Block lengths, speed caps, interlocking progression, invalid/uncontrolled behaviour.

### OQ04 — Signal Boxes
Signal capacities, territory/overlap/reassignment and generated-linkage technical details (routing, equipment coverage, regeneration, performance and multiplayer).

### OQ05 — Locomotives
Whether Medium is fastest; exact traction, acceleration, mass, capacities, and consumption.

### OQ06 — Regions
Exact Core launch regions, world/save style selection, fallback and visual/stat migration; dynamic versus construction-fixed data, running trains, total mass, save migration and switching exploits. Regional variation is Agreed; identical class statistics are Superseded.

### OQ07 — Wagons
Launch wagon roster, capacities, dimensions, costs, platform compatibility.

### OQ08 — Supplies
Supported fuels, starvation behaviour, range calculation, buffers, transfer rates.

### OQ09 — Stations
Dimensions, servicing animation, service reach, simultaneous operations, multiple locomotive handling.

### OQ10 — Tenders
Launch tender types, entity model, coupling rules, refill/resource distribution.

### OQ11 — Service Points
Facility set, timetable controls, departure conditions, signal-box requirements.

### OQ12 — Monorail Conversion
Geometry preservation, costs, safeguards, occupied track, partial conversion, recovery.

### OQ13 — Launch Scope
Core/later non-expansion scope; advanced late-game steam infrastructure is expansion-only, with catalogue open under OQ22.

### OQ14 — Implementation
Final toolchain validation, multiplayer/save architecture, performance, testing and packaging.

### OQ15–OQ18 — Railway Assistant and Animated Tutorials

Character/name/dialogue/avatar/palette/interface (OQ15); historical origin and older-FICSIT lore status (OQ16); launch roster, unlock mapping, and milestone narration (OQ17); controls, first-unlock trigger, ADA-style presentation, animated demonstrations, unlock tracking, and audio integration requiring technical verification (OQ18). Full questions remain in the dedicated GAME_DESIGN section.

---

### OQ19–OQ30 — Expansion, identity and UX questions

Build-menu support/nesting (19); expansion roster/roles/progression and milestone API (20); chronology (21); advanced infrastructure (22); technical regional correspondence/migration and advanced-asset fallback (23); Advanced formulas/slip/advantage (24); liveries/VIP roster/prices/licensing (25); commercial delivery (26); multiplayer/saves (27); Fleet Identity storage/lifecycle (28); historical numbering data/rules/collision domain (29); renumber-unlock and fleet-search UI (30). The missing-counterpart locomotive retention rule is Agreed; its implementation remains open. Details remain in GAME_DESIGN.

## 24. Superseded Ideas

Do not accidentally reintroduce these without a deliberate design decision:

- early rail being limited to roughly half vanilla placement length;
- universal physical chassis for all regional locomotives;
- identical locomotive class statistics between regional variants;
- steam locomotives remaining compatible with upgraded FICSIT monorail.

---

## 25. File Authority / Recommended Project Documents

Project authority order:

1. `INDEX.md` — current project overview, navigation, and status.
2. `Design/GAME_DESIGN.md` — canonical gameplay and design authority.
3. `Development/PROGRESS_LOG.md` — current development checkpoint, blockers, work history, and exact next action.
4. `Development/TECHNICAL_ENVIRONMENT.md` — verified toolchain, API, and environment facts.
5. `CHANGELOG.md` — meaningful project, design, and implementation history.
6. `WORKFLOW.md` — coordination and change discipline.
7. `Development/SPECIALIST_DELEGATION.md` — detailed specialist selection, model/effort, task, handoff, and verification rules.
8. `CLAUDE.md` — Claude-specific implementation rules.

`References/` remains supporting/historical material outside the authority chain.

`ROADMAP.docx` — human-readable project direction and phase roadmap; maintained from canonical information, overview only and non-authoritative on conflict. It is outside the formal authority order.

[Design/Early Locomotion Feature Catalogue.docx](Design/Early%20Locomotion%20Feature%20Catalogue.docx) — comprehensive human-readable explanation of planned gameplay/features, derived from GAME_DESIGN.md and non-authoritative on conflict. It explains what features do and why; ROADMAP.docx retains current position and phase planning.

`WORKFLOW.md` is the concise human-and-agent guide to coordination and change flow. [Development/SPECIALIST_DELEGATION.md](Development/SPECIALIST_DELEGATION.md) is the detailed authoritative specialist-selection, model/effort, task-construction, handoff and verification guide. `Design/Early Locomotion Design Reference.docx` is the human-readable Word copy of the design master. `Balance/` holds future balance models and playtest data.

Future chats and AI agents should read `INDEX.md` first, then follow its references.

---

## 26. Index Maintenance Rules

This file should describe **current project truth**, not every historical discussion.

When a major decision changes:

1. update the relevant detailed design document;
2. update this Index;
3. mark any previous idea as superseded where needed;
4. update `CHANGELOG.md`;
5. do not silently convert proposals into agreed design;
6. keep unresolved items in the Open Questions section.

A future planning chat may maintain this file independently, provided it reads the canonical design files and does not invent or resolve design decisions without approval.
