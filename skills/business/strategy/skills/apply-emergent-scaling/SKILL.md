---
name: apply-emergent-scaling
description: Use when a validated approach is working at its current scale and the question of pushing it much further (10x, 100x) comes up — treat what happens at that larger scale as a genuinely open, separately testable question rather than assuming diminishing returns, and catalogue the technical, financial, and organizational resistance to scaling so each can be addressed individually, because scale can produce qualitatively new value unpredictable from smaller-scale results.
source: 'Wei et al., "Emergent Abilities of Large Language Models", Transactions on Machine Learning Research (2022) — peer-reviewed documentation of capabilities appearing discontinuously at scale thresholds, not by smooth extrapolation; Sam Altman, public commentary on OpenAI model-scaling strategy and Y Combinator batch-scaling (2024–2025); Altman was president of Y Combinator (2014–2019) before co-founding and leading OpenAI'
tags: [strategy, scaling, innovation, resource-allocation, organizational-execution]
related: [apply-commit-with-no-retreat, apply-force-concentration, apply-mental-models-framework]
---

# Apply Emergent Scaling

When a validated approach is working at its current scale, treat what happens at a much larger scale as a genuinely open, separately testable question rather than assuming proportional or diminishing returns — and separately catalogue the technical, financial, and organizational resistance to scaling so each can be addressed individually, because scale can produce qualitatively new value that cannot be predicted from smaller-scale results.

## Why This Is Best Practice

**Why best:** The specific, checkable claim here is not "bigger is always better" — it's that certain kinds of value are emergent: undetectable and unpredictable from smaller-scale data, appearing only once a scale threshold is actually crossed, rather than smoothly extrapolatable in advance. Because this value genuinely cannot be predicted from below the threshold, the decision to stop scaling once something "works" at a given size is often made without the evidence needed to justify it — the absence of visible further gains in a smaller-scale test says nothing about whether emergent value exists at a larger one. The resistance to actually testing this (technical difficulty, capital requirements, and the organizational instinct to spread resources across many smaller, individually safer bets instead) is real, but is a separate problem from whether scaling would produce value — conflating "scaling is hard" with "scaling wouldn't help" is the specific error this technique targets.

**Wei et al., "Emergent Abilities of Large Language Models" (2022):** This peer-reviewed research formally documented that certain language-model capabilities do not appear as a smooth function of model scale — they are effectively absent below a certain size and appear only once scale crosses a specific threshold, in a way that could not have been predicted by extrapolating performance curves from smaller models. This provides rigorous, independent, peer-reviewed grounding for the general claim that scale can produce qualitatively new capabilities rather than merely proportionally more of the same capability — a finding distinct from and stronger than an informal observation that "bigger models tend to do better."

**Sam Altman on scaling strategy:** Altman's publicly documented commentary on OpenAI's continued model-scaling strategy — pursued through multiple rounds of substantial skepticism from parts of the field that a given scale already represented diminishing returns — and on Y Combinator's batch-scaling approach during his presidency there, both describe the same underlying pattern: value that only became visible once scale was actually pushed further, plus a documented, specific analysis of why most teams don't attempt this, breaking the resistance into technical (unproven engineering feasibility at the target scale), financial (large, uncertain capital commitment), and organizational (the instinct to spread available resources across several smaller, individually less risky bets rather than commit fully to one).

**Adopted by:** OpenAI's documented model-scaling strategy and Y Combinator's batch-scaling approach are both widely cited examples of this pattern in technology and startup-ecosystem strategy discussions; Wei et al.'s emergent-abilities research is a widely cited paper in machine learning research literature documenting the underlying phenomenon rigorously.
**Impact:** Wei et al.'s peer-reviewed analysis documented specific capabilities appearing only once model scale crossed particular thresholds, in a way not predictable from smaller-scale performance curves — direct, independent evidence that scale can produce qualitatively new value rather than only proportionally more of existing value; OpenAI's continued-scaling strategy is documented as having produced capability gains at multiple successive scale thresholds that were not predicted in advance by contemporaneous critics who expected returns to have already plateaued.

## Steps

1. **When a validated approach is working at its current scale, treat the question of what happens at significantly larger scale (10x, 100x) as a genuinely open, separately testable question — not something to infer by extrapolating current results.** The absence of visible additional gains at the current scale is not evidence that no further gains exist at a larger one.

