---
name: apply-small-batch-delivery
description: Use when sequencing multi-step work — sweeps, migrations, runs of similar edits — and when stacking commits or pull requests; break the work into small units that each end in a verifiable state, check each before advancing to the next, and order delivery so the sequence itself proves the work to a reviewer.
source: 'Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate: The Science of Lean Software and DevOps", IT Revolution Press (2018) — batch size and deployment frequency as predictors of software delivery performance; Google Engineering Practices, "Small CLs" guide'
tags: [continuous-delivery, batch-size, code-review, devops, software-delivery]
related: [propose-conventional-commit, apply-trunk-based-development, apply-parallel-change]
---

# Apply Small-Batch Delivery

Break multi-step work into small units that each end in a verifiable state, check each one before advancing, and order delivery so the sequence itself proves the work to a reviewer.

## Why This Is Best Practice

**Forsgren, Humble, Kim, "Accelerate" (2018):** The DORA research program's multi-year study of software delivery performance, surveying thousands of organizations, establishes small batch size and deployment frequency as statistically significant predictors of both software delivery performance and organizational performance — smaller units of work, delivered and verified more frequently, correlate with lower change-failure rates and faster recovery from the failures that do occur.

**Google Engineering Practices, "Small CLs":** Google's internal engineering guide explicitly instructs engineers to keep each changelist small and focused on one change, citing faster, more thorough review and easier rollback as the direct, observed benefits — a guide maintained and enforced as policy across Google's engineering organization, not offered as optional advice.

**Why best:** A large batch of changes delivered and verified as one unit hides which specific part caused a failure, and makes rollback an all-or-nothing decision — a reviewer or an incident responder has to untangle the whole batch to find the one change that broke something. Small, independently-verifiable units isolate failure to the smallest possible scope and let a reviewer or a future bisect pinpoint the exact unit responsible.

**Adopted by:** DORA's research is the industry-standard empirical basis for continuous-delivery practice, cited across the DevOps community and embedded in Google's, as well as many other large engineering organizations', formal review and release practices; Google's "Small CLs" policy is enforced engineering practice across its organization.
**Impact:** Accelerate's research across thousands of organizations found that small batch size and frequent, small deployments are among the strongest predictors measured of elite software delivery performance (low change-failure rate, fast recovery, high deployment frequency) — strong enough that DORA's resulting metrics are now a standard industry benchmark for engineering organization performance.

## Steps

1. **Break multi-step work — a sweep, a migration, a run of similar edits — into units that each end in a state you can independently check.**
2. **Treat each unit as a bracket**: start from a known-good state, make one change, run the check for that unit, and only then proceed to the next.
3. **Run the per-unit check even when a tool performs the edits automatically** — an automated sweep still needs each resulting unit verified, not just the final aggregate state.
4. **Do not advance to the next unit until the current one passes its check.** Stopping on a red unit prevents errors from compounding across the rest of the batch.
5. **Order delivery so the sequence itself proves the work to a reviewer**: the failing test before the fix that makes it pass, the subtraction before the reshape it enables, the baseline measurement before the treatment being compared against it.
6. **Land each unit as its own commit or pull request** where the project's workflow allows it, so each is independently reviewable, revertible, and attributable.

## Rules

- Break work into the smallest units that each independently end in a verifiable state.
- Check each unit before advancing to the next — never batch verification to the end of a long sequence.
- Order the sequence so it proves itself: dependency before dependent, failing test before fix, baseline before comparison.
- Land units as separate commits or pull requests whenever the project's workflow supports it.

## Examples

**Migration as verified units:** A codebase-wide rename across 50 files is done as one commit per file (or per logical group), each verified by running the build and tests before the next file is touched — rather than one giant commit covering all 50 files verified only at the very end.

**Sequence that proves itself:** A bug fix is delivered as two commits: the first adds a failing test that reproduces the bug, the second makes the fix that turns it green. A reviewer can see from the sequence alone that the fix actually addresses the reproduced bug, rather than trusting a single combined commit's claim.

## Common Mistakes

- **Batching a long sweep or migration into one commit verified only at the end**, making it impossible to tell which specific change caused a failure that shows up.
- **Running an automated edit tool across many files and verifying only the aggregate result**, skipping the per-unit check that would catch a bad edit early.
- **Landing a fix and its supporting test in the wrong order** (or combined into one commit), losing the proof that the test actually reproduces the bug the fix addresses.
- **Mixing unrelated changes into one large pull request**, forcing a reviewer to evaluate several independent decisions as if they were one.

## When NOT to Use

- For a genuinely atomic change that cannot be meaningfully subdivided into smaller independently-verifiable units — forcing an artificial split would add overhead with no benefit.
- In a context where the project's tooling or workflow cannot support independent verification per unit (e.g., a monolithic deploy with no partial-rollout capability) — the principle still applies to how the work is structured internally, even if delivery itself must be atomic.
