---
name: apply-lean-startup-methodology
description: Use when a validated problem is ready to move into building — deciding what minimum viable product to build first, what to measure to test whether it actually solves the problem, and whether to pivot or persevere — bridging the gap between problem-validation interviews and post-launch growth experimentation.
source: Eric Ries, "The Lean Startup" (Crown Business, 2011); Steve Blank, "The Four Steps to the Epiphany" (2005); documented case studies including IMVU, Dropbox, and Zappos
tags: [lean-startup, mvp, validated-learning, pivot, entrepreneurship, product-development, innovation-accounting]
related: [run-customer-discovery, run-growth-experiment, apply-probe-strategy, write-business-plan, apply-product-market-fit-test]
---

# Apply Lean Startup Methodology

Run the Build-Measure-Learn loop — build the smallest possible product that tests a specific hypothesis, measure whether it produces real validated learning, and decide explicitly whether to pivot or persevere — rather than building a full product on faith before any real usage data exists.

## Why This Is Best Practice

**Adopted by:** Eric Ries developed the methodology from his experience at IMVU; it has since become standard startup-building practice, taught at Y Combinator and Stanford, and credited in the growth of companies including Dropbox (whose MVP was a demo video, not a working product) and Zappos (whose MVP was Nick Swinmurn manually photographing shoes at local stores and fulfilling orders by hand before building any inventory system).

**Impact:** Ries documented IMVU's own pivot history as the origin case: repeated small, cheap experiments redirected the product away from a doomed initial direction toward one that found real traction, at a fraction of the cost of building the originally planned full feature set. Dropbox's MVP video, rather than a built product, is documented to have grown its beta waitlist from 5,000 to 75,000 signups overnight — validating demand before writing the storage-sync infrastructure.

**Why best:** This fills a specific gap between two adjacent practices already in use. `run-customer-discovery` validates that a problem is real and worth solving, then explicitly stops once there are "paying customers and usage data." `run-growth-experiment` optimizes an existing live product's funnel metrics, assuming real traffic already exists. Neither covers the step in between: what to actually build first, at what scope, and how to measure whether it produced real learning rather than vanity signals — the Build-Measure-Learn loop, with its own vocabulary (MVP types, innovation accounting, the pivot taxonomy) that this bridges.

Sources: Ries, *The Lean Startup* (2011); Blank, *The Four Steps to the Epiphany* (2005); documented IMVU, Dropbox, and Zappos case histories.

## Steps

1. **State the riskiest assumption as a falsifiable hypothesis.** Before building anything, identify the single assumption that, if wrong, breaks the whole business — not a minor detail. Format it so it can be proven false: "We believe [customer segment] will [specific behavior] because [reason]."

2. **Choose the cheapest MVP type that tests that specific hypothesis.** Match the MVP to what's actually being tested, not to what's easiest to build in general:
   - **Concierge MVP** — manually deliver the service by hand (Zappos: buy shoes at retail, ship them personally) to test whether people want the outcome at all before building any automation.
   - **Wizard-of-Oz MVP** — a front end that looks automated but is operated manually behind the scenes, to test the user experience before building the real backend.
   - **Landing-page / smoke-test MVP** — a page describing the product with a signup or purchase call-to-action, to test demand before building the product itself (Dropbox's explainer video).
   - **Single-feature MVP** — build only the one feature central to the hypothesis, omitting everything else the eventual product will need.

3. **Define the specific metric that would prove the hypothesis false.** Vanity metrics (raw signups, page views, downloads) don't count — pick a metric tied directly to the hypothesized behavior (conversion to paid, repeat usage, a specific action taken unprompted).

4. **Run innovation accounting.** Track the metric across three checkpoints: establish the baseline from the current MVP, tune the product toward the ideal, and decide pivot-or-persevere based on whether the metric is actually moving toward the ideal — not based on whether it moved at all.

5. **Decide pivot or persevere explicitly, on a schedule.** Set a checkpoint in advance (a date or a data threshold) to force the decision rather than drifting indefinitely. If persevering, continue with the current hypothesis; if pivoting, change one structural element while keeping the rest constant — common pivot types include customer segment (same problem, different customer), customer need (same customer, different problem), zoom-in (one feature becomes the whole product), zoom-out (the whole product becomes one feature of something larger), platform, business model (e.g., subscription to one-time), value-capture/monetization, engine of growth (viral vs. paid vs. sticky), channel, and technology.

6. **Repeat the loop, not just once.** Each cycle should be as short as the hypothesis allows — the loop is meant to run many times cheaply, not once expensively.

## Rules

- The riskiest assumption gets tested first — testing an easy, low-risk assumption because it's convenient wastes the cycle's value.
- Match MVP type to the specific hypothesis being tested — a concierge MVP tests desirability, not scalability; don't draw scalability conclusions from it.
- Set the pivot-or-persevere checkpoint in advance — deciding it after seeing the data invites motivated reasoning.
- A pivot changes one structural element while holding others constant — changing everything at once destroys the ability to attribute what worked.

## Examples

**Trigger:** A validated customer-discovery process confirmed the problem is real, but there's no product yet and no capital to build the full planned feature set.
→ State the riskiest assumption (e.g., "customers will pay for automated X" vs. "customers just want X done, regardless of automation"). Run a concierge MVP: deliver the outcome manually to a handful of customers. Measure willingness to pay and repeat usage, not just interest. Set a two-week checkpoint to decide whether to build the automated version or pivot the underlying assumption.

**Trigger:** A team has been iterating on a product feature for months with steadily increasing raw signups but no growth in paid conversion.
→ Recognize raw signups as a vanity metric relative to the actual hypothesis (willingness to pay). Re-run innovation accounting against the metric that matters, and treat the flat conversion trend as evidence to consider a pivot rather than continuing to optimize a number that was never the real test.

## Common Mistakes

- **Building a fuller product than the hypothesis requires.** The MVP only needs to be as complete as what's necessary to test the specific riskiest assumption — anything beyond that is wasted build time before real learning exists.
- **Measuring vanity metrics instead of validated learning.** Signups, downloads, and page views can rise while the actual hypothesis about paid demand or retained usage remains untested.
- **Never setting a pivot-or-persevere checkpoint, so the team drifts indefinitely on the same unproven hypothesis.** Without a forced decision point, sunk cost keeps the team iterating on a direction the data already argues against.
- **Pivoting on everything at once.** Changing customer segment, pricing, and core feature simultaneously destroys the ability to tell which change actually mattered.

## When NOT to Use

- Before the underlying problem itself has been validated — run `run-customer-discovery` first; building any MVP against an unvalidated problem just moves the same risk downstream.
- Once a product already has real paying customers and usage data at scale — shift to `run-growth-experiment`'s funnel-optimization framework, which is built for that stage.
- Compliance-driven, regulatory, or safety-critical builds that must meet a fixed specification regardless of validated learning — an MVP that deliberately omits required safety or compliance features to move faster is not an acceptable trade-off in these contexts.
