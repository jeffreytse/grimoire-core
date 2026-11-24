---
name: design-pagination-pattern
description: Use when a list, feed, search results page, or product grid has more items than fit on one screen and you must choose between numbered pagination, a "Load more" button, or infinite scrolling.
source: Nielsen Norman Group "Infinite Scrolling: When to Use It, When to Avoid It" and "Infinite Scrolling Tips"; Baymard Institute Product List & Search usability research (2016, updated 2024); Etsy infinite-scroll experiment (McKinley, "Design for Continuous Experimentation", 2012)
tags: [pagination, infinite-scroll, load-more, search-results, product-listing, content-feed, findability]
---

# Design Pagination Pattern

Choose how long lists load — pagination, "Load more", or infinite scroll — based on the user's task, then implement it so position, footer access, and accessibility are preserved.

## Why This Is Best Practice

**Adopted by:** Google Search (numbered pagination / continuous load with explicit boundaries), Amazon search (pagination), Instagram, X and TikTok feeds (infinite scroll), most large e-commerce category pages following Baymard guidance ("Load more"). NN/g and Baymard both publish task-based selection rules rather than a single winner.
**Impact:** Baymard's e-commerce testing found users browsed far fewer products with pagination than with "Load more" or infinite scroll, and recommends never using infinite scroll for search results. Etsy's A/B test of infinite scroll on search (2012) produced fewer item clicks and fewer purchases than pagination — the test was rolled back.
**Why best:** Each pattern fails in a predictable context: infinite scroll breaks goal-directed finding, footers, and returning to position; pagination adds interruptions to browsing. Choosing by task avoids both failure modes instead of defaulting to whichever is fashionable.

Sources: nngroup.com/articles/infinite-scrolling-tips; baymard.com/blog/external-load-more-vs-pagination-vs-infinite-scrolling; McKinley (2012) Etsy

## Steps

### 1. Classify the user's task

| Task type | Example | Recommended pattern |
|-----------|---------|---------------------|
| **Goal-directed finding / comparing** | Search results, admin tables, documentation lists | Numbered pagination |
| **Browsing a bounded set** | E-commerce category, image gallery | "Load more" button |
| **Open-ended streaming consumption** | Social feed, news stream, chronological activity | Infinite scroll |
| **Data tables with sort/filter** | Orders, users, logs | Pagination with page-size selector (see `design-data-tables`) |

If the page has a footer users need (contact, legal, help links), do not use pure infinite scroll.

### 2. Implement numbered pagination well

- Show: Previous, first, current ±1–2, last, Next. Hide middle pages behind "…".
- Highlight the current page; make the whole number a ≥24×24 px target.
- Reflect the page in the URL (`?page=3`) so Back, bookmarks, and sharing work.
- On page change, scroll to the top of the results and move focus to the results heading.
- Show the range: "Showing 41–60 of 1,248 results".

### 3. Implement "Load more" well

- Load a sensible default batch (Baymard: roughly 25–50 items for product lists on desktop, fewer on mobile).
- Show progress: "Showing 48 of 312 — Load more".
- Append items below; keep keyboard focus on the first newly loaded item.
- Persist loaded count in the URL or history state so Back returns users to the same position.
- Optionally auto-load 1–2 batches on scroll, then switch to the button (hybrid).

### 4. Implement infinite scroll well (only when step 1 allows)

- Preserve scroll position on Back (restore state or use history API).
- Show a loading indicator at the bottom; never a blank gap.
- Provide an end-of-list message ("You're all caught up").
- Move the footer content elsewhere (sidebar, menu) or stop auto-loading after N batches.
- Use `role="feed"` with `aria-setsize`/`aria-posinset` on articles, and announce new content via a polite live region (see `apply-aria-live-regions`).
- Keyboard users must be able to skip past the feed (skip link or landmark).

### 5. Test with the real task

- Measure for finding tasks: time to locate a known item, success rate.
- Measure for browsing tasks: items viewed, depth reached, click-through.
- Check: Back button returns to the same item; screen reader announces new items; footer is reachable.

## Rules

- Never use infinite scroll for search results or goal-directed finding.
- Every pagination state must be addressable by URL or restorable on Back.
- Always tell users how many items exist or that the list has ended.
- Loading more must never move keyboard focus unexpectedly or to the top of the page.

## Common Mistakes

- **Infinite scroll + footer:** users chase the footer that keeps escaping.
- **Losing position on Back:** user clicks item 80, presses Back, lands at item 1.
- **Tiny page links** clustered together on mobile — misclicks between page 2 and 3.
- **No total count:** users cannot judge whether to keep scrolling or refine the search.
- **Choosing by trend:** copying a social-feed pattern for a task-oriented admin list.

## When NOT to Use

- Lists that fit on one screen (≤ ~25 short items) — show them all.
- Content that users must print or read in full order — prefer a single long page or real document pagination.
