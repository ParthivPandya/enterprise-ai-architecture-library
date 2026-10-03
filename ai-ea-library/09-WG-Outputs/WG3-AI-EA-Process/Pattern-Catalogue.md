# AI-in-EA Pattern Catalogue

| Metadata | Description |
|---|---|
| **Purpose** | Provide reusable patterns for applying AI to enterprise architecture work with clear boundaries and review controls. |
| **Audience** | Architecture practitioners, practice leaders, repository owners, platform teams and governance reviewers. |
| **Use When** | Selecting an AI-assisted workflow, comparing intervention options or defining reusable EA tooling. |
| **Outputs** | Selected pattern, source and control requirements, human review point, fallback and evaluation criteria. |
| **Content classification** | Pattern boundaries and safeguards are **Normative** for adopters. Pattern descriptions and examples are **Informative**. |

## 1. Pattern selection rules — Normative

Select the least generative pattern that can meet the need. Deterministic search, validation or repository queries should be preferred when they can answer the question reliably. Every pattern shall define:

- the architecture decision it supports;
- authorised sources and information boundary;
- what AI may and may not do;
- accountable reviewer and decision authority;
- evaluation and rejection conditions;
- fallback when AI is unavailable or unreliable; and
- evidence retained.

## 2. Catalogue summary — Informative

| ID | Pattern | Best used for | AI role | Human decision point |
|---|---|---|---|---|
| EA-01 | Evidence Extractor | Turning documents into traceable facts | Extract | Verify material facts |
| EA-02 | Repository Reconciler | Finding inconsistent architecture records | Compare | Approve every change |
| EA-03 | View Drafting Assistant | Producing a first structured architecture view | Transform and generate | Validate entities, relationships and scope |
| EA-04 | Option Challenger | Exposing trade-offs and failure modes | Challenge | Judge feasibility and choose |
| EA-05 | Principle Conformance Reviewer | Testing design statements against principles | Compare | Interpret principle and exception |
| EA-06 | Decision Record Curator | Structuring an approved decision | Transform | Confirm rationale and approval |
| EA-07 | Operational Evidence Synthesiser | Connecting incidents and telemetry to architecture | Summarise | Determine cause and architecture response |
| EA-08 | Natural-Language Repository Guide | Helping readers find governed EA content | Retrieve and explain | Apply retrieved content to the decision |

## 3. EA-01 — Evidence Extractor

**Problem — Informative:** Architecture facts are distributed across approved documents and use inconsistent terms.

**Pattern — Normative:** The service extracts entities, attributes, relationships and quotations into a staging table. Every row carries a source identifier and location. It may suggest synonyms but shall not invent or merge records.

| Element | Requirement |
|---|---|
| Inputs | Labelled, authorised sources and extraction schema |
| Outputs | Fact table, relationship table, conflicts and open questions |
| Controls | Citation requirement, schema validation, sensitive-data handling |
| Evaluation | Source fidelity and coverage sample |
| Fallback | Manual extraction or deterministic parser |

## 4. EA-02 — Repository Reconciler

**Problem — Informative:** Duplicate, orphaned or conflicting repository entries reduce trust.

**Pattern — Normative:** Export only the records the reviewer may access. AI identifies possible inconsistencies and proposes review actions. All write, merge and deletion operations remain outside the model workflow until explicitly approved.

**Do not use** similarity alone to conclude that two applications, capabilities or data objects are identical.

## 5. EA-03 — View Drafting Assistant

**Problem — Informative:** Creating a first view from verified facts is repetitive.

**Pattern — Normative:** Generate a draft in the organisation’s metamodel from an approved fact table. Mark inferred relationships visually or in a separate list. Validate syntax automatically where possible and require the architect to confirm semantic correctness.

| Review focus | Question |
|---|---|
| Scope | Does the view answer the stated concern? |
| Semantics | Are element types and relationships valid? |
| Evidence | Can each material element be traced? |
| Omission | Which affected domain or stakeholder is absent? |

## 6. EA-04 — Option Challenger

**Problem — Informative:** Teams converge on a preferred design before examining alternatives.

**Pattern — Normative:** Give the service fixed options, criteria and evidence. Ask for contradictions, failure modes, dependencies and conditions under which each option is unsuitable. The service shall not rank an option where material evidence is missing.

The architect owns feasibility, weighting and recommendation. Use the pattern to broaden questions, not outsource judgement.

## 7. EA-05 — Principle Conformance Reviewer

**Problem — Informative:** Design reviews apply architecture principles inconsistently.

**Pattern — Normative:** Compare explicit design statements with the exact text and implications of approved principles. Return **supported**, **possible conflict** or **insufficient evidence**, with citations. Only authorised governance roles may decide conformance or approve an exception.

## 8. EA-06 — Decision Record Curator

**Problem — Informative:** Important decisions are poorly structured after meetings.

**Pattern — Normative:** Draft a decision record only from approved minutes, option evidence and the recorded decision. Missing rationale stays missing and becomes an open question; it shall not be reconstructed from plausibility.

Required sections are context, decision, alternatives, rationale, consequences, assumptions, reconsideration triggers and evidence.

## 9. EA-07 — Operational Evidence Synthesiser

**Problem — Informative:** Incidents, service data and feedback do not reliably inform architecture.

**Pattern — Normative:** Summarise de-identified or appropriately controlled evidence by architecture component, failure mode and affected outcome. Separate correlation from established cause. Route suspected safety, privacy or security events through the relevant incident process before wider synthesis.

## 10. EA-08 — Natural-Language Repository Guide

**Problem — Informative:** Readers cannot locate or interpret relevant repository content.

**Pattern — Normative:** Retrieve only content permitted to the user, cite the repository record and distinguish approved content from explanation. The interface shall not represent generated interpretation as an approved architecture decision.

## 11. Anti-patterns — Normative

| Anti-pattern | Why it fails | Safer response |
|---|---|---|
| Autonomous repository editor | Errors become authoritative and difficult to detect | Stage a difference for human approval |
| Architecture oracle | Fluent answers conceal missing organisational context | Require sources, uncertainty and accountable judgement |
| Unbounded document upload | Sensitive and irrelevant content crosses service boundaries | Curate and minimise the evidence set |
| Synthetic consensus | Minority concerns disappear in summarisation | Preserve dissent and source attribution |
| Compliance-by-keyword | Text similarity is mistaken for applicability | Route interpretation to competent specialists |
| Diagram as proof | A plausible view is treated as evidence of actual structure | Trace elements to authoritative records |

## 12. Pattern record — Normative

- [ ] Decision and intended reader
- [ ] Pattern ID and reason for selection
- [ ] Sources, permissions and exclusions
- [ ] Prompt and output schema
- [ ] Evaluation and rejection conditions
- [ ] Human review and decision authority
- [ ] Fallback and escalation
- [ ] Evidence retained and repository destination

## Related links

- [WG3 reference set](README.md)
- [AI in the EA Lifecycle Playbook](AI-in-EA-Lifecycle-Playbook.md)
- [Reusable Prompt and Workflow Library](Reusable-Prompt-and-Workflow-Library.md)
- [Evaluation and Escalation](Evaluation-and-Escalation.md)
