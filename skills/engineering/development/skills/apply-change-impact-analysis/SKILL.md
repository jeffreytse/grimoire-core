---
name: apply-change-impact-analysis
description: Use when about to ship a change you don't fully trust, or when asked "what could this break" — find the one fact the change's safety actually depends on, trace effects beyond what a caller search shows (serialized formats, downstream consumers, timing, feature flags), and prove the safety claim by running real code instead of handing back a convincing-sounding writeup.
source: 'Shawn A. Bohner and Robert S. Arnold, "Software Change Impact Analysis", IEEE Computer Society Press (1996); Google Site Reliability Engineering, "Site Reliability Engineering", O''Reilly (2016), Ch. 16 — limiting the blast radius of a change via staged rollouts and canarying'
tags: [change-management, risk-assessment, code-review, software-engineering, regression-prevention]
related: [review-pull-request, diagnose-bug, apply-hypothesis-driven-debugging]
---

# Apply Change Impact Analysis

Before shipping a change you don't fully trust, find the one fact its safety depends on, trace its effects beyond what a caller search shows, and prove the claim by running real code rather than handing back a writeup that merely sounds right.

## Why This Is Best Practice

**Bohner & Arnold, "Software Change Impact Analysis" (1996):** The foundational, widely-cited text formalizing impact analysis as a distinct engineering discipline: identifying the potential consequences of a change, including effects beyond the immediately-modified code, before the change ships — explicitly distinguishing it from simply listing direct callers, since many real effects (data formats, timing, downstream consumers) aren't visible from a static call-site search.

**Google SRE book, Ch. 16:** Formalizes "blast radius" as a named engineering concept — the scope of what a given change could affect if it goes wrong — and prescribes staged rollouts and canarying specifically to bound it, on the premise that a change's true blast radius is routinely larger than its author's mental model of "what this touches."

**Why best:** A caller search finds what a tool can already show you in seconds; it does not find what a tool can't show you — a downstream consumer of a serialized format, a timing-dependent interaction, a feature flag gating a code path, another language reading the same bytes. A written risk analysis that "sounds right" is not evidence: prose is convincing whether or not it's true, so the only claim worth trusting is one that was proven by actually running the code in question, not one that was argued persuasively.

**Adopted by:** Change impact analysis is standard practice in formal software engineering curricula and safety-critical development processes building on Bohner & Arnold's work; "blast radius" containment via canarying and staged rollout is standard SRE practice at Google and widely adopted across the industry as a named risk-management discipline.
**Impact:** Google's SRE practice attributes a significant share of avoided large-scale outages to deliberately bounding blast radius (canary stages, staged rollouts) specifically because the full impact of a change is routinely wider than the diff suggests — the discipline exists because trusting the diff alone has a demonstrated failure history.

## Steps

1. **Read the full change**: the diff, every symbol it adds, changes, or deletes, and what now behaves differently — including effects the diff itself doesn't spell out directly.
2. **Find the one or two facts the change's safety actually depends on.** Most changes that look risky are safe because of a single underlying fact (e.g., "this only touches already-expired cache entries"); find that fact rather than enumerating an open-ended list of maybes.
3. **Look specifically where a caller search stops**: read the actual source of any library involved at its pinned version, trace what a serialized format or wire format means to another consumer, check feature flags and timing-dependent paths (unmount/teardown order, async scheduling), and consider another language or service reading the same data.
4. **Rate your confidence in each safety-critical fact honestly**, from weakest to strongest evidence: an assertion with no backing; a cited `file:line`; a traced argument that the bad case can't be reached; a script or test that actually runs the real code and fails loudly if you're wrong; a reproduction in the running system itself.
5. **Prove the load-bearing fact by running real code** — write the smallest script or test that exercises the actual function or path in question, run it, and keep the output as evidence, rather than stopping at a written argument for why it's safe.
6. **Separate confirmed risks from cleared ones explicitly** in what you report — list what you checked and ruled out, not just what you're still worried about, and never invent a caller or API that wasn't actually found.

## Rules

- A caller or dependency search finds the easy, visible effects; actively look past it for format, timing, flag, and cross-language effects it can't show you.
- Do not accept a risk assessment — your own or someone else's — on the strength of how convincing it reads; only a run of the real code counts as proof.
- Identify the specific fact a change's safety depends on, rather than producing an open-ended list of hypothetical risks.
- Report confirmed risks and cleared risks as two separate, explicit categories, each backed by a real citation or a real run.

## Examples

**Finding the load-bearing fact:** A change modifies a cache-eviction function. The engineer identifies the single fact the change's safety depends on — "this function only ever evicts entries already past their TTL" — and writes a short script that calls the real function against a cache with both expired and live entries, confirming live entries are never touched, rather than arguing the point in prose.

**Looking past the caller search:** A change to an API response's field name has no remaining callers in the current codebase. Checking further, the engineer finds the field is also consumed by a downstream analytics pipeline reading the same JSON from a message queue — a consumer a symbol search inside the repository would never surface.

## Common Mistakes

- **Treating a list of direct callers found by search as a complete impact analysis**, missing serialized formats, timing dependencies, feature flags, and cross-service or cross-language consumers.
- **Trusting a well-written risk assessment as sufficient proof**, when no part of it was verified by actually running the code in question.
- **Listing every conceivable risk with equal weight** instead of identifying the one or two facts the change's actual safety depends on.
- **Inventing a plausible-sounding caller or API** when a search turns up nothing, rather than reporting the negative search result as the actual answer.

## When NOT to Use

- For a trivial, clearly-scoped change with no plausible path to affecting anything outside the immediate diff — full impact analysis has a cost that isn't justified for every change.
- When the change is already covered by a comprehensive, trusted automated test suite that exercises the exact paths in question — the proof-by-execution this skill calls for may already exist as a passing test run.
