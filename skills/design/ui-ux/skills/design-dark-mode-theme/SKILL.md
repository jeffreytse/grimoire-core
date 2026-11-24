---
name: design-dark-mode-theme
description: Use when adding a dark mode or dark theme to an app or website, or when an existing dark theme has unreadable text, glowing saturated colors, lost elevation, or images that look wrong on dark backgrounds.
source: Material Design "Dark theme" guidelines (m2.material.io/design/color/dark-theme); Apple Human Interface Guidelines "Dark Mode"; WCAG 2.2 SC 1.4.3 / 1.4.11; Dash & Hu (2021) "How much battery does dark mode save?" ACM MobiSys, Purdue University
tags: [dark-mode, dark-theme, color-contrast, theming, oled-battery, design-tokens, prefers-color-scheme]
---

# Design Dark Mode Theme

Build a dark theme as a separate, token-driven color system — not an inverted light theme — that keeps contrast, hierarchy, and elevation legible and follows the user's system preference.

## Why This Is Best Practice

**Adopted by:** Apple (system-wide Dark Mode since macOS 10.14 / iOS 13, HIG requires apps to support it), Google (Android 10 system dark theme, Material dark theme spec), Microsoft (Windows/Fluent), and major products — YouTube, Slack, GitHub, X, VS Code — ship dark themes driven by the OS preference.
**Impact:** Purdue's MobiSys 2021 study (Dash & Hu) measured that switching from light to dark mode at 100% brightness saves on average 39–47% of battery power on OLED phones. Material's spec requires text and primary colors to keep ≥4.5:1 contrast at every elevation — naive inversion routinely fails this.
**Why best:** The alternatives — no dark theme, or automatic color inversion — either ignore a system-level user preference or produce broken contrast, pure-black halation, and inverted images. A dedicated token set fixes these once for every component.

Sources: m2.material.io/design/color/dark-theme; developer.apple.com/design/human-interface-guidelines/dark-mode; w3.org/TR/WCAG22; Dash & Hu (2021)

## Steps

### 1. Put color behind semantic tokens

Before designing any dark colors, replace raw values with role tokens (see `write-design-system-token`):

```
--color-bg              --color-surface          --color-surface-raised
--color-text            --color-text-muted       --color-border
--color-primary         --color-on-primary       --color-danger
```

Components reference roles only. The dark theme is a second set of values for the same tokens.

### 2. Choose the dark base surfaces

- Use dark gray, not pure black, for the base: Material recommends `#121212`. Pure black with white text causes halation/smearing for many readers, especially those with astigmatism.
- Express elevation with **lighter surfaces**, not shadows: Material overlays white at 0% (base) up to ~16% (highest elevation). Apple uses "base" and "elevated" background colors.
- Keep 3–5 surface levels maximum.

### 3. Adjust text and accent colors

- Body text: off-white (e.g., `rgba(255,255,255,0.87)` high emphasis, `0.60` medium, `0.38` disabled per Material).
- Desaturate brand/accent colors (lighter tones, e.g., Material 200–300 range) — saturated colors vibrate against dark backgrounds.
- Verify every pair at every elevation: text ≥4.5:1 (SC 1.4.3), large text and UI component boundaries ≥3:1 (SC 1.4.11).
- Status colors (error, warning, success) need their own dark-tuned values; don't reuse light-theme reds.

### 4. Handle images, illustrations, and shadows

- Photos: keep as-is; optionally reduce brightness slightly (`filter: brightness(.9)`).
- Icons and illustrations with transparent backgrounds: supply dark variants or use `currentColor`.
- Logos: provide a dark-background version.
- Charts: re-validate categorical palettes against the dark surface.
- Shadows nearly disappear — rely on surface lightness and borders.

### 5. Respect the user's choice

```css
:root { color-scheme: light dark; }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { /* dark token values */ }
}
:root[data-theme="dark"] { /* dark token values */ }
```

- Default to the OS setting (`prefers-color-scheme`, `UITraitCollection`, `Configuration.UI_MODE_NIGHT`).
- Offer an in-app override: System / Light / Dark. Persist it.
- Set the theme before first paint to avoid a light flash (inline script or server-rendered attribute).
- Set `<meta name="theme-color">` per scheme for browser chrome.

### 6. Test

- Run automated contrast checks on both themes (axe, Stark, Figma contrast plugins).
- Check every component state (hover, focus, disabled, selected, error) — focus rings are often invisible in dark.
- Review in low ambient light and at minimum brightness.
- Test emails, PDFs, and embedded third-party widgets that may not inherit the theme.

## Rules

- Never ship dark mode by inverting colors or with `filter: invert()`.
- Never use pure `#000000` as the main surface with pure `#FFFFFF` body text.
- Every token pair must pass WCAG contrast in both themes.
- Follow the system preference by default; never force one theme without an override.

## Common Mistakes

- **Forgetting states:** focus outlines and disabled text drop below 3:1 on dark surfaces.
- **Same brand color in both themes:** fully saturated blue on `#121212` fails contrast or vibrates.
- **Shadows for elevation:** cards merge into the background.
- **Light flash on load:** theme applied after JS hydration.
- **Hard-coded colors** in one-off components that ignore the token set.

## When NOT to Use

- Content where color fidelity is the product (photo/print proofing) — offer a neutral gray workspace instead.
- Single-use print or document layouts that will never render on screen in dark mode.
