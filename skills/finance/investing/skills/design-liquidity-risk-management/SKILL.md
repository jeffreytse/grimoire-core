---
name: design-liquidity-risk-management
description: Use when managing a fund or portfolio that offers investors redemption rights — matching the redemption terms offered to investors against the actual liquidity of the underlying holdings, so the fund can meet redemption requests even during stressed market conditions without being forced into fire-sale liquidations.
source: Basel III Liquidity Coverage Ratio framework; U.S. Securities and Exchange Commission Investment Company Liquidity Risk Management Programs Rule (Rule 22e-4)
tags: [finance, investing, liquidity-risk, redemption-risk, fund-management, asset-liability-matching]
related: [design-fortress-balance-sheet-strategy, calculate-value-at-risk, design-portfolio-stress-test]
---

# Design Liquidity Risk Management

Match the redemption terms offered to a fund's investors against the actual liquidity of the fund's underlying holdings — so the fund can meet redemption requests even during stressed market conditions, without being forced into fire-sale liquidations of illiquid holdings at severely depressed prices to raise cash.

## Why This Is Best Practice

**Adopted by:** The Basel III framework requires banks to maintain a Liquidity Coverage Ratio ensuring sufficient high-quality liquid assets to survive a defined stress scenario, and the U.S. Securities and Exchange Commission's Investment Company Liquidity Risk Management Programs Rule (Rule 22e-4) requires registered funds offering daily redemption to formally classify their holdings' liquidity and manage redemption risk against that classification — both reflecting a regulatory consensus that liquidity risk is a distinct discipline requiring its own explicit management process, separate from market or credit risk.
**Impact:** A fund that offers investors liquid redemption terms (e.g., daily redemption) while holding illiquid underlying assets faces a specific structural mismatch — during a period of heavy redemption requests, the fund may be forced to sell its most liquid holdings first (leaving remaining investors holding a disproportionately illiquid portfolio) or sell illiquid holdings at a severe, forced-sale discount, either of which can disadvantage remaining investors or the fund's overall performance in ways that proper liquidity risk management specifically prevents.
**Why best:** A fund's market or credit risk assessment doesn't capture whether the fund can actually convert its holdings to cash on the terms it has promised investors — liquidity risk is a genuinely distinct dimension, since even a fund holding fundamentally sound assets can face a severe liquidity crisis if its promised redemption terms don't match how quickly and cheaply those assets can actually be sold, particularly during stressed market conditions when many funds may be trying to sell similar assets simultaneously.

Sources: Basel Committee on Banking Supervision, Basel III Liquidity Coverage Ratio framework; U.S. Securities and Exchange Commission, Investment Company Liquidity Risk Management Programs Rule (Rule 22e-4)

## Steps

### Step 1: Classify underlying holdings by actual liquidity

Classify each holding in the fund's portfolio by its actual liquidity — how quickly and at what price impact it could realistically be sold, particularly under stressed market conditions — rather than assuming all holdings are equally liquid or relying on a security's listed/traded status alone as a liquidity proxy.

### Step 2: Assess redemption terms against the classified liquidity profile

Assess whether the redemption terms offered to investors (daily, weekly, monthly, or with gates and notice periods) are actually matched to the fund's classified liquidity profile — a fund holding a meaningful proportion of illiquid assets while offering daily redemption carries a structural mismatch that this assessment is specifically designed to surface.

### Step 3: Maintain a liquidity buffer of readily convertible assets

Maintain a buffer of highly liquid assets sized to cover reasonably expected redemption activity, including a stressed scenario of elevated redemption requests, so that ordinary and moderately elevated redemption demand can be met without needing to sell less-liquid core holdings under pressure.

### Step 4: Establish redemption tools for genuinely severe liquidity stress

Establish, in advance, the tools available for genuinely severe liquidity stress — redemption gates, notice period extensions, or swing pricing (adjusting the redemption price to reflect the cost of liquidating to meet redemptions) — so these tools exist and are understood by investors before a crisis, rather than being improvised during an actual liquidity event.

### Step 5: Monitor liquidity risk on an ongoing basis, not only at fund launch

Monitor the fund's liquidity profile and redemption-term match on an ongoing basis as the portfolio's composition and market liquidity conditions change over time — a liquidity assessment accurate at fund launch can become mismatched as the fund's holdings or the broader market's liquidity conditions shift.

## Rules

- Classify holdings by actual, realistic liquidity — including under stressed conditions — not by listed/traded status alone.
- Match redemption terms offered to investors against the fund's actual classified liquidity profile, not set independently of it.
- Maintain a liquidity buffer sized to cover a reasonably stressed redemption scenario, not merely ordinary expected redemption activity.
- Establish redemption-management tools (gates, swing pricing) in advance of any actual liquidity crisis, not improvised during one.

## Examples

**Liquidity risk management preventing a forced fire sale:** A fund holding a mix of liquid and illiquid assets maintains a liquidity buffer and monitors its redemption-term match on an ongoing basis. During a period of unusually elevated redemption requests, the buffer and pre-established tools allow the fund to meet redemptions without being forced to sell illiquid core holdings at a severe discount, protecting remaining investors' interests.

**Liquidity mismatch exposed during stress (illustrative caution):** A different fund offers daily redemption while holding a substantial proportion of genuinely illiquid assets, without an adequate liquidity buffer or pre-established stress tools. During a period of heavy redemptions, the fund is forced to sell its most liquid holdings first, leaving remaining investors disproportionately exposed to the illiquid remainder — a structural mismatch proper liquidity risk management is specifically designed to prevent.

## Common Mistakes

- **Classifying holdings' liquidity based on listed/traded status alone rather than realistic, stress-scenario liquidity** — a security can be nominally "listed" while still being genuinely difficult to sell in size without significant price impact, especially under stress.
- **Setting redemption terms independent of the fund's actual liquidity profile** — offering more liquid redemption terms than the underlying holdings can genuinely support creates a structural mismatch that surfaces precisely during periods of stress.
- **Maintaining a liquidity buffer sized only for ordinary redemption activity, not a stressed scenario** — the buffer's real value is tested specifically during periods of elevated, not ordinary, redemption demand.
- **Waiting until an actual liquidity crisis to establish redemption-management tools** — gates, notice periods, and swing pricing mechanisms need to be established and understood by investors in advance to be usable and legally sound when actually needed.

## When NOT to Use

- For a fund with no investor redemption rights (e.g., a closed-end or fully locked-up vehicle) — liquidity risk in the sense addressed here specifically concerns the mismatch between promised redemption terms and underlying asset liquidity, which doesn't arise without redemption rights.
- For a fund holding exclusively highly liquid assets with no meaningful liquidity mismatch risk — the practice's overhead should be proportionate to the actual presence of a liquidity mismatch.
- As a substitute for market or credit risk assessment — liquidity risk is a distinct dimension from market risk (see `calculate-value-at-risk`) and credit risk (see `audit-counterparty-credit-risk`), and a fund needs all three assessed, not one in place of the others.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
