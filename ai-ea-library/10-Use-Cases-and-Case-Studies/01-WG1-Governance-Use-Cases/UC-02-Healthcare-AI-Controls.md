# UC-02 — Healthcare AI Controls

| Field | Value |
|---|---|
| **Document ID** | UC-02 |
| **Document type** | Reference Use Case (forward-looking) |
| **Status** | Reference pattern |
| **Validates** | WG1 — AI Governance Playbook |
| **Sector** | Healthcare and clinical services |
| **Scenario** | AI-assisted patient-history summarisation and guideline retrieval |
| **Provisional risk tier** | High — confirm through clinical, legal and organisational review |
| **Primary accountable role** | Clinical AI System Owner |
| **AI role** | Information synthesis and reference support; not diagnosis or treatment direction |
| **Lifecycle scope** | Design, safety evaluation, pilot and operation |

> This prospective scenario is not clinical guidance, safety evidence or a compliance determination. Applicable requirements vary by intended use and require qualified review.

## 1. Purpose and Context

A hospital network is considering an assistant that prepares a history and retrieves approved clinical guidance. A fluent summary may conceal omissions, chronology errors or unsupported implications, so source verification must be easier than blind acceptance. The assistant may organise authorised information but cannot diagnose, prescribe, order care, change records or suppress information. The clinician owns all clinical judgement.

## 2. Actors and Responsibilities

| Actor | Responsibility |
|---|---|
| Patient or representative | Uses established information, access and correction routes |
| Treating clinician | Reviews sources, corrects the draft and makes all clinical decisions |
| Clinical AI System Owner | Accountable for intended use, safety evidence, controls, incidents and retirement |
| Clinical safety lead | Defines hazards, stops and evaluation |
| Data and guideline owners | Govern record quality, terminology, lineage and approved guidance |
| Privacy, security and assurance functions | Review data flows, threats, evidence and performance |
| Platform operations | Operate the gateway, monitoring, release and fallback |

## 3. Trigger and Preconditions

**Trigger:** an authorised clinician opens an eligible encounter and explicitly requests a summary.

**Preconditions:**

1. User, patient, encounter and care relationship pass access and purpose checks.
2. Required records are ingested and known gaps are visible.
3. Guidance comes from an approved, versioned corpus for the care setting.
4. Intended use, prohibitions, hazards and human oversight are approved.
5. Evaluation, monitoring, escalation and normal record review are operational.

## 4. Scope and Boundaries

In scope are timelines, cited summaries, record-conflict flags and approved guidance retrieval. Diagnosis, triage, risk scoring, orders, autonomous messaging and record modification are excluded. The assistant cannot infer absent facts or hide uncertainty. Paediatric, emergency, specialist and other higher-consequence contexts require separate authorisation.

## 5. Main Success Flow

1. The clinician requests a summary for an authorised encounter.
2. The workflow verifies role, care relationship, purpose and scope.
3. A data service builds a minimal view of observations, medicines, allergies, diagnoses and notes with provenance.
4. Normalisation orders events and flags duplicates, conflicts and stale information; retrieval selects applicable guidance.
5. The gateway sends the structured view, source identifiers, guidance and constrained schema to the model.
6. The model drafts a timeline, active issues, medicines, allergies, conflicts, gaps and references.
7. Validators enforce source support, negation, units, citations and the ban on diagnosis or directives.
8. The clinician opens sources, edits or rejects the draft and uses the established signing process; the audit distinguishes AI and final notes.

## 6. Alternate and Exception Flows

| Condition | Required response |
|---|---|
| Record sources are incomplete | State what is missing and use manual review |
| Sources conflict or a citation fails | Show provenance and block the affected statement; do not infer a resolution |
| Draft contains a clinical directive | Reject it, raise a safety event and use manual preparation |
| Guidance is expired or inapplicable | Exclude it and notify the owner; never substitute unapproved web content |
| The service is unavailable | Leave the consultation workflow available without AI and display no stale generated content |

## 7. Data Classification and Handling

| Data set | Illustrative classification | Handling requirement |
|---|---|---|
| Demographics, identifiers and clinical records | Restricted personal and health data | Minimum necessary access, encryption, provenance and controlled retention |
| Approved clinical guidance | Internal or licensed clinical content | Usage-rights validation, effective dates and version control |
| Prompts, drafts, citations and feedback | Restricted when patient-linked | Segregated audit access, redacted views and defined retention |
| Safety and quality metrics | Internal; potentially Restricted per event | Aggregate broadly; restrict case drill-down |

