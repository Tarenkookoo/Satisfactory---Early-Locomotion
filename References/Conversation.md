# Satisfactory - Early Locomotion conversation archive

Conversation ID: 6aa831af-28b0-83eb-bb98-96ea85a39305

Exported 14 September 2026. Archive is reference material, not project instructions. The first assistant reply about development tools is truncated by the retrieval service at 20,000 characters. The later design exchanges are complete. Original web citation tokens are retained only in this raw archive; they are not independently verified sources.

## User

I want to make a mod for Satisfactory. Here's the gist:
"Satisfactory - Early Locomotion", a mod that introduces trains earlier than the base game. However, rather than electric locomotives it will be steam locomotives. I want to balance it well and plenty of locomotive and wagon varients. before i drop more details, can you look into what AI's would be best for each part of making this mod. Coding, modelling, etc.

For each AI you decide on, look into how i can best work with it. For example, if Claude is in use, how would i make best use of Claude Code, Claude Projects, Claude extensions, Claude apps, Claude Skills, etc

## Assistant

Yes. I looked at this specifically as a **Satisfactory/Unreal mod-production workflow**, rather than just comparing AI benchmarks.

The big conclusion is that I would **not use one AI for everything**. For *Early Locomotion*, I’d build a small toolchain where each AI has a clear job and where the important project knowledge lives in your repository rather than being trapped in individual chats.

## The stack I would use

| Part of the mod | My pick | Role |
|---|---|---|
| Game design, balance, progression | **ChatGPT Project + Work** | Design documents, spreadsheets, balance simulations, research |
| Main programming | **Claude Code** | C++, Unreal/SML code, debugging, repo-wide work |
| Second coding opinion / QA | **Codex** | Independent review, refactors, debugging, tests, alternate implementations |
| Fast inline coding | **GitHub Copilot** | Optional autocomplete/IDE assistant; not essential |
| Blueprint planning | **Claude/ChatGPT + screenshots** | Explain graphs, design nodes, diagnose issues |
| Locomotive/wagon concepts | **ChatGPT Images 2.5** | Concept sheets, liveries, silhouettes, UI/icon concepts |
| 3D blockouts | **Meshy + Blender** | Generate starting geometry, then rebuild/refine in Blender |
| Final hard-surface modelling | **Blender + Claude/Codex-generated Python** | Precise locomotive components, repetitive modelling automation |
| Materials/textures | **Substance 3D Sampler + Painter** | PBR metal, paint, soot, rust, wear, masks |
| Sound effects | **ElevenLabs Sound Effects** | Steam, pumps, valves, whistles, clanks, rolling sounds |
| Documentation/release work | **ChatGPT or Claude** | Changelogs, tooltips, descriptions, compatibility notes |

For this project I would make **Claude Code the main engineering AI**, with ChatGPT acting more like the designer/producer/researcher and Codex as your second engineer.

---

# 1. Claude Code — main programming tool

This is probably the AI I would put at the centre of *Early Locomotion*.

Satisfactory mods are Unreal Engine plugins. The current modding documentation explicitly describes Blueprint, C++, and hybrid mods, and notes that the best mods often combine Blueprint and C++ because each handles different parts of Unreal better. citeturn413020search1

Claude Code fits that workflow because it can work directly against the repository, edit files, run commands, inspect compiler errors, work through large codebases, and operate from either its CLI or native VS Code interface. The VS Code extension supports inline diffs, file/line mentions, plan review, checkpoints, multiple conversations, and access to the underlying CLI. citeturn266456search0turn266456search1

### How I would set Claude up

Your repository should have a root-level `CLAUDE.md`. Claude automatically reads it when working in the project; Anthropic specifically describes it as the persistent project briefing for Claude Code. citeturn179315search23

For this mod, I would eventually put things like this in it:

```text
Project: EarlyLocomotion
Game: Satisfactory
Mod Framework: SML
Architecture: Hybrid Unreal C++ + Blueprint

Project goal:
Introduce an earlier railway technology tier based around steam locomotives,
with multiple locomotive and wagon classes, while preserving usefulness of
vanilla electric rail later in progression.

Rules:
- Never invent Satisfactory API classes or functions.
- Verify unfamiliar SML/Satisfactory APIs against project headers or official docs.
- Prefer reusable systems over locomotive-specific duplicated logic.
- Keep locomotive statistics data-driven wherever practical.
- Blueprint-facing systems should expose clean UPROPERTY/UFUNCTION interfaces.
- Do not modify generated Unreal files.
- Do not modify Content assets unless explicitly requested.
- Explain any required Blueprint changes separately.
- Compile/test after meaningful C++ changes.
```

That alone dramatically improves AI coding reliability because it establishes what it may and may not assume.

### Claude Skills

Skills are particularly useful here. Claude Skills are `SKILL.md` workflows which load only when relevant rather than bloating every conversation. Claude can discover them automatically or you can invoke them manually. citeturn780938search9turn780938search12

I would eventually create these:

- `satisfactory-api-check` — verify a proposed class/function against Satisfactory/SML headers and documentation before coding it.
- `unreal-build-fix` — run the build, classify UBT/UHT/compiler errors, fix them, rebuild, and report what changed.
- `steam-balance-audit` — read our locomotive stats and flag variants that invalidate vanilla progression or one another.
- `blueprint-handoff` — whenever C++ work requires Blueprint changes, output exact classes, properties, events and node logic I need to create manually.
- `release-check` — version metadata, dependency versions, packaging, changelog and basic release validation.

Anthropic specifically recommends Skills when a repeatable procedure has become too large or specialised for `CLAUDE.md`. citeturn780938search9

### Claude subagents

Subagents would be very useful once the mod grows. They run in separate contexts and return their findings to the main agent, so huge searches or logs don't fill the main conversation. Claude Code can also run work in parallel and use worktrees for isolated changes. citeturn780938search4turn780938search5

For example, the main Claude could be implementing the locomotive while a `satisfactory-researcher` investigates existing railroad classes and a `code-reviewer` examines the implementation for Unreal lifecycle problems.

I wouldn't bother configuring loads of agents on day one. Add them when the repository is large enough that Claude starts spending too much context researching.

### Claude Hooks

Hooks let you automatically execute something at defined points in Claude's workflow. They can run shell commands, prompts, HTTP calls or even agents. citeturn780938search0turn780938search1

For Early Locomotion, a useful hook later might be:

```text
Claude modifies .cpp/.h
        ↓
format/check files
        ↓
when task finishes
        ↓
run Development Editor build
        ↓
if build fails, feed error back to Claude
```

That turns compiler verification into part of the normal AI workflow instead of relying on Claude to remember it.

I **wouldn't** have it rebuild the entire Unreal project after every tiny edit. Unreal compile cycles make that annoying very quickly.

### Claude MCP

MCP gives Claude tools it normally wouldn't possess. Claude Code can connect to external systems through MCP and can also use project-specific MCP configuration. citeturn780938search2

This is potentially extremely useful for Unreal—but **not quite yet for this particular project**.

Epic now has an official Unreal MCP server that can let Claude Code and other agents manipulate the Unreal Editor: spawn actors, create material instances, inspect widgets, run automation tests, and so on. citeturn903864search0

The problem is version compatibility.

