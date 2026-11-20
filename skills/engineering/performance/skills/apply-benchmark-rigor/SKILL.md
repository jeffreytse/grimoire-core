---
name: apply-benchmark-rigor
description: Use when you are about to trust, report, or act on a measured number — a speedup, a regression, a throughput, a latency, or an eval result — find what actually limits it and rule out that it measured something other than the work intended, rather than trusting a single run or a plausible-looking result.
source: 'Brendan Gregg, "Systems Performance: Enterprise and the Cloud", 2nd ed., Addison-Wesley (2020); Georges, Buytaert, Eeckhout, "Statistically Rigorous Java Performance Evaluation", OOPSLA (2007)'
tags: [performance-engineering, benchmarking, measurement, statistical-rigor, developer]
related: [calculate-statistical-power, profile-web-vitals, audit-performance]
---

# Apply Benchmark Rigor

Before trusting a measured number, find what limits it and rule out that it measured something other than the work you think it measured.

## Why This Is Best Practice

**Gregg, "Systems Performance" (2020):** The standard reference for production performance analysis at scale, used throughout Gregg's work at Netflix and formerly Sun/Oracle and Joyent, builds its methodology around identifying the actual resource or code path that bounds a result (CPU, memory bandwidth, I/O, lock contention) from direct evidence — profiles, counters, traces — rather than from guesses formed by reading code.

**Georges, Buytaert, Eeckhout, "Statistically Rigorous Java Performance Evaluation" (OOPSLA 2007):** A widely-cited empirical study showing that single-run benchmark comparisons on managed runtimes routinely report "improvements" and "regressions" that are statistical noise — run-to-run variance alone can exceed the claimed effect size — and prescribes multiple-run measurement with confidence intervals as the minimum bar for a trustworthy performance claim.

**Why best:** A number without its limiter, its spread, and a check for confounds is not evidence — it is a guess with decimal points. Acting on an unexplained number (shipping a "20% faster" change, or trusting a regression alert) risks optimizing or reverting based on noise, caching effects, or a code path that never actually ran during the measurement, rather than the real change in behavior.

**Adopted by:** Gregg's USE method (Utilization, Saturation, Errors) and systematic performance-analysis methodology are standard practice at Netflix and widely taught in SRE and performance-engineering training industry-wide; statistically rigorous, multi-run benchmarking with reported variance is standard practice in language-runtime benchmarking suites (JMH for Java, criterion for Rust) built directly on the Georges et al. methodology.
**Impact:** Georges et al. demonstrate empirically that naive single-run benchmarking on the JVM produces contradictory conclusions about the same code across repeated trials at a rate high enough to invalidate many published "performance improvement" claims of that era — multi-run measurement with explicit confidence intervals is the field's response, now standard in credible benchmarking tooling.

## Steps

1. **Write the decision before you run the benchmark.** Name the result that would actually change what you do, and the noise floor below which a difference doesn't matter.
2. **Run multiple trials and report the spread, not a single number.** Stop and treat the result as inconclusive if the run-to-run spread is larger than the claimed effect.
3. **Ask "why not double?" for any number you intend to trust.** Name the specific resource or code path that bounds the result, identified from a profile or counters taken during the run — not inferred from reading the code.
4. **List every alternative explanation for the number** — errors swallowed, work skipped or cached, a code path that never executed, noise, or a piece of work too small relative to overhead to matter — and rule out each one with evidence before trusting the result.
5. **Keep the run count, the spread, and the identified limiter attached to the number** whenever you report or act on it, not just the headline figure.
6. **For a performance claim specifically, profile before and after the change**, not just time it, so the limiter you identified before the change is confirmed to be what actually changed.

## Rules

- Never trust or report a single-run number as a performance result; report the spread across multiple runs.
- Identify the limiter from direct evidence (a profile, a counter) taken during the run, not from a guess formed by reading the code.
- Rule out every plausible alternative explanation for the number before acting on it — don't accept the first plausible-looking explanation.
- Stop when the run-to-run spread exceeds the effect size you're trying to measure; a result inside the noise floor is not a result.

## Examples

**Noise floor catches a false regression:** A CI alert flags a 4% latency regression on a single run. Re-running the benchmark ten times shows a baseline spread of ±6% run-to-run — the "regression" is within noise, and the alert threshold is adjusted rather than the code being reverted.

**"Why not double" surfaces the real limiter:** A cache-layer change claims a 10% throughput improvement. Profiling during the run shows the service was still bottlenecked on a downstream database call that the cache change didn't touch — the actual limiter — so the claimed improvement is re-measured isolating the cache layer specifically, rather than trusted end-to-end.

## Common Mistakes

- **Reporting a single-run number as if it were a stable result**, without checking run-to-run variance at all.
- **Explaining a number by reading the code and guessing at the bottleneck**, instead of confirming the limiter with a profile or counters from the actual run.
- **Stopping at the first plausible explanation for a surprising number** without checking the other items on the confound list (caching, skipped work, measurement error).
- **Dropping the spread and limiter when reporting the number**, leaving a reader with no way to judge whether the headline figure is trustworthy.

## When NOT to Use

- For a quick, low-stakes, exploratory timing check with no decision riding on the result — full rigor is overkill when nothing will be acted on based on the number.
- When the effect size is so large relative to any plausible noise floor that a single clear run is genuinely sufficient (an order-of-magnitude change) — judgment still applies, but the bar scales with the stakes of the decision.
