# Early Locomotion - Technical Environment

Toolchain baseline verified: 19 September 2026

Editor/startup evidence inspected: 26 September 2026

Project generation and first-build results: 20 September 2026, verified by The Manager/user. Build result recorded on 26 September 2026; toolchain versions unchanged.

## Verified Development Target

- Satisfactory: 1.2
- Satisfactory Mod Loader: SML 3.12.0
- Coffee Stain Unreal Engine: 5.6.1-CSS

Current supported pairing:

Satisfactory 1.2 <-> SML 3.12.x <-> Unreal Engine 5.6.1-CSS

Older SML 3.11 / Unreal Engine 5.3 development information must be treated as potentially outdated.

## Verified Installed Setup

The current setup checkpoint records:

- Coffee Stain Unreal Engine 5.6.1-CSS installed.
- `SatisfactoryModLoader` repository cloned successfully.
- `FactoryGame.uproject` associated with 5.6.1-CSS.
- Wwise Authoring and SDK (C++) 2023.1.14.8770 installed.
- Required Wwise deployment targets installed.
- Wwise Unreal integration 2023.1.14.8770.3555 completed.
- Companion Wwise project created.
- SoundBanks regenerated for all platforms with the required metadata fields enabled; the Wwise Windows metadata/platform and Init resource-loading issue is resolved (Manager/user verified 26 September 2026; see resolution below).
- Visual Studio Community 2022 17.14.x installed.
- Required Visual Studio workloads/components selected during installation:
  - .NET Desktop Development;
  - Desktop Development with C++;
  - Game Development with C++;
  - MSVC v143 VS 2022 C++ build tools, including the recorded v14.38-17.8 selection;
  - .NET 8 Runtime;
  - .NET Framework 4.8.1 SDK.
- Windows restarted after Visual Studio installation.
- Visual Studio project generation succeeded on 20 September 2026; `FactoryGame.sln` appeared in the SML repository.
- First FactoryGame **Development Editor / Win64** build succeeded in Visual Studio 2022 on 20 September 2026: **12 succeeded, 0 failed, 0 up-to-date, 0 skipped**; duration **09:44.449**.
- First usable editor launch and FactoryGame environment load completed on 26 September 2026 in 5.6.1-CSS; SML 3.12.0 initialization completed.
- Git available and used successfully for the SML clone and project tracking; exact installed version not recorded.

The exact Visual Studio patch/build is not recorded. The relocated SML checkout HEAD is recorded below. Project generation, FactoryGame Development Editor / Win64 build, editor loading and temporary probe Windows Shipping packaging/deployment are verified. Runtime Probe 1 now verifies the specific construction/rail/input/braking/unpowered-movement behaviour recorded below. The tested implementation's traction-causality result is recorded below; production Early Locomotion implementation and a warning/error-free environment remain unverified. The previous Visual Studio/project-generation blocker is cleared.

### Startup issue evidence — 2026-09-26

Historical initial inspection: the following records the earlier startup evidence, before the later Wwise resolution below. No SoundBanks, engine files, installed components, or dependency versions were changed during that initial read-only inspection.

**Wwise:** Saved/Logs/FactoryGame.log in the SML repository records Wwise SDK 2023.1.14 Build 8770 and successful SoundEngine initialization (lines 707–714), followed by “Current platform Windows not found”, “No JSON Metadata file found” for the configured Windows output, and failed Init Bank resource loading (lines 719–737).

The inspected root is `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\SatisfactoryModLoader_WwiseProject\GeneratedSoundBanks`. Windows exists and contains exactly `Init.bnk` (453 bytes), `Init.txt` (214 bytes), `PlatformInfo.xml` (1480 bytes), `PluginInfo.xml` (337 bytes), and `SoundbanksInfo.xml` (1019 bytes). No JSON files were found anywhere under GeneratedSoundBanks. The other platform directory is Mac, containing the same five filenames; its Init.bnk is 449 bytes. The root also contains ProjectInfo.xml. Windows/SoundbanksInfo.xml identifies the Windows platform and references Init.bnk. Thus the previous successful-generation record is preserved: bank/XML output exists, while the editor's required JSON metadata is absent at the inspected location. The reason for missing JSON and Init resource-load failure remains unresolved; the Init bank itself is not absent.

**Turnkey / AutomationTool:** FactoryGame.log lines 741–765 and `C:\Users\a156b\AppData\Roaming\Unreal Engine\AutomationTool\Logs\C+Program+Files+Unreal+Engine+-+CSS\Log.txt` (exception at line 282) record `System.IO.FileNotFoundException: Could not load file or assembly 'System.Windows.Forms, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'` during Turnkey.SetupVisuals, followed by ExitCode=1. This automatic SDK-detection failure did not prevent editor initialization.

