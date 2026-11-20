---
name: apply-product-simplicity
description: Use when a product, UX, or feature-scope tradeoff comes up — choose fewer, more polished features and user delight over implementation convenience or feature count, and require every feature, control, and option to justify its place in the core experience.
source: 'Apple Human Interface Guidelines — clarity and deference principles; Walter Isaacson, "Steve Jobs", Simon & Schuster (2011) — product simplicity discipline, verified by the iPhone becoming the highest-revenue consumer product in history'
tags: [product-design, ux, feature-prioritization, simplicity, user-experience]
related: [apply-jobs-to-be-done, design-information-architecture-product, apply-yagni-principle]
---

# Apply Product Simplicity

When implementation convenience conflicts with user delight, choose delight — and require every feature, control, and option to earn its place rather than defaulting to including it.

## Why This Is Best Practice

**Apple Human Interface Guidelines:** Apple's official, published design standard states clarity and deference as core principles — the interface should recede in favor of content and task, and every element must justify the attention it demands from the user. This is not a stylistic preference but Apple's formal, institutionally-maintained design doctrine applied across its entire product line.

**Isaacson, "Steve Jobs" (2011):** Documents Jobs's product discipline as a repeated, verifiable pattern at Apple: ruthlessly cutting features and options in favor of a smaller set executed to a high polish, famously demonstrated by the original iPhone's decision to ship without a physical keyboard, replaceable battery, or expansion slot — choices that traded convenience and feature-count for a simpler, more polished core experience. This qualifies as a visionary-practitioner practice: Jobs's outsized, verifiable outcome (the iPhone became the highest-revenue consumer product in history) backs a specific, actionable method, not an abstract philosophy.

**Why best:** Feature count and implementation convenience are proxies that are easy to optimize for and easy to measure internally, but they are not what the user experiences — a user experiences the quality of the small set of things they actually touch. Prioritizing fewer, more polished features over more, rougher ones directly targets the dimension the user actually perceives, at the cost of metrics (feature count, backlog velocity) that don't reflect it.

**Adopted by:** Apple's Human Interface Guidelines, applied across macOS, iOS, watchOS, and visionOS design review; Jobs's product-simplicity discipline at Apple, with the iPhone and iPod as the most commercially verified instances.
**Impact:** The iPhone, built on exactly this discipline (fewer hardware features, higher polish on each), became the best-selling and highest-revenue consumer electronics product in history — a directly verifiable outcome tied to the specific decision to cut features rather than add them.

## Steps

1. **For every feature, control, or option under consideration, require an explicit justification** for its place in the product — "it's possible to build" or "a competitor has it" is not sufficient justification on its own.
2. **Default to shipping fewer features at higher polish** over more features at lower polish — a product with three well-executed capabilities beats one with ten rough ones.
3. **Prototype cheaply before committing** — design and UX decisions that depend on feel are far cheaper to iterate in throwaway mockups than in production code; build 2–3 competing options for a genuinely novel interaction and compare them directly rather than committing to the first idea.
4. **Get the details right on what you do ship**: transitions, alignment, spacing, feedback states, and error states — these are where "polish" is actually perceived, not in feature count.
5. **Tighten the core loop**: every feature should serve the product's central workflow directly, or be cut; features that are merely adjacent to the core loop dilute it.
6. **Identify who "the user" is for the specific surface in question** — the end user for a UI, the integrating engineer for a library or internal API, the future maintainer for the code itself — and weigh their experience explicitly, from their perspective, not a generic one.

## Rules

- Every feature, control, and option must be justified against the core experience, not included by default.
- Choose fewer, more polished features over more, rougher ones when the two trade off against each other.
- Prototype cheaply when a decision depends on feel rather than logic, before committing to production implementation.
- Treat transitions, spacing, feedback, and error states as first-class parts of "the feature," not afterthought polish.

## Examples

**Feature cut for polish:** A team debates adding a fourth, rarely-requested export format alongside three well-supported ones. Rather than adding it at the same polish level as the existing three (which would stretch QA and support thin), the team ships only the three, each hardened with clear error states and fast performance.

**Prototype before commit:** A novel drag-and-drop interaction has no precedent in the existing product. The team builds three disposable HTML prototypes exploring different feels before writing any production code, and picks the one that tested best for actual user comprehension — not the one that was fastest to prototype.

## Common Mistakes

- **Including a feature because it's technically easy to build**, without asking whether it earns its place in the user's experience of the product.
- **Shipping many features at uniform, mediocre polish** instead of fewer features executed well — optimizing for breadth of a feature list rather than depth of experience.
- **Committing to a production implementation of a feel-dependent design decision** without first comparing cheap, disposable prototypes.
- **Treating "the user" as only the end customer**, while ignoring the experience of the engineer who has to integrate a library or maintain the code later.

## When NOT to Use

- For infrastructure, internal tooling, or compliance-mandated features where the relevant "experience" criterion is correctness or auditability, not delight — apply judgment on which quality dimension actually matters for that surface.
- In an extremely early-stage prototype meant purely to validate a hypothesis quickly, where investing in polish before the hypothesis is validated would waste the exploration budget.
