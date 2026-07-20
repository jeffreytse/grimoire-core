---
name: design-access-governance-review
description: Use when an organization needs an ongoing process to verify that users' system and data access remains appropriate over time — running periodic access recertification campaigns where accountable managers explicitly confirm or revoke each user's access, rather than granting access once and never systematically reviewing whether it's still needed.
source: ISACA COBIT framework; Sarbanes-Oxley IT General Controls (ITGC) access-review requirements
tags: [engineering, data, access-governance, access-recertification, itgc, sox-compliance]
related: [design-data-stewardship-program, design-data-governance-policy, audit-internal-controls]
---

# Design Access Governance Review

Run periodic access recertification campaigns where accountable managers explicitly confirm or revoke each user's system and data access — rather than granting access once and never systematically reviewing whether it's still needed.

## Why This Is Best Practice

**Adopted by:** ISACA's COBIT framework and Sarbanes-Oxley IT General Controls (ITGC) requirements both establish periodic access review as a required control for organizations subject to SOX financial reporting requirements, and periodic access recertification is standard practice across regulated industries (financial services, healthcare) as a core identity and access management control.
**Impact:** Access that accumulates over time without periodic review — commonly through role changes, project completions, and departures where access removal is incomplete — is documented as a leading contributor to excessive access ("access creep") that materially increases both insider-risk exposure and the potential blast radius of a compromised account, since unreviewed access tends only to accumulate, never to shrink on its own.
**Why best:** Access granted once and never revisited tends to persist indefinitely regardless of whether the underlying business need still exists — a departed employee's account not fully deprovisioned, or a former project member retaining access to systems no longer relevant to their current role — and periodic recertification is specifically designed to catch and correct this accumulation before it becomes a genuine security or compliance exposure.

Sources: ISACA, COBIT framework, identity and access management control objectives; Sarbanes-Oxley Act, IT General Controls (ITGC) access-review requirements

## Steps

### Step 1: Establish a recurring recertification cadence

Establish a defined, recurring cadence for access recertification — commonly quarterly for high-risk systems (financial systems, systems with sensitive data) and at least annually for lower-risk systems — rather than reviewing access only reactively or on an ad hoc basis.

### Step 2: Route each recertification to the accountable manager, not IT alone

Route each user's access recertification to their accountable business manager (who understands whether the access is still needed for the user's current role), not solely to the IT or security team, since the manager has the business context to judge appropriateness that IT alone typically lacks.

### Step 3: Require an explicit confirm-or-revoke decision, not passive approval

Require the reviewing manager to make an explicit confirm-or-revoke decision for each access grant under review — not a passive, unreviewed approval of a long list — since passive approval (rubber-stamping) defeats the purpose of the review and tends to simply re-certify accumulated access without genuine scrutiny.

### Step 4: Act on revocation decisions promptly

Ensure that access identified for revocation during a recertification campaign is actually removed promptly, not merely flagged — a recertification process that identifies access to revoke but doesn't reliably execute that revocation provides only the appearance of control, not the actual risk reduction.

### Step 5: Trigger an out-of-cycle review on role change or departure

Trigger an access review outside the standard recertification cycle whenever a user changes roles or departs the organization, since waiting for the next scheduled cycle leaves a window where access no longer matching the user's actual role or employment status persists unaddressed.

## Rules

- Establish a recurring recertification cadence, with more frequent review for higher-risk systems.
- Route recertification decisions to the accountable business manager, not to IT or security alone.
- Require an explicit confirm-or-revoke decision for each access grant, not passive or bulk approval.
- Ensure identified revocations are actually executed promptly, and trigger out-of-cycle reviews on role change or departure rather than waiting for the next scheduled cycle.

## Examples

**Recertification catching accumulated access:** A quarterly recertification campaign requires a manager to explicitly confirm or revoke each of their team's access grants to a financial system. The manager identifies a team member who moved to a different role six months ago but retained access from their prior role — access that had persisted because no out-of-cycle review was triggered at the time of the role change — and revokes it during the campaign.

**Out-of-cycle review preventing a departure gap:** An employee's departure triggers an immediate access review rather than waiting for the next quarterly cycle, ensuring their system access is revoked promptly rather than persisting for up to three months until the next scheduled recertification would have caught it.

## Common Mistakes

- **Routing recertification only to IT or security teams rather than accountable business managers** — IT typically lacks the business context to judge whether a specific access grant is still appropriate for a user's current role.
- **Allowing passive or bulk approval of recertification lists** — rubber-stamping a long list without genuine review re-certifies accumulated access without providing the actual scrutiny the process is meant to provide.
- **Identifying access for revocation but not reliably executing the revocation** — a recertification process is only as effective as its follow-through; flagged-but-not-executed revocations provide no real risk reduction.
- **Relying solely on the standard recertification cycle without triggering reviews on role change or departure** — waiting for the next scheduled cycle leaves a window of inappropriate access following these events.

## When NOT to Use

- For a very small organization with few systems and informal, easily-tracked access — formal recertification campaign infrastructure should be proportionate to actual organizational scale and system complexity.
- For systems with no sensitive data or material business risk, where lighter-touch, less frequent review may be proportionate rather than the same rigor applied to high-risk systems.
- As a substitute for the underlying access provisioning process — recertification catches and corrects accumulated access; it doesn't replace the separate need for a sound initial access-granting process that limits over-provisioning in the first place.
