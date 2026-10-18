# ASSET MANIFEST — Early Locomotion explainer deck

Written 18 October 2026. One row per image actually used (19 photos, 5 mod renders; the brief allowed about 30 and 15). Every original path was checked to exist on disk on this date; every bundle copy exists in `Reporting/Claude Presents/images/`.

## Read this first

- **The images are not on GitHub yet.** Only the seven Jinty photos under `Asset References/Locomotives/LMS Fowler Class 3F Jinty/` and no `Blender/` renders are tracked in git (checked with read-only `git ls-files`). The cloud build session can only see what is pushed, so Stage 1 saved web-sized copies in `Reporting/Claude Presents/images/` (about 5 MB in total). **The coordinator must commit and push that folder to `claude-presents`.** Stage 2 should embed the bundle copies (the `Bundle path` column), never the original paths.
- **Publishing is the owner's decision.** The repo is public, and these photos are third-party Creative Commons works. Several infrastructure manifests record: "Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task" (see the `Repo note` column). Their licences allow redistribution with credit, but the owner should confirm before the images are pushed.
- **Licences are copied exactly as recorded** in each `PHOTO_REFERENCES.md`, `SOURCE_MANIFEST.json` or `notes.md`. None is UNCLEAR. CC BY-SA means share-alike: the copies here are unmodified apart from resizing, each with its credit, and the deck should say so (slides 41 and 42 do). Where a choice existed, CC BY was preferred over CC BY-SA (the BY-SA photos are used only where no BY photo showed the subject).
- **Mod renders** have no separate licence recorded. They are project-owned and approved for this deck in the brief. R01 is an early yellow test model ("visual probe") and must not be presented as a final or Small-class design. R02 and R05 are high-detail visual development that is not Unreal-tested or production-ready.
- Pixel sizes: `Original` is the file in the repo; `Bundle` is the copy to embed. Bundle copies are the originals unchanged when the original was already 1,280 px or smaller on the long edge and under 600 KB; otherwise they are resized (JPEG, quality 85–90).

## Photographs

