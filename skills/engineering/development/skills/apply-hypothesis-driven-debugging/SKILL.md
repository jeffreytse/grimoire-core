---
name: apply-hypothesis-driven-debugging
description: Use when two or more fixes that share an assumption have failed the same test or gate — write the shared assumption down as a falsifiable hypothesis and test it directly with an observation that would come out differently if the assumption is wrong, before attempting another fix that relies on it.
source: 'Andreas Zeller, "Why Programs Fail: A Guide to Systematic Debugging", 2nd ed., Morgan Kaufmann (2009); David J. Agans, "Debugging: The 9 Indispensable Rules", AMACOM (2002)'
tags: [debugging, root-cause-analysis, scientific-method, software-engineering, developer]
related: [apply-five-whys, diagnose-bug, apply-chestertons-fence]
---

# Apply Hypothesis-Driven Debugging

When two or more fixes that share an assumption have failed the same gate, stop writing fixes and test the shared assumption directly, as a falsifiable hypothesis.

## Why This Is Best Practice

**Zeller, "Why Programs Fail" (2009):** Formalizes debugging as a scientific process — observe the failure, form a hypothesis about the cause, derive a prediction the hypothesis makes, run an experiment that could falsify it, and refine or discard the hypothesis based on the result. Zeller's delta-debugging algorithm, built on this cycle, is adopted in Mozilla's automated test-case reduction tooling and taught as the standard debugging curriculum at Saarland University and CMU.

**Agans, "Debugging" (2002):** Codifies the same discipline for working engineers as "Understand the system," "Make it fail," and "Quit thinking and look" — the repeated failure of fixes that share an assumption is the signal that the assumption itself, not the code around it, needs a direct test.

**Why best:** A second or third fix built on an unverified, shared assumption has no better odds than the first — if the assumption is wrong, every fix built on it fails the same way for the same hidden reason, and the engineer burns cycles on the wrong layer of the problem. Writing the assumption down as a hypothesis and finding an observation that would come out differently if it's false converts a guess into a test, which either clears the real obstacle or saves the time that a third guess would have cost.

**Adopted by:** Standard content in university systematic-debugging courses (Zeller's "Why Programs Fail" is used at Saarland, CMU, and in ACM's debugging curricula); the underlying hypothesize-predict-test cycle is the basis of delta debugging, used in Mozilla's bug-reduction tooling and in GCC/LLVM test-case minimization.
**Impact:** Zeller's longitudinal studies of real-world bug reports show that engineers who skip explicit hypothesis testing and iterate on fixes by intuition take measurably longer to converge on root causes than those who test an explicit, falsifiable prediction at each step — because an untested assumption that's wrong silently invalidates every fix built on it.

## Steps

1. **Notice the trigger**: two or more fixes that share one assumption have failed the same test or gate.
2. **Write the assumption down as one sentence** — the thing every failed fix assumed was true.
3. **Find a prediction the assumption makes that a direct observation could contradict.** Look at how failures are distributed (which inputs, which code path, which timing), not only at their size.
4. **Make the observation before writing the next fix.** Instrument, log, or inspect state directly — do not infer the answer from reading the code a second time.
5. **If the evidence contradicts the assumption**, find what the failures share that the assumption did not predict, and fix what causes that pattern — not another patch that still assumes the broken premise.
6. **If the evidence confirms the assumption**, you've eliminated a cause and narrowed the search — move to the next candidate assumption rather than repeating the same one.

## Rules

- Do not write a third fix before the shared assumption behind the first two is written down and tested.
- A hypothesis without a prediction that could come out false is not a hypothesis — find the observation that would disprove it before you trust it.
- Prefer a direct observation (a log, an instrumented value, a reproduced failure) over inference from reading the code.
- When the assumption is wrong, fix what produces the pattern the failures share — not the individual instances.

## Examples

**Premise test before a third patch:** Two independent fixes to a flaky integration test both assume the test's setup fixture runs before the service under test is ready, and both still fail intermittently. Before writing a third retry-based fix, the engineer logs the exact wall-clock readiness time of the service and the exact time the fixture completes across ten runs — confirming the fixture sometimes finishes first, which neither fix addressed because both assumed it never would.

**Hypothesis confirmed, cause eliminated:** A performance regression is suspected to be caused by a new serialization step. Rather than reverting it as a third guess, the engineer profiles a run and confirms serialization time did not change — disproving the hypothesis and redirecting the search to the actual bottleneck.

## Common Mistakes

- **Writing a third or fourth fix on the same unverified assumption** instead of stopping to test the assumption itself once two fixes relying on it have failed.
- **Choosing a hypothesis test that cannot come out false** — an observation that confirms the assumption no matter what, which proves nothing.
- **Inferring the answer from re-reading the code** instead of making a direct observation of the actual running state.
- **Treating the first confirming data point as proof** without checking whether the pattern holds across the full set of failures, not just the most visible one.

## When NOT to Use

- On a first attempt at a fix, before any pattern of repeated failure on a shared assumption exists — this discipline kicks in specifically after that pattern appears.
- When the cost of a direct observation genuinely exceeds the cost of trying one more fix and checking the result (e.g., a trivial, instantly-reversible change) — use judgment on genuinely cheap next attempts.
