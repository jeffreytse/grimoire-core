---
name: apply-monte-carlo-risk-simulation
description: Use when a project's cost or schedule depends on multiple uncertain estimates — running a Monte Carlo simulation across many randomized combinations of those estimates to produce a probability distribution of likely outcomes, rather than relying on a single-point estimate that hides how much uncertainty actually surrounds it.
source: Project Management Institute (PMI), PMBOK Guide, quantitative risk analysis techniques; AACE International Recommended Practices for Monte Carlo schedule and cost risk analysis
tags: [engineering, project-management, monte-carlo-simulation, quantitative-risk, expected-monetary-value, schedule-risk]
related: [design-risk-register, design-portfolio-stress-test, apply-fmea-analysis]
---

# Apply Monte Carlo Risk Simulation

When a project's cost or schedule depends on multiple uncertain estimates, run a Monte Carlo simulation — repeatedly recalculating the project outcome using many randomized combinations of those estimates drawn from their plausible ranges — to produce a full probability distribution of likely outcomes, rather than relying on a single-point estimate that hides how much genuine uncertainty actually surrounds it.

## Why This Is Best Practice

**Adopted by:** The Project Management Institute's PMBOK Guide documents Monte Carlo simulation as a standard quantitative risk analysis technique, and AACE International (the Association for the Advancement of Cost Engineering) publishes Recommended Practices specifically for applying Monte Carlo simulation to schedule and cost risk analysis, both reflecting broad adoption of this technique across project-based industries (construction, engineering, IT, aerospace) as the standard method for quantifying cost and schedule uncertainty.
**Impact:** A single-point cost or schedule estimate presents a single number without communicating how much uncertainty surrounds it — two projects with identical single-point estimates can have very different underlying uncertainty (one built from tightly-estimated, well-understood tasks, another from highly uncertain, novel tasks), and a single-point estimate alone doesn't distinguish between these genuinely different risk profiles the way a full Monte Carlo-derived probability distribution does.
**Why best:** Simply adding up "most likely" estimates for each project task and presenting the sum as the project's cost or schedule ignores that uncertainty in individual tasks compounds in ways a simple sum doesn't capture — Monte Carlo simulation, by running many randomized combinations of the individual uncertain inputs, produces a genuine probability distribution of overall outcomes (e.g., "70% probability of finishing within X weeks"), providing decision-makers a much richer, more honest picture of project risk than a single deterministic number.

Sources: Project Management Institute, PMBOK Guide, quantitative risk analysis techniques; AACE International Recommended Practice for Monte Carlo schedule and cost risk analysis

## Steps

### Step 1: Identify the project's uncertain cost or schedule inputs

Identify the specific project cost or schedule inputs that carry meaningful uncertainty — individual task durations, cost estimates, or other variables where a single-point estimate would understate the genuine range of plausible outcomes — as the inputs the simulation will vary.

### Step 2: Define a plausible range and distribution for each uncertain input

For each identified uncertain input, define a plausible range (a minimum, most likely, and maximum estimate) and an appropriate probability distribution shape (commonly triangular or PERT/beta distributions for project estimates) reflecting the actual uncertainty around that specific input, rather than treating every input as equally and symmetrically uncertain by default.

### Step 3: Run the simulation across many randomized iterations

Run the Monte Carlo simulation across a large number of iterations (commonly thousands), each iteration randomly sampling a value for every uncertain input from its defined distribution and calculating the resulting overall project cost or schedule outcome for that specific combination of sampled values.

### Step 4: Interpret the resulting probability distribution of outcomes

Interpret the simulation's output as a full probability distribution of possible project outcomes — for example, reading off the cost or schedule value associated with a specific confidence level (e.g., "there is a 70% probability of completing within this cost or timeframe") — rather than reducing the rich distribution back down to a single number without its accompanying probability context.

### Step 5: Use the simulation results to inform contingency and risk-response decisions

Use the simulation's probability distribution to inform concrete decisions — setting cost or schedule contingency reserves at a chosen confidence level, identifying which uncertain inputs contribute most to overall variability (to prioritize risk-reduction effort on those specific inputs), and communicating project risk to stakeholders with genuine probabilistic context rather than false single-number precision.

## Rules

- Identify which specific cost or schedule inputs carry meaningful uncertainty, rather than treating every input as equally uncertain or applying the technique without this identification step.
- Define a plausible range and appropriate distribution shape for each uncertain input based on its actual characteristics, not a default, uniform assumption applied to every input.
- Run the simulation across a sufficient number of iterations to produce a stable, reliable probability distribution, not too few iterations to be statistically meaningful.
- Interpret and communicate results as a full probability distribution with an associated confidence level, not reduced back to a single deterministic number without that context.

## Examples

**Monte Carlo simulation revealing hidden schedule risk:** A project team's simple sum of "most likely" task durations produces a single-point schedule estimate. Running a Monte Carlo simulation across the same tasks' full uncertainty ranges reveals that achieving that single-point date carries only a 40% probability of success — informing a more realistic contingency and communication with stakeholders than the original single-point estimate alone would have supported.

**Simulation identifying the dominant source of project risk:** A different project's simulation results show that the overall schedule variability is driven disproportionately by uncertainty in one or two specific tasks, rather than being evenly distributed across all tasks. This finding directs the team's risk-reduction effort specifically toward those few high-contribution tasks, rather than spreading limited risk-management effort evenly and less effectively across the entire project.

## Common Mistakes

- **Treating every input as equally and symmetrically uncertain rather than defining a specific, realistic range and distribution for each** — this produces a simulation output that doesn't genuinely reflect the project's actual risk profile.
- **Running too few simulation iterations to produce a statistically stable probability distribution** — an inadequate number of iterations can produce misleading or unstable results.
- **Reducing the simulation's rich probability distribution back down to a single number without its confidence-level context** — this discards the specific advantage Monte Carlo simulation provides over a simple single-point estimate.
- **Failing to use the simulation results to inform actual contingency-setting or risk-reduction prioritization decisions** — the analysis should directly inform concrete project decisions, not remain a standalone reporting exercise.

## When NOT to Use

- For a very small or simple project where the effort of defining input distributions and running a simulation exceeds its practical decision-making value — a simpler estimating approach may be proportionate in this case.
- Without genuine, reasonably informed estimates of each uncertain input's plausible range — a simulation built on arbitrary or poorly-considered input ranges produces an output no more reliable than the poorly-considered inputs feeding it.
- As a substitute for qualitative risk identification — see `design-risk-register` for identifying and tracking the specific risks that inform which inputs actually carry meaningful uncertainty in the first place.
