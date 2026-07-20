---
name: design-model-risk-management-framework
description: Use when a financial institution or similarly regulated organization relies on quantitative models for decisions with material financial consequences — establishing independent model validation, a model inventory with defined ownership, and ongoing performance monitoring, rather than treating a model as trustworthy simply because it was built by a competent team.
source: Board of Governors of the Federal Reserve System / Office of the Comptroller of the Currency, SR 11-7, "Guidance on Model Risk Management" (2011)
tags: [finance, corporate, model-risk-management, model-validation, sr-11-7, governance]
related: [design-ai-governance-framework, calculate-risk-adjusted-return, design-fortress-balance-sheet-strategy]
---

# Design Model Risk Management Framework

Establish independent model validation, a model inventory with defined ownership, and ongoing performance monitoring for quantitative models used in decisions with material financial consequences — rather than treating a model as trustworthy simply because it was built by a competent team.

## Why This Is Best Practice

**Adopted by:** SR 11-7, jointly issued by the Federal Reserve and the Office of the Comptroller of the Currency in 2011, establishes the supervisory expectation for model risk management at regulated financial institutions and has become the de facto industry standard framework for model governance, referenced and adopted well beyond the banks directly subject to it, including by insurers, asset managers, and increasingly by companies using models for AI-driven decisions.
**Impact:** SR 11-7 was issued specifically in response to documented cases where flawed models (in areas including mortgage risk assessment) produced materially wrong outputs that were not caught because no independent party had validated the model's assumptions or ongoing performance — a systemic gap the framework's independent-validation requirement directly targets.
**Why best:** A model built and validated only by the same team that developed it lacks a genuine independent check on its assumptions, limitations, and ongoing performance — the team that built a model has an inherent stake in believing it works, which independent validation (performed by a party with no stake in the model's original development) is specifically designed to counteract.

Sources: Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency, SR 11-7, "Guidance on Model Risk Management" (2011)

## Steps

### Step 1: Maintain a comprehensive model inventory

Maintain an inventory of every model used for decisions with material financial consequences — what the model does, what decisions it informs, who owns it, and when it was last validated — since model risk management can't be applied to models the organization doesn't have visibility into, and models proliferate faster than centralized awareness without active inventory maintenance.

### Step 2: Classify models by risk tier

Classify each inventoried model by risk tier based on the materiality of the decisions it informs and the complexity of its assumptions, since not every model warrants the same depth of validation — a model informing a small operational decision doesn't need the same rigor as one informing material credit or capital decisions.

### Step 3: Require validation independent of model development

Require that model validation be performed by a party independent of the team that developed the model — a separate model risk management function, or at minimum a different individual with no stake in the model's original design — evaluating the model's conceptual soundness, the appropriateness of its assumptions, and whether its outputs are reasonable given its inputs.

### Step 4: Establish ongoing performance monitoring, not just point-in-time validation

Establish ongoing monitoring of each model's actual performance against expectations after deployment, since a model validated as sound at one point in time can degrade as underlying conditions change (a phenomenon sometimes called model drift) — validation at deployment alone doesn't catch this subsequent degradation.

### Step 5: Document model limitations and appropriate use boundaries

Document each model's known limitations and the boundaries of its appropriate use — the specific conditions under which the model's assumptions hold and the conditions under which they don't — so that users of the model's output understand when to apply additional judgment rather than relying on the model output uncritically.

## Rules

- Maintain a comprehensive, current model inventory covering every model used for decisions with material financial consequences.
- Classify models by risk tier and apply validation rigor proportionate to that tier, not uniformly to every model regardless of materiality.
- Require model validation performed independently of the model's original development team — never validation performed solely by the model's own developers.
- Establish ongoing performance monitoring after deployment, not only point-in-time validation before initial use.

## Examples

**Independent validation catching a flawed assumption:** A model's independent validation team identifies that a credit-risk model's key assumption (a stable relationship between two economic variables) no longer holds under current market conditions — a limitation the model's original development team, having built the model under different conditions, had not revisited. The validation team's independence is specifically what allows this fresh, unbiased assessment.

**Ongoing monitoring catching model drift:** A model validated as sound at deployment begins producing measurably less accurate predictions eighteen months later, as underlying customer behavior patterns shift. Ongoing performance monitoring catches this degradation and triggers a re-validation, which point-in-time validation alone (performed only at initial deployment) would have missed entirely.

## Common Mistakes

- **Validating a model only through its own development team, without independent review** — this misses the fundamental purpose of validation, which is to provide a check the original team's own inherent stake in the model's success can't provide.
- **Validating a model once at deployment and never monitoring its ongoing performance** — models can degrade as underlying conditions change, a risk point-in-time validation alone doesn't address.
- **Applying uniform validation rigor to every model regardless of materiality** — this either wastes validation resources on low-stakes models or under-scrutinizes genuinely material ones.
- **Failing to document a model's known limitations and appropriate use boundaries** — users who don't understand a model's limitations tend to apply its output uncritically even in conditions where its assumptions no longer hold.

## When NOT to Use

- For a very simple calculation or rule-based tool with no genuinely material decision consequence — apply model risk management rigor proportionate to actual materiality, not to every calculation regardless of stakes.
- For an organization with no regulatory obligation under SR 11-7 or an equivalent framework and no models informing decisions with material financial consequence — the framework's overhead should be proportionate to actual model risk exposure.
- As a substitute for the separate discipline of governing AI systems more broadly — model risk management specifically addresses quantitative models informing financial decisions; see `design-ai-governance-framework` for the broader AI governance practice.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
