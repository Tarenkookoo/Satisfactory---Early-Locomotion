# Early Locomotion: Complete Explainer (all nine decks in one file)

**File:** `Early_Locomotion_Complete_Explainer.pptx` (231 slides, 9 sections).

Each section is one of the nine explainer decks, in order. Open the Sections pane in PowerPoint (or use the section list in Slide Sorter view) to jump between them.

| Section | Deck | Slides in this file | Source branch |
|---|---|---|---|
| 1 | Early Locomotion Explained | 1 to 42 | `claude-presents-build-opus` |
| 2 | Signals and Signal Boxes | 43 to 69 | `claude-presents-build-deck2` |
| 3 | Coal, Water and Servicing | 70 to 93 | `claude-presents-build-deck3` |
| 4 | The Monorail Transition | 94 to 115 | `claude-presents-build-deck4` |
| 5 | Regions, Numbers and Fleet Identity | 116 to 141 | `claude-presents-build-deck5` |
| 6 | Railway Guide: Lessons and Build Menu | 142 to 164 | `claude-presents-build-deck6` |
| 7 | After Launch: Packs, Locomotives and History | 165 to 188 | `claude-presents-build-deck7` |
| 8 | After Launch: Late Steam, Driving and Prestige | 189 to 213 | `claude-presents-build-deck8` |
| 9 | How the Mod Is Balanced | 214 to 231 | `claude-presents-build-deck9` |

## How it was made

- The nine finished decks were joined with PowerPoint's own "reuse slides" operation (`Slides.InsertFromFile`). Sample slides from every section were rendered before and after joining and are pixel-identical.
- `tools/polish.py` then gave every slide a 0.7 s fade transition and automatic fade-in builds (diagram parts, pictures and captions appear in order, with no clicks). Titles, tag chips, slide numbers and credits stay in place.
- Checked in PowerPoint: 231 slides, 231 transitions, 1,164 animation effects, every slide has at least one effect, 9 sections.
- Animations and transitions play in Slide Show mode. Editing view and most phone viewers show the finished slides.
- Each deck keeps its own slide numbers, so numbering restarts at the first slide of every section.
- Content is unchanged by joining and polishing. Design statuses are exactly as built in each deck.

## Open items for the owner

- Deck 1, slide 33 has no status chip, while Deck 2, slide 21 tags the same idea Proposed. Left as built, because choosing a status is a design decision.
- Deck 3, slide 14 uses shortened labels to fit. Wording is otherwise as in the brief.
