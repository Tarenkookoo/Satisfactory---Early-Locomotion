# Early Locomotion — Public Presentation Brief

**Project:** Satisfactory - Early Locomotion  
**Snapshot:** 18 October 2026  
**Purpose:** Public-safe input for an executive or project-history presentation.  
**Authority:** Derived reference only. This brief creates no design decision, implementation approval or release commitment. The latest approved local canonical records remain authoritative.

This document is self-contained. Source names and visual filenames below are provenance labels, not links to uploaded evidence. The original canonical working copies, raw logs and images are not dependencies of this publication. Existing repository documents may represent older snapshots; use this dated brief for the presentation's current-position claims.

## 1. Project identity

Early Locomotion introduces affordable conventional steam railways before Satisfactory's electric monorail trains. Its identity is operational: cheap track and rolling stock make early bulk transport attractive, while fuel, water, servicing, signalling limits and locomotive choice create meaningful engineering trade-offs. Steam is intended to complement factory progression before the superior throughput and convenience of mature electric rail.

**Current position:** Experimental locomotives and conventional-track prototypes have demonstrated important runtime capabilities. A new HD track visual baseline has been accepted. The project is still validating integration and production readiness; it is not a finished playable mod or a selected final architecture. [C01]

## 2. Read status labels precisely

| Label | Meaning in this brief |
| --- | --- |
| **Agreed** | Approved design direction; not evidence that it has been implemented. |
| **Proposed** | Candidate direction or experiment awaiting relevant approval/verification. |
| **Playtest Target** | Illustrative balance value requiring testing, not a final specification. |
| **Superseded** | Replaced historical idea, not an active requirement. |
| **Open Question** | Unresolved choice or technical question; this brief resolves none. |

Workflow states such as COMPLETE or PAUSED apply to the stated task scope. A completed diagnostic, Blender asset or package is not automatically a completed production feature. [C02]

## 3. Major design direction

### Agreed Core direction

- **Singleplayer first:** Core 1.0 prioritises a robust singleplayer experience. Singleplayer persistence/save-load remains required. Multiplayer implementation and validation are deferred post-release.
- **Conventional railway:** Two rails with sleepers; inexpensive construction using Iron Plates and Iron Rods as the agreed material direction. Exact quantities, geometry rules, limits and recipes remain open.
- **Distinct operational balance:** Coal and water determine useful range alongside train load and operating conditions. Servicing should involve replenishment and meaningful time, rather than arbitrary extra clicks.
- **Three locomotive roles:** Small, Medium and Large retain different useful duties. British design references are the LMS Fowler Dock Tank, Merchant Navy and BR Standard Class 9F respectively. These design references are distinct from the Jinty, Yellow Pannier and Black 5 experimental assets.
- **Stations and support:** Steam stations combine freight handling, supplies, servicing and an integrated signal box. Dedicated service facilities and auxiliary tenders support longer routes; exact implementations remain unresolved.
- **Mechanical signalling:** Semaphores belong to signal boxes with limited capacity/territory. Connected-territory assignment avoids manual wiring. Automatic mechanical-looking rods/wires communicate control relationships; full physical transmission simulation is excluded.
- **Fleet identity and regions:** Normal locomotives have visible running numbers and a distinct permanent hidden Fleet Identity. Standardised/Historical Operator modes, remembered regional numbers and fleet search are approved directions. Regional presentation is world/save-level; connected wagon presentation follows the controlling locomotive. Exact datasets, controlling-locomotive logic, migration and persistence remain unverified.
- **Electric transition:** Steam and monorail are intended to be physically incompatible in the finished design. Conversion should preserve route-planning work where technically possible. Temporary vanilla compatibility in probes is testing permission, not a reversal of that design. [C03]

### Manual operation and education

**Agreed:** The Manual Railway Operations Diagram is a compact side-panel topological schematic for manual driving, with local network/nearby-point awareness, permitted turnout control, clear lined routes and AUTO/YARD/MAINLINE modes. Signal-box/interlocking authority remains meaningful. It is separate from automatic train control and the future coupling interface.

