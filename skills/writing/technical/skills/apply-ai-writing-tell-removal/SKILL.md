---
name: apply-ai-writing-tell-removal
description: Use when editing AI-generated or AI-assisted prose before it's published — check for and remove recurring stylistic tells (false-contrast constructions like "it's not just X, it's Y," compulsive rule-of-three listing, excessive em-dashes, hedge-stacking, unearned grandiosity) that read as generated rather than written, because these patterns are specific and recognizable enough to flag and fix directly rather than relying on a vague sense the prose "sounds like AI."
source: 'Wikipedia, "Wikipedia:Signs of AI writing" (community-maintained essay, English Wikipedia, ongoing); Google Developer Documentation Style Guide — plain, direct prose conventions used as the contrasting baseline'
tags: [writing, editing, ai-generated-content, technical-writing, style]
related: [design-documentation-structure, write-readme]
---

# Apply AI Writing Tell Removal

Check for and remove recurring stylistic tells before publishing AI-generated or AI-assisted prose — false-contrast constructions, compulsive rule-of-three listing, excessive em-dashes, hedge-stacking, title-case subheadings, unearned grandiosity — because these patterns are now specific and recognizable enough to flag and fix directly, rather than relying on a vague sense that the prose "sounds like AI."

## Why This Is Best Practice

**Wikipedia, "Signs of AI Writing":** A community-maintained, continuously-updated essay cataloguing specific, recurring stylistic patterns editors have identified in AI-generated encyclopedia contributions — including false-range or false-contrast constructions ("it's not just a tool, it's a revolution"), undue emphasis via bold or italics on ordinary words, promotional or reverential language disproportionate to the subject, and a preference for rule-of-three lists regardless of whether the content actually has three natural parts. The essay exists specifically because these patterns recur often enough, across unrelated AI-generated content, to be treated as checkable signals rather than vague impressions.

**Why best:** "This sounds like AI" is originally a vague, hard-to-action intuition — but the specific patterns behind that intuition are enumerable and checkable: look for the false-contrast template, count em-dashes per paragraph, check whether every list defaults to exactly three items regardless of content, check subheadings for unearned superlatives. Treating tell-removal as a specific checklist rather than a vibe is what makes it correctable in an edit pass rather than requiring a full rewrite from scratch.

**Adopted by:** Wikipedia's own content-review process for flagging and remediating AI-generated additions; increasingly referenced in professional technical-writing and editorial workflows reviewing AI-assisted drafts before publication.
**Impact:** Wikipedia editors have used the cataloged patterns specifically to triage and flag large volumes of AI-inserted content for review at a scale that relying on individual editors' unstructured impressions could not match — the specific, named patterns are what make the check teachable and consistent across many reviewers.

## Steps

1. **Scan for false-contrast constructions** — "it's not just X, it's Y," "this isn't just about A, it's about B" — and replace them with a direct statement of what's actually true, since the contrast is usually manufactured rather than meaningful.
2. **Check every list for forced rule-of-three structure** — if a list defaults to exactly three items regardless of whether the content naturally has two, four, or five, recount what's actually there and let the real number stand.
3. **Count em-dash density per paragraph** — a high, uniform rate of em-dash use across unrelated sentences is a specific, checkable tell; replace most with periods, commas, or a plainer connector.
4. **Flag hedge-stacking** — multiple hedges compounded in one sentence ("it could potentially perhaps suggest") — and cut to the single hedge that's actually warranted, or to a direct statement if none is.
5. **Check subheadings and emphasis for unearned grandiosity** — title-case headers, bolded ordinary words, or superlative framing ("a game-changing approach," "a revolutionary insight") applied to routine content — and flatten to plain, proportionate language.
6. **Read the edited version against the plain, direct baseline a style guide like Google's Developer Documentation Style Guide describes**, and prefer the plainer version whenever both convey the same information.

## Rules

- Treat each tell as a specific, checkable pattern (a construction, a ratio, a structural default), not a vague stylistic impression — this is what makes the edit pass repeatable and teachable.
- Don't remove a rhetorical device just because it appears once — the tells are specifically about *recurring, templated* overuse (every list is exactly three items; every other sentence has an em-dash), not the isolated, well-placed instance.
- Match emphasis and framing language to the actual proportionate significance of the content — reserve strong language for content that actually warrants it.
- Re-read against a plain, direct style baseline and prefer it whenever the plainer version loses no actual information.

## Examples

**False-contrast tell removed:** Original: "This isn't just a bug fix — it's a fundamental rethinking of how the system handles state." Edited: "This fix changes how the system handles state, not just where the bug surfaced." The second version states the actual claim without the manufactured contrast template.

**Forced rule-of-three corrected:** Original: "The redesign improves performance, readability, and maintainability." (when the actual change affects only performance and readability). Edited: "The redesign improves performance and readability." The list reflects what's actually true rather than defaulting to three items.

**Em-dash density reduced:** Original: "The service was slow — not because of the database — but because of an unindexed query — which we found via the trace." Edited: "The service was slow because of an unindexed query, which we found via the trace, not because of the database." Replacing templated em-dashes with ordinary connectors reads as written rather than generated.

## Common Mistakes

- **Treating "sounds like AI" as un-actionable and leaving the prose unedited**, instead of checking it against the specific, enumerable patterns that produce that impression.
- **Removing every em-dash or every list on principle**, rather than checking whether the specific instance is a templated default or a genuinely well-placed usage.
- **Fixing the surface pattern while leaving the underlying manufactured contrast or inflated framing intact** — e.g., rewording "it's not just X, it's Y" into a different sentence that still asserts an unsupported, inflated claim.
- **Applying this check only to AI-generated drafts and never to human-written drafts that have picked up the same tics** — the patterns are checkable regardless of the prose's origin.

## When NOT to Use

- For prose where the rhetorical device in question is genuinely well-placed and proportionate to the content — a single, well-earned em-dash or an actual three-part structure that reflects the real content doesn't need to be removed to satisfy a pattern-matching pass.
- For creative or literary writing where stylistic repetition and rhetorical contrast are deliberate authorial choices rather than unintentional tells — this skill targets technical, informational, and documentation prose specifically.
- As a substitute for substantive editing (checking facts, structure, and argument quality) — tell removal addresses surface style, not whether the underlying content is accurate, complete, or well-organized.