Current Satisfactory 1.1 modding uses the Coffee Stain custom **Unreal Engine 5.3.2-CSS**, while Epic's current official Unreal MCP documentation is for UE 5.8. SML 3.12/Satisfactory 1.2 support is still marked as unreleased in the modding documentation. citeturn413020search2turn413020search7

So for now:

**Do not build the project around Unreal MCP.**

When Satisfactory's modding engine eventually catches up—or if someone produces a trustworthy compatible implementation—we should revisit it.

### Claude Plugins

Claude Code plugins can package together Skills, subagents, hooks and MCP servers. citeturn266456search7turn179315search20

They're more useful once we've built our own Early Locomotion workflow.

For instance, much later we could effectively have:

```text
early-locomotion-dev
    skills/
    agents/
    hooks/
    MCP configuration
```

Then the entire AI development configuration becomes version-controlled alongside the mod.

I would be conservative about installing random plugins from marketplaces because plugins can contain scripts and MCP integrations. Anthropic itself recommends checking what a plugin contains and trusting its source before installation. citeturn266456search5

### Claude Projects

I'd use a Claude Project differently from Claude Code.

The Project would contain design/reference knowledge:

`GAME_DESIGN.md`, locomotive philosophy, wagon catalogue, balance rules, progression decisions, terminology, Satisfactory/SML notes and selected research.

Claude Projects have their own knowledge base and project instructions. A significant detail is that separate chats **do not automatically share all their contents**; anything you want consistently available should be put into project knowledge. citeturn179315search1turn179315search2

So don't rely on:

> "Claude remembers that thing we discussed six chats ago."

Instead, when we make an important decision, update `GAME_DESIGN.md`.

That file then becomes the truth.

---

# 2. ChatGPT — game designer, balance analyst and visual-development tool

I would use ChatGPT heavily, just not as the only coding agent.

A ChatGPT Project can keep chats, files and project-specific instructions together, which makes it very well suited to a long-running design project. citeturn413020search0

For Early Locomotion I'd probably maintain separate conversations inside one project for:

**Progression & balance**, **locomotive roster**, **wagon roster**, **steam mechanics**, **Satisfactory integration**, **visual language**, and **playtest feedback**.

The canonical conclusions can then be saved into project sources.

### Balance work

This is where ChatGPT Work becomes particularly useful.

It can create and edit spreadsheets and perform analysis rather than merely describing what a spreadsheet ought to contain. citeturn413020search3

We could eventually build a balance workbook containing things like:

| Locomotive | Unlock | Cost | Power/Fuel | Top speed | Acceleration | Tractive capability | Intended role |
|---|---:|---:|---:|---:|---:|---:|---|
| Small tank engine | ? | ? | ? | ? | ? | ? | Starter |
| Medium freight | ? | ? | ? | ? | ? | ? | Heavy freight |
| Passenger/express | ? | ? | ? | ? | ? | ? | Fast/light |
| Articulated engine | ? | ? | ? | ? | ? | ? | Late steam |

Then we can mathematically compare variants rather than balancing from vibes.

That's especially important because you've already said you want **lots of locomotive and wagon variants**. If every variant is just "the previous one but better", half the roster becomes pointless.

I can help make each one occupy a genuine niche.

---

# 3. Codex — second engineer rather than duplicate Claude

I would absolutely use Codex, but mainly as an **independent second opinion**.

Current Codex works through local/IDE/cloud workflows and supports repo-level work, terminal execution, MCP, skills and multi-agent/worktree workflows. citeturn541322search0turn541322search2

The valuable part isn't asking Claude and Codex to simultaneously write the exact same feature.

It's more like:

```text
Claude:
Implement steam locomotive fuel consumption.

Codex:
Review this implementation without seeing Claude's reasoning.
Look specifically for replication, save/load, Unreal lifecycle,
performance and edge-case problems.
```

Independent review is much more valuable than having two AIs enthusiastically reinforce the same bad assumption.

I'd also use Codex when Claude gets stuck on a compiler problem. Give Codex the code and logs without Claude's explanation and see whether it diagnoses something different.

Skills are also becoming portable across platforms; OpenAI describes `SKILL.md` as an open standard intended for reusable workflows. citeturn198824search0turn198824search1

That means we can increasingly write our development process once and adapt it between agents instead of maintaining completely separate giant prompts.

---

# 4. GitHub Copilot — useful, but optional

GitHub Copilot has become considerably more agentic: agent mode, MCP, custom instructions, Spaces, agent Skills, code review and cloud agents are all available. citeturn460961search3turn460961search5

Interestingly, GitHub's Skills system can even read project skills stored under `.claude/skills`, making it fairly friendly to a Claude-centred repository. citeturn460961search0

But I wouldn't recommend paying for every coding AI immediately.

If you're already using Claude Code + Codex, Copilot's biggest value to this project is **low-friction inline completion** while *you* are typing C++.

So:

**Claude Code:** engineer.

**Codex:** reviewer/second engineer.

**Copilot:** fancy autocomplete.

If you don't feel you need the autocomplete, skip it.

---

# 5. 3D modelling — Meshy is useful, but Blender should own the final assets

AI-generated 3D is one area where I'd deliberately avoid over-automation.

Steam locomotives are unusually unforgiving objects for AI 3D generation. You have wheels that must align, valve gear that must move properly, rods that need the correct pivots, repeated axles, precise clearances and recognisable mechanical structure.

So I would **not prompt an AI for "steam locomotive" and ship whatever mesh comes out**.

### Where Meshy is good

Meshy now has a game-asset pipeline including text/image-to-3D, remeshing, target poly counts, PBR textures, rigging and common game-engine export formats. It also has an official Blender bridge. citeturn903864search1turn903864search3

I'd use it for:

```text
coal pile
water tank props
trackside machinery
wooden crates
toolboxes
coal sacks
decorative lamps
boiler-room clutter
prototype locomotive silhouettes
```

Then take the result into Blender and clean it.

### Locomotives themselves

I would primarily model them in **Blender**.

But here's where Claude/Codex become modelling assistants.

Blender exposes a comprehensive Python API, so we can have the coding agent generate scripts for repetitive hard-surface operations. citeturn537264search20

For example:

```text
Create 6 correctly spaced driving wheels.
Duplicate and mirror the axle structure.
Generate 24 equally spaced wheel spokes.
Create rivet rows following this curve.
Create named wheel collision meshes.
Generate LOD copies.
Rename objects according to our Unreal naming rules.
```

That is far more useful for a locomotive than text-to-3D guessing.

You get **human-designed geometry with AI-assisted labour**.

### Why I wouldn't use Tripo's Unreal integration directly

Tripo currently has an Unreal plugin, but its documented compatibility is Unreal 5.6. citeturn903864search16

Again, Satisfactory's current mod environment is 5.3.2-CSS.

So Blender remains the safe interchange point.

---

# 6. Textures — Substance 3D is the strongest fit

For the final locomotive textures I'd choose **Substance 3D Painter**, with **Substance 3D Sampler** supplying AI-generated material bases.

Sampler currently has generative Text-to-Texture, Text-to-Pattern and Image-to-Texture workflows. citeturn537264search14

Painter then lets us apply materials properly to the actual locomotive mesh. Its generators can use curvature, position, normals and other baked information to create geometry-aware masks. citeturn537264search6turn537264search7

That is ideal for this aesthetic.