**Proposed:** Advanced MAINLINE destination-based route calculation and automatic turnout setting after later signalling progression. Exact interface, algorithms, permissions and technical APIs remain Open Questions.

**Agreed:** A warm, expressive scripted railway assistant, voiced by the creator, teaches through optional/replayable miniature animated lessons on a clean white model-railway table. A progressive reference library remains accessible. Live network diagnosis, automatic repairs, route operation and generative AI are excluded.

**Proposed:** The first-unlock apparent ADA takeover and legacy-FICSIT lore treatment. Character particulars, dialogue, lesson roster, final UI and implementation remain OQ15–OQ18. [C04]

### Balance, superseded ideas and later scope

**Playtest Targets:** Initial examples include roughly 400–500 m semaphore blocks, about 60 km/h automated speed, 6–8 signals for a station box, 12–16 for a dedicated box and roughly 1–1.5 km territory. These are not final balance or demonstrated runtime limits.

**Proposed/Open Question:** Longer convenient track placement, exact progression milestones, whether Medium is the fastest steam role and detailed performance curves. Do not present older ascending Small/Medium/Large speed examples as settled alongside the later fastest-Medium proposal.

**Superseded:** Half-vanilla maximum placement length; a universal regional physical chassis; identical regional locomotive statistics; steam locomotives continuing to run on converted monorail.

Post-Core enthusiast expansion packs remain **Proposed**, with approved Core-priority/shared-foundation constraints. Optional expansion Advanced driving focuses on firebox, regulator and reverser/cutoff; competent Simple operation remains the default. The approved VIP/prestige framework is for enthusiast rewards, not superior logistics. Exact rosters, unlocks, formulas, licensing and delivery remain open. No commercial release mechanism is established. [C05]

## 4. Development milestones

Recorded technical target: Satisfactory 1.2, SML 3.12.0 within the 3.12.x pairing, and Coffee Stain Unreal Engine 5.6.1-CSS. Wwise 2023.1.14 integration is functioning; this is recorded environment context, not a new dependency change.

Dates below are recorded milestone dates; some are reconciliation dates rather than precise runtime timestamps. Results are limited to the tested prototypes.

| Recorded date | Achievement | Boundary |
| --- | --- | --- |
| 14–19 September | Project/design records established; custom Unreal/SML and audio/toolchain setup progressed. | Setup is separate from gameplay implementation. |
| 20 September | Project files generated and first FactoryGame Development Editor / Win64 build succeeded: 12 succeeded, 0 failed. | Build success did not itself establish editor/runtime success. |
| 26 September | Usable Unreal Editor launch, project loading and SML initialisation; railway header reconnaissance completed. | Native implementation stubs left important runtime questions unanswered. |
| 1 October | Jinty asset experiment demonstrated editable reference-driven modelling and coupled-running-gear animation. | Non-production workflow experiment; paused, not export-ready final art. |
| 2 October | Runtime Probe 1 demonstrated construction, vanilla rail attachment, input, braking and unpowered movement; causality controls and vanilla-wagon integration followed. | Experimental AFGLocomotive-derived probe, not production architecture. |
| 3 October | Logical-power/timetable, powered-station cargo compatibility, dynamic readiness and vanilla Blueprint inheritance experiments recorded. | Specific tested capabilities; no custom steam simulation or final architecture. |
| 9–10 October | Six-wheel animation, prototype camera correction and read-only diagnostic UI reconciled; conventional-track feasibility and retail tests progressed. | Coupling rods still static; production UI/track systems remain unfinished. |
| 10 October | Black 5 v014 provisional asset milestone and validation toolkit D2 recorded. | Blender/static evidence does not prove retail behaviour. |
| 12 October | Basic Manual Railway Operations Diagram design approved. | Design approval, not a built UI. |
| 18 October | Stage 3B-4G diagnostic closed; material investigations/v003 packaging, HD track v004 visual baseline and rendering research reconciled. | Permanent hologram correction, v003 retail comparison and v004 engine/performance validation remain incomplete. |

[C06]

## 5. What locomotive experiments actually demonstrated