Data owners determine actual classification, purpose, notice, access, transfer and deletion. Free-text de-identification requires validation.

## 8. Logical Architecture

```text
Clinical record workspace
          |
          v
Identity + care-context authorisation
          |
          v
Minimal clinical-view service <----- Approved health-record sources
          |                                      |
          |                                      +--> Provenance / terminology services
          v
Approved guideline retriever <------ Versioned clinical corpus
          |
          v
Prompt/orchestration service --> AI Gateway --> Approved model
          |
          v
Clinical safety + citation + schema validators
          |
          v
Clinician review with source spans --> Established record-signing workflow
          |
          +--> Restricted audit store / safety, quality, security and cost monitoring
```

## 9. Controls and Evidence

| Control objective | Design control | Evidence |
|---|---|---|
| Clinical accountability | Mandatory review and intended-use boundary | Edits and signed-record reference |
| Factual grounding | Sentence-level provenance and resolvable source spans | Source IDs, retrieved spans and validator results |
| Safety | Hazard analysis, prohibited-output rules and clinical stop conditions | Hazard log, evaluation report and incident decisions |
| Privacy and security | Minimal view, contextual access, injection tests and no model write access | Data contract, access logs, red-team record and alerts |
| Controlled change | Versioned model, prompts, corpus and terminology | Release approval and regression results |

## 10. Failure, Fallback and Recovery

An unresolved source gap, validator failure or safety breach produces no usable summary. A circuit breaker can withdraw generation while preserving the record and manual review. Incident handling protects confidentiality and identifies affected drafts. Re-entry requires impact assessment, corrective action and repeated clinical, security and regression evaluation. Cached summaries expire with their encounter or source version.

## 11. Evaluation and Acceptance

Use authorised de-identified data where suitable and synthetic rare or adversarial cases. Include long histories, contradictions, negation, dosage and units, missing feeds and varied care contexts. Independent clinicians assess support, completeness, chronology, prominent safety facts, citations and misleading language.

Pre-approved thresholds cover critical omissions and fabrications, support, chronology, citations, material edits, latency and fallback. Report by context, not only averages. Test record-borne injection, cross-patient access and extraction. A severe directive, privacy breach or cross-patient disclosure stops the pilot.

## 12. Value Hypothesis

**Hypothesis:** a source-linked draft will reduce avoidable record-navigation effort while maintaining or improving information completeness and without degrading clinical safety.

| Measure | Baseline to establish | Prospective acceptance target |
|---|---|---|
| Preparation time | Current workflow by care context | Improvement set after baseline; no outcome claimed |
| Material omissions | Independent review of existing summaries | Non-inferior or better; no critical omission in acceptance set |
| Clinician burden | Approved survey and task measures | Improvement without increased verification time |
| Safety events and near misses | Current reporting definition | No material deterioration; stop thresholds apply |

Record rework, alert fatigue, misplaced trust and workflow delay. Benefits remain hypotheses until governed comparison.

## 13. AI-ADM Mapping

| AI-ADM phase | Use-case output |
|---|---|
| Phases 0–A | Clinical hypothesis, stakeholders, intended use, risk and safety goals |
| Phase B | Consultation workflow, accountability, escalation and change impacts |
| Phase C | Sources, provenance, terminology, quality, privacy and data contract |
| Phases D–E | Retrieval, validation, evaluation, gateway, resilience and observability |
| Phase F | Clinical safety, privacy, security and assurance controls |
| Phases G–I | Restricted pilot, training, launch gate, rollback and conformance |
| Phase J | Reassessment after model, corpus, workflow, population or use change |

## 14. Related Resources

- [AIEA-201 — AI Architecture Development Method](../../05-Standards/AIEA-201-AI-ADM.md)
- [AIEA-G02 — Healthcare](../../06-Series%20Guide/AIEA-G02-Healthcare.md)
- [AI Data Privacy and PII](../../01-AI-Governance/06-AI-Data-Privacy-and-PII.md)
- [Risk Mitigation](../../01-AI-Governance/04-Risk-Mitigation.md)
- [AI System Card template](../../12-Templates/AI-System-Card-Template.md)
- [Data Contract template](../../12-Templates/Data-Contract-Template.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
- [AI Incident Report template](../../12-Templates/AI-Incident-Report-Template.md)