Imagine:

```text
paint
↓
exposed steel on edges
↓
grease around moving components
↓
soot concentrated around smokebox/chimney
↓
water streaking
↓
heat staining
↓
rust in selected recesses
```

The AI generates source materials.

**Painter makes them belong to the locomotive.**

That's the difference between "AI texture slapped on model" and something that actually looks like a Satisfactory asset.

---

# 7. Concept art, UI and icons — ChatGPT Images

ChatGPT's current Images system supports generation, iterative editing, text and transparent backgrounds, which makes it particularly useful for UI/icon work as well as concept art. citeturn537264search2turn537264search3

I'd use it before modelling a locomotive.

For each class, we can create a reference board showing roughly:

```text
3/4 front
3/4 rear
side profile
cab
boiler/front detailing
colour/material breakdown
silhouette at Satisfactory gameplay distance
```

Then **we decide what is correct** before Blender work begins.

For UI it can create starting points for locomotive/wagon icons, milestone artwork and steam-related symbols.

Again, I wouldn't treat generated concept art as an engineering drawing. Steam locomotive geometry tends to mutate between AI views. We use it for design language rather than measurements.

---

# 8. Sound — ElevenLabs Sound Effects

This is one of the places AI could save a ridiculous amount of time.

ElevenLabs can generate sound effects from natural-language descriptions, control duration and prompt adherence, and produce looping effects intended for game/interactive use. citeturn984945search0turn984945search1

For Early Locomotion that gives us raw material for things such as:

```text
low-pressure steam exhaust
high-pressure exhaust
injector hiss
safety valve
steam whistle
cylinder drain
pump rhythm
connecting-rod clatter
wheel-on-rail rhythm
brake application
coupler impact
coal handling
cab machinery
```

I would generate those as **individual layers**, not ask for an entire locomotive soundtrack in one prompt. ElevenLabs itself recommends generating individual effects separately for complex sound sequences and combining them afterward. citeturn984945search7

That also lets Unreal blend sounds according to speed, throttle and operating state.

---

# 9. Blueprint work is the awkward bit

Blueprints remain the area where the AI workflow will be least automatic.

Epic's own asset diff system exists partly because assets and Blueprints don't have a useful normal textual representation like source files do. citeturn903864search12

So until we have an Unreal MCP compatible with the Satisfactory editor, the best workflow is:

**You show Claude/ChatGPT a Blueprint screenshot → AI analyses it → AI describes exact nodes/variables/functions → you make the graph → send another screenshot if something fails.**

For C++/Blueprint hybrid development, I'd intentionally put complicated calculations and state logic in C++ and leave Blueprint responsible for areas where Blueprint genuinely excels.

---

# The architecture I think this suggests for Early Locomotion

Even before you give me the rest of the design, your "plenty of locomotive and wagon variants" requirement strongly suggests we should **not write a separate system for every locomotive**.

I'd aim toward something roughly like:

```text
SteamRailSystem
│
├── SteamLocomotiveBase
│     ├── shared fuel logic
│     ├── steam state
│     ├── traction logic
│     ├── audio interfaces
│     └── common UI
│
├── Locomotive definitions / data
│     ├── Small Tank Engine
│     ├── Medium Freight Engine
│     ├── Heavy Freight Engine
│     ├── Fast Engine
│     └── ...
│
├── WagonBase
│     ├── Cargo variants
│     ├── Fluid variants
│     └── specialist variants
│
└── Blueprint children
      ├── meshes
      ├── materials
      ├── audio
      ├── VFX
      └── visual configuration
```

Then adding locomotive number 12 means mostly supplying **data + assets**, rather than writing locomotive number 12's own version of the steam system.

That approach will also make AI assistance substantially more reliable because the agents learn one architecture and keep extending it.

## So my recommended working arrangement

**Claude Code** becomes the main developer and repo expert.

**ChatGPT** becomes the design lead, researcher, balance modeller and visual-development assistant.

**Codex** becomes the independent code reviewer/debugger and occasional second implementation agent.

**Blender + Meshy** handle 3D, with Meshy making protot

## User

as you have chosen yourself as the designer, I will explain the mod fully to you and you can tell me what you think in terms of balance.

The tracks will be made of iron plates and iron rods. the max build length will be half that of the base game rails. They will be textured/modeled to appear as normal rails we see in real life, two thin tracks with beams holding them together.

Signalling is a little more complicated - creating a decision between early worldwide cargo or easier signalling. The semaphore signals will only be able to create blocks of a certain length before needing another signal. they will have a maximum operating speed. Signals will need to be run by a signal box building, that will be able to control a maximum number of signals down the line before another box needs to be placed. Stations will come with a signal box.

Locomotives will also be much cheaper than the base trains, aswell as the wagons. there will be three locomotive types. Small, medium and large. what would be really cool is if based on the set language in game, the locomotives and wagons would have different models. Now, i know this would be HUGE for the amount of languages and would take a lot of resources to research what locos were used in the country, but i think it would be epic. I'm willing to put in the effort. They, of course, will need coal and water. both of which can be loaded when docked in a station. the Station building will have inputs for water and coal. Compacted coal will be more efficient of course. The locomotives will have a maximum distance before needing to rewater and refuel.

That's all i have so far, any thoughts?

## Assistant

I think the concept has **a very solid balance identity already**. Steam rail shouldn't simply be “vanilla trains but unlocked earlier”; it should be a different logistics system that is powerful early because of its scale, while being worse in speed, automation, convenience and operational density. Your ideas naturally point in exactly that direction.

The current vanilla benchmark is useful here: trains arrive at Tier 6, the electric locomotive can reach roughly 120 km/h, draws 25–110 MW, and applies 2,000 kN of tractive force. Vanilla freight cars carry 32 item stacks, while stations and active freight platforms each consume 50 MW. citeturn685706search1turn685706search2turn685706search4turn685706search6turn685706search9

My main concern therefore isn't whether steam trains will be too weak. It's making sure they don't accidentally make **tractors obsolete at Tier 3** or make **electric rail pointless at Tier 6**.

## Where I think Early Locomotion should sit

I'd put the first railway milestone in **Tier 3**, probably requiring both Coal Power and Basic Steel Production.

That's almost perfect in vanilla progression. Water Extractors arrive with Coal Power at Tier 3, and tractors are also a Tier 3 transport system. citeturn904785search1turn904785search10

That creates three distinct logistics choices:

| Transport | Best at |
|---|---|
| Belts | Short/medium permanent connections |
| Tractor | Flexible routes, low infrastructure, moderate cargo |
| Steam railway | Expensive infrastructure, cheap bulk movement over long distances |
| Electric railway later | High-speed, high-capacity, high-density automated network |

That relationship is important. A steam railway should absolutely destroy tractors in **raw long-distance throughput**, because otherwise there isn't much reason to spend ages building rails. The tractor wins by requiring virtually no permanent route infrastructure.

---

# The track system

I really like **Iron Plates + Iron Rods** aesthetically and mechanically.

It immediately communicates:

> primitive railway technology rather than futuristic FICSIT monorail.

Vanilla railway uses Steel Beams and Steel Pipes, with roughly one of each per ~12 m after the initial portion. citeturn227311search0turn227311search4

So cheap iron rails create a nice distinction.

I would, however, reconsider one thing:

### I don't think the 50 m maximum segment is good *balance*

Vanilla gives you up to 100 m. citeturn685706search5

Imagine building a 4 km transcontinental steam route.

At 100 m pieces that's approximately 40 placements.

At 50 m it's approximately 80.

The second isn't really more difficult. It's just twice as much clicking.

I'd rather punish primitive railways through **operational disadvantages**—speed, signalling, gradients, train length, braking, maintenance infrastructure—than through construction annoyance.

If you really like 50 m because it visually/technically distinguishes the track, I'm not completely against it. But I'd test it heavily.

One possible compromise would be:

**Early Light Railway:** 50 m maximum.

**Improved Railway Construction unlock:** eventually raises/builds an improved version with 100 m sections.

That would make the limitation itself part of progression instead of permanent irritation.

---

# Your signalling idea is probably my favourite part

This is what stops early railway from becoming ridiculously overpowered.

And I think there should be a very deliberate distinction:

**Steam rail should be extremely easy to operate badly, but difficult to operate efficiently.**

For instance, a simple line:

```text
IRON MINE ========================== FACTORY
      station                    station

                one train
```

should require essentially no signalling expertise.

You should be able to build one train, give it two stations and go.

But then somebody tries:

```text
       Mine A
         \
Mine B ===+================ Factory
         /
       Mine C
```

with six trains...

...and suddenly the Victorian railway engineer simulator begins.

That's where signal boxes become valuable.

## Semaphore blocks

Your maximum block-distance idea works particularly well.

Vanilla signalling doesn't really care how geographically large a block becomes, although the community commonly uses roughly 300–400 m blocks and trains start reacting to red signals at around 250 m. citeturn685706search7

For steam signals, I'd tentatively start testing around:

| System | Initial balance target |
|---|---:|
| Maximum semaphore block | **400–500 m** |
| Early automatic signal speed | **~60 km/h** |
| Signals per station signal box | **6–8** |
| Signals per dedicated signal box | **12–16** |
| Signal-box territory | **~1–1.5 km of connected railway** |

Those aren't values I'd lock yet. They're starting points for playtesting.

And importantly, I wouldn't make the player physically connect every signal to the box with ten thousand cables.

I'd have the signal system automatically determine something like:

> This semaphore belongs to Signal Box A because it is within its railway territory.

Then interacting with the signal box shows:

```text
FICSIT MECHANICAL SIGNAL BOX

Controlled Signals: 9 / 12

S01 - Clear
S02 - Clear
S03 - Danger
S04 - Clear
...

Maximum controlled distance: 1,200m
```

That gives you railway-management flavour without becoming Wiring Simulator 2026.

---

# I love the maximum signalling speed

This is especially clever because it gives locomotives **two speeds**.

Suppose the large locomotive can physically reach 90 km/h.

On an unsignalled private line, manually driving it at 90 is completely possible.

But automated operation through early semaphore territory might be limited to 60–70.

That creates the feeling that the **infrastructure**, not merely the engine, is primitive.

Later you might unlock an improved signalling system:

```text
Mechanical Semaphore
60 km/h
400m maximum block

↓ upgrade

Advanced Semaphore / Interlocking
90 km/h
800m maximum block

↓ eventually

FICSIT electronic signalling
vanilla capability
```

That is fantastic progression.

And I would strongly consider withholding anything equivalent to the vanilla **Path Signal** until quite late.

Steam rail could initially have only conventional block signalling.

That means complicated junctions work, but inefficiently.

Then vanilla electronic signalling arrives and suddenly those giant junctions become far easier to manage.

That's a real reason to upgrade.

---

# Signal boxes

Stations including a signal box by default is absolutely the right call.

Otherwise somebody's first experience would be:

> Build station → build track → build another station → build train → why doesn't anything work → apparently I need three more buildings.

An integrated starter box removes that friction.

Dedicated signal boxes then become necessary when the network gets complicated.

I'd actually make them nice-looking buildings rather than tiny utility boxes: windows, levers visible inside, cable/rod conduits, maybe animated lever banks when trains reserve routes.

It could become one of the visual signatures of the mod.

---

# Small, medium and large locomotives

Three locomotive classes is an excellent foundation.

I don't think these should simply be:

> Small = bad  
> Medium = better  
> Large = best

They should solve different problems.

I'd start around this philosophy:

| | Small | Medium | Large | Vanilla Electric |
|---|---:|---:|---:|---:|
| Top speed | ~50–55 km/h | ~70–75 | ~85–90 | ~120 |
| Relative traction | Low | Medium | High | Very high |
| Fuel use | Low | Medium | High | Electricity |
| Water use | Low | Medium | High | — |
| Best train | 1–3 wagons | 3–6 | 6–10+ | Large/high-speed |
| Best use | Branch/local | General freight | Heavy trunk freight | Mature network |

The really important thing is that **small shouldn't become obsolete**.

A small tank locomotive could have:

low purchase cost, extremely low coal consumption, good acceleration and a small footprint.

A large freight locomotive could have:

enormous pulling power, terrible coal/water consumption, slower acceleration and perhaps higher servicing requirements.

So running this:

```text
LARGE ENGINE + 1 WAGON
```

should be economically stupid.

Likewise:

```text
SMALL ENGINE + 12 LOADED WAGONS
```

should crawl up hills.

That makes locomotive selection interesting rather than cosmetic.

---

# I'd unlock them progressively

Something roughly like:

**Tier 3 — Early Steam Railways**  
Small locomotive, basic wagon, station, semaphore, basic signal box.

**Later Tier 3 / early Tier 4 — Railway Expansion**  
Medium locomotive, more wagon types, improved signal box.

**Tier 4/5 — Heavy Steam Engineering**  
Large locomotive, heavy freight wagons, auxiliary tenders, improved semaphore/interlocking.

**Tier 6 — Monorail Train Technology**  
Vanilla electric railway takes over the premier high-capacity role.

That would let the railway system grow alongside the player's factory rather than dumping twenty vehicles on them in one milestone.

---

# Coal and water

Absolutely yes.

And I would **not make "range" an arbitrary kilometre timer**.

Instead, locomotives should physically contain:

```text
Coal bunker
Water tank
```

and consume both while operating.

Your maximum range then emerges naturally from tank capacity.

Even better, consumption should ideally depend somewhat on work performed.

Heavy acceleration + heavy train + uphill:

**lots of coal and water.**

Coasting downhill:

**very little.**

That would produce some wonderfully Satisfactory situations where somebody designs a ridiculously steep railway and discovers their locomotive burns through coal like there's no tomorrow.

The UI can still calculate:

> Estimated remaining operating range: ~3.2 km

so players aren't forced to guess.

---

# Water should probably be the tighter restriction

That's both thematically appropriate and better for gameplay.

I'd roughly target normal-load ranges like:

| Engine | Water target | Coal target |
|---|---:|---:|
| Small | ~2–3 km | ~4–5 km |
| Medium | ~4–5 km | ~7 km |
| Large | ~6–7 km | ~10 km |

Again: **playtest numbers, not final numbers.**

The important principle is:

**you should normally run out of water before coal.**

That makes access to water strategically important without requiring a coal depot every five minutes.

And because the Water Extractor doesn't arrive until Coal Power, it reinforces Tier 3 as the perfect unlock. citeturn904785search1

---