**Traction causality:** In the tested implementation, `SetTractivePowerFactor(1.f)` was necessary for unpowered traction; a no-op `UpdatePower()` alone was insufficient. Vanilla unpowered control did not move. The successful probe accepted input, generated tractive force and braked on unpowered track.

**Logical readiness:** Probe 2b set inherited logical `mHasPower=true` while `PowerInfoHasPower=false`; successful timetable samples also had no sliding-shoe electrical power. Two opposing locomotives repeatedly travelled between stations, stopped, reversed operational direction and continued. The per-tick reflected write was a temporary mechanism, not the approved production setter.

**Wagon/station compatibility:** A probe–vanilla Freight Wagon–probe consist self-drove, stopped and reversed on an unpowered railway. Unpowered station machinery did not dock/load. Powered infrastructure docked and loaded the wagon, transported items and retained timetable operation. This does not implement custom stations or coal/water servicing.

**Dynamic readiness:** A temporary mod-owned readiness boolean controlled both traction and timetable readiness. False readiness prevented operation even with rail power; restoring it returned operation without rebuilding. No fuel, water or boiler simulation is implemented by that boolean.

**Presentation/integration:** Direct vanilla BP_Locomotive inheritance preserved normal look-around, HUD, horn/sounds, exit and powered driving in its separate probe. It supports further component-adapter experimentation, not a production selection. The Yellow Pannier's later probe-specific camera correction, six-wheel animation and Slate diagnostics were accepted within prototype scope. Diagnostic UI limitations include hide-HUD interaction, dynamic-brake display and direction interpretation. [C07]

## 6. Conventional track and diagnostic closure

The 3.048 m calibration segment demonstrated conventional two-rail appearance, curved deformation, Pannier movement, construction/dismantling and persistence after rejoining. Post-reload driving was not verified. Gauge, height, collision/clearance and calibration dimensions must not become production specifications by implication.

**Stage 3B-4G — COMPLETE bounded diagnostic, not a correction:**

| Test | Accepted observation |
| --- | --- |
| T0 | Unwanted perpendicular hologram geometry present. |
| T1: hide relative X=0 component | Artifact remains. |
| T2: hide relative X=+100 cm component | Artifact remains. |
| T3: hide both | Perpendicular artifact disappears, leaving parallel preview lines. |
| Restore T3 | Artifact returns. |

Logs confirmed expected targeting/restoration and clean shutdown, with no relevant diagnostic errors/crashes. Visual results came from Manager-reviewed screenshots; Claude Code did not directly inspect them. T3 used a separate launch. T4 curved-preview confirmation and an additional repeat were not completed.

Either ordinary static component can sustain the unwanted geometry when the other is hidden; joint hiding removes it. Creation pathway/purpose and a safe permanent correction remain unresolved. Visibility changes do not establish safe removal for placement or collision. [C08]

## 7. Material diagnostics versus the HD visual baseline

**Audit/A0/A1:** Flat-colour 8×8 albedos, a shared banded reflection mask, default flat normals, simplified forms and UV mapping were investigated. Inspected development-kit graphs and UV analysis establish a plausible material mechanism; the retail dark-area symptom and material-parent parity were not conclusively diagnosed.

**B0/B1/B2a — completed within their scopes:** Three independently validated constant masks were created. A separate v003 editor candidate contained ten new assets total: three textures, three material instances, one mesh duplicate, Blueprint, descriptor and recipe. Shipping packaging/deployment succeeded; cooked evidence contained all ten assets, seven deployed files matched package output and prior deployment was preserved. Original v001/v002 assets remained separate.

**B2b — NOT performed:** The v001-versus-v003 retail material comparison remains paused and requires renewed authorisation. v003 is a diagnostic, not the finished HD remaster.

**HD v004 — accepted visual-development baseline:** Separately versioned Blender source/export/FBX, nine PBR maps, sixteen Cycles renders and five comparison sheets show improved bullhead rails, timber grain/wear/end-grain, detailed chairs/keys/screws/washers and non-mirrored UVs. Retained attempt-2 verification records 130/130 checks passing and FBX reimport passing; all 58 manifest files were checked against retained hashes during documentation reconciliation. The earlier failed attempt remains retained as failure history.

