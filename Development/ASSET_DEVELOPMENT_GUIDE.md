# Asset development guide

**Current shared workflow helper — 4 October 2026.** Summarises established rules and verified workflow lessons; subordinate to SPECIALIST_DELEGATION.md and the existing authority order. It is not gameplay/design authority and does not approve production assets. Toolkit extraction, GitHub publication and final binary/LFS policy remain proposals in [the readiness report](SHARED_TOOLING_AND_GITHUB_READINESS.md).

Authority and detailed rules: [INDEX](../INDEX.md), [canonical design](../Design/GAME_DESIGN.md), [WORKFLOW](../WORKFLOW.md), [specialist delegation](SPECIALIST_DELEGATION.md), [Claude implementation rules](../CLAUDE.md). Preserve Agreed / Proposed / Playtest Target / Superseded / Open Question. Specialist output does not become project truth without review.

## 1. Discover the workspace

Read [ASSET_PATHS](../Blender/ASSET_PATHS.md) and inspect `Blender/`, `Assets/` and existing reference packs. Reuse one workspace per lineage. Pannie and Black 5 have existing populated workspaces; a new stage is not a new root. The canonical root is the Early Locomotion project; `C:\SML` is separate and requires its own task authority.

## 2. Use the reference pack

Read the selected class brief, must-follow images, source manifest and prior-stage Notes/export notes before researching or editing. Keep one coherent visual configuration. Separate verified measurements from secondary, inferred, provisional and unknown values. Reference scale is not gameplay balance; a visually convincing prototype is not proof of historical accuracy.

## 3. Preserve the folder roles

Use `Source/` for editable milestones, `Export/` for derivatives, `Export/FBX/` for interchange, `Previews/` for review evidence and `Notes/` for scripts, measurements and export notes. External research stays in the mapped `Asset References/` workspace. Respect compatibility-path exceptions in ASSET_PATHS; do not copy documentation or create parallel roots to make old paths appear current.

## 4. Make scale explicit

Pannie/Black 5 use metric real-world scale, 1 Blender unit = 1 m, +X forward, +Y left, +Z up, origin at track centre/rail head/middle driving axle. Record the actual convention per asset rather than assuming all future stock shares that origin. Check overall dimensions, axle centres, wheel tread versus flange and a 1.8 m review figure. Exclude review helpers from export.

## 5. Keep meaningful milestones

Preserve the previous approved/tested source and create a clearly named stage/version. Keep the builder or edit script and parameters with the new milestone. `.blend1` is an automatic backup, not milestone naming; do not delete existing backups without approval. Missing historical builders make source preservation especially important.

## 6. Make motion understandable

Name controls, parts, collections and pivots by role. Record the master wheel angle, driven axle, crank radius, phase/quartering, rod endpoints, slide axes and rolling ratios. Keep mechanics configurable and editable. Mark assumed link lengths and visual-only valve gear; do not reuse Black 5 constants as historical facts for another class.

## 7. Verify geometry and motion

Check scale, transforms, pivot positions, non-null materials and mesh/triangle totals. Sweep forward/reverse motion, check rod closure, quartering, crosshead paths and loop boundaries. Record sample density, excluded contact pairs and units for numerical/BVH checks. Sampled no-overlap findings are not continuous collision guarantees. Saved reports describe the tested source only; future reports should include source/script hashes.

## 8. Prepare a small review pack

Include silhouette, front/rear three-quarter, useful detail and scale views, plus a motion-position strip and relevant comparison. Inspect the actual renders. Distinguish numeric checks, image review, encoded-video validation and human playback. Avoid retaining every temporary render as a milestone.

## 9. Export from a derivative

Preserve the editable source. Use explicit export selection and a separate output path; keep moving meshes/pivots where required by the approved handoff. Record axes, units, materials, dimensions and options. Fresh-scene reimport checks counts, transforms, dimensions, pivots and unwanted helpers. Current Pannie/Black 5 FBXs are rest-pose exports: Blender drivers/constraints are not transferred as playable animation.

## 10. Make the Unreal handoff truthful

Provide source/export paths, version/hash, part/motion map, scale, dependencies, verification and remaining work. Export/reimport success does not prove Unreal import, collision, runtime motion or production readiness. Engine asset edits, packaging and deployment need their own authorised scope. Do not alter compatibility paths casually.

## 11. Research only the gaps

Search existing briefs first. Use browser/search or Firecrawl for a bounded missing fact; preserve URLs, attribution/licence and configuration caveats. Do not fabricate unavailable GA dimensions. Update the brief rather than pasting a research dump into the next prompt.

## 12. Keep Git changes deliberate

Inspect status/diff before and after work; preserve unrelated files. Commit only when authorised and stage explicit paths. Ordinary text/scripts/docs use normal Git. Large binary sources/assets are candidates for Git LFS pending separate approval; LFS is not enabled. Clearly disposable/local output is excluded only by the narrow [repository ignore rules](../.gitignore). Existing automatic Blender backups remain on disk but are ignored; named .blend milestones, FBX exports, retained previews and reference packs remain eligible. Broader binary retention/exclusion rules remain pending; ignoring is not deletion or backup. Local current files remain canonical; remote history must be identified by commit and checked for freshness.

## 13. Reuse tooling carefully

The proposed `Tools/Blender/` toolkit is not installed. Consult the [actual script inventory](SHARED_TOOLING_AND_GITHUB_READINESS.md#6-reusable-blender-tooling-inventory) before extracting helpers. Existing Stage B scripts are asset-specific and may overwrite outputs; do not treat them as safe library imports. Start with verified maths/reporting and explicit configuration, then test on isolated copies.

## 14. Keep asset-specific decisions local

Silhouette, fittings, wheel/axle layout, cylinder/gear type, handedness evidence, cab/tender geometry, materials, triangle budget and production export contract remain asset-specific. Record assumptions in that asset's Notes/brief. Use the current dated service/role handoff from SPECIALIST_DELEGATION; report limitations and decisions needing Manager review.
