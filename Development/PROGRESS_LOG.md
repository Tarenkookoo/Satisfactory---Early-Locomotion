# Early Locomotion - Progress Log

## Current Checkpoint

**Date:** 2026-10-03
**Phase:** Probe 2a power/timetable diagnostics completed; Probe 2b power-gate isolation next
**Status:** Manager/user-verified PowerDiagnostics2A runtime log records 1,069 samples with HasPower=false and PowerInfoHasPower=false. Powered shoe contact did not clear the locomotive-level self-driving No Power condition; manual forward/reverse traction remained functional and returned immediately when self-driving was disabled. The timetable/self-driving No Power condition is locomotive-level rather than simply lack of powered third rail. The exact gate remains unresolved because `HasPower` and `PowerInfoHasPower` were always identical in this run. Prior Probe 1 traction-causality and construction-time vanilla-wagon results remain verified.
**Current blocker:** Self-driving reports SDLE_NoPower and suppresses traction despite powered shoe contact. The exact locomotive-level gate needs Probe 2b isolation. Earlier powering-related manual-drive failure did not reproduce and remains unverified. Coupling alignment, loose-wagon workflow, camera/UI/exit residuals and deferred Turnkey remain unresolved.
**Implementation status:** The temporary non-production EL_ArchitectureProbe now has verified normal construction-time vanilla wagon consist formation, forward/reverse movement and braking without railway power. Final production architecture and gameplay implementation remain unresolved; save/load, multiplayer and other untested integration areas remain unverified.

Earlier chronological entries remain historical records of what was known at the time. The Claude/Blender asset capability experiment remains paused; its existing outputs are preserved.

### Current Environment

| Item | Recorded version / selection | Status at checkpoint |
| --- | --- | --- |
| Satisfactory | 1.2 | Agreed development target |
| Satisfactory Mod Loader | SML 3.12.0; pairing uses 3.12.x | Recorded target; relocated checkout HEAD `d2162c999bbaa9650594ee9ad6e6e06190306009` |
| Coffee Stain Unreal Engine | 5.6.1-CSS | User reported installed; FactoryGame.uproject engine association confirmed in conversation |
| Audiokinetic Launcher | Version not recorded | Used for Wwise installation and integration |
| Wwise Authoring and SDK (C++) | 2023.1.14.8770 | Installation completed |
| Wwise Unreal integration | 2023.1.14.8770.3555 | Integration completed; .3555 is the integration revision |
| Wwise deployment targets | Linux; Microsoft > Windows > Visual Studio 2019, Visual Studio 2022, Game Core | Selection confirmed before successful installation |
| Visual Studio Community | 2022, 17.14.x channel | Installation completed; Windows restarted; exact installed patch unconfirmed |
| MSVC | v143, x64/x86 build tools, v14.38-17.8 | Required component was selected during the completed Visual Studio installation |
| .NET | 8.0 Runtime (Long Term Support); .NET Framework 4.8.1 SDK | Required components were selected during the completed Visual Studio installation |
| Git | Exact installed version not recorded | Used successfully for project tracking and SML clone |

Visual Studio workloads selected during the completed installation: **.NET desktop development**, **Desktop development with C++**, and **Game development with C++**. Windows was restarted afterward. The selections are recorded as verified progress; exact component patch/build details have not been independently inventoried in this log.

### Project Locations

- Project/design master: `C:\Users\a156b\Documents\Satisfactory - Early Locomotion`
- Separate SML development environment: `C:\SML`
- Unreal project: `C:\SML\FactoryGame.uproject`
- Companion Wwise project: `SatisfactoryModLoader_WwiseProject\SatisfactoryModLoader_WwiseProject.wproj`, under the SML checkout as described in the setup conversation.

Keep the design/project repository separate from the SML development environment.

### Exact Next Action

Probe 2b: set only the inherited locomotive `mHasPower` state true via verified Unreal property reflection while leaving `PowerInfoHasPower` unchanged, then test self-driving. This is the next planned test, not a verified outcome; do not select final production architecture.

### Remaining Milestones

- Probe 2b isolation of locomotive mHasPower versus PowerInfoHasPower for self-driving.
- Successful station/timetable operation and broader railway integration before final architecture assessment.
- Coupling alignment, loose-wagon workflow support, camera/UI/exit residuals, track connectivity, save/load and replication remain unverified/unresolved; Turnkey remains deferred.

### Documentation Reconciliation

Local documentation reconciliation and placement are complete, including restoration of INDEX.md to the project root. The Manager confirmed removal of the obsolete Git installer and empty encoded wrapper folder.

Project Operations (Local) is established inside the ChatGPT Project and has verified local repository access. Project Operations (Cloud) remains available for cloud/project-source work.

The completed documentation/design batch was committed as `eda2873` (Canonicalize railway assistant design and sync project docs), and the repository was confirmed clean afterward. The project-generation checkpoint is preserved alongside the first-build record below; the successful-build documentation was committed as `f5c0035`. The editor-launch and Wwise-resolution documentation checkpoint was committed as `7102365`. The reconnaissance reconciliation and CLAUDE.md state correction were committed as `42d878c` — Record railway reconnaissance and next experiments.

## Chronological History

Entries below are oldest first. Dates reflect conversation evidence; where individual events were only summarized later, that limitation is explicit.

### Before 2026-09-19 - Project Preparation