LOD0 is **14,656 triangles per 3.048 m segment**; eight chair assemblies account for **8,880 triangles, about 61%**. The CEO reviewed actual comparison sheets and the Manager accepted the visual baseline. Heritage direction remains **Proposed** and uncertain fastening dimensions **provisional**. v004 is not Unreal-tested, performance-validated or production-ready; Unreal integration has not been authorised/performed. [C09]

## 8. Rendering, LODs and supporting assets

AD Building completed only a preliminary read-only geometry audit before stopping at its usage gate. **No LOD1, LOD2 or LOD3 mesh was created.** Approximately 4,000-triangle LOD1 and 1,552-triangle LOD2 figures are proposed targets, not achieved results.

Accepted local rendering research identifies placed track's lightweight/AbstractInstance path, material deformation using instance data and engine per-instance mesh LOD support. Development-kit railway assets record four source models and a dedicated low-detail material. Actual retail LOD meshes, switching distances and native details remain unverified. A 3.048 m section compared with development-kit 12 m metadata implies about four times as many visual sections per kilometre, not a measured slowdown.

Embedded StaticMesh LODs are only the **Proposed working integration approach**; a single-material far LOD remains **Proposed**. No renderer modification, LOD integration, retail ForceLOD test or performance benchmark is approved. Far geometry, instance density, material slots and shadows all require attention.

Other assets: Black 5 Stage C.11 v014 is a completed provisional visual prototype, not frozen or Unreal-tested. C.12 remains incomplete; no completed V15 milestone is recorded. Semaphore Stage A v001 has Blender-side verification but no production/runtime implementation. The Jinty experiment's animation must not be misrepresented as animated Pannier coupling rods.

Validation toolkit D2 includes a Blender inspection layer. Retained combined baseline: 372 PASS, 0 FAIL, 6 WARNING, 1 NOT VERIFIED; self-tests detected 117/117 introduced defects with 5/5 controls. These results validate tested evidence checks, not retail behaviour or production readiness. [C10]

## 9. Remaining work and scheduling

Open technical work includes component origin/permanent hologram correction; v003 retail comparison; v004 engine import/spline deformation, normal orientation, roughness remap/AO policy, LODs/performance/seams/shadows; foundation height; rail-centre versus Pannier tread alignment; historical fastening dimensions; production locomotive/track architecture; actual coal/water/steam systems; custom station servicing; robust singleplayer persistence; and the historical intermittent shutdown audio-callback crash. It did not recur in the accepted 3B-4G sessions, but its cause is not resolved.

Open Questions OQ01–OQ30 retain their canonical scope and numbering. Major groups cover progression/track/signalling, regions and performance, stock/supplies/stations/tenders, conversion/implementation, assistant/tutorials, expansion scope, identity/numbering, UI and post-release multiplayer. This brief resolves none.

**Project suspension:** No project progress is authorised 19–23 October inclusive. All specialist development/research/testing and automatic resumption remain suspended. Earliest possible return is 24 October, requiring an explicit new CEO instruction; a date or usage reset is not permission. This single-file publication is a separately authorised maintenance exception, not permission to resume development. [C11]

## 10. Visuals suitable for a presentation

**No images or asset binaries are published with this brief.** These are a local visual shortlist, not public download links; the creator must provide any chosen image separately through an approved channel. Do not substitute a broken repository link or imply that a cloud reader has the files.

| Candidate filename / lineage | Presentation use | Required caption / boundary |
| --- | --- | --- |
| `SHEET_01_Compare_v001_vs_HD_v004.png` — Track v004 comparisons | Primary before/after evidence of visual development; inspected for this brief. | “Blender visual comparison: calibration v001 versus accepted HD v004 candidate; not an Unreal/retail comparison.” |
| `SHEET_04_Rail_Fastening_Closeups_v004.png` — Track v004 comparisons | Detail and repeated-segment views; inspected for this brief. | “Blender prototype; casting/key/screw layout provisional.” |
| `SHEET_03_Sleeper_Closeups_v004.png` / `SHEET_05_Material_Daylight_v001_vs_v004.png` — same set | Additional timber/material illustrations; present in the accepted set. | “Blender appearance evidence, not retail shadow/performance validation.” |
| `hero_lit_v004.png` — Track v004 | Clean hero image from the accepted render set. | “Accepted visual-development baseline; production readiness unverified.” |