The editor log identifies bundled DotNet SDK 8.0.300 win-x64. Its executable is `C:\Program Files\Unreal Engine - CSS\Engine\Binaries\ThirdParty\DotNet\8.0.300\win-x64\dotnet.exe`. Read-only --list-runtimes reports Microsoft.NETCore.App, Microsoft.AspNetCore.App, and Microsoft.WindowsDesktop.App at 8.0.5. Its WindowsDesktop runtime contains System.Windows.Forms.dll with assembly identity Version=8.0.0.0. `Engine/Binaries/DotNET/AutomationTool/AutomationTool.runtimeconfig.json` specifies net8.0 / Microsoft.NETCore.App 8.0.0.

The separately inspected `C:\Program Files\dotnet\dotnet.exe` reports NETCore runtimes 3.1.32, 6.0.12, 8.0.22, 8.0.31, and 9.0.20; WindowsDesktop runtimes 8.0.22, 8.0.31, and 9.0.20; and AspNetCore runtimes 8.0.31 and 9.0.20. No WindowsDesktop 6.x is listed by either inspected host. This establishes the failed assembly identity and available runtime inventories, not the cause of assembly resolution failure or which installation/repair would fix it. No dependency change is prescribed.

**Scope boundary:** The same editor log also contains other warnings/errors, including SML property-initialization messages (lines 1017–1019). These were not diagnosed in this two-issue inspection and do not establish a new launch blocker. This is not a warning/error-free environment certification.

### Wwise resolution and deferred Turnkey issue — 2026-09-26

The Manager/user verified on 2026-09-26 that JSON metadata existed under GeneratedSoundBanks and Unreal was reading the Windows metadata, but four required fields were missing. In **Wwise Project Settings > SoundBanks > Include in Metadata**, **Object GUID**, **Object Path**, **Max Attenuation**, and **Estimated Duration** were enabled. SoundBanks were regenerated for all platforms, then Unreal was restarted.

WwiseProjectDatabase then reported:

```text
Platform Windows: Using "Generate All Banks Metadata file" is less efficient than Per Bank.
UpdateDataStructure: Done.
```

The previous Windows-platform, missing-metadata, "No data for Init bank", and Init bank resource-loading errors are resolved. The Generate All Banks Metadata efficiency message is advisory, not a blocker.

This later verified result supersedes the unresolved Wwise status in the historical initial inspection above. First successful editor launch and FactoryGame loading remain verified. Turnkey/System.Windows.Forms, Version=6.0.2.0 remains unresolved but deferred because it has not blocked project generation, the FactoryGame build, or editor launch. No dependency/toolchain versions changed. The exact Turnkey cause/remedy remains unverified.

## Active SML Workspace and Probe Preparation — 2026-10-02

- **Canonical project/documentation root:** `C:\Users\a156b\Documents\Satisfactory - Early Locomotion` (unchanged).
- **Active SML development workspace:** `C:\SML`.
- **Unreal project / solution:** `C:\SML\FactoryGame.uproject` / `C:\SML\FactoryGame.sln`; project generation succeeded after relocation.
- **Checkout HEAD before/after:** `d2162c999bbaa9650594ee9ad6e6e06190306009`; tracked Git status and ignored state matched immediately after the move; final tracked working tree clean.
- **EngineAssociation:** `5.6.1-CSS`, unchanged.
- **Development Editor / Win64:** build succeeded at the new path in **488.10 seconds**; FactoryGame/SML loaded and SML 3.12.0 initialized.
- **Temporary probe:** `Mods/EL_ArchitectureProbe` implementation/Blueprint configuration exists; module loaded, `BP_EL_ProbeLocomotive` resolved/opened and native class resolved. Runtime Probe 1 results are recorded below; this is not production gameplay implementation.
- **Blueprint SHA-256 before/after:** `882de775beaa0458924c616e3fb0ca65899b6211f8c165bcbd29096402b99564`.
- **FactoryGame.uproject SHA-256 before/after:** `a4b627b3d11537131f0610c914471db69245018561278cf2a5e508c96aba923b`.
- **Wwise:** integration survived relocation, SoundEngine initialized, and WwiseProjectDatabase reported `UpdateDataStructure: Done.` Companion Wwise project is `C:\SML\SatisfactoryModLoader_WwiseProject\SatisfactoryModLoader_WwiseProject.wproj`; generated output is `C:\SML\SatisfactoryModLoader_WwiseProject\GeneratedSoundBanks`. The configured relative project/output paths remain valid.

**Shipping path limit:** The former root `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader` produced 262-character Shipping action paths. UBT's hard-coded 260-character action-path validation was not bypassed by Windows LongPathsEnabled. Relocation to `C:\SML` removed this blocker; subsequent Shipping packaging succeeded. No toolchain/dependency versions changed.

