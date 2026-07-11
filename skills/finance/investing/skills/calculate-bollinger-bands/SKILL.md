---
name: calculate-bollinger-bands
description: Use when assessing a security's current volatility and relative price position — plotting bands a set number of standard deviations above and below a moving average, and reading band width and price position relative to the bands as signals of volatility contraction/expansion and potential overbought/oversold conditions.
source: John Bollinger, developer of Bollinger Bands; widely adopted across technical-analysis charting platforms and trading education
tags: [finance, investing, technical-analysis, bollinger-bands, volatility, moving-average]
related: [calculate-williams-percent-r, apply-guppy-multiple-moving-average, apply-dow-theory]
---

# Calculate Bollinger Bands

Plot bands set a defined number of standard deviations above and below a moving average, and read the band width (a measure of relative volatility) and the price's position relative to the bands (a measure of relative extension) as complementary signals — narrowing bands suggesting a potential volatility expansion ahead, and price reaching a band suggesting a relatively extended position rather than an automatic reversal signal.

## Why This Is Best Practice

**Adopted by:** John Bollinger developed Bollinger Bands, and the indicator has since become one of the most widely adopted technical-analysis tools across virtually every major charting platform and trading education curriculum, used to visualize a security's relative volatility and price extension in a single, standardized format.
**Impact:** Because the bands are calculated using standard deviations of price around a moving average, they automatically widen during periods of higher volatility and narrow during periods of lower volatility — this self-adjusting property means the bands provide a relative, volatility-normalized measure of price extension that a fixed-percentage band around a moving average would not, and the specific pattern of narrowing bands ("the squeeze") is widely used as a signal that a period of low volatility may precede a subsequent volatility expansion.
**Why best:** A security's absolute price level or a fixed-percentage band doesn't account for the fact that "normal" price fluctuation varies over time as volatility itself changes — Bollinger Bands' standard-deviation basis automatically adjusts for this, providing a more consistently interpretable measure of relative price extension and volatility regime across different market conditions for the same security.

Sources: Bollinger Bands, widely documented across technical-analysis education and charting platforms

## Steps

### Step 1: Calculate the moving average and standard deviation

Calculate a moving average over a standard period (commonly 20 periods) and the standard deviation of price around that average over the same period, as the basis for the bands.

### Step 2: Plot the upper and lower bands

Plot the upper band a defined number of standard deviations (commonly 2) above the moving average, and the lower band the same number of standard deviations below it — these bands will automatically widen during higher-volatility periods and narrow during lower-volatility periods.

### Step 3: Read narrowing bands as a potential precursor to volatility expansion

Treat a period of unusually narrow bands (sometimes called a "squeeze") as indicating unusually low relative volatility, which is commonly followed by a subsequent expansion in volatility — though the direction of the eventual breakout is not itself indicated by the squeeze alone.

### Step 4: Read price position relative to the bands as relative extension, not an automatic reversal signal

Treat price reaching or exceeding the upper band as indicating a relatively extended position to the upside, and price reaching or exceeding the lower band as a relatively extended position to the downside — recognizing that during a strong trend, price can "walk the band," remaining near or beyond it for an extended period without an immediate reversal.

### Step 5: Combine band signals with broader trend and momentum context

Use Bollinger Band signals alongside broader trend-confirmation tools (see `apply-dow-theory`) and momentum indicators (see `calculate-williams-percent-r`) — a price reaching the upper band within a strong confirmed uptrend carries different implications than the same signal occurring within a weakening or range-bound market.

## Rules

- Calculate using a consistent, standard period and standard-deviation multiplier unless a specific reason calls for adjustment.
- Treat band narrowing as signaling a potential volatility expansion ahead, without assuming a specific direction for the resulting move.
- Never treat price reaching a band as an automatic reversal signal — strong trends can "walk the band" for extended periods.
- Combine with broader trend and momentum context rather than relying on band position alone.

## Examples

**Squeeze correctly interpreted as volatility warning, not directional signal:** An investor observes Bollinger Bands narrowing unusually on a security, correctly interpreting this as a signal that a period of low volatility may precede an expansion, without assuming which direction the eventual move will take. The investor prepares for increased volatility without committing to a directional bet based on the squeeze alone.

**Band-walk correctly recognized during a strong trend:** A different security's price reaches and remains near the upper Bollinger Band for an extended period during a strong, confirmed uptrend. Rather than treating this as an automatic overbought reversal signal, the investor recognizes the "band walk" pattern common during strong trends and combines this observation with broader trend-confirmation context before drawing any conclusion about a potential reversal.

## Common Mistakes

- **Treating price reaching a band as an automatic reversal signal** — strong trends can "walk the band" for extended periods without an immediate reversal.
- **Assuming a squeeze indicates the direction of the subsequent breakout** — narrowing bands signal a likely volatility expansion, not which direction that expansion will move.
- **Using an unusual period or standard-deviation multiplier without a specific reason** — the standard settings provide comparability across analyses; deviate only with clear rationale.
- **Relying on band signals in isolation without broader trend or momentum context** — combine with `apply-dow-theory` and `calculate-williams-percent-r` for a fuller picture.

## When NOT to Use

- As a standalone basis for a long-term fundamental investment decision — see `audit-investment-thesis`; this tool addresses short-term volatility and relative price extension, not long-term valuation.
- Without broader trend context — band position alone, without checking the prevailing trend, can lead to premature or incorrect reversal conclusions.
- For a security with insufficient price history to calculate a meaningful moving average and standard deviation.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