The accepted track set contains sixteen renders and five sheets; only the first two listed sheets were directly re-inspected for this brief. Visual-baseline acceptance is not a new blanket publication licence. Third-party locomotive/reference photography is not cleared for public reuse by this task; attribution/licensing and exact selection need separate review. No proposed image is evidence of unimplemented gameplay. [C12]

## 11. Source-to-claim map and evidence boundaries

These source labels identify the reviewed local snapshot. They are not links to unpublished records, and no personal paths, private communications or raw operational evidence are required to read this brief. Traceability is to named source sections, not a claim that the latest canonical working copies were committed here.

| Source | Reviewed record / section |
| --- | --- |
| S1 | `INDEX.md`: Project Goal; Current Development Status; Current next task. |
| S2 | `Design/GAME_DESIGN.md`: release scope; track/signalling/locomotives; Manual Railway Operations Diagram; assistant/tutorials; regional/identity/expansion sections; Open questions. |
| S3 | `Development/PROGRESS_LOG.md`: chronological setup/runtime milestones; current checkpoint; 18 October diagnostic closure and end-of-day track/holiday entry. |
| S4 | `Development/TECHNICAL_ENVIRONMENT.md`: locomotive/track experiments; 3B-4G closure; Track Material Diagnostics, HD v004 and Rendering Research; D2. |
| S5 | `CHANGELOG.md`: approved design revisions and development milestones. |
| S6 | `WORKFLOW.md`, `Development/SPECIALIST_DELEGATION.md`, `CLAUDE.md`: authority, role boundaries and evidence/reporting discipline. |
| S7 | `Reporting/Daily/2026-10-18.md`, `Reporting/HANDOFF_REGISTER.md`: end-of-day reconciliation and explicit Manager dispositions, checked without publishing private provenance. |
| S8 | Track `EXPORT_NOTES_StageC1_HD_v004.md`, retained verification/reimport/manifest and comparison sheets: asset contents, counts and Blender-only limitations. |
| S9 | Black 5 `EXPORT_NOTES_StageC11_Refine_v014.md` and current asset navigation: provisional milestone and outstanding work. |

| Claims | Source mapping |
| --- | --- |
| C01 Project identity/current position | S1, S2 core concept; S3 current/end-of-day checkpoint. |
| C02 Status discipline | S2 status convention; S6 change/reporting rules. |
| C03 Core direction and regional/identity systems | S2 corresponding design sections; S1 overview. |
| C04 Manual operation and education | S2 dedicated diagram and assistant sections; S5 approved revisions. |
| C05 Targets, superseded ideas, later scope | S2 signalling/locomotive/expansion sections; Open questions. |
| C06 Recorded chronology | S3 dated entries; S4/S5 corroboration. |
| C07 Locomotive experiment results and limits | S3 Probe 1/2/3a, inheritance and 9–10 October entries; S4. |
| C08 Track/3B-4G diagnostic closure | S3/S4 dedicated closure; S7 accepted result. |
| C09 Materials and HD v004 | S3 end-of-day entry; S4; S7; S8. |
| C10 LOD/rendering/assets/toolkit | S3/S4 end-of-day and D2 records; S7/S8/S9. |
| C11 Pending work and suspension | S1 current task; S3/S4 checkpoint; S7. |
| C12 Visual shortlist | S7 visual acceptance; S8 filenames and sheets; direct inspection of the two labelled sheets. |

Published information is a curated summary, not independent execution of the historical tests. Runtime observations, local source/editor research, retained validation, Manager acceptance and presentation suitability remain separate evidence categories. Do not invent progress percentages, release dates, completed tasks, final architecture or extra approvals when building a presentation from this brief.
