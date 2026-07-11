---
name: apply-index-fund-investing
description: Use when choosing between actively managed funds and low-cost index funds, or building a simple diversified portfolio from a small number of funds — e.g., "should I pick stocks or index funds?", "what is a three-fund portfolio?", "active vs passive investing"
source: John Bogle, "The Little Book of Common Sense Investing" (2007); S&P Dow Jones Indices SPIVA (S&P Indices Versus Active) scorecards
tags: [finance, investing, index-funds, passive-investing, low-cost, diversification]
related: [design-portfolio-allocation, audit-investment-fees, calculate-compound-interest]
---

# Apply Index Fund Investing

Default to low-cost, broadly diversified index funds over actively managed funds or individual stock-picking for the core of a portfolio — because the evidence that active management persistently beats index benchmarks after fees is weak, while the cost advantage of passive investing compounds reliably over decades.

## Why This Is Best Practice

**Adopted by:** John Bogle founded Vanguard on this principle in 1975 and it has since become the default recommendation of nearly every major independent personal-finance educator and a large share of financial advisors. S&P Dow Jones Indices publishes the SPIVA (S&P Indices Versus Active) scorecard annually, tracking what percentage of actively managed funds beat their benchmark index — the data has driven a multi-decade, industry-wide shift of assets from actively managed funds into low-cost index funds and ETFs.
**Impact:** SPIVA's persistent finding, repeated across nearly every reporting period since the scorecard began, is that a large majority of actively managed U.S. equity funds — commonly 80–90% depending on category and time horizon — underperform their benchmark index over 10-to-15-year periods after fees. This isn't a claim that no manager ever beats the market in a given year; it's that identifying in advance which manager will do so persistently, net of fees, has not been reliably achievable at the population level.
**Why best:** Active management's central problem isn't that skilled managers don't exist — it's that fees are certain and paid regardless of performance, while outperformance is uncertain and, in aggregate, has consistently failed to overcome those fees for most funds over long horizons. Index investing sidesteps the problem of having to correctly identify outperforming managers in advance by capturing the market's return directly, at a fraction of the cost, which compounds into a substantial advantage over a multi-decade holding period (see `calculate-compound-interest` for how seemingly small fee differences compound).

Sources: Bogle, "The Little Book of Common Sense Investing" (2007); S&P Dow Jones Indices, SPIVA U.S. Scorecard (published annually, spglobal.com)

## Steps

### Step 1: Default to low-cost index funds for the core of the portfolio

Unless there's a specific, evidence-based reason otherwise (see Step 4), build the core equity and bond allocation from broad-market index funds or ETFs rather than actively managed funds or individual stock picks. "Broad market" means funds tracking a wide index (total U.S. stock market, total international stock market, total bond market) rather than a narrow sector or thematic index.

### Step 2: Prioritize expense ratio as a primary, not secondary, selection criterion

Among index funds tracking the same or a very similar index, expense ratio is one of the few genuinely predictive factors for future relative performance — a lower-cost fund tracking the same index will, almost by definition, deliver a return closer to the index's actual return. Use `audit-investment-fees` to compare expense ratios across fund options before selecting one.

### Step 3: Build a simple portfolio from a small number of broad funds

A common minimal implementation — the "three-fund portfolio" — uses a total U.S. stock market index fund, a total international stock market index fund, and a total bond market index fund, combined in whatever proportion matches the target asset allocation (see `design-portfolio-allocation`). Additional funds add complexity and potential overlap without a corresponding diversification benefit once these three broad categories are covered.

### Step 4: Reserve active management for situations with a specific, evidence-based rationale

Active management has a more defensible case in less efficient market segments (some emerging markets, certain fixed-income niches, or small-cap/micro-cap segments with less analyst coverage) than in broad, highly covered public equity markets like large-cap U.S. stocks. If choosing active management, require a specific rationale tied to market inefficiency in that particular segment — not a general belief that active management works, given the SPIVA evidence to the contrary in broad markets.

### Step 5: Hold the position through market cycles rather than switching funds based on recent performance

Chasing whichever fund had the best recent returns — whether active or passive — undermines the entire premise of low-cost, long-horizon investing. Once a low-cost, broadly diversified fund selection is made, changing it should be driven by a change in the investor's actual asset allocation needs, not by recent relative performance.

## Rules

- Default to low-cost index funds for the core portfolio; require a specific, evidence-based rationale (not general belief) to deviate into active management for any given market segment.
- Treat expense ratio as a primary selection factor among comparable index funds — it is one of the most reliably predictive metrics available for a fund choice.
- Don't multiply funds unnecessarily — three or four broad-market funds typically provide sufficient diversification; adding more funds without a specific gap they fill increases complexity without benefit.
- Never switch fund selection based on recent relative performance — that reintroduces the market-timing/performance-chasing problem index investing is meant to avoid.

## Examples

**Three-fund portfolio, new investor:** A first-time investor with no strong view on specific sectors or countries builds their entire portfolio from three funds: a total U.S. stock market index fund, a total international stock market index fund, and a total bond market index fund, weighted according to their target allocation. This achieves broad diversification at minimal cost with no requirement to select individual securities or actively managed funds.

**Selective active allocation with rationale:** An investor otherwise indexed broadly chooses an actively managed fund for a small allocation to a specific emerging-market segment with historically lower analyst coverage and less efficient pricing — a deliberate, bounded exception with a specific rationale, not a wholesale rejection of the indexing default.

## Common Mistakes

- **Chasing last year's best-performing fund** — switching into whichever active fund had the best recent returns (survivorship-biased and unlikely to persist) undermines the discipline that makes low-cost indexing effective in the first place.
- **Treating a low expense ratio as sufficient without checking index breadth** — a low-cost fund tracking a narrow or concentrated index is not the same as a low-cost fund tracking a broad market; check what the fund actually holds, not just its cost.
- **Over-diversifying across many overlapping funds** — holding numerous funds that all substantially overlap in underlying holdings adds complexity and rebalancing overhead without a real diversification benefit.
- **Using "active vs. passive" as an all-or-nothing decision without segment-specific reasoning** — the strength of the evidence for indexing varies by market segment; applying a blanket rule without considering where active management has a more defensible case oversimplifies the decision.

## When NOT to Use

- When the specific market segment has good evidence of persistent, fee-adjusted active outperformance (some niche fixed-income or genuinely under-covered small-cap segments) — the broad-market SPIVA evidence doesn't apply equally to every corner of the investable universe.
- When the investor has a specific, well-reasoned thesis about an individual company or sector and is investing risk capital they can afford to lose beyond their core diversified portfolio — that's a distinct, bounded activity from the core-portfolio construction this skill addresses.
- When choosing the target asset allocation itself (stock/bond mix, domestic/international split) — see `design-portfolio-allocation`; this skill addresses fund selection within a chosen allocation, not the allocation decision itself.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
