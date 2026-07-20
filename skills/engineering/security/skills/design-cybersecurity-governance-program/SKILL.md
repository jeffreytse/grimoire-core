---
name: design-cybersecurity-governance-program
description: Use when a public company needs board-level cybersecurity risk governance and disclosure meeting SEC requirements — establishing defined board oversight of cyber risk, a documented incident materiality-assessment process, and required disclosure of both governance practices and material incidents, rather than treating cybersecurity purely as a technical, management-level function with no board accountability structure.
source: SEC, "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure" rule (effective 2023); NIST Cybersecurity Framework 2.0, Govern function
tags: [engineering, security, cybersecurity-governance, sec-disclosure, board-oversight, incident-disclosure]
related: [design-ai-governance-framework, design-enterprise-risk-management-committee, design-threat-model]
---

# Design Cybersecurity Governance Program

Establish board-level cybersecurity risk governance and disclosure meeting SEC requirements — defined board oversight of cyber risk, a documented incident materiality-assessment process, and required disclosure of both governance practices and material incidents — rather than treating cybersecurity purely as a technical, management-level function with no board accountability structure.

## Why This Is Best Practice

**Adopted by:** The SEC's cybersecurity disclosure rule (effective for annual reports beginning in fiscal year 2023) requires public companies to describe their board's oversight of cybersecurity risk and management's role in assessing and managing that risk, and to disclose material cybersecurity incidents within four business days of determining materiality — making structured cyber governance and a formal materiality-assessment process now mandatory disclosure elements for public companies, not merely a best-practice recommendation.
**Impact:** Companies without a defined board oversight structure and documented materiality-assessment process for cybersecurity incidents are documented to face compliance risk under the SEC's rule itself, since the disclosure requirements presume the underlying governance and assessment processes actually exist — a company can't accurately describe board oversight of cyber risk in its annual report if no such oversight structure genuinely operates.
**Why best:** Treating cybersecurity purely as a technical, IT-department-level function with no board accountability misses that the SEC rule now specifically requires companies to describe board-level oversight and a documented incident-materiality process — building genuine governance structure (not just technical controls) is what actually enables accurate, compliant disclosure, as opposed to attempting to describe governance processes that don't actually operate.

Sources: U.S. Securities and Exchange Commission, "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure," Release No. 33-11216 (2023); National Institute of Standards and Technology, Cybersecurity Framework 2.0, Govern function

## Steps

### Step 1: Establish defined board-level oversight of cybersecurity risk

Establish a specific board or committee (a dedicated risk committee, or the audit committee with an explicitly expanded mandate) responsible for cybersecurity risk oversight, with defined reporting cadence from the company's security leadership (CISO or equivalent) — since the SEC rule requires the company to describe this oversight structure in its annual report.

### Step 2: Establish a documented incident materiality-assessment process

Establish a specific, documented process for assessing whether a cybersecurity incident is material — considering financial impact, operational disruption, and reputational consequence — with clear ownership of the materiality determination, since the SEC rule's four-business-day disclosure clock starts running from the determination of materiality, making a slow or undefined assessment process itself a compliance risk.

### Step 3: Integrate cybersecurity risk into the company's broader enterprise risk management process

Integrate cybersecurity risk assessment into the company's broader enterprise risk management framework rather than treating it as an isolated, purely technical risk category, consistent with the governance integration the SEC rule and NIST Cybersecurity Framework's Govern function both expect.

### Step 4: Establish management's specific role and expertise in cyber risk assessment

Document management's specific role and relevant expertise in assessing and managing cybersecurity risk, since the SEC rule requires disclosure of management's role, not only the board's — this requires a genuinely defined management-level process, not an assumed or informal arrangement.

### Step 5: Prepare and rehearse the incident disclosure process before an actual incident occurs

Prepare and rehearse the process for assessing materiality and preparing required disclosure before an actual incident occurs, since the four-business-day disclosure clock leaves little room for an unrehearsed, ad hoc process to be developed under the pressure of an actual live incident.

## Rules

- Establish a specific, named board or committee responsible for cybersecurity oversight, with a defined management reporting cadence.
- Document a specific incident materiality-assessment process with clear ownership, since the SEC's disclosure clock depends on this determination.
- Integrate cybersecurity risk into the broader enterprise risk management framework, not as an isolated technical risk category.
- Rehearse the incident materiality-assessment and disclosure process before an actual incident occurs, not for the first time during a live event.

## Examples

**Rehearsed process enabling timely disclosure:** A company experiences a cybersecurity incident and, because its materiality-assessment process was previously documented and rehearsed through a tabletop exercise, the responsible team completes the materiality determination and required disclosure preparation within the SEC's four-business-day window — a timeline an unrehearsed, ad hoc process developed for the first time during the actual incident would have struggled to meet.

**Defined board oversight supporting accurate disclosure:** A company's risk committee receives quarterly briefings from the CISO on the cybersecurity risk landscape and the company's risk posture, providing genuine substance behind the board oversight description in the company's annual report — rather than describing an oversight structure that exists only nominally, without actual board engagement behind it.

## Common Mistakes

- **Treating cybersecurity purely as a technical, IT-department function with no defined board accountability structure** — this creates a gap between what the SEC rule requires companies to disclose and what governance structure actually exists to support that disclosure.
- **Lacking a documented, clearly-owned materiality-assessment process** — since the disclosure clock starts at the materiality determination, an undefined or slow assessment process creates direct compliance risk.
- **Developing the incident disclosure process for the first time during an actual live incident** — the four-business-day window leaves little margin for a process that hasn't been rehearsed in advance.
- **Treating cybersecurity risk as isolated from the company's broader enterprise risk management process** — this fragmentation makes it harder to assess cyber risk in the context of the company's overall risk profile and priorities.

## When NOT to Use

- For a private company with no SEC reporting obligations — the specific disclosure requirements addressed here apply to SEC-reporting public companies; the underlying governance principles may still be valuable but aren't a compliance mandate.
- As a substitute for the underlying technical security practices needed to actually prevent and detect incidents — governance provides oversight and disclosure structure; it doesn't replace the technical work of threat modeling, detection, and response (see `design-threat-model`).
- For determining whether a specific past incident should have been disclosed under the rule — that determination requires case-specific legal and materiality analysis at the time of the incident.

> **Legal disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Cybersecurity disclosure obligations carry significant securities-law compliance risk — consult licensed securities counsel before finalizing a cybersecurity governance and disclosure program.