- The project/design repository was established separately from the future SML development environment.
- Git was set up; `CLAUDE.md` and canonical design/reference files were in place. Claude's onboarding and initial technical reconnaissance were reported complete.
- On 2026-09-15, instructions were given to create and commit `Development/TECHNICAL_ENVIRONMENT.md`. The user subsequently reported “nothing to commit”; the conversation treated the technical-reference checkpoint as completed and clean.
- Recorded target: Satisfactory 1.2 / SML 3.12.0 / Coffee Stain Unreal Engine 5.6.1-CSS. Exact Wwise version was still unresolved at that stage.
- Next setup requirement was custom-engine access through Epic Games/GitHub linking and the Satisfactory Modding Unreal Linker. Steam ownership of Satisfactory was separate from engine-source access.
- No gameplay implementation or locomotive architecture decision was completed.

### 2026-09-19 - Custom Engine and SML Starter Project

**Completed:** User reported “unreal is installed, so we're at step 7.” The SML starter repository was cloned into the separate `SatisfactoryModding\SatisfactoryModLoader` folder. The conversation subsequently confirmed `FactoryGame.uproject` uses `5.6.1-CSS`.

**Errors and resolutions:**

- A repeated clone attempt produced: `fatal: destination path '.\SatisfactoryModLoader' already exists and is not an empty directory`. The existing clone was retained; no deletion or replacement was needed.
- Repository status was attempted from `C:\Users\a156b\Documents\SatisfactoryModding`, outside the cloned repository. The fix was to change into the full `SatisfactoryModLoader` path and run `git status` there. The user then confirmed “that worked.”

**Evidence limit:** Exact clone commit, engine release asset, installation method, and individual account-linking completion times were not recorded in the recovered setup sequence.

### 2026-09-19 - Resolve Wwise Version and Install

**Initial findings:** The check for `C:\Program Files (x86)\Audiokinetic` returned no folder. Searches in the starter project confirmed Wwise references but did not reveal its exact required version. Early documentation lookups exposed unresolved placeholders such as `{wwise-version-full}`.

**Resolution:** The later conversation resolved the required version to **2023.1.14.8770**. In the Audiokinetic Launcher, the filter was changed from **Latest** to **All**, major **2023.1** was selected, and the required version was chosen. The initially offered **2025.1.11.9262** was not used as the setup target.

**Completed:** Wwise installation succeeded with Authoring, SDK (C++), Linux, and the Windows deployment selections listed above. Optional Wwise plug-ins were instructed to be deselected before installation; no separate final plug-in inventory was recorded.

**Clarification:** The Linux selection was a Wwise deployment target for server support, not installation of a Linux desktop operating system. The Wwise Visual Studio deployment selections did not establish that the full Visual Studio compiler/IDE was installed.

### 2026-09-19 - Wwise Integration and SoundBanks

**Problem:** The Wwise Project field referred to a project that did not yet exist, producing **“Please select a valid Wwise project”**.

**Resolution:** Clear the Wwise Project field so the launcher creates a new companion project. The displayed integration version **2023.1.14.8770.3555** retained the required Wwise base version.

**Completed:** The conversation recorded successful integration into `FactoryGame.uproject`, creation of the companion Wwise project, and subsequent completion of the Wwise steps. The SoundBank action was **Generate SoundBank(s) for all platforms** from the top-level SoundBanks folder. Later summaries explicitly recorded SoundBanks generated successfully.

**Evidence limit:** “Completed with message(s)” was described as an expected possible message, not transcribed as the user's actual result. The full SoundBank output was not preserved in the retrieved text.

### 2026-09-19 - Visual Studio Project Generation Failed

**Attempt:** Generate Visual Studio project files for `FactoryGame.uproject`.

**Reported error:**

> Visual Studio 2022 x64 must be installed in order to build this target.

**Diagnosis:** Visual Studio Code was present, but it was not the required Visual Studio 2022 compiler/IDE. The subsequent installer search did not find the installed toolchain.

**Resolution underway:** Install Visual Studio Community 2022 with the required workloads and components. A successful retry has not yet been recorded.

### 2026-09-19 - Locate Correct Visual Studio Installer

**Problem:** Microsoft download routes repeatedly led to Visual Studio Community 2026, including an installer offering that generation. The older-downloads / Dev Essentials route did not immediately produce the required installer.

**Resolution:** Use the Visual Studio 2022 release-history page's **Evergreen bootstrappers**, **Current / 17.14 / Community** entry. The conversation subsequently confirmed the correct **Visual Studio Community 2022** installer and all three workloads selected.

**Component checkpoint:** .NET 8.0 Runtime was already checked; instructions were given to check MSVC v143 **v14.38-17.8** and **.NET Framework 4.8.1 SDK**. The MSVC “Out of Support” label was expected in this recorded setup. The separate Spectre-mitigated libraries were not selected as an additional requirement.

**Stopped at:** Installation in progress. The user said they were waiting, then switched to organizing project continuity logs. Restart, successful regeneration, first build, and editor launch remain unconfirmed.

### 2026-09-19 - Establish Persistent Work Log

**Agreed:** Keep `CHANGELOG.md` for meaningful project/design/implementation changes and `Development/PROGRESS_LOG.md` for factual work history, errors, resolutions, and the current development checkpoint. Put Claude memory transfer on hold while organizing these logs.

**Completed in this documentation task:** Created this initial progress log from the referenced conversation and checked the local project documentation for terminology and conflicts. No software installation, toolchain repair, project generation, build, or gameplay work was performed by this documentation task.

### 2026-09-19 - Visual Studio Installation Completed and Windows Restarted

