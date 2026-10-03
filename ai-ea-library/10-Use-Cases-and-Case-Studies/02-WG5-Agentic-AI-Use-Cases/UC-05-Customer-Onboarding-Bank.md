# UC-05 — Customer Onboarding Assistant (Bank)

| Field | Value |
|---|---|
| **Document ID** | UC-05 |
| **Document type** | Reference Use Case (forward-looking) |
| **Status** | Agentic architecture pattern for adaptation |
| **Validates** | WG5 — Scaling Agentic AI |
| **Sector** | Retail banking |
| **Scenario** | Guided application intake and bounded onboarding orchestration |
| **Provisional risk tier** | High because errors may affect financial access and identity controls |
| **Primary accountable role** | Customer Onboarding AI System Owner |
| **AI role** | Guidance and workflow coordination; no KYC, account-opening or credit decision authority |
| **Lifecycle scope** | Usability evaluation, supervised pilot and monitored operation |

> This prospective use case is not evidence of deployment and does not determine KYC, anti-money-laundering, privacy or consumer-law compliance. The institution must obtain current advice from its own legal, compliance and risk functions.

## 1. Purpose and Context

A retail bank wants to guide applicants without weakening identity, eligibility or financial-crime controls. The assistant explains requests, checks completeness and coordinates approved services. Authoritative KYC, screening and account-opening remain separate. A state machine determines transitions; the model explains the current step but cannot advance a case without validated events.

## 2. Actors and Responsibilities

| Actor | Responsibility |
|---|---|
| Applicant | Provides information through approved channels, reviews notices and may request human assistance |
| Support colleague and KYC analyst | Handle accessibility, exceptions, complaints and controlled decisions |
| Onboarding AI System Owner | Accountable for intended use, controls, outcomes, incidents and retirement |
| Product and data owners | Define journey, disclosures, alternatives, data quality and retention |
| Privacy, compliance, security and assurance | Review processing, threats, controls and evidence |
| Platform operations | Operate integrations, monitoring and fallback |

## 3. Trigger and Preconditions

**Trigger:** an applicant starts or resumes an eligible account-opening journey and chooses the assisted channel.

**Preconditions:**

1. Product, customer type, channel and jurisdiction are supported.
2. Current notices, processing records and accessibility options are available.
3. Identity, document, sanctions and fraud services return approved result states.
4. The state machine defines steps, timeouts, retries and human review.
5. Intended languages and documents are evaluated; non-AI and human routes remain available.

## 4. Scope and Boundaries

In scope are guidance, required-field collection, capture assistance, completeness checks, status explanation and approved validation calls. Identity, suspicious-activity, sanctions, eligibility and credit decisions; unapproved account creation; sensitive-attribute steering; and detection-rule disclosure are excluded. Technical errors must not appear as rejection.

## 5. Main Success Flow

1. The applicant selects assistance and receives clear AI disclosure.
2. The workflow performs high-level eligibility and creates an opaque case identifier.
3. The assistant requests only fields required for the current state; secure forms capture sensitive values.
4. Document services return structured quality and tamper statuses.
5. Authoritative KYC and screening run outside the model boundary.
6. The state engine advances, asks for a permitted correction or routes to an analyst.
7. The assistant explains approved status codes without exposing rules or inventing reasons.
8. An authorised system or colleague controls account creation; the case captures decisions, disclosures, versions and human intervention.

## 6. Alternate and Exception Flows

| Condition | Required response |
|---|---|
| Applicant declines the assisted channel | Continue through the available non-AI or human-supported route |
| Document is unreadable or a control returns an exception | Limit retries and route to approved guidance or analyst review |
| Applicant provides sensitive data in free text | Warn, minimise display, apply redaction and direct future entry to secure fields |
| The applicant requests a decision or reason the assistant cannot provide | State the limitation and offer the established review or support route |
| Model output conflicts with state | Ignore it, retain authoritative state and raise a quality event |
| Dependency or model is unavailable | Save permissible progress, show a neutral status and allow later resumption or human support |

## 7. Data Classification and Handling

| Data set | Illustrative classification | Handling requirement |
|---|---|---|
| Identity, contact, documents and biometric-derived results, if used | Restricted or Highly Restricted locally | Secure fields, minimal exposure, encryption and controlled retention |
| KYC, sanctions and fraud indicators | Restricted control data | Never reveal logic; analyst and system-only access |
| Conversation and guidance | Confidential; Restricted when personal | Redaction, bounded retention and no unapproved training |
| Consent, notice and disclosure records | Confidential governance evidence | Versioned content and tamper-evident timestamps |
| Aggregate journey metrics | Internal | Remove identifiers and assess re-identification risk |

