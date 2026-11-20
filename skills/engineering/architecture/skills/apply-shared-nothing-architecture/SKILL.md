---
name: apply-shared-nothing-architecture
description: Use when concurrent actors might write to the same file, branch, key, or state object — eliminate the sharing first by giving each actor its own partition, and merge only where the state is read; serialize access structurally (a lock, a single writer, compare-and-swap) only when one shared writer is a genuine invariant.
source: 'Michael Stonebraker, "The Case for Shared Nothing", IEEE Database Engineering Bulletin (1986); Brian Goetz et al., "Java Concurrency in Practice", Addison-Wesley (2006) — thread confinement over synchronization'
tags: [concurrency, distributed-systems, software-architecture, scalability, data-sharding]
related: [apply-idempotent-operations, design-event-driven-architecture, apply-low-coupling]
---

# Apply Shared-Nothing Architecture

When concurrent actors might write to the same resource, default to eliminating the sharing by giving each actor its own partition, and reach for structural serialization only when one shared writer is a real invariant.

## Why This Is Best Practice

**Stonebraker, "The Case for Shared Nothing" (1986):** The foundational paper arguing that partitioning data and processing so that each node owns its own memory and disk, with no shared resource contended by multiple nodes, scales further and fails more gracefully than shared-memory or shared-disk architectures that require coordinating access to a common resource. This architecture underlies the design of large-scale distributed systems built since.

**Goetz et al., "Java Concurrency in Practice" (2006):** The standard reference on concurrent programming correctness, which states as a core principle that thread confinement — giving each thread its own data it never shares — eliminates entire classes of concurrency bugs by construction, and should be preferred over synchronizing access to shared mutable state whenever the design allows it.

**Why best:** Synchronizing access to a shared mutable resource (a lock, a transaction, a compare-and-swap loop) is strictly harder to get correct and scales worse than simply not sharing the resource in the first place — every lock is a potential contention point, deadlock risk, and single point of coordination failure. Eliminating the sharing at the design level removes the problem rather than managing it.

**Adopted by:** Shared-nothing is the architectural basis of Google Bigtable and Spanner, Amazon DynamoDB, and most horizontally-sharded database and distributed-processing systems at scale (originally popularized in this form by Teradata and Tandem in the systems Stonebraker's paper discusses); thread confinement is standard concurrent-programming discipline wherever "Java Concurrency in Practice" is taught or referenced, which is throughout the JVM ecosystem and beyond.
**Impact:** Stonebraker's analysis, borne out by decades of systems built on it since, shows shared-nothing architectures scale near-linearly with added nodes because there's no shared resource to become a bottleneck — the alternative architectures he compares it against (shared-memory, shared-disk) hit a scaling ceiling specifically because contention on the shared resource grows with the number of nodes contending for it.

## Steps

1. **When concurrent actors might write the same file, branch, key, or object, first ask whether they need one shared object at all** — or whether they're actually publishing independent facts that happen to be collected in one place.
2. **Default to giving each actor its own file, key, branch, partition, or state directory.** Two workers each writing their own field into one shared `state.json` is still shared mutation — partition at the object level, not just the field level.
3. **Merge independent contributions only at read time**, by combining each actor's own partition, rather than having actors write into a shared structure concurrently.
4. **Only when one shared write target is a genuine invariant** (a single counter that must be exactly consistent, a unique resource that truly has one owner) should you serialize access structurally — a lockfile, a designated single writer, sequential phases, or compare-and-swap.
5. **Treat "we need a lock" as a signal to check step 1 first**, not as the default solution — ask again whether the sharing itself can be eliminated before reaching for coordination.
6. **Never rely on instructions or convention as concurrency control** — "don't write to this at the same time" documented in a comment or prompt is not a substitute for actual isolation or actual serialization.

## Rules

- Eliminate shared mutable state between concurrent actors by default; serialize access only when a shared writer is a real, unavoidable invariant.
- Partition at the level of the whole object (file, key, branch), not just individual fields within a shared object — field-level partitioning inside one shared structure is still shared mutation.
- Merge independent contributions at read time from separate partitions, rather than coordinating concurrent writes into one structure.
- Treat a perceived need for a lock as a prompt to re-examine whether the underlying sharing can be removed first.

## Examples

**Partitioning instead of locking:** Multiple CI jobs need to report their individual results. Instead of all jobs writing into one shared `results.json` under a lock, each job writes its own `results/<job-id>.json`, and a final aggregation step reads and merges all of them — no lock needed, no contention.

**Genuine shared invariant, serialized structurally:** A single sequence number must be strictly increasing across all writers with no gaps or duplicates. Because this is a real, unavoidable shared invariant, the system uses a single designated writer (or a compare-and-swap loop against one source of truth) rather than attempting to partition the counter.

## Common Mistakes

- **Letting multiple actors write into the same shared file or object, even if each touches a different field**, and calling it safe because "they don't touch the same field" — the shared container itself is still a race.
- **Reaching for a lock as the first solution** to concurrent-write contention, without first asking whether partitioning the actors' outputs would eliminate the contention entirely.
- **Relying on written instructions ("only worker A writes this") as the actual concurrency-control mechanism**, rather than enforcing it structurally.
- **Serializing access to a resource that was never a genuine shared invariant** in the first place, paying a coordination cost that partitioning would have avoided.

## When NOT to Use

- When a resource genuinely has exactly one logical owner that must enforce a strict, global invariant (a unique ID sequence, a single leader election) — serialize that specific resource structurally rather than forcing an artificial partition onto it.
- In a single-threaded, non-concurrent context where no actual concurrent access is possible — the discipline targets genuine concurrent-write scenarios, not all shared state universally.
