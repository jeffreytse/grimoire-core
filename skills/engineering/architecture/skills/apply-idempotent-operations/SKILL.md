---
name: apply-idempotent-operations
description: Use when designing a state-changing operation, lifecycle step, or processing loop that can run amid crashes, retries, or restarts — derive each run from the current state compared against the goal state, rather than from what the previous run meant to do, so the operation converges to the same correct end state no matter how many times it runs or where a prior run stopped.
source: 'Pat Helland, "Idempotence Is Not a Medical Condition", ACM Queue (2012); Roy Fielding, "Architectural Styles and the Design of Network-based Software Architectures" (2000) — idempotent HTTP method semantics; AWS Builders'' Library, "Challenges with distributed systems"'
tags: [idempotency, distributed-systems, reliability, architecture, fault-tolerance]
related: [design-event-driven-architecture, design-restful-api, apply-parallel-change]
---

# Apply Idempotent Operations

Derive each run of a state-changing operation from the current state compared against the goal state, rather than from what the previous run meant to do, so the operation converges to the same correct end state no matter how many times it runs or where a prior run stopped.

## Why This Is Best Practice

**Helland, "Idempotence Is Not a Medical Condition" (ACM Queue, 2012):** A foundational treatment establishing idempotency as the property that lets a distributed system tolerate retries, duplicate messages, and partial failures safely — an operation is idempotent when applying it multiple times produces the same result as applying it once, which is what makes "at-least-once" delivery (the only kind reliably achievable across an unreliable network) safe to build on.

**Fielding, "Architectural Styles..." (2000):** Defines idempotent HTTP method semantics (GET, PUT, DELETE) as part of REST's foundational constraints, specifically because a client that doesn't know whether a request succeeded must be able to safely retry it without causing a different or duplicated effect.

**Why best:** In any system that can crash, retry, or receive duplicate messages — which is effectively every distributed or long-running system — an operation that isn't idempotent requires the caller to somehow know exactly how far a prior attempt got before deciding whether to retry, which is often impossible to determine reliably. An idempotent operation sidesteps this entirely: retry freely, from any point, any number of times, and the result converges to the same correct end state.

**Adopted by:** Idempotency keys are standard practice at Stripe, AWS, and most payment and critical-creation API providers specifically for this reason; idempotent HTTP semantics are foundational to REST and enforced by `design-restful-api` in this repository.
**Impact:** AWS's Builders' Library and widely-cited postmortems attribute a large share of distributed-systems correctness bugs specifically to non-idempotent operations run twice (duplicate charges, double-sent notifications, corrupted partial state) after a retry or a crash-and-restart — idempotent design is the standard mitigation, not a special case.

## Steps

1. **Identify every state-changing operation that could run more than once** due to retries, crashes, restarts, or duplicate message delivery — in practice, this is nearly every operation in a distributed or long-running system.
2. **Derive the operation from the current observed state compared against the goal state**, not from "what the previous run was supposed to do." Read the current state, compute the difference from the goal, and apply only that difference.
3. **Make anything a run leaves behind recognizable as stale by the next run** — a lock, a temporary file, a half-written record, a claimed job — using evidence that holds regardless of exactly where the previous run stopped (a timestamp, a unique run ID, a status field).
4. **Use write-then-rename for file-based state changes** — write to a temporary path and atomically rename it into place, so a crash mid-write never leaves a partially-written file mistaken for a complete one.
5. **Ask the explicit test question for every operation**: what happens if this runs twice? What if the previous run crashed at every possible point within it? If the answer depends on what was left behind by the interrupted run, add a reconciliation step that handles that specific leftover state.
6. **Use idempotency keys for operations that can't be made naturally idempotent** (e.g., "charge this card") — a client-supplied unique key lets the receiving system detect and safely no-op a duplicate request rather than re-executing it.

## Rules

- Derive every run from current-state-vs-goal-state comparison, not from the assumption that "this is the first time this runs."
- Treat anything a run leaves behind as potentially stale, and design it to be recognizable as such regardless of exactly when the interruption happened.
- Use atomic write-then-rename for file-based state changes rather than in-place writes that can be observed in a partially-complete state.
- For operations that genuinely cannot be made naturally idempotent, use an explicit idempotency key rather than leaving the caller to guess whether a retry is safe.

## Examples

**Correct idempotent design:** A job-processing system marks a job as "claimed" with a unique worker ID and a timestamp before starting work, rather than simply starting work and marking it "done" at the end. If the worker crashes mid-job, a reconciliation sweep recognizes claims older than a timeout threshold as stale and safely reassigns the job — the claim record, not assumed completion, is what the next run checks against.

**Non-idempotent failure mode (contrast case):** A payment-processing endpoint charges a customer's card and then records the charge in a database, with no idempotency key. A network timeout after the charge succeeds but before the client receives a response causes the client to retry, resulting in the customer being charged twice — a failure specifically caused by the operation not being designed to detect and no-op a duplicate.

## Common Mistakes

- **Designing an operation around "the previous run either succeeded or didn't happen"**, without accounting for the state space of a run crashing partway through.
- **Using in-place writes for state that must survive a crash mid-write**, producing partially-written state indistinguishable from either a complete or an un-started state.
- **Treating idempotency as a concern only for payment-adjacent or famously-dangerous operations**, rather than as a default design requirement for any operation that retries, restarts, or duplicate delivery can reach.
- **Relying on "this shouldn't happen twice in practice" instead of an explicit mechanism** — network timeouts, process restarts, and message-queue redelivery routinely cause operations to run more than once in real systems.

## When NOT to Use

- For genuinely one-shot, non-retriable operations with no failure mode that could cause a second execution — purely in-memory, single-process, non-persisted computations don't need this discipline.
- When the operation is already naturally idempotent by construction (a pure "set this field to value X" operation is idempotent without any additional design work) — this skill is specifically for operations that aren't naturally idempotent and need deliberate design to become so.
- When the performance cost of state comparison before every operation is prohibitive and the operation's actual retry/duplicate-delivery risk has been assessed as genuinely negligible — a deliberate, documented risk acceptance, not a default assumption.
