---
name: start-best-practice
description: Use when responding to any user request — entry point into grimoire. Routes the input to the matching grimoire workflow (as listed in README.md), or exits silently if grimoire is not installed.
source: Toyota Production System poka-yoke (Shingo, 1986) — error prevention before the action, not after
tags: [proactive, interception, pre-action, best-practice-discovery, guardian, poka-yoke, quality-gate]
---

# Start Best Practice

Entry point into grimoire. Routes any user input to the matching grimoire workflow listed in README.md. Exits silently if grimoire is not installed or no workflow applies — invisible when not needed.

## Why This Is Best Practice

**Adopted by:** Toyota's poka-yoke principle (Shingo, 1986) is the foundation of error prevention in manufacturing — checking conditions *before* an action begins, not after defects appear. This principle is applied across aviation (pre-flight checklists), surgery (WHO Surgical Safety Checklist), and software (pre-commit hooks, CI gates).
**Impact:** The WHO Surgical Safety Checklist reduced surgical complications by 36% and deaths by 47% — not by changing technique, but by systematically intercepting the moment before each critical step (Haynes et al., 2009, NEJM). Pre-commit hooks catch an estimated 30–40% of common defects before they enter the codebase (GitHub internal data).
**Why best:** Reactive systems wait for the user to ask. Proactive interception closes the "I didn't know a best practice existed" gap — the most common reason practices aren't applied. The cost is minimal (a silent route check); the benefit is consistent practice application without requiring the user to know what to ask.

Sources: Shingo (1986) "Zero Quality Control: Source Inspection and the Poka-Yoke System"; Haynes et al. (2009) NEJM; GitHub Engineering blog

## Skill Access

This skill finds and loads other grimoire skills. Use whichever access this session has:
- **Skills mode** — grimoire skills are installed in the agent: they are listed in context; load one with the Skill tool (or its `/skill-name` command).
- **MCP mode** — grimoire MCP tools are available (`grimoire_get_skill`, …): find candidates with `grimoire_search_skills` (one focused query per need) or `grimoire_list_skills` for a domain; load one with `grimoire_get_skill`. Score and name only skills these tools return.

Below, "installed skills" means the skills reachable this way, and "load" / "invoke" means the matching loader.

## Steps

### Step 0: Route to grimoire workflow (silent)

Silently match the input to a grimoire workflow. No scoring, no output. If no row matches, exit immediately and proceed with the original request unmodified.

| Intent signal | Route |
|---------------|-------|
| Describes a problem, goal, or situation without specifying an approach — including vague or unclear problems | invoke `suggest-best-practice` |
| Has a solution, plan, or design — wants gap analysis | invoke `review-best-practice-fit` |
| Needs 2+ practices coordinated in sequence — across one domain or many — and sub-problems are identifiable upfront | invoke `plan-best-practice-solution` |
| Complex problem where sub-problems are opaque and emerge through execution, not upfront | invoke `apply-best-practice-tree` |
| Mentions a domain or asks what skills/practices exist — without a specific problem to solve | invoke `discover-best-practices` |
| Wants to understand what a skill does, why it exists, or how to use it | invoke `explain-best-practice` |
| Wants to learn or teach a practice through structured explanation or walkthrough | invoke `teach-best-practice` |
| Wants to install, upgrade, or health-check grimoire | invoke `install-grimoire` |
| Wants to view, change, or validate grimoire settings or preferences | invoke `configure-grimoire` |
| Wants to activate a named paradigm or methodology (OOP, TDD, clean-architecture, etc.) | invoke `apply-best-practice-profile` |
| Wants to systematically align a project to stated practice preferences | invoke `apply-best-practice-driven-development` |
| Wants a compliance check of an artifact against pinned preferences | invoke `check-best-practice-compliance` |
| Has a specific finding from a compliance report to fix | invoke `fix-best-practice-finding` |
| Two practices exist — wants side-by-side comparison before deciding | invoke `compare-best-practices` |
| Two practices conflict — wants to reason through which fits better | invoke `resolve-best-practice-conflict` |
| Resolved a conflict — wants to save the decision for future sessions | invoke `pin-best-practice-preference` |
| States a standing preference or standard to follow — "I follow X when there's a conflict", "we always use Y" — even without asking for anything | invoke `pin-best-practice-preference` |
| **None of the above** | **exit silently** — grimoire not installed or not applicable |

Note: `analyze-best-practice-problem` has no direct routing row — vague or unclear problems are routed to `suggest-best-practice` (via "Describes a problem... including vague or unclear problems"), which internally invokes `analyze-best-practice-problem` via its clarity check. This keeps the routing table's problem-description row as the single entry point for all problem inputs.

**Transparent passthrough (exit silently — grimoire not applicable):**
- Primary verb is explanatory: *explain, describe, what is, how does, tell me about, define* — for general facts and definitions ("what is TDD?", "how does BM25 work?"). **Exceptions:** "give me best practices for X" signals discovery, route to `discover-best-practices`; asking *why* a practice works, or what evidence supports it ("why does TDD actually work?"), wants the practice explained, route to `explain-best-practice`
- Conversational acknowledgment: "ok", "thanks", "looks good", "got it", "continue"
- Explicit skill invocations — `/skill-name`, `/grimoire:skill <name>`, or `grimoire:<name>` — user already knows what they want (see Rules)
- Follow-up message in an ongoing execution (not a new intent)
- User signals they know what they want: "just [verb]", "quickly [verb]", "I know how to…", "skip guidance", "no best practices"

