---
name: calculate-williams-percent-r
description: Use when assessing whether a security is short-term overbought or oversold — calculating Williams %R (the position of the current close relative to the recent high-low range) to identify potential short-term reversal points, distinct from longer-horizon valuation methods.
source: Larry Williams, developer of the Williams %R indicator; widely adopted across technical-analysis charting platforms and trading education
tags: [finance, investing, technical-analysis, williams-percent-r, overbought-oversold, momentum]
related: [calculate-bollinger-bands, apply-guppy-multiple-moving-average, apply-kostolany-egg-theory]
---

# Calculate Williams %R

Calculate Williams %R — the position of the current closing price relative to the recent high-low trading range — to identify potential short-term overbought or oversold conditions, as a momentum-based signal distinct from and complementary to longer-horizon fundamental valuation methods.

## Why This Is Best Practice

**Adopted by:** Larry Williams developed the %R indicator, and it has since been adopted as a standard technical-analysis tool across virtually every major charting platform and trading education curriculum, alongside other widely-used momentum oscillators, as a measure of a security's short-term position within its recent trading range.
**Impact:** Williams %R specifically measures where the current closing price sits relative to the highest high and lowest low over a defined recent lookback period (commonly 14 periods), expressed as a percentage — a reading near the top of the recent range (conventionally near 0 to -20) suggests the security is trading near recent highs (potentially overbought in the short term), while a reading near the bottom (conventionally near -80 to -100) suggests it's trading near recent lows (potentially oversold).
**Why best:** A security's absolute price level alone provides no information about whether it's currently trading near the extreme of its recent range — Williams %R makes this specifically visible, providing a standardized, comparable measure across different securities of how "stretched" the current price is relative to its own recent trading behavior, useful as a short-term timing input distinct from a longer-horizon valuation assessment.

Sources: Williams %R, widely documented across technical-analysis education and charting platforms

## Steps

### Step 1: Calculate the indicator over the chosen lookback period

Calculate %R as the difference between the period's highest high and the current close, divided by the difference between the period's highest high and lowest low, expressed as a negative percentage (0 to -100) — using a standard lookback period (commonly 14 periods) unless a specific reason calls for a different window.

### Step 2: Interpret readings near the extremes as short-term overbought/oversold signals

Treat a reading near the top of the range (near 0 to -20) as indicating the security is trading near recent highs — a potential short-term overbought condition — and a reading near the bottom (near -80 to -100) as indicating trading near recent lows — a potential short-term oversold condition.

### Step 3: Treat extreme readings as context-dependent, not automatic reversal signals

Recognize that an extreme reading during a genuinely strong trend can persist for an extended period without a reversal — a security in a strong uptrend can remain "overbought" by this measure for a sustained stretch, so an extreme reading alone shouldn't be treated as a standalone signal to act against the prevailing trend.

### Step 4: Combine with trend-confirmation tools before acting on a signal

Use Williams %R readings alongside broader trend-confirmation context (see `apply-dow-theory`, `apply-guppy-multiple-moving-average`) — an oversold reading within a broader downtrend carries different implications than one occurring during a broader uptrend's pullback.

### Step 5: Use as a short-term timing input, not a substitute for fundamental valuation

Treat Williams %R as informing short-term entry or exit timing within a position otherwise justified by fundamental or longer-horizon analysis, rather than as a standalone basis for a longer-term investment decision.

## Rules

- Calculate using a consistent, standard lookback period unless a specific reason calls for adjustment.
- Never treat an extreme reading alone as an automatic reversal signal — extreme readings can persist through strong trends.
- Combine with broader trend-confirmation context before acting on any specific reading.
- Use as a short-term timing tool layered onto a fundamentally-justified position, not as a standalone longer-term investment basis.

## Examples

**Extreme reading combined with trend context:** An investor observes a security showing an oversold Williams %R reading, and checks broader trend context, finding the security is in a pullback within an established, still-intact uptrend rather than a genuine downtrend. Combined with a fundamentally sound underlying thesis, the investor treats this as a potentially favorable short-term entry timing signal within an otherwise longer-term position.

**Extreme reading misapplied without trend context (contrast case):** A different investor sees the same oversold reading on a security that is actually in a strong, established downtrend, and treats the reading alone as a buy signal without checking the broader trend. The security continues declining, since an oversold reading within a genuine downtrend can persist for an extended period rather than immediately reversing.

## Common Mistakes

- **Treating an extreme reading as an automatic reversal signal regardless of trend context** — extreme readings can persist through strong trends without a near-term reversal.
- **Using the indicator as a standalone basis for a longer-term investment decision** — this is a short-term timing tool, not a substitute for fundamental valuation.
- **Ignoring broader trend context when interpreting a specific reading** — the same reading carries different implications depending on whether it occurs within an established uptrend or downtrend.
- **Applying an unusual lookback period without a specific reason** — the standard period provides comparability across different analyses and securities; deviate only with a clear rationale.

## When NOT to Use

- As a standalone basis for a long-term fundamental investment decision — see `audit-investment-thesis` for that distinct process; this indicator addresses short-term timing only.
- Without broader trend-confirmation context — an extreme reading in isolation, without checking the prevailing trend, can be misleading.
- For a security with insufficient price history to establish a meaningful recent trading range.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
