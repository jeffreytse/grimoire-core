---
name: apply-theory-of-constraints
description: Use when a system's overall output is capped by one bottleneck resource — a production line, a dev/release pipeline, a service queue, a hiring funnel — and local optimizations elsewhere aren't moving system-wide throughput.
source: Eliyahu M. Goldratt & Jeff Cox, "The Goal" (1984); Goldratt, "It's Not Luck" (1994); Theory of Constraints Institute; APICS/ASCM curriculum
tags: [bottleneck, throughput, constraint-management, lean, operations, process-improvement, capacity-planning, systems-thinking]
related: [apply-pdca, apply-fishbone-diagram, audit-process-efficiency]
---

# Apply Theory of Constraints

Find the single resource that caps a system's throughput, subordinate everything else to it, then elevate it — instead of optimizing parts of the system that aren't the limiting factor.

## Why This Is Best Practice

**Adopted by:** APICS/ASCM (constraint management is a core body-of-knowledge domain in CPIM certification), manufacturers worldwide via Drum-Buffer-Rope scheduling (Ford, Boeing suppliers, Amazon fulfillment network design documented case studies), the Theory of Constraints Institute's certified practitioner network, and widely taught in MBA operations curricula alongside Lean and Six Sigma.
**Impact:** Goldratt Institute case-study compilations and independent TOC literature reviews (Mabin & Balderstone, 2003, "The performance of the theory of constraints methodology," meta-analysis of ~80 published TOC implementations) report median lead-time reductions of ~70%, inventory reductions of ~49%, and revenue/throughput increases of ~63% across manufacturing and project environments. Individual documented cases (e.g., GM's Powertrain Division, Boeing) report double-digit throughput gains within a single fiscal year of implementing the Five Focusing Steps.
**Why best:** Most process-improvement effort defaults to optimizing whatever is easiest to see or measure — busy workers, idle machines, backlog size at any one step. TOC's core insight is that a chain's strength is set by its weakest link: improving any non-constraint resource does not increase system throughput and often just moves inventory or wait time to the real bottleneck. TOC forces improvement effort onto the one point that actually changes the system's output.

Sources: Goldratt & Cox, "The Goal" (1984); Goldratt, "It's Not Luck" (1994); Mabin & Balderstone (2003), International Journal of Operations & Production Management; APICS/ASCM CPIM Body of Knowledge

## Steps

The Five Focusing Steps — run them in order, and treat step 5 as a loop back to step 1, not an end point.

1. **Identify the constraint** — Find the single resource, step, or policy that limits the system's throughput. Look for where work piles up waiting (a queue that never empties) or where the resource runs at or near 100% utilization while other steps sit idle waiting on it. In a pipeline, this is usually the slowest stage measured by time-per-unit-of-work, not the busiest-looking one.
2. **Exploit the constraint** — Before spending money or adding capacity, get maximum output from the constraint as it currently exists. Eliminate anything that wastes its time: don't let it work on items that will be reworked or rejected downstream, don't let it sit idle waiting on upstream handoffs, don't let it context-switch across priorities. Every minute lost on the constraint is a minute of system throughput lost permanently — it can never be recovered.
3. **Subordinate everything else to the constraint** — Set the pace of every non-constraint resource to match the constraint's output rate, even if that means those resources run below their own maximum capacity. Build a buffer of work in front of the constraint so it never starves, and stop feeding work into the system faster than the constraint can process it — excess work-in-progress ahead of the bottleneck just becomes inventory and delay, not output.
4. **Elevate the constraint** — Only after steps 2–3 are exhausted, invest in increasing the constraint's capacity: add a shift, add a machine, add headcount, automate the slow step, change the policy causing the limit. Elevating before exploiting wastes money on capacity the constraint didn't need yet.
5. **Repeat — do not let inertia become the new constraint** — Once the current constraint is broken, a new one appears somewhere else in the system. Go back to step 1 and re-identify it. Explicitly re-examine policies, buffers, and subordination rules set in steps 2–3 for the old constraint — carrying them forward unquestioned onto the new constraint is a common cause of stalled improvement.

Supporting techniques used inside these steps:

- **Throughput accounting** — evaluate decisions by their effect on Throughput (rate of new money generated through sales), Inventory/Investment (money tied up in things intended for sale), and Operating Expense (money spent turning inventory into throughput) — not by local efficiency or unit cost. A change that raises a non-constraint resource's utilization but doesn't raise Throughput is not an improvement.
- **Drum-Buffer-Rope (DBR) scheduling** — the constraint sets the "drum" beat (the pace for the whole system), a time or stock "buffer" protects the constraint from upstream variability, and a "rope" signals upstream release points to only start work at the rate the drum can consume it.

## Rules

- Never improve a non-constraint resource's local efficiency at the cost of constraint uptime or clarity — local efficiency gains that don't raise system throughput are waste, not improvement.
- Always exploit (step 2) before elevating (step 4) — buying capacity for a constraint that's losing output to fixable waste is spending money to hide a process problem.
- Size buffers by variability, not by guesswork — a buffer in front of the constraint should be large enough to absorb the observed variability of upstream steps feeding it, and re-sized as that variability changes.
- Re-run step 1 after every successful elevation — a fixed constraint is followed by a new one; treating the current constraint as permanent stalls the next improvement cycle.

## Examples

**Manufacturing line:** Identify: Station 3 (heat treatment) runs at 98% utilization while Stations 1, 2, 4 average 60–70%; work-in-progress piles up before Station 3. Exploit: eliminate changeover time between batches at Station 3, move quality inspection earlier so Station 3 never processes parts that will be scrapped downstream. Subordinate: Stations 1–2 slow their release rate to match Station 3's throughput, cutting in-process inventory by half. Elevate: add a second heat-treatment unit once exploitation gains plateau. Repeat: Station 4 (final assembly) becomes the new constraint; restart at step 1.

**Software release pipeline:** Identify: the manual QA sign-off step is the constraint — code sits in a "ready for QA" queue for days while CI, code review, and deploy steps are underutilized. Exploit: QA stops re-testing unrelated regressions on every change and focuses only on affected areas; a dedicated triage removes low-risk changes from the manual queue entirely. Subordinate: developers stop merging faster than QA can absorb, capping work-in-progress in the "ready for QA" column. Elevate: add a second QA engineer or invest in automated regression coverage for the highest-volume test paths. Repeat: once QA throughput matches upstream, the deploy-approval step becomes the new constraint.

## When NOT to Use

- When no single resource dominates — throughput is limited roughly equally across several steps, or bottlenecks shift so quickly that "the constraint" isn't stable enough to exploit or subordinate around; start with a broader Lean/waste audit instead (see `audit-process-efficiency`).
- When the system's output isn't the goal — for purely exploratory, creative, or one-off work with no repeatable throughput to optimize, TOC's accounting and subordination concepts don't apply.
- When the true constraint is a market/demand limit rather than an internal resource — if the system can already produce more than customers will buy, elevating internal capacity doesn't increase throughput; the constraint is external and requires a different (sales/market) response.