**Completed:** The Manager/user verified that Visual Studio Community 2022 17.14.x finished installing with the required workloads/components selected, and that Windows was restarted afterward.

**Historical context preserved:** The earlier project-generation attempt failed because Visual Studio 2022 x64 was not installed at that time. That failure remains recorded above and has not been rewritten.

**Verification boundary:** A new project-generation attempt has not yet been recorded. `FactoryGame.sln` generation, the first FactoryGame build, and Unreal Editor launch remain pending.

**Exact next action:** Generate Visual Studio project files from `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject`. Success means `FactoryGame.sln` is created without errors; it does not mean the project has built successfully.

### 2026-09-19 - End-of-Session Documentation and Local Operations Checkpoint

**Completed:** The Manager confirmed completion of local documentation reconciliation and repository cleanup: the obsolete Git installer and empty encoded wrapper folder were removed, INDEX.md was restored, and reconciled project documents were placed correctly. Project Operations (Local) completed its read-only bootstrap, read the seven core files, verified local access, and confirmed a clean project repository. It is established inside the ChatGPT Project; Project Operations (Cloud) remains available for cloud/project-source work.

**Environment:** Satisfactory target 1.2; SML target 3.12.0 / 3.12.x pairing; Coffee Stain Unreal Engine 5.6.1-CSS installed; SML repository cloned successfully; FactoryGame.uproject associated with 5.6.1-CSS. Wwise 2023.1.14.8770 is installed, integration 2023.1.14.8770.3555 completed, the companion project created, and SoundBanks generated successfully. Visual Studio Community 2022 is installed with required workloads/components selected, and Windows restarted. These are The Manager's verified setup facts; no new exact patch or component inventory verification is claimed.

**Files changed:** Development/PROGRESS_LOG.md records this checkpoint; INDEX.md records concise documentation/local operations status; CHANGELOG.md records the documentation/workflow milestone. Development/TECHNICAL_ENVIRONMENT.md already contains the verified technical facts and remains unchanged.

**Verification:** Git status confirmed the local project repository was clean before these edits. Prior historical entries and maintenance rules are preserved. These end-of-session edits remain uncommitted. Cleanup completion is recorded from The Manager's report; cleanup was not repeated in this task.

**Attempted / incomplete:** The next project-generation attempt has NOT been performed. Successful project generation, first FactoryGame build, and Unreal Editor launch remain pending. No Early Locomotion gameplay implementation has started.

**Current blocker:** No setup blocker is recorded; project-generation results remain pending.

**Exact next action:** Open C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader, right-click FactoryGame.uproject, and select **Generate Visual Studio project files**. Success requires generation without errors and FactoryGame.sln appearing in that folder. This proves project generation only, not a successful build. If generation fails, capture the full error; do not change engine, Wwise, Visual Studio, SML, or dependency versions as a speculative fix.

### 2026-09-20 - Visual Studio Project Generation Succeeded

**Completed:** The Manager/user confirmed successful Visual Studio project generation for `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject`. `FactoryGame.sln` appeared in `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader`.

**Resolution:** The previous Visual Studio/project-generation blocker is cleared. The earlier failed attempt remains preserved in the history.

**Verification boundary:** This confirms project generation only, based on The Manager/user's verified result. A successful FactoryGame build, Unreal Editor launch, and Early Locomotion implementation are not verified. No toolchain versions were changed or newly inventoried.

**Files changed:** Development/PROGRESS_LOG.md, INDEX.md, and Development/TECHNICAL_ENVIRONMENT.md updated for the successful generation checkpoint. No commit made for this update.

**Exact next action:** Open `FactoryGame.sln` in Visual Studio 2022 and perform the first **FactoryGame** build using the documented **Development Editor / Win64** configuration. Record the result; capture full errors before changing dependencies if it fails.

### 2026-09-20 - First FactoryGame Build Succeeded

**Completed:** The Manager/user verified that the first FactoryGame build completed successfully in Visual Studio 2022 using **Development Editor / Win64**.

**Build result:** 12 succeeded; 0 failed; 0 up-to-date; 0 skipped.

**Build duration:** `09:44.449`.

**Verification:** FactoryGame.sln generation and the FactoryGame Development Editor / Win64 target build with the installed toolchain are verified. The build-verification milestone is complete. This previous-session result was supplied by The Manager/user and recorded on 2026-09-26; no build was rerun in this documentation task and no toolchain versions were changed.

**Not yet verified:** Unreal Editor launch, successful FactoryGame project load in Unreal Editor, Early Locomotion implementation, mod packaging, and runtime behaviour.

**Files changed:** Development/PROGRESS_LOG.md, Development/TECHNICAL_ENVIRONMENT.md, and INDEX.md. Prior project-generation documentation and chronological history are preserved.

**Exact next action:** Launch `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject` in the **Coffee Stain Unreal Engine 5.6.1-CSS editor** and verify that the project loads successfully.

### 2026-09-26 - First Unreal Editor Launch and Startup Inspection

**Completed:** The Manager/user confirmed a usable Coffee Stain Unreal Engine 5.6.1-CSS editor UI and successful FactoryGame editor-environment loading. Local Saved/Logs/FactoryGame.log records engine 5.6.1-83+++5.6.1-CSS (line 357), SML 3.12.0+d2162c99 pre-initialization (line 917), SML “Initialization finished!” (line 1181), and “Engine is initialized” (line 1373).

**Verification boundary:** Editor launch, environment loading, and SML 3.12.0 initialization are verified separately from the 2026-09-20 build. Early Locomotion implementation, packaging, runtime/in-game behaviour, and a completely warning/error-free environment are not verified.

