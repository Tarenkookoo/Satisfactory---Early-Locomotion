# Shared tooling and GitHub readiness

Audit date: 3 October 2026. **Audit and proposals only; not an approved storage-policy change.** Local project root: `C:\Users\a156b\Documents\Satisfactory - Early Locomotion`. `C:\SML` is separate and was not inspected or modified. Sources are current local files, static script inspection, saved verification reports, and the official documentation linked below. No Blender build, export or runtime test was rerun.

## Approved low-risk follow-up — 4 October 2026

This dated addendum supersedes the stale ignore/skill/guide-status findings below. The 3 October audit and its evidence remain a historical baseline, not a claim that those gaps are still open.

- Added a narrow root `.gitignore`: portable local Claude permissions exclusion, automatic Blender backups, Python/OS/IDE junk, root-only Unreal generated directories and explicitly named asset/release scratch folders. No blanket preview/export/reference exclusion. Existing files are preserved; the only expected newly ignored current files are the four `.blend1` backups. Named .blend/FBX milestones, reference packs, docs and scripts remain eligible.
- Corrected the asset skill's discovery and dated handoff instructions; CLAUDE uses the universal completion fields. Concise guide pointers require the relevant class brief and prior-stage notes. Authority order is unchanged.
- ASSET_DEVELOPMENT_GUIDE is now the current subordinate helper for established practice. No installed shared toolkit is claimed. Ordinary text/scripts/docs use normal Git; large binary source/assets remain LFS candidates pending approval; disposable output is excluded only where scoped. Final LFS policy, GitHub publication and broader retention decisions are still pending.
- Historical installer: exact repository-relative path `Git-2.55.0.5-64-bit.exe` (former absolute path `C:\Users\a156b\Documents\Satisfactory - Early Locomotion\Git-2.55.0.5-64-bit.exe`), blob `1f4b2e90a8cd3883ed9146203649c32b7f17edff`, 65,343,712 bytes (62.32 MiB). Absent from disk and current tracked file set: neither currently tracked nor untracked; retained in reachable Git history. It has already been removed from the current tree, so no future normal deletion commit is needed. Removing that reachable payload requires separately approved history cleanup, followed by appropriate object reclamation; a normal commit or ignore rule cannot do it. No history or object cleanup was performed.

Next operations step: review this scoped change set and authorise an explicit-path checkpoint if wanted. Full-history secret/privacy and reference-redistribution review remain prerequisites to publication; the earlier scoped scan is not a fresh or complete clearance.

---

## 1. Executive summary

The project is suitable for a small, deliberate documentation/script checkpoint after review, but **not for an indiscriminate whole-folder upload**. The local repository has no remote, no shared ignore rules and no LFS tracking rules. Most asset work is untracked. Selective storage and licensing review should precede adding it.

Keep local files canonical; use GitHub for reviewed history, collaboration and an additional backup of committed content. Preserve editable Blender milestones. Start shared tooling with measurement, reports and motion mathematics, not a class-generating framework. Black 5 Stage B offers useful extraction candidates, but its build depends on the preserved Stage A `.blend`; the Stage A builder is missing and Pannie builders are not stored locally.

This task creates this report and a [draft asset guide](ASSET_DEVELOPMENT_GUIDE.md), and corrects the stale Black 5 status in [ASSET_PATHS](../Blender/ASSET_PATHS.md). It does not install a toolkit, amend authority, select architecture or change design status.

## 2. Current Git/GitHub state

Baseline before these edits:

