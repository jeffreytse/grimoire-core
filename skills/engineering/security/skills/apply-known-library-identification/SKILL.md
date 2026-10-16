---
name: apply-known-library-identification
description: Use when beginning analysis of a binary that statically links third-party or standard-library code — run signature-based library identification (FLIRT, Ghidra Version Tracking/FunctionID) first and label matched functions as known, before manually analyzing anything, so analysis effort concentrates on the binary's custom logic instead of re-deriving the behavior of well-documented library code that was simply compiled in.
source: 'FLIRT (Fast Library Identification and Recognition Technology), Ilfak Guilfanov/Hex-Rays, documented in Chris Eagle, "The IDA Pro Book", No Starch Press, 2nd ed. (2011); Ghidra Version Tracking and FunctionID features, National Security Agency (public release 2019)'
tags: [reverse-engineering, static-analysis, signature-matching, security, binary-analysis]
related: [apply-decompiler-assisted-triage, apply-static-before-dynamic-analysis]
---

# Apply Known-Library Identification

Run signature-based library identification first and label matched functions as known, before manually analyzing anything, when beginning analysis of a binary that statically links third-party or standard-library code — so analysis effort concentrates on the binary's custom logic instead of re-deriving the behavior of well-documented library code that was simply compiled in.

## Why This Is Best Practice

**FLIRT, documented in Eagle's "The IDA Pro Book" (2011):** FLIRT signatures let a disassembler recognize statically-linked standard-library and common third-party-library functions by their compiled byte patterns, automatically labeling them with their real names (`malloc`, `strcpy`, a specific compression library's internals) rather than leaving them as anonymous, unlabeled code the analyst would otherwise have to manually identify or re-derive from scratch.

**Ghidra Version Tracking / FunctionID (NSA, 2019):** Ghidra's equivalent feature set performs the same function-matching against reference libraries, establishing this as a standard capability across the two dominant modern disassembly/decompilation platforms, not a niche or tool-specific technique.

**Why best:** A statically-linked binary often contains far more library code (compression, networking, cryptography, standard C runtime) than custom logic by instruction count. Without library identification, an analyst wastes significant time manually analyzing well-known, already-documented library internals that contribute nothing to understanding what the binary itself was specifically built to do — the custom logic is frequently a small fraction of the total code, and finding it quickly depends on first ruling out everything that's already known.

**Adopted by:** Standard first step in professional reverse-engineering workflow using IDA Pro or Ghidra; signature databases for common compilers, standard libraries, and popular third-party libraries are maintained and distributed specifically to support this step.
**Impact:** Library identification routinely resolves a large share of a statically-linked binary's functions automatically, reducing the actual manual-analysis surface to the binary's custom logic — turning what would otherwise be a full-binary analysis effort into a targeted one.

## Steps

1. **Run signature-based library matching (FLIRT in IDA Pro, Version Tracking/FunctionID in Ghidra) as one of the first steps after loading the binary**, before manual function-by-function analysis begins.
2. **Review and apply the matched library signatures**, accepting high-confidence matches and flagging low-confidence or partial matches for manual confirmation rather than blind acceptance.
3. **If a relevant library signature database doesn't already exist** (a less common third-party library, a custom-built static library used elsewhere), consider generating one from a known-good copy of the library if the same library is likely to recur across future analysis targets.
4. **Use the now-labeled library functions as landmarks** to orient navigation through the binary — custom logic is often identifiable by what library functions it calls and in what sequence.
5. **Concentrate manual analysis effort specifically on the unmatched, unlabeled functions** — these are the binary's actual custom logic and the primary analysis target.
6. **Re-run signature matching after any unpacking step** (see `apply-unpacking-before-analysis`) — signatures generally only match against the unpacked, as-compiled code, not a packed wrapper.

## Rules

- Run library identification before manual function analysis begins, not as an afterthought once significant manual effort has already been spent.
- Treat low-confidence signature matches as flags for manual confirmation, not as settled — a false match mislabeling custom logic as library code would cause an analyst to skip over exactly the code that mattered.
- Concentrate manual analysis on unmatched functions — re-analyzing a correctly-matched standard library function from scratch is wasted effort regardless of how thorough the resulting analysis is.
- Re-run identification after unpacking — signature matching against a packed binary's wrapper will fail to match anything meaningful.

## Examples

**Efficient use:** An analyst loads a statically-linked binary, runs FLIRT signature matching, and finds that roughly 60% of the binary's functions are immediately labeled as standard C runtime and a known compression library. They focus remaining analysis time entirely on the unmatched 40%, which turns out to contain the binary's actual custom networking and persistence logic.

**Skipped-identification failure mode (contrast case):** An analyst skips library identification and manually analyzes a function for an hour, concluding it implements a custom hashing algorithm — only to later discover, after finally applying signature matching, that the function was an unmodified standard-library hash implementation that had already been identified and documented publicly years earlier.

## Common Mistakes

- **Skipping library identification and manually analyzing every function from scratch**, including well-documented standard-library and third-party-library code that didn't need re-analysis.
- **Blindly accepting low-confidence signature matches** without manual confirmation, risking mislabeling custom logic as library code and overlooking it entirely.
- **Running signature matching before unpacking a packed binary**, producing no useful matches and incorrectly concluding the binary contains no recognizable library code.
- **Not maintaining or updating signature databases for libraries commonly seen in a given analysis domain**, repeatedly re-deriving the same library's behavior across multiple unrelated analysis targets.

## When NOT to Use

- For small, purpose-built binaries with no significant statically-linked library code (common in embedded or minimal-runtime targets) — identification has little to match against and adds no analytical value.
- When analyzing dynamically-linked code where the library functions are already resolved and named by the loader/symbol table — identification specifically addresses statically-linked, unlabeled library code.
- When the analysis goal is specifically to audit the library code itself for vulnerabilities (rather than the custom logic built on top of it) — in that case, the library code is the actual target, not something to skip past.
