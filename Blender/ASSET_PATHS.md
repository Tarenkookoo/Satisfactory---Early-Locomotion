# Asset workspace paths

Verified 03 October 2026. Storage/navigation only; these identities do not select gameplay classes or production art. Detailed workspace policy: `Development/SPECIALIST_DELEGATION.md`. Paths below are relative to the canonical project root.

## Current working folders

| Lineage | Working workspace | Separate references |
| --- | --- | --- |
| Yellow Pannier / Pannie | `Blender/Pannie/` | `Asset References/Steam_Visual_Probe_1_Yellow_Pannier/` |
| LMS Stanier Black 5 | `Blender/LMS_Stanier_Black_5/` (Stage A v001 and Stage B v002 visual prototypes present) | `Asset References/LMS_Stanier_Black_5/` |
| Earlier Jinty capability tests | `Blender/Jinty_Prototype/` | `Asset References/Locomotives/LMS Fowler Class 3F Jinty/` |

Pannie and Jinty use `Source/`, `Export/FBX/`, `Previews/` and `Notes/` as applicable. Black 5 now has Stage A/Stage B sources, export derivatives, FBXs, previews and notes; Stage B build scripts and verification JSON are preserved under Notes/. These remain visual prototypes, with Unreal import unverified in their export notes. Empty folders are local preparation; they are not tracked by Git unless populated. No new binary-storage or Git LFS policy is introduced.

## Relocation mapping

- Loose Pannier base/Stage A and refined v002/v003/v004 `.blend` files, including the base `.blend1`, moved to `Blender/Pannie/Source/` with original filenames.
- Pannier export-preparation `.blend` derivatives v001–v004 moved to `Blender/Pannie/Export/`.
- FBXs v003/v004 moved to `Blender/Pannie/Export/FBX/`.
- Stage A previews moved from `Assets/Prototypes/Claude/Steam_Visual_Probe_Yellow_Pannier_Previews/` to `Blender/Pannie/Previews/Stage_A/`.
- The six loose v001 export-preview images moved from `Assets/Prototypes/Claude/Steam_Visual_Probe_Yellow_Pannier_Export/` to `Blender/Pannie/Previews/Export_v001/`; v002/v003/v004 preview subfolders moved to `Blender/Pannie/Previews/` retaining their names.
- `EXPORT_NOTES.md` and `EXPORT_NOTES_v002.md` through `EXPORT_NOTES_v004.md` moved to `Blender/Pannie/Notes/`. Their contents are preserved as milestone records; their original path listings are historical. Use this mapping for current source/export/preview locations rather than recreating the old folders.
- `Jinty_Blockout_Test.blend`, `Jinty_Blockout_V2.blend` and both `.blend1` backups moved to `Blender/Jinty_Prototype/Source/`.
- `Assets/Prototypes/Claude/Jinty_Blockout_V2_Previews/` moved to `Blender/Jinty_Prototype/Previews/Jinty_Blockout_V2_Previews/`.

## Retained compatibility paths and exceptions

- `Assets/Prototypes/Claude/Steam_Visual_Probe_Yellow_Pannier_Export/SVP_YellowPannier_v001.fbx` and `SVP_YellowPannier_v002.fbx` remain at their existing locations. Current Unreal import metadata references those paths; changing it would require asset edits outside this filesystem task. These are retained members of the Pannie lineage, not a second workspace. Do not create duplicate FBXs in the new folder.
- `Assets/Prototypes/Claude/Jinty_Blockout_Test_Previews/` remains because the V1 source stores an absolute render output there. It is mapped to the Jinty prototype lineage, not a competing workspace.
- With explicit Manager approval, `Blender/Blender Test.blend` and `.blend1` moved unchanged to `Blender/Legacy_Tests/Source/`, retaining both filenames. Both SHA-256 hashes matched before/after; the earlier protected-file relocation exception is cleared.
- Jinty V2 retains its pre-existing temporary render-output path. Before future rendering, review the output path in an authorised modelling task. Relocation did not change that absolute path.
- Blender files with built-in brush-library paths retain their existing absolute Blender installation dependency. No relative external-image or linked-library dependency was found that required changing a moved model.

## Preservation and authority

All 98 initially moved files and the two subsequently approved legacy/test files were checked by SHA-256 before and after relocation; contents were unchanged. No `.blend` file was resaved. Earlier milestones and legitimate backups remain present. Reference packs were neither moved nor duplicated. Historical documentation paths remain historical; use the current mappings above for new work. No SML file was modified. Files remain untracked where they were untracked before; nothing was staged or committed.
