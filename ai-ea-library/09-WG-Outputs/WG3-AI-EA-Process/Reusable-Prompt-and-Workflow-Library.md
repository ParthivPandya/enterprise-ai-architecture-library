# Reusable Prompt and Workflow Library

| Metadata | Description |
|---|---|
| **Purpose** | Provide reusable, source-bound prompts for common enterprise architecture activities. |
| **Audience** | Enterprise, domain and solution architects, business analysts, repository curators and architecture reviewers. |
| **Use When** | Extracting facts, comparing options, drafting artefacts, challenging designs or checking repository consistency with an approved AI service. |
| **Outputs** | Structured draft, source references, assumptions, missing evidence, review questions and evaluation record. |
| **Content classification** | Prompt safeguards and review workflow are **Normative** for adopters. Prompt templates are **Informative** starting points that must be tailored. |

## 1. Safe-use wrapper — Normative

Before using a prompt:

- confirm that the selected service is approved for the information;
- remove irrelevant personal, confidential and secret material;
- give sources stable identifiers such as `S1`, `S2` and `S3`;
- state the architecture decision and intended reader;
- require the output to separate sourced fact, inference and recommendation; and
- appoint a competent reviewer.

Append this instruction to every prompt:

```text
Use only the supplied sources for factual claims. Cite the source identifier
and location for each material claim. Do not invent systems, relationships,
requirements, measures or decisions. Mark any inference as INFERENCE and
state its basis. Put missing, conflicting or ambiguous evidence in an
OPEN QUESTIONS section. If the requested task cannot be completed from the
sources, say so rather than filling gaps. Return the requested structure only.
```

## 2. Workflow — Normative

1. **Prepare:** Define decision, audience, sources, exclusions and output schema.
2. **Run:** Use one bounded task rather than combining unrelated analysis.
3. **Inspect:** Check citations, unsupported claims, omissions and sensitive output.
4. **Verify:** Compare material statements with authoritative sources.
5. **Challenge:** Use a separate review prompt or human reviewer to test assumptions.
6. **Decide:** Accept, edit, reject or escalate.
7. **Record:** Retain the reviewed artefact and proportionate trace evidence.

## 3. Prompt A — Architecture baseline extraction — Informative

```text
ROLE: You are assisting an enterprise architect with evidence extraction.
DECISION: [state the decision this baseline supports]
SOURCES: [paste or attach labelled sources]

TASK:
Extract only explicitly supported facts about:
1. business capabilities and owners;
2. applications and services;
3. data created, read, changed or shared;
4. integrations and external dependencies;
5. stated constraints and known issues.

OUTPUT:
- FACT TABLE: entity | type | fact | source | confidence reason
- RELATIONSHIP TABLE: from | relationship | to | source
- CONFLICTS
- OPEN QUESTIONS
- REVIEW PRIORITIES

[safe-use wrapper]
```

Review by sampling every high-consequence relationship and any item used to support retirement, consolidation or control decisions.

## 4. Prompt B — Stakeholder and concern map — Informative

```text
ROLE: You are structuring supplied stakeholder evidence, not identifying people.
ARCHITECTURE QUESTION: [question]
SOURCES: [labelled interview notes, role descriptions and service records]

TASK:
Group evidence by organisational role. Identify stated concerns, decisions,
information needs, affected outcomes and unresolved disagreement. Do not infer
authority from job title alone.

OUTPUT:
role | stated concern | decision or influence | evidence needed | source
Then provide: MISSING PERSPECTIVES, CONFLICTS, OPEN QUESTIONS.

[safe-use wrapper]
```

## 5. Prompt C — Option comparison — Informative

```text
ROLE: You are comparing architecture options using fixed criteria.
DECISION: [decision]
OPTIONS: [option descriptions]
CRITERIA: [value, risk, data, interoperability, operability, cost, exit, other]
SOURCES: [labelled evidence]

TASK:
Apply every criterion to every option. Distinguish evidence from assumption.
Do not rank an option when evidence is insufficient.

OUTPUT:
1. COMPARISON MATRIX: criterion | option | evidence | consequence | uncertainty
2. TRADE-OFFS that cannot be optimised simultaneously
3. DISQUALIFYING CONSTRAINTS
4. EVIDENCE NEEDED
5. CONDITIONAL RECOMMENDATION, or NO RECOMMENDATION if unsupported

[safe-use wrapper]
```

## 6. Prompt D — Architecture decision record draft — Informative

```text
ROLE: You are drafting an architecture decision record from an approved decision.
DECISION EVIDENCE: [minutes, option assessment and approval]
CONTEXT SOURCES: [labelled sources]

TASK:
Draft: context, decision, alternatives considered, rationale, positive
consequences, negative consequences, assumptions, implementation constraints,
reconsideration triggers and evidence references.

Do not create rationale that is absent from the decision evidence. Mark missing
elements as OPEN QUESTION.

[safe-use wrapper]
```

## 7. Prompt E — Design challenge — Informative

```text
ROLE: You are a critical architecture reviewer.
DESIGN: [architecture description and views]
REQUIREMENTS: [labelled requirements and principles]

TASK:
Identify possible contradictions, single points of failure, permission
escalation, data-boundary gaps, supplier concentration, unsafe failure,
unobservable behaviour and difficult exit. Frame each finding as a testable
review question unless directly proven.

OUTPUT:
finding | evidence | consequence | review question | suggested test
Then provide: ASSUMPTIONS, MISSING VIEWS, POSITIVE PROPERTIES.

[safe-use wrapper]
```

## 8. Prompt F — Repository consistency check — Informative

```text
ROLE: You are checking repository records for consistency.
METAMODEL RULES: [allowed types, relationships and mandatory attributes]
RECORDS: [exported, access-controlled records]

TASK:
Find duplicate identifiers, conflicting attributes, orphan records, invalid
relationships, missing mandatory fields and terms that may be synonyms.
Do not merge, delete or overwrite records.

OUTPUT:
issue type | record identifiers | evidence | proposed reviewer action
Then provide a separate POSSIBLE SYNONYMS table with reasons.

[safe-use wrapper]
```

## 9. Output evaluation rubric — Normative

| Criterion | Acceptable evidence |
|---|---|
| Source fidelity | Material claims trace to the supplied source |
| Completeness | Required sections are present; omissions are disclosed |
| Separation | Fact, inference and recommendation are distinguishable |
| Architecture coherence | Terms and relationships follow the supplied metamodel |
| Uncertainty | Conflict and missing evidence remain visible |
| Safety and confidentiality | Output does not expose or expand sensitive content |
| Usefulness | A reviewer can take a defined next action |

Any invented material fact, concealed source conflict or unsafe disclosure is a rejection condition.

## 10. Reviewer checklist — Normative

- [ ] The service and data use are authorised.
- [ ] The decision and output schema are explicit.
- [ ] Sources have stable identifiers and authority.
- [ ] The prompt contains the safe-use wrapper.
- [ ] Citations were checked against source content.
- [ ] Numbers, obligations and critical dependencies were reverified.
- [ ] Recommendations follow evidence rather than fluency.
- [ ] Sensitive output is handled at the source classification.
- [ ] Only the reviewed version enters the repository.

## Related links

- [WG3 reference set](README.md)
- [AI in the EA Lifecycle Playbook](AI-in-EA-Lifecycle-Playbook.md)
- [Evaluation and Escalation](Evaluation-and-Escalation.md)
- [Pattern Catalogue](Pattern-Catalogue.md)

