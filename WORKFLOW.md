# Early Locomotion Project Workflow

This file is the quick guide to how work is coordinated and recorded. Project files are persistent project memory; chat history and specialist output are not authoritative by themselves.

## Chat Roles

### The Manager

The main coordination and control chat. It tracks project state; handles setup guidance, decisions, approvals, debugging triage, delegation, ordinary research, and specialist review; and determines which documentation needs updating. It does not create new Work chats automatically.

### Ideas Lab

A normal chat for brainstorming and speculative game design. It may challenge, develop, and refine ideas, but it does not make them canonical. Ideas ready for adoption return to The Manager for approval and reconciliation.

### Project Operations

The persistent Work-mode chat for creating or editing project files and artifacts. It handles multi-file documentation updates, conversion, reconciliation, and substantial research deliverables. It must not independently make game-design decisions.

## External Specialists

- **Claude Code:** Primary implementation engineer for Unreal/SML C++, repository implementation, API and header investigation, build/debug work, and Blueprint handoffs.
- **Codex:** Independent code review, debugging, QA, refactoring review, architecture second opinions, and alternative implementation analysis.

Specialist output does not automatically become project truth. Results return to The Manager for review against the canonical files.

## Project Authority

Read and apply project sources in this order:

1. `INDEX.md` — current project overview, navigation, and status.
2. `Design/GAME_DESIGN.md` — canonical gameplay and design authority.
3. `Development/PROGRESS_LOG.md` — current development checkpoint, blockers, work history, and exact next action.
4. `Development/TECHNICAL_ENVIRONMENT.md` — verified toolchain, API, and environment facts.
5. `CHANGELOG.md` — meaningful project, design, and implementation history.
6. `CLAUDE.md` — Claude-specific implementation rules.
7. `References/` — historical and supporting material; not automatically authoritative.

If sources disagree, flag the conflict and identify what needs correction. Do not silently reconcile it.

## Delegation Loop

1. An idea or problem goes to The Manager.
2. The Manager assesses it and selects the appropriate specialist or tool.
3. The specialist receives a scoped task and returns results.
4. The Manager reviews those results against the canonical files.
5. The user approves decisions where required.
6. Project Operations updates documentation when appropriate.

## Change Discipline

For an approved design change:

1. Update the detailed authoritative file first.
2. Update `INDEX.md` when the overview or status changes.
3. Update `CHANGELOG.md`.
4. Update `Development/PROGRESS_LOG.md` only when actual work or progress occurred.

For development or setup progress:

1. Update `Development/PROGRESS_LOG.md`.
2. Update `Development/TECHNICAL_ENVIRONMENT.md` when verified technical facts change.
3. Update `INDEX.md` when the project phase or status materially changes.

Never silently resolve an **Open Question** or change an item's status between **Agreed**, **Proposed**, **Playtest Target**, **Superseded**, and **Open Question**.

## Work Principles

- Treat project files, not chat history, as persistent project memory.
- Prefer existing chats and files over new management systems.
- Flag conflicts instead of silently reconciling them.
- Do not create unnecessary task-management or documentation systems.
- Keep tasks scoped, decisions explicit, and implementation, design, and documentation synchronized.
