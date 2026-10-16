---
name: apply-patch-diffing-technique
description: Use when a patched and an unpatched version of the same binary are both available — structurally diff the two (BinDiff-style function matching) to directly localize what changed, rather than re-analyzing either binary from scratch, because the specific functions that changed between versions are exactly where a fixed vulnerability (or a newly introduced feature) is located.
source: 'Halvar Flake (Thomas Dullien), "Structural Comparison of Executable Objects", DIMVA (2005) — the structural-diffing algorithm underlying BinDiff; Google/Zynamics BinDiff documentation'
tags: [reverse-engineering, patch-diffing, vulnerability-research, static-analysis, security]
related: [apply-decompiler-assisted-triage, apply-known-library-identification]
---

# Apply Patch-Diffing Technique

Structurally diff a patched and unpatched version of the same binary to directly localize what changed, rather than re-analyzing either binary from scratch, when both versions are available — because the specific functions that changed between versions are exactly where a fixed vulnerability, or a newly introduced feature, is located.

## Why This Is Best Practice

**Flake (Dullien), "Structural Comparison of Executable Objects" (DIMVA, 2005):** Introduced the structural-diffing algorithm — matching functions between two binary versions by their call graph and control-flow structure rather than by byte-for-byte comparison, which breaks under compiler recompilation even when the logic is unchanged — that underlies BinDiff and similar tools. This lets an analyst compare two versions of a large binary and get a ranked list of functions that actually changed, out of the much larger set that recompiled identically or near-identically.

**Why best:** When a vendor ships a security patch, the patch notes rarely specify exactly which function or code path was modified. Re-analyzing the entire patched binary from scratch to find the fix (and infer the vulnerability it addresses) wastes effort on the overwhelming majority of the binary that didn't change. Structural diffing instead directly surfaces the small set of changed functions, turning a full-binary analysis task into a targeted one.

**Adopted by:** Standard technique in vulnerability research and exploit development for analyzing vendor security patches (widely associated with "Patch Tuesday" 1-day vulnerability research against Microsoft's monthly security updates) and in malware-family tracking (diffing samples to identify what changed between variants).
**Impact:** Patch diffing is the standard method by which security researchers reconstruct the vulnerability a patch addresses when the vendor's advisory doesn't specify technical detail — turning the patch itself into the primary source of vulnerability information, often faster than independently rediscovering the bug through fresh analysis.

## Steps

1. **Obtain both the pre-patch and post-patch versions of the exact same binary** — version mismatches (different build, different architecture) degrade match quality significantly.
2. **Run a structural diffing tool (BinDiff or equivalent) to generate a function-matching report** between the two versions.
3. **Review the report's confidence-ranked list of changed functions**, prioritizing high-confidence matches with meaningful instruction-level differences over near-identical or low-confidence matches.
4. **Focus analysis specifically on the changed functions**, using the unchanged, matched functions as a reliable baseline for understanding call context and data flow around the change.
5. **Characterize the specific change** — an added bounds check, a changed comparison operator, a new validation call — as the basis for reconstructing what vulnerability the patch addresses.
6. **Cross-reference the changed function's location and behavior against the vendor's advisory** (if one exists) to confirm the diffing result matches the publicly described issue, or to add technical detail the advisory omitted.

## Rules

- Always compare the exact matching binary pair (same build target, same architecture) — diffing mismatched builds produces noisy, low-confidence results that obscure the actual patch content.
- Prioritize high-confidence, substantively-different function matches in the diffing report — low-confidence matches and purely cosmetic differences (compiler-introduced reordering) are not the patch content of interest.
- Use unchanged, matched functions as reliable context for understanding the changed function's surrounding call graph and data flow, rather than re-deriving that context from scratch.
- Treat the diffing result as the starting point for understanding the vulnerability, not the complete answer — confirm the security implication of the specific code change through further analysis.

## Examples

**Patch Tuesday vulnerability reconstruction:** A researcher obtains a vendor's pre-patch and post-patch DLL for a given month's security update, runs BinDiff, and finds a single function with a newly added bounds check immediately before a buffer copy operation that was previously unchecked — directly localizing the memory-safety vulnerability the patch addresses without needing to analyze the rest of the (much larger) unchanged binary.

**Malware-family variant tracking:** An analyst diffs two samples believed to be variants of the same malware family and finds the core logic is structurally near-identical except for one function containing an updated C2 domain list and a newly added string-obfuscation routine — confirming the variant relationship and precisely scoping what's different between them.

## Common Mistakes

- **Diffing mismatched binary builds** (different compiler version, different architecture, or an unrelated build), producing a noisy result where legitimate changes are buried in spurious differences.
- **Re-analyzing the entire patched binary from scratch instead of diffing against the prior version**, when the prior version was available and would have directly localized the change.
- **Treating low-confidence or cosmetic diff matches as significant**, chasing compiler-introduced reordering or renaming rather than the actual functional change.
- **Stopping at "this function changed" without characterizing the specific nature of the change** (what check was added, what logic was altered) needed to actually understand the vulnerability or feature the patch addresses.

## When NOT to Use

- When only one version of the binary is available (no prior, unpatched version to diff against) — this technique specifically requires a comparison pair; use `apply-static-before-dynamic-analysis` and standard static analysis instead.
- When the patch is known (from vendor documentation) to be a non-functional change (build metadata, signing certificate update) with no code-level difference — diffing adds no value in that case.
- For open-source software where the actual source-level diff (commit history, changelog) is directly available — source-level diffing is more precise and faster than binary structural diffing when source access exists.
