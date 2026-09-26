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

The exact Visual Studio patch/build and exact SML checkout commit are not recorded. Visual Studio project generation and the FactoryGame Development Editor / Win64 build are confirmed. Unreal Editor launch and FactoryGame environment load are confirmed. Early Locomotion implementation, packaging, runtime behaviour, and a warning/error-free environment remain unverified. The previous Visual Studio/project-generation blocker is cleared.

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

## Headers / Systems To Inspect After Project Generation and Build Setup

Before deciding the locomotive architecture, inspect:

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

## Current Unknowns

The following still require verification:

- exact SML checkout commit
- exact installed Visual Studio patch/build and component inventory, if needed for diagnosis
- concrete railroad movement component classes
- train composition / timetable class details
- save/load behavior needed for custom steam state
- multiplayer replication design for steam systems
- best inheritance architecture for steam locomotives
- feasibility of custom conventional track using the vanilla railroad graph
- exact monorail conversion implementation

## Current Next Technical Step

Inspect the real local SML/FactoryGame railway APIs and headers in `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader` and prepare an architecture assessment before any Early Locomotion gameplay implementation.

Assess viable options for locomotive inheritance; railroad vehicle movement; steam power/fuel replacement versus vanilla third-rail behaviour; track integration; train composition/timetable handling; signalling; stations/platforms; save/load; replication/multiplayer; and compatibility with the vanilla railroad graph/subsystem. Report evidence, constraints, and options to The Manager; do not select an architecture in this documentation task.

Do not begin major gameplay implementation until:

1. Visual Studio project generation succeeds (completed 20 September 2026);
2. the SML development environment builds successfully (FactoryGame Development Editor / Win64 completed 20 September 2026);
3. Unreal Editor launches and the FactoryGame project loads successfully (completed 26 September 2026; Wwise metadata issue resolved, Turnkey issue deferred);
4. the relevant railroad headers are inspected locally;
5. locomotive architecture has been reviewed against the real APIs.

## Sources Used During Reconnaissance

Primary sources included:

- satisfactorymodding/SatisfactoryModLoader GitHub repository
- SML 3.12.0 release notes
- satisfactorymodding/Documentation GitHub repository
- current FactoryGame.uproject
- official Unreal Engine documentation

Archived project conversations are not authoritative for current technical environment facts.