**Verified Alpakit configuration/result:** Windows client enabled, copy-to-game enabled for `D:\Steam\steamapps\common\Satisfactory`, launch game disabled; Windows Server and Linux Server disabled; advanced settings unchanged/default. Only `EL_ArchitectureProbe` was packaged, using Shipping configuration. Alpakit's backend automation completed with ExitCode **0** in approximately **6 minutes 41 seconds** and deployed the package to the retail game folder. Alpakit did not launch retail Satisfactory during packaging. The later retail Runtime Probe 1 is now completed; see the runtime result below.

The editor build initially encountered a Wwise prebuild PowerShell security-module loading failure. A process-local Windows PowerShell module search path allowed the existing build step to succeed; system policy and dependency versions were not changed. Startup warnings remain; successful package automation does not establish resolution of the separately deferred Turnkey/System.Windows.Forms issue.

Temporary recovery backup: `C:\Users\a156b\Documents\Codex\2026-09-19\referenced-chatgpt-conversation-this-is-an-2\sml-relocation\safety-backup`. It contains the probe and companion Wwise project, is retained pending Manager review, and is not a permanent development tree or canonical source.

## Retail Runtime Probe 1 Result — 2026-10-02

**Evidence:** Manager/user-verified runtime observation and FactoryGame.log analysis; no independent log re-analysis was performed in this documentation task.

The EL Probe Locomotive built normally through the Build Gun; its vanilla locomotive hologram snapped correctly to vanilla railway track. Diagnostic samples consistently showed `HasTrain=true`, `IsDerailed=false` and `HasPower=false`, with `FGLocomotiveMovementComponent` retained. Reverser/throttle inputs changed normally; TrainStatus changed between Parked and ManualDriving. `TractiveEffortPct` and `TractiveForceN` became non-zero, and `ForwardSpeedCmS` rose from standstill. Air and dynamic braking stopped the locomotive. Two separately placed probe locomotives reproduced the result.

**Verified viability:** AFGLocomotive subclassing is runtime-verified viable for construction, vanilla rail attachment, input, braking and unpowered movement in the tested probe. This does not select a final production architecture or establish all vanilla railroad compatibility.

**Presentation/configuration residuals:** Camera could not rotate/look left/right normally, normal locomotive UI was absent, and exiting placed the player partly underneath/intersecting the locomotive. These presentation/configuration residuals remain unresolved but do not currently invalidate the observed traction/rail integration result.

**Historical initial causality uncertainty (before the later control result below):** This does not prove that `SetTractivePowerFactor(1.f)` specifically caused unpowered traction. Vanilla unpowered movement on the same dead track, sufficiency of the probe's no-op `UpdatePower`, and necessity of `SetTractivePowerFactor` remain untested. Final production architecture remains unresolved.

## Runtime Probe 1 Traction-causality Result — 2026-10-02

**Evidence:** Manager/user-verified three-way control; no new source inspection or runtime testing was performed in this documentation task.

1. **Vanilla control:** On deliberately unpowered railway, the Vanilla Electric Locomotive showed No Power; a W throttle attempt produced no movement.
2. **Working EL probe:** With `SetTractivePowerFactor(1.f)` active and `UpdatePower()` a no-op, `HasPower=false` while driver input was accepted, `TractiveEffortPct` and `TractiveForceN` were non-zero, the locomotive accelerated/moved normally, and braking worked.
3. **Single-change EL control:** Only `SetTractivePowerFactor(1.f)` was disabled; `UpdatePower()` remained the same no-op. `HasTrain=true`, `IsDerailed=false` and `HasPower=false` each held for **165/165 samples**. Reverser/throttle input was observed, `TractiveEffortPct` reached **0.340**, and air brake was released during driving attempts. `TractiveForceN` and `ForwardSpeedCmS` remained **0 throughout**.

**Verified conclusion:** Within the currently tested implementation, `SetTractivePowerFactor(1.f)` is necessary for producing unpowered traction; the no-op `UpdatePower()` alone is insufficient. This does not establish the final production locomotive architecture. The result is specific to the current tested implementation, not a claim about every possible unpowered-traction design.

**Historical direction after the causality control (superseded by the wagon test below):** Restore the successful working probe with `SetTractivePowerFactor(1.f)` active and `UpdatePower()` remaining a no-op, then proceed to normal railway-integration tests beginning with vanilla wagon coupling. Record observations before final production architecture selection. Restoration and coupling testing are next actions, not completed milestones. Camera, normal locomotive UI and exit-placement residuals remain unresolved. Coupling and broader integration are not yet verified.

## Runtime Probe 1 Vanilla-wagon Integration — 2026-10-02

