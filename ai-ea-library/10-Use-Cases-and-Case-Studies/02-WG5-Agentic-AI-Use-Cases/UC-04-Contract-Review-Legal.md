# UC-04 — Contract Review Agent (Legal)

| Field | Value |
|---|---|
| **Document ID** | UC-04 |
| **Document type** | Reference Use Case (forward-looking) |
| **Status** | Agentic architecture pattern for adaptation |
| **Validates** | WG5 — Scaling Agentic AI |
| **Sector** | Cross-industry legal and procurement |
| **Scenario** | Clause extraction, playbook comparison and draft redlines |
| **Provisional risk tier** | High because outputs may influence binding agreements; confirm locally |
| **Primary accountable role** | Contract Review AI System Owner |
| **AI role** | Analysis and reversible drafting only |
| **Lifecycle scope** | Offline evaluation, lawyer-supervised pilot and monitored use |

> This prospective scenario is not legal advice, an account of a deployed system or a compliance conclusion. Qualified counsel must determine the permitted use, review standard and applicable contractual and professional obligations.

## 1. Purpose and Context

An enterprise legal team compares varied vendor contracts with an approved playbook. Repeated extraction consumes specialist time, yet a missed clause may create material exposure. The agent prepares a cited issue list and optional redline for a lawyer; it never accepts language, contacts a counterparty or executes an agreement. Authoritative status remains in the human-controlled contract workflow.

## 2. Actors and Responsibilities

| Actor | Responsibility |
|---|---|
| Requesting business or procurement team | Supplies the contract, transaction context and required review date |
| Reviewing lawyer | Verifies findings, chooses redlines and owns advice and approval |
| Contract Review AI System Owner | Accountable for scope, controls, evaluation, incidents and retirement |
| Contracting playbook owner | Approves fallback positions, escalation rules and jurisdictional variants |
| Information and platform owners | Govern classification, access, retention, workflow and release gates |
| Security, privacy and assurance functions | Review handling, integrations, threats and evidence |

## 3. Trigger and Preconditions

**Trigger:** an authorised user submits a supported contract type for first-pass review and supplies the required matter metadata.

**Preconditions:**

1. Access, confidentiality, retention and legal-hold rules cover the document.
2. Contract type, legal context and transaction category are known.
3. The applicable playbook and clause library are published and searchable.
4. Parsing meets quality checks; reviewers understand draft status and escalation.
5. The system cannot send, sign, accept or publish a document.

## 4. Scope and Boundaries

In scope are parsing, clause comparison, issue ranking, cited explanations and tracked changes. Unreviewed advice, commercial approval, negotiation, signature, autonomous transmission and public-web authority are excluded. Unsupported languages, corrupted files, novel agreements and contexts without a playbook route to manual review.

## 5. Main Success Flow

1. The user uploads a contract with purpose, type and legal context.
2. The workflow checks entitlement, classification, file safety and eligibility.
3. Parsing creates page- and paragraph-addressable text while preserving the original.
4. Retrieval selects the effective playbook, clauses and escalation guidance.
5. The agent maps each issue to contract text and playbook, with severity, rationale, uncertainty and action.
6. It may create tracked changes in a non-authoritative copy for approved clause types.
7. Validators check citations, quotes, defined terms, numbers, prohibited commitments and schema.
8. The lawyer accepts, edits or rejects proposals; the platform records only the human-approved version as authoritative and retains restricted evidence.

## 6. Alternate and Exception Flows

| Condition | Required response |
|---|---|
| Parsing confidence is below threshold | Identify affected pages and require manual review; do not analyse reconstructed text as authoritative |
| No playbook, or ambiguous sources | Produce intake context and assign specialist review without interpreting |
| Contract text contains model instructions | Treat document text as untrusted data and follow only system policy |
| A redline alters terms or references unexpectedly | Block it and flag dependent clauses |
| User requests external sending or signature | Refuse and direct the user to the authorised contract workflow |
| Model, retriever or validator is unavailable | Preserve the original document and continue with the existing manual process |

## 7. Data Classification and Handling

| Data set | Illustrative classification | Handling requirement |
|---|---|---|
| Contracts and sensitive schedules | Confidential or Restricted | Matter access, encryption, minimised context, retention and legal hold |
| Contracting playbook and clause library | Confidential internal or privileged, as determined locally | Versioned publishing and need-to-know retrieval |
| Prompts, issues, redlines and lawyer feedback | Same or higher classification as the source contract | Segregated audit access and controlled reuse |
| Aggregate quality and cost | Internal | Remove matter content and sensitive identifiers |

