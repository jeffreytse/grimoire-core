---
name: design-risk-parity-portfolio
description: Use when constructing a portfolio intended to perform reasonably across different economic environments — allocating by balanced risk contribution across asset classes suited to growth-up, growth-down, inflation-up, and inflation-down regimes, rather than by capital allocation alone or a single static stock-bond split.
source: Ray Dalio, "Principles" (2017) and Bridgewater Associates' published "All Weather" portfolio methodology
tags: [finance, investing, risk-parity, all-weather-portfolio, asset-allocation, dalio]
related: [design-portfolio-allocation, design-defensive-stock-bond-range, design-glide-path-allocation]
---

# Design Risk Parity Portfolio

Construct a portfolio balanced by risk contribution across asset classes suited to different economic environments — growth rising or falling, inflation rising or falling — rather than allocating by capital amount alone or relying on a single static stock-bond split that performs well in only some of these environments.

## Why This Is Best Practice

**Adopted by:** Ray Dalio developed and published this approach — commonly known as the "All Weather" methodology — through Bridgewater Associates, the hedge fund he founded, and documented the underlying philosophy extensively in "Principles" (2017). The approach is explicitly designed to perform reasonably across a full range of economic environments rather than being optimized for the specific historical period a more conventional stock-heavy portfolio has typically been backtested against.
**Impact:** A conventional portfolio allocated mostly by capital amount (e.g., 60% stocks, 40% bonds) is, in practice, dominated by equity risk, since equities are typically far more volatile than bonds — meaning the portfolio's actual risk exposure is concentrated in growth-sensitive assets even though the capital split looks more balanced. Dalio's published methodology specifically addresses this by balancing risk contribution, not just capital allocation, across asset classes that tend to perform differently depending on whether growth and inflation are rising or falling, aiming for a portfolio less dependent on any single economic environment persisting.
**Why best:** A portfolio that performs well specifically in the economic environment of its recent backtest period (commonly a period of generally falling interest rates and inflation, favorable to both stocks and bonds) may perform poorly in a different environment (e.g., rising inflation, which can hurt both stocks and nominal bonds simultaneously) — balancing risk contribution across assets suited to different regimes reduces dependence on any single environment persisting, at the potential cost of lower returns in the specific environment a conventional portfolio happens to be best suited for.

Sources: Dalio, "Principles" (2017); Bridgewater Associates published "All Weather" portfolio methodology

## Steps

### Step 1: Map the four economic environment quadrants

Identify the four broad economic environments relevant to asset performance: growth rising, growth falling, inflation rising, and inflation falling — and recognize that different asset classes tend to perform differently depending on which combination of these conditions is occurring.

### Step 2: Identify asset classes suited to each environment

Map specific asset classes to the environments they tend to perform best in — equities and corporate credit typically benefit from rising growth; nominal government bonds typically benefit from falling growth and falling inflation; inflation-linked bonds and commodities typically benefit from rising inflation; and other asset combinations suited to the remaining quadrants.

### Step 3: Balance risk contribution, not capital allocation, across the environments

Rather than allocating capital amounts evenly or by a traditional stock-heavy split, size each asset class's position so that its contribution to the portfolio's overall risk (accounting for each asset's typical volatility) is balanced across the different economic-environment exposures — this typically means allocating a smaller capital amount to higher-volatility assets like equities and a larger capital amount to lower-volatility assets like bonds, so that neither dominates the portfolio's actual risk.

### Step 4: Use leverage carefully, if applied, to reach a target overall risk level

Since balancing risk contribions this way can result in a lower-volatility, lower-expected-return portfolio than a conventional stock-heavy allocation, some implementations use modest leverage on the lower-risk assets to bring the overall portfolio's risk and expected return back toward a target level — this step requires particular caution and is not appropriate for every investor (see `apply-leverage-avoidance` for the general risks of leverage).

### Step 5: Rebalance periodically as relative asset volatilities shift

Since the risk-parity balancing depends on each asset class's volatility, and volatility levels change over time, rebalance the portfolio periodically to maintain the intended risk-contribution balance across the four economic-environment exposures, rather than treating an initial risk-parity allocation as fixed indefinitely.

## Rules

- Balance risk contribution across asset classes, not just capital allocation amounts — a capital-balanced portfolio is typically still risk-concentrated in its most volatile component.
- Map specific asset classes to the four growth/inflation environment combinations deliberately, rather than assuming a generic diversified mix automatically covers all environments.
- Apply leverage, if used at all to reach a target risk level, cautiously and with full awareness of its risks (see `apply-leverage-avoidance`).
- Rebalance periodically to maintain the intended risk-contribution balance as relative asset volatilities shift over time.

## Examples

**Risk parity applied correctly:** An investor constructs a portfolio allocating a smaller capital amount to equities (a higher-volatility asset) and a larger capital amount to government bonds and inflation-linked assets (lower-volatility assets), such that each asset class contributes roughly equally to the portfolio's overall risk rather than equities dominating the portfolio's actual volatility despite a smaller capital allocation. The portfolio is designed to hold up reasonably across rising and falling growth and inflation environments, rather than being optimized for one specific environment.

**Capital-balanced but risk-concentrated portfolio (contrast case):** A different investor builds a 60/40 stock-bond portfolio, believing the capital split provides meaningful diversification. Because equities are considerably more volatile than bonds, the portfolio's actual risk is still dominated by equity exposure — illustrating the specific gap between capital-balanced and risk-balanced portfolio construction that this approach addresses.

## Common Mistakes

- **Confusing a capital-balanced portfolio with a risk-balanced one** — a 60/40 stock-bond split looks diversified by capital amount but is typically still dominated by equity risk given the volatility difference between the two asset classes.
- **Assuming a generic diversified portfolio automatically covers all four growth/inflation environments** — deliberately mapping specific asset classes to each environment is required; a portfolio built without this mapping may still be concentrated in exposure to only some environments.
- **Applying leverage without full awareness of its risks** — leverage used to bring a risk-parity portfolio's expected return back toward a target level introduces real risks (see `apply-leverage-avoidance`) that require careful, deliberate consideration.
- **Treating an initial risk-parity allocation as permanently fixed** — relative asset-class volatilities shift over time, requiring periodic rebalancing to maintain the intended risk-contribution balance.

## When NOT to Use

- For an investor whose primary goal is maximizing expected return in a specific, anticipated economic environment rather than robustness across multiple environments — a risk-parity approach may underperform a more concentrated allocation if that specific environment does persist.
- When leverage would be required to reach an acceptable expected return and the investor lacks the risk tolerance or understanding to manage leverage safely — see `apply-leverage-avoidance`.
- For a simpler, standard asset-allocation approach where the added complexity of risk-contribution balancing isn't warranted — see `design-portfolio-allocation` for the more conventional MPT-based approach.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
