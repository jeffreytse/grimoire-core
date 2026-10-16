---
name: apply-static-before-dynamic-analysis
description: Use when beginning reverse engineering of an unfamiliar binary — run basic static analysis (strings, imports, headers, disassembly overview) before any dynamic/behavioral analysis, because static analysis is cheap, safe, and builds falsifiable hypotheses about the binary's purpose that dynamic analysis can then target and confirm, rather than running the binary blind and hoping to observe the relevant behavior.
source: 'Michael Sikorski & Andrew Honig, "Practical Malware Analysis", No Starch Press (2012) — the canonical basic-static-analysis-before-basic-dynamic-analysis sequencing; SANS FOR610 malware analysis curriculum'
tags: [reverse-engineering, malware-analysis, static-analysis, security, binary-analysis]
related: [apply-isolated-analysis-environment, apply-unpacking-before-analysis, apply-known-library-identification]
---

# Apply Static-Before-Dynamic Analysis

Run basic static analysis — strings, imports, headers, a disassembly overview — before any dynamic or behavioral analysis of an unfamiliar binary, because static analysis is cheap, safe, and builds falsifiable hypotheses about the binary's purpose that dynamic analysis can then target and confirm, rather than running the binary blind and hoping to observe the relevant behavior.

## Why This Is Best Practice

**Sikorski & Honig, "Practical Malware Analysis" (2012):** The canonical malware-analysis text structures its entire methodology around this sequencing — basic static analysis (file hashing, strings, PE header inspection, import table review) always precedes basic dynamic analysis (running the sample under observation), which in turn precedes advanced static and advanced dynamic analysis. Static indicators gathered first (suspicious imports like `CreateRemoteThread` or `InternetOpenUrl`, embedded strings like URLs or registry keys) generate specific, checkable hypotheses — "this likely does process injection" or "this likely contacts this domain" — that the analyst can then confirm or refute with targeted dynamic observation, rather than watching unstructured runtime behavior and trying to infer purpose after the fact.

**Why best:** Static analysis carries no execution risk and is far cheaper per unit of information gathered. Jumping straight to execution without a static-analysis-derived hypothesis means the analyst doesn't know what to watch for, what environment conditions to set up, or what inputs might be required to trigger the behavior of interest — and risks executing something harmful before understanding even its basic capability profile.

**Adopted by:** Standard sequencing taught in SANS FOR610 (Reverse-Engineering Malware) and used as the default workflow framework in professional malware-analysis and incident-response teams.
**Impact:** Static indicators (suspicious import tables, embedded strings) routinely allow analysts to classify a sample's general capability (keylogger, ransomware, backdoor) within minutes, before any execution risk is taken on — materially reducing the time and risk cost of the subsequent dynamic analysis phase by narrowing what it needs to confirm.

## Steps

1. **Hash the sample and check it against known-malware and known-good databases first** (VirusTotal, NSRL) — this alone may resolve the analysis before deeper work is needed.
2. **Extract strings and review them for URLs, IPs, file paths, registry keys, and command-and-control-style formatting** — strings frequently reveal intent even in stripped or lightly obfuscated binaries.
3. **Inspect the file header and import/export tables** (PE, ELF, Mach-O as applicable) — the specific APIs a binary imports (`VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`, `InternetOpenUrl`) strongly constrain what categories of behavior are even possible.
4. **Check whether the binary is packed or obfuscated before investing further static effort** — if so, address unpacking first (see `apply-unpacking-before-analysis`); static analysis of packed code produces largely meaningless results.
5. **Form specific, falsifiable hypotheses from the static evidence** ("this likely performs process injection," "this likely beacons to this domain") before moving to dynamic analysis.
6. **Use dynamic analysis specifically to confirm or refute those hypotheses**, in an isolated environment (see `apply-isolated-analysis-environment`), rather than as an unstructured first step.

## Rules

- Never run an unfamiliar or untrusted binary before completing basic static analysis — execution risk should be taken on deliberately, after forming a hypothesis about what the binary can do, not before.
- Treat static analysis results as hypotheses to confirm, not conclusions — static analysis alone can miss runtime-only behavior (unpacked payloads, dynamically resolved APIs, environment-triggered logic).
- If the binary is packed, resolve that first — static analysis of the packed wrapper tells you little about the payload's actual behavior.
- Document static findings before moving to dynamic analysis so the dynamic session has specific, written targets to confirm rather than relying on memory.

## Examples

**Correctly sequenced analysis:** An analyst extracts strings from an unfamiliar sample and finds a hardcoded URL and references to `schtasks.exe`; the import table shows `WinExec` and `RegSetValueEx`. Before executing anything, they form the hypothesis "likely persistence via scheduled task plus a C2 callback to this URL," then run the sample in an isolated sandbox specifically watching for scheduled-task creation and network traffic to that URL — confirming the hypothesis in a single, targeted dynamic pass.

**Skipped-static-analysis failure mode (contrast case):** An analyst runs an unfamiliar sample directly in a debugger with no prior static review, with no specific behavior to watch for. The binary executes a short-lived payload and self-deletes before the analyst notices the relevant behavior, requiring a second, more carefully prepared run — the static pass that would have flagged the self-deletion routine and told them what to watch for was skipped.

## Common Mistakes

- **Executing an unfamiliar binary before basic static analysis**, losing the opportunity to form a targeted hypothesis and increasing uncontrolled execution risk.
- **Treating static analysis results as final conclusions** rather than hypotheses that still need dynamic confirmation — static analysis can miss runtime-only or environment-triggered behavior entirely.
- **Attempting static analysis on a packed binary without unpacking first**, producing disassembly and strings that reflect the packer, not the actual payload.
- **Skipping string/import review and going straight to full disassembly**, spending analysis time on low-level detail before the high-level capability picture is established.

## When NOT to Use

- When the binary is already known (matched by hash to a well-documented, previously-analyzed sample) — in that case, consult existing analysis reports before re-deriving the same static findings from scratch.
- For heavily obfuscated or packed samples where static analysis genuinely cannot proceed until unpacking is resolved — address `apply-unpacking-before-analysis` first.
- In live incident response under severe time pressure where a quick dynamic detonation in an isolated sandbox is needed to confirm active compromise indicators immediately — static analysis can proceed in parallel rather than strictly gating the response.
