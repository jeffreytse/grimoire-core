---
name: apply-toil-elimination
description: Use when facing non-trivial manual work that will recur — edits, migrations, analyses, checks — even if it won't repeat many times; build the tool that does it or proves it (a script, codemod, generator, or rerunnable check) instead of doing it by hand, with the tool itself as the artifact a reviewer can rerun.
source: 'Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.), "Site Reliability Engineering", Google / O''Reilly (2016), Ch. 5 "Eliminating Toil"'
tags: [toil-elimination, automation, sre, developer-productivity, tooling]
related: [apply-twelve-factor-app, apply-idempotent-operations, apply-dry-principle]
---

# Apply Toil Elimination

When facing non-trivial manual work, build the tool that does it or proves it instead of doing it by hand — the tool, not the completed task, is the artifact a reviewer can rerun and trust.

## Why This Is Best Practice

**Google SRE Book, Ch. 5:** Defines toil as work that is manual, repetitive, automatable, tactical, and that scales linearly with service growth rather than providing enduring value — and sets an explicit organizational policy capping SRE time spent on toil at 50%, with the rest reserved for engineering that reduces future toil. The chapter's central claim: toil that isn't automated doesn't stay constant, it grows with the system, eventually consuming all available engineering time.

**Why best:** Manual, repeatable work has a hidden second cost beyond the time it takes once: it has to be redone correctly every time it recurs, by whoever does it, with no artifact proving it was done right. A script, codemod, or generator pays a fixed cost once and then is provably reproducible — a reviewer can rerun it and get the same, auditable result, which hand-done work cannot offer regardless of how carefully it was performed.

**Adopted by:** Formal toil-tracking and toil-reduction targets are standard SRE practice at Google and widely adopted across the industry following the SRE book's publication (Dropbox, Evernote, and numerous enterprises publish their own toil-budget policies modeled on it); "automate anything you do more than twice" is longstanding practice in DevOps and platform engineering generally.
**Impact:** Google reports that SRE teams which actively track and cap toil free measurable engineering capacity for reliability work that reduces future incidents, compared to teams whose time is consumed by recurring manual operations — the explicit 50% toil cap exists because, left unmanaged, toil consumes a growing share of available time as a service scales.

## Steps

1. **Judge the task by triviality, not repetition.** A single complex migration, analysis, or check deserves a tool just as much as a task repeated weekly — the bar is "is this non-trivial to do correctly," not "will I do this again."
2. **Do the first unit by hand** to learn the actual shape of the problem, then build the tool and prove it by rerunning it on that same unit to confirm it reproduces the correct result.
3. **Make the tool safe to rerun** — idempotent, side-effect-aware, and loud about what it changed — so a reviewer or a future you can run it again without fear.
4. **Prefer a deterministic tool over fanning the work out to multiple people or multiple agents.** When fan-out is unavoidable, write the recipe, the verification contract, and the fences as one script or skill the delegates follow and cannot silently deviate from.
5. **Build the smallest tool that does or proves the job** — a script, not a framework; a focused codemod, not a general-purpose refactoring engine.
6. **Commit the tool when the work it does outlives the current task.** A script, codemod, generator, or check with no artifact left in the repository means the work wasn't actually automated — it was done once by hand and will have to be redone by hand again.

## Rules

- Skip building a tool only for a couple of genuinely trivial, one-off edits — the default for anything else is to build it.
- Prove the tool on the first unit before trusting it on the rest.
- A tool must be safe to rerun; if rerunning it could cause harm, that's a defect in the tool, not an acceptable constraint on using it.
- Commit the tool alongside the work it produced when that work could plausibly need to be redone, audited, or reapplied.

## Examples

**Codemod over hand-editing:** A rename affects 40 call sites across a codebase with subtly different argument orders at each site. Instead of editing each by hand, the engineer writes a small codemod, runs it on one file, verifies the diff is correct, then runs it on the rest — leaving the codemod in the repository's `scripts/` directory for the next similar rename.

**Reusable check over a one-time manual audit:** Verifying that every API endpoint has a corresponding rate limit is a one-time ask, but the engineer writes it as a script that lists endpoints lacking a limit, rather than manually cross-referencing a spreadsheet — so the same check can run again after the next endpoint is added.

## Common Mistakes

- **Deciding not to automate because "it's only once"** without checking whether the task is non-trivial — triviality, not repetition, is the actual bar.
- **Building the tool but not proving it on a real unit first**, then discovering on a wide rollout that it was wrong the whole time.
- **Fanning complex work out to several people or agents with instructions only in prose**, instead of writing the recipe and verification contract as a script or skill they must follow.
- **Leaving no artifact in the repository** — the task got done, but the next person who needs to do it again starts from zero.

## When NOT to Use

- For genuinely trivial, one-off edits — a couple of obvious, low-risk changes don't justify the overhead of a tool.
- When building the tool would cost meaningfully more than the total cost of doing the work by hand every time it will realistically recur, including the audit and correctness cost — a judgment call to make explicitly, not to default past.