| Slot | Bundle path | Original path (repo-relative) | What it shows (also the alt text) | Credit / licence (as recorded) | Source URL | Slides | Original px | Bundle px | KB | Tracked in git | Repo note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | `images/P01_oxenhope_chairs.jpg` | `Asset References/British_Heritage_Track/Photos/P01_Oxenhope_Chairs.jpg` | Old-style chairs and clips holding rail to wooden sleepers on preserved track at Oxenhope. | Stephen Craven; CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Old_style_rail_clips_at_Oxenhope_-_geograph.org.uk_-_5380435.jpg | 6 | 640 x 480 | 640 x 480 | 119 | no | permitted subject to attribution and applicable ShareAlike |
| P02 | `images/P02_sheffield_park_track.jpg` | `Asset References/British_Heritage_Track/Photos/P03_Sheffield_Park_Track.jpg` | Full-size railway track at Sheffield Park station: rails, sleepers and ballast. | James E. Petts; CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Track_at_Sheffield_Park.jpg | 17 | 960 x 720 | 960 x 720 | 206 | no | permitted subject to attribution and applicable ShareAlike |
| P03 | `images/P03_9f_valve_gear.jpg` | `Asset References/Locomotives/BR Standard Class 9F/Images/92203_valve_gear_closeup_22444365.jpg` | Outside valve gear, rods and crosshead on the side of BR Standard 9F No. 92203. | Ben Salter from Wales.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Valve_gear_(530245247).jpg | 7 | 800 x 533 | 800 x 533 | 424 | no | not recorded |
| P04 | `images/P04_tender_engine_73082.jpg` | `Asset References/Locomotives/BR_Standard_5/Images/73082_side_profile_172810787.jpg` | BR Standard Class 5 No. 73082 'Camelot', a tender engine, seen from the side. | www.mgaylard.co.uk and thanks for looking.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:73082_Camelot_British_Railways_Standard_Class_5_4-6-0_-_54304789041.jpg | 9 | 960 x 639 | 960 x 639 | 263 | no | not recorded |
| P05 | `images/P05_tank_engine_80151.jpg` | `Asset References/Locomotives/BR_Standard_4_2-6-4T/Images/80151_side_profile_172811139.jpg` | BR Standard Class 4 tank engine No. 80151 from the side, showing side tanks and rear bunker. | www.mgaylard.co.uk and thanks for looking.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:British_Railways_Standard_Class_4MT_2-6-4_Tank_Locomotive_No._80151_-_54303345950.jpg | 9 | 960 x 639 | 960 x 639 | 295 | no | not recorded |
| P06 | `images/P06_water_crane_didcot.jpg` | `Asset References/Service Equipment/Water_Servicing/Photos/Didcot_Railway_Centre_Water_4714616590__42351443.jpg` | A water crane at Didcot Railway Centre. | Barry Skeates from newbury, UK; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Didcot_Railway_Centre_Water_(4714616590).jpg | 10 | 1280 x 2309 | 710 x 1280 | 186 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P07 | `images/P07_water_tower_signal.jpg` | `Asset References/Service Equipment/Water_Servicing/Photos/Signal_and_Water_Tower_3715807921__26938449.jpg` | A water tower with a signal beside it. | David Merrett from Daventry, England; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Signal_and_Water_Tower_(3715807921).jpg | 10 | 1280 x 1925 | 851 x 1280 | 246 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P08 | `images/P08_coaling_stage_didcot.jpg` | `Asset References/Service Equipment/Coaling_Infrastructure/Photos/Coaling_stage_GWS_Didcot-9940117084_55817092.jpg` | A raised coaling stage at the Great Western Society site, Didcot. | Gillett's Crossing; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Coaling_stage,_GWS_Didcot-9940117084.jpg | 11 | 1280 x 960 | 1280 x 960 | 289 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P09 | `images/P09_coaling_tower_carnforth.jpg` | `Asset References/Service Equipment/Coaling_Infrastructure/Photos/Carnforth_Ash_plant_water_tower_and_Cenotaph_coaling_tower_175333935.jpg` | A tall coaling tower and a water tower at Carnforth. | kitmasterbloke; CC BY 4.0 | https://commons.wikimedia.org/wiki/File:Carnforth_Ash_plant,_water_tower_and_Cenotaph_coaling_tower.jpg | 11 | 1280 x 486 | 1280 x 486 | 171 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P10 | `images/P10_jinty_47406.jpg` | `Asset References/Locomotives/LMS Fowler Class 3F Jinty/02-47406-front-three-quarter.jpg` | LMS Fowler Class 3F 'Jinty' tank engine No. 47406 at the Great Central Railway. A related Fowler tank engine, NOT the Dock Tank. | Duncan Harris; CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:47406_Great_Central_Railway_(2).jpg | 19 | 3200 x 2304 | 1280 x 922 | 245 | yes | not recorded in notes.md |
| P11 | `images/P11_merchant_navy_35005.jpg` | `Asset References/Locomotives/SR Merchant Navy/Images/35005_elevated_front_106432617.jpg` | Merchant Navy class No. 35005 'Canadian Pacific', raised front three-quarter view showing boiler and tender. | kitmasterbloke.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:35005_Canadian_Pacific_at_Loughborough_1993.jpg | 20 | 960 x 589 | 960 x 589 | 198 | no | not recorded |
| P12 | `images/P12_9f_92203.jpg` | `Asset References/Locomotives/BR Standard Class 9F/Images/92203_front_three_quarter_9963772.jpg` | BR Standard 9F No. 92203 at Toddington, front three-quarter view. | Tony Hisgett from Birmingham, UK.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:92203_at_Toddington_on_the_Gloucestershire_and_Warwickshire_Railway_(3).jpg | 21 | 960 x 620 | 960 x 620 | 170 | no | not recorded |
| P13 | `images/P13_distant_signal_henley.jpg` | `Asset References/Semaphore Signals/Focused_Family/Photos/Semaphore_distant_signal_on_the_approach_to_Henley_in_Arden._-_geograph.org.uk_-_11867.jpg` | A semaphore distant signal beside the line near Henley-in-Arden, arm raised. | Richard Dunn; CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Semaphore_distant_signal_on_the_approach_to_Henley_in_Arden._-_geograph.org.uk_-_11867.jpg | 29 | 640 x 499 | 640 x 499 | 123 | no | not recorded |
| P14 | `images/P14_williton_signal_box.jpg` | `Asset References/Signal Boxes/Photos/Williton_Signal_Box_-_November_2014_160121943.jpg` | Williton signal box on the West Somerset Railway. | Reading Tom; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Williton_Signal_Box_-_November_2014.jpg | 30 | 1280 x 1707 | 960 x 1280 | 251 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P15 | `images/P15_lever_frame_didcot.jpg` | `Asset References/Signal Boxes/Photos/Signalbox_workings_Didcot_Railway_Centre_-_geograph_org_uk_-_658545_13196511.jpg` | Lever frame and workings inside a signal box at Didcot Railway Centre. | Nigel Brown; CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Signalbox_workings,_Didcot_Railway_Centre_-_geograph.org.uk_-_658545.jpg | 30 | 640 x 480 | 640 x 480 | 151 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P16 | `images/P16_williton_rods_wires.jpg` | `Asset References/Mechanical_Signalling_Linkages/Photos/Williton_railway_station_MMB_10_20093256.jpg` | Pulleys, rods and wires of mechanical signal linkage beside the track at Williton station. | mattbuck (category); CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Williton_railway_station_MMB_10.jpg | 33 | 1280 x 853 | 1280 x 853 | 394 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P17 | `images/P17_coal_stage_water_tank_didcot.jpg` | `Asset References/Service Equipment/Coaling_Infrastructure/Photos/Coal_stage_and_water_tank_Didcot_Railway_Centre_England_80532940.jpg` | A coal stage and a water tank at Didcot Railway Centre. | Rosser1954; CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Coal_stage_and_water_tank,_Didcot_Railway_Centre,_England.jpg | 25 | 1280 x 719 | 1280 x 719 | 210 | no | Allowed subject to attribution and applicable ShareAlike; NOT authorised to publish in this task |
| P18 | `images/P18_lms_tender.jpg` | `Asset References/Locomotives/LMS_Fowler_4F/Images/44422_detached_tender_47638834.jpg` | A detached LMS tender at Norton Fitzwarren. Comparison only: not any particular engine's tender. | Geof Sheppard.; CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Norton_Fitzwarren_-_LMS_tender.JPG | 24 | 960 x 640 | 960 x 640 | 194 | no | not recorded |
| P19 | `images/P19_west_country_34007.jpg` | `Asset References/Locomotives/SR_West_Country_Battle_of_Britain/Images/34007_side_three_quarter_22444402.jpg` | Southern Railway West Country class No. 34007, side three-quarter view. | Ben Salter from Wales.; CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Out_in_the_open_(530236847)_(2).jpg | 36 | 800 x 533 | 800 x 533 | 516 | no | not recorded |