**Read-only findings:** Windows SoundBank output exists with Init.bnk, Init.txt, PlatformInfo.xml, PluginInfo.xml, and SoundbanksInfo.xml; Mac is the only other generated platform directory. No JSON metadata exists under GeneratedSoundBanks. Wwise SoundEngine initialized as SDK 2023.1.14 Build 8770, but the integration reported missing Windows platform/JSON metadata and failed Init Bank resource loading. Prior SoundBank-generation history is preserved; generated bank/XML files exist but startup metadata expectations are unmet.

**Turnkey:** Automatic SDK detection failed with System.IO.FileNotFoundException for System.Windows.Forms, Version=6.0.2.0 and ExitCode=1. Bundled SDK 8.0.300 has NETCore/AspNetCore/WindowsDesktop 8.0.5; its Windows Forms assembly is version 8.0.0.0. No WindowsDesktop 6.x was listed by the inspected bundled or system host. The exact resolution cause and remedy remain unverified. Full inventories and log paths are recorded in Development/TECHNICAL_ENVIRONMENT.md, “Startup issue evidence — 2026-09-26”.

**Actions not taken:** No component installation, Visual Studio repair, engine modification, SoundBank regeneration, Wwise update, dependency change, implementation, or architecture decision.

**Files changed:** Development/PROGRESS_LOG.md, Development/TECHNICAL_ENVIRONMENT.md, INDEX.md. No commit made.

**Exact next action:** The Manager reviews the evidence and scopes environment cleanup. After cleanup, proceed to local railway API/header inspection and architecture assessment before implementation.

### 2026-09-26 - Wwise Windows Metadata/Platform Issue Resolved

**Investigation and resolution:** The Manager/user verified on 2026-09-26 that JSON metadata existed under GeneratedSoundBanks and Unreal was reading the Windows metadata, but four required fields were missing. In **Wwise Project Settings > SoundBanks > Include in Metadata**, **Object GUID**, **Object Path**, **Max Attenuation**, and **Estimated Duration** were enabled. SoundBanks were regenerated for all platforms, then Unreal was restarted.

**Verified result:** WwiseProjectDatabase then reported:

```text
Platform Windows: Using "Generate All Banks Metadata file" is less efficient than Per Bank.
UpdateDataStructure: Done.
```

The previous Windows-platform, missing-metadata, "No data for Init bank", and Init bank resource-loading errors are resolved. The Generate All Banks Metadata efficiency message is advisory, not a blocker.

**Historical clarification:** The earlier startup inspection recorded no JSON at that inspection time. Later local cache inspections found seven JSON files, including Windows/SoundbanksInfo.json. Cache invalidation alone did not establish resolution; the verified fix was enabling the four required metadata fields and regenerating SoundBanks. Earlier findings remain preserved above.

**Remaining issue:** Turnkey/System.Windows.Forms, Version=6.0.2.0 remains unresolved but deferred because it has not blocked project generation, the FactoryGame build, or editor launch. No dependency/toolchain versions changed.

**Verification boundary:** The first successful Unreal Editor launch and FactoryGame environment load remain verified separately from the successful build. The resolution is recorded from The Manager/user's verified report; no editor restart or regeneration was performed in this documentation task. Implementation, packaging, runtime behaviour, and a completely warning/error-free environment remain unverified.

**Files changed:** Development/PROGRESS_LOG.md, Development/TECHNICAL_ENVIRONMENT.md, INDEX.md. Existing uncommitted startup documentation is preserved; no commit made.

**Exact next action:** Inspect the real local SML/FactoryGame railway APIs and headers in `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader` and prepare an architecture assessment before any Early Locomotion gameplay implementation. Assess viable options for locomotive inheritance; railroad vehicle movement; steam power/fuel replacement versus vanilla third-rail behaviour; track integration; train composition/timetable handling; signalling; stations/platforms; save/load; replication/multiplayer; and compatibility with the vanilla railroad graph/subsystem. Report evidence, constraints, and options to The Manager; do not select an architecture in this documentation task.

### 2026-09-26 - Railway Reconnaissance Completed; Runtime Experiments Next

**Completed:** The Manager/user confirms that Claude Code completed read-only railway header/API reconnaissance. Local FactoryGame Private `.cpp` implementations are generated stubs, so runtime behaviour could not be verified from source.

**Unresolved runtime questions:** unpowered locomotive behaviour; electric subobject requirements; track `CanConnectTo` behaviour; vanilla/Early Locomotion vehicle coupling compatibility; station/platform behaviour without power; and client prediction implications for steam traction.

**Verification boundary:** Completion and findings are recorded from The Manager/user's verified report. This documentation task did not repeat reconnaissance or run experiments. No Early Locomotion gameplay plugin/prototype exists; locomotive/track architecture and Open Questions remain unresolved. No gameplay/design decision or toolchain change was made.

**Files changed:** INDEX.md, Development/PROGRESS_LOG.md, Development/TECHNICAL_ENVIRONMENT.md; the existing CLAUDE.md state correction is preserved for inclusion in the authorised checkpoint.

**Exact next action:** Run small runtime baseline experiments in the local SML/FactoryGame environment before selecting a locomotive/track architecture. Record observed behaviour and return the evidence to The Manager; architecture remains unresolved.

### 2026-09-26 - End-of-Day Workflow and Experiment 1 Preparation