**Evidence / completed:** Manager/user-verified runtime observations; not independently repeated in this documentation task. The restored known-good EL Probe Locomotive was tested on the same deliberately unpowered railway. A vanilla Freight Wagon built/snapped directly onto the probe formed a usable consist. The locomotive moved the consist forward and in reverse; normal braking stopped locomotive and wagon cleanly. No derailment or separation was observed during normal movement/braking.

**Verified scope:** AFGLocomotive-derived probe integration with vanilla rolling stock is runtime-verified for normal construction-time consist formation, forward/reverse movement and braking while electrically unpowered. Final production architecture remains unresolved. This establishes the tested construction-time workflow, not every vehicle combination or coupling method.

**Residuals / unresolved:** The temporary probe coupling node/position is visibly misaligned. Driving the probe into an independently placed loose wagon made the train unresponsive to commands. Whether collision-coupling independently placed rail vehicles is a supported vanilla workflow has not been established; this observation is not classified as an architecture failure. Earlier camera, normal locomotive UI and exit-placement residuals remain unresolved.

**Historical direction after the wagon test (before Probe 2a below):** Proceed to station/timetable integration testing using the restored known-good working probe. Record observations before final production architecture selection; station/timetable success is not yet verified.

## Probe 2a Locomotive-power and Timetable Diagnostics — 2026-10-03

**Evidence:** Manager/user-verified runtime log; not independently rerun/reanalysed in this documentation task. `ProbeVariant=PowerDiagnostics2A` ran successfully. Runtime log: `HasPower=false` and `PowerInfoHasPower=false` on all **1,069 samples**. `PowerInfoConnected=true`, `PowerInfoFuseTriggered=false`, `ShoeCircuit=true`, `HasTrain=true` and `IsDerailed=false` throughout.

**Powered railway/stations:** When railway/stations were powered, `ShoeHasPower` changed false -> true while `HasPower` and `PowerInfoHasPower` remained false. Manual forward/reverse traction continued to work.

**Self-driving:** Enabling self-driving set `SelfDrivingEnabled=true`; one tick later `GetSelfDrivingError=SDLE_NoPower`. At that time `ShoeHasPower=true`, both locomotive power flags were false, and `TrainStatus=Self Driving`. Throttle, tractive effort and tractive force were suppressed to zero; air/dynamic braking held the train stationary. Disabling self-driving restored manual traction immediately.

**Verified conclusion:** The timetable/self-driving No Power condition is locomotive-level rather than simply lack of powered third rail. The exact gate remains unresolved because `HasPower` and `PowerInfoHasPower` were always identical in this run. The earlier observation that powering an already-placed probe breaks manual driving did not reproduce in this controlled run and remains unverified. It is not treated as established behaviour or an architecture failure. Final production architecture remains unresolved.

**Historical next test after Probe 2a (completed by Probe 2b below):** Probe 2b: set only the inherited locomotive `mHasPower` state true via verified Unreal property reflection while leaving `PowerInfoHasPower` unchanged, then test self-driving. This is the next planned test, not a verified outcome; do not select final production architecture.

## Probe 2b Logical-power / Self-driving Milestone — 2026-10-03

**Evidence:** Manager/user-verified runtime observations and log result; not independently rerun or reanalysed in this documentation task.

**Single behavioural change:** Server-authoritative reflected write sets inherited AFGLocomotive `mHasPower=true` each tick. `UpdatePower()` remained no-op; `SetTractivePowerFactor(1.f)` remained active. PowerInfo and sliding-shoe behaviour were not modified; no AccessTransformer was used.

**Log verification:** `ProbeVariant=LogicalPower2B` on all **291 periodic samples**; reflection lookup `found=true` on all tested placements. First write changed HasPower false -> true. `HasPower=true` and `PowerInfoHasPower=false` each held for **291/291 samples**. `PowerInfoConnected=true`, `PowerInfoFuseTriggered=false`, `ShoeCircuit=true`, `HasTrain=true` and `IsDerailed=false` throughout. `ShoeHasPower=true` during the temporary powered-track window, but **false during all successful self-driving samples**.

**Self-driving / consist:** `SDLE_NoPower` on **0 samples**. Self-driving produced normal throttle/traction and reached approximately **2,879.3 cm/s (~104 km/h)**. Autopilot reduced throttle, applied braking, approached/stopped at stations, reversed operational direction and departed. Two opposing EL Probe Locomotives received successful reflected writes and participated in multiple-unit behaviour with opposing reverser signs / mirrored force. The train repeatedly travelled between End 1 and End 2 on unpowered railway; the user observed correct station stops, brief dwell/wait and timetable continuation.

**Inference boundary:** A transient `SDLE_StationUnreachable` with one locomotive disappeared after adding the opposing second locomotive. A one-way limitation explanation is inference, not verified causality.