# Compacted Coal

Your idea works exceptionally well here.

Current Compacted Coal lasts more than twice as long as ordinary coal when burned: the wiki gives 4 seconds versus 8.4 seconds in a Coal Generator. citeturn904785search0

I'd use the **actual fuel-energy system** rather than coding:

```text
if CompactCoal:
    efficiency *= 2
```

That means its naturally higher energy density translates into locomotive range.

So a route that is *just slightly too long* for standard coal might suddenly become practical once the player invests in sulfur research.

That's exactly the sort of cross-system interaction Satisfactory does well.

---

# Your station coal/water inputs

I like this, although I'd make servicing visible.

Imagine the station having:

**1 × conveyor fuel input**

**1 × pipe water input**

Then while the locomotive stops:

```text
CHUFF CHUFF CHUFF
      ↓
water crane swings over
      ↓
coal loader activates
      ↓
locomotive replenished
```

I'd even make servicing add a little dwell time.

Maybe a properly supplied station spends another 5–15 seconds topping up the locomotive depending upon how depleted it is.

Now you get another beautiful tradeoff:

> Frequent servicing = reliable but slower network.

> Fewer servicing points = faster schedules but range risk.

That's railway-game gold.

---

# I would add auxiliary tenders

This fits your wagon-variant idea beautifully.

Suppose a remote route is just beyond the Large locomotive's comfortable water range.

The player could attach:

**Auxiliary Water Tender**

or perhaps a combined:

**Long-Distance Tender**

It carries no cargo but considerably increases train range.

Now the decision becomes:

```text
Locomotive
+ 6 freight wagons
```

versus

```text
Locomotive
+ auxiliary tender
+ 5 freight wagons
```

You sacrificed approximately 17% of your cargo train length to obtain much greater range.

That's meaningful balance.

And steam enthusiasts get another cool wagon.

---

# Wagons should probably be smaller than vanilla ones

Vanilla item freight cars currently carry **32 stacks**. citeturn685706search4

I would not give early wagons the same capacity.

Something around **16–24 stacks** feels more appropriate initially.

That alone preserves a huge advantage for the Tier 6 system.

Steam:

```text
6 cars × 20 stacks
= 120 stacks
```

Electric:

```text
6 cars × 32 stacks
= 192 stacks
```

before even considering the electric locomotive's greater speed.

Suddenly electric rail is a very substantial upgrade without us having to make steam terrible.

---

# The regional locomotive idea

This is an **absolutely brilliant aesthetic idea**, with one change I'd strongly recommend:

### Don't actually bind nationality permanently to language.

Language ≠ country.

English could mean:

UK  
USA  
Canada  
Australia  
New Zealand  
India  
etc.

Spanish has an even bigger problem.

Portuguese could mean Portugal or Brazil.

French could mean France, Canada, Belgium, Switzerland, etc.

And somebody in Germany might simply prefer playing Satisfactory in English.

Instead I'd implement:

> **Regional Rolling Stock Style**

with:

```text
Automatic
British
North American
German/Central European
French
Japanese
...
```

**Automatic** can use game language as its best guess.

But players can override it.

That gives you your original magical effect—install the mod in German and German locomotives appear by default—without forcing players into the wrong country's railway style.

---

# Crucially: regional models should have identical statistics

For example:

```text
SMALL LOCOMOTIVE

British model
German model
American model
French model
Japanese model
```

All five share:

same collision box, same wheel/socket layout where feasible, same coal capacity, same water capacity, same traction and same speed.

Only the visual model, sounds and perhaps minor animation details differ.

Otherwise changing the game language could literally alter the optimal strategy.

We absolutely don't want:

> German is meta because its Large locomotive has 8% more traction.

Funny, but horrifying to balance.

---

# There is a clever way to make the modelling workload manageable

Instead of treating every regional train as an entirely unique vehicle, create a standardized invisible **mechanical chassis**.

Something like:

```text
SMALL LOCOMOTIVE CHASSIS
├── wheel positions
├── couplers
├── collision
├── animation sockets
├── cab interaction position
├── steam emitters
└── gameplay component

        ↓

Regional visual shell
├── UK
├── Germany
├── France
└── etc.
```

Likewise with wagons.

That means adding the 11th regional pack doesn't require rewriting the vehicle.

It requires making new meshes that conform to established dimensions.

That turns an insane project into merely a **very large project**. 😄

---

# One potentially serious design problem: Tier 6

This is the part I think we need to solve before development begins.

Your railway is:

> conventional two-rail track.

Vanilla Satisfactory railway is:

> futuristic monorail.

So imagine the player spends twenty hours constructing this:

```text
ENTIRE WORLD
===============================
=======================
==============================
```

Then reaches Tier 6.

If the game effectively tells them:

> Congratulations! Electric trains unlocked.  
> Demolish your entire railway network.

...they're probably never going to use vanilla trains.

Not because steam is stronger.

Because replacement is miserable.

I think there needs to be some kind of **upgrade path**.

My favourite version would be an in-place railway upgrade system.

Conceptually:

```text
Early Railway
iron construction
steam only

       ↓ Tier 6 upgrade

Electrified / Modern Railway
steel construction
electric capability
better signalling
higher permitted speeds
```

Whether it visually becomes vanilla monorail or an electrified conventional line is something we'd have to decide with technical feasibility in mind.

But the player's **route geometry should survive**.

That means steam rail becomes the foundation upon which their later railway empire grows instead of a dead-end technology.

And that is probably the single biggest balance/design decision I would want us to nail.

---

## Overall

At this stage, I would keep almost everything you've proposed.

The strongest pieces are the **signal boxes, limited semaphore signalling, water/coal logistics and multiple locomotive sizes**. Those aren't arbitrary debuffs; they produce interesting railway-management decisions.

The three things I'd modify are:

1. **Question the 50 m track limit** unless we can make construction convenient.
2. **Use regional style selection with language-based automatic defaults**, rather than hard-binding models to languages.
3. **Give steam railway an upgrade/migration route into Tier 6**, otherwise players will be punished for investing in exactly the system your mod encourages them to build.

And I think there is another idea hiding in what you've designed: **Small/Medium/Large shouldn't necessarily be the only locomotives. They should be the three gameplay classes.** Within those classes we could eventually have several locomotive variants—tank engines, tender locomotives, freight-focused engines, fast mixed-traffic engines, articulated heavy haulers—without creating balance chaos.

That would give you the enormous locomotive roster you want while still reducing everything to three comprehensible balance families.

## User

I will now reply to some of your points, anything i dont reply to assume i agree with:

"I don't think the 50 m maximum segment is good *balance* " - Perhaps we could do something backwards. The cheaper rail actually has a longer max distance. This makes it easier to build the infastructure, but its still limited by speed limits, signaling and locomotive limitations. the drawback to early locos isnt the track, its the trains themselves.

"I'd even make servicing add a little dwell time." - precicely, but i would like to be more specific with this. The locomotive will pull in slowly, let out a long hiss as it 'docks' before spending a short while as the coal is chuted in and the water tower swings around. I would like the station building to be much larger than the normal one, with a water tower and coal conveyer, both of which will move and adjust with an incricate animation as they find the water hatch and coal storage.