| Check | Observed result |
| --- | --- |
| Branch / HEAD | `master`; `c69e2bbfed7c6cf77e31aa1b634ebfb7982ae611` — Prioritize singleplayer Core and defer multiplayer |
| History | 24 commits; one local branch; no remote configured |
| Existing modifications | `CHANGELOG.md`, `CLAUDE.md`, `Development/PROGRESS_LOG.md`, `Development/SPECIALIST_DELEGATION.md`, `Development/TECHNICAL_ENVIRONMENT.md`, `INDEX.md` |
| Index | Nothing staged |
| Current file inventory, excluding `.git` | 50 tracked files (17.37 MiB), 357 untracked (281.76 MiB), one ignored (238 bytes); 408 files total |
| Tracked areas | Canonical docs, three derived DOCX files, project-local asset skill, initial reference material/Jinty photos, supporting notes and folder placeholders |
| Untracked areas | All populated `Blender/`, most locomotive reference-library work, compatibility exports/Jinty previews in `Assets/Prototypes/Claude/`, and `Development/DAILY_REPORT_2026-10-03.md` |
| Ignore rules | No project `.gitignore`; `.git/info/exclude` contains comments only. User-global ignore excludes `.claude/settings.local.json`; that protection is not portable to another machine |
| Attributes/LFS | No `.gitattributes` or `.lfsconfig`; Git LFS 3.7.1 installed and filter keys available, but `git lfs ls-files` is empty |
| Local config | Ordinary non-bare Windows repository; `filemode=false`, `symlinks=false`, `ignorecase=true`; effective `autocrlf=true`. Identity configured; identity values are not reproduced |
| GitHub readiness | No repository remote, upstream or tracked `.github` setup found. User reports connector availability, but account/repository access was not verified in this session |

No callable Firecrawl research tools or general GitHub repository connector tools were exposed in this session's tool inventory. This is a session capability limit, not a finding that the user's installations are broken. Official web documentation was used as a fallback. No connector configuration or authentication files were changed.

**Secret review:** all current project files were inventoried, including tracked, untracked and ignored files. Pattern scanning covered 135 readable text/empty files or DOCX XML/relationship containers. It checked recognizable provider/GitHub keys, private-key headers, quoted credential assignments and credentials embedded in URLs; no matches were found. The ignored local Claude settings file was included. The remaining 273 opaque binary files were hashed, not certified free of embedded sensitive content. Historical Git payloads, credential stores outside the project, encrypted content and arbitrary unknown credential formats were not scanned. Before first publication, run a dedicated full-history secret scan and review reference/history privacy. No secret values were printed or copied to this report.

## 3. Binary asset/storage assessment

Logical working-file sizes (not filesystem allocation):

| Class | Count | Total MiB | Significance |
| --- | ---: | ---: | --- |
| PNG | 132 | 225.46 | Dominant current storage; principally review renders/sheets, not all source textures |
| JPG | 110 | 49.15 | Research photography; redistribution rights differ by source |
| `.blend` | 15 | 10.46 | Editable sources plus export derivatives; all currently untracked |
| `.blend1` | 4 | 0.78 | Automatic backups; preserve existing files, not milestone substitutes |
| FBX | 6 | 8.69 | Export candidates, including protected compatibility paths |
| MP4 | 6 | 3.29 | Review evidence, usually regenerable only when source and scripts survive |
| DOCX | 3 | 0.17 | Small derived human-readable documents; ordinary Git is proportionate |

The largest current file is the tracked Jinty `04-47406-front-smokebox.jpg`, 7,196,463 bytes (6.86 MiB). No current file exceeds 50 MiB; no `.blend`, `.blend1`, FBX or MP4 is currently tracked. Binary tracking already exists for photographs, PNG and DOCX files.

`git count-objects -vH` reports 228 loose objects occupying 303.94 MiB, no packs. Reachable history contains 122 blobs totalling 81.85 MiB uncompressed; its largest is the deleted `Git-2.55.0.5-64-bit.exe`, 65,343,712 bytes (62.32 MiB). No reachable blob exceeds 100 MiB. Loose-object footprint and reachable uncompressed payload are different measures; this audit did not prune or diagnose all retained/unreachable objects. Deleting a working file does not erase its historical blob.