**Proven capability / limit:** In this tested AFGLocomotive-derived probe, logical `mHasPower` satisfies the vanilla self-driving/timetable readiness gate with `HasPower=true`, `PowerInfoHasPower=false` and `ShoeHasPower=false`. Powered third rail and PowerInfoHasPower are not required for the tested timetable operation. Combined with the earlier SetTractivePowerFactor traction control, traction availability and automation readiness can be independently substituted while retaining the tested vanilla train/timetable behaviour. The per-tick reflection write is a **temporary probe mechanism**, not the chosen production implementation. Final production locomotive architecture remains unresolved.

**Remaining production questions:** Correct production logical-readiness state-setting path; `OnHasPowerChanged` side effects; headlights/animation/HUD; replication/client behaviour; save/load; multi-locomotive master/slave details; station docking/loading; vanilla-wagon timetable behaviour; and replacing unconditional true with actual fuel/water/operational steam readiness remain unresolved.

**Next direction:** Return Probe 2b evidence to The Manager and scope the next normal railway-integration checks, including station docking/loading and vanilla-wagon timetable behaviour. Resolve the production readiness/state-setting questions through separate verified work before final architecture selection; no new runtime test or production implementation is claimed here.

## Probe 2b Station Docking and Vanilla Freight-wagon Compatibility — 2026-10-03

**Evidence:** Verified user runtime observations using the existing LogicalPower2B build. This documentation task did not repeat the tests or independently inspect new logs; no new sample counts are claimed.

**Consist:** EL Probe Locomotive / vanilla Freight Wagon / EL Probe Locomotive, with the two locomotives facing opposite directions.

**Test 1 — Unpowered railway / basic timetable:** Using the existing Probe 2b / LogicalPower2B build, an EL Probe Locomotive–vanilla Freight Wagon–EL Probe Locomotive consist, with opposing locomotives, self-drove on unpowered railway, reached/stopped at both stations, reversed route direction and returned normally. Adding the vanilla Freight Wagon did not break timetable operation.

**Test 2 — Station docking without power:** With stations unpowered, vanilla docking/loading did not operate. Train movement and timetable operation remained available through Probe 2b logical locomotive readiness; station machinery remained unavailable.

**Test 3 — Station powered:** Powering station infrastructure allowed normal vanilla docking, correct wagon positioning, correct cargo loading, successful item transport and continuing timetable operation.

**Interpretation:** Runtime evidence separates locomotive/train movement and timetable readiness without powered third rail from vanilla station docking/cargo machinery, which still requires station power. The user confirms the intended custom stations will have their own power connections while railway track will not distribute traction power; this is recorded as user-confirmed direction, not proof of custom station implementation or an independent design/Open Question decision.

**Limit:** This verifies vanilla station power behaviour, vanilla Freight Wagon timetable compatibility and vanilla cargo docking/loading compatibility with the current probe only. Custom Early Locomotion stations, servicing, coal/water handling, custom dwell behaviour, custom station power logic and final station architecture remain unimplemented/unresolved. The reflected logical-power write remains a temporary probe mechanism. Final production locomotive architecture and all design Open Questions remain unresolved.

**Next direction:** Return the completed vanilla-wagon timetable and powered-station docking/loading evidence to The Manager for selection of the next scoped production-readiness or railway-integration test. Final locomotive/station architecture remains unresolved; no further experiment is selected by this documentation task.

## Probe 3a Dynamic Steam Readiness — 2026-10-03

**Evidence:** Verified user runtime observations using `ProbeVariant=SteamReadiness3A`; the same locomotive was tested without rebuilding. This documentation task did not independently inspect new logs/source or repeat the test.

**Ready true — `EL.SteamReady 1`:** Manual forward/reverse movement worked on unpowered rail. Timetable/self-driving worked and the train travelled back and forth normally.

**Ready false — `EL.SteamReady 0`:** Manual traction became unresponsive; timetable/UI reported "No Power". Applying electrical rail power did not restore locomotive operation.

**Ready restored — `EL.SteamReady 1`:** Locomotive operation returned without rebuilding.

**Interpretation:** The tested mod-owned steam-readiness state dynamically controls both traction availability and vanilla logical/timetable readiness. Rail electrical power does not bypass `SteamReady=false`. This is runtime evidence supporting the candidate AFGLocomotive-derived steam architecture, not selection of final production architecture.

**Limits:** The current component contains only a temporary readiness boolean. Reflection is not selected as the production `mHasPower` setter. Coal/water/boiler gameplay is not implemented; save/load and multiplayer are not verified. Production state-setting and its side effects remain unresolved. No design Open Question is resolved by this result.

## Stage C v002 and Vanilla BP_Locomotive Inheritance Probe — Recorded 2026-10-03

