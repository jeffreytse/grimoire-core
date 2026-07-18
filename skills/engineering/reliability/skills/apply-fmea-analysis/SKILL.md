---
name: apply-fmea-analysis
description: Use when evaluating a system, process, or design for potential failure modes before they occur — systematically scoring each potential failure by severity, occurrence likelihood, and detectability to prioritize which failure modes most urgently need a design change or additional control, rather than addressing failures reactively only after they've already happened.
source: AIAG-VDA FMEA Handbook (Automotive Industry Action Group / Verband der Automobilindustrie); originated in MIL-STD-1629A, U.S. military reliability engineering standard
tags: [engineering, reliability, fmea, failure-mode-analysis, proactive-risk-assessment, reliability-engineering]
related: [run-chaos-engineering, design-risk-register, apply-premortem]
---

# Apply FMEA Analysis

Systematically evaluate a system, process, or design for potential failure modes before they occur — scoring each potential failure by severity (how bad the consequence would be), occurrence likelihood (how often it's expected to happen), and detectability (how likely it is to be caught before causing harm) — to prioritize which failure modes most urgently need a design change or additional control, rather than addressing failures only reactively after they've already occurred.

## Why This Is Best Practice

**Adopted by:** Failure Mode and Effects Analysis (FMEA) originated in U.S. military reliability engineering standard MIL-STD-1629A and has since become a standard practice across automotive, aerospace, and manufacturing industries, formalized in the jointly-developed AIAG-VDA FMEA Handbook used across the global automotive supply chain to systematically assess and prioritize potential failure modes during design and process development.
**Impact:** Systems and processes evaluated reactively — where failure modes are addressed only after an actual failure occurs — accumulate the full cost of failures that a proactive analysis could have caught and addressed beforehand; FMEA's systematic scoring specifically surfaces which potential failure modes deserve preventive attention before a real-world failure event forces the issue.
**Why best:** Not every potential failure mode deserves equal preventive attention — a systematic severity × occurrence × detectability scoring method distinguishes failure modes that are both likely and severe (and thus urgently need attention) from those that are unlikely, low-impact, or already well-detected before causing harm, providing a disciplined way to prioritize limited preventive-engineering effort rather than addressing failure modes based on whichever ones happen to be most recently discussed or most memorable.

Sources: AIAG-VDA FMEA Handbook, Automotive Industry Action Group / Verband der Automobilindustrie; MIL-STD-1629A, "Procedures for Performing a Failure Mode, Effects and Criticality Analysis"

## Steps

### Step 1: Identify the system, process, or design elements to be analyzed

Break the system, process, or design under review into its constituent elements or steps — components, process steps, or functions — as the units the failure-mode analysis will be applied to individually, rather than attempting to assess failure risk for the system as an undifferentiated whole.

### Step 2: Identify potential failure modes for each element

For each element, identify its potential failure modes — the specific ways it could fail to perform its intended function — along with the potential effects of each failure mode on the broader system, process, or end user.

### Step 3: Score each failure mode on severity, occurrence, and detectability

Score each identified failure mode on three dimensions: severity (how serious the consequence would be if it occurred), occurrence (how likely the failure is to happen), and detectability (how likely the failure is to be caught before it causes harm) — typically using a numeric scale (e.g., 1-10) for each dimension.

### Step 4: Calculate a risk priority number and prioritize accordingly

Combine the three scores (commonly by multiplying severity × occurrence × detectability) into a risk priority number for each failure mode, and use this number to prioritize which failure modes most urgently warrant a design change, additional control, or further investigation — focusing limited preventive effort on the highest-priority failure modes first.

### Step 5: Implement changes for high-priority failure modes and re-score

For failure modes prioritized for action, implement a design change, additional control, or improved detection mechanism specifically targeting the failure mode's severity, occurrence, or detectability, then re-score the failure mode after the change to confirm the risk priority has actually been reduced — treating FMEA as an iterative process rather than a single static assessment.

## Rules

- Break the system or process into specific constituent elements before identifying failure modes — assessing failure risk for an undifferentiated whole misses many of the specific, addressable failure modes.
- Score every failure mode on all three dimensions (severity, occurrence, detectability) separately, not a single combined risk rating that obscures which dimension actually drives the failure mode's priority.
- Prioritize action based on the combined risk priority number, not merely on whichever failure modes are most recently discussed or most memorable to the team.
- Re-score failure modes after implementing a change to confirm the risk has actually been reduced, rather than assuming a change was effective without verification.

## Examples

**FMEA prioritizing a high-risk failure mode over a memorable but lower-priority one:** A team analyzing a manufacturing process identifies a highly memorable, dramatic-sounding failure mode that scores low on occurrence and has strong existing detection controls, alongside a less dramatic but frequently occurring failure mode with weak detection controls. The systematic severity × occurrence × detectability scoring correctly prioritizes the less dramatic but higher-risk-priority-number failure mode for immediate design attention, avoiding the natural bias toward addressing whichever failure mode is most memorable.

**Iterative FMEA confirming a design change's effectiveness:** A different team implements a design change intended to reduce a failure mode's occurrence likelihood, then re-scores the failure mode and confirms the risk priority number has decreased as intended — verifying the change's actual effectiveness rather than assuming it worked based on the change's intent alone.

## Common Mistakes

- **Assessing failure risk for a system as an undifferentiated whole rather than breaking it into specific elements** — this misses many specific, addressable failure modes that a more granular analysis would surface.
- **Combining severity, occurrence, and detectability into a single subjective risk rating rather than scoring each dimension separately** — this obscures which specific dimension is driving a failure mode's priority and what kind of intervention would most effectively address it.
- **Prioritizing failure modes based on how memorable or recently discussed they are, rather than their calculated risk priority number** — this defeats the systematic prioritization the scoring method is specifically designed to provide.
- **Failing to re-score a failure mode after implementing a change** — without re-scoring, there's no verification that the change actually reduced the risk as intended.

## When NOT to Use

- For a very simple system or process where an informal review adequately surfaces the relevant failure modes without the overhead of formal FMEA scoring.
- As a substitute for direct empirical failure testing — see `run-chaos-engineering` for actively inducing and observing real failures, a complementary but distinct practice from FMEA's structured, analytical failure-mode identification.
- When the system changes so rapidly that a formal FMEA becomes outdated before it can inform any actual design decision — in this case, a lighter-weight, more frequently updated risk assessment approach may better fit the pace of change.
