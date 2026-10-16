---
name: apply-decompiler-assisted-triage
description: Use when analyzing a function or module in a disassembler — read the decompiler's pseudocode output first to build a fast high-level understanding of the logic, and drop down to raw disassembly only for the specific instructions the decompiler renders unreliably (obfuscated, hand-optimized, or non-standard-calling-convention code), rather than reading every instruction of the raw disassembly line by line.
source: 'Chris Eagle, "The IDA Pro Book", No Starch Press, 2nd ed. (2011); Ghidra documentation, National Security Agency (public release 2019) — decompiler-first triage workflow'
tags: [reverse-engineering, decompiler, static-analysis, security, binary-analysis]
related: [apply-static-before-dynamic-analysis, apply-incremental-annotation-workflow, apply-known-library-identification]
---

# Apply Decompiler-Assisted Triage

Read a decompiler's pseudocode output first to build a fast high-level understanding of a function's logic, and drop down to raw disassembly only for the specific instructions the decompiler renders unreliably, rather than reading every instruction of the raw disassembly line by line.

## Why This Is Best Practice

**Eagle, "The IDA Pro Book" (2011):** Documents the shift in professional reverse-engineering workflow once mature decompilers (Hex-Rays, and later Ghidra) became available — pseudocode output, while imperfect, compresses dozens of assembly instructions into a handful of C-like statements that convey the same control flow and data operations far faster than reading raw disassembly line by line.

**Ghidra documentation (NSA, 2019):** Ghidra's public release and documentation establish the same decompiler-first workflow as standard practice in a widely-adopted, free tool — the decompiler view is treated as the primary analysis surface, with the listing (raw disassembly) view used specifically to resolve ambiguities the decompiler flags or handles incorrectly.

**Why best:** Raw disassembly reading doesn't scale — a function with a few hundred instructions can take many times longer to read as assembly than as decompiler-generated pseudocode conveying the same logic. The decompiler is not perfectly reliable (it can mis-render hand-optimized code, non-standard calling conventions, or code employing anti-decompilation tricks), but the efficient workflow is to read pseudocode first and fall back to disassembly specifically where the decompiler's output looks suspicious or doesn't type-check, not to distrust it uniformly from the start.

**Adopted by:** Standard workflow in modern reverse-engineering practice using Hex-Rays (IDA Pro) or Ghidra, both of which structure their UI around a side-by-side pseudocode/disassembly view specifically to support this triage pattern.
**Impact:** Decompiler-assisted triage is the primary reason modern reverse engineers can process unfamiliar codebases at a pace that raw-disassembly-only analysis (the standard before mature decompilers existed) could not match — entire functions can often be understood in the time it previously took to read their prologue.

## Steps

1. **Open the decompiler's pseudocode view for the function being analyzed, not the raw disassembly listing, as the default starting point.**
2. **Read the pseudocode for overall control flow and data operations** — branches, loop structure, function calls, and the general shape of what the function does.
3. **Watch for specific decompiler failure signatures**: type confusion, variables that don't type-check sensibly, control flow that looks structurally impossible, or a function the decompiler flags as having failed to fully decompile.
4. **Drop down to raw disassembly specifically for the flagged region**, not the whole function, when the pseudocode looks unreliable.
5. **Cross-check register and stack usage in the disassembly against what the pseudocode implied**, to resolve the specific discrepancy, then return to pseudocode-level reading for the rest of the function.
6. **Annotate the pseudocode (rename variables, add comments) as understanding develops**, rather than keeping notes separately (see `apply-incremental-annotation-workflow`).

## Rules

- Default to pseudocode as the primary reading surface; treat the disassembly listing as a resolution tool for specific ambiguities, not a parallel full read-through.
- Watch specifically for the decompiler's own failure signatures (type confusion, flagged decompilation failures, structurally implausible control flow) as the trigger to drop to disassembly, rather than distrusting the decompiler uniformly.
- Hand-optimized code, non-standard calling conventions, and deliberate anti-decompilation tricks are the main categories where decompiler output becomes unreliable — expect more disassembly fallback in code exhibiting these properties.
- Don't skip raw disassembly entirely — some logic (certain bitwise tricks, specific instruction-level timing or side-channel behavior) is only visible at the assembly level regardless of decompiler quality.

## Examples

**Efficient triage:** An analyst opens a 200-instruction function's pseudocode view and reads a dozen lines of clean, type-sensible C-like code describing a buffer copy with a length check — confirming the function's purpose in under a minute, with no need to read the full disassembly.

**Decompiler fallback:** An analyst reading pseudocode for a different function notices a variable the decompiler labels as an integer being used in a way that doesn't make sense (implying it's actually a packed structure). They drop to the raw disassembly for that specific instruction range, identify the actual bit-packing the decompiler mis-rendered, then return to pseudocode-level reading for the rest of the function with the correct interpretation in hand.

## Common Mistakes

- **Reading the full raw disassembly for every function out of general distrust of the decompiler**, losing most of the speed benefit the tool provides.
- **Trusting decompiler output uncritically even when it shows a clear failure signature** (type confusion, a flagged decompilation error), producing an incorrect understanding of the function's actual behavior.
- **Dropping to disassembly for the entire function instead of just the ambiguous region**, spending more time than the specific discrepancy warranted.
- **Not annotating the pseudocode as understanding develops**, losing the cumulative benefit of the analysis for later review or for other analysts.

## When NOT to Use

- When no decompiler is available for the target architecture (some embedded or uncommon architectures have limited decompiler support) — raw disassembly reading is the only option in that case.
- For code specifically designed to defeat decompilation (certain obfuscators deliberately target decompiler weaknesses) — in that case, raw disassembly or manual de-obfuscation is required as the primary technique, not a fallback.
- For very short functions (a few instructions) where reading the raw disassembly directly is already fast enough that the decompiler adds no meaningful speed benefit.
