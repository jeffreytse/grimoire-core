---
name: refactor-ai-generated-code
description: Use when reviewing or cleaning up code that was substantially written by an AI coding assistant — check specifically for the recurring patterns AI assistants introduce (unnecessary comments, defensive checks and try/catch blocks abnormal for the surrounding trusted code, `any`-casts used only to silence the type checker, unneeded nesting) and remove them without changing behavior.
emerging: true
source: 'GitClear, "AI Copilot Code Quality" Research Report (2024) — four-year study of 211M changed lines showing a measurable rise in code duplication and churn correlated with AI-assisted authorship; Addy Osmani (Google Chrome engineering lead), "The 70% Problem: Hard Truths about AI-Assisted Coding" (2025)'
tags: [code-quality, ai-assisted-development, refactoring, code-review, maintainability]
related: [apply-ai-writing-tell-removal, review-code-style, apply-dry-principle]
---

# Refactor AI-Generated Code

Check code substantially written by an AI assistant for its recurring, recognizable smells — and remove them without changing behavior.

## Why This Is Best Practice

**Status:** Emerging — the specific failure modes of AI-generated code are documented with early empirical evidence from GitClear's large-scale analysis and named directly by senior engineers at Google (Osmani) and other AI-coding-tooling practitioners, but the practice of systematically auditing for them is new enough that it has not yet reached the years of majority top-tier adoption a stable practice requires. Review for promotion or deprecation by 2028.

**GitClear, "AI Copilot Code Quality" (2024):** An empirical study of 211 million changed lines across a large sample of commits found a measurable, continuing rise in duplicated code blocks and "churn" (code rewritten or deleted shortly after being added) correlating with the growth of AI-assisted coding tools — a data-backed signal that AI-generated code carries specific, recurring quality costs distinct from human-authored code.

**Osmani, "The 70% Problem" (2025):** Names the specific recurring patterns directly from production experience reviewing AI-assisted code at scale: excessive defensive programming and error handling around code paths that can't actually fail, redundant comments that restate what the code already says, and type-safety escape hatches (`any`-casts) used to silence the compiler rather than to model a real need — arguing these patterns accumulate as a distinct, recognizable class of technical debt specific to AI-authored code.

**Why best:** An AI assistant optimizes locally for "this change looks complete and safe," which systematically produces defensive ceremony, explanatory comments, and type-safety bypasses that a careful human author reviewing their own code would typically omit — because the assistant has no felt cost for the extra ceremony and a strong incentive to look thorough. Left unreviewed, these patterns compound: each file accumulates its own dialect of unnecessary guards and comments that make the codebase harder to read without making it more correct.

**Adopted by:** GitClear's report is based on repository data from a broad commercial sample and is widely cited in engineering-leadership discussion of AI-coding quality; Osmani's analysis is informed by code review at Google-scale and has been broadly circulated in senior-engineering discourse on AI-assisted development.
**Impact:** GitClear's four-year longitudinal data shows the duplication and churn trend specifically tracking the adoption curve of AI coding assistants, rather than remaining flat — the first large-scale empirical evidence that AI-generated code has a distinct, measurable quality signature that unreviewed code doesn't self-correct for.

## Steps

1. **Scope the check to the diff against the relevant base** — the PR's base branch, or the branch this one was cut from, or the repository's default branch — including uncommitted changes, rather than the whole file or codebase.
2. **Check for comments that add no information** — comments restating what the following line already says in code, rather than explaining a non-obvious why. Remove them.
3. **Check for defensive checks and try/catch blocks that are abnormal for the surrounding trusted code path** — error handling added around calls that can't actually fail in this context, or that duplicate a guarantee already enforced upstream. Remove them unless they guard a genuine boundary.
4. **Check for `any`-casts or other type-safety escape hatches used only to silence the type checker**, rather than to express a real, validated need. Replace with the correct type or a validated narrowing.
5. **Check for nesting that should be flattened with early returns or guard clauses**, and other structural patterns inconsistent with the surrounding file's own style.
6. **After editing, rerun the checks that verified the change** — tests, type check, lint — and revert any edit whose check fails. Keep behavior unchanged unless you're fixing a clear, separately-identified bug.

## Rules

- Scope the review to the actual diff, not the whole file or codebase, unless explicitly asked to audit more broadly.
- Remove only what's demonstrably unnecessary ceremony — a comment or guard that restates an existing guarantee, not one that documents a real constraint.
- Keep behavior unchanged; this is a refactor, not a logic change, unless a genuine bug is found and called out separately.
- Rerun verification after every edit and revert anything that breaks a check.

## Examples

**Removing redundant defensive code:** An AI-generated function wraps a call to an in-memory, type-checked helper in a try/catch that logs and returns a default value, even though the helper cannot throw given its actual signature and the surrounding code's invariants. The try/catch is removed; the call is left to propagate naturally since nothing upstream expects it to fail silently.

**Removing a silencing cast:** A function casts a parsed JSON value `as SpecificType` immediately after fetching it, with no validation. Replacing the cast with the codebase's existing schema-validation helper (which was already available and used elsewhere) surfaces malformed input as an explicit error instead of a false type guarantee.

## Common Mistakes

- **Removing a defensive check or comment that documents a real, non-obvious constraint**, mistaking necessary context for AI-style ceremony.
- **Reviewing the whole file instead of scoping to the diff**, mixing pre-existing code style into what should be a focused cleanup.
- **Treating the cleanup as license for a broader rewrite**, rather than minimal, behavior-preserving edits.
- **Skipping the re-verification step after editing**, risking a "simplification" that silently changes behavior.

## When NOT to Use

- On code that was not substantially AI-generated — the specific patterns this targets are characteristic of AI-assisted authorship, not a general code-smell checklist (use a general code-review or refactoring skill for human-authored code).
- When a defensive check or comment, though it looks like ceremony, documents a constraint that isn't obvious from the surrounding code — verify before removing, don't remove by pattern-match alone.
