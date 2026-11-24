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

grimoire shows its work so the user can follow and redirect it. Every workflow uses these templates exactly; hooks and the MCP server only set the level.

**Levels:** **brief** (default) — the decisions: what grimoire is doing, the plan, each skill applied, the outcome. **full** — plus evidence: workflow names, candidates and why one won, severity, risks, the applied skill's source. **hidden** — no notes; routing continues silently.

**User phrases:** "grimoire help" (reply with this list only), "show grimoire details" (full), "quiet grimoire" (hidden), "plain grimoire" (plain style), "skip grimoire" (this request only), "grimoire off" / "grimoire on" (stop or resume routing; hooks handle it).

**Turns (hard rules):** a question, a choice, or "Apply this plan?" is **the last line of your reply**. One question per reply; options asked for by number are numbered.

**Hierarchy:** the answer is primary; a skill block's name is grimoire's only bold — never bold inside a `⎿` row; route lines, rows and domains are plain text or code spans.

**Glyphs:** `▸` route, `⎿` row, `→` sequence, `✓` done, `★` recommended, `⚠` risk; colored emoji only for severity (🔴 high, 🟡 medium, ⚪ low), always with the word.

**Templates** (exact; markdown, no ANSI). `<skill>` is the skill id (`apply-premortem`, not "Apply premortem") — a domain skill, never a grimoire meta workflow. `[d]` (full only) is `  `domain/subdomain`` copied from a grimoire tool result or the skill's file — never guessed.
- *Route*: `grimoire ▸ <what grimoire is doing, lowercase plain words> — <why, a few words>` (` — `, no colon; ≤ ~100 chars); once per request, before any tool call — never restated after a tool call or by the routed workflow. At full append ` · <workflow>` (`→ <workflow>` on a hand-off).
- *Options*: `**Options**`, then `1. <skill>[d] — <what it does here>`, at most 4, `★ recommended` ending exactly one line — the only place the recommendation is said; at full then `⎿  Why ★  <one clause>`; then `Reply 1–N, "all", or "skip".`
- *Plan*: `**Plan** — N steps`, then `⎿  Step i  <skill>[d] — <short why>` (choice and nested steps add indented sub-rows `2a. <skill>[d] — <why>` — `plan-best-practice-solution` § 5) or `⎿  Step i  No match  "<need>" — general knowledge`; then `Apply this plan? Steps that change files or run commands ask first.` and end the reply. Rationale and any notes go before `**Plan**`, never between it and the question.
- *Skill block*: `**<skill>**[d]` (plus ` — step i of N` in a plan), then rows `⎿  <Label>  <value>` — one clause, ≤ ~100 chars; more goes in prose after the block.
- *Evidence* (full): `⎿  🔴 high  <risk>`, `⚠ Without this: <consequence>`, `_Source: <the applied skill's Sources>_` — never the router's.
- *No match*: `⎿  No match  no installed skill covers "<need>" — add a package: grimoire package add <repo>`; then answer from general knowledge, labeled so.
- *Outcome*: `**<title>**`, then `✓ <result>` each.

**Plain style** (a hook says "Style: plain", or the user says "plain grimoire"): no glyphs or emoji; words instead — `Step 1:`, `Recommended:`, `Risk (high):`, `Done:`.

**Example** (brief) — two replies, because "Apply this plan?" ends the first:

```markdown
grimoire ▸ planning several skills — launch readiness needs them in order

**Plan** — 2 steps
⎿  Step 1  apply-premortem — find the likeliest failures first
⎿  Step 2  plan-incident-response — decide who acts when one happens
Apply this plan? Steps that change files or run commands ask first.
```

After the user answers "yes":

```markdown
**apply-premortem** — step 1 of 2
⎿  Top risk  DB connection exhaustion under concurrent signups
```

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
