# Tool / Permission Matrix — Completed Example

> **Illustrative only:** fictional proposed permissions, not a production authorisation. Source template: [Tool-Permission-Matrix-Template.md](../Tool-Permission-Matrix-Template.md).

| Field | Value |
|---|---|
| **Agent system** | AI-SYS-EX-001 |
| **Version** | 0.8 |
| **Owner** | Customer Onboarding AI System Owner role |
| **Last reviewed** | 2026-09-15 (illustrative) |

## 1. Granted Tools

| Tool / API | Operation | Scope / limits | Reversible? | Human approval required | Justification |
|---|---|---|---|---|---|
| `read_journey_state` | Read | Current tokenised case only; approved fields from DC-EX-001; 10 calls per session | Yes | None | Explain the authoritative current step |
| `get_approved_guidance` | Read | Published content for current state and locale; no web access | Yes | None | Answer within approved onboarding content |
| `check_upload_quality` | Execute validation | Current upload only; returns quality codes, not document contents | Yes | None | Give capture guidance without making an identity decision |
| `create_support_handoff` | Write | Creates one queue item with case token and reason code; no free-text transcript by default | Yes | Applicant confirmation | Provide a human route |

The broker validates tool, case token, state, parameters, rate limit and session expiry independently of model output.

## 2. Explicitly Denied

| Capability | Reason |
|---|---|
| Create, approve or close an account | Irreversible financial action outside assistant scope |
| Read raw identity documents or screening indicators | Not required for guidance and unnecessarily exposes Restricted data |
| Change journey state | The deterministic workflow is authoritative |
| Send email, SMS or external messages | Established notification services own approved communications |
| General database, shell, web or code-execution access | No business need; unacceptable blast radius |

## 3. Irreversible Actions

No irreversible action is granted to the assistant.

| Action | Approver role | Approval mechanism |
|---|---|---|
| Account creation | Authorised Onboarding Operations role | Independent workflow gate after mandatory controls; agent has no callable tool |
| Adverse customer disposition | Authorised KYC or Compliance role | Case-management decision with review and evidence; agent has no callable tool |

## 4. Review

- **Review trigger:** every production deployment; any new tool, field, workflow state or model capability; security incident.
- **Reviewed by:** Architecture, Security, Onboarding Operations and Risk roles.
- **Least-privilege confirmed?** `[ ] Yes` — pending independent retest and launch-gate review.
