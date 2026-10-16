---
name: apply-product-market-fit-test
description: Use when deciding whether a startup has found product-market fit before investing in growth, sales, or scaling — survey active users with Sean Ellis's "how would you feel if you could no longer use this product" question and treat 40%+ answering "very disappointed" as the threshold, rather than relying on founder intuition or vanity metrics, because premature scaling before this threshold is met is the leading documented cause of early-stage startup failure.
source: 'Sean Ellis, "Find Your Product/Market Fit Before Scaling", Startup-Marketing.com (2009) — the 40% test; Marc Andreessen, "The Only Thing That Matters", pmarca blog (2007) — qualitative definition and symptoms of product-market fit; Marmer, Herrmann, Dogrultan & Berman, "Startup Genome Report", Startup Genome (2011) — premature scaling as the leading documented cause of startup failure'
tags: [startup, product-market-fit, entrepreneurship, growth, lean-startup]
related: [apply-lean-startup-methodology, run-customer-discovery, apply-market-size-first-screening]
---

# Apply Product-Market Fit Test

Survey active users with Sean Ellis's "how would you feel if you could no longer use this product" question and treat 40%+ answering "very disappointed" as the threshold before investing in growth, sales, or scaling — rather than relying on founder intuition or vanity metrics — because premature scaling before this threshold is met is the leading documented cause of early-stage startup failure.

## Why This Is Best Practice

**Sean Ellis, "Find Your Product/Market Fit Before Scaling" (2009):** Developed a standardized survey — asking active users "How would you feel if you could no longer use [product]?" with options Very disappointed / Somewhat disappointed / Not disappointed / N/A — and established, through testing across many startups he advised, that a result of 40% or more answering "very disappointed" reliably distinguished companies ready to scale from those still needing product iteration.

**Marc Andreessen, "The Only Thing That Matters" (2007):** Provides the qualitative complement to Ellis's quantitative test — describing product-market fit as a state a founder can feel operationally: usage growing faster than the team can serve it, servers strained by organic demand, press and word-of-mouth pulling in customers without paid acquisition, and hiring struggling to keep pace with demand. Andreessen's essay argues market — not team or product execution alone — is the dominant variable in early-stage outcomes, and that fit with that market is legible through these observable symptoms.

**Marmer, Herrmann, Dogrultan & Berman, "Startup Genome Report" (2011):** A large-scale study of startup failure patterns identified premature scaling — hiring, spending on paid acquisition, or expanding operationally before validating fit — as the single most common documented cause of early-stage failure, and found it strongly correlated with skipping or ignoring a product-market fit check like Ellis's test.

**Why best:** Revenue growth, signup counts, and funding raised are frequently used as informal proxies for "the product is working," but none of them specifically measure whether users would suffer from the product's disappearance — which is the precise signal Ellis's test is built to surface, and the signal Andreessen's qualitative symptoms independently corroborate. A startup can show growth on vanity metrics while still lacking the underlying fit that makes further scaling investment pay off.

**Adopted by:** Widely used across Y Combinator-affiliated and broader startup ecosystems as a standard pre-scaling checkpoint; cited in Andreessen Horowitz's public commentary on evaluating portfolio companies' readiness to scale.
**Impact:** The Startup Genome Report's analysis of startup failure patterns found premature scaling to be the most common documented cause of early failure among the startups studied, specifically correlated with scaling decisions made without a product-market fit check in place.

## Steps

1. **Survey a sample of users who have had meaningful exposure to the core product experience** — not brand-new signups — using Ellis's exact question: "How would you feel if you could no longer use [product]?" with the four standard answer options.

2. **Calculate the percentage answering "very disappointed."** Treat 40% as the threshold: below it, product-market fit has not yet been reached, regardless of growth rate, revenue, or founder confidence in the product.

3. **Segment survey responses by cohort** (acquisition channel, use case, persona) rather than reading only the aggregate score. Ellis's method specifically recommends this because a below-40% aggregate result can still conceal an above-40% pocket — the true early-adopter segment worth focusing on rather than the market as a whole.

4. **Cross-check the survey result against Andreessen's qualitative symptoms of genuine fit** — usage outpacing your ability to serve it, organic press and word-of-mouth pulling in customers, hiring struggling to keep pace with demand. A survey score near the 40% line should be corroborated with these observable operational symptoms rather than treated as the sole signal.

5. **If below 40% (or the qualitative symptoms are absent), do not shift spend into growth or scaling channels.** Return to customer discovery and iterate on the product for the segment showing the strongest signal instead — scaling an unvalidated product accelerates the wrong outcome faster than it accelerates the right one.

6. **Re-run the test periodically as the product or target segment changes.** Passing the test once for an early version does not certify fit for a pivoted or expanded product — treat it as a recurring checkpoint, not a one-time certification.

## Rules

- Survey users who've had meaningful exposure to the core value proposition, not brand-new signups who haven't experienced it yet — testing too early produces a false negative.
- The 40% threshold is a floor, not a target — treat scores meaningfully above 40% as a stronger signal, and scores just above 40% as fragile rather than definitively solved.
- Segment before concluding from the aggregate — a below-40% aggregate can still conceal a real, servable early-adopter segment above it.
- Do not substitute vanity metrics (signups, downloads, funding raised) for this test — none of them measure whether users would suffer from the product's absence, which is the specific signal this test is designed to surface.

## Examples

**Segmented re-test after a weak aggregate score:** A B2B SaaS startup surveys 150 active users at week six; 25% answer "very disappointed." Rather than proceeding with a planned paid-acquisition campaign, the team segments responses by industry vertical and finds one vertical scoring 52% — they refocus product and go-to-market on that vertical instead of scaling broadly on an unvalidated aggregate.

**Qualitative corroboration near the threshold:** A consumer app's survey score sits at 38%, just below threshold, but its servers are consistently strained by organic growth and support is fielding more inbound requests than it can answer. Read together with the survey, these qualitative symptoms suggest fit is emerging in a way a single point-in-time survey doesn't yet fully capture, warranting a segment-level re-test rather than either premature scaling or premature abandonment.

## Common Mistakes

- **Scaling growth spend based on revenue or user-count growth alone**, without ever running the disappointment-survey test — the Startup Genome Report specifically identifies this pattern as the leading documented cause of early failure.
- **Surveying too early**, before users have had meaningful exposure to the core value proposition, producing a false-negative reading.
- **Treating a below-40% aggregate score as final without segmenting by cohort** — the true signal is often present in a specific segment, not absent from the product entirely.
- **Treating the test as a one-time gate rather than a recurring checkpoint** — a pivot or expansion invalidates a prior passing score.

## When NOT to Use

- Before the product has a working core experience for users to react to — there's nothing to survey yet; run `run-customer-discovery` interviews first.
- As the sole input for a scaling decision that also depends on unit economics, market size, or competitive dynamics — pair with `calculate-startup-unit-economics` and `apply-market-size-first-screening` rather than relying on the fit signal alone.
- In enterprise or long-sales-cycle B2B contexts with very small early user counts, where a 40%-of-N survey with fewer than roughly 10–15 respondents is too statistically noisy to be meaningful — supplement with qualitative account-level signals (renewal intent, expansion within account) instead.
