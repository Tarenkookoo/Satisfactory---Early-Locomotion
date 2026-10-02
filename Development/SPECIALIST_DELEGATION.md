# Early Locomotion — Specialist Delegation

**Approved guidance / last verified:** 2026-10-02

This is the detailed authoritative guide for specialist selection, model/effort selection, escalation, task construction, handoffs and verification. WORKFLOW.md retains the concise coordination/change workflow; CLAUDE.md retains Claude-specific implementation rules.

## Project authority and boundaries

1. `INDEX.md` — current project overview, navigation, and status.
2. `Design/GAME_DESIGN.md` — canonical gameplay and design authority.
3. `Development/PROGRESS_LOG.md` — current development checkpoint, blockers, work history, and exact next action.
4. `Development/TECHNICAL_ENVIRONMENT.md` — verified toolchain, API, and environment facts.
5. `CHANGELOG.md` — meaningful project, design, and implementation history.
6. `WORKFLOW.md` — coordination and change discipline.
7. `Development/SPECIALIST_DELEGATION.md` — detailed specialist selection, model/effort, task, handoff, and verification rules.
8. `CLAUDE.md` — Claude-specific implementation rules.

References/ is supporting/historical and is not automatically authoritative. ROADMAP.docx and the Word design/reference artefacts remain derived viewing/planning copies outside the authority chain. Report conflicting sources to The Manager rather than silently choosing a resolution. Preserve **Agreed / Proposed / Playtest Target / Superseded / Open Question** exactly; specialist work must not resolve an Open Question or change design status independently.

The canonical project/documentation root is `C:\Users\a156b\Documents\Satisfactory - Early Locomotion`; the separate active implementation workspace is `C:\SML`. Assign the correct root explicitly. Temporary relocation backups are recovery material, not canonical project trees.

## Universal model / effort recommendation

Before every Claude Code or Project Operations handoff, The Manager recommends the most cost-effective model and effort level likely to complete the task reliably. Do not default to the most expensive model or highest effort.

Escalate only when complexity, ambiguity, architecture risk, debugging difficulty, verification burden, long-horizon reasoning or previous failure justifies it. Prefer increasing effort before switching to a more expensive model when the current model is otherwise appropriate.

Present this recommendation to the **user before the delegated task**:

```text
Recommended <Specialist> configuration:
- Model: <model>
- Effort: <effort>
- Reason: <one concise sentence>
```

This recommendation is Manager guidance and normally must **not** be inserted into the specialist task prompt itself. Keep the task focused on the objective, scope, evidence, constraints and deliverables.

## Specialist selection

| Specialist | Appropriate work | Boundary |
| --- | --- | --- |
| Project Operations | Project/document/file reconciliation, filesystem operations, artefacts/conversion and substantial document work | No independent gameplay/design decisions |
| Claude Code | Primary implementation engineering, Unreal/SML C++, repository implementation, API/header investigation, build/debug work and Blueprint/technical implementation | Implements approved behaviour; unresolved design choices return to The Manager |
| Codex | Independent review, debugging/QA, refactoring review and architecture second opinions | Review/evidence does not independently approve architecture or design |
| Ideas Lab | Brainstorming and speculation | Cannot make ideas canonical |

Specialist output is never automatically project truth. The Manager reviews it against authoritative files before approving any reconciliation.

## Claude model / effort guidance

This guidance is time-sensitive. Reverify against current official Anthropic documentation when model availability materially changes. The following model/effort policy is Manager-approved as of **2026-10-02**; model names and effort support were checked against official documentation. These are project selection rules, not promises of task success or a pricing table.

Default Claude Code model: **Claude Sonnet 5.5**.

| Sonnet 5.5 effort | Project guidance |
| --- | --- |
| Low | Very small/simple/latency-sensitive work; verification may be lighter, but required checks still apply |
| Medium | Preferred starting point for well-specified agentic coding and multistep tool work |
| High | Harder/longer implementation, debugging, ambiguity or substantial verification |
| Xhigh / Max | Exceptional; use only where extra reasoning provides a justified quality benefit |

