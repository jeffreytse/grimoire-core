---
name: design-business-continuity-plan
description: Use when preparing an organization to keep critical business functions running through a major disruption — a facility loss, a key-supplier failure, a pandemic, or another severe operational shock — covering people, processes, and facilities broadly, not only IT systems and data recovery.
source: ISO 22301, "Security and Resilience — Business Continuity Management Systems," International Organization for Standardization
tags: [business, operations, business-continuity, disaster-recovery, resilience, iso-22301, crisis-management]
related: [apply-iso-31000-risk-framework, design-vendor-risk-assessment, design-risk-register]
---

# Design Business Continuity Plan

Prepare the organization to keep its critical business functions running through a major disruption — a facility loss, a key-supplier failure, a pandemic, or another severe operational shock — covering the full range of people, processes, and facilities the organization depends on, not only its IT systems and data recovery, which a narrower disaster-recovery plan typically addresses.

## Why This Is Best Practice

**Adopted by:** ISO 22301, "Security and Resilience — Business Continuity Management Systems," is the internationally recognized standard for organizational business continuity management, adopted and certified against by organizations across industries seeking to formalize their preparedness for disruptions that go beyond IT infrastructure alone.
**Impact:** An organization with a well-developed IT disaster-recovery plan but no broader business continity plan can find its technology systems restored quickly after a disruption while still being unable to actually operate — because key personnel are unavailable, a critical physical facility is inaccessible, or an essential supplier relationship has failed — gaps a narrowly IT-focused plan doesn't address at all.
**Why best:** Modern organizations depend on far more than their IT systems to function — physical facilities, specific personnel and their availability, supplier and partner relationships, and manual or semi-manual processes all represent points of failure a disruption can hit, and a business continuity plan addressing only IT systems leaves these other dependencies entirely unprepared for, even if the technology recovery itself is well executed.

Sources: ISO 22301:2019, "Security and Resilience — Business Continuity Management Systems — Requirements," International Organization for Standardization

## Steps

### Step 1: Identify critical business functions and their dependencies

Identify the organization's critical business functions — the activities that must continue or be restored quickly to avoid unacceptable damage — and map each function's actual dependencies: specific personnel, facilities, suppliers, technology systems, and processes it relies on.

### Step 2: Assess the potential impact of losing each critical dependency

For each critical function's dependencies, assess the potential business impact of losing that dependency and how quickly the function would need to be restored (its recovery time objective) to avoid unacceptable damage — this impact analysis should span the full range of dependency types identified in Step 1, not IT systems alone.

### Step 3: Develop continuity strategies covering people, process, and facilities

Develop specific continuity strategies for each critical dependency — alternate facilities or remote-work arrangements if a primary facility is lost, cross-trained personnel or documented procedures if key staff are unavailable, alternate suppliers or safety-stock arrangements if a supplier fails — addressing the full range of dependency types, not defaulting to a technology-recovery plan alone.

### Step 4: Document the plan and assign clear roles and responsibilities

Document the continuity plan with clear, specific roles and responsibilities for who does what during a disruption — who activates the plan, who communicates with staff and stakeholders, who executes each continuity strategy — since an undocumented or ambiguously-owned plan tends to fail exactly when clear, fast action is most needed.

### Step 5: Test the plan through exercises and update it based on findings

Test the plan through regular exercises — tabletop discussions or fuller simulations — specifically to surface gaps between the documented plan and what would actually happen during a real disruption, and update the plan based on exercise findings, rather than treating a written plan as sufficient without any practical testing.

## Rules

- Identify and address the full range of critical dependencies — people, process, facilities, and suppliers, not IT systems alone.
- Assess business impact and recovery time objectives for each critical function before developing continuity strategies, so effort is prioritized toward what actually matters most.
- Document the plan with clear, specific roles and responsibilities — an undocumented or ambiguously-owned plan tends to fail during an actual disruption.
- Test the plan through regular exercises and update it based on what the exercises reveal, rather than treating a written plan as sufficient on its own.

## Examples

**Business continuity plan addressing a non-IT disruption:** An organization's primary office becomes inaccessible due to a local infrastructure failure unrelated to any IT system. Because the organization's business continuity plan specifically addressed facility-loss scenarios — pre-arranged remote-work capability and an alternate meeting location for critical functions — operations continue with limited disruption, illustrating the value of continuity planning that goes beyond IT systems alone.

**IT-only disaster recovery leaving a gap (illustrative caution):** A different organization has a well-tested IT disaster-recovery plan but no broader business continuity plan. When a critical supplier unexpectedly fails, the organization's IT systems remain fully operational, but the business function depending on that supplier is unable to continue — a gap the IT-focused plan never addressed.

## Common Mistakes

- **Treating business continuity planning as equivalent to IT disaster recovery** — see `design-disaster-recovery-plan` for the important but narrower IT/cloud-specific discipline; a full business continuity plan must address people, process, and facility dependencies as well.
- **Skipping the business impact analysis and jumping directly to continuity strategies** — without understanding which functions matter most and how quickly they need restoration, continuity effort risks being misallocated.
- **Leaving the plan undocumented or without clearly assigned roles and responsibilities** — this tends to produce confusion and delay exactly when fast, clear action is most needed.
- **Never testing the plan through exercises** — an untested plan often contains gaps that only become apparent when a real disruption (or a realistic simulation) actually occurs.

## When NOT to Use

- For a very small organization where the overhead of a formal, ISO 22301-aligned plan exceeds its practical value — a lighter, informal continuity discussion covering the same core dependencies may be proportionate in this case.
- As a substitute for IT-specific disaster recovery planning — business continuity and IT disaster recovery are complementary; a full continuity plan should incorporate the IT recovery plan rather than replace it (see `design-disaster-recovery-plan`).
- When the organization has no genuinely critical functions whose loss would cause significant damage — the effort of formal continuity planning should be proportionate to the actual consequences of disruption.