**Completed:** The Manager/user confirmed two persistent Claude Code chats: **EL — Architecture & Research** and **EL — Implementation**. Priming now distinguishes the canonical project/documentation root `C:\Users\a156b\Documents\Satisfactory - Early Locomotion` from the SML/implementation workspace `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader`. Claude Code Implementation was successfully primed against both roots.

**Repository and documentation checkpoint:** The SML repository was verified clean after restoring the representation-only Config/DefaultGame.ini change (UTF-8 BOM / line-ending differences). Read-only railway architecture reconnaissance was completed; documentation was reconciled and committed as `42d878c` — Record railway reconnaissance and next experiments, including correction of stale CLAUDE.md environment wording.

**Technical evidence:** Claude verified that locomotive implementation `.cpp` files are generated stubs, so they cannot prove runtime locomotive power behaviour. Relevant headers expose locomotive power state, tractive power factor, third-rail power connection, and related interfaces. Retail Satisfactory is installed at `D:\Steam\steamapps\common\Satisfactory`. These findings are recorded from The Manager/user's verified report; this documentation task did not rerun reconnaissance.

**Experiment preparation:** Claude proposed a zero-code retail-game test. The Manager narrowed Runtime Baseline Experiment 1 to the powered-control and unpowered-from-rest tests recorded in Current Checkpoint. The experiment has not yet been run; no result is claimed. All six runtime unknowns from the preceding reconnaissance entry remain unresolved.

**Decisions and limits:** No locomotive/track architecture or gameplay design decision was made. Open Questions remain unresolved. No gameplay plugin/prototype or temporary logging mod was created by this documentation task.

**Files changed:** Development/PROGRESS_LOG.md, Development/TECHNICAL_ENVIRONMENT.md, INDEX.md. Documentation checkpoint commit authorised by The Manager; historical entries preserved.

**Exact next action:** Run TEST 1 — POWERED CONTROL, then TEST 2 — UNPOWERED FROM REST, using the Current Checkpoint sequence. Record motion, visible input response, no-power indication, and UI/menu function; defer all expanded tests.

### 2026-10-01 - Asset Development Workspace Preparation

**Completed:** Ensured Assets/Prototypes/Claude, Assets/Locomotives, Assets/Wagons, Assets/Infrastructure, Assets/Signalling, Assets/Materials, Assets/Textures, Assets/Animations, Assets/Exports, Blender, and References/Locomotives exist for **EL — Asset Development**. Its intended scope is Blender modelling, rigging, animation, materials, prototypes, and future export preparation. This task prepared folders, not a new chat or management structure.

**Files changed:** Nine minimal .gitkeep placeholders in new empty leaf folders, plus this setup entry required by WORKFLOW.md. Existing Assets/Textures and Blender are nonempty and need no placeholder. No INDEX navigation update was necessary.

**Preserved:** Existing assets/references, Blender Test.blend and Blender Test.blend1, and unrelated pending design edits. No production assets, gameplay/design decisions, duplicated documentation, or SML repository changes. Existing Blender files remain untracked and excluded from this checkpoint.

**Verification:** Folder inspection and Git review; existing file hashes checked after creation. Commit scope is the nine placeholders and this log only. Pending design edits remain outside the checkpoint.

**Exact next action:** Use the prepared folders for scoped asset work. The main technical next action remains Runtime Baseline Experiment 1: powered control, then unpowered from rest. No experiment was run.

### 2026-10-01 - Manager-approved Design and Roadmap Reconciliation

**Completed:** Documentation-only reconciliation of Manager-approved design statuses, compatible pending linkage edits and post-Core scope; synchronized the Word design reference and created the non-authoritative ROADMAP.docx overview. Updated INDEX, CHANGELOG, WORKFLOW and concise CLAUDE foundation constraints. This history entry records documentation work, not Ideas Lab brainstorming as implementation progress.

**Preserved:** Current Checkpoint and Exact Next Action are unchanged. Runtime Baseline Experiment 1 has not been run; architecture remains unresolved. No gameplay code, production asset or verified toolchain/API fact was changed. TECHNICAL_ENVIRONMENT.md is unchanged. Blender/prototype work and committed reference-library work are excluded.

**Verification:** Canonical status/OQ and document-content comparison; Word layout QA is recorded in the Manager handoff, not presumed from text extraction. Git checkpoint scope reviewed separately; no commit hash is claimed in advance.

**Exact next action:** Run the existing powered-control and unpowered-from-rest first pass, return observations to The Manager, then assess architecture. Future expansion ambitions do not change current technical priority.

### 2026-10-01 - Claude/Blender Asset-development Capability Test

**Completed (Manager-reviewed result):** V1 proved the Claude + Blender MCP workflow could create an editable locomotive prototype. V2 improved it through documented real-world dimension anchors and multi-angle visual-reference comparison, producing a recognisable LMS Fowler Class 3F "Jinty" silhouette rather than a generic steam locomotive, correctly scaled prototype geometry and an organised editable scene. Six-driver coupled running gear and coherent looping coupling-rod animation were verified visually and numerically in the completed experiment. V1 was preserved while V2 was created separately.

**Prototype measurements:** V2 measured approximately 9.5695 m long, 2.667 m wide and 3.8306 m high, with 1.397 m driving-wheel diameter and approximately 5.0292 m total wheelbase. These are prototype/reference modelling values, not gameplay balance values.

