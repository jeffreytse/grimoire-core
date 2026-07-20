---
name: design-data-stewardship-program
description: Use when an organization's data governance policy exists on paper but no specific person is actually accountable for a given data domain's quality, definitions, and appropriate use — assigning named data stewards to specific data domains with clear accountability, rather than leaving data quality and definitional consistency as an unowned, organization-wide responsibility.
source: "DAMA International, \"DAMA-DMBOK: Data Management Body of Knowledge\" (2nd Edition, 2017)"
tags: [engineering, data, data-stewardship, data-governance, data-ownership, dama-dmbok]
related: [design-data-governance-policy, design-access-governance-review, design-data-quality-framework]
---

# Design Data Stewardship Program

Assign named data stewards to specific data domains with clear accountability for that domain's quality, definitions, and appropriate use — rather than leaving data quality and definitional consistency as an unowned, organization-wide responsibility that a written governance policy alone doesn't actually assign to anyone specific.

## Why This Is Best Practice

**Adopted by:** DAMA International's Data Management Body of Knowledge (DAMA-DMBOK) establishes data stewardship as a core data management function distinct from data governance policy itself, and organizations with mature data management programs — across finance, healthcare, and technology sectors — document assigned data stewards for specific data domains as standard practice, distinct from the separate exercise of writing a governance policy document.
**Impact:** Organizations that have a written data governance policy but no assigned data stewards are documented to experience persistent data quality problems (inconsistent definitions of core business terms across departments, unaddressed data quality issues) that the policy itself doesn't fix, since a policy document assigns no specific person the ongoing responsibility of maintaining a given data domain's quality and consistency.
**Why best:** A data governance policy states the rules; a data steward is the specific person accountable for a data domain actually following them day to day — without a named steward, data quality issues and definitional inconsistencies tend to persist because no single person owns identifying and resolving them, exactly the accountability gap assigning specific stewards is designed to close.

Sources: DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge," 2nd Edition (2017)

## Steps

### Step 1: Identify the organization's core data domains

Identify the organization's core data domains — customer data, product data, financial data, employee data, and other major categories — as the units data stewardship will be assigned against, since stewardship needs specific, bounded domains rather than an undifferentiated "all organizational data" assignment.

### Step 2: Assign a named data steward to each domain

Assign a specific, named individual as the data steward for each identified domain — typically someone with subject-matter expertise in that domain from the business side, not solely a technical data engineering role — responsible for that domain's definitional consistency, quality standards, and appropriate-use guidance.

### Step 3: Define the steward's specific responsibilities

Define what the data steward is actually responsible for: maintaining the domain's data dictionary and business definitions, serving as the point of escalation for data quality issues in that domain, and approving changes to how the domain's data is classified or used — distinct from the technical work of data engineering, which the steward oversees but doesn't necessarily perform directly.

### Step 4: Establish a forum for stewards to resolve cross-domain issues

Establish a regular forum (a data governance council or working group) where data stewards from different domains coordinate on cross-domain issues — data that spans multiple domains, or definitional conflicts between domains — since data quality issues frequently arise at the boundaries between domains rather than within a single domain alone.

### Step 5: Track data quality metrics by domain and steward

Track data quality metrics (completeness, accuracy, consistency) by domain, attributed to the responsible steward, so stewardship responsibility is connected to a measurable outcome rather than remaining a purely nominal title with no accountability mechanism behind it.

## Rules

- Assign a specific, named steward to each defined data domain — not an undifferentiated, organization-wide data quality responsibility.
- Select stewards with genuine subject-matter expertise in their assigned domain, not solely technical data engineering staff.
- Define the steward's specific responsibilities explicitly — data dictionary maintenance, quality escalation, use-classification approval — rather than leaving the role's scope vague.
- Track data quality metrics by domain and attribute them to the responsible steward, connecting the role to a measurable outcome.

## Examples

**Named stewardship resolving a definitional inconsistency:** An organization's finance and sales teams have been using inconsistent definitions of "active customer" for months, producing conflicting reports. Once a customer-data steward is assigned, they resolve the definitional conflict, document the agreed definition in the data dictionary, and become the ongoing point of escalation for future definitional questions in that domain.

**Cross-domain forum catching a boundary issue:** A data quality issue spanning both the customer-data and financial-data domains (inconsistent customer-ID matching across systems) is identified and resolved through the stewards' regular cross-domain coordination forum — a problem that either steward working in isolation on their own domain would have been less likely to catch.

## Common Mistakes

- **Writing a data governance policy without assigning any specific stewards to carry it out** — a policy document alone doesn't create the ongoing, day-to-day accountability that actually maintains data quality.
- **Assigning stewardship to purely technical data engineering staff without business subject-matter expertise** — data definitions and appropriate-use judgments require genuine domain knowledge, not only technical database familiarity.
- **Leaving the steward's specific responsibilities undefined** — a vague "data steward" title with no defined scope of responsibility tends to produce no actual accountability in practice.
- **Never tracking data quality metrics against stewardship domains** — without a measurable outcome connected to the role, stewardship risks becoming a nominal title rather than genuine ongoing accountability.

## When NOT to Use

- For a very small organization with limited data complexity, where a lighter, less formal data ownership arrangement may be proportionate — full stewardship program infrastructure should scale with actual data complexity and organizational size.
- As a substitute for the broader data governance policy itself — stewardship implements and carries out the policy's day-to-day accountability; it doesn't replace the separate need for the policy defining classification, access, and lifecycle rules (see `design-data-governance-policy`).
- When data domains are so small or simple that formal domain boundaries and dedicated stewardship add more overhead than value — apply stewardship structure proportionate to actual data complexity.
