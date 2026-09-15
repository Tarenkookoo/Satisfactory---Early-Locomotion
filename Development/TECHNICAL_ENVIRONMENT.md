# Early Locomotion - Technical Environment

Last verified: 14 September 2026

## Verified Development Target

- Satisfactory: 1.2
- Satisfactory Mod Loader: SML 3.12.0
- Coffee Stain Unreal Engine: 5.6.1-CSS

Current supported pairing:

Satisfactory 1.2 <-> SML 3.12.x <-> Unreal Engine 5.6.1-CSS

Older SML 3.11 / Unreal Engine 5.3 development information must be treated as potentially outdated.

## Required Windows Software

Current research indicates the development environment requires:

- Visual Studio 2022 Community
- .NET Desktop Development workload
- Desktop Development with C++
- Game Development with C++
- MSVC v143 VS 2022 C++ build tools
- .NET 8 Runtime
- .NET Framework 4.8.1 SDK
- Git
- GitHub account
- Access to the Satisfactory Modding custom Unreal Engine
- Wwise integration

The exact required Wwise version is still unresolved and must be verified before installation.

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

## Headers / Systems To Inspect Once Development Environment Exists

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

- exact required Wwise version
- exact Coffee Stain engine release / branch to install
- final installation method for the custom engine
- concrete railroad movement component classes
- train composition / timetable class details
- save/load behavior needed for custom steam state
- multiplayer replication design for steam systems
- best inheritance architecture for steam locomotives
- feasibility of custom conventional track using the vanilla railroad graph
- exact monorail conversion implementation

## Current Next Technical Step

Obtain access to the Satisfactory Modding custom Unreal Engine repository.

Do not begin major gameplay implementation until:

1. the correct engine is installed;
2. the SML development environment builds successfully;
3. the relevant railroad headers are available locally;
4. locomotive architecture has been reviewed against the real APIs.

## Sources Used During Reconnaissance

Primary sources included:

- satisfactorymodding/SatisfactoryModLoader GitHub repository
- SML 3.12.0 release notes
- satisfactorymodding/Documentation GitHub repository
- current FactoryGame.uproject
- official Unreal Engine documentation

Archived project conversations are not authoritative for current technical environment facts.