2. **Before concluding that further scaling isn't worth pursuing, distinguish whether that conclusion rests on genuine evidence of diminishing returns or on discomfort with the resistance further scaling would require.** These are different questions, and conflating them is the specific error this technique targets.

3. **Separately catalogue the distinct types of resistance to a scale-up: technical (engineering feasibility unproven at the target magnitude), financial (large, uncertain capital investment), and organizational (the instinct to spread available resources across several smaller, individually safer bets instead of committing to one).** Each requires a different kind of solution, and treating "scaling is hard" as one undifferentiated obstacle obscures which specific barrier is actually blocking the decision.

4. **Address each identified barrier individually and concretely** — a technical proof-of-concept at an intermediate scale for the technical barrier, a staged or phased capital commitment for the financial barrier, and an explicit organizational decision to concentrate resources rather than diversify them for the organizational barrier.

5. **Check whether the organizational default toward spreading resources across many smaller bets is actually the better-evidenced choice, or simply the more comfortable one.** This default should be treated as a bias to examine specifically when a validated approach is being considered for scale-up, not as a neutral baseline.

6. **When the decision is made to scale, communicate the commitment explicitly and unconditionally to the team, including who bears responsibility if it doesn't work.** An ambiguous or hedged commitment undermines the execution discipline a genuine scale-up requires (see `apply-commit-with-no-retreat`).

## Rules

- Treat "what happens at significantly larger scale" as an empirically open question requiring its own test, never an assumption inferred by extrapolating smaller-scale results.
- Distinguish technical, financial, and organizational resistance to a scale-up as separate problems requiring separate solutions, rather than treating "scaling is hard" as a single undifferentiated obstacle.
- Treat the default instinct to spread resources across many smaller, individually safer bets as a bias to explicitly check against the evidence, not a neutral default, whenever a validated approach is being considered for scale-up.
- Communicate a decision to scale as an explicit, unconditional commitment — an ambiguous or hedged one undermines the execution discipline the decision requires.

## Examples

**AI model scaling:** A research team continues scaling a model architecture well beyond the point where many contemporaneous observers expected returns to plateau, specifically to test for capabilities not predictable from smaller-scale results — consistent with the peer-reviewed finding that some language-model capabilities appear discontinuously at scale rather than through smooth extrapolation.

**Startup accelerator batch size:** An accelerator finds that increasing cohort size produces network-effect value — founder-to-founder resource matching, information flow, peer collaboration — that does not exist in smaller cohorts, treating batch scale itself as a distinct lever for value that a smaller, already-"sufficient" batch size would never reveal.

**Dismantling resistance systematically:** A team considering scaling a validated approach identifies three separate barriers — unproven technical feasibility at the target scale, the magnitude of capital required, and the organizational instinct to instead spread the same resources across several smaller initiatives — and addresses each individually: a technical proof-of-concept at intermediate scale, a staged capital commitment, and an explicit, unconditional leadership decision to concentrate on the one direction, rather than treating the scale-up as a single monolithic decision to accept or reject.

## Common Mistakes

- **Assuming a validated small-scale result caps out at proportional gains from further scaling**, without treating significantly larger scale as its own open, separately testable question.
- **Treating "scaling is hard" as one undifferentiated obstacle** instead of separately identifying and solving its distinct technical, financial, and organizational components.
- **Defaulting to spreading available resources across many smaller, individually safer bets** without checking whether committing fully to one validated direction at larger scale is actually the better-evidenced choice.
- **Communicating a scale-up decision ambiguously or with implicit hedges**, undermining the team's execution discipline relative to an explicit, unconditional commitment.

## When NOT to Use

- When genuine evidence — not merely discomfort with the resistance — shows diminishing or negative returns to further scale; this technique argues against assuming a plateau without evidence, not against ever concluding one genuinely exists.
- When the capital or resource commitment required for the scale-up genuinely exceeds what the organization could survive losing if it failed — the technique argues for systematically addressing resistance, not for accepting existential risk regardless of its magnitude.
- For approaches that are inherently non-scalable in kind, not merely in current implementation (a genuinely bespoke, one-off service) — the emergent-value-from-scale logic specifically applies to approaches whose underlying mechanism is scale-sensitive in the first place.
