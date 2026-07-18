---
name: design-concentration-risk-limits
description: Use when constructing or managing a portfolio — setting explicit maximum exposure limits to a single issuer, sector, country, or correlated risk factor at the aggregate portfolio level, so no single concentrated exposure can inflict outsized damage even if each individual position was sized reasonably on its own.
source: Basel III large-exposure framework; UCITS (Undertakings for Collective Investment in Transferable Securities) diversification rules
tags: [finance, investing, concentration-risk, diversification, exposure-limits, portfolio-construction]
related: [apply-fixed-fractional-risk-limit, calculate-value-at-risk, design-portfolio-stress-test]
---

# Design Concentration Risk Limits

Set explicit maximum exposure limits to a single issuer, sector, country, or correlated risk factor at the aggregate portfolio level — so that no single concentrated exposure can inflict outsized damage on the portfolio, even in a case where each individual position within that exposure was sized reasonably on its own.

## Why This Is Best Practice

**Adopted by:** The Basel III large-exposure framework requires regulated banks to limit exposure to any single counterparty or connected group of counterparties to a defined percentage of capital, and UCITS diversification rules impose explicit maximum concentration limits on regulated European investment funds — both reflecting a regulatory consensus that position-level risk discipline alone is insufficient without a separate, aggregate-level concentration check.
**Impact:** A portfolio can pass every individual position-sizing check (see `apply-fixed-fractional-risk-limit`) while still accumulating a dangerous aggregate concentration — multiple individually reasonable positions in the same issuer, sector, country, or correlated risk factor can combine into an outsized aggregate exposure that a position-by-position risk check doesn't surface, since it evaluates each position in isolation rather than the portfolio's aggregate exposure profile.
**Why best:** Position-level risk limits and aggregate concentration limits address genuinely different risks — a position-level limit caps how much a single bad call can cost, while a concentration limit caps how much a single correlated risk factor (which may span many nominally different positions) can cost the portfolio as a whole. A portfolio needs both checks, since neither alone catches the risk the other is specifically designed to address.

Sources: Basel Committee on Banking Supervision, "Basel III: Finalising Post-Crisis Reforms," large-exposure framework; European Union UCITS Directive diversification requirements

## Steps

### Step 1: Identify the relevant concentration dimensions for the portfolio

Identify the specific dimensions along which concentration risk matters for the portfolio — single issuer, sector, country, currency, or a shared underlying risk factor (e.g., multiple positions all sensitive to the same commodity price or interest-rate move) — since concentration can occur along any of these dimensions independent of individual position sizing.

### Step 2: Set explicit maximum exposure limits for each relevant dimension

Set explicit, quantified maximum exposure limits for each identified concentration dimension (e.g., no more than a stated percentage of the portfolio in a single issuer, sector, or country), calibrated to the portfolio's specific risk tolerance and mandate, rather than relying on an implicit sense that the portfolio is "reasonably diversified."

### Step 3: Aggregate exposure across nominally distinct positions sharing the same risk factor

Calculate aggregate exposure by summing across all positions that share a given risk factor, even if those positions are nominally distinct (different tickers, different position-level risk assessments) — since the concentration risk arises specifically from the shared underlying factor, not from any single position considered alone.

### Step 4: Check the portfolio's actual aggregate exposures against the set limits

Regularly check the portfolio's actual aggregate exposure along each concentration dimension against the limits set in Step 2, flagging and addressing any limit breach before it accumulates further, rather than only checking concentration at the point of initial portfolio construction.

### Step 5: Reduce or hedge exposure when a concentration limit is breached

When an aggregate exposure limit is breached, reduce the concentrated exposure (trimming positions contributing to it) or hedge the shared underlying risk factor directly (see `apply-cheap-tail-risk-hedging` for one hedging approach) — treating limit breaches as requiring action, not merely as a reporting flag.

## Rules

- Set explicit, quantified concentration limits for each relevant dimension (issuer, sector, country, correlated risk factor), not an implicit sense of adequate diversification.
- Aggregate exposure across nominally distinct positions that share an underlying risk factor, since concentration risk arises from the shared factor, not from any single position in isolation.
- Check aggregate exposures against limits on an ongoing basis, not only at initial portfolio construction.
- Treat a concentration-limit breach as requiring active reduction or hedging, not merely a reporting or monitoring flag.

## Examples

**Concentration limit surfacing a risk position-level checks missed:** A portfolio holds several individually well-sized positions across companies in the same commodity-exporting sector, each passing its own position-level risk check. Aggregating exposure by sector reveals the combined position exceeds the portfolio's set sector concentration limit — a risk invisible to any single position's own risk assessment, prompting the manager to trim the aggregate exposure.

**Concentration limits maintained through portfolio growth:** A different portfolio manager continuously checks aggregate country and currency exposure as the portfolio grows and its composition shifts over time, catching and addressing a gradual concentration buildup in a single country before it breaches the portfolio's set limit — illustrating the value of ongoing, not just initial, concentration checking.

## Common Mistakes

- **Relying solely on position-level risk limits without a separate aggregate concentration check** — individually reasonable position sizes can still combine into a dangerous aggregate concentration along a shared dimension.
- **Checking concentration only at initial portfolio construction, not on an ongoing basis** — concentration can build up gradually as a portfolio's composition shifts over time, requiring continuous monitoring.
- **Failing to aggregate exposure across nominally distinct positions that share an underlying risk factor** — concentration risk specifically arises from this shared factor, which a position-by-position view doesn't surface.
- **Treating a concentration-limit breach as informational rather than requiring action** — a breach should trigger active exposure reduction or hedging, not simply be noted and left unaddressed.

## When NOT to Use

- For a portfolio explicitly and deliberately concentrated by mandate (e.g., a highly concentrated conviction-based strategy, see `apply-concentrated-conviction-investing`) — concentration limits should be calibrated to the portfolio's actual mandate and risk tolerance, not applied as a generic, one-size-fits-all diversification requirement.
- For a very small portfolio where formal concentration-limit infrastructure isn't proportionate to the portfolio's scale — simpler qualitative diversification judgment may be adequate in this case.
- As a substitute for position-level risk sizing — concentration limits address aggregate exposure across positions, not the separate discipline of sizing any individual position (see `apply-fixed-fractional-risk-limit`).

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
