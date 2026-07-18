---
name: design-operational-risk-framework
description: Use when managing the risk of loss from failed internal processes, people, systems, or external events — organizing operational risk into a specific loss-event taxonomy, tracking key risk indicators, and running periodic risk-control self-assessments, rather than treating "operational risk" as a vague catch-all category with no structured process of its own.
source: Basel Committee on Banking Supervision, "Sound Practices for the Management and Supervision of Operational Risk"
tags: [business, operations, operational-risk, key-risk-indicators, risk-control-self-assessment, loss-event-taxonomy]
related: [apply-iso-31000-risk-framework, apply-fmea-analysis, design-compliance-risk-assessment]
---

# Design Operational Risk Framework

Manage the risk of loss arising from failed internal processes, people, systems, or external events by organizing operational risk into a specific loss-event taxonomy, tracking key risk indicators that provide early warning of rising operational risk, and running periodic risk-control self-assessments — rather than treating "operational risk" as a vague catch-all category with no structured process of its own.

## Why This Is Best Practice

**Adopted by:** The Basel Committee on Banking Supervision's "Sound Practices for the Management and Supervision of Operational Risk" establishes operational risk as a distinct risk category (alongside credit and market risk) requiring its own structured management framework, including a standard loss-event taxonomy (internal fraud, external fraud, employment practices, clients/products/business practices, damage to physical assets, business disruption and system failures, and execution/delivery/process management), and this structured approach has become standard practice across regulated financial institutions and increasingly across other large organizations managing operational risk.
**Impact:** Organizations that treat operational risk as an undifferentiated catch-all — "anything that isn't market or credit risk" — tend to lack the specific tools (a defined loss-event taxonomy, tracked leading indicators, systematic control self-assessment) needed to actually identify, measure, and manage this risk category with the same rigor applied to market and credit risk, resulting in operational losses that a more structured framework would have provided earlier warning of or better prevented.
**Why best:** Operational risk spans a genuinely diverse set of failure types — internal fraud, system outages, process errors, external events — that don't share a common driver the way market risk (price movements) or credit risk (counterparty default) do; a specific taxonomy and dedicated tracking tools (key risk indicators, risk-control self-assessments) are needed to bring the same structured rigor to this diverse category that other risk types already receive by default, rather than leaving it as an unstructured residual category.

Sources: Basel Committee on Banking Supervision, "Sound Practices for the Management and Supervision of Operational Risk"

## Steps

### Step 1: Adopt a specific loss-event taxonomy for operational risk

Adopt a specific taxonomy categorizing operational risk into its constituent types — internal fraud, external fraud, employment practices and workplace safety, clients/products/business practices, damage to physical assets, business disruption and system failures, and execution/delivery/process management errors — providing a structured basis for identifying and tracking operational risk rather than treating it as an undifferentiated category.

### Step 2: Identify key risk indicators for each operational risk category

For each category in the taxonomy, identify specific, measurable key risk indicators (KRIs) — metrics that provide early warning of rising operational risk before an actual loss event occurs, such as staff turnover rate for employment-practices risk, system downtime frequency for business-disruption risk, or transaction error rates for process-management risk.

### Step 3: Track key risk indicators on an ongoing basis and set alert thresholds

Track the identified key risk indicators on an ongoing, regular basis and set explicit alert thresholds that trigger a response when a KRI moves into a range indicating elevated operational risk — providing genuine early warning rather than only recognizing rising operational risk after an actual loss event has already occurred.

### Step 4: Conduct periodic risk-control self-assessments

Conduct periodic risk-control self-assessments (RCSAs) — structured reviews where business units assess the operational risks specific to their function and the effectiveness of the controls currently in place to manage them — surfacing control gaps proactively rather than only after a loss event reveals them.

### Step 5: Log actual operational loss events and use them to refine the framework

Log actual operational loss events as they occur, categorized against the taxonomy from Step 1, and use this loss-event history to refine key risk indicators, alert thresholds, and self-assessment focus areas over time — treating the framework as one that improves based on genuine experience, not a static structure set once and left unchanged.

## Rules

- Adopt a specific loss-event taxonomy for operational risk rather than treating it as an undifferentiated catch-all category.
- Identify measurable key risk indicators for each taxonomy category, providing early warning ahead of an actual loss event, not only recognition after one occurs.
- Set explicit alert thresholds for key risk indicators and respond when they're triggered, rather than tracking metrics without a defined action threshold.
- Log actual operational loss events against the taxonomy and use this history to refine the framework's indicators and self-assessment focus over time.

## Examples

**Key risk indicator providing early warning before a loss event:** An organization tracks a key risk indicator for its business-disruption/system-failure category and observes it moving toward its set alert threshold well before any actual outage occurs. This early warning prompts a proactive review and remediation of the underlying system issue, avoiding what could otherwise have become an actual operational loss event.

**Undifferentiated operational risk missing a control gap (illustrative failure mode):** A different organization treats operational risk as a vague, undifferentiated category with no specific taxonomy, key risk indicators, or structured self-assessment process. A control gap in its execution/process-management function goes unidentified until an actual costly processing error occurs — a gap a structured risk-control self-assessment would very plausibly have surfaced proactively.

## Common Mistakes

- **Treating operational risk as an undifferentiated catch-all rather than adopting a specific loss-event taxonomy** — this prevents the kind of structured, category-specific tracking and management that reduces operational losses.
- **Tracking key risk indicators without setting explicit alert thresholds or a defined response** — metrics tracked without an action threshold provide data but not genuine early warning that triggers timely action.
- **Skipping periodic risk-control self-assessments** — waiting for an actual loss event to reveal a control gap is far costlier than proactively surfacing the gap through structured self-assessment.
- **Failing to use actual logged loss events to refine the framework over time** — a framework that doesn't learn from genuine operational-loss experience misses the opportunity to improve its own indicators and focus areas.

## When NOT to Use

- For a very small organization where the overhead of a formal, Basel-style operational risk framework exceeds its practical value — a lighter, less formal approach to identifying and managing operational failure points may be proportionate in this case.
- As a substitute for the organization's general enterprise risk management process — operational risk is one specific risk category within the broader ERM process, not a replacement for addressing strategic, financial, or compliance risk.
- When a specific operational failure mode is better addressed through a more targeted technique — see `apply-fmea-analysis` for structured, engineering-level failure-mode analysis of a specific system or process, which can feed into this broader organizational framework.
