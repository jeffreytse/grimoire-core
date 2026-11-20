---
name: apply-illegal-states-unrepresentable
description: Use when a type's fields can be combined into states that shouldn't exist — optional fields that are only sometimes valid together, booleans that must stay in sync, a string field that's really one of a few fixed cases — redesign the type (discriminated unions, parsed domain types, state machines) so the invalid combination cannot be constructed at all, rather than validating against it at runtime.
source: 'Yaron Minsky, "Effective ML Revisited", Jane Street Tech Blog (2011) — "make illegal states unrepresentable"; Alexis King, "Parse, Don''t Validate", blog post (2019); Scott Wlaschin, "Domain Modeling Made Functional", Pragmatic Bookshelf (2018)'
tags: [type-design, domain-modeling, software-architecture, engineering, correctness]
related: [apply-domain-driven-design, apply-encapsulation, apply-fail-fast]
---

# Apply Illegal States Unrepresentable

When a type's fields can be combined into states that shouldn't exist, redesign the type — using discriminated unions, parsed domain types, or state machines — so the invalid combination cannot be constructed at all, rather than validating against it at runtime.

## Why This Is Best Practice

**Minsky, "Effective ML Revisited" (Jane Street, 2011):** Coined "make illegal states unrepresentable" as a specific design discipline: instead of writing a type broad enough to hold both valid and invalid data and then checking for validity at every use site, design the type so the invalid combination has no representation in it at all — the compiler, not a runtime check, becomes the enforcement mechanism.

**King, "Parse, Don't Validate" (2019):** Distinguishes validating (checking that data meets a condition, then discarding that proof and passing around the original, still-weakly-typed value) from parsing (converting weakly-typed data into a more precise type that itself proves the condition holds, so every downstream consumer gets the guarantee for free without re-checking it). A parsed type carries its own validity as a property of its shape.

**Wlaschin, "Domain Modeling Made Functional" (2018):** Demonstrates the technique systematically across real domain-modeling examples — replacing a "contact info" type with optional email and optional phone fields (which can represent the invalid state of having neither) with a discriminated union of "email only / phone only / both," which cannot represent the invalid state structurally.

**Why best:** A validated-but-not-parsed type still requires every function that touches it to either re-check the condition or risk an unhandled bad-state bug — the invalid combination still exists as a representable value, waiting for the one call site that forgets to check. A type that structurally excludes the invalid state moves the check to a single point (construction) and eliminates the bug class everywhere else, rather than requiring discipline at every use site.

**Adopted by:** Standard discipline in the OCaml/F#/Haskell functional-programming community (Jane Street, origin of the phrase), and widely adopted beyond it as discriminated unions and sum types have become mainstream in TypeScript, Rust, Swift, and Kotlin.
**Impact:** Wlaschin's worked examples and Minsky's original post both document the same empirical pattern: a significant share of null-reference and invalid-combination bugs in large codebases trace back to a type that could represent more states than the domain actually allows — redesigning the type to exclude those states eliminates the entire bug class rather than requiring a defensive check to catch each instance.

## Steps

1. **Identify a type with fields that can combine into a state that shouldn't exist** — two optional fields where exactly one must be present, a boolean flag that must stay synchronized with another field, a string field that's really one of a small fixed set of cases.
2. **Enumerate the actual valid states the domain allows**, not the states the current type's shape happens to permit.
3. **Redesign the type to have exactly one representation per valid state** — a discriminated union with one variant per case, a state machine with explicit transitions, or a parsed type constructed only through a function that enforces the invariant.
4. **Move validation to a single construction point** (a parse function, a smart constructor) rather than scattering checks across every function that consumes the type.
5. **Let every downstream consumer rely on the type's shape as a guarantee**, removing the redundant re-validation or defensive null/case checks that the old, broader type required.
6. **Apply the same discipline at system boundaries**: parse external data (JSON, CLI args, database rows) into the precise domain type immediately, rather than passing the loosely-typed raw form deeper into the system.

## Rules

- Redesign the type itself when a state shouldn't exist, rather than relying on a runtime check at every site that constructs or consumes it.
- Give each valid domain state exactly one representation — if two different field combinations can mean the same thing, or one combination can mean two different things, the type doesn't yet match the domain.
- Validate once, at construction (parsing), not repeatedly at every use site — the type's shape should make the downstream re-check unnecessary.
- Apply this at system boundaries specifically — external data is unparsed and untyped until it passes through a parse function that returns the domain's precise type.

## Examples

**Discriminated union replacing optional-field soup:** A `ContactInfo` type with optional `email` and optional `phone` fields can represent an invalid "neither" state and an ambiguous "both, but which is primary" state. Replacing it with a discriminated union — `EmailOnly(email)`, `PhoneOnly(phone)`, `Both(email, phone)` — makes the "neither" state unconstructable and makes the "both" case's handling explicit rather than inferred.

**Parse-don't-validate at a boundary:** Instead of accepting a raw string as a user's age and checking `age >= 0 && age <= 150` at every function that uses it, a parse function converts the raw string into a `ValidAge` type at the system boundary, returning an error for invalid input. Every downstream function accepting `ValidAge` is guaranteed the value is sane without re-checking.

**State machine replacing boolean soup:** An order-processing type with `isPaid`, `isShipped`, and `isCancelled` booleans can represent impossible combinations (shipped but not paid, cancelled but also shipped). A state machine with explicit states (`Pending`, `Paid`, `Shipped`, `Cancelled`) and defined transitions between them makes the impossible combinations unconstructable and the valid transition sequence explicit.

## Common Mistakes

- **Adding a runtime check or assertion for an invalid combination instead of redesigning the type**, leaving the invalid state representable and requiring the same check to be remembered at every other site that touches the type.
- **Validating data and then discarding the proof**, passing the original loosely-typed value downstream instead of the more precise, parsed type that would let consumers skip re-validation.
- **Letting two boolean flags represent what is really one three-or-more-way state**, instead of using a single enum or discriminated union with one case per actual possibility.
- **Parsing external data deep inside business logic rather than at the system boundary**, leaving earlier code to handle the raw, unparsed form unnecessarily.

## When NOT to Use

- For a type with no invalid combinations possible given its actual field set — this technique specifically targets types that can represent more states than the domain allows; a type that already matches its domain exactly needs no redesign.
- In a language or context without sum types or discriminated unions available, where the equivalent redesign would require disproportionate ceremony — a well-documented runtime invariant check may be the pragmatic fallback, with the trade-off made explicit.
- For genuinely transient, internal-only data where the cost of a redesign exceeds the risk of the invalid state ever mattering (a short-lived local variable checked once, immediately after creation, with no other consumer).
