---
name: apply-data-dominance
description: Use when choosing core types, data structures, or sequencing scaffold-versus-feature work before writing logic — get the data's shape and ownership right first; the right structure makes the surrounding code and algorithm obvious instead of a design problem in its own right.
source: 'Rob Pike, "Notes on Programming in C" (1989), Rule 5 "Data dominates"; Fred Brooks, "The Mythical Man-Month", Addison-Wesley (1975/1995) — "Show me your flowcharts... and I''ll be mystified. Show me your tables... and I won''t usually need your flowcharts"'
tags: [data-structures, software-architecture, system-design, engineering, maintainability]
related: [apply-domain-driven-design, apply-illegal-states-unrepresentable, apply-information-expert]
---

# Apply Data Dominance

Get the data's shape and ownership right before writing logic — the right structure makes the algorithm and the surrounding code nearly write themselves.

## Why This Is Best Practice

**Pike, "Notes on Programming in C" (1989), Rule 5:** States plainly that "data dominates... if you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming." Pike's rules, written at Bell Labs and widely circulated since, remain foundational reading in systems-programming culture (Go's own design, which Pike co-created, reflects the same discipline).

**Brooks, "The Mythical Man-Month":** Makes the same claim independently, two decades earlier, from a different vantage point — decades of observing large software projects at IBM: tables (data layouts) communicate a system's design more clearly and durably than flowcharts (control flow) ever do, because the data's shape constrains and clarifies everything built on top of it.

**Why best:** Logic written against a data structure that doesn't match the actual access pattern accumulates special cases, synchronization bugs, and branches as the system grows — because the logic is fighting the shape of the data at every turn. Getting the structure right first means the dominant access patterns are cheap and the logic that follows has few special cases to handle, because the structure itself already excludes most of them.

**Adopted by:** Pike's rules are standard reading in systems-programming and Go community culture (Pike co-designed Go); Brooks's table-over-flowchart claim is foundational in software engineering pedagogy and still cited in modern system-design literature and interviews.
**Impact:** Both sources independently converge on the same empirical observation across very different eras and contexts (Bell Labs systems code vs. IBM's OS/360 project management) — that the shape of the data, not the cleverness of the algorithm, is what determines whether the resulting code stays simple as the system grows, which is why both treat it as the first design decision, not an implementation detail decided after the logic is sketched.

## Steps

1. **Before writing logic, define the core types and data structures the feature needs.** Trace every access pattern the data will actually go through — reads, writes, concurrent access, the dominant query shape.
2. **Choose the structure that matches the dominant access pattern**, not the structure that's most familiar or the first one that comes to mind.
3. **DRY the structure, not every line.** A repeated structural shape across the codebase is worth consolidating into one type; superficially similar individual lines are not worth abstracting if the underlying shapes differ.
4. **Before sharing state between concurrent actors, ask explicitly what happens if another actor modifies it at the same time.** If the answer isn't "nothing," isolate the state instead of coordinating access to it after the fact.
5. **Sequence scaffold work before feature work.** Whatever will help every later phase — CI, shared types, test harnesses — goes in first, after removing dead code that would otherwise need to be carried through the scaffold.
6. **Keep commits small and single-purpose** so that a structural decision and the logic built on it can each be reviewed and, if wrong, reverted independently.

## Rules

- Define and validate the data shape before writing the logic that consumes it, not alongside it or after.
- Match the structure to the dominant access pattern observed from tracing real usage, not to familiarity or convention.
- Treat concurrent access to shared mutable state as a design question to resolve by isolation, answered before the sharing is implemented, not a bug to patch afterward.
- Sequence foundational, broadly-reused scaffolding ahead of feature-specific logic within a body of work.

## Examples

**Structure chosen from the access pattern:** A feature needs to look up users by ID constantly and iterate all users rarely. The engineer chooses a hash map keyed by ID as the primary structure, with a separate derived list built only when the rare iteration case actually runs — rather than a list scanned linearly for every lookup, which would have been the simpler-looking first draft.

**Isolation chosen over post-hoc synchronization:** Two background workers both need to update progress counters. Rather than sharing one mutable counter object and adding a lock after a race condition appears, each worker is given its own counter from the start, and the totals are merged only when read — eliminating the shared-mutation question instead of solving it after the fact.

## Common Mistakes

- **Writing the algorithm first and picking a data structure to fit it**, discovering later that the structure doesn't match the actual access pattern and needs a rewrite.
- **Defaulting to a familiar data structure (a list, a dictionary) without tracing the real access pattern** the feature will exercise at scale.
- **Sharing one mutable object between concurrent actors without asking what happens under concurrent modification**, and only addressing it once a race condition is observed in production.
- **Abstracting every superficially similar line of code into one function**, rather than reserving consolidation for genuinely repeated structural shapes.

## When NOT to Use

- For small, clearly-scoped, unlikely-to-grow code where the obvious structure is already correct — formal access-pattern tracing adds no value there.
- When the dominant access pattern is itself still unknown or actively changing (early exploratory prototyping) — in that phase, keep the structure simple and revisit this discipline once real usage patterns emerge.
