# UC-01 — Financial Services AI Governance

| Field | Value |
|---|---|
| **Document ID** | UC-01 |
| **Document type** | Reference Use Case (forward-looking) |
| **Status** | Reference pattern |
| **Validates** | WG1 — AI Governance Playbook |
| **Sector** | Banking, financial services and insurance |
| **Scenario** | AI-assisted drafting of credit-decision rationales |
| **Provisional risk tier** | High — confirm through the organisation's approved classification process |
| **Primary accountable role** | Credit Decision System Owner |
| **AI role** | Decision support only; no approval, decline or pricing authority |
| **Lifecycle scope** | Design, pilot and operation |

> This scenario is not deployment evidence or a regulatory conclusion. Each organisation must validate requirements, credit policy and risk classification.

## 1. Purpose and Context

A bank wants more consistent, traceable business-credit rationales. The assistant assembles verified facts, retrieves approved policy and drafts for a qualified credit officer. It does not calculate the authoritative score, change source data, use prohibited attributes or make the lending decision. Evidence, generation and decision remain separate so the authorised human owns the final record.

## 2. Actors and Responsibilities

| Actor | Responsibility |
|---|---|
| Applicant and relationship manager | Provide application and business context through established channels |
| Credit officer | Verifies evidence, edits the rationale and owns the decision |
| Credit Decision System Owner | Accountable for scope, performance, controls, incidents and retirement |
| Credit policy owner | Publishes effective policy and interpretation guidance |
| Data, risk, security and privacy functions | Govern data, evidence and protection controls |
| Assurance | Independently examines control design and retained evidence |

## 3. Trigger and Preconditions

**Trigger:** a credit case reaches the rationale-drafting stage after mandatory identity, eligibility and data-quality checks have completed.

**Preconditions:**

1. The case is active and the user is authorised.
2. Facts come from approved systems; missing mandatory fields or unresolved conflicts block generation.
3. Only effective, version-controlled policy is searchable.
4. The model, prompt, retrieval and output schema have passed the launch gate.
5. Human review, monitoring, retention, incident handling and a manual route are operational.

## 4. Scope and Boundaries

In scope are evidence assembly, policy retrieval, a cited draft, uncertainty flags and audit evidence. Scoring, approval or decline, pricing, limit setting, external communication and record modification are out of scope. Unauthorised sensitive attributes are excluded. A new product, jurisdiction or action scope requires reassessment.

## 5. Main Success Flow

1. The relationship manager or credit officer requests a draft for an eligible case.
2. Orchestration checks entitlement, case state, purpose and policy version.
3. A data service builds a minimal verified case view with provenance; retrieval selects applicable policy.
4. The gateway sends only that view, cited passages and a constrained prompt to the approved model.
5. The model returns structured facts, citations, reasoning, uncertainty and missing-data warnings.
6. Deterministic validators reject unsupported amounts, missing citations, prohibited fields and malformed output.
7. The credit officer checks sources, edits the draft and records acceptance or rejection.
8. The workflow separates the final human rationale from the AI draft and logs versions, review, quality, security, latency and cost.

## 6. Alternate and Exception Flows

| Condition | Required response |
|---|---|
| Mandatory data is missing or contradictory | Do not generate; return the conflicting fields and route the case to normal data-resolution procedures |
| No applicable policy passage is retrieved | Produce no rationale; ask the credit officer to use the manual policy route and notify the policy-content owner |
| Sources disagree or a statement is unsupported | Block the affected draft, show evidence and require clarification |
| User asks the assistant to decide or bypass policy | Refuse, state the scope and record a policy event |
| Model or retrieval service is unavailable | Continue the credit workflow using the existing manual rationale process |

## 7. Data Classification and Handling

| Data set | Illustrative classification | Handling requirement |
|---|---|---|
| Identity, KYC, contact and financial data | Restricted personal and financial data | Case access, minimisation, encryption and controlled retention |
| Credit scores and risk attributes | Restricted decision data | Read-only use; provenance and version retained |
| Credit policy and product rules | Confidential internal | Effective-date control, approved publishing workflow and retrieval access |
| Prompts, drafts, citations and review | Restricted where applicant data appears | Tamper-evident logging, dashboard redaction and policy-based retention |
| Aggregate monitoring | Internal | De-identify before broad access |