**Status and verification boundary:** The Manager has reviewed the completed V2 prototype and confirms that Claude + Blender MCP is viable for future reference-driven locomotive modelling. The asset capability experiment is now **paused**. The prototypes are non-production, not final art and not Unreal-export-ready. This documentation task records the Manager/user's verified results; it did not rerun Blender, remeasure geometry or repeat animation verification. Local inspection confirmed both .blend files and their associated preview folders exist.

**Preserved outputs:** Blender/Jinty_Blockout_Test.blend, Blender/Jinty_Blockout_V2.blend, their existing backups and Assets/Prototypes/Claude/Jinty_Blockout_Test_Previews and Jinty_Blockout_V2_Previews were not renamed, moved, deleted or overwritten. They currently remain untracked; no applicable Git LFS attributes or documented Blender-specific storage policy were found. No storage policy was introduced and no binary assets were staged.

**Future work:** A separately verified production pipeline must cover high-detail modelling, production topology, normals/bevel strategy, UVs, PBR materials/textures, Satisfactory visual/material conventions, production animation, LODs, collision, Blender-to-Unreal export and in-engine validation. None of those production/export capabilities is established by this prototype test.

**Files changed / next action:** Development/PROGRESS_LOG.md only; no commit made. Current implementation checkpoint and exact next action remain unchanged: Runtime Baseline Experiment 1 powered control, then unpowered from rest. No gameplay/design decision, Open Question or technical-toolchain claim was changed. Resume asset experimentation or production pipeline work only as a separate Manager-scoped task.

### 2026-10-02 - Approved Identity, Numbering and Expansion Documentation Refinement

**Completed:** Applied the Manager-approved revised Ideas Lab handoff to current canonical design; reconciled INDEX/CHANGELOG and concise CLAUDE identity constraints, synchronized the existing Word Design Reference, ROADMAP and Feature Catalogue. Revised OQ06/OQ20/OQ23–OQ25/OQ27 and added OQ28–OQ30. This records documentation work only, not brainstorming as gameplay implementation.

**Preserved:** Current Checkpoint and Exact Next Action remain unchanged. Runtime Baseline Experiment 1 is still unrun and architecture remains unresolved. TECHNICAL_ENVIRONMENT and gameplay implementation state are unchanged; no speculative API/storage/formula, toolchain fact, production asset or licence is claimed. Prior uncommitted Claude/Blender capability entry and all experimental outputs are preserved and excluded from this checkpoint commit.

**Verification:** Canonical status/OQ consistency and synchronized Word content/layout checks are reported in the Manager handoff. Exact next technical action remains powered control followed by unpowered from rest, returning observations before architecture selection.

### 2026-10-02 - SML Short-path Relocation and Runtime Probe 1 Packaging Preparation

**Completed:** Relocated the active SML workspace from `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader` to `C:\SML`. The prior root produced 262-character Shipping action paths, exceeding UBT's hard-coded 260-character limit; Windows LongPathsEnabled did not bypass this validation. The shorter root removed the blocker. Probe implementation/Blueprint configuration is complete; project files regenerated successfully at the new path, and FactoryGame Development Editor / Win64 built successfully in **488.10 seconds**. The editor initialized SML 3.12.0 and loaded the probe module; its Blueprint resolved/opened and native class resolved. Wwise SoundEngine initialized and WwiseProjectDatabase reported `UpdateDataStructure: Done.`

**Integrity:** Git HEAD before/after was `d2162c999bbaa9650594ee9ad6e6e06190306009`; tracked status and ignored state matched immediately after relocation, and the final SML working tree was clean. Probe Blueprint SHA-256 before/after: `882de775beaa0458924c616e3fb0ca65899b6211f8c165bcbd29096402b99564`. FactoryGame.uproject SHA-256 before/after: `a4b627b3d11537131f0610c914471db69245018561278cf2a5e508c96aba923b`; EngineAssociation remains `5.6.1-CSS`. All 114 protected probe/Wwise files matched the temporary backup before rebuilding.

**Packaging/deployment:** Alpakit's own automation command succeeded (AutomationTool ExitCode **0**, approximately **6 minutes 41 seconds**). Only `EL_ArchitectureProbe` was packaged, Windows client / Shipping only, with copy-to-game enabled for `D:\Steam\steamapps\common\Satisfactory`; Windows Server and Linux Server were disabled and retail launch was off. Native UI control was unavailable, so automation invoked the same backend used by Alpakit Dev. The original path blocker did not recur; no new packaging error occurred.

**Operational notes:** Only the two explicitly authorised workspace-bound processes were terminated before repeat safety checks. The initial filesystem move stopped partially with an access error; native same-drive directory moves completed relocation, followed by verification. An initial build failed in the Wwise prebuild step because Windows PowerShell could not load its security module; retrying with a process-local Windows PowerShell module search path succeeded. No dependency versions or system execution policy changed. The old empty source root/parent folders and logs were retained.

**Recovery material:** Temporary hash-verified backup retained at `C:\Users\a156b\Documents\Codex\2026-09-19\referenced-chatgpt-conversation-this-is-an-2\sml-relocation\safety-backup`. This is recovery material, not a second canonical or permanent SML development tree; do not delete it before Manager review.

**Boundary / next action:** Runtime Probe 1 in retail Satisfactory remains pending/unverified; no traction outcome, architecture decision, production implementation or warning/error-free certification is claimed. Run the prepared probe under the Manager-approved procedure and return observations before architecture selection. Reconciled the active path and preparation status in project documentation/derived roadmap and added the approved universal specialist model/effort handoff rule; gameplay design and Open Questions are unchanged.

### 2026-10-02 - Project Governance and Specialist Delegation Reconciliation