The bank must document actual classification, purpose, notice, rights, transfer, residency and retention. Consent is not assumed to be the appropriate basis.

## 8. Logical Architecture

```text
Web/mobile/human-assisted channel
             |
             v
Identity session + disclosure service
             |
             v
Onboarding state-machine / policy engine
       |          |             |
       |          |             +--> Human analyst queue
       |          +--> Secure forms / document capture
       +--> Authoritative KYC, screening and eligibility services
             |
             v
Conversation orchestrator --> AI Gateway --> Approved model
             |
             v
Output policy + state-consistency validator
             |
             v
Approved status and guidance response
             |
             +--> Case audit / quality, fairness, security and cost monitoring
```

## 9. Controls and Evidence

| Control objective | Design control | Evidence |
|---|---|---|
| Human accountability | Named owner and analyst disposition for exceptions | System Card, queue record and decision reference |
| Minimum agency | State-machine-controlled transitions and no direct account-creation tool | Permission matrix and integration tests |
| Privacy and security | Secure fields, minimisation, access control, redaction and upload isolation | Data contract, logs, review and red-team record |
| Fair treatment | Approved language, alternatives and suitable outcome monitoring | Content, accessibility tests and review |
| Explainability | Status uses authoritative codes and approved text | Code mapping and message version |

## 10. Failure, Fallback and Recovery

Failure preserves case state and never implies acceptance or rejection. Model failure uses deterministic help or a colleague; control-service failure pauses the case. Repeated state conflict, abnormal drop-off, disclosure failure, leakage or segment-level harm trips the circuit breaker. Recovery identifies affected journeys, corrects communication through authorised channels, repeats evaluation and requires staged approval.

## 11. Evaluation and Acceptance

Use synthetic identities and documents plus governed test data. Cover standard journeys, mismatches, poor images, accessibility, languages, timeouts, hostile text and attempts to elicit screening logic. Review guidance, status fidelity, refusal, minimisation and escalation.

Measure completion accuracy, unsupported requirements, incorrect progression, handoff success, abandonment, latency, cost and security events. Examine groups where lawful and meaningful. Unauthorised progression, restricted-data leakage or a fabricated rejection reason stops the pilot.

## 12. Value Hypothesis

**Hypothesis:** clear, state-aware guidance will reduce avoidable abandonment and support effort while maintaining the effectiveness and independence of KYC and financial-crime controls.

| Measure | Baseline to establish | Prospective acceptance target |
|---|---|---|
| Completion and elapsed time | Current channel and step baseline | Improvement agreed after baseline; no result claimed |
| Avoidable support contacts | Categorised contact reasons | Reduction in navigation and capture queries |
| KYC and screening detection | Authoritative control baseline | No material degradation |
| Complaints and accessibility failures | Current reporting | No material deterioration; critical events stop |

Conversion cannot displace control quality or fair access. Also measure retries, inappropriate nudging, rework and guidance-caused abandonment.

## 13. AI-ADM Mapping

| AI-ADM phase | Use-case output |
|---|---|
| Phases 0–A | Journey hypothesis, customers, intended use, risk and criteria |
| Phase B | Journey states, colleague roles, exceptions and accessibility |
| Phase C | Personal-data flows, secure fields, classification and retention |
| Phases D–E | State orchestration, validation, gateway, integrations and resilience |
| Phase F | KYC separation, privacy, security, fairness and safeguards |
| Phases G–I | Synthetic tests, supervised pilot, launch gate and staged rollout |
| Phase J | Reassessment after product, rule, language, model or channel change |

## 14. Related Resources

- [AIEA-201 — AI Architecture Development Method](../../05-Standards/AIEA-201-AI-ADM.md)
- [AIEA-G01 — Financial Services](../../06-Series%20Guide/AIEA-G01-Financial-Services.md)
- [AIEA-G03 — Indian Enterprises](../../06-Series%20Guide/AIEA-G03-Indian-Enterprises.md)
- [AI Data Privacy and PII](../../01-AI-Governance/06-AI-Data-Privacy-and-PII.md)
- [Tool / Permission Matrix template](../../12-Templates/Tool-Permission-Matrix-Template.md)
- [DPDPA Compliance Checklist](../../12-Templates/DPDPA-Compliance-Checklist.md)
- [Data Contract template](../../12-Templates/Data-Contract-Template.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
