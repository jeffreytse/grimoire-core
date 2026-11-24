---
name: design-button-hierarchy
description: Use when a screen, form, dialog, or toolbar has more than one action button and it is unclear which action users should take, or when every button looks equally important.
source: IBM Carbon Design System (Button usage); Material Design 3 (Buttons, emphasis levels); Apple Human Interface Guidelines (Buttons); Nielsen Norman Group "Flat UI Elements Attract Less Attention and Cause Uncertainty" (2017)
tags: [button-hierarchy, call-to-action, visual-emphasis, primary-action, interaction-design, decision-speed]
---

# Design Button Hierarchy

Assign each action on a screen one emphasis level — primary, secondary, tertiary, or destructive — so the most likely next step is visually obvious and competing actions recede.

## Why This Is Best Practice

**Adopted by:** IBM Carbon ("Primary buttons should only appear once per screen"), Google Material Design 3 (filled → tonal → outlined → text emphasis scale), Apple HIG (one prominent/default button per view), GOV.UK Design System, Atlassian Design System, Shopify Polaris — every major public design system ships an explicit button emphasis scale.
**Impact:** NN/g eyetracking (2017) found users took 22% longer to find the target and showed more uncertainty when clickable elements had weak visual signifiers. Hick's Law (Hick, 1952) shows decision time grows with the number of equally weighted choices — a clear primary action collapses that choice to one obvious option.
**Why best:** The alternatives — all buttons styled the same, or multiple filled "primary" buttons — force users to read and compare every label before acting. A hierarchy lets the eye land on the intended action first while keeping alternatives available.

Sources: carbondesignsystem.com/components/button/usage; m3.material.io/components/buttons; developer.apple.com/design/human-interface-guidelines/buttons; NN/g (2017) Flat UI Elements Attract Less Attention

## Steps

### 1. Inventory actions per view

List every button in the view (page, dialog, side panel, card). For each, note:
- How often users choose it (analytics or best estimate)
- Whether it moves the user forward in their main task
- Whether it is destructive or irreversible

### 2. Assign one emphasis level to each action

| Level | When | Typical style |
|-------|------|---------------|
| **Primary** | The single most likely / intended next step | Filled, brand color |
| **Secondary** | Valid alternatives (Cancel, Back, Save draft) | Outlined or tonal |
| **Tertiary** | Low-frequency or supplementary actions | Text / ghost button |
| **Destructive** | Delete, remove, revoke | Red; filled only when it *is* the primary action of a confirmation dialog |

Rule: **at most one primary per view.** Dialogs and side panels are separate views and get their own primary.

If you cannot pick one primary, the screen is doing two jobs — split it or use progressive disclosure (see `apply-progressive-disclosure`).

### 3. Order and place buttons consistently

- Follow the platform convention for primary placement and keep it identical across the product:
  - Web (Carbon, Material, GOV.UK): primary right-aligned in dialogs; left-aligned at the end of single-column forms (aligned with fields)
  - macOS / iOS (Apple HIG): default button on the trailing (right) side
  - Windows: OK/Cancel with primary on the left of the pair
- Group related actions; separate destructive actions spatially from the primary (e.g., Delete at far left, Save/Cancel at right).
- Keep button groups to ≤3 visible actions. Overflow the rest into a "More" menu.

### 4. Label with verbs that name the outcome

```
❌ [OK]  [Cancel]           ✅ [Delete project]  [Keep project]
❌ [Submit]                 ✅ [Create account]
❌ [Yes]  [No]              ✅ [Discard changes]  [Keep editing]
```

Primary and secondary labels must be distinguishable without reading the style (also see `write-microcopy`).

### 5. Handle disabled and loading states

- Prefer keeping the primary enabled and showing validation errors on click over a disabled button with no explanation. If you disable, show why (helper text next to the button).
- On click, show a loading state inside the button and block repeat clicks (see `design-loading-states`).

### 6. Verify the hierarchy

- **Squint / blur test:** blur a screenshot — only one button should stand out.
- **5-second test:** show the screen for 5 seconds; ask "what would you click next?". ≥80% should name the primary.
- **Contrast check:** every button style, including ghost/text buttons, meets 3:1 non-text contrast against its background and 4.5:1 for label text (see `apply-accessible-color`).
- **Target size:** ≥24×24 CSS px (WCAG 2.2 AA); 44×44 pt recommended on touch (see `apply-fitts-law`).

## Rules

- One primary action per view — never two filled brand-colored buttons side by side.
- Destructive actions are never styled as the primary of a normal form; only inside a confirmation dialog whose purpose is that destruction.
- Button placement order is a product-wide convention, not a per-screen decision.
- Ghost/text buttons still need visible affordance (label color, hover/focus state) — not plain text.
- Use links for navigation and buttons for actions.

## Common Mistakes

- **Everything primary:** stakeholders each want "their" button filled; the result is no hierarchy at all.
- **Cancel as primary:** styling the escape route most prominently makes users abandon the task.
- **Inconsistent order:** Save on the right in one dialog and on the left in another causes misclicks.
- **Hiding the primary below the fold** on long forms — repeat it or use a sticky action bar.
- **Disabled primary with no reason:** users cannot discover what is missing.

## When NOT to Use

- Toolbars of equal-weight tools (text formatting, drawing tools) — use icon button groups/toggles instead.
- Lists where every row has the same action — use row-level tertiary actions, not repeated primaries.