Labels are illustrative. Data owners must record the actual classification, purpose, residency, transfer and retention decisions; no single control guarantees compliance.

## 8. Logical Architecture

```text
Authorised case workflow
          |
          v
Entitlement + purpose check -----> Policy/version registry
          |
          v
Minimal case-view service <------ Systems of record
          |
          +------> Governed policy retriever
                         |
                         v
                 Prompt/orchestration service
                         |
                         v
                     AI Gateway
                         |
                         v
                  Approved model endpoint
                         |
                         v
Citation + schema + policy validators
          |
          v
Credit-officer review workspace -----> Final decision workflow
          |
          +------> Audit store / quality, security and cost monitoring
```

## 9. Controls and Evidence

| Control objective | Design control | Evidence retained |
|---|---|---|
| Human accountability | Credit officer owns the final rationale; system owner is recorded | Review, edits and final decision reference |
| Grounding and explainability | Every material statement must cite a verified case field or effective policy passage | Source identifiers, passages, retrieval scores and validation result |
| Data minimisation | A purpose-built case view excludes unused fields | Data contract, field allow-list and access logs |
| Security | Case access, encryption, injection tests and output filtering | Access reviews, tests and security events |
| Change and monitoring | Versioning, regression tests and quality, drift, incident and cost triggers | Release, dashboard, alert and review records |

## 10. Failure, Fallback and Recovery

The safe failure mode is **no AI draft**, never an inferred decision. Repeated validation failures, abnormal latency, cost excursions or a security alert trip a circuit breaker. Cases return to the manual template. Operations retain diagnostics, identify drafts from the suspect window and follow incident procedures. Re-enablement requires cause analysis, regression and adversarial tests, and proportionate approval.

## 11. Evaluation and Acceptance

Use a de-identified or synthetic golden set covering products, exceptions, missing data and conflicts. Credit reviewers score factual support, policy applicability, completeness, citations and misleading language. Security tests cover injection, unauthorised access and extraction.

Approve thresholds before viewing results. Measure supported statements, critical unsupported statements, citation precision, material edits, correct blocking, latency and cost. Slice results where lawful and meaningful. Severe harm, disclosure or autonomous decision behaviour is a stop condition.

## 12. Value Hypothesis

**Hypothesis:** cited, structured drafts will reduce avoidable drafting effort and improve rationale completeness while preserving human decision quality and applicant protections.

| Measure | Baseline to establish | Prospective acceptance target |
|---|---|---|
| Active drafting time | Current-process time study | Improvement agreed after baseline; no result is claimed |
| Completeness and citation correctness | Blind pre-pilot review | Non-inferior or better; no critical omission |
| Material-edit rate | Not applicable before pilot | Diagnostic threshold that triggers redesign |
| Fairness and adverse-decision indicators | Approved benchmark | No material degradation within defined confidence |

Compare like-for-like cases and report rework, false confidence, complaints and fallback volume. Benefits remain hypotheses until measured.

## 13. AI-ADM Mapping

| AI-ADM phase | Use-case output |
|---|---|
| Phases 0–A | Value hypothesis, stakeholders, risk, boundary and success criteria |
| Phase B | Credit workflow, accountability, rules and human review |
| Phase C | Case view, policy corpus, classification, lineage and data contract |
| Phases D–E | Retrieval, gateway, validators, evaluation, resilience and observability |
| Phase F | Risk treatment, privacy, security, model-risk and assurance |
| Phases G–I | Pilot, launch gate, rollback, evidence and conformance reviews |
| Phase J | Reassessment after policy, model, data, product or regulatory change |

## 14. Related Resources

- [AIEA-201 — AI Architecture Development Method](../../05-Standards/AIEA-201-AI-ADM.md)
- [AIEA-G01 — Financial Services](../../06-Series%20Guide/AIEA-G01-Financial-Services.md)
- [AI Governance Operating Playbook](../../07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md)
- [AI System Card template](../../12-Templates/AI-System-Card-Template.md)
- [Data Contract template](../../12-Templates/Data-Contract-Template.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
- [Red-Team Log template](../../12-Templates/Red-Team-Log-Template.md)