GitHub warns above 50 MiB and blocks ordinary Git files above 100 MiB; repository health still matters below those limits. The historical installer is a warning/avoidable-history burden, not evidence of a 100 MiB hard-block violation. Preserve history for now; do not migrate or rewrite it merely to tidy an audit. [GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

No Unreal build/cache/output tree was found in this documentation-root file inventory. Preview renders, derived exports, `.blend1` files and local scratch would nevertheless be eligible for accidental broad staging because no shared exclusions exist. `C:\SML` remains a separate repository boundary.

## 4. Recommended Git/LFS/exclude policy — proposal

| Material | Recommendation | Tradeoff / condition |
| --- | --- | --- |
| Markdown, helper Python, portable config, manifests, attribution, verification JSON, export notes | Ordinary Git | Reviewable diffs; remove credentials and machine-specific permission settings. Preserve scripts beside the milestone they produced |
| Small derived DOCX | Ordinary Git | Binary diff is poor, but size is modest; maintain from canonical Markdown and visually QA changes |
| Named editable `.blend` milestones | Preserve and version selectively; ordinary Git is reasonable at today's sizes; consider LFS before sustained binary churn | Source is not expendable just because a builder exists. LFS helps checkout/history handling but adds client/service dependency and storage cost |
| `.blend1`, temporary saves, caches | Future local-only exclusion by approval; retain current backups unchanged | Automatic backups are not meaningful milestones. Exclusion must be paired with a separate backup plan, not deletion |
| Export-preparation `.blend` / FBX | Retain reviewed integration milestones; possible LFS when large or frequently revised; exclude transient regenerated copies only after reproducibility is proven | Pannie builders are absent. v001/v002 FBX compatibility paths must remain until an authorised dependency migration |
| High-resolution source textures and audio | LFS candidates if authored/essential, large and changing; ordinary Git for genuinely small stable files | None inventoried as a dedicated authored texture/audio set; do not pre-enable broad rules. Retain licensing and source files |
| PNG sheets / MP4 review clips | Keep a small decisive review set per milestone; LFS only if retained volume warrants it; other temporary renders local/generated | Current PNG volume dominates. Preserve evidence while avoiding every intermediate frame in history; source+scripts alone do not yet reproduce all old work |
| External photographs, diagrams, PDF/reference binaries | Ordinary Git for small, stable, redistribution-permitted selected files; LFS only for necessary large licensed files; otherwise links/manifests | Public accessibility is not redistribution permission. Source/author/licence/caveats travel with retained evidence |
| Unreal Intermediate/Binaries/Saved/DerivedDataCache, packages, installers, scratch | Exclude from this docs/asset repository under an approved narrow ignore policy | Keep reproducible outputs separate; no changes to the implementation repository in this task |

Do not use `*.png`, `*.fbx` or all binaries as automatic LFS/exclude rules without reviewing actual roles. With LFS, each changed version is stored as a complete file and downloads consume bandwidth; agree the account budget and retention expectations first. LFS pointers are not a backup without the corresponding objects. [GitHub LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs), [LFS overview](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)

## 5. Proposed GitHub workflow

1. Keep this local repository canonical. Retain `master`; no branch rename is needed. Use short-lived `docs/...`, `tools/...` or `asset/<lineage>-<stage>` branches for substantial isolated work, with one editor owning a binary at a time. Small approved documentation checkpoints can remain direct commits.
2. Begin with local status, HEAD, relevant diff and the current file map. Record the task's intended file list. Do not switch a shared dirty checkout or sweep unrelated pending work into a commit.
3. Commit only when authorised: stage explicit paths, review staged names/stat/diff and verify intended binary hashes. Separate documentation/tooling from asset milestones where practical; keep each asset source, its evidence/manifest and essential provenance together. Example messages: `Document shared asset workflow`, `Add Black 5 Stage B source and review evidence`.
4. Agree remote owner, repository name, visibility and licensing/privacy before creating a remote. A private initial repository is a proposal, not an action already taken. GitHub backs up only pushed, included content; untracked/ignored files need independent backup.
5. When remote use is approved, check remote identity and freshness using a fetch and compare local/remote commit IDs before remote review. GitHub has no working-tree/untracked changes. A remote review must state its SHA and explicitly exclude newer local edits. Never overwrite local state from a connector summary/cache.
6. If LFS is approved later, scope reviewed patterns before adding new eligible assets, validate attributes/pointers, and verify a clean clone can fetch the real objects. Decide any historical migration separately; no force-push or history rewrite is implicit.
7. Review diff/status again, then push only with explicit authorisation. Report commit and remote SHA. No CI, branch-protection bureaucracy or automatic publishing is needed for the initial workflow.

## 6. Reusable Blender-tooling inventory

Source key: **B** = [Black 5 Stage B scripts](../Blender/LMS_Stanier_Black_5/Notes/StageB_build_scripts/); **A** = [Stage A notes](../Blender/LMS_Stanier_Black_5/Notes/EXPORT_NOTES_StageA_v001.md); **P** = [Pannie v004 notes](../Blender/Pannie/Notes/EXPORT_NOTES_v004.md). **R** means a reusable algorithm candidate, not a drop-in tested library; **P/R** means extraction/configuration is needed; **M** means class/stage-specific; **missing** means no standalone implementation was found.

| Capability | Actual source / symbol | Classification, dependencies and limits |
| --- | --- | --- |
| 1.8 m QA figure | B `render_review.py:figs`, `shot`; A figure description | P/R for visibility/review. Creation helper missing; scripts expect existing `SCALE_REFERENCE` objects in Stage A source |
| Rail datum / QA track | B `render_anim.py:key_sleepers`; A scale/axes | P/R; existing `Ref_Sleepers`, pitch 0.52 m and driver radius 0.9144 m hard-coded. Track creation helper missing |
| Wheel creation | B `b5lib.py:lathe`, `cyl`, `ring_tube`; Stage A wheel meshes | R primitives, but complete wheel builder missing. Do not mistake a generic lathe for a verified multi-class wheel generator |
| Master angle / axle count | B `s08_anim.py:make_action`; `verify_mech.py:setctl` | P/R; existing `B5_Anim_Control`, three coupled axle names and metre/radian conventions. Control creation and original wheel drivers inherited from A |
| Quartering | B `verify_mech.py` phase loop; A/P motion notes | P/R measurement; right-leading 90° is a provisional asset assumption, not universal historical truth |
| Coupling rods | B `b5lib.py:rod_plate`; `verify_mech.py` coupling-pin checks; A constraints | P/R; same-side pins in phase, three axles, source COPY_LOCATION constraints. Parameterise arbitrary axle lists and segment endpoints |
| Connecting rods / crossheads | B `s03_motion.py:band`, `disc_y`; `verify_mech.py:P`, conrod checks; P explicit slider-crank formula | P/R; planar slider geometry and DAMPED_TRACK concepts reusable. Black 5 rod 2.74 m / crank 0.3556 m differ from Pannie's assumed 1.95 / 0.305 m. Full original solver builder missing |
| Walschaerts visual linkage | B `s03_motion.py` driver-expression substitutions; `s08_anim.py` gear control; `verify_mech.py` closure | M geometry, P/R future solver. It patches existing `B5_VG_Solver_L/R` expressions using string replacements; fixed pivots/link lengths/lateral bands are not a reusable gear specification. Valve timing is unverified |
| Pivots / geometry transforms | B `b5lib.py:mk(origin=...)`, `xform_verts`, `bbox`, `single_user` | R with `bpy`, `bmesh`, `mathutils`; defaults assume B5 collections/materials/parent and world-authored vertices |
| Forward/reverse timelines | B `s08_anim.py:fcurves_of`, `make_action` | P/R; Blender 5.x layered actions, frames 1–49, 24 fps, two named B5 actions; preserve/restore prior action/state |
| Numeric motion / loop checks | B `verify_mech.py:W`, `P`, `setctl`; `verify_anim.py:wrap`, `sample` | P/R; named object lists, hard-coded dimensions/tolerances/frame range. Checks currently report metrics, not a comprehensive fail/pass contract |
| Rolling/no-slip checks | B `verify_mech.py` rolling section; `render_anim.py:key_sleepers`; P reported contact checks | P/R; wheel-radius ratios and direction signs. Small wheels do not repeat after one driver revolution; a cyclic visual clip is not automatically seamless |
| BVH overlap / clearance | B `verify_mech.py:world_geo`, `assembly`, `geo` | P/R; `mathutils.bvhtree`, evaluated meshes, 10° overlap/20° clearance samples, explicit pair exclusions. Static union assumes static parts stay static; sampled vertex/surface distances do not prove continuous clearance |
| Contact sheets / strips | B `compose.py:load_rgba`, `save_rgba`, `label`, `grid`, `side_by_side`, `stack_v`; `contact.py` | R core functions; Blender image/render API and NumPy, not standalone Pillow. Remove B5-specific file lists and label-scene side effects |
| QA cameras / still previews | B `views.py:ensure_rig`, `cam`, `render`, `go`; `render_review.py:shot` | P/R; camera utilities reusable; positions, hide prefixes and comparisons are Black 5-specific. Restore temporary visibility even after errors |
| Animation previews | B `render_anim.py:movie` | P/R; four named clips, frames 1–96, FFmpeg support, B5 controls. Renames/replaces outputs; never run against an unreviewed output directory |
| Coal levels | B `s07_tender.py` explicitly preserves existing coal; A/P notes list three additive layers | Reusable convention, creation helper missing. Pile geometry, bunker envelope, level heights and pivots remain asset-specific |
| Material helpers | B `b5lib.py:mat`, `Parts`; export material gathering | R lookup/grouping, not material authoring: named B5 materials must already exist. Generic material creation helper missing; add null-slot checks before export |
| FBX export | B `export_stageb.py:export_objects`, `eval_geo`, `add_to_joined`, `new_object_from_bm` | P/R; separates static/moving parts, bakes rest pose and preserves pivots. B5 regexes, hierarchy, collection names, 3 drivers/2 bogie/3 tender axles and +X/+Z are hard-coded |
| Fresh-scene FBX verification | B `reimport_check.py` top-level report | P/R; factory-empty scene and actual FBX import; mesh/empty count, dimensions, transforms, material count, pivots and helper exclusions. No Unreal verification |
| Triangle / mesh reporting | B `b5lib.py:tri_count`, export/reimport reports | R counts; generic report schema needed, with explicit units, expected values and source hashes |
| Build orchestration / proportions | B `build.py`; `s01`–`s07`, `s09` | M. Opens fixed absolute Stage A path, saves Stage B, mutates named parts, disables backups and purges orphan data. Not safe to import as a general-purpose helper |

All 21 standalone Python files found in the project are in B. No standalone Pannie or Stage A Python builder was found. The [Stage B notes](../Blender/LMS_Stanier_Black_5/Notes/EXPORT_NOTES_StageB_v002.md) explicitly say the Stage A builder no longer exists; P says its builders are not stored in the project. Source `.blend` files retain rig relationships, but embedded text blocks were not extracted during this audit. Preserve those sources; recover earlier scripts only from an authorised, known source rather than inventing provenance.

Saved evidence inspected in [StageB_verification](../Blender/LMS_Stanier_Black_5/Notes/StageB_verification/): `mech_v002.json`, `anim_v002.json`, `export_v002.json`, `reimport_v002.json`, `build_log.json`. Mechanical report records 72 sampled poses, no reported collision pairs, and linear closure errors up to 4e-7 m; angular metrics are mixed into a misleading `closure_max_err_m` container. Animation records forward/reverse checks and the expected nonperiodic small-wheel phase. Export notes/report record 43 meshes, 134,346 triangles and 13 materials. These are stored results, not fresh reruns or proof of physical/historical accuracy. Human video playback and Black 5 Unreal import remain unverified in the milestone notes.

## 7. Proposed shared toolkit structure

Do not move or refactor the existing scripts yet. Proposed small `Tools/Blender/` package:

```text
README.md                 # supported Blender version, safe invocation, scope
el_manifest.py            # units, axes, object map, source hash, evidence status
el_scale_qa.py            # measure bbox/rail contact; optional 1.8 m review figure
el_geometry.py            # selected bmesh primitives and explicit pivot transforms
el_motion_math.py         # pure math: crank, slider, circle closure, radius ratios
el_running_gear.py        # Blender adapter: configured axle/pin/rod/control maps
el_clearance.py           # sampled evaluated-mesh scans, exclusions and limits
el_preview.py             # configurable cameras, strips, state restoration
el_export.py              # explicit selection, derivative-only save, reimport report
el_materials.py           # simple materials and non-null slot validation
tests/                    # meaningful math and isolated Blender fixtures
```

Keep class configuration in the existing asset `Notes/`, not hard-coded in helpers. A configuration should specify units/axis/datum, 3 or 5 coupled axle centres, wheel radii, driven axle, crank radius, phase/quartering with confidence/source, rod endpoint maps, cylinder slide axis, lateral layers, review collections, allowed contact pairs and export selection. Fail on missing objects, unreachable linkage geometry or contradictory units; do not silently clamp an impossible mechanism into a plausible pose.

Pure maths should have no `bpy` dependency; Blender adapters may use `bpy/bmesh/mathutils`. Support the actual recorded 5.2.2 pipeline first and test other versions separately. Helpers should not write files on import, overwrite source, purge data or change global preferences. Every write takes explicit input/output paths, refuses the source path, and restores temporary scene state where practical.

Verification JSON should carry source/script hashes, Blender version, configuration, units per metric, sample coverage, exclusions, tolerances and failures. Separate linear closure, angular aim, sampled clearance and render/playback findings. Test forward/reverse/zero, offset cylinders, invalid lengths and 3/5-axle fixtures independently of a full locomotive. Compare results with the preserved B5 baseline before using extracted code in a new model. This proposes reusable helpers and checks, not a giant locomotive generator or production animation architecture.

## 8. Asset guide outline

The accompanying [ASSET_DEVELOPMENT_GUIDE.md](ASSET_DEVELOPMENT_GUIDE.md) is a concise draft helper covering discovery, references, folders, scale, milestones, running gear, checks, previews, export, Unreal handoff, research gaps, Git discipline, toolkit use and asset-specific decisions. It links to existing authority instead of replacing it. New toolkit/storage recommendations remain Proposed pending Manager approval.

## 9. Claude context-reduction plan

Actual local structure: 496-line `CLAUDE.md`, one project skill at `.claude/skills/early-locomotion-asset-specialist/SKILL.md`, and ignored `.claude/settings.local.json` containing a permissions section. No project `.claude/rules` or nested instruction system was found. Existing instructions use ordinary file references rather than an established `@` import chain.

| Load | Proposed content |
| --- | --- |
| Always | Compact role/authority boundaries, two roots, preserve unrelated work, discover workspace, no automatic commit, pointers to detailed rules. Keep current rules in force until a separately approved cleanup |
| Task-loaded | Asset guide, relevant specialist/workflow sections, current checkpoint and applicable design sections; export or research procedure only when needed |
| Asset-specific | ASSET_PATHS mapping, one class brief/source manifest, latest source/export notes, relevant verification JSON/scripts and current stage goal |

Current Claude documentation supports `@path` imports, but imports expand into context; importing every long authority file would not save tokens. Skills can keep the description available while loading the full procedure on invocation. Prefer short pointers and an asset skill that loads this guide and the selected class brief. Verify behavior in the installed Claude version before changing its configuration. [Claude memory/imports](https://code.claude.com/docs/en/memory), [Claude skills](https://code.claude.com/docs/en/skills)

**Conflicts to reconcile separately:** the asset skill still defaults to `Assets/Prototypes/Claude` and uses the old undated handoff header, whereas SPECIALIST_DELEGATION/ASSET_PATHS now specify discovery/reuse and the dated service/role header. `CLAUDE.md` also contains a separate legacy completion-report structure. The higher-priority delegation rules win; this audit does not silently rewrite specialist configuration. Avoid copying the new guide wholesale into CLAUDE.md or automatically importing the entire library.

## 10. GPT context-reduction plan

Start with current local INDEX/checkpoint and the scoped file map. Read only relevant sections of detailed authority, then the existing class brief and latest export notes. A task prompt needs objective, lineage/stage, input paths, constraints and acceptance checks—not the complete project history. A handoff should carry evidence paths, changed files and unresolved questions.

Use GitHub for commit/diff review only after identifying the repository and SHA and comparing freshness with local HEAD plus the dirty-file list. If local access is absent, label the result as remote-only and request/obtain current local evidence before reconciling authority. Inspect the library index before web research; update the existing brief when a genuine gap is filled. Use targeted search/Firecrawl only for those gaps, not for repeated class-level discovery.

## 11. Firecrawl research convention

Use ordinary search/browser reading for finding a small number of sources and judging images. Use Firecrawl selectively for extracting readable text/metadata from awkward public pages or a bounded set of catalogue pages; its scrape API can return Markdown and other formats. It does not authenticate a historical measurement, resolve image rights or replace visual inspection of a drawing. [Firecrawl scrape documentation](https://docs.firecrawl.dev/features/scrape)

For each retained item, record source URL, author/organisation, access date, licence/attribution, locomotive/configuration, view, modelling use, confidence and local filename/hash. Distinguish VERIFIED primary evidence, SECONDARY reports, INFERRED/PROVISIONAL geometry and UNKNOWN data; preserve disagreements. Check existing URLs and hashes before downloads. Save only useful permitted files; otherwise retain the link. Record inaccessible archive catalogue/drawing IDs and access limits, never dimensions invented from their titles. Keep raw bulk scrape dumps out of agent prompts and normal Git checkpoints. Update the class brief and manifest with concise evidence. No private project uploads to external research tools are needed.

## 12. Risks / blockers

- First publication still needs repository/visibility approval, full-history secret/privacy review and source redistribution review. No remote backup is presently verified.
- Shared ignore policy is missing; local-only Claude settings currently rely on a user-global rule. Propose portable exclusions in a separate approved change.
- Six pre-existing documentation edits and 357 untracked files make broad staging unsafe. The old installer remains in reachable history; no cleanup was performed.
- Missing Pannie/Stage A builders make blanket “generated, discardable” classification unsafe. Stage B is source-dependent, not a from-scratch generator.
- Current scripts contain class names, absolute paths, destructive in-memory operations and overwriteable destinations. Do not bulk-import/run them as a toolkit.
- Sampled geometry checks and visually plausible gear do not prove continuous clearance, real valve timing, engine animation or production readiness. Current JSON lacks complete provenance and has mixed-unit naming.
- Stale local skill/completion instructions need a focused governance follow-up. This report does not alter their behavior.
- Current runtime/architecture and Open Questions remain exactly as recorded in canonical files; tooling reuse cannot settle them.

## 13. Recommended implementation sequence

1. Manager reviews this report and draft guide; reconcile the small skill/header conflicts separately.
2. Agree narrow shared exclusions, retained asset milestones and redistribution/privacy scope. Preserve untracked work in an independent backup before any storage cleanup.
3. Checkpoint approved docs/scripts by explicit path, separately from reviewed assets. Authorise remote owner/visibility and run dedicated history scanning before first push.
4. Decide ordinary Git versus selective LFS from retained-file size/churn and available budget; no migration unless specifically approved.
5. Extract measurement/reporting and pure motion maths first, with provenance and real failure criteria. Validate on small fixtures, then preserved B5/Pannie copies in scratch; never overwrite milestones.
6. Add configurable preview/export/reimport helpers. Only then consider reusable visual Walschaerts helpers, with asset-specific geometry and limitations explicit.

## 14. Do now / Do later / Do not do yet

**Do now:** review the audit/guide and corrected Black 5 navigation; preserve current assets and pending work; keep handoffs short and evidence-linked.

**Do later, with scoped approval:** reconcile the skill, add shared exclusions, checkpoint selected files, configure GitHub, consider LFS, extract/test helpers and recover missing builders if available.

**Do not do yet:** broad `git add -A`, upload the whole tree, rewrite history, enable/migrate LFS, remove backups/previews, move binaries, run live builders, change SML or select gameplay/architecture.

### Verification boundary

The task's intended changes are exactly this report, the draft guide and two stale Black 5 status sentences in ASSET_PATHS. Existing pending authority edits remain separate. Final verification: all 407 other baseline files matched their SHA-256 hashes; no baseline path was removed and no binary moved or changed. Git config, index, HEAD, local exclusions and absent attributes/ignore/LFS configuration matched the baseline. Local document links passed and git diff --check passed (only the pre-existing SPECIALIST_DELEGATION LF/CRLF warning). Final status retains the same six modified tracked files and pre-existing untracked work, plus the two new documents; ASSET_PATHS was already untracked. Nothing staged, committed or pushed.
