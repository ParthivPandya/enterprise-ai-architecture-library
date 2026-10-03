# AI in the Enterprise Architecture Lifecycle Playbook

| Metadata | Description |
|---|---|
| **Purpose** | Show how AI can assist enterprise architecture work while preserving evidence, professional judgement and accountable decisions. |
| **Audience** | Enterprise, domain and solution architects; architecture practice leaders; business analysts; repository owners; and review boards. |
| **Use When** | Planning or performing architecture work, improving repository quality, comparing options, preparing reviews or examining operational feedback. |
| **Outputs** | Source-bound analyses, reviewed architecture artefacts, decision evidence, repository updates and recorded limitations. |
| **Content classification** | Workflow controls and review responsibilities are **Normative** for adopters. Suggested uses and examples are **Informative**. |

## 1. Operating rules — Normative

AI may accelerate discovery, synthesis, comparison and quality checking. It shall not be treated as the accountable architect, source of record or final decision-maker.

An adopting practice shall:

- use only information authorised for the selected service and purpose;
- identify source material and distinguish evidence from inference;
- require a competent person to review every artefact before architectural reliance;
- retain prompts, relevant context, model or service version and reviewed output where the decision warrants traceability;
- test important factual, numerical and dependency claims against authoritative sources;
- disclose material uncertainty, missing evidence and conflicting sources; and
- use the [Evaluation and Escalation](Evaluation-and-Escalation.md) route when output cannot be safely corrected in the normal workflow.

## 2. Lifecycle map — Normative

| Architecture activity | Suitable AI assistance — Informative | Human responsibility | Required output |
|---|---|---|---|
| Frame the concern | Cluster stakeholder questions; identify ambiguous terms; draft interview guides | Confirm scope, decision owner and affected groups | Architecture question and evidence plan |
| Discover the baseline | Extract entities and relationships; compare repository and documents; flag inconsistencies | Verify facts with system and process owners | Evidence-backed baseline view and issue list |
| Define outcomes and principles | Structure outcome statements; test principle conflicts; surface assumptions | Decide value, constraints and acceptable trade-offs | Outcome map, principles and measures |
| Develop options | Generate bounded alternatives; compare patterns; identify dependencies and failure modes | Ensure options are feasible and not artificially narrowed | Option set and comparison record |
| Create architecture | Draft views, interface contracts, data flows and decision records from approved facts | Own coherence across domains and approve content | Reviewed architecture package |
| Assess risk and compliance | Map stated requirements to design elements; generate review questions | Determine applicability and obtain specialist interpretation | Traceability matrix and unresolved questions |
| Plan change | Identify capability dependencies, transition constraints and sequencing choices | Decide organisational change and investment route | Dependency map and work packages |
| Govern implementation | Compare implementation evidence with decisions; identify deviation | Judge materiality and approve or reject exceptions | Conformance findings and decisions |
| Learn from operation | Summarise incidents, user feedback, cost and quality evidence | Interpret causes and authorise architecture change | Updated decisions, patterns and repository content |

## 3. Standard workflow — Normative

### Step 1: Define the decision

State the architecture decision, audience, permitted evidence, confidentiality boundary and required output format. If no decision is served, do not use AI merely to produce more documentation.

### Step 2: Prepare evidence

Create a source manifest with owner, date or version, authority and known limitations. Remove irrelevant personal or confidential information. Prefer retrieval from controlled sources to copying uncontrolled context.

### Step 3: Select assistance mode

| Mode | Appropriate use | Main control |
|---|---|---|
| Extract | Find specified facts in supplied sources | Quote and cite source location |
| Transform | Reformat approved content | Preserve meaning and identify omissions |
| Compare | Apply explicit criteria to alternatives | Use the same criteria and evidence for each option |
| Challenge | Search for assumptions, contradictions and failure modes | Treat findings as questions until verified |
| Generate | Draft new structure or candidate content | Mark inference and require full professional review |

### Step 4: Run a bounded prompt

Use the [Reusable Prompt and Workflow Library](Reusable-Prompt-and-Workflow-Library.md). Require the model to state missing evidence, avoid invented facts and return a structured output that can be reviewed.

### Step 5: Evaluate

Check source fidelity, completeness, architecture coherence, uncertainty, safety and usability. Reperform material calculations and verify links, system names, obligations and dependencies.

### Step 6: Decide and record

Accept, edit, reject or escalate the output. Record the reviewer, sources, material corrections and remaining limitations. Only the reviewed artefact enters the architecture repository.

## 4. Artefact-specific guidance — Normative

| Artefact | AI may help with | Reviewer shall verify |
|---|---|---|
| Stakeholder map | Candidate roles and concerns from approved records | Missing or misrepresented affected groups |
| Capability map | Normalise terms and find duplicates | Business ownership and capability boundaries |
| Application portfolio | Classify attributes and flag conflicting records | Source accuracy, lifecycle facts and dependencies |
| Data-flow view | Extract flows from interfaces and diagrams | Direction, sensitivity, trust boundary and retention |
| Principle catalogue | Compare proposed decisions with principles | Interpretation and authorised exceptions |
| Architecture decision record | Draft context, options and consequences | Decision rationale, evidence and accountable approval |
| Risk register | Suggest failure scenarios and control questions | Likelihood, consequence, applicability and treatment |
| Review report | Summarise evidence and group findings | Severity, required action and formal decision |

## 5. Repository safeguards — Normative

AI-generated content shall not overwrite authoritative repository content automatically. Proposed changes should be staged as a reviewable difference showing additions, removals and source references. The reviewer shall resolve naming conflicts, duplicates and inferred relationships before publication.

Sensitive repository queries should enforce the requesting user’s permissions. Retrieval indexes and generated embeddings shall follow the same information-handling rules as their source material.

## 6. Quality and escalation checklist — Normative

- [ ] A real architecture decision and accountable reviewer are identified.
- [ ] Sources are authorised, versioned and listed.
- [ ] The assistance mode matches the task.
- [ ] The prompt forbids invented facts and requests uncertainty.
- [ ] Claims and relationships can be traced to evidence.
- [ ] Important omissions, dissent and alternatives remain visible.
- [ ] Domain, security, privacy and operational implications are reviewed.
- [ ] Material calculations and obligation mappings are independently checked.
- [ ] Only reviewed content reaches the architecture repository.
- [ ] Unsafe, sensitive or irreconcilable output follows the escalation route.

## 7. Example hand-off — Informative

For an application rationalisation decision, an AI service can normalise application descriptions and group apparent duplicates. The architect then checks ownership, integrations, contractual constraints and business criticality with authoritative records. The output is a candidate comparison, not a retirement decision. This distinction preserves speed without converting uncertain similarity into an organisational commitment.

## Related links

- [WG3 reference set](README.md)
- [Reusable Prompt and Workflow Library](Reusable-Prompt-and-Workflow-Library.md)
- [Evaluation and Escalation](Evaluation-and-Escalation.md)
- [Pattern Catalogue](Pattern-Catalogue.md)
- [EA Practice Evolution Playbook](../../07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md)

