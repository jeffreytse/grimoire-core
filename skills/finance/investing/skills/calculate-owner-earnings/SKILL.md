---
name: calculate-owner-earnings
description: Use when assessing a company's true distributable cash-generating power for valuation purposes — calculating owner earnings (reported earnings adjusted for maintenance capital expenditures) rather than relying on GAAP net income alone.
source: Warren Buffett, Berkshire Hathaway Shareholder Letters (1986, formal introduction of the "owner earnings" concept)
tags: [finance, investing, owner-earnings, valuation, cash-flow, buffett]
related: [calculate-dcf, audit-investment-thesis, audit-management-capital-allocation]
---

# Calculate Owner Earnings

Calculate owner earnings — reported earnings adjusted for the capital expenditures actually required to maintain the business's competitive position and unit volume — as a truer measure of a company's distributable cash-generating power than GAAP net income alone.

## Why This Is Best Practice

**Adopted by:** Warren Buffett formally introduced the owner-earnings concept in Berkshire Hathaway's 1986 shareholder letter, explicitly defining it as a more accurate representation of a business's true earning power than reported net income, and has used it as a central valuation input throughout Berkshire's investment process since. The concept has since been adopted broadly across value-investing education and professional equity analysis as a standard adjustment to reported earnings.
**Impact:** GAAP net income can materially overstate a capital-intensive business's true distributable cash by using a depreciation schedule that understates the capital actually required to maintain the business's competitive position and unit volume over time — a business can report steady or growing net income while requiring ever-larger capital expenditures just to stand still competitively, a distinction reported net income alone does not surface. Owner earnings makes this adjustment explicit, producing a cash-flow figure closer to what could genuinely be distributed to owners without degrading the business.
**Why best:** Reported net income is a GAAP accounting construct subject to depreciation policy choices, non-cash charges, and other conventions that don't necessarily track the actual cash a business could sustainably distribute to its owners while maintaining its competitive position. Owner earnings strips away this gap by explicitly separating maintenance capital expenditure (required just to stay competitive) from growth capital expenditure (optional, expansion-oriented spending), giving a cleaner input to any valuation model.

Sources: Berkshire Hathaway Shareholder Letters (Buffett, 1986 and recurring, berkshirehathaway.com)

## Steps

### Step 1: Start from reported net income

Begin with the company's GAAP net income as the starting point — this is the baseline that will be adjusted, not the final figure.

### Step 2: Add back depreciation, depletion, amortization, and other non-cash charges

Add back the non-cash charges already subtracted in arriving at net income (depreciation, depletion, amortization, and any other significant non-cash items) — these reduced reported earnings without representing an actual cash outflow in the current period.

### Step 3: Subtract maintenance capital expenditures — not total capital expenditures

Estimate the capital expenditure genuinely required to maintain the business's current competitive position and unit sales volume — distinct from capital expenditure aimed at growth or expansion. This is the step requiring the most judgment: a business's reported total capex figure often blends maintenance and growth spending together, and separating them requires understanding the specific business's capital cycle (e.g., what does it cost each year just to replace aging equipment and maintain existing capacity, versus what's being spent to add new capacity or enter new markets).

### Step 4: Adjust for any other item that distorts true distributable cash

Normalize for any other significant item that causes reported earnings to diverge from true distributable cash — for example, unusually large or small working-capital swings, one-time charges or gains unrelated to ongoing operations, or stock-based compensation if it represents a genuine dilutive cost not otherwise captured.

### Step 5: Use the resulting owner-earnings figure as the cash-flow input to valuation

Feed the owner-earnings estimate into a discounted cash flow model (see `calculate-dcf`) or as the basis for a thesis's return expectations (see `audit-investment-thesis`), rather than using reported net income directly — owner earnings is meant to replace, not supplement, net income as the valuation-relevant cash-flow figure.

## Rules

- Never conflate total capital expenditure with maintenance capital expenditure — the distinction between spending to stay competitive and spending to grow is the entire point of the owner-earnings adjustment.
- Require a specific, reasoned estimate of maintenance capex rather than an arbitrary rule of thumb — the estimate should reflect the specific business's actual capital cycle and competitive requirements.
- Treat owner earnings as a replacement for, not a supplement to, GAAP net income in valuation work — using both without reconciling them produces an inconsistent analysis.
- Re-estimate maintenance capex periodically as the business's capital intensity changes — a business's maintenance capital requirements are not static over a long holding period.

## Examples

**Capital-intensive business with understated depreciation:** A manufacturing company reports steady net income, but its depreciation schedule assumes equipment lasts longer than it actually does in practice, understating the true annual cost of maintaining production capacity. An owner-earnings calculation that estimates realistic maintenance capex (higher than the reported depreciation charge) reveals a lower true distributable cash figure than net income alone suggests — a material difference for valuation purposes.

**Asset-light business with owner earnings close to net income:** A software or services business with minimal physical capital requirements has maintenance capex that is small relative to net income, so its owner earnings figure is close to reported net income after adding back modest non-cash charges — illustrating that the owner-earnings adjustment matters most for capital-intensive businesses and less for asset-light ones.

## Common Mistakes

- **Using total capital expenditure instead of estimating maintenance capex specifically** — this understates owner earnings for growing businesses (where much of capex is genuinely growth-oriented, not maintenance) and can overstate it for businesses masking maintenance needs as "growth" spending.
- **Skipping the estimate because it requires judgment** — the maintenance-vs-growth capex distinction is inherently an estimate, not a precise line item most companies report separately; avoiding the estimate because it's imprecise discards the entire value of the adjustment.
- **Using owner earnings for one valuation and net income for another without reconciling** — mixing the two inconsistently across an analysis produces a confused, internally inconsistent result.
- **Treating owner earnings as unnecessary for asset-light businesses** — while the adjustment matters less for low-capital-intensity businesses, checking that it's genuinely small (rather than assuming it) still matters.

## When NOT to Use

- For a business with capital expenditure so minimal that the owner-earnings adjustment would not meaningfully differ from net income — the extra estimation effort isn't worthwhile if the answer is unlikely to change.
- When a reliable, already-adjusted free cash flow figure is available from a source that has already made a comparable maintenance-capex distinction — recalculating from scratch may be redundant if the adjustment has already been done credibly.
- For a business whose capital cycle is genuinely unpredictable or highly irregular, making any maintenance-capex estimate more speculative than informative — in that case, disclose the uncertainty explicitly rather than presenting an owner-earnings figure with false precision.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