**Completed:** Created `Development/SPECIALIST_DELEGATION.md` as the detailed specialist-selection, model/effort, escalation, task-construction, handoff and verification guide. Shortened WORKFLOW to link to that guide and aligned active authority lists to INDEX, GAME_DESIGN, PROGRESS_LOG, TECHNICAL_ENVIRONMENT, CHANGELOG, WORKFLOW, SPECIALIST_DELEGATION, then CLAUDE. Preserved Claude-specific implementation guidance; recommendations now precede the task for the user and normally remain outside the specialist prompt. Recorded Manager-approved Claude Sonnet 5.5 / Opus 5.5 and Project Operations GPT-5.6 Sol effort guidance, with official Anthropic source notes and a time-sensitive re-verification rule, without pricing.

**Current development state preserved:** The relocation/build/packaging facts above remain verified; active SML workspace is `C:\SML`, Wwise remains functional, and Windows Shipping probe deployment is prepared. Runtime Probe 1 in retail Satisfactory remains pending/unverified. No runtime test, architecture choice, gameplay/design decision, Open Question resolution, dependency change or implementation-workspace modification occurred in this documentation task. Historical entries and recovery backup are preserved. Updated the derived roadmap's governance navigation and recorded the restructuring in CHANGELOG.

**Next action:** Run the prepared retail Runtime Probe 1 under the Manager-approved procedure and return evidence before architecture selection.

### 2026-10-02 - Retail Runtime Probe 1 Completed and Analysed

**Completed / evidence:** The Manager/user reports completed runtime observation and FactoryGame.log analysis. The EL Probe Locomotive built normally through the Build Gun; its vanilla locomotive hologram snapped correctly to vanilla railway track. Diagnostic samples consistently showed `HasTrain=true`, `IsDerailed=false` and `HasPower=false`, with `FGLocomotiveMovementComponent` retained. Reverser/throttle inputs changed normally; TrainStatus changed between Parked and ManualDriving. `TractiveEffortPct` and `TractiveForceN` became non-zero, and `ForwardSpeedCmS` rose from standstill. Air and dynamic braking stopped the locomotive. Two separately placed probe locomotives reproduced the result.

**Verified scope:** AFGLocomotive subclassing is runtime-verified viable for construction, vanilla rail attachment, input, braking and unpowered movement in this probe. No final production architecture is selected.

**Residuals:** Camera could not rotate/look left/right normally, normal locomotive UI was absent, and exiting placed the player partly underneath/intersecting the locomotive. These presentation/configuration residuals remain unresolved but do not currently invalidate the observed traction/rail integration result.

**Causality limit:** This does not prove that `SetTractivePowerFactor(1.f)` specifically caused unpowered traction. Vanilla unpowered movement on the same dead track, sufficiency of the probe's no-op `UpdatePower`, and necessity of `SetTractivePowerFactor` remain untested. Final production architecture remains unresolved.

**Next action:** Perform Manager-scoped causality control testing on the same dead track: establish whether a vanilla unpowered locomotive moves, whether the probe's no-op `UpdatePower` alone is sufficient, and whether `SetTractivePowerFactor(1.f)` is necessary. Return observations and log evidence before selecting the final production locomotive architecture.

**Documentation boundary:** This task records the supplied verified results; it did not rerun the experiment or independently analyse the log. No gameplay requirements, design statuses or Open Questions changed.

### 2026-10-02 - Runtime Probe 1 Traction-causality Control Completed

**Evidence:** Manager/user-verified three-way runtime result; this documentation task did not rerun the experiment.

1. **Vanilla control:** On deliberately unpowered railway, the Vanilla Electric Locomotive showed No Power; a W throttle attempt produced no movement.
2. **Working EL probe:** With `SetTractivePowerFactor(1.f)` active and `UpdatePower()` a no-op, `HasPower=false` while driver input was accepted, `TractiveEffortPct` and `TractiveForceN` were non-zero, the locomotive accelerated/moved normally, and braking worked.
3. **Single-change EL control:** Only `SetTractivePowerFactor(1.f)` was disabled; `UpdatePower()` remained the same no-op. `HasTrain=true`, `IsDerailed=false` and `HasPower=false` each held for **165/165 samples**. Reverser/throttle input was observed, `TractiveEffortPct` reached **0.340**, and air brake was released during driving attempts. `TractiveForceN` and `ForwardSpeedCmS` remained **0 throughout**.

**Conclusion / scope:** Within the currently tested implementation, `SetTractivePowerFactor(1.f)` is necessary for producing unpowered traction; the no-op `UpdatePower()` alone is insufficient. This does not establish the final production locomotive architecture.

**Next action:** Restore the successful working probe with `SetTractivePowerFactor(1.f)` active and `UpdatePower()` remaining a no-op, then proceed to normal railway-integration tests beginning with vanilla wagon coupling. Record observations before final production architecture selection. Restoration and coupling testing are next actions, not completed milestones.

No gameplay requirements, design statuses or Open Questions were changed. Historical Probe 1 observations and earlier causality uncertainty are preserved as records of what was known at the time.

### 2026-10-02 - Runtime Probe 1 Vanilla-wagon Integration Verified

**Evidence / completed:** Manager/user-verified runtime observations; this documentation task did not rerun the test. The restored known-good EL Probe Locomotive was tested on the same deliberately unpowered railway. A vanilla Freight Wagon built/snapped directly onto the probe formed a usable consist. The locomotive moved the consist forward and in reverse; normal braking stopped locomotive and wagon cleanly. No derailment or separation was observed during normal movement/braking.

