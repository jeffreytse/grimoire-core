---
name: calculate-value-at-risk
description: Use when quantifying how much a portfolio could plausibly lose over a specific time horizon at a specific confidence level — expressing risk as a single, comparable dollar or percentage figure (Value at Risk) rather than a qualitative sense of "risky" or "safe."
source: J.P. Morgan RiskMetrics methodology (1994); Basel Committee on Banking Supervision market-risk capital framework
tags: [finance, investing, value-at-risk, var, risk-measurement, quantitative-risk, portfolio-risk]
related: [calculate-risk-adjusted-return, design-portfolio-stress-test, design-concentration-risk-limits]
---

# Calculate Value at Risk

Quantify how much a portfolio could plausibly lose over a specific time horizon at a specific confidence level, expressing risk as a single, comparable figure — Value at Risk (VaR) — rather than relying on a qualitative sense of a portfolio being "risky" or "safe."

## Why This Is Best Practice

**Adopted by:** J.P. Morgan popularized Value at Risk as a standardized risk metric through its RiskMetrics methodology, published in 1994 and subsequently made freely available to the industry, and VaR has since become a core component of the Basel Committee on Banking Supervision's market-risk capital framework, required or expected of regulated banks and widely adopted by asset managers and institutional investors as a standard portfolio risk metric.
**Impact:** Prior to VaR's standardization, portfolio risk was often communicated through disparate, hard-to-compare metrics (volatility, beta, qualitative risk ratings) that didn't translate into a single, actionable figure decision-makers could use directly — VaR's specific contribution was expressing risk as "we could lose no more than $X with Y% confidence over Z days," a figure directly comparable across different portfolios, asset classes, and time horizons.
**Why best:** A qualitative risk assessment ("this portfolio seems more volatile") doesn't tell a decision-maker how much capital is actually at stake, or allow direct comparison against a risk limit or capital reserve — VaR converts risk into a specific, actionable number that can be checked against a limit, compared across portfolios, and tracked over time, at the cost of depending on assumptions (historical data, distributional assumptions) that can break down in extreme, unprecedented conditions.

Sources: J.P. Morgan RiskMetrics Technical Document (1994); Basel Committee on Banking Supervision, "Minimum Capital Requirements for Market Risk"

## Steps

### Step 1: Choose the time horizon and confidence level

Select the time horizon (commonly one day or ten days for trading portfolios, longer for less liquid portfolios) and confidence level (commonly 95% or 99%) the VaR figure will be calculated at — these choices directly determine the resulting figure's interpretation and must be stated explicitly alongside any VaR number.

### Step 2: Select a calculation methodology appropriate to the portfolio

Choose a VaR calculation methodology — historical simulation (using actual historical return data), variance-covariance/parametric (assuming a return distribution, commonly normal), or Monte Carlo simulation (generating many simulated future paths) — based on the portfolio's complexity and the data available, recognizing each methodology carries different assumptions and limitations.

### Step 3: Calculate the VaR figure using the chosen methodology and inputs

Apply the chosen methodology to the portfolio's current holdings and historical or simulated return data to produce the VaR figure — the maximum loss not expected to be exceeded over the chosen horizon at the chosen confidence level, under the methodology's assumptions.

### Step 4: Interpret VaR as a threshold, not a worst-case guarantee

Interpret the resulting VaR figure correctly as a threshold expected to be exceeded only in the stated percentage of scenarios (e.g., a 95% one-day VaR is expected to be exceeded roughly 5% of trading days) — not as an absolute worst-case loss, since losses beyond the VaR threshold remain possible and can be substantially larger, a limitation VaR alone does not communicate.

### Step 5: Complement VaR with tail-scenario analysis beyond the confidence threshold

Pair the VaR figure with separate analysis of what a loss beyond the VaR threshold could look like (see `design-portfolio-stress-test`), since VaR by construction says nothing about the severity of losses in the tail scenarios beyond its stated confidence level — a critical limitation any VaR-based risk process must explicitly address, not merely acknowledge.

## Rules

- Always state the time horizon and confidence level alongside any VaR figure — the number is meaningless without both.
- Choose the calculation methodology (historical, parametric, Monte Carlo) deliberately based on the portfolio's characteristics and available data, not by default.
- Never present VaR as a worst-case loss guarantee — it is a threshold expected to be exceeded in the stated minority of scenarios, and losses beyond it can be substantially larger.
- Pair VaR with separate tail-scenario or stress-test analysis, since VaR alone provides no information about losses beyond its confidence threshold.

## Examples

**VaR correctly interpreted as a threshold:** A portfolio manager calculates a one-day 95% VaR of $2 million, correctly communicating this as "on a typical trading day, we don't expect to lose more than $2 million, but on roughly one trading day in twenty, losses could exceed this figure — and this calculation says nothing about how much they could exceed it by." This framing correctly conveys both what VaR does and does not tell the risk committee.

**VaR misused as a worst-case guarantee (illustrative failure mode):** A different team presents VaR as the portfolio's maximum possible loss, without any complementary tail-scenario analysis. During an unprecedented market dislocation, losses substantially exceed the stated VaR figure — a failure of interpretation, not calculation, since VaR was never designed to bound losses in the tail scenarios beyond its stated confidence level.

## Common Mistakes

- **Presenting a VaR figure without stating its time horizon and confidence level** — the number is uninterpretable and potentially misleading without both.
- **Treating VaR as an absolute worst-case loss bound** — VaR is a threshold expected to be exceeded in the stated minority of scenarios, not a guarantee against larger losses.
- **Relying solely on VaR without complementary tail-scenario or stress-test analysis** — VaR provides no information about the severity of losses beyond its confidence threshold, a gap that must be addressed separately.
- **Using a VaR methodology poorly suited to the portfolio's actual characteristics** — a parametric model assuming normal returns can significantly understate risk for portfolios with fat-tailed or asymmetric return distributions.

## When NOT to Use

- As the sole risk metric for a portfolio with significant tail risk or non-normal return distributions — VaR must be paired with stress-testing and tail-scenario analysis in these cases (see `design-portfolio-stress-test`).
- For communicating risk to an audience that will predictably misinterpret it as a worst-case guarantee without the necessary context — in this situation, invest in clearer risk communication alongside or instead of a bare VaR figure.
- As a substitute for genuine position-level and concentration-level risk limits — VaR is a portfolio-level aggregate metric and doesn't by itself surface concentrated exposure to a single position or risk factor (see `design-concentration-risk-limits`).

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
