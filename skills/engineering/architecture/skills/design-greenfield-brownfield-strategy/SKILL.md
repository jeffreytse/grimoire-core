---
name: design-greenfield-brownfield-strategy
description: Use when starting a new software project or major initiative — classifying it as greenfield (no existing system or constraints), brownfield (must integrate with or replace an existing system), or retrofit (upgrading an existing system in place) before choosing an architecture and rollout strategy.
source: Michael Feathers, "Working Effectively with Legacy Systems" (2004); Martin Fowler, "StranglerFigApplication" (martinfowler.com, 2004); standard enterprise-architecture and TOGAF project-classification treatment
tags: [project-classification, legacy-systems, migration-strategy, architecture-risk, rollout-strategy, technical-debt]
related: [apply-strangler-fig-pattern, apply-branch-by-abstraction, apply-chestertons-fence, write-adr]
---

# Design Greenfield/Brownfield Strategy

Classify a project as greenfield, brownfield, or retrofit before choosing an architecture or rollout approach — because each classification carries a different risk profile and rewards a different strategy, and applying the wrong one is a leading cause of failed migrations and needlessly slow new-builds.

## Why This Is Best Practice

**Adopted by:** Enterprise-architecture frameworks (TOGAF's project classification) and standard consulting/delivery practice distinguish greenfield, brownfield, and retrofit engagements as a first planning step because the risk profile, required due diligence, and viable architecture options differ fundamentally between them. Michael Feathers' "Working Effectively with Legacy Systems" (2004) formalized brownfield practice around characterization tests and seams; Martin Fowler's Strangler Fig write-up (2004) formalized the standard brownfield migration technique now used industry-wide (Shopify, Amazon, and most large-scale legacy modernizations document strangler-fig-style incremental migration rather than big-bang rewrites).

**Impact:** Industry post-mortems on failed "rewrite the legacy system" initiatives converge on a consistent root cause: the project was planned and resourced as if it were greenfield (fixed scope, clean architecture, straightforward timeline) when it was actually brownfield (unknown behavior to preserve, live data to migrate, users who cannot tolerate downtime). Joel Spolsky's widely-cited "things you should never do" analysis of full rewrites, and repeated case studies of multi-year "rewrite" projects that were eventually abandoned, both trace back to this same misclassification. Conversely, treating a genuine greenfield opportunity with brownfield-level caution (excessive upfront architecture, unnecessary compatibility constraints) measurably slows time-to-first-value without a corresponding risk reduction, since there is no existing behavior to protect.

**Why best:** The alternative — picking an architecture and rollout approach before establishing which of the three situations you're actually in — means the strategy is chosen independently of the risk it needs to manage. A brownfield migration strategy applied to a greenfield project adds unneeded process overhead; a greenfield strategy applied to a brownfield project systematically underestimates integration surface, data migration cost, and the blast radius of getting it wrong. Classifying first makes the strategy a function of the actual risk, not of habit or the most recent project's approach.

Sources: Feathers, "Working Effectively with Legacy Systems" (2004); Fowler, "StranglerFigApplication" (martinfowler.com, 2004); Spolsky, "Things You Should Never Do, Part I" (2000); TOGAF Architecture Development Method

## Steps

### Step 1: Determine whether a live system already exists

Ask: is there a system in production today, with real users, real data, and real integrations depending on it? If no — this is greenfield. If yes, proceed to Step 2. Do not classify based on whether the *code* is old — a live system with light usage is still brownfield; an unreleased rewrite of an old codebase with no live users yet is still greenfield.

### Step 2: Determine whether the new work must interoperate with or fully replace the existing system

If the existing system must keep running (in whole or in part) while the new work is built and rolled out — because full replacement in one step is infeasible, too risky, or would require unacceptable downtime — this is brownfield: the new work and the old system coexist for some period, with a defined boundary between them. If the intent is instead to modify the existing system in place, without introducing a separate replacement system running alongside it, this is retrofit: the same system is upgraded, but its identity, deployment, and continuity are preserved throughout.

### Step 3: Apply the classification's default strategy — do not carry over the wrong one

- **Greenfield:** Optimize for speed of learning and time-to-first-value. Defer architecture decisions that lack real usage data to justify them (see `apply-yagni-principle`); a wrong early architecture choice is cheap to change because nothing depends on it yet.
- **Brownfield:** Assess the integration surface first — what data, APIs, and behaviors the existing system exposes that the new work must honor or gradually take over. Choose a migration technique proportional to the system's criticality and the acceptable risk of a cutover: `apply-strangler-fig-pattern` for a live system that must keep serving traffic throughout, `apply-branch-by-abstraction` for large in-codebase changes that can't be delivered as one atomic change, or a scheduled cutover only when the system's criticality and blast radius are both low enough to tolerate it.
- **Retrofit:** Scope the exact boundary of what is being upgraded in place, and write characterization tests (per Feathers) to capture the existing behavior before changing it, so unintended behavior changes are caught rather than silently shipped. Plan an explicit rollback path for the in-place change before starting, since there is no separate "old system" left running to fall back to.

### Step 4: Verify the classification against the existing system's real constraints, not assumptions

Before committing to a strategy, confirm firsthand — not from secondhand description — what the existing system's actual data volume, uptime requirements, and undocumented behaviors are. A system assumed to be "brownfield but simple" often turns out to have significant undocumented dependents; verifying this before choosing a migration technique prevents discovering the real integration surface mid-migration, when it is most expensive to address.

### Step 5: Re-classify if the project's scope changes mid-flight

A project that starts as retrofit (in-place upgrade) sometimes needs to become brownfield (a parallel replacement system) once the in-place change proves too risky to do safely — and vice versa, a brownfield migration sometimes discovers the legacy system has few real dependents and can be safely retired outright. Re-run Steps 1–2 when scope materially changes rather than continuing to execute the original strategy on a project that has quietly become a different kind of project.

## Rules

- Never plan a brownfield project on a greenfield timeline — integration surface discovery, data migration, and compatibility work are brownfield-specific costs that a greenfield estimate does not account for.
- Never big-bang replace a system whose criticality or blast radius hasn't been explicitly assessed — default to an incremental technique (strangler fig, branch-by-abstraction) unless the risk assessment specifically justifies a scheduled cutover.
- Write characterization tests before modifying an existing system's behavior in a retrofit — without them, there is no way to distinguish an intentional improvement from an accidental regression.
- Re-run the classification when scope changes — a project's risk profile is a function of its current shape, not its shape at kickoff.

## Examples

**Genuine greenfield:** A team builds a new internal analytics dashboard with no existing system, no prior users, and no data migration required. They intentionally defer choosing a long-term data architecture until real usage patterns emerge, ship a minimal version in weeks, and iterate — appropriately treating the low-risk, no-dependents situation as greenfield rather than over-engineering for hypothetical future scale.

**Brownfield handled correctly:** A company needs to replace a 10-year-old monolithic order-processing system that still handles all live orders. Rather than a full rewrite, they apply `apply-strangler-fig-pattern`: new order types are routed to the new system first, while the old system continues handling existing order types, with the boundary between them shrinking over 18 months until the legacy system is fully retired. Data migration and integration surface are assessed explicitly before any cutover.

**Brownfield misclassified as greenfield (failure case):** A team plans a "from-scratch rewrite" of a legacy CRM, estimating the timeline as if building a new product, without accounting for the CRM's undocumented integrations, years of accumulated data-quality quirks, and users who cannot tolerate a feature regression. The rewrite runs years over its greenfield-based estimate and is eventually abandoned in favor of an incremental strangler-fig approach — the classic failure mode this skill exists to prevent.

**Retrofit:** A team upgrades an existing payment-processing service's encryption library in place to meet a new compliance requirement, without changing its external API or introducing a parallel system. They write characterization tests capturing every current transaction code path before touching the encryption code, make the change, and verify behavior is unchanged — then have a tested rollback path ready in case the upgrade introduces a regression.

## When NOT to Use

- For trivial or prototype work with no real users or stakes — the classification overhead isn't worth it when the answer is obviously greenfield and uncontested.
- When the classification is already explicit and undisputed in the project's charter — re-deriving it from scratch adds no value if everyone already agrees on the situation.
- When the actual need is a specific migration *technique* rather than the upstream classification decision — go directly to `apply-strangler-fig-pattern` or `apply-branch-by-abstraction` if the project is already confirmed brownfield and the only open question is execution mechanics.