**Evidence:** Manager/user-verified runtime results supplied for this reconciliation; no runtime retest or independent source/log inspection was performed here. No sample counts or exact event times are inferred.

**Stage C v002:** Stage C v002 Yellow Pannier imported/deployed successfully and appeared in retail with credible player scale, visual centring on vanilla railway and corrected boiler/firebox/cab geometry. Exit placed the player beside the locomotive. The new v002 locomotive dismantled without crash; the previous dismantle crash stopped after non-null materials were assigned/saved. Vanilla monorail geometry intersects the conventional running gear, accepted for temporary probe use. The custom AEL_ProbeLocomotive camera remained locked.

**Camera diagnostics:** While the custom probe was possessed and the user moved the mouse, ControlRotation did not change; Actor, SpringArm, Camera and final view remained static. This is evidence of missing upstream vanilla look/possession behaviour rather than merely an FOV or spring-arm setting problem; the exact missing path remains unverified.

**Vanilla Blueprint inheritance:** A new mod Blueprint parented directly to vanilla BP_Locomotive cooked/packaged and built successfully in retail. Normal camera look-around, locomotive HUD, horn/sounds and exit worked. On powered rail it behaved as a normal controllable vanilla locomotive. After removing rail power, HUD/sounds remained available but "No Power" appeared and traction/control were unavailable. Dismantling completed without crash.

**Dated correction — recipe exposure:** The recipe required cheats to expose. Correct sequence: `SML.ForceAllowCheats 1`, then `EnableCheats`, then `UnlockSpecificRecipe ...`. The earlier claim that `UnlockSpecificRecipe` alone had been verified is retracted. The ellipsis is a recipe-argument placeholder; no exact recipe identifier was supplied in this evidence.

**Interpretation:** The inheritance experiment is a STRONG PASS for technical feasibility of preserving vanilla presentation/possession behaviour through a mod Blueprint parented to BP_Locomotive. It supports further component-based steam-adapter experimentation, not approval or selection of production architecture.

**Limits:** Final architecture and the production mHasPower setter remain unresolved. SaveGame persistence remains unverified; singleplayer save/load remains mandatory for Core. Multiplayer remains deferred post-release. Inherited electric HUD/VFX presentation still requires assessment. The inheritance test did not verify steam readiness/traction substitution in that Blueprint. No gameplay/design change or Open Question resolution.

**Next direction:** Return the Stage C v002, camera diagnostic and BP_Locomotive inheritance evidence to The Manager for review and scoping of further component-based steam-adapter experimentation. Retain the verified presentation/possession baseline while assessing production readiness/state-setting options. No final architecture or next implementation mechanism is selected by this documentation task.

## End-of-day Technical Supplement — Recorded 2026-10-03

Additional Manager-supplied evidence: Stage A/B/B.1 Yellow Pannier dimensions/reference limitations and export work; Stage C animation/pivot/collision limits; initial dismantle crash in UFGMaterialEffectComponent::InitializeMaterials with None static-mesh material interfaces and successful new/older/v002 dismantling after saved/assigned non-null prototype materials; unsuccessful use_pawn_control_rotation camera fix; and source-confirmed UFGCheatManager Exec/cheat-enabling behaviour. Null materials remain the strong leading cause, not absolute private-source proof. These details were not independently re-inspected here. See [daily report](DAILY_REPORT_2026-10-03.md) for the concise evidence, limitations and restart checkpoint.

## Important Compatibility Notes

- Do not use stock Unreal Engine from the Epic Games Launcher as a replacement for the Coffee Stain custom engine.
- Satisfactory 1.2 / SML 3.12 uses Unreal Engine 5.6.1-CSS.
- Older mods built for SML 3.11 / Unreal Engine 5.3 are not binary-compatible with the current environment.
- SML 3.12 uses newer Unreal build settings.
- Full include paths may be required in module source files.
- Satisfactory has increased use of TObjectPtr<>.
- FGGameFeatureData requirements changed in the SML 3.12 generation.
- Enhanced Input integration changed from older versions.
- Visual Studio 2022 is currently the required Visual Studio generation for this toolchain.

## Verified Relevant Railroad Classes

Current public Satisfactory headers include:

- AFGRailroadVehicle
- AFGLocomotive
- AFGBuildableRailroadTrack
- AFGBuildableRailroadSignal
- AFGBuildableRailroadStation
- AFGRailroadSubsystem

These indicate that Early Locomotion may be able to reuse parts of Satisfactory's existing railroad graph, train, station, and signalling systems.

AFGLocomotive is designed around vanilla electric / third-rail power and should not automatically be assumed to be the correct base class for steam locomotives.

The final steam locomotive architecture is unresolved.

## Railway Reconnaissance Status — 2026-09-26