**Conclusion / scope:** AFGLocomotive-derived probe integration with vanilla rolling stock is runtime-verified for normal construction-time consist formation, forward/reverse movement and braking while electrically unpowered. Final production architecture remains unresolved.

**Residuals / unresolved:** The temporary probe coupling node/position is visibly misaligned. Driving the probe into an independently placed loose wagon made the train unresponsive to commands. Whether collision-coupling independently placed rail vehicles is a supported vanilla workflow has not been established; this observation is not classified as an architecture failure. Earlier camera, normal locomotive UI and exit-placement residuals remain unresolved.

**Next action:** Proceed to station/timetable integration testing using the restored known-good working probe. Record observations before final production architecture selection; station/timetable success is not yet verified.

No final architecture, gameplay/design requirement or Open Question was selected/resolved. All prior history and the traction-causality result are preserved.

### 2026-10-03 - Probe 2a Locomotive-power / Timetable Diagnostics

**Evidence / completed:** Manager/user-verified runtime log result; no independent test/log analysis performed in this documentation task. `ProbeVariant=PowerDiagnostics2A` ran successfully. Runtime log: `HasPower=false` and `PowerInfoHasPower=false` on all **1,069 samples**. `PowerInfoConnected=true`, `PowerInfoFuseTriggered=false`, `ShoeCircuit=true`, `HasTrain=true` and `IsDerailed=false` throughout.

**Powered railway/stations:** When railway/stations were powered, `ShoeHasPower` changed false -> true while `HasPower` and `PowerInfoHasPower` remained false. Manual forward/reverse traction continued to work.

**Self-driving:** Enabling self-driving set `SelfDrivingEnabled=true`; one tick later `GetSelfDrivingError=SDLE_NoPower`. At that time `ShoeHasPower=true`, both locomotive power flags were false, and `TrainStatus=Self Driving`. Throttle, tractive effort and tractive force were suppressed to zero; air/dynamic braking held the train stationary. Disabling self-driving restored manual traction immediately.

**Conclusion / limits:** The timetable/self-driving No Power condition is locomotive-level rather than simply lack of powered third rail. The exact gate remains unresolved because `HasPower` and `PowerInfoHasPower` were always identical in this run. The earlier observation that powering an already-placed probe breaks manual driving did not reproduce in this controlled run and remains unverified. It is not treated as established behaviour or an architecture failure. Final production architecture remains unresolved.

**Next action:** Probe 2b: set only the inherited locomotive `mHasPower` state true via verified Unreal property reflection while leaving `PowerInfoHasPower` unchanged, then test self-driving. This is the next planned test, not a verified outcome; do not select final production architecture.

No final architecture or gameplay/design decision was made; no Open Question was resolved. Prior history is preserved.

## Rules for Maintaining This Log

1. After every meaningful work session, update **Current Checkpoint** and append a dated history entry. Keep the checkpoint at the top and history oldest first.
2. Record actions actually taken, their outcomes, errors, fixes, versions, files changed, and the exact next action. Distinguish **planned**, **in progress**, **completed**, and **verified**.
3. Never mark an installation complete because its components were selected. Never mark a build successful because project generation succeeded. Record editor launch separately.
4. Preserve old entries. Correct mistakes with a dated correction referencing the earlier entry; do not silently rewrite history.
5. Capture full error text and useful log paths when available. Label paraphrases and unavailable output. Do not invent commands run, commit hashes, timestamps, paths, or verification results.
6. Use dates in YYYY-MM-DD format. Add local times and timezone when known; do not infer exact event times from a later summary.
7. Keep brainstorming and unresolved design proposals in the appropriate design notes. Preserve Agreed / Proposed / Playtest Target / Superseded labels; do not resolve Open Questions through a progress entry.
8. Read `INDEX.md` first when available, then this checkpoint. Use `Design/GAME_DESIGN.md` for canonical design, `Development/TECHNICAL_ENVIRONMENT.md` for verified toolchain/API facts, `CHANGELOG.md` for meaningful changes, and `CLAUDE.md` for Claude-specific working rules. Flag conflicts explicitly.
9. When an approved change affects another continuity file, update the relevant detailed reference and then the Index/Changelog as appropriate. Avoid copying the whole work diary into those files.
10. Keep version changes deliberate and evidence-based. Preserve the recorded custom-engine/Wwise pairing; investigate errors before changing dependencies. Re-verify technical requirements before future implementation rather than treating this historical log as current upstream documentation.
11. Preserve the setup cautions recorded in the conversation: do not casually use Wwise Update, enable the Visual Studio Integration Tool or Unreal Engine Test Adapter, or upgrade dependencies in response to notices. Revisit these against verified project requirements if the toolchain changes.
12. Do not commit automatically. Record any commit only after it has actually been made and verified. Keep account details, tokens, and other secrets out of the log.

### Future Entry Template

```markdown
### YYYY-MM-DD - Session / Milestone

**Completed:** Actual work and evidence of success.
**Attempted / incomplete:** What was tried and where it stopped.
**Errors:** Exact text or log path; identify paraphrases.
**Resolution:** Fix applied and result, or unresolved.
**Environment changes:** Previous -> new version; verification source.
**Files changed:** Project-relative paths; commit only if made.
**Verification:** Checks actually performed and their outcomes.
**Current blocker:** Specific blocker, or none.
**Exact next action:** Starting folder/tool, action, expected result, failure capture.
```
