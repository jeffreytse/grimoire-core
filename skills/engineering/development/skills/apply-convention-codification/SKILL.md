---
name: apply-convention-codification
description: Use when you catch yourself writing the same code-review comment or instruction a second time, or notice a recurring correction on the same mistake — encode the rule as a lint rule, type constraint, CI check, or script instead of relying on a written note or memory to catch it next time.
source: 'Airbnb JavaScript Style Guide and eslint-config-airbnb (2012–present) — style-guide rules codified as enforced lint rules; Google Engineering Practices, "Code Review Guide" — style issues should be automated, not litigated in review'
tags: [tooling, code-quality, linting, developer-experience, consistency]
related: [apply-illegal-states-unrepresentable, propose-conventional-commit, design-contribution-standard]
---

# Apply Convention Codification

When you catch a recurring correction — the same review comment, the same mistake, the same instruction repeated — encode it as a lint rule, type constraint, CI check, or script instead of writing it down again as a note or reminder.

## Why This Is Best Practice

**Airbnb JavaScript Style Guide:** One of the most widely adopted style guides in the JavaScript ecosystem precisely because it ships as `eslint-config-airbnb` — an enforced, automatically-checked rule set — rather than as prose guidelines reviewers have to remember and apply by hand. The project's own history shows the guide evolving by converting recurring review disagreements into new lint rules rather than new paragraphs of prose.

**Google Engineering Practices, "Code Review Guide":** Explicitly separates style nits, which should be handled by an automated formatter or linter, from substantive review, which requires human judgment — on the stated reasoning that human reviewer attention is a scarce resource that re-litigating the same style point wastes, and that an automated check never forgets to flag it or applies it inconsistently.

**Why best:** A written instruction or review comment depends on every future reader remembering it and applying it correctly — a lint rule, type constraint, or CI check does not forget, does not tire, and catches the violation before it reaches review at all. Converting a recurring correction into structure moves the enforcement cost from "a human must remember and repeat this" to "a machine checks this every time," which is strictly more reliable once the rule is codified once.

**Adopted by:** Airbnb, Google, and the broader JavaScript/TypeScript ecosystem via shared, enforced lint configs; Google's internal code-review culture, which explicitly delegates style enforcement to tooling (`clang-format`, `gofmt`) so reviewers can focus on substance.
**Impact:** Airbnb's style guide, by shipping as an enforced config rather than prose, is one of the most-adopted JavaScript style configs in the ecosystem (millions of weekly npm downloads of `eslint-config-airbnb`) specifically because teams can adopt the enforcement, not just the recommendation, in one step — eliminating the need for every team's reviewers to independently learn and remember the same rules.

## Steps

1. **Notice the trigger**: you're about to write an instruction, leave a review comment, or give a correction that you recognize as a repeat of one you've given before.
2. **Ask whether the rule can be encoded structurally** — a lint rule, a type that makes the mistake impossible to construct, a CI check, or a script that flags or fixes the violation.
3. **If it can be encoded, encode it once** and remove the prose instruction — the structural check replaces the written reminder; don't keep both indefinitely.
4. **If it can't be encoded** (it requires judgment a machine can't apply), make the instruction more prominent and add a concrete example of the failure mode it's meant to prevent, rather than just restating the rule.
5. **Prefer the earliest-possible enforcement point**: a type error at compile time beats a lint warning, which beats a CI check, which beats a review comment, which beats a wiki page nobody reads.
6. **Treat a second occurrence of the same correction as the signal to stop writing more prose and start writing a check.**

## Rules

- The instruction is a symptom; if a structural fix exists, the structural fix is the whole answer, not an addition to more documentation.
- Encode the rule once a correction has recurred — don't wait for a third or fourth occurrence.
- When a rule can't be encoded because it genuinely requires judgment, invest in a sharper example of the failure mode rather than more abstract phrasing.
- Remove the superseded written instruction once its structural replacement is in place — a rule enforced by both a lint check and a stale wiki page invites drift between the two.

## Examples

**Review comment becomes a lint rule:** A reviewer flags "don't use `==`, use `===`" on three separate pull requests. The team adds `eqeqeq` to the shared ESLint config instead of leaving a fourth comment — the mistake is now caught before review.

**Judgment call stays an instruction, with an example added:** A recurring review note is "this error message doesn't tell the caller what to do differently." No lint rule can judge message quality, so the team's style guide keeps the instruction but adds a concrete before/after example of a vague versus actionable error message.

## Common Mistakes

- **Writing a third version of the same instruction** instead of converting it into a check after the second occurrence.
- **Encoding a rule as a lint check but leaving the old prose instruction in place**, so the two can drift out of sync over time.
- **Trying to force a judgment-dependent rule into a mechanical check**, producing false positives that erode trust in the linter.
- **Treating "add an example" as optional** when a rule genuinely can't be encoded — a restated abstract rule without a concrete failure-mode example is as easy to forget as the first version.

## When NOT to Use

- For a one-off correction with no sign it will recur — codifying every single comment into tooling has its own maintenance cost and isn't warranted until a pattern appears.
- When the team or project is too small or short-lived for the upfront tooling investment to pay back before the project ends.