Escalate to **Claude Opus 5.5** for genuinely open-ended problems, sustained architectural judgment, ambiguous root causes after competent Sonnet investigation, high-risk refactors, difficult cross-system reasoning, or Sonnet failure/insufficient confidence.

| Opus 5.5 effort | Project guidance |
| --- | --- |
| Medium | Normal starting point |
| High | Difficult architecture, root-cause or long-horizon work |
| Xhigh / Max | Exceptional |

Do not choose Opus merely because a task is important or multi-file. Prefer Sonnet 5.5 at suitable effort for well-scoped work. Do not hard-code pricing.

Official source notes (checked 2026-10-02):

- [Anthropic Sonnet 5.5 prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5): medium for specified agentic coding/multistep tools, high for harder/longer work, and exceptional xhigh/max with demonstrated benefit.
- [Anthropic Opus 5.5 prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5): effort and long-horizon reasoning guidance.
- [Anthropic effort reference](https://platform.claude.com/docs/en/build-with-claude/effort): supported levels and model-specific defaults. Project starting points are not a claim that API and application defaults are identical.

## Project Operations model / effort guidance

Default: **GPT-5.6 Sol**.

| Effort | Project guidance |
| --- | --- |
| Low | Simple inspection/discovery and tiny mechanical edits |
| Medium | Routine documentation, controlled filesystem work, ordinary artefacts and straightforward multi-file reconciliation |
| High | Ambiguous project state, verification-heavy reconciliation, difficult artefact work or operations where mistakes are costly |
| Higher / maximal, if available | Exceptional; require a concrete justification |

Prefer increasing effort before switching to a more expensive model when the current model is otherwise appropriate. Confirm available configurations in the actual environment; no external pricing is fixed here.

## Constructing the specialist task

Give one scoped objective, the exact project/workspace paths, the relevant authoritative inputs and evidence, allowed/prohibited changes, required deliverables, verification and completion criteria. Identify known unknowns and status boundaries. State whether edits, external actions, cleanup, staging or committing are authorised; do not assume those actions from a request to inspect.

For implementation, describe approved behaviour and constraints without inventing APIs or silently resolving architecture. For filesystem work, specify exact targets, preservation/backup requirements and stop conditions. For documents, identify the canonical source and any derived copies requiring synchronization.

Request the required Manager handoff. Keep model/effort recommendations in the user-facing Manager preamble rather than duplicating them in the task body.

## Verification expectations

- Inspect current files and repository state before editing; preserve legitimate unrelated work.
- Verify facts using real local evidence or current authoritative external sources when appropriate. Distinguish direct verification, Manager/user-confirmed results and unverified assumptions.
- Report generation, build, editor loading, packaging/deployment and in-game behaviour as separate milestones. A successful earlier stage does not verify a later one.
- Apply checks proportionate to scope: content/status consistency, history preservation, API inspection, relevant builds/tests or file/hash checks. Render and visually inspect every modified DOCX.
- Review the final diff/status. Stage or commit only when authorised, and exclude unrelated work.
- Report exact failures, conflicting authority and unresolved issues. Do not invent completion or change dependencies speculatively.
- Return results to The Manager; specialist conclusions alone do not alter project truth.

## Required handoff

Every delegated specialist task must request a final handoff using the appropriate label:

- `MANAGER HANDOFF - GPT OP`
- `MANAGER HANDOFF - Claude Code`
- `MANAGER HANDOFF - Codex`

```text
MANAGER HANDOFF - [Specialist]

Task:
Result:
Files changed:
Verification:
Decisions made:
Assumptions:
Blockers / unresolved issues:
Documentation follow-up:
Recommended next action:
```

For Claude Code, retain the existing requirement to put the entire single handoff in one fenced code block where its project-local instructions require it. Include no unsupported success claim; distinguish completed work from recommended future action.
