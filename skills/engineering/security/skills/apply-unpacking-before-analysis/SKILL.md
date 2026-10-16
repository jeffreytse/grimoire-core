---
name: apply-unpacking-before-analysis
description: Use when a binary's strings, imports, and disassembly look sparse, garbled, or unusually small relative to its file size — identify the packer and unpack or dump the binary at its original entry point before attempting further static analysis, because analyzing a packed binary directly only reveals the packer's unpacking stub, not the actual payload's logic.
source: 'Michael Sikorski & Andrew Honig, "Practical Malware Analysis", No Starch Press (2012), Ch. 18 "Packing and Unpacking" — the dump-at-original-entry-point methodology; PEiD/Detect It Easy packer-signature identification tools'
tags: [reverse-engineering, malware-analysis, unpacking, static-analysis, security]
related: [apply-static-before-dynamic-analysis, apply-decompiler-assisted-triage]
---

# Apply Unpacking Before Analysis

Identify the packer and unpack or dump the binary at its original entry point before attempting further static analysis, when a binary's strings, imports, and disassembly look sparse, garbled, or unusually small relative to its file size — because analyzing a packed binary directly only reveals the packer's unpacking stub, not the actual payload's logic.

## Why This Is Best Practice

**Sikorski & Honig, "Practical Malware Analysis" (2012), Ch. 18:** Establishes packing detection and the dump-at-original-entry-point (OEP) technique as a required step before static analysis can proceed meaningfully on a packed sample — a packer compresses or encrypts the actual payload and wraps it in a small unpacking stub that only decompresses the real code into memory at runtime, so disassembling the file as stored on disk shows only the stub's generic unpacking logic, not the payload's actual behavior.

**PEiD / Detect It Easy methodology:** Packer-signature databases and entropy analysis are the standard first checks for identifying whether, and with what tool, a binary has been packed — high file entropy, a tiny import table, and a disassembly that resolves to a short, generic loop are the characteristic signature of a packed sample, distinguishable from genuinely small or simple software.

**Why best:** Investing static-analysis effort (string review, import analysis, manual disassembly reading) on a packed binary before unpacking wastes that effort entirely — none of it reflects the payload the analyst actually needs to understand. Unpacking first, even though it adds an upfront step, is what makes every subsequent static-analysis technique actually productive.

**Adopted by:** Standard step in professional malware-analysis workflows and SANS FOR610 curriculum; built into automated sandboxes (which frequently memory-dump a process post-unpacking as part of their standard pipeline) and semi-automated tools.
**Impact:** Memory-dumping a packed sample at its original entry point routinely converts a disassembly of meaningless stub logic into a fully analyzable payload with readable strings and a normal-looking import table — the difference between "nothing useful learned" and "full static analysis possible" for a large share of commodity malware, which is commonly packed specifically to defeat static analysis and signature-based detection.

## Steps

1. **Check entropy and import-table size as the first signal of packing** — high entropy (near-random byte distribution) combined with a tiny import table (often just enough to load a library and resolve the rest of the imports dynamically) is the characteristic packed-binary profile.
2. **Identify the specific packer if possible** using a signature database (PEiD, Detect It Easy) — knowing the specific packer often means a known, documented unpacking method already exists.
3. **Run the sample under a debugger and set a breakpoint strategy to catch the transition to the original entry point** (common techniques: breaking on memory writes to newly-allocated executable regions, or on the specific API calls a known packer uses to transfer control).
4. **Dump the process memory at the original entry point**, once reached, rather than analyzing the on-disk file.
5. **Fix up the dumped image's import table** (many dumping tools require this separately) so the dumped binary loads and disassembles correctly in a disassembler/decompiler.
6. **Proceed with static analysis on the unpacked dump**, not the original packed file — re-run string extraction, import review, and disassembly against the unpacked version.

## Rules

- Don't invest significant static-analysis effort on a binary exhibiting packed-binary signatures (high entropy, tiny import table, generic stub disassembly) before unpacking — the effort won't transfer to understanding the actual payload.
- Identify the specific packer before attempting a generic unpacking approach where possible — packer-specific unpacking methods are usually faster and more reliable than generic OEP-hunting.
- Always fix the import table on a dumped image — a memory dump without import-table repair frequently fails to disassemble or load correctly even though the code itself was successfully recovered.
- Re-run basic static analysis (strings, imports) on the unpacked dump, not just the original file — the whole point of unpacking is that the original file's static properties are uninformative.

## Examples

**Successful unpacking workflow:** An analyst notices a sample's import table contains only `LoadLibraryA` and `GetProcAddress` and the file has unusually high entropy. They identify a known packer via signature match, set a breakpoint on the documented API call that packer uses to transfer control to the unpacked payload, dump memory at that point, repair the import table, and successfully extract readable strings referencing the payload's actual C2 infrastructure.

**Skipped-unpacking failure mode (contrast case):** An analyst spends an hour manually disassembling a packed sample's on-disk stub, producing detailed notes on a generic decompression loop that reveals nothing about the payload's actual purpose — time that would have been saved by recognizing the packing signature and dumping the unpacked payload first.

## Common Mistakes

- **Attempting manual disassembly of a packed binary's stub** without recognizing the packing signature first, wasting analysis effort on code that isn't the actual payload.
- **Dumping memory at the original entry point but skipping import-table repair**, producing a dump that won't load correctly in standard tools even though the unpacking step itself succeeded.
- **Assuming a small file size means simple, easily-analyzed software**, rather than checking entropy — a small, high-entropy file is a packing signature, not a simplicity signal.
- **Using a generic unpacking approach when a packer-specific, documented method already exists** for the identified packer — generic approaches are slower and less reliable when a known method is available.

## When NOT to Use

- When the binary shows no packing signatures (normal entropy, a full and sensible-looking import table, disassembly that resolves to recognizable program logic) — unpacking adds no value to an already-unpacked binary.
- When a fully automated sandbox already provides an unpacked memory dump as part of its standard output — manual unpacking is redundant in that case.
- For custom, non-standard packing/obfuscation specifically designed to defeat automated and signature-based unpacking — this requires a dedicated, often sample-specific reverse-engineering effort beyond the scope of standard unpacking technique, and should be scoped as its own analysis task.
