---
name: apply-boundary-validation
description: Use when wiring input validation, error handling, or a framework adapter — concentrate guards where data crosses a system boundary (CLI args, config, network calls, external APIs), parse it into a domain type there, and let everything inside trust that type without re-validating or re-checking it.
source: 'OWASP Application Security Verification Standard (ASVS) v4.0, V5 "Validation, Sanitization and Encoding" — validate at trust boundaries; Alexis King, "Parse, Don''t Validate", blog post (2019); Eric Evans, "Domain-Driven Design", Addison-Wesley (2003) — anti-corruption layer'
tags: [input-validation, system-design, boundary-discipline, software-architecture, defect-reduction]
related: [validate-external-input, apply-illegal-states-unrepresentable, apply-domain-driven-design]
---

# Apply Boundary Validation

Validate and parse data into domain types exactly where it crosses a system boundary, and let everything inside that boundary trust the type without re-checking it.

## Why This Is Best Practice

**OWASP ASVS V5:** Requires that all input be validated at a defined trust boundary before it is used, specifically because validating inconsistently or redundantly throughout a codebase is what produces the gaps attackers find — a single, enforced boundary is auditable; scattered checks are not.

**King, "Parse, Don't Validate" (2019):** Distinguishes checking a condition and discarding the proof (validating) from converting data into a type that itself proves the condition holds (parsing) — a parsed type lets every downstream consumer rely on the guarantee for free, while a merely-validated value still requires the next function to re-check or risk a bug.

**Evans, "Domain-Driven Design" (2003):** The anti-corruption layer pattern formalizes the same boundary: translate a foreign model into your domain's own types at the seam where they meet, so internal code never has to reason about the external system's shape or failure modes directly.

**Why best:** Redundant or inconsistent validation scattered across a codebase is strictly worse than validation concentrated at the boundary: it costs more code, it's harder to audit for completeness, and any call site that forgets to check becomes a silent gap. Concentrating guards at the boundary and parsing into a domain type turns "did we validate this?" into a question with one answer, checkable in one place, instead of a question that has to be re-asked at every function that touches the data.

**Adopted by:** OWASP ASVS is the baseline security-review standard at most enterprises with a formal AppSec program; parse-at-the-boundary is standard practice in Rust, Haskell, OCaml, and increasingly TypeScript codebases (zod/io-ts-style boundary parsers); the anti-corruption layer is standard DDD practice for integrating with legacy or third-party systems.
**Impact:** OWASP's own top-10 and ASVS data attribute a large share of injection, type-confusion, and logic-error vulnerabilities to validation gaps at points where data entered the system without being checked at all, or was checked once but the untyped form was still passed deeper into the code — concentrating validation at the boundary and parsing closes both failure modes at the same time.

## Steps

1. **Identify every point where data crosses a system boundary**: CLI args, config files, environment variables, HTTP request bodies, database rows read back, and responses from external APIs.
2. **Write a parse function at each boundary** that converts the raw, untyped input into a precise domain type — rejecting (not silently coercing) input that doesn't fit.
3. **Pass only the parsed domain type deeper into the system.** Never let the raw, unparsed form travel past the boundary function that was supposed to check it.
4. **Remove validation and defensive checks from internal code** that only re-confirms something already guaranteed by the type coming in — trust the type.
5. **Extract business logic into pure functions with no framework or transport dependency.** The boundary — the CLI handler, the HTTP controller, the adapter — stays thin: parse, call the pure function, serialize the result.
6. **For integrations with external or legacy systems, add an explicit anti-corruption layer** that translates the foreign model into your own domain types, so internal code never depends on the external system's shape.

## Rules

- Ask two tests at every validation or defensive check: is this data crossing a boundary right now? If not, it's redundant. Could this logic be a pure function the boundary just calls? If yes, extract it.
- Parse into a domain type at the boundary; never pass the raw, unparsed input past that point.
- Keep transport and framework types (HTTP request objects, ORM rows, CLI arg structs) out of the business logic's public surface.
- For third-party or legacy integrations, translate at a defined seam rather than letting the foreign model's shape leak into your own code.

## Examples

**Boundary parse replacing scattered checks:** An API handler parses the incoming JSON body into a typed `CreateOrderRequest` domain type immediately, rejecting malformed input with a 400 before any business logic runs. The order-creation function downstream accepts only `CreateOrderRequest` and never checks for missing or malformed fields — the type guarantees it.

**Anti-corruption layer at a legacy integration:** A service integrating with a decades-old SOAP API writes one adapter module that translates SOAP responses into the service's own domain types. No code outside that module ever parses XML or knows the SOAP schema exists.

## Common Mistakes

- **Validating input, then passing the original untyped value downstream** instead of the parsed, guaranteed type — every consumer still has to re-check.
- **Re-validating data deep inside business logic** that was already validated and parsed at the boundary, adding redundant code with no safety benefit.
- **Letting a framework or transport type (an HTTP request object, an ORM row) leak into the business logic's function signatures**, coupling internal code to an external shape.
- **Skipping the anti-corruption layer for a legacy integration** and letting the foreign system's model spread through the codebase, making every future change to that integration a wide-reaching refactor.

## When NOT to Use

- For data that never crosses a trust or system boundary — a value computed and consumed within the same function or module has no boundary to validate at.
- In a very small script or prototype where the cost of a formal boundary layer exceeds the risk — a deliberate, temporary trade-off, not a default.