**If ambiguous:** prefer the more specific workflow row. Only exit silently when no row matches.

**When a workflow matches:** show the route line (see Display), then invoke the workflow. Then stop — the routed skill handles everything from that point.

## Rules

- Never announce when no workflow matches — proceed silently
- No clarifying questions — route on what's available, or pass through silently
- If user explicitly invoked a skill by name, don't intercept — they already know what they want
- No scoring, no confidence thresholds — routing only

## Display

grimoire shows its work so the user can follow each decision and redirect it. This section is the one definition of that display; grimoire's hooks and MCP server only say which level is on.

**Levels** (progressive disclosure — primary decisions always, evidence on demand):
- **brief** (default) — the decisions: the route, the plan, each skill as it is applied, the outcome.
- **full** — brief plus the evidence: candidate skills and why one was chosen, severity rows, ⚠️ risks, and each skill's source.
- **off** — nothing; route and apply silently.

The user changes the level for the rest of the session by saying "show grimoire details" (full) or "quiet grimoire" (off — this only hides grimoire's notes; keep routing and applying skills silently. Turning grimoire itself off is "grimoire off", handled by grimoire's hooks). "skip grimoire" skips grimoire for the current request.

**Hierarchy** — three levels, so grimoire's process never outweighs the answer:
1. *Primary* — the answer itself.
2. *Secondary* — each skill block's name, the only bold text in grimoire's output.
3. *Tertiary* — everything else: the route line, rows, domains (plain text or code spans). Nothing in a `⎿` row is bold — not the label, not a word in the value; a point that matters that much belongs in the answer.

**Glyphs** — one text family for structure: `▸` route, `⎿` row, `→` sequence, `✓` done, `★` recommended, `⚠` risk. Colored emoji only where color is the meaning: severity 🔴 high, 🟡 medium, ⚪ low — always followed by the word.

**Elements** — markdown only, no ANSI codes (the agent renders the markdown):
- *Route* — one plain line: `start-best-practice ▸ [workflow]`, the domain in a code span, a dash, and why.
- *Block* — one per workflow or skill as it runs: the bold skill name, its domain in a code span, then rows. A plan step's header ends with its position — `— step 2 of 4` — so the user knows where the plan is.
- *Row* — one per line: `⎿`, a plain label, two spaces, the value.
- *Severity, risk, source* (full) — `⎿  🔴 high  …`, `⚠ Without this: …`, the skill's Sources line in italics.
- *Question* — one at a time, as a block's body; then stop and wait (use the agent's question tool if it has one).
- *No match* — when a workflow ran but no installed skill fits, say so with the need you searched for and how to add coverage: `⎿  No match  no installed skill covers "rotation scheduling" — add a package: grimoire package add <repo>`. Then answer from general knowledge, labeled as such.
- *Outcome* — a bold title, then one `✓` row per result.

**Plain style** — when a grimoire hook says "Style: plain" (for screen readers, or `NO_COLOR`): no glyphs or emoji; the same structure in words — `Step 1:`, `Risk (high):`, `Done:`.

**Example** (brief):

```markdown
start-best-practice ▸ plan-best-practice-solution  `meta/routing` — several practices are needed, in order

**plan-best-practice-solution**  `meta/planning`
⎿  Step 1  apply-premortem  `business/strategy`
⎿  Step 2  design-slo  `engineering/reliability`
⎿  Step 3  plan-incident-response  `engineering/devops`
Apply this plan?

**apply-premortem**  `business/strategy` — step 1 of 3
⎿  Top risk  DB connection exhaustion under concurrent signups

**Pre-launch protocol ready**
✓ Risks mapped — fix the DB pool today
```

At **full**, add rows under each block — for example `⎿  🔴 high  DB connection exhaustion`, `⚠ Without this: you find failure modes in production`, `_Source: Klein, Sources of Power (1998)_`.

Show nothing for grimoire when no workflow routes. Never put grimoire formatting on the answer itself.

## Key Differences from `suggest-best-practice`

| | `suggest-best-practice` | `start-best-practice` |
|---|---|---|
| Invocation | User invokes directly | Runs before every request when the agent's instructions trigger it (skills mode); in MCP mode, invoke as `grimoire:start-best-practice` |
| Unrelated inputs | N/A — user invokes directly | Exit silently (grimoire not installed) |
| Low confidence | Asks clarifying question | Exits silently |
| Scoring | Yes — scores all installed skills | No — routes only |
| Browse mode | Supported | Not supported |
| Dispatch role | No | Yes — entry point into grimoire |

## Common Mistakes

**Announcing a failed match**: if no row matches, say nothing and proceed. Interrupting the user for uncertain matches destroys trust.

**Intercepting explicit skill invocations**: if the user said `/write-unit-test` or `grimoire:write-unit-test`, they already know what they want. Don't re-intercept.

**Routing then not stopping**: after invoking a workflow skill, stop. The routed skill handles everything from that point.

**Treating task-starts as a special case**: "implement X", "write Y", "fix Z" all match "Describes a problem, goal, or situation" → route to `suggest-best-practice`. No separate domain scoring needed here.