"I would add auxiliary tenders" - Yes, but not quite as you implied. The larger locomotives will come with a tender anyway. I will use British locomotives as an example. Small - **LMS Fowler Dock**  , this is a tank engine, so no tender at all. you could have an aux tender but it would be a risky trade as its the weakest engine. Medium - [Merchant Navy](https://en.wikipedia.org/wiki/SR_Merchant_Navy_Class) Class, a tender engine with a much increased coal and water capacity, but also higher consumption. suddenly the auxiliary tender becomes a viable option. Finally, Large - [Class 9F](https://en.wikipedia.org/wiki/BR_Standard_Class_9F "BR Standard Class 9F"), the biggest and most powerful. an auxiliary tender might be a good idea for especially long journeys.

Speaking of long journeys, i think having coal/water towers as separate buildings that you can put on the railway. this means especially long journeys become possible, at the cost of time, as the locomotive needs to take a break to refuel/water.

"Instead of treating every regional train as an entirely unique vehicle, create a standardized invisible **mechanical chassis**." - possibly? but you must remember that different classes from across the world look very different. for example, the UK's biggest freighter was the 9F, a 2-10-0 locomotive. Meanwhile the US's biggest, the 4000 class, better known as "Big Boy", is a 4-8-8-2 locomotive. Those two would be impossible to put under the same universal model.

"conventional two-rail track vs futuristic monorail" - A simple idea. it will work the same as conveyors, miners, and every other building with "Mk1, Mk2, Mk3..", the player would select the better rail and point it over existing track and be able to replace it.

## Assistant

Yes — these changes make the design considerably stronger. I also think your locomotive examples expose something I was getting wrong: **we should standardise the locomotive system, not the physical locomotive chassis**.

Small correction first: the Union Pacific Big Boy is **4-8-8-4**, rather than 4-8-8-2. Union Pacific itself describes that arrangement: four pilot wheels, two sets of eight driving wheels, and four trailing wheels. citeturn252511search0turn252511search16 Your broader point is completely right, though. A British 9F is a 2-10-0, while a Big Boy is an articulated 4-8-8-4; trying to force those onto one physical template would undermine the entire regional idea. The 9F's five coupled driving axles were specifically chosen for high adhesion and relatively low axle load. citeturn252511search13

## Cheap track being *easier* to build

I much prefer this inversion.

The early railway's sales pitch becomes:

> **“Put a railway across the map surprisingly early and surprisingly cheaply.”**

And then, after the player has done that:

> **“Now operate it.”**

That's much more interesting.

I'd actually be comfortable experimenting with the primitive railway having a **longer placement length than the later railway**, assuming the Satisfactory rail spline implementation permits it technically. Something like 150 m wouldn't bother me from a balance perspective.

The cheap track itself doesn't need to suck. It can be excellent infrastructure with a low permitted speed.

That gives us three independent concepts:

**Track speed** — how fast the physical railway safely permits travel.

**Signal speed** — how fast automated trains are allowed through that signalling territory.

**Locomotive speed** — what the engine is mechanically capable of.

Actual permitted speed becomes effectively:

`min(track limit, signalling limit, locomotive limit)`

That's an excellent system because every later railway technology can improve a different bottleneck.

---

## Your station idea is much better than my generic “dwell time”

I now picture this as a major part of the mod's identity rather than merely a timer.

The train enters the platform under a fairly restrictive approach speed. As the locomotive reaches its stopping position, you hear braking, mechanical noises and then that long steam release as it settles into the servicing position.

Then the station comes alive.

The **water crane rotates toward the locomotive**, extends or adjusts itself, finds the locomotive's filler point and lowers into position. Simultaneously, the **coal loading apparatus moves over the bunker/tender**, adjusts for the particular locomotive and starts loading it. Once servicing finishes, both pieces of machinery retract before departure.

That could look *fantastic*.

More importantly, the large building footprint becomes part of the balance.

A primitive railway station might be cheap in advanced materials, but it's physically enormous because you're effectively building:

> station + water tower + coal storage + locomotive servicing facility + signal box

whereas the futuristic FICSIT station is compact and technologically sophisticated.

So we're trading **technology for land and infrastructure**.

That feels very Satisfactory.

### And regional locomotives give us an animation solution

Rather than requiring the station animation to magically understand the mesh, every locomotive model can expose standard servicing targets:

```text
WaterFillSocket
CoalFillSocket
SteamExhaustSocket
FrontCouplerSocket
RearCouplerSocket
CabInteractionSocket
```

The British Dock Tank might have its water socket on the tank and its coal socket behind the cab.

The Merchant Navy has them on its tender.

The Big Boy has completely different geometry.

Doesn't matter.

The station machinery animates toward **that model's sockets**.

So regional variation becomes compatible with one servicing system without making the locomotives physically identical.

---

# The three British locomotives actually suggest excellent balance

Your choices are more interesting than my original generic Small → Medium → Large progression.

### Small — LMS Fowler Dock Tank

This thing is almost perfect for the starter locomotive.

Historically, it was a compact **0-6-0T** dock/shunting locomotive with only about 1.5 long tons of coal and 1,000 imperial gallons of water, specifically designed around tight curves and constrained working areas. citeturn252511search14

That gives us an obvious gameplay personality:

**Cheap. Compact. Nimble. Short range. Low maximum speed. Weak on long/heavy trains.**

But I don't want “weak” to mean useless.

I'd make the small locomotive quite punchy at very low speed. It should happily start two or three loaded wagons and work tight industrial branches.

Its weakness should appear when somebody says:

> “I'm going to attach eight wagons and cross the entire map.”

Then its acceleration, hills, water supply and coal capacity become painful.

That keeps small engines permanently useful as **industrial locomotives**.

---

# Medium — Merchant Navy

This is where it gets interesting.

The Merchant Navy wasn't really a medium freight engine historically. It was a large, powerful **4-6-2 Pacific**, primarily intended for heavy express/boat-train work, although it was officially classified for mixed traffic and could haul freight. citeturn252511image2

But I actually think that makes it an *excellent* gameplay medium.

Don't make Medium simply:

> Small but stronger.

Make it the **fast locomotive**.

So perhaps:

**Fowler Dock Tank**
- low speed
- excellent economy
- short trains
- tiny internal supply
- branch/shunting work

**Merchant Navy**
- **highest steam speed**
- good but not enormous traction
- substantial tender
- moderate/large train
- relatively thirsty
- excellent long-distance mixed freight

**9F**
- somewhat lower top speed than Merchant Navy
- enormous starting/continuous traction
- heavy fuel/water consumption
- huge freight consists
- slower acceleration
- trunk freight monster

The 9F was specifically designed as a heavy freight 2-10-0, with the five coupled axles giving increased traction. citeturn252511search13

So now Medium and Large don't invalidate one another.

For a relatively light 4 km route:

> Merchant Navy wins because it completes the journey sooner.

For hauling ten loaded wagons up horrible gradients:

> 9F wins because it can actually drag them there efficiently.

That is **far better** than simply making Large superior in every statistic.

---

# Tenders

I understand what you mean now, and yes.

We need to distinguish:

**Integral/standard tender**  
Part of the locomotive model and included in its normal stats.

from

**Auxiliary tender**  
An additional vehicle intentionally consuming train length in exchange for range.

So:

```text
Fowler Dock Tank
[LOCO]
```

No normal tender.

```text
Merchant Navy
[LOCO][TENDER]
```

Its normal locomotive entity visually includes its historically appropriate tender.

Then:

```text
[MERCHANT NAVY][NORMAL TENDER][AUXILIARY TENDER][CARGO][CARGO]...
```

is the long-range configuration.

I'd probably still treat the normal locomotive+tender as **one game vehicle/entity** if technically practical. Otherwise scheduling, station alignment, train length calculation and player interaction may get needlessly awkward.

The auxiliary tender, however, should absolutely be a genuine wagon.

### And the Dock Tank auxiliary tender should be hilariously questionable

You described this really well.

Technically:

> Yes, you can put an auxiliary water/coal vehicle behind the Dock Tank.

But now you've added dead weight to your weakest locomotive.

So you're solving one limitation while aggravating another.

That's exactly the sort of player decision we want.

---

# Trackside water and coal servicing

**Absolutely. Keep this.**

I'd actually make three service levels.

| Facility | Coal | Water | Full station? | Signal box? |
|---|---|---|---|---|
| Water Tower | — | ✓ | No | No |
| Coaling Stage | ✓ | — | No | No |
| Steam Service Point | ✓ | ✓ | No | Possibly optional |
| Station | ✓ | ✓ | Yes | Yes |

I'm not completely committed to all four being separate buildables—we don't want menu bloat—but I strongly like the ability to service a locomotive **without making it stop at a cargo station**.

It turns geography into railway planning.

Suppose:

```text
Coal Mine =============================== Factory
```

is too long for your locomotive.

You can either:

**A.** Add auxiliary tender → less cargo capacity / more dead weight.

**B.** Build:

```text
Coal Mine =========== WATER ============ Factory
```

**C.** Build full servicing infrastructure:

```text
Coal Mine ====== SERVICE POINT ========= Factory
```

**D.** Eventually buy/use a locomotive with greater range.

Four valid solutions to one problem.

That's superb.

---

# I'd make service stops schedulable

This could become one of the really distinctive features.

The timetable might eventually contain entries like:

```text
Ironworks Station
    Unload

→ Water Tower 3
    Service: Water
    Depart when full

→ Northern Mine
    Load: Coal
```

Or perhaps automatic servicing could happen when the train passes/stops at a configured facility.

I'd actually prefer the player to **explicitly add service stops to the timetable**, at least initially.

It makes railway planning understandable:

> “Why did Engine 12 run dry?”

Look at the schedule.

> “Ah. I forgot to send it through the water stop.”

That's much better than invisible background logic making the train mysteriously choose where to refuel.

---

# Refuelling time should depend on quantity

I want to modify something else I previously suggested.

Don't make it a fixed:

> +10 seconds for servicing.

Make the machinery have **transfer rates**.

For example—not final numbers:

```text
Water crane:
X m³ water / second

Coal chute:
Y items / second
```

Then arriving nearly full creates a brief top-up.

Arriving nearly empty means:

**you're sitting there for a while.**

That's much richer.

It also creates potential upgrade buildings later:

```text
Basic Water Crane
↓
High-Flow Water Column
```

and

```text
Manual Coaling Stage
↓
Mechanical Coaling Plant
```

A railway designed around frequent tiny top-ups can therefore achieve higher throughput than one that runs locomotives dry between giant servicing stops.

That's a genuine optimisation problem.

---

# Throw out my “universal chassis” idea

You're right.

I was thinking too much like a developer trying to reduce asset work and not enough like the designer of *this particular mod*.

These things should genuinely look and move differently.

image_group{"layout":"carousel","aspect_ratio":"16:9","image_refs":["turn252511image0","turn252511image2","turn252511image1"]}

Even within your examples:

**Fowler Dock Tank:** compact 0-6-0 tank engine. citeturn252511search14

**Merchant Navy:** 4-6-2 Pacific.

**9F:** long-wheelbase 2-10-0. citeturn252511search13

**Big Boy:** articulated 4-8-8-4 and about 133 ft long. citeturn252511search0

There's simply no sensible shared physical chassis.

## What we standardise instead

We standardise the **software contract**:

```text
SteamLocomotiveBase
│
├── performance data
│   ├── max speed
│   ├── tractive effort
│   ├── mass
│   ├── coal capacity
│   ├── water capacity
│   └── consumption curves
│
├── service interfaces
│   ├── water socket
│   ├── coal socket
│   └── service state
│
├── railway interfaces
│   ├── front coupling
│   ├── rear coupling
│   └── signal behaviour
│
└── presentation
    ├── wheel configuration
    ├── animation rig
    ├── steam emitters
    ├── audio
    └── regional mesh
```

Then each regional locomotive gets its **own wheel arrangement, wheelbase, rig and animation**.

That's much better.

---

# We can still have balance equivalence without physical equivalence

This becomes important with regional packs.

Suppose Britain gets:

> Large = 9F

while America gets:

> Large = Big Boy.

A literal simulation would make the Big Boy enormously superior.

We don't want that.

But making their numbers completely identical might also feel bizarre when one is visibly gigantic.

My preferred compromise would be **same overall balance budget, different distribution**.

For example:

### British Large — 9F
- cheaper
- somewhat lighter
- lower fuel consumption
- shorter
- good traction
- easier station fit

### American Large — Big Boy
- extremely expensive
- enormous traction
- enormous coal/water consumption
- very long
- possibly worse acceleration per total consist mass
- needs substantially more servicing
- potentially restricted from very tight railway geometry if we ever simulate that

Over a whole route, neither should be objectively superior.

The Big Boy can pull something absurd, but keeping it fed is absurd too.

That actually makes the regional variations **gameplay-interesting**, rather than skins, while maintaining approximately equal effectiveness.

The danger is that this becomes an impossible balancing exercise across twenty languages. So I'd only do regional mechanical differences if we're confident we can test them properly. Otherwise identical gameplay classes with wildly different visual models remains completely defensible.

---

# Mk1 → Mk2 track replacement

Yes.

This is better than every migration system I was contemplating.

It's completely understandable to a Satisfactory player:

```text
Primitive Railway Mk.1
          ↓
hover upgraded rail over it
          ↓
Modern Railway Mk.2
```

**Same spline. Same route. Same supports. Same junction geometry.**

Just like upgrading a belt.

I would extend that philosophy throughout the mod.

Potentially:

```text
Semaphore Signal Mk.1
→ Automatic Signal Mk.2

Mechanical Signal Box
→ Electronic Interlocking

Early Station
→ Modern Station
```

Not everything necessarily has to upgrade in place, but wherever we *can* preserve the player's work, we should.

That gives the mod a really important philosophy:

> **Early Locomotion isn't temporary infrastructure. It's early infrastructure that grows with your factory.**

That's much stronger.

---

# And I think Mk2 rail should still support steam

This matters a lot.

When the player reaches electric trains, upgrading their line shouldn't mean:

> Steam locomotives forbidden.

I'd make modern rail backwards compatible.

So eventually you could see:

```text
9F hauling local freight
        ↓
electric express overtakes elsewhere
        ↓
Dock Tank shunting at factory
```

on the same modern network.

The electric locomotive becomes technologically superior for new mainline service, but steam doesn't disappear from the player's world.

That has two advantages.

Gameplay-wise, players can transition gradually instead of replacing a dozen locomotives simultaneously.

Aesthetically, someone who loves steam can continue using it forever if they're willing to accept the disadvantages.

**That is exactly how I'd want this mod to behave.**

---

## Where I think the design now stands

We've stumbled into a much clearer philosophy than we had at the beginning:

> **Early track is cheap and unusually easy to deploy. Steam trains are cheap to purchase but expensive in attention, land, time and logistics.**

And every inconvenience is something the player can engineer around.

Short range?

→ tender or service stop.

Low throughput?

→ bigger locomotive, longer train or more trains.

More trains?

→ now you need signalling.

More signals?

→ now you need signal boxes.

Signal congestion?

→ improve signalling technology.

Steam servicing slowing the main line?

→ build dedicated service sidings.

Rail speed becoming restrictive?

→ upgrade the physical railway.

Network getting too busy for steam?

→ introduce electric traction.

That's exactly the kind of **problems creating new engineering problems** loop that suits Satisfactory.

The next thing I'd want to tackle isn't implementation yet. It's the **actual steam railway technology tree**—what you get in the first unlock, when Medium and Large engines appear, when auxiliary tenders/service points appear, the semaphore progression, and precisely what Tier 6 electric rail improves. Once that's settled, we can start putting provisional numbers against the locomotives.

## User

"And I think Mk2 rail should still support steam" - Yes, ideally, but remember that the two track types are two entirely different constructs. One has two rails flat on the ground, the other is a monorail that the train practically hugs with it's wheels.

regarding Big boy, that was an extreme example, i think we will use a smaller but still impressive class of steam freighter.

[User attached 1 image; image contents were not included]

## Assistant

Exactly. The image makes the incompatibility pretty stark: the vanilla locomotive isn't merely a conventional train sitting on a strange rail. Its running gear wraps around the monorail beam, whereas our steam locomotives need two conventional steel rails under flanged wheels. Trying to make a 9F somehow run on that would look ridiculous.

So I'd revise what I said earlier: **steam locomotives should not run on upgraded FICSIT monorail track at all.** The upgrade system should preserve the *route*, not compatibility between the vehicles.

I think the progression should work like this:

```text
EARLY CONVENTIONAL RAILWAY
══════════════════════════
Two conventional rails
Steam traction
Semaphore signalling
Coal + water servicing
Low/medium permitted speeds

             │
             │ Tier 6 conversion
             ▼

FICSIT MONORAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━
Vanilla beam-style railway
Electric locomotive
Electronic signalling
No fuel/water servicing
Much higher operating capability
```

When the player selects the vanilla/FICSIT railway and points it at an existing conventional rail segment, they get the familiar **upgrade hologram**. Confirming it replaces the conventional spline with a monorail spline along exactly the same path.

That means you retain the thing that was expensive in player time—**route planning**—without pretending the two technologies are physically compatible.

There could be a really satisfying conversion animation too. You point the hologram over the old railway, get something like:

> **UPGRADE: EARLY RAILWAY → FICSIT RAILWAY**  
> Existing route geometry will be retained.  
> Steam rolling stock cannot use the upgraded section.

That warning matters, because otherwise somebody upgrades three kilometres of mainline and strands five steam trains.

I also wouldn't force complete conversion. That's actually more interesting.

A mature save could have a big electric trunk route while old conventional branches remain:

```text
Iron Mine ───── steam branch ────┐
                                  │ Transfer Yard
Coal Mine ───── steam branch ─────┤
                                  ╞═════════════════ FICSIT MAINLINE
Limestone ───── steam branch ─────┘
```

Now the little tank engines can remain genuinely useful late-game. They shuttle material from small outposts to a major interchange, while electric trains handle long-haul transport.

That gives the steam system a graceful endgame role without artificially making nineteenth/twentieth-century machinery competitive with FICSIT technology.

And it gives us a potential **Transfer Station / Interchange** building later in the mod: conventional rail on one side, monorail on the other, with freight automatically transferred between platforms. That could be quite a cool late-game piece of infrastructure.

### Stations need the same conversion philosophy

The early station you're describing is going to be enormous compared with the vanilla one because it includes the signal box, coal equipment, water tower, servicing machinery, etc.

So I don't think I'd literally morph:

```text
Giant Victorian servicing complex
```

into:

```text
compact FICSIT station
```

and pretend they're equivalent.

Instead, perhaps the early station has an **upgrade/replace mode** which places the vanilla station at the same track alignment and preserves its station name/timetable references where technically possible.

The old water tower, coal stage and associated equipment disappear because they're no longer required.

That creates a visually satisfying technological transition too. The player's network slowly loses all the sprawling steam-era infrastructure as they modernise.

---

## Big Boy

Agreed. Big Boy is useful for demonstrating why one universal chassis wouldn't work, but it's probably excessive as the normal American “Large” locomotive.

It creates a problem beyond physical dimensions too: if Britain gets a 9F and America gets a Big Boy, the American locomotive visually screams:

> “I should be capable of pulling half the planet.”

Trying to balance those as equivalent classes becomes awkward.

I'd choose regional locomotives that are **roughly comparable in role and prestige**, rather than necessarily comparable in exact engineering.

For an American Large freight engine, I'd look much more seriously at something like a **2-10-2 Santa Fe type**, a large **2-8-2 Mikado**, or perhaps one of the heavier 4-8-2/2-8-4 types depending on what visual identity we want.

A 2-10-2 in particular could pair nicely against the 9F:

```text
BRITAIN
BR Standard Class 9F
2-10-0
Long, purposeful heavy-freight machine

USA
Large Santa Fe-type
2-10-2
Big American boiler, large tender,
substantial freight locomotive without becoming absurd
```

They still look completely different, which is what we want, but they're psychologically in the same category.

Then an articulated American locomotive such as a Challenger/Y-class/Big Boy-type machine could potentially appear much later as something special rather than simply being the ordinary Large option.

That suggests another possibility for the distant future: the three classes don't have to contain **every locomotive we ever add**.

We could eventually have:

**Small / Medium / Large** as the core progression, and then a few **specialist locomotives** earned through later milestones or MAM research.

For example, an articulated heavy-haul locomotive could be a late steam technology that gives absurd traction but equally absurd fuel consumption and servicing requirements. It wouldn't need a direct British equivalent because it wouldn't be part of the regional three-engine baseline.

But that's something I'd leave for well after the core system works.

The immediate design now feels clearer: **conventional steam railway is its own genuinely different transport technology; Tier 6 lets the player convert its routes into FICSIT monorail rather than magically making the two systems interoperable.** That distinction actually makes the mod more believable *and* gives the transition to vanilla rail much more character.

## User

[@Documents](plugin://documents@openai-primary-runtime) Can you  make a project file where we will store all our creations of this mod. also include a word doccument outlining what we have discussed so far with all neccecary details, thjis way oyu can refer back and dont need to rely on your memory

## Assistant

Done — I created a new Work chat specifically for the **Satisfactory: Early Locomotion** project so the project files and Word document can be built and maintained there.

The brief I passed over includes the full structure we discussed: core concept, balance philosophy, early conventional track, semaphore signalling and signal boxes, locomotive classes, regional variants, coal/water servicing, animated stations, auxiliary tenders, trackside service points, and eventual conversion to vanilla FICSIT monorail.

That gives us a persistent project record so we can keep updating the design rather than relying on memory alone.
