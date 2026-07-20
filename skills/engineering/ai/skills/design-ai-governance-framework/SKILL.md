---
name: design-ai-governance-framework
description: Use when an organization is establishing oversight for how it develops, deploys, or uses AI systems — classifying AI use cases by risk level, assigning accountable owners, and applying oversight proportionate to each use case's actual risk, rather than applying either no governance or the same uniform review process to every AI use case regardless of its actual risk level.
source: NIST AI Risk Management Framework (AI RMF 1.0, 2023)
tags: [engineering, ai, ai-governance, risk-management, model-oversight, nist-ai-rmf]
related: [design-model-risk-management-framework, audit-model-fairness, design-data-governance-policy]
---

# Design AI Governance Framework

Establish oversight for how the organization develops, deploys, or uses AI systems by classifying AI use cases by risk level, assigning accountable owners, and applying oversight proportionate to each use case's actual risk — rather than applying either no governance or the same uniform review process to every AI use case regardless of its actual risk level.

## Why This Is Best Practice

**Adopted by:** The NIST AI Risk Management Framework (AI RMF 1.0, 2023) provides the US government's voluntary framework for AI risk governance, structured around four core functions (Govern, Map, Measure, Manage), and has been adopted as a reference framework by organizations across sectors establishing formal AI governance programs, including explicit incorporation into federal agency AI governance requirements.
**Impact:** Organizations that apply the same AI governance process uniformly — either reviewing every AI use case with the same heavy process, or applying essentially no formal review to any of them — are documented to either bottleneck low-risk AI adoption unnecessarily or miss genuine risk in high-stakes use cases (biased hiring models, safety-critical automated decisions) that warrant substantially more scrutiny than a low-stakes internal productivity tool.
**Why best:** AI use cases genuinely differ enormously in their risk profile — an internal writing-assistance tool and an automated loan-approval model carry categorically different consequences if they behave unexpectedly — and a risk-tiered governance approach applies oversight proportionate to actual risk, avoiding both the unnecessary friction of uniform heavy review and the genuine exposure of uniform light review applied to high-stakes use cases.

Sources: National Institute of Standards and Technology (NIST), AI Risk Management Framework (AI RMF 1.0), January 2023

## Steps

### Step 1: Inventory current and planned AI use cases

Build and maintain an inventory of the organization's current and planned AI use cases — what AI systems are in use, for what purpose, and by which teams — since governance can't be applied to use cases the organization doesn't have visibility into.

### Step 2: Classify each use case by risk level

Classify each AI use case by risk level based on factors including the consequence of the system behaving incorrectly (safety, financial, legal, reputational impact), whether the system makes or materially influences decisions about people (hiring, lending, healthcare), and the degree of human oversight in the decision loop — using these factors to sort use cases into risk tiers (e.g., minimal, limited, high) consistent with the tiered-risk approach used across major AI governance frameworks.

### Step 3: Assign accountable ownership for each use case

Assign a specific, accountable owner for each AI use case — a named individual or team responsible for the system's ongoing appropriateness, not an assumed or undefined shared responsibility — since AI systems that drift out of appropriate use or degrade in performance need a clear, accountable party to catch and address this.

### Step 4: Apply oversight proportionate to each risk tier

Apply a defined level of governance rigor to each risk tier — minimal-risk use cases may require only basic documentation, while high-risk use cases require formal pre-deployment review, ongoing performance monitoring, and defined escalation paths for detected issues — rather than applying the same process uniformly regardless of tier.

### Step 5: Establish ongoing monitoring and periodic re-classification

Establish ongoing monitoring for deployed AI systems, and periodically re-classify use cases as their actual usage or context evolves, since a system initially deployed for a low-risk purpose can be repurposed into a higher-risk use case over time without a corresponding governance review unless this re-classification step is built in.

## Rules

- Maintain a current inventory of AI use cases — governance can't be applied to use cases the organization lacks visibility into.
- Classify every use case by risk tier based on consequence, impact on individuals, and degree of human oversight — not treated as uniformly high- or low-risk by default.
- Assign a specific, accountable owner to every AI use case, not an assumed shared responsibility.
- Apply governance rigor proportionate to each use case's risk tier, and re-classify use cases periodically as their actual usage evolves.

## Examples

**Risk-tiered governance avoiding unnecessary friction:** An organization classifies an internal AI writing assistant as minimal-risk, requiring only basic documentation of intended use, while classifying an AI-based candidate-screening tool as high-risk, requiring formal bias testing, documented human review of every flagged decision, and periodic performance audits — applying proportionate oversight rather than subjecting the writing assistant to the same heavy review as the hiring tool.

**Re-classification catching scope creep:** An AI system originally deployed for internal data summarization (minimal risk) is later repurposed by a business unit to draft customer-facing communications without a corresponding governance review. A periodic re-classification check catches this usage change and triggers the higher-tier review the new use case actually warrants.

## Common Mistakes

- **Applying the same governance process uniformly to all AI use cases regardless of risk** — this either bottlenecks legitimate low-risk adoption or under-scrutinizes genuinely high-stakes use cases.
- **Failing to maintain a current inventory of AI use cases across the organization** — governance requires visibility into what's actually being deployed, which tends to proliferate faster than centralized awareness without an active inventory process.
- **Leaving AI use cases without a specific, accountable owner** — an AI system with no assigned owner tends to have no one actively monitoring for drift, degradation, or inappropriate scope expansion.
- **Never re-classifying use cases as their actual usage evolves** — a system's risk profile can change substantially if its usage expands beyond its original intended scope, and static classification misses this.

## When NOT to Use

- For a very small organization with minimal or no genuine AI deployment — formal governance infrastructure should be proportionate to actual AI usage and risk exposure.
- As a substitute for the specific technical practices needed to build safe, fair AI systems — governance provides the oversight structure; it doesn't replace specific technical work like bias testing (see `audit-model-fairness`) or output validation.
- For research or experimental AI use with no path to production deployment or real-world decision impact — apply proportionately lighter oversight to genuinely exploratory work, reserving full governance rigor for use cases with actual deployment consequences.