## Mod renders

Credit line to print: "Early Locomotion project render. Early test model, not final art." No third-party licence applies.

| Slot | Bundle path | Original path (repo-relative) | What it shows (also the alt text) | Slides | Original px | Bundle px | KB | Tracked in git |
|---|---|---|---|---|---|---|---|---|
| R01 | `images/R01_pannier_visual_probe_v004.jpg` | `Blender/Pannie/Previews/v004_Previews/SVP_v004_05_front_three_quarter.png` | Early test model of a tank engine (a yellow 'visual probe') on a short length of track. Not final art. | 1, 3, 39 | 1800 x 1000 | 1280 x 711 | 71 | no |
| R02 | `images/R02_track_hero_hd_v004.jpg` | `Blender/Track/Previews/StageC1_HD_v004/hero_lit_v004.png` | High-detail render of the mod's two-rail track. Visual development only: not Unreal-tested, not production-ready. | 17, 39 | 1600 x 900 | 1280 x 720 | 49 | no |
| R03 | `images/R03_semaphore_stop.jpg` | `Blender/Semaphore/Previews/StageA_Building_v001/STOP_Signal/STOP_01_full_front34_ON.png` | The mod's semaphore stop signal model with its arm flat (stop). | 29 | 1280 x 960 | 1280 x 960 | 50 | no |
| R04 | `images/R04_semaphore_clear.jpg` | `Blender/Semaphore/Previews/StageA_Building_v001/STOP_Signal/STOP_02_full_front34_OFF.png` | The same signal model with its arm raised (clear). | 29 | 1280 x 960 | 1280 x 960 | 52 | no |
| R05 | `images/R05_track_chairs_hd_v004.jpg` | `Blender/Track/Previews/StageC1_HD_v004/chair_field_lit_v004.png` | Close-up render of the mod's track: rail seated in a chair bolted to a sleeper. Visual development only. | 17 | 1200 x 900 | 1200 x 900 | 67 | no |

## Slide-to-image map

