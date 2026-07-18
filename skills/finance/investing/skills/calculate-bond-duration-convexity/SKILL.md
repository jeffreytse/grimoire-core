---
name: calculate-bond-duration-convexity
description: Use when assessing how sensitive a bond or bond portfolio's price is to a change in interest rates — calculating duration as the first-order approximation of price sensitivity and convexity as the correction for how that sensitivity itself changes as rates move, rather than assuming a bond's rate sensitivity is constant regardless of the size of the rate change.
source: Frederick Macaulay, "Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856" (1938) — Macaulay duration; standard fixed-income risk literature
tags: [finance, investing, duration, convexity, interest-rate-risk, fixed-income, bond-risk]
related: [design-bond-ladder, apply-active-bond-total-return-management, calculate-value-at-risk]
---

# Calculate Bond Duration and Convexity

Assess how sensitive a bond or bond portfolio's price is to a change in interest rates by calculating duration — the first-order approximation of price sensitivity to a small rate change — and convexity, the correction accounting for how that sensitivity itself changes as rates move further, rather than assuming a bond's interest-rate sensitivity remains constant regardless of the size of the rate change.

## Why This Is Best Practice

**Adopted by:** Frederick Macaulay introduced the duration concept in his 1938 study of interest rates and bond yields, and Macaulay duration (along with its modified-duration variant) has since become the standard measure of bond interest-rate sensitivity taught and applied throughout fixed-income investment practice, with convexity as its standard companion correction documented across fixed-income risk management literature.
**Impact:** Duration alone provides an accurate approximation of price sensitivity only for small interest-rate changes — for larger rate moves, the actual price change deviates from the duration-based linear approximation, and this deviation (convexity) can be substantial for longer-duration bonds or bonds with embedded options, meaning a risk assessment based on duration alone can meaningfully understate or overstate actual price sensitivity for larger rate moves.
**Why best:** Treating a bond's interest-rate sensitivity as a single constant figure (duration alone) ignores that this sensitivity itself changes as rates move — convexity specifically captures this second-order effect, and combining both measures produces a substantially more accurate estimate of a bond's actual price behavior across a realistic range of rate-change scenarios than duration alone would provide.

Sources: Macaulay, "Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856" (1938); standard fixed-income risk management literature on duration and convexity

## Steps

### Step 1: Calculate the bond or portfolio's duration

Calculate duration — the weighted average time until the bond's cash flows are received (Macaulay duration), or its more directly usable variant, modified duration, which approximates the percentage price change for a given small change in yield — as the starting point for assessing interest-rate sensitivity.

### Step 2: Use duration to estimate price impact for a given rate change

Use the calculated duration figure to estimate the approximate percentage price change the bond or portfolio would experience for a given, relatively small change in interest rates — recognizing this estimate is a linear approximation that becomes less accurate as the size of the assumed rate change grows.

### Step 3: Calculate convexity to capture the correction for larger rate moves

Calculate convexity — a measure of how the bond's duration itself changes as rates move — as a second-order correction that captures a bond's actual price behavior more accurately than duration alone, particularly for larger rate changes where the duration-only linear approximation diverges most from actual price behavior.

### Step 4: Combine duration and convexity for a more accurate price-sensitivity estimate

Combine the duration-based linear estimate with the convexity correction to produce a more accurate estimate of the bond or portfolio's actual price change for a given rate move — particularly important for longer-duration bonds, larger assumed rate changes, or bonds with embedded options (callable or puttable bonds) where convexity effects can be pronounced or even negative.

### Step 5: Use combined duration-convexity analysis to inform portfolio interest-rate positioning

Use the resulting duration and convexity figures to inform portfolio-level interest-rate positioning decisions — assessing whether the portfolio's current interest-rate sensitivity matches the investor's actual rate view and risk tolerance (see `apply-active-bond-total-return-management` for how this analysis feeds into active duration positioning decisions).

## Rules

- Calculate both duration and convexity together, not duration alone, particularly when assessing sensitivity to larger potential rate changes.
- Recognize duration as a linear approximation that becomes less accurate as the assumed rate change grows in size.
- Pay particular attention to convexity for bonds with embedded options (callable or puttable bonds), where convexity can behave differently (including negative convexity) than for straightforward option-free bonds.
- Use the combined duration-convexity analysis to inform deliberate interest-rate positioning decisions, not merely as a reporting exercise.

## Examples

**Convexity correction improving accuracy for a large rate move:** An analyst estimates a bond's price change for a substantial interest-rate increase using duration alone, then recalculates including the convexity correction. The convexity-adjusted estimate proves meaningfully more accurate against the bond's actual subsequent price behavior, illustrating why duration alone is insufficient for larger rate moves.

**Negative convexity in a callable bond (illustrative caution):** A different analysis involves a callable bond, which can exhibit negative convexity in falling-rate environments (its price appreciation is capped because the issuer becomes more likely to call and refinance the bond). Failing to account for this embedded option's effect on convexity would overstate the bond's price appreciation potential in a rate-decline scenario.

## Common Mistakes

- **Relying on duration alone without calculating convexity, especially for larger assumed rate changes** — this understates the actual sensitivity difference for larger moves, since duration is only a linear approximation.
- **Applying standard convexity assumptions to bonds with embedded options** — callable and puttable bonds can exhibit meaningfully different (including negative) convexity behavior that a standard calculation for option-free bonds would miss.
- **Treating duration as a static figure that doesn't need recalculation as the bond's characteristics or market rates change** — duration itself changes as the bond ages and as rates move, requiring periodic recalculation.
- **Failing to connect duration-convexity analysis to actual portfolio positioning decisions** — the analysis should directly inform whether the portfolio's rate sensitivity matches the investor's actual view and risk tolerance.

## When NOT to Use

- For a very short-duration instrument (e.g., a money-market instrument) where interest-rate sensitivity is minimal and the calculation effort provides little incremental risk-management value.
- As a substitute for credit-risk analysis — duration and convexity address interest-rate risk specifically, not the separate risk of the issuer's ability to pay (see `audit-counterparty-credit-risk` for that distinct risk dimension).
- For an equity or non-fixed-income asset — duration and convexity are specifically fixed-income concepts and don't directly translate to other asset classes.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