The Manager/user confirms that Claude Code completed read-only railway header/API reconnaissance. Local FactoryGame Private `.cpp` implementations are generated stubs, so runtime behaviour could not be verified from source.

The Manager/user additionally reports that Claude verified headers exposing locomotive power state, tractive power factor, third-rail power connection, and related interfaces. These declarations do not prove runtime traction behaviour. Retail Satisfactory is installed at `D:\Steam\steamapps\common\Satisfactory`.

The previous header/system checklist is retained as a reference, not a pending next task; no new exact API signatures or per-header findings are asserted here:

- FGRailroadVehicle.h
- FGLocomotive.h
- FGRailroadSubsystem.h
- FGBuildableRailroadTrack.h
- FGBuildableRailroadSignal.h
- FGBuildableRailroadStation.h
- FGBuildableRailroadAttachment.h
- FGBuildableRailroadSwitchControl.h
- FGBuildableTrainPlatform.h
- FGBuildableTrainPlatformCargo.h
- railroad vehicle movement component classes
- locomotive movement component classes
- train composition / timetable classes

## Unreal MCP / AI Editor Integration

Do not currently depend on official Unreal MCP integration for Early Locomotion.

The official Epic Unreal MCP tooling targets newer Unreal versions than the current Satisfactory 5.6.1-CSS environment.

Any third-party MCP/editor integration must be tested separately before it becomes part of the development workflow.

## Current Release Scope and Prepared Multiplayer Diagnostic

Agreed: Core 1.0 / the first public release prioritises a complete, robust singleplayer experience. Multiplayer support is deferred to a post-release update and is not a Core release requirement or blocker. Listen-server, dedicated-server, client replication and multiplayer-specific UI/presentation validation are deferred.

Agreed: singleplayer persistence and save/load correctness remain Core requirements. Multiplayer replication and multiplayer save/session semantics are separate, deferred post-release questions; their technical answers remain Open Question.

`ProbeVariant=LogicalPower2B_NetDiag` exists as prepared diagnostic capability according to the Manager/user. It has not been runtime-tested. Multiplayer runtime testing is deferred post-release and is not required before continuing singleplayer architecture work. This records the user-verified preparation report, not independent build/source inspection or runtime evidence.

## Repository Infrastructure — Verified 2026-10-04

The canonical documentation/asset repository has infrastructure checkpoint `e1eb43e2785884a1e8d8f563a3307e70214db25e` on `master`. It contains narrow shared ignore rules, asset workspace/helper guidance and current specialist handoffs. Local Git inspection confirms no remote and no LFS-tracked files; `.gitattributes` and `.lfsconfig` are absent. Installed Git LFS does not mean this repository uses LFS. Publication, final binary-storage policy and historical installer removal from Git history remain separate decisions. No SML/toolchain/dependency versions changed. Asset/reference bulk is local and untracked; Blender milestone reports are documented in PROGRESS_LOG, not promoted here into fresh environment/runtime verification.

## Current Unknowns

The following still require verification:

- exact installed Visual Studio patch/build and component inventory, if needed for diagnosis
- production logical-readiness state-setting path and OnHasPowerChanged side effects
- headlights/animation/HUD effects, actual steam fuel/water/boiler/operational readiness beyond the verified temporary boolean, and multi-locomotive master/slave details
- earlier powering-related manual-drive failure, not reproduced in Probe 2a
- railroad movement beyond the tested probe and custom station servicing, coal/water handling, dwell behaviour and power logic
- coupling-node alignment and whether collision-coupling independently placed loose vehicles is supported vanilla workflow
- custom AEL probe upstream look/possession behaviour and normal locomotive UI; inheritance probe camera/HUD/exit passed, and v002 exit placement passed
- inherited electric HUD/VFX suitability and integration of steam readiness into the vanilla Blueprint-derived candidate
- save/load behavior needed for custom steam state
- deferred post-release: multiplayer replication/client prediction, listen/dedicated-server behaviour, multiplayer UI/presentation and multiplayer save/session semantics
- best inheritance architecture for steam locomotives
- feasibility of custom conventional track using the vanilla railroad graph
- exact monorail conversion implementation

## Current Next Technical Step

Next session: The Manager first scopes the exact component-based steam-adapter/hook test against documented evidence. Then run an isolated BP_Locomotive-derived test Blueprint experiment with UEL_SteamStateComponent and a native steam adapter candidate, aiming to preserve vanilla camera/HUD/menu/horn/possession while reproducing Probe 3a SteamReady-controlled traction and logical readiness. This is experimental, not selected production architecture. See Development/DAILY_REPORT_2026-10-03.md.

