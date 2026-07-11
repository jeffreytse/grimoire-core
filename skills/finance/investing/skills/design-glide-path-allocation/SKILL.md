---
name: design-glide-path-allocation
description: Use when setting an asset allocation that should shift over time as an investor approaches a target date (retirement, tuition, major purchase) — e.g., "how should my allocation change as I age?", "target-date fund glide path", "how conservative should I get near retirement?"
source: Vanguard, Fidelity, and T. Rowe Price target-date fund glide-path methodology whitepapers; "to" vs. "through" retirement glide path design literature
tags: [finance, investing, glide-path, target-date, asset-allocation, retirement-planning]
related: [design-portfolio-allocation, design-rebalancing-strategy, calculate-fire-number]
---

# Design Glide Path Allocation

Define how an asset allocation shifts from growth-oriented toward capital-preservation as an investor approaches a target date — rather than holding a single static allocation indefinitely or making ad-hoc de-risking decisions as the date approaches.

## Why This Is Best Practice

**Adopted by:** Every major target-date fund family (Vanguard Target Retirement, Fidelity Freedom, T. Rowe Price Retirement) is built around a published glide path — a predetermined schedule of how equity/bond allocation shifts by age or years-to-target. These are among the most widely held retirement investment vehicles in defined-contribution plans, meaning glide-path investing is already the de facto default for a large share of retirement savers, whether or not they've thought about it explicitly.
**Impact:** A static allocation held unchanged from early career through retirement either carries too much equity risk into the years just before/after retirement — when a market downturn does the most damage due to reduced ability to recover before withdrawals begin — or carries too little growth exposure during the decades when the investor could most afford volatility. Glide-path design directly addresses sequence-of-returns risk: the same average return delivered in a different order (a downturn right before or during early retirement withdrawals) can deplete a portfolio meaningfully faster than if the downturn had occurred decades earlier.
**Why best:** The alternative — a fixed allocation forever, or discretionary "get more conservative when it feels right" decisions — either ignores the fact that risk capacity genuinely changes over a saving-and-spending lifecycle, or introduces the exact behavioral timing risk this skill is meant to avoid. A predetermined glide path decided in advance shifts the allocation systematically as the target date approaches, independent of market conditions or emotional state at any single point in time.

Sources: Vanguard Target Retirement glide-path methodology; Fidelity Freedom Fund glide-path design papers; T. Rowe Price "to" vs. "through" retirement glide path research

## Steps

### Step 1: Choose the glide path's target date and philosophy

Establish the target date (e.g., a specific retirement year, a tuition due date) and choose between a "to" glide path (equity allocation continues declining up to the target date and then holds flat, appropriate when a large portion of assets will be spent down shortly after the target date) and a "through" glide path (equity allocation continues declining gradually for years past the target date, appropriate when assets need to last decades further, as in a long retirement funded primarily by the portfolio itself).

### Step 2: Set the starting and ending allocation points

Define the equity/bond split at the far end of the glide path (e.g., 90% equity decades from the target date) and at or near the target date (e.g., 30–50% equity at retirement, depending on the "to" vs. "through" choice and the investor's other income sources like a pension or Social Security). These two endpoints, plus the chosen shape of the path between them, define the whole glide path.

### Step 3: Define the shift schedule between the endpoints

Specify how allocation moves between the two endpoints — commonly a roughly linear reduction in equity percentage per year as the target date approaches, though many published glide paths flatten the rate of change in the final years before the target date rather than a strictly straight line. Document this schedule explicitly rather than leaving the pace of de-risking to be decided each year in the moment.

### Step 4: Account for other income sources when setting how conservative the endpoint should be

An investor with a pension or other guaranteed income source can typically sustain a higher equity allocation at retirement than one relying entirely on portfolio withdrawals, since their fixed-cost coverage is already provided independent of portfolio performance. Adjust the glide path's target-date endpoint based on this, rather than using a generic age-based target-date fund's assumptions that may not match the specific investor's income situation.

### Step 5: Rebalance to the glide path's current-year target on a regular schedule

The glide path itself only defines what the target allocation should be at each point in time — actually executing the shift requires periodic rebalancing (see `design-rebalancing-strategy`) to bring the portfolio to that year's target. A glide path that's designed but never executed via rebalancing doesn't actually de-risk the portfolio on schedule.

## Rules

- Decide the glide path's shape and endpoints in advance, while calm — don't decide how much to de-risk in the moment, especially not in response to recent market performance.
- Choose "to" vs. "through" deliberately based on how quickly assets will be spent down after the target date, not by default.
- Account for other income sources (pension, Social Security, rental income) when setting the target-date endpoint — a generic age-based glide path may be more conservative than a specific investor's situation actually requires.
- Execute the glide path through actual rebalancing on a regular schedule — a documented glide path that isn't implemented provides no real risk reduction.

## Examples

**"To" retirement glide path:** An investor planning to annuitize a large portion of their portfolio at retirement to fund fixed expenses builds a "to" glide path: 90% equity at 30 years from retirement, declining roughly linearly to 40% equity at the retirement date, then holding flat — since most of the growth-phase risk-taking is done by the time the annuitization occurs.

**"Through" retirement glide path:** An investor expecting a 30-year retirement funded primarily by portfolio withdrawals builds a "through" glide path: 90% equity decades out, reaching 50% equity at retirement, and continuing to gradually decline to 30% equity over the subsequent 15 years of retirement — since the portfolio needs to keep growing to outlast a long withdrawal period, just with reduced volatility as sequence-of-returns risk becomes most acute in the initial retirement years.

**Adjusting for a pension:** An investor with a substantial pension covering most fixed living expenses in retirement sets a less conservative target-date endpoint (60% equity, versus the 40% a generic target-date fund of the same vintage might use), since their essential expenses are already covered independent of portfolio performance and they can tolerate more portfolio volatility.

## Common Mistakes

- **Holding a static allocation from early career through retirement** — ignores that risk capacity and the consequences of a downturn change meaningfully over the saving-and-spending lifecycle, especially the outsized damage a downturn does in the years immediately before/after the target date.
- **De-risking reactively based on recent market performance** — cutting equity exposure because of a recent downturn (rather than because the glide path schedule called for it) is behavioral market-timing wearing a risk-management label.
- **Using a generic age-based target-date fund without checking whether its assumptions fit** — a target-date fund's glide path is built for an average investor profile; an investor with a pension, unusually high risk tolerance, or an unusually long or short retirement horizon may need a materially different glide path.
- **Designing a glide path but never rebalancing to it** — a documented schedule with no execution mechanism doesn't actually reduce risk on schedule; see `design-rebalancing-strategy` for the execution step.

## When NOT to Use

- When there is no specific target date the allocation needs to shift toward — a static, long-horizon allocation with no defined endpoint is a `design-portfolio-allocation` question, not a glide-path one.
- When a commercial target-date fund's published glide path already closely matches the investor's actual income situation and risk tolerance — building a custom glide path adds complexity without benefit if the off-the-shelf option already fits.
- For the near-target-date portion of the plan where predictable cash flow, not further allocation shifting, is the goal — see `design-bond-ladder` for structuring the fixed-income portion once the glide path has reached its conservative endpoint.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