| Slide | Slots |
|---|---|
| 1 | R01 |
| 3 | R01 |
| 6 | P01 |
| 7 | P03 |
| 9 | P04, P05 |
| 10 | P06, P07 |
| 11 | P08, P09 |
| 17 | P02, R02, R05 |
| 19 | P10 |
| 20 | P11 |
| 21 | P12 |
| 24 | P18 |
| 25 | P17 |
| 29 | P13, R03, R04 |
| 30 | P14, P15 |
| 33 | P16 |
| 36 | P19 |
| 39 | R01, R02 |
| 41 | credits for P01 to P12 |
| 42 | credits for P13 to P19 and R01 to R05 |

## Credit text for slides 41 and 42

Print one row per slot as: `Slot | Slide | Author, licence | Source link`. Short author form for the slide: strip the trailing full stop and the "from <place>" tail (for example "Tony Hisgett"). Make the source link a hyperlink on the word "Commons".

| Slot | Slide credit text | Link |
|---|---|---|
| P01 | Stephen Craven, CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Old_style_rail_clips_at_Oxenhope_-_geograph.org.uk_-_5380435.jpg |
| P02 | James E. Petts, CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Track_at_Sheffield_Park.jpg |
| P03 | Ben Salter, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Valve_gear_(530245247).jpg |
| P04 | www.mgaylard.co.uk, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:73082_Camelot_British_Railways_Standard_Class_5_4-6-0_-_54304789041.jpg |
| P05 | www.mgaylard.co.uk, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:British_Railways_Standard_Class_4MT_2-6-4_Tank_Locomotive_No._80151_-_54303345950.jpg |
| P06 | Barry Skeates, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Didcot_Railway_Centre_Water_(4714616590).jpg |
| P07 | David Merrett, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Signal_and_Water_Tower_(3715807921).jpg |
| P08 | Gillett's Crossing, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Coaling_stage,_GWS_Didcot-9940117084.jpg |
| P09 | kitmasterbloke, CC BY 4.0 | https://commons.wikimedia.org/wiki/File:Carnforth_Ash_plant,_water_tower_and_Cenotaph_coaling_tower.jpg |
| P10 | Duncan Harris, CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:47406_Great_Central_Railway_(2).jpg |
| P11 | kitmasterbloke, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:35005_Canadian_Pacific_at_Loughborough_1993.jpg |
| P12 | Tony Hisgett, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:92203_at_Toddington_on_the_Gloucestershire_and_Warwickshire_Railway_(3).jpg |
| P13 | Richard Dunn, CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Semaphore_distant_signal_on_the_approach_to_Henley_in_Arden._-_geograph.org.uk_-_11867.jpg |
| P14 | Reading Tom, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Williton_Signal_Box_-_November_2014.jpg |
| P15 | Nigel Brown, CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Signalbox_workings,_Didcot_Railway_Centre_-_geograph.org.uk_-_658545.jpg |
| P16 | mattbuck (category), CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Williton_railway_station_MMB_10.jpg |
| P17 | Rosser1954, CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Coal_stage_and_water_tank,_Didcot_Railway_Centre,_England.jpg |
| P18 | Geof Sheppard, CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Norton_Fitzwarren_-_LMS_tender.JPG |
| P19 | Ben Salter, CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Out_in_the_open_(530236847)_(2).jpg |

## Considered and excluded

- `Semaphore Signals/Focused_Family/Sheets/*.jpg` (four sheets): AI-generated reference sheets (credit line "OpenAI GPT OP for Satisfactory"). Excluded so the deck shows no AI-generated imagery.
- `British_Heritage_Track/Photos/P08_Loose_Chair_CC0.jpg`: listed in its manifest but the file is missing on disk.
- `Semaphore Signals/Focused_Family/Photos/Combined_Home_and_Distant_Signal_...jpg` (10 MB), `Consall_loop_bracket_signal.jpg` (2.7 MB) and `Signal_post_at_Harmans_Cross...jpg` (1.6 MB): very large. Not needed; P13 serves slide 29.
- `Signal Boxes/Photos/Arley_Signal_Box...jpg` (several): good alternatives for slide 30 if the owner prefers a different box. Not used.
- `Locomotives/LMS_Stanier_Black_5/` previews and every other Blender preview: not used. No `.blend` file was opened.
- No photo of the LMS Fowler Dock Tank exists in the repo (none preserved). Slide 19 uses a Jinty and says so.
- No in-game Satisfactory screenshots were found or used (none needed: slide 4 is a native diagram).

