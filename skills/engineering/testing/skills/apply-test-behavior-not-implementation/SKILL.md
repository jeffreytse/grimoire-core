---
name: apply-test-behavior-not-implementation
description: Use when writing, reviewing, or deciding whether to keep a test — assert only what the code's users can observe (return values, errors, readable state, effects on outside systems), never internal call order or intermediate data, and judge each test with two mutations — breaking real behavior should fail it, changing only internals should not — because a test failing either check proves nothing or is pinned to implementation it shouldn't care about.
source: 'Kent Beck, "Test-Driven Development: By Example", Addison-Wesley (2002); Ian Cooper, "TDD, Where Did It All Go Wrong", ACCU London (2017); Gerard Meszaros, "xUnit Test Patterns: Refactoring Test Code", Addison-Wesley (2007) — classicist vs. mockist testing'
tags: [testing, unit-testing, test-design, software-quality, engineering]
related: [write-unit-test, apply-test-driven-development, audit-test-coverage]
---

# Apply Test Behavior, Not Implementation

Assert only what the code's users can observe through its interface — return values, errors, readable state, effects on outside systems — never internal call order or intermediate data, and judge each test against two mutations: breaking the real behavior should fail it, and changing only the internals while preserving behavior should not.

## Why This Is Best Practice

**Beck, "Test-Driven Development: By Example" (2002):** Frames tests as a specification of behavior from the caller's perspective — a test should describe what the code does, observable through its public interface, not how it does it internally. This framing is what makes tests a safe refactoring aid rather than an obstacle to refactoring.

**Cooper, "TDD, Where Did It All Go Wrong" (2017):** A widely-cited talk arguing that much of the frustration developers report with TDD comes specifically from testing implementation details (mocking every internal collaborator, asserting on private method call order) rather than testing behavior through the public interface — producing tests that break on every internal refactor even when the externally-visible behavior is unchanged, training teams to see tests as a liability rather than a safety net.

**Meszaros, "xUnit Test Patterns" (2007):** Formalizes the classicist-versus-mockist testing distinction — classicist tests exercise real collaborators and assert on observable outcomes, while mockist tests replace collaborators with mocks and assert on the interactions between the unit and its (mocked) dependencies. Meszaros documents the specific fragility mockist-style, interaction-heavy tests introduce: they encode assumptions about internal call structure that behavior-preserving refactors routinely violate.

**Why best:** A test's entire value is that it keeps passing when behavior is preserved and fails when behavior breaks — a test that does the opposite (passes when behavior breaks, fails when only internals change) is actively harmful: it gives false confidence in the first case and blocks legitimate refactoring in the second. The two-mutation check makes this concrete and checkable rather than a matter of taste.

**Adopted by:** The classicist testing style is the default recommendation in Beck's own TDD writing and is widely taught alongside the "don't mock what you don't own" and "test behavior, not implementation" heuristics in modern testing guidance (Google Testing Blog, Martin Fowler's writing on test doubles).
**Impact:** Cooper's talk and the broader classicist/mockist discussion are frequently cited as the explanation for teams abandoning unit testing after bad early experiences with implementation-coupled tests — the specific, recurring failure mode is tests that break on every internal refactor despite the refactor changing no observable behavior, which erodes trust in the test suite's value.

## Steps

1. **Identify what the code's users can actually observe** through its interface: return values, thrown errors or rejected promises, state that can be read back through a public accessor, and effects on external systems (a database write, a network call, a file written).
2. **Write assertions only against that observable surface** — never against private method call counts, internal call order between collaborators the test doesn't own, or intermediate variables not exposed by the interface.
3. **Apply the "break the behavior" mutation check**: imagine introducing a real bug (a wrong value, a skipped or doubled effect) and ask whether the test would fail. If it wouldn't, the test proves nothing — the usual causes are an assertion that's too loose, an expected value computed by the code under test itself, or an assertion on data the test constructed rather than data the code under test produced.
4. **Apply the "change the internals" mutation check**: imagine refactoring the implementation while keeping every observable result identical, and ask whether the test would still pass. If it wouldn't, the test is pinned to implementation details it shouldn't care about.
5. **Prefer real collaborators over mocks where feasible**, reserving mocks specifically for genuine external boundaries (network calls, third-party services, non-deterministic sources) rather than for every internal collaborator.
6. **When a test fails after a refactor with no behavior change, treat that as a signal the test was implementation-coupled**, and rewrite it against the observable interface rather than simply updating the assertion to match the new internals.

## Rules

- Assert only on what's observable through the code's public interface — return values, errors, readable state, external effects — never on private internals or inter-collaborator call order the interface doesn't expose.
- Run both mutation checks on every test you write or review: does it fail when real behavior breaks, and does it survive a behavior-preserving internal refactor?
- Reserve mocks for genuine external boundaries (network, third-party services, non-determinism), not as a default substitute for real internal collaborators.
- When a refactor with no behavior change breaks a test, fix the test's coupling to implementation rather than treating the refactor as the problem.

## Examples

**Behavior-focused test:** A test for a shopping cart's `addItem` method asserts that, after adding two of the same item, `cart.getTotal()` returns the correct summed price and `cart.getItemCount()` returns 2 — both observable through the cart's public interface, regardless of whether the internal implementation uses a map, a list, or a different data structure to track items.

**Implementation-coupled test (contrast case, fails the check):** A test for the same `addItem` method instead asserts that a private `_recalculatePriceCache()` method was called exactly once and that an internal `_items` array has a specific internal shape. Refactoring the cart to use a different internal data structure — with `getTotal()` and `getItemCount()` still returning identical, correct values — breaks this test even though no observable behavior changed.

**The "break the behavior" check catching a weak test:** A test asserts `result.success === true` after calling a payment function, without checking the actual charged amount. Introducing a bug that charges the wrong amount while still returning `success: true` doesn't fail this test — revealing that the assertion was too loose to actually verify the behavior that matters.

## Common Mistakes

- **Asserting on internal call order or private method invocation counts** instead of on the method's observable return value, errors, or external effects.
- **Mocking every internal collaborator by default**, producing tests that verify the test's own mock setup rather than the unit's actual behavior.
- **Writing an assertion so loose it would pass even if the real behavior were broken** — the "break the behavior" mutation check is specifically designed to catch this.
- **"Fixing" a test that broke after a pure refactor by updating its assertions to match the new internals**, rather than recognizing the test was coupled to implementation and rewriting it against the observable interface.

## When NOT to Use

- For genuine integration or contract tests whose explicit purpose is verifying interaction with a specific external collaborator (confirming the right API endpoint was called with the right payload) — that interaction is the observable behavior being tested in that specific case, not an implementation detail.
- For performance or resource-usage tests where the number of expensive internal calls (e.g., database queries) is itself the behavior under test — counting calls is appropriate when the count itself is a stated requirement, not an implementation accident.
- When a function has no meaningful external interface at all (a genuinely private, single-caller helper with no independent contract) — in that case, test it through its one caller's observable behavior rather than directly.
