---
name: apply-a3-problem-solving
description: Use when a problem is important or recurring enough to solve properly — performance is below where it should be, a quick fix has already failed, or people disagree about what the problem even is — and you need to go from a vague complaint to a closed, measured gap.
source: 'Toyota Business Practices (TBP) eight-step problem-solving process; John Shook, "Managing to Learn: Using the A3 Management Process" (Lean Enterprise Institute, 2008); Sobek & Smalley, "Understanding A3 Thinking" (Productivity Press, 2008); Liker, "The Toyota Way" (2004); Tucker & Edmondson, "Why Hospitals Don''t Learn from Failures", California Management Review (2003)'
tags: [a3-problem-solving, gap-analysis, root-cause-analysis, countermeasures, toyota-business-practices, continuous-improvement, structured-problem-solving]
related: [apply-problem-reframing, apply-five-whys, apply-fishbone-diagram, apply-pdca, write-okrs]
---

# Apply A3 Problem Solving

Define a problem as the measured gap between the goal and the current state, find the root causes of that gap, match a countermeasure to each cause, then track the gap until it closes — all on one page.

## Why This Is Best Practice

**Adopted by:** Toyota (Toyota Business Practices, taught to every manager), Danaher Business System, Lean Enterprise Institute, and lean healthcare programs at Virginia Mason, ThedaCare, and the UK NHS; the same goal–current state–gap–cause–countermeasure logic underlies Six Sigma DMAIC (GE, Motorola) and McKinsey's structured problem solving.
**Impact:** Tucker & Edmondson (2003) observed hospital nurses and found that in roughly 9 of 10 operational failures, staff applied a quick workaround and never addressed the underlying cause — so the same failures recurred. A3/TBP exists to break this pattern by requiring a verified root cause and a measured gap before any countermeasure, and Toyota attributes its sustained quality and productivity lead to applying it organization-wide (Liker, 2004).
**Why best:** Common alternatives — jumping to a solution, brainstorming fixes without a measured gap, or one-off root-cause analysis with no follow-up — either solve the wrong problem or never confirm the fix worked. A3 links all four stages (right goal, real cause, matched countermeasure, measured follow-up) in one visible document others can challenge.

Sources: Shook (2008); Sobek & Smalley (2008); Liker (2004); Tucker & Edmondson (2003)

## Steps

### 1. Clarify the real goal — ask "why" upward

The first request is often a means, not the end. Ask "why do we want this?" until you reach a goal you can't usefully go above:

```
"We need a new CRM"
  → why? "To track leads better"
  → why? "Leads fall through the cracks"
  → why does that matter? "We lose deals"      ← real goal: win rate on qualified leads
```

Stop when the answer is a business or personal outcome that owners agree on. Choosing the goal at the right level opens solutions the first request ruled out (see `apply-problem-reframing`).

### 2. Measure the current state and state the gap

Write the problem in one sentence with numbers:

```
Goal:     close 30% of qualified leads within 60 days
Current:  18% (last two quarters, CRM export)
Gap:      12 percentage points
```

- Go and see: get the data and look at the actual process, not reports about it.
- If you can't measure the gap, you can't tell later whether it closed — find a proxy metric.

### 3. Break the problem down and pick where to focus

Split the gap into parts (by stage, product, region, shift, customer type) and find where most of it sits:

```
Lost deals by stage:  demo → proposal 45% | proposal → close 35% | other 20%
Focus: demo → proposal
```

Focusing on the biggest piece first prevents spreading effort across everything.

### 4. Set a target for the focused problem

Define what, how much, and by when: "Raise demo→proposal conversion from 40% to 55% by end of Q3."

### 5. Find root causes — ask "why" downward

For the focused problem, ask "why does this happen?" repeatedly until you reach a cause you can act on and that, if removed, would stop the problem (see `apply-five-whys`). For problems with many possible causes, map them first with `apply-fishbone-diagram`.

- Verify each cause with data or direct observation before accepting it.
- Expect several root causes; record each one separately.

### 6. Match one countermeasure to each root cause

| Root cause | Countermeasure | Owner | Due |
|-----------|----------------|-------|-----|
| No follow-up within 48h of demo | Auto-task + template email after every demo | Sales ops | Jul 1 |
| Demo doesn't show buyer's use case | Pre-demo discovery call checklist | Sales lead | Jul 15 |
| Pricing unclear until proposal | Share pricing range at demo | Product marketing | Jul 15 |

A countermeasure with no root cause behind it is a guess. A root cause with no countermeasure stays open.

### 7. Implement and track the gap

Review regularly (weekly for fast processes, monthly for slow ones):
- **Is each countermeasure actually implemented?** If not, remove the blocker.
- **Is the gap shrinking?** Plot the metric against the target.
- **If implemented but the gap isn't closing:** the cause was wrong or incomplete — return to step 5.

Run each countermeasure as a test, not a final answer (see `apply-pdca`).

### 8. Standardize and share

When the target is reached and holds:
- Update the standard process, checklist, or system so the fix doesn't rely on memory.
- Share the A3 so teams with similar problems can reuse it.
- Pick the next-largest piece of the gap from step 3.

### Fit it on one page

Keep the whole story on one A3 sheet (or one doc page): left side = steps 1–5 (goal, current state, gap, breakdown, target, causes); right side = steps 6–8 (countermeasures, follow-up, results). Review the page with the people affected; their challenges are part of the method.

## Rules

- No countermeasure before the gap is measured and the root cause verified.
- One countermeasure per root cause; one owner and date per countermeasure.
- Judge success by the gap metric, not by whether tasks were completed.
- If the gap doesn't close, go back to causes — don't add more actions on top.

## Common Mistakes

- **Starting with the solution:** "the problem is we don't have X" is a solution in disguise; go back to step 1.
- **Unmeasured gaps:** "communication is bad" can never be shown to be fixed.
- **Stopping at the first why:** fixing the symptom brings the problem back.
- **Blame as root cause:** "person X made a mistake" — ask why the process allowed it.
- **No follow-up:** declaring victory at implementation instead of when the gap closes.

## When NOT to Use

- Small one-off issues with an obvious fix — just fix them.
- Emergencies — contain first (stop the bleeding), then run A3 on the cause.
- Highly uncertain, novel problems where cause and effect can only be seen after experimenting — use rapid experiments first, then A3 once patterns appear.
