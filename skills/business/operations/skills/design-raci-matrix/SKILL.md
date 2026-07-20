---
name: design-raci-matrix
description: Use when a task, process, or decision has unclear ownership — multiple people assuming someone else is handling it, or no one being sure who has final authority — mapping every significant activity to exactly one Responsible party, one Accountable party, and explicitly defined Consulted and Informed parties, rather than leaving task ownership implicit and assumed.
source: Project Management Institute (PMI), PMBOK Guide, responsibility assignment matrix practice
tags: [business, operations, raci-matrix, decision-rights, accountability, responsibility-assignment]
related: [design-decision-rights-framework, design-organizational-structure, design-committee-charter-framework]
---

# Design RACI Matrix

Map every significant activity in a process or project to exactly one Responsible party, one Accountable party, and explicitly defined Consulted and Informed parties — rather than leaving task ownership implicit and assumed, where multiple people each assume someone else is handling it.

## Why This Is Best Practice

**Adopted by:** The Project Management Institute's PMBOK Guide documents the responsibility assignment matrix (RACI) as a standard project management practice for clarifying roles across complex, multi-stakeholder activities, and RACI matrices are widely used across consulting, technology, and operations functions specifically for cross-functional processes where ownership would otherwise be ambiguous.
**Impact:** Processes and projects without explicit role clarity are documented to experience the "bystander effect" at an organizational level — when responsibility for an activity is diffuse or assumed rather than explicitly assigned, multiple people each assume someone else is handling it, and the activity can go undone entirely, a failure mode explicit RACI assignment specifically prevents by ensuring exactly one person is Accountable for any given outcome.
**Why best:** Leaving task ownership implicit works only as long as informal assumptions about who's responsible happen to align — as soon as they diverge (a new team member unaware of the informal norm, a cross-functional process spanning multiple departments' unstated assumptions), gaps emerge with no clear owner to catch them; an explicit RACI assignment removes this reliance on aligned informal assumption entirely.

Sources: Project Management Institute, PMBOK Guide, responsibility assignment matrix (RACI) practice

## Steps

### Step 1: List the significant activities or decisions in the process

List the significant activities, deliverables, or decisions within the process or project being mapped — specific enough that each line item represents a genuinely distinct activity, not so granular that the matrix becomes unwieldy with dozens of trivial line items.

### Step 2: Assign exactly one Accountable party per activity

For each activity, assign exactly one person as Accountable — the person who ultimately answers for whether the activity is done correctly, even if they don't personally perform it. Assigning more than one Accountable party for a single activity defeats the purpose of the framework, since it recreates the diffuse-responsibility problem RACI is designed to solve.

### Step 3: Assign one or more Responsible parties who actually do the work

Assign the Responsible party or parties — the person or people who actually perform the activity — which can be one or several people, distinct from the single Accountable party who answers for the outcome.

### Step 4: Explicitly identify who is Consulted and who is Informed

Identify who must be Consulted (their input is sought before the activity is finalized, typically because they have relevant expertise or will be materially affected) and who is merely Informed (notified of the outcome, with no input role) — this distinction prevents both under-consultation (missing important input) and over-consultation (bottlenecking simple activities with unnecessary approval layers).

### Step 5: Review and validate the matrix with all parties before finalizing

Review the completed matrix with everyone named in it before treating it as final, since a RACI matrix built without input from the people it assigns roles to risks encoding incorrect assumptions about who actually has the relevant expertise or authority for a given activity.

## Rules

- Assign exactly one Accountable party per activity — never more than one, since shared accountability recreates the diffuse-responsibility problem the framework exists to prevent.
- Distinguish Responsible (who does the work) from Accountable (who answers for the outcome) — these can be, but aren't necessarily, the same person.
- Explicitly distinguish Consulted (input sought before finalizing) from Informed (notified after the fact) — conflating these either bottlenecks simple activities or skips important input.
- Validate the completed matrix with everyone named in it before finalizing, rather than building it in isolation from the people it assigns.

## Examples

**RACI resolving a diffuse-ownership gap:** A cross-functional product launch process previously had no explicit ownership for the go/no-go launch decision, with marketing, engineering, and product each assuming another team owned it. A RACI matrix assigns the product manager as Accountable for the go/no-go decision, with engineering and marketing leads as Consulted — resolving the ambiguity that previously caused the decision to stall with no one taking ownership.

**Distinguishing Consulted from Informed preventing over-bottlenecking:** A process previously required every stakeholder's sign-off before a routine operational change could proceed, causing delays. A RACI matrix reclassifies most stakeholders as Informed rather than Consulted for routine changes, reserving genuine consultation for stakeholders whose input is actually needed — speeding up the process without losing meaningful input.

## Common Mistakes

- **Assigning more than one Accountable party per activity** — this recreates exactly the diffuse-responsibility problem the framework exists to solve.
- **Conflating Responsible and Accountable as always the same person** — the person doing the work and the person who ultimately answers for the outcome are often, but not always, the same, and conflating them can obscure genuine escalation paths.
- **Over-classifying stakeholders as Consulted when they should be Informed** — unnecessary consultation requirements bottleneck routine activities that don't genuinely need broad input.
- **Building the matrix without validating it with the people it assigns roles to** — a matrix built in isolation risks encoding incorrect assumptions about who actually has relevant expertise or authority.

## When NOT to Use

- For a very small team or simple process where ownership is already genuinely clear and unambiguous to everyone involved — formal RACI documentation adds overhead without addressing an actual ambiguity problem in this case.
- For a one-time, simple task rather than a recurring process or complex project — the framework's value is highest for processes with genuine cross-functional ambiguity, not single isolated tasks.
- As a substitute for genuine decision-rights clarity at a strategic level — RACI maps task-level responsibility within a known process; broader questions of who has authority over strategic decisions are better addressed by a decision-rights framework (see `design-decision-rights-framework`).
