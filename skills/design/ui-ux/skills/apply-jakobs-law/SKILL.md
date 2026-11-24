---
name: apply-jakobs-law
description: Use when designing or reviewing a layout, navigation, or interaction that departs from how comparable products or the platform already work — or when a team proposes a "novel" pattern for a common task like login, cart, search, or settings.
source: Jakob Nielsen, "Jakob's Law of Internet User Experience" (Nielsen Norman Group, 2000); ISO 9241-110:2020 (conformity with user expectations); Roth et al. (2010) "Mental models for web objects" IJHCS; Tuch et al. (2012) "The role of visual complexity and prototypicality regarding first impression of websites" IJHCS
tags: [jakobs-law, design-conventions, mental-models, consistency, platform-guidelines, learnability, novel-patterns]
---

# Apply Jakob's Law

Users spend most of their time on other products, so they expect yours to work the same way — reuse established conventions for common tasks and reserve novelty for where it creates real value.

## Why This Is Best Practice

**Adopted by:** Apple HIG and Material Design (platform conventions are the explicit default), ISO 9241-110 (ergonomic principle "conformity with user expectations"), Nielsen's 10 usability heuristics (#4 "Consistency and standards"), Baymard Institute e-commerce guidelines, GOV.UK Design System ("use established patterns").
**Impact:** Roth et al. (2010) showed users hold strong, shared location expectations for web objects (logo top-left, search top-right, login top-right) and find them faster when placed there. Tuch et al. (2012) found sites with low prototypicality (unconventional layout) were rated less attractive within 17–50 ms of exposure. NN/g usability studies repeatedly identify "violates conventions" as a leading cause of task failure in heuristic evaluations.
**Why best:** The alternative — designing each interaction from first principles — forces users to learn a new model for something they already know how to do, raising error rates and abandonment. Conventions transfer learned skill for free.

Sources: nngroup.com (Jakob's Law); ISO 9241-110:2020; Roth et al. (2010); Tuch et al. (2012)

## Steps

### 1. Identify the pattern category

For the screen or flow under design, list each common task it contains: navigation, search, login, cart/checkout, settings, filters, forms, data tables, file upload, sharing.

Common tasks → **convention first**. Truly unique product value → room for novelty.

### 2. Collect the established convention

For each common task:
1. Check the platform guideline (Apple HIG, Material, Windows Fluent, WCAG for web semantics).
2. Survey 5–10 products your users use most (direct competitors + top general apps in the category).
3. Record where the element is placed, what it looks like, what it is called, and how it behaves.

| Element | Convention | Source |
|---------|-----------|--------|
| Logo | Top-left, links to home | Roth et al. 2010, NN/g |
| Search | Top / top-right, magnifier icon, Enter submits | NN/g |
| Cart | Top-right icon with item count | Baymard |
| Account/login | Top-right | Roth et al. 2010 |
| Primary nav (mobile app) | Bottom tab bar (iOS), navigation bar (Android) | HIG, Material |
| Links | Distinguishable color + underline in body text | WCAG 1.4.1, NN/g |

### 3. Compare your design against the convention

For each deviation, answer:
- What measurable benefit does the deviation give users (not the brand)?
- What will users who expect the convention do wrong?
- Is the benefit larger than the learning cost for first-time and infrequent users?

If you cannot answer the first question with evidence, revert to the convention.

### 4. When you must innovate, bridge from the familiar

- Keep familiar affordances (icons, labels, placement) while changing behavior underneath.
- Offer the old way alongside the new one during transition (e.g., keep classic search while adding AI search).
- Add just-in-time onboarding at the point of use, not a front-loaded tour (see `design-onboarding-flow`).
- When redesigning your own product, remember your existing users' conventions are *your* product — migrate gradually and allow temporary opt-out.

### 5. Validate

- Run a first-click test: ≥80% of participants should click the correct element for each common task.
- Include conventions explicitly in `run-heuristic-evaluation` (heuristic #4).
- Track error and abandonment metrics before/after any deviation ships.

## Rules

- Common tasks follow platform and industry conventions unless a test proves the deviation better.
- Follow the host platform's conventions over cross-platform consistency for system-level interactions (back navigation, share sheets, date pickers).
- Internal consistency is required too: the same action looks and behaves the same everywhere in the product.
- Never redesign a familiar control purely for visual differentiation.

## Common Mistakes

- **Novelty for branding:** hamburger icons that aren't hamburgers, custom scrollbars, hidden navigation behind gestures.
- **Copying one competitor** instead of the majority convention — check several.
- **Ignoring your own users' conventions** during a redesign — a big-bang change breaks power users' habits.
- **Applying web conventions inside native apps** (or vice versa).
- **Treating convention as an excuse** for a pattern that fails accessibility — conventions must still meet WCAG.

## When NOT to Use

- Genuinely new interaction categories with no established convention — use `run-usability-test` to develop one.
- Games and expressive/artistic experiences where discovery is part of the value.
- When the prevailing convention is a known dark pattern (see `prevent-dark-patterns`) — break it.