The inheritance experiment is a STRONG PASS for technical feasibility of preserving vanilla presentation/possession behaviour through a mod Blueprint parented to BP_Locomotive. It supports further component-based steam-adapter experimentation, not approval or selection of production architecture. Final architecture and the production mHasPower setter remain unresolved. SaveGame persistence remains unverified; singleplayer save/load remains mandatory for Core. Multiplayer remains deferred post-release. Inherited electric HUD/VFX presentation still requires assessment. The inheritance test did not verify steam readiness/traction substitution in that Blueprint.

Probe 3a (`ProbeVariant=SteamReadiness3A`) completed successfully from verified user runtime observations on the same EL Probe Locomotive without rebuilding. With `EL.SteamReady 1`, manual forward/reverse movement and timetable/self-driving worked on unpowered rail, with normal back-and-forth travel. With `EL.SteamReady 0`, manual traction became unresponsive and timetable/UI reported "No Power"; applying electrical power to the rail did not restore operation. Reissuing `EL.SteamReady 1` restored operation without rebuilding. The tested mod-owned steam-readiness state dynamically controls both traction availability and vanilla logical/timetable readiness. Rail electrical power does not bypass `SteamReady=false`. This is runtime evidence supporting the candidate AFGLocomotive-derived steam architecture, not selection of final production architecture. The current component contains only a temporary readiness boolean. Reflection is not selected as the production `mHasPower` setter. Coal/water/boiler gameplay is not implemented; save/load and multiplayer are not verified.

Probe 2b (`LogicalPower2B`) completed successfully: server-authoritative reflected writes set inherited `mHasPower=true`, while `UpdatePower()` remained a no-op and `SetTractivePowerFactor(1.f)` remained active. All 291 periodic samples showed `HasPower=true` and `PowerInfoHasPower=false`; successful self-driving occurred with `ShoeHasPower=false` and no `SDLE_NoPower` samples. Two opposing probe locomotives repeatedly ran the timetable between End 1 and End 2, with station stops, brief dwell, direction reversal and departure. In the tested probe, logical mHasPower satisfies the vanilla self-driving/timetable readiness gate without powered third rail or PowerInfoHasPower. Together with the earlier traction control, this demonstrates independently substitutable traction availability and automation readiness while retaining tested vanilla train/timetable behaviour. The per-tick reflected write is a temporary probe mechanism, not selected production implementation; final architecture remains unresolved. Correct production logical-readiness state-setting path; `OnHasPowerChanged` side effects; headlights/animation/HUD; replication/client behaviour (deferred post-release); singleplayer save/load (Core requirement); multi-locomotive master/slave details; custom station implementation; and replacing unconditional true with actual fuel/water/operational steam readiness remain unresolved. Other integration unknowns include track CanConnectTo and other vehicle combinations/coupling methods.

Using the existing Probe 2b / LogicalPower2B build, an EL Probe Locomotive–vanilla Freight Wagon–EL Probe Locomotive consist, with opposing locomotives, self-drove on unpowered railway, reached/stopped at both stations, reversed route direction and returned normally. Adding the vanilla Freight Wagon did not break timetable operation. Unpowered stations did not operate the vanilla docking/loading procedure. After powering station infrastructure, docking operated normally, the wagon was positioned correctly, cargo loaded correctly, items were transported successfully and timetable operation continued. Runtime evidence separates locomotive/train movement and timetable readiness without powered third rail from vanilla station docking/cargo machinery, which still requires station power. The user confirms the intended custom stations will have their own power connections while railway track will not distribute traction power; this is recorded as user-confirmed direction, not proof of custom station implementation or an independent design/Open Question decision. This verifies vanilla station power behaviour, vanilla Freight Wagon timetable compatibility and vanilla cargo docking/loading compatibility with the current probe only. Custom Early Locomotion stations, servicing, coal/water handling, custom dwell behaviour, custom station power logic and final station architecture remain unimplemented/unresolved.

Do not begin major gameplay implementation until:

1. Visual Studio project generation succeeds (completed 20 September 2026);
2. the SML development environment builds successfully (FactoryGame Development Editor / Win64 completed 20 September 2026);
3. Unreal Editor launches and the FactoryGame project loads successfully (completed 26 September 2026; Wwise metadata issue resolved, Turnkey issue deferred);
4. the relevant railroad headers are inspected locally (read-only reconnaissance completed, Manager/user confirmed 26 September 2026);
5. runtime baseline experiments establish the behaviour needed for architecture selection;
6. locomotive/track architecture has been reviewed against the real APIs and runtime evidence (unresolved).

## Sources Used During Reconnaissance

Primary sources included:

- satisfactorymodding/SatisfactoryModLoader GitHub repository
- SML 3.12.0 release notes
- satisfactorymodding/Documentation GitHub repository
- current FactoryGame.uproject
- official Unreal Engine documentation

Archived project conversations are not authoritative for current technical environment facts.
