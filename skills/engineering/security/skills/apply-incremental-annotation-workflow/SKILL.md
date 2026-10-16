---
name: apply-incremental-annotation-workflow
description: Use when reverse engineering any non-trivial binary — rename functions and variables and add comments directly in the disassembler/decompiler's own database as understanding develops, rather than keeping separate notes, because the renamed database is itself a persistent, cumulative, binary-synchronized record of what's already been understood, and external notes drift out of sync with the binary as analysis progresses.
source: 'Chris Eagle, "The IDA Pro Book", No Starch Press, 2nd ed. (2011) — the IDA database (IDB) as the central, persistent analysis artifact'
tags: [reverse-engineering, static-analysis, documentation, workflow, security]
related: [apply-decompiler-assisted-triage, apply-known-library-identification]
---

# Apply Incremental Annotation Workflow

Rename functions and variables and add comments directly in the disassembler or decompiler's own database as understanding develops, rather than keeping separate notes, when reverse engineering any non-trivial binary — because the renamed database is itself a persistent, cumulative, binary-synchronized record of what's already been understood, and external notes drift out of sync with the binary as analysis progresses.

## Why This Is Best Practice

**Eagle, "The IDA Pro Book" (2011):** Establishes the IDA database (IDB) — and the equivalent project database in Ghidra and other modern tools — as the central artifact of a reverse-engineering effort, not a disposable working file. Renaming a function from `sub_401230` to `decrypt_config_blob` and adding a comment explaining the specific algorithm identified is a direct, location-anchored annotation that stays correct as long as the binary itself doesn't change — unlike a separate notes document, which requires the analyst to manually keep addresses and descriptions in sync by hand.

**Why best:** External notes ("function at 0x401230 seems to decrypt something") require the analyst to re-locate the referenced address every time the notes are consulted, and silently go stale if the analyst re-numbers or re-analyzes the binary. In-database annotation is addressed directly to the thing it describes — reopening the database later shows the renamed function and comment exactly where they apply, with no translation step required. This compounds across a long analysis: later-session productivity depends heavily on how well earlier sessions' understanding was captured in a form the tool itself preserves and surfaces automatically.

**Adopted by:** Standard practice in professional reverse-engineering workflow using IDA Pro, Ghidra, Binary Ninja, and similar tools, all of which are built around a persistent project database specifically to support this annotation-as-you-go model.
**Impact:** A well-annotated database turns a second analysis session (by the same analyst after a break, or by a different analyst entirely) from a cold restart into a continuation — renamed functions and comments immediately convey what's already understood, letting new effort concentrate on what remains unexplained rather than re-deriving prior findings.

## Steps

1. **Rename a function as soon as its purpose becomes reasonably clear**, even with a provisional name (`maybe_decrypt_config`) that can be refined later — don't wait for complete certainty before annotating at all.
2. **Rename variables to reflect their actual role** (`encrypted_buf`, `key_len`) rather than leaving decompiler-generated generic names (`v1`, `a2`) once their purpose is understood.
3. **Add a comment at the specific point where non-obvious logic occurs** — a comment explaining a particular algorithm, magic constant, or unusual control-flow choice, placed exactly where it applies.
4. **Use the tool's structure/type definitions for recovered data structures**, rather than only commenting about them, so the decompiler's type-aware rendering benefits from the structure too.
5. **Revisit and refine provisional names and comments as later analysis confirms or contradicts earlier hypotheses** — treat the annotation layer as a living document, not a one-time pass.
6. **Save/checkpoint the database regularly**, treating it as the primary analysis deliverable rather than a disposable scratch file.

## Rules

- Annotate in the tool's own database, not in a separate document — the database's persistent linkage between annotation and the exact code location is the specific advantage this workflow provides.
- Use provisional names and comments as soon as a reasonable hypothesis forms, rather than waiting for full certainty — the cost of revising a provisional name later is much lower than the cost of re-deriving unannotated analysis from scratch.
- Treat the annotated database as the primary deliverable of the analysis effort — a correct conclusion that exists only in the analyst's head or a disconnected notes file doesn't transfer to the next session or the next analyst.
- Refine annotations as understanding evolves — a provisional name that turns out to be wrong should be corrected, not left as stale, misleading documentation.

## Examples

**Effective incremental annotation:** An analyst renames a function `sub_401230` to `decrypt_config_blob` after identifying its general purpose, then later — after fully reverse engineering the specific algorithm — refines the comment to name the exact cipher and key-derivation method used, and renames the local variables accordingly. A colleague reopening the database weeks later immediately understands the function's role without re-analyzing it.

**Notes-drift failure mode (contrast case):** An analyst keeps a separate text file of findings ("0x401230 = decrypt function, uses XOR") while working in the disassembler. After the binary is re-analyzed with an updated tool version that shifts some addresses, the notes file's references no longer match the actual locations, and the analyst has to manually re-locate each referenced finding before the notes are useful again.

## Common Mistakes

- **Keeping findings in a separate notes document instead of the tool's database**, creating a synchronization burden that the database's own addressing would have avoided entirely.
- **Waiting for complete certainty before renaming anything**, leaving long stretches of the database unannotated even after a reasonable, if provisional, hypothesis has formed.
- **Not revisiting provisional names once later analysis contradicts them**, leaving misleading annotations that actively harm rather than help a later session.
- **Annotating function names but not variable names or type structures**, leaving the decompiler's output far less readable than full annotation would have made it.

## When NOT to Use

- For a very short, one-off analysis task where no second session or handoff is expected and the overhead of careful annotation exceeds its benefit for that single pass.
- When using a disassembler/decompiler without persistent-database support, where this specific in-tool annotation mechanism isn't available — an external, carefully-maintained notes system is the fallback in that case.
- When the analysis is purely automated (scripted bulk processing of many samples) with no human analyst building cumulative understanding of any individual binary — annotation specifically supports human comprehension over multiple sessions, which doesn't apply to a one-shot automated pass.
