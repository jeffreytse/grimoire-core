---
name: apply-reader-load-reduction
description: Use when reviewing or shaping code that's hard to trace — count the layers a reader must cross between a question and its answer, and the hidden or mutable state they must hold in their head; collapse one-caller wrappers and shrink mutable scope until both are low.
source: 'John Ousterhout, "A Philosophy of Software Design", 2nd ed., Yaknyam Press (2021); Google Engineering Practices, "Code Review Guide" — readability standard'
tags: [code-readability, cognitive-load, maintainability, code-review, software-design]
related: [apply-abstraction, apply-encapsulation, apply-law-of-demeter]
---

# Apply Reader Load Reduction

Measure the work a reader must do to understand code — layers to trace, and state to hold in their head — and cut both until a new reader can answer basic questions about it quickly.

## Why This Is Best Practice

**Ousterhout, "A Philosophy of Software Design":** Developed from Ousterhout's Stanford CS 190 course, built around the central thesis that complexity in software is best measured as the cognitive load it imposes on the next person who has to understand it — not lines of code, not cyclomatic complexity alone. The book's core prescriptions (deep modules, pulling complexity downward, avoiding shallow pass-through layers) are specifically aimed at reducing that load, and the course has become one of the most widely referenced modern treatments of software design taught at a top-tier CS program.

**Google Engineering Practices, "Code Review Guide":** States readability explicitly as a review criterion independent of correctness — code that works but that the next engineer cannot quickly understand is treated as a defect in review, not a stylistic nitpick, because the cost of that misunderstanding compounds every time the code is touched again.

**Why best:** Code that technically works but costs a reader minutes of tracing through layers and holding scattered mutable state in their head is a standing tax on every future change — a bug fix, a feature addition, or an incident response all pay that tax again. Measuring and cutting reader load directly (counting layers, shrinking state scope) targets the actual cost driver, rather than proxies like line count that don't reliably track how hard code is to understand.

**Adopted by:** Ousterhout's "A Philosophy of Software Design" is widely assigned in industry reading lists and university courses as the standard modern treatment of this problem; Google's code review culture treats readability as an explicit, enforced review criterion across its engineering organization.
**Impact:** Ousterhout's course and book document repeated case studies where collapsing unnecessary layers and shrinking mutable state scope measurably reduced the number of files and amount of context an engineer needed to hold to make a correct change — the same category of defect (unnecessary complexity) recurring across very different codebases and teams.

## Steps

1. **Pick a piece of code and ask: how many layers does a reader cross between a question ("where does X come from?") and its answer?** Count wrappers, adapters, and indirection hops.
2. **Collapse layers that only forward**: a wrapper with exactly one caller, an adapter with no second implementation, a pass-through method that adds no behavior. Inline them.
3. **Separately, ask how much hidden or mutable state a reader must hold in their head** to predict what the code does — fields, module-level state, globals.
4. **Shrink that state's scope**, in order of preference: a return value over a mutation, a local variable over a field, a field over module-level state, module-level state over a global. Derive values instead of keeping two in sync.
5. **Name an invariant once, at the boundary where it's established**, rather than re-asserting or re-documenting it at every place that consumes it.
6. **Apply the 30-second test**: can a new reader answer "where does X come from?" and "what can change X?" in under 30 seconds? If not, cut another layer or narrow another piece of state's scope.

## Rules

- Measure reader load on two independent axes — layers to trace, and state to track — and address whichever is actually high; they don't always move together.
- Collapse a wrapper or adapter with only one real caller or implementation; the indirection isn't earning its cost.
- Prefer the narrowest scope that works for any piece of state: return value, then local, then field, then module state, then global, in that order of preference.
- Name an invariant at its single point of establishment, not repeated at every consumption site.

## Examples

**Collapsing a one-caller wrapper:** A `UserRepository` interface has exactly one implementation and one caller, added for a hypothetical future second data source that never materialized. Removing the interface and calling the implementation directly removes one layer a reader has to cross with no loss of real flexibility.

**Shrinking mutable scope:** A module-level `currentUser` variable is read and written from six different functions across a file. Refactoring to pass `currentUser` as a function parameter and return value, rather than mutating shared module state, means a reader no longer has to trace all six functions to know what the value might be at any point.

## Common Mistakes

- **Adding an abstraction layer "for future flexibility" with no second implementation or caller yet**, imposing a permanent reading cost for a speculative future benefit.
- **Measuring code quality by line count or file count alone**, missing cases where fewer, denser lines actually require more state-tracking than more, simpler ones.
- **Promoting state to module-level or global scope for convenience**, when passing it explicitly would have kept its scope — and the reader's tracking burden — local.
- **Re-documenting the same invariant at every call site** instead of establishing and naming it once where it's guaranteed.

## When NOT to Use

- For a module with exactly one consumer where a second implementation is concretely planned and imminent, not speculative — the abstraction may be earning its cost already.
- When collapsing a layer would require breaking an externally-depended-upon interface with real external consumers — weigh the reader-load benefit against the compatibility cost explicitly.
