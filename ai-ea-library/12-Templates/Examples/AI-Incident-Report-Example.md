# AI Incident Report — Completed Example

> **Illustrative only:** fictional synthetic-test incident; no person, customer or production system was affected. Source template: [AI-Incident-Report-Template.md](../AI-Incident-Report-Template.md).

| Field | Value |
|---|---|
| **Incident ID** | INC-EX-001 |
| **System** | AI-SYS-EX-001 |
| **Severity** | SEV3 — synthetic test environment |
| **Detected** | 2026-09-12 10:05 UTC (illustrative) |
| **Resolved** | 2026-09-12 14:20 UTC (illustrative) |
| **Reporter** | AI Security Testing role |
| **System Owner** | Customer Onboarding AI System Owner role |

## 1. Summary

During a synthetic red-team exercise, uploaded text instructed the assistant to report identity as verified. The model repeated that statement in a draft response even though the authoritative workflow state remained `DOCUMENT_RETRY`. The deterministic state validator blocked the response before display. The event exposed a defence-in-depth weakness but did not alter workflow state.

## 2. Impact

- **Affected users / stakeholders:** synthetic test operator only; no real applicant or personal data.
- **Harm type:** potentially misleading output if the validator were absent or misconfigured.
- **Regulatory reportability:** `[ ] Yes  [x] No for this synthetic drill` — a real event would require assessment by the authorised legal and privacy functions; this checkbox is not a general conclusion.

## 3. Timeline

| Time (UTC, illustrative) | Event |
|---|---|
| 10:05 | State-conflict alert generated and response blocked |
| 10:20 | Test session isolated; evidence preserved |
| 11:10 | Cause reproduced with the same synthetic upload |
| 13:30 | Context-channel separation and regression test implemented |
| 14:20 | Engineering verification passed; independent security retest left open |

## 4. Root Cause

The upload-extraction component placed untrusted document text too close to task instructions. The model followed that text, while the downstream state validator operated correctly. The prompt boundary was therefore inadequate even though the independent workflow control prevented impact.

## 5. Corrective and Preventive Actions

| Action | Type | Owner | Target | Status |
|---|---|---|---|---|
| Mark extracted text as untrusted data and remove imperative fragments from model context | Corrective | Application Security role | Before pilot | Done; retest pending |
| Add state-conflict and document-injection cases to release evaluation | Preventive | AI Quality role | Before pilot | Done |
| Verify the state validator cannot be disabled by feature configuration | Preventive | Platform Assurance role | Before pilot | Open |
| Review any synthetic drafts produced by the affected build | Corrective | Test Governance role | Immediate | Done |

## 6. Lessons Learned

Output validation limited impact but did not make weak prompt boundaries acceptable. Untrusted document content requires explicit isolation, and critical workflow constraints need both pre-model context controls and post-model deterministic enforcement. The launch remains blocked until independent retest.
