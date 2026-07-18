---
name: apply-iso-31000-risk-framework
description: Use when an organization needs a systematic, repeatable process for managing risk broadly — establishing context, identifying risks, analyzing and evaluating them, treating the significant ones, and monitoring the whole process over time — rather than handling risk ad hoc through isolated, disconnected efforts (an incident response process here, a security review there).
source: ISO 31000:2018, "Risk Management — Guidelines," International Organization for Standardization
tags: [business, operations, enterprise-risk-management, iso-31000, risk-framework, governance]
related: [design-risk-register, design-risk-appetite-framework, design-business-continuity-plan]
---

# Apply ISO 31000 Risk Framework

Apply a systematic, repeatable process for managing risk across an organization broadly — establishing context, identifying risks, analyzing and evaluating them, treating the significant ones, and monitoring the whole process over time — rather than handling risk ad hoc through isolated, disconnected efforts that don't add up to a coherent, organization-wide risk-management discipline.

## Why This Is Best Practice

**Adopted by:** ISO 31000, "Risk Management — Guidelines," published by the International Organization for Standardization, is the internationally recognized standard for enterprise risk management, adopted or referenced by organizations across industries and countries as the common framework for structuring an organization's risk-management process, and forming the basis for many national and industry-specific risk-management standards built on its core structure.
**Impact:** Organizations that manage risk only through isolated, disconnected efforts — an incident response process for outages, a separate security review for new systems, an unrelated insurance review for property — tend to miss risks that fall between these isolated efforts' scope, and lack a consistent way to compare and prioritize risks across very different categories (operational, financial, strategic, reputational) that a unified framework specifically enables.
**Why best:** A collection of disconnected, ad hoc risk-management efforts, however individually competent, doesn't provide the organization a single, comparable view of its overall risk profile or a consistent process for deciding where to invest limited risk-management resources — ISO 31000's structured process specifically provides this unifying framework, at the cost of requiring genuine organizational commitment to implement consistently rather than treating it as a one-time exercise.

Sources: ISO 31000:2018, "Risk Management — Guidelines," International Organization for Standardization

## Steps

### Step 1: Establish the context for the risk-management process

Establish the scope, objectives, and criteria for the risk-management process — what parts of the organization and what categories of risk are in scope, what the organization's risk criteria (how risks will be evaluated and compared) are, and how the process connects to the organization's broader objectives and governance.

### Step 2: Identify risks systematically across relevant categories

Identify risks systematically across the categories relevant to the organization's context — operational, financial, strategic, reputational, legal/compliance, and others — using structured techniques (interviews, workshops, historical incident review) rather than relying on whichever risks happen to be top of mind for whoever is running the process.

### Step 3: Analyze and evaluate identified risks against consistent criteria

Analyze each identified risk's likelihood and potential impact, and evaluate it against the risk criteria established in Step 1 to determine its priority — using a consistent method across risk categories so that a financial risk and an operational risk, for example, can be meaningfully compared and prioritized against each other (see `design-risk-register` for a concrete tool implementing this analysis and prioritization).

### Step 4: Treat the significant risks with a deliberate response

For risks evaluated as significant, select and implement a deliberate treatment — avoiding the risk, reducing its likelihood or impact, transferring it (e.g., through insurance or contractual allocation), or knowingly accepting it within the organization's risk appetite (see `design-risk-appetite-framework`) — rather than leaving significant risks unaddressed by default.

### Step 5: Monitor, review, and communicate throughout the process

Monitor the risk landscape and the effectiveness of risk treatments on an ongoing basis, review and update the risk assessment as the organization's context changes, and maintain consistent communication and consultation with stakeholders throughout — treating risk management as a continuous, iterative process rather than a one-time assessment.

## Rules

- Establish explicit scope, objectives, and risk criteria before identifying or evaluating any specific risk — without this context, subsequent risk comparisons and prioritization lack a consistent basis.
- Identify risks systematically across all relevant categories, not only the categories the current team happens to be most familiar with.
- Evaluate risks against consistent criteria so that risks from different categories can be meaningfully compared and prioritized against each other.
- Select and implement a deliberate treatment for every significant risk — avoid, reduce, transfer, or knowingly accept — rather than leaving significant risks unaddressed by default.

## Examples

**Unified framework surfacing a cross-category risk comparison:** An organization applying this framework identifies both an operational risk (a single-supplier dependency) and a strategic risk (a competitor's emerging technology threat) using consistent evaluation criteria, allowing leadership to meaningfully compare and prioritize between two very different risk categories that isolated, disconnected risk efforts would have evaluated using inconsistent, non-comparable methods.

**Ad hoc risk management missing a significant risk (illustrative failure mode):** A different organization manages risk only through isolated efforts — a security team handling technical vulnerabilities, a separate legal team handling contract risk — with no unifying process. A significant risk that falls between these isolated scopes (e.g., a strategic dependency risk not clearly owned by either team) goes unidentified until it materializes, illustrating the gap a systematic framework is designed to close.

## Common Mistakes

- **Treating the framework as a one-time assessment rather than a continuous, iterative process** — risk context changes over time, and the framework's value depends on ongoing monitoring and review, not a single point-in-time exercise.
- **Identifying risks only in categories the current team is already familiar with** — systematic identification across all relevant categories is specifically what a unified framework adds beyond ad hoc, isolated efforts.
- **Evaluating risks from different categories using inconsistent criteria** — this defeats the framework's core value of enabling meaningful cross-category comparison and prioritization.
- **Identifying and evaluating risks without following through to a deliberate treatment decision** — a risk assessment that doesn't lead to an explicit avoid/reduce/transfer/accept decision for significant risks has not completed the process.

## When NOT to Use

- For a very small organization where the overhead of a full, formal framework exceeds its risk-management value — a lighter-weight, less formal risk process may be proportionate in this case.
- As a substitute for domain-specific risk expertise — the framework provides the structuring process, not the specific technical knowledge needed to identify and assess risks in specialized domains (security, financial, legal), which still requires appropriate domain expertise.
- When the organization isn't prepared to genuinely commit to ongoing monitoring and review — implementing the framework as a one-time exercise without follow-through provides limited lasting value.
