# Early Locomotion - Technical Environment

Last verified: 19 September 2026

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
- SoundBanks generated successfully.
- Visual Studio Community 2022 17.14.x installed.
- Required Visual Studio workloads/components selected during installation:
  - .NET Desktop Development;
  - Desktop Development with C++;
  - Game Development with C++;
  - MSVC v143 VS 2022 C++ build tools, including the recorded v14.38-17.8 selection;
  - .NET 8 Runtime;
  - .NET Framework 4.8.1 SDK.
- Windows restarted after Visual Studio installation.
- Git available and used successfully for the SML clone and project tracking; exact installed version not recorded.

The exact Visual Studio patch/build and exact SML checkout commit are not recorded. The blank FactoryGame/SML environment has not yet been confirmed to generate, build, or open successfully.

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

Generate Visual Studio project files from:

`C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject`

Success at this step means generation completes without errors and `FactoryGame.sln` is created. It does **not** establish that the project builds successfully.

Do not begin major gameplay implementation until:

1. Visual Studio project generation succeeds;
2. the SML development environment builds successfully;
3. Unreal Editor launches successfully;
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