Map labels to the local scheme and determine privilege, purpose, transfer, retention and deletion. Logging must not create an uncontrolled duplicate repository.

## 8. Logical Architecture

```text
Contract / matter workspace
          |
          v
Access + classification + file-safety checks
          |
          v
Document parser / OCR ----------> Immutable original
          |
          +----> Approved playbook and clause retriever
                         |
                         v
                 Agent orchestrator
                         |
                         v
                     AI Gateway --> Approved model
                         |
                         v
Citation + term + number + policy validators
          |
          v
Lawyer review workspace --> Authoritative contract workflow / signature gate
          |
          +----> Restricted audit / quality, security and cost monitoring
```

## 9. Controls and Evidence

| Control objective | Design control | Evidence |
|---|---|---|
| Human accountability | Lawyer review before any output becomes authoritative | Edits and approved version |
| Grounding | Every issue cites exact contract and playbook passages | Page/paragraph references and retrieval versions |
| Minimum agency | Read-only source access and draft-only output | Tool matrix and access review |
| Confidentiality and injection resistance | Matter access, encryption, provider restrictions and untrusted-content isolation | Access logs, data flow and red-team evidence |
| Change control | Versioned playbook, prompt, model and validators | Release record and regression results |

## 10. Failure, Fallback and Recovery

Fallback is manual review of the unchanged original. A partial review is never presented as complete. Repeated malformed output, source mismatch, abnormal spend or security events trip a circuit breaker. Suspect drafts are quarantined under matter rules. Recovery requires cause analysis, representative replay, impact confirmation and proportionate approval.

## 11. Evaluation and Acceptance

The governed test set covers supported types, clause variants, scans, tables, defined terms, cross-references, absent clauses and embedded attacks. Lawyers establish reference findings independently. Measure clause recall and precision, severity agreement, citations, number and term preservation, material edits, false reassurance, latency and cost.

Distinguish boilerplate from material liability, privacy, intellectual-property, security and termination clauses. Aggregate scores cannot offset a critical miss. Pilot contracts remain fully human-reviewed; feedback is not training data without separate approval.

## 12. Value Hypothesis

**Hypothesis:** a source-linked first pass will reduce repetitive extraction and comparison effort while maintaining or improving detection of playbook deviations.

| Measure | Baseline to establish | Prospective acceptance target |
|---|---|---|
| Lawyer time by contract type | Current first-pass time study | Improvement set after baseline; no outcome claimed |
| Material deviations detected | Blind representative set | Non-inferior or better at the critical-clause threshold |
| Incorrect-suggestion rework | Current peer-review findings | No material increase |
| Queue age and escalation quality | Current workflow | Improvement without displacing high-risk work |

Counter-metrics include misses, unnecessary redlines, over-reliance, confidentiality events and verification effort. Only measured evidence supports a result.

## 13. AI-ADM Mapping

| AI-ADM phase | Use-case output |
|---|---|
| Phases 0–A | Effort hypothesis, stakeholders, legal boundary, risk and criteria |
| Phase B | Intake, lawyer review, escalation and authoritative workflow |
| Phase C | Classification, parsing, playbook lineage and retention |
| Phases D–E | Retrieval, drafting, validation, gateway, storage and resilience |
| Phase F | Confidentiality, privilege, security, oversight and assurance |
| Phases G–I | Offline benchmark, supervised pilot, launch gate and conformance |
| Phase J | Re-evaluation after playbook, context, model, contract type or tool change |

## 14. Related Resources

- [AIEA-201 — AI Architecture Development Method](../../05-Standards/AIEA-201-AI-ADM.md)
- [AIEA-G05 — Agentic AI Architecture](../../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)
- [AI Procurement and Contracts](../../02-AI-Strategy/07-AI-Procurement-and-Contracts.md)
- [Risk Mitigation](../../01-AI-Governance/04-Risk-Mitigation.md)
- [AI System Card template](../../12-Templates/AI-System-Card-Template.md)
- [Tool / Permission Matrix template](../../12-Templates/Tool-Permission-Matrix-Template.md)
- [Red-Team Log template](../../12-Templates/Red-Team-Log-Template.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
