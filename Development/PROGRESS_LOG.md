# Early Locomotion - Progress Log

## Current Checkpoint

**Date:** 2026-09-20
**Phase:** Development environment setup  
**Status:** Project generation and the first FactoryGame Development Editor / Win64 build succeeded on 2026-09-20. Build verification is complete; first successful Unreal Editor launch and project load are next.
**Current blocker:** The previous generation blocker is cleared and build verification is complete. No new blocker is recorded; editor launch and project load remain unverified.
**Implementation status:** No actual Early Locomotion mod implementation has started. The FactoryGame/SML target builds successfully; Unreal Editor launch, project load, mod packaging, and runtime behaviour remain unverified.

This checkpoint records the 2026-09-20 build result verified by The Manager/user and documented on 2026-09-26. Earlier chronological entries remain historical records of what was known at the time.

### Current Environment

| Item | Recorded version / selection | Status at checkpoint |
| --- | --- | --- |
| Satisfactory | 1.2 | Agreed development target |
| Satisfactory Mod Loader | SML 3.12.0; pairing uses 3.12.x | Recorded development target; starter repository cloned; exact checkout commit not recorded |
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
- Separate SML development environment: `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader`
- Unreal project: `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject`
- Companion Wwise project: `SatisfactoryModLoader_WwiseProject\SatisfactoryModLoader_WwiseProject.wproj`, under the SML checkout as described in the setup conversation.

Keep the design/project repository separate from the SML development environment.

### Exact Next Action

1. Launch `C:\Users\a156b\Documents\SatisfactoryModding\SatisfactoryModLoader\FactoryGame.uproject` in the **Coffee Stain Unreal Engine 5.6.1-CSS editor** and verify that the project loads successfully.
2. Record editor launch and project-load results separately from the already successful build. Capture the full error/output if either fails.

**If it fails:** Diagnose the new error against the recorded toolchain. Do not change engine, Wwise, Visual Studio, SML, or dependency versions as a speculative fix.

### Remaining Milestones

- First successful Unreal Editor launch and FactoryGame project load.
- Inspect the real local railway headers and prepare an architecture assessment before gameplay implementation. Steam locomotive inheritance, movement, save/load, replication, and reuse of the vanilla railroad graph remain unresolved.
- Early Locomotion implementation, mod packaging, and runtime verification remain pending.

### Documentation Reconciliation

Local documentation reconciliation and placement are complete, including restoration of INDEX.md to the project root. The Manager confirmed removal of the obsolete Git installer and empty encoded wrapper folder.

Project Operations (Local) is established inside the ChatGPT Project and has verified local repository access. Project Operations (Cloud) remains available for cloud/project-source work.

The completed documentation/design batch was committed as `eda2873` (Canonicalize railway assistant design and sync project docs), and the repository was confirmed clean afterward. The project-generation checkpoint is preserved alongside the first-build record below; the 2026-09-26 documentation task includes an explicitly authorised Git checkpoint.

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
