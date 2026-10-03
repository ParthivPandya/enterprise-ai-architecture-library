# AIEA Series Guide
## AIEA-G12: Defence & Education AI
### Document Number: AIEA-G12 | Version 1.0 | 2026

| Metadata | Detail |
|---|---|
| Document type | Independent combined sector reference guide |
| Audience | Defence enterprise and solution architects working on non-weaponised support capabilities; education leaders, educators, safeguarding and student-support teams, architects, data and AI teams, and governance functions |
| Use when | Designing, procuring, assuring, deploying, or reviewing AI in the in-scope defence-support or education contexts defined below |
| Scope | Part A: non-weaponised logistics, readiness, document analysis, defensive cyber support, and training. Part B: teaching, learning, assessment support, research, administration, and learner services |
| Last verified | October 2026 |
| Standing | Independent guidance, not law, operational doctrine, an authorisation to deploy, a safety or security accreditation, a child-safeguarding determination, or a declaration of compliance |

---

## Preface

This document is an independent AIEA Series Guide supplementing the core AIEA Reference Framework. It elevates two high-stakes domains — **defence** and **education** — into a dedicated guide, building on the material in the library's strategy section ([02-AI-Strategy/03](../02-AI-Strategy/03-Education-and-Defence.md)).

These domains sit at opposite ends of a spectrum but share a trait: AI decisions carry outsized human consequences — national security on one side, the formation of learners on the other. Both demand exceptional governance, sovereignty, and human authority.

This guide is intended for Enterprise Architects and governance leads supporting defence or education programmes. It extends [AIEA-101](../05-Standards/AIEA-101-Introduction-Core-Concepts.md) and complements [AIEA-G06: Sovereign AI](AIEA-G06-Sovereign-AI.md) and [AIEA-G10: Government & Public Sector AI](AIEA-G10-Government-Public-Sector-AI.md).

---

## Part A — Defence AI

### A.1 Context

Defence AI spans decision support, logistics, intelligence analysis, cyber defence, and training simulation. The non-negotiable constraint is **meaningful human control**: AI informs and accelerates, but human authority over consequential action is absolute.

#### A.1.1 Scope boundary

Part A is intentionally **non-weaponised**. It covers support functions such as inventory and maintenance planning, readiness analysis, authorised document triage, defensive cyber detection, enterprise knowledge assistance, and instructor-governed simulation. It does not provide architecture or implementation guidance for target selection, weapon control, engagement decisions, lethal force, autonomous weapons, or techniques intended to cause physical or cyber harm. Those matters require separate legal, policy, ethical, operational, safety, and command processes outside this guide.

The [NATO revised AI strategy](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2024/07/10/summary-of-natos-revised-artificial-intelligence-ai-strategy) sets out principles including lawfulness, accountability, explainability, traceability, reliability, governability, and bias mitigation. The [United States Department of Defense Responsible AI Strategy and Implementation Pathway](https://media.defense.gov/2022/Jun/22/2003022604/-1/-1/0/Department-of-Defense-Responsible-Artificial-Intelligence-Strategy-and-Implementation-Pathway.PDF) is a further lifecycle reference. Neither substitutes for the authority governing a particular organisation or mission.

### A.2 Governance Imperatives

| Imperative | Requirement |
|---|---|
| Meaningful human control | No AI-initiated consequential action without human authority (Principle D4, maximal) |
| Sovereignty | Sovereign infrastructure and models; strict data residency ([AIEA-G06](AIEA-G06-Sovereign-AI.md)) |
| Assurance | Rigorous evaluation, red teaming, and adversarial robustness |
| Classification | Data classification and strict segmentation enforced in architecture |
| Explainability | Analysts must be able to interrogate the basis of AI outputs |

### A.3 Reference Use Cases (non-weaponised, support-oriented)

| Use Case | Pattern | Human Control |
|---|---|---|
| Logistics and readiness optimisation | Forecasting + planning support | Human-approved |
| Intelligence document triage | Extraction + classification | Analyst adjudication |
| Cyber-defence anomaly detection | Detection + analyst response | Human-led response |
| Training simulation | Scenario generation | Instructor-governed |

### A.4 Defence Architecture Views

#### Context and authority view

Identify the mission-support owner, authorised users, analyst or planner, data owners, security authority, operational risk owner, model and platform suppliers, assurance function, and the person empowered to suspend the service. Mark every point at which an AI output could influence a consequential decision. Record the human authority, independent evidence, and non-AI route at that point.

#### Classification and deployment view

Partition services by classification, releasability, mission, community of interest, and need to know. Show data stores, model weights, prompts, embeddings, indexes, logs, administrative planes, update route, remote support, and telemetry. Do not assume that a model approved in one environment can cross into another. Treat model files, retrieval indexes, evaluation sets, and generated output according to their content and applicable classification decisions.

Cross-domain movement uses authorised mechanisms and release processes. A model must not become an informal network bridge: summaries can reproduce, infer, or combine protected details. Disconnected operations need local identity, time, model, knowledge, logging, capacity, revocation, and safe loss-of-service behaviour.

#### Logical assurance view

Use a traceable chain:

```
authorised source -> provenance and classification check -> approved transformation
                  -> model/inference -> policy and security guard
                  -> analyst review against source evidence
                  -> authorised support decision -> protected record
```

Separate experimentation, training, evaluation, staging, and operational release. Promote signed, versioned artefacts through controlled transfer. The release package should include model and dependency provenance, configuration, evaluation results, intended and excluded uses, known limitations, threat assessment, approval, and rollback material.

### A.5 Defence Control Set

| Control area | Defence-support requirement |
|---|---|
| Purpose and authority | Defined support task, lawful and policy basis, accountable authority, excluded uses, and stop authority |
| Human control | User can interrogate sources, reject output, seek review, and continue safely without the model |
| Data and classification | Need-to-know access, provenance, releasability, minimisation, approved labelling, retention, and spill response |
| Supply chain | Provenance of weights, data, libraries, hardware and updates; integrity verification; vulnerability and support process |
| Adversarial robustness | Threat model covering evasion, poisoning, prompt injection, extraction, model theft, spoofing, and manipulated source material |
| Model release | Representative mission-support evaluation, segregation of duties, signed artefact, configuration control, and rollback |
| Interfaces and tools | Allow-listed schemas, least privilege, short-lived credentials, rate limits, two-person or role approval where required |
| Monitoring | Security, quality, drift, anomalous use, policy violations, degraded dependencies, and protected audit records |
| Incident response | Isolation, evidence preservation, classification-aware handling, operational notification, supplier coordination, and re-authorisation |
| Withdrawal | Ability to revoke a model, knowledge source, user, credential, tool, or entire service without disabling the supported function |

Authorised, scoped red teaming should test leakage, adversarial content, source manipulation, deceptive confidence, unsafe tool requests, and over-reliance, with remediation and protected operational data.

### A.6 Defence Implementation Patterns

**Logistics and readiness support.** Combine governed asset, demand, maintenance, and supply data; expose assumptions and uncertainty; and let authorised planners decide. Avoid optimising a proxy such as nominal availability while hiding cannibalisation, deferred maintenance, safety, or supply fragility.

**Document triage and analysis.** Apply source authentication, classification and releasability checks before inference. Preserve page-level citations and distinguish translation, extraction, entity resolution, summarisation, and analytic judgement. Analysts verify against source material; generated text is not new intelligence merely because it is fluent.

**Defensive cyber support.** Use AI to correlate authorised defensive telemetry, enrich alerts, explain detections, or draft response steps. Analysts validate evidence and execute under established defensive authorities. Tool access is bounded to approved defensive systems; the model cannot improvise actions or cross security boundaries.

**Training simulation.** Instructors select learning objectives, approve scenarios, identify synthetic material, and control difficulty and debrief. Separate simulation from operational systems and prevent generated scenario details from being mistaken for current operational information.

### A.7 Defence Failure Modes and Evaluation

| Failure mode | Control response |
|---|---|
| Protected data appears in prompts, output, embeddings, or telemetry | Classification-aware handling, access filtering, minimised logs, spill procedure, environment isolation |
| Manipulated source drives a false analytic conclusion | Provenance, source diversity, content inspection, citations, adversarial evaluation |
| Model behaves differently after an update | Controlled versioning, fixed regression set, change impact assessment, rollback |
| Analyst over-trusts confident output | Uncertainty and source display, challenge training, independent corroboration, sampled review |
| Edge service is stale or disconnected | Package expiry, freshness display, local fallback, controlled resynchronisation |
| Supplier or component compromise | Integrity checks, component inventory, isolated acceptance, revocation, alternative route |
| Tool call exceeds authority | Allow-list, least privilege, approval, deterministic validation, immutable audit |

The governing authority sets thresholds. Measures include citation correctness, error severity, calibration, abstention, adversarial performance, blocked data-spill attempts, unauthorised tool requests, update regression, analyst disagreement, override, degraded service, and recovery. Break results down by source, language, environment, task, and threat.

### A.8 Defence Adoption Guidance

Move from offline evaluation, to a protected experiment, to shadow support, to limited operational assistance only when the preceding evidence is accepted. Start read-only. Exercise compromise, disconnection, revocation, rollback, and human continuation before operational use. Re-authorise after material changes to purpose, environment, data, threat, model, tools, or supplier. Adoption is an assurance decision.

---

## Part B — Education AI

### B.1 Context

Education AI includes tutoring assistants, content generation, assessment support, and administration. The core constraint is **learner welfare and integrity**: AI should support learning and educators, not undermine integrity, equity, or child safety.

### B.2 Governance Imperatives

| Imperative | Requirement |
|---|---|
| Child safety | Age-appropriate design; strong safety guardrails; minors' data protection |
| Academic integrity | Clear rules on AI use; detection-aware but fairness-first |
| Equity | Works across languages, abilities, and access conditions |
| Educator authority | Teachers remain accountable for assessment and progression |
| Explainability | Learners and parents can understand AI-influenced outcomes |

### B.3 Reference Use Cases

| Use Case | Pattern | Risk Tier |
|---|---|---|
| Grounded tutoring assistant | RAG over approved curriculum | Limited |
| Content and lesson generation | LLM + educator review | Limited |
| Formative assessment support | ML scoring + educator adjudication | High (if it affects progression) |
| Administrative automation | Workflow automation | Limited |

### B.4 Data Protection for Minors

Section 9 of India's [Digital Personal Data Protection Act, 2023](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023) addresses processing children's personal data, including verifiable parental consent and restrictions concerning detrimental processing, tracking, behavioural monitoring, and targeted advertising, subject to the Act's definitions, notified rules, exemptions, and applicability. Determine the current legal position for the institution and service rather than treating this summary as advice. Complete the [DPDPA Compliance Checklist](../12-Templates/DPDPA-Compliance-Checklist.md) with child rights, minimisation, safeguarding, and applicable consent or authorisation foregrounded.

### B.5 Education Architecture Views

#### Learner and authority view

Map learners, parents or guardians where relevant, educators, safeguarding staff, assessors, administrators, disability support, institutional leadership, suppliers, and regulators or awarding bodies. For each use, identify who is affected, who sees the output, who can correct it, and who is accountable. Educator review must be genuine: a teacher needs source evidence, time, competence, and authority to disagree.

#### Learning-service view

```
age/role-appropriate identity
    -> approved learning task and content boundary
    -> curriculum or course retrieval
    -> model with safety and privacy controls
    -> learner/educator interaction
    -> escalation, feedback, and safeguarding route
    -> minimal learning and assurance record
```

Separate the learning platform, student-information system, assessment system, safeguarding case system, and model provider. Integrate only the data required for the stated purpose. A tutoring assistant does not need unrestricted access to pastoral records; an administrative extraction service does not need to profile learner behaviour.

#### Content and assessment view

Approved learning content should have an owner, curriculum or course context, validity status, language, accessibility information, and rights for use. Retrieval preserves source permissions and citations. Generated materials pass educator review for factual accuracy, level, representation, safety, accessibility, and copyright risk.

Keep formative assistance distinct from summative judgement. Where AI supports assessment, document the construct being assessed, permitted learner use, evidence available to the assessor, review and moderation, correction route, and effect on progression. Do not infer misconduct from an AI-detection score alone.

### B.6 Child Safety, Integrity, and Sector Controls

The [UNICEF Policy Guidance on AI for Children](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children) frames child-centred AI around safety, privacy, fairness, transparency, accountability, inclusion, well-being, and children's rights. The [UNESCO Guidance for Generative AI in Education and Research](https://unesdoc.unesco.org/ark:/48223/pf0000386692) provides a further authoritative reference for human-centred use. Convert these principles into controls:

| Control area | Education requirement |
|---|---|
| Age and role | Age-appropriate experience, role-based capabilities, clear boundaries, and no adult feature silently exposed to children |
| Safeguarding | Visible reporting, trained human response, escalation for self-harm, abuse, grooming, sexual content, bullying, or other risk; no model-only safeguarding decision |
| Privacy | Purpose limitation, minimum learner data, approved retention, protected records, supplier restrictions, and no unnecessary profiling |
| Academic integrity | Clear course-level rules, disclosure expectations, assessment redesign where needed, evidence-based investigation, and human due process |
| Educator authority | Educator approves materials and consequential assessment; model supports rather than replaces professional judgement |
| Fairness and inclusion | Evaluation across language, disability, age, subject, device, connectivity, and other contextually relevant groups |
| Accessibility | Assess [WCAG 2.2](https://www.w3.org/TR/WCAG22/), assistive technology, alternative formats, captions, keyboard use, cognitive accessibility, and accommodation processes |
| Grounding | Approved curriculum or course sources, citations, version validity, and refusal where support is absent |
| Commercial influence | No undisclosed advertising, manipulative engagement, or recommendation shaped by a commercial interest |
| Records and challenge | Understandable notice, output correction, educator review, learner complaint or appeal route, and evidence for material decisions |

Academic integrity is an educational and assessment-design issue, not merely a detection problem. State whether brainstorming, translation, coding, editing, tutoring, or generation is allowed; teach citation and disclosure; use authentic process evidence where appropriate; and investigate suspected misconduct under established procedure. Detection tools can be uncertain and uneven across language groups, so their output should be treated as a signal requiring corroboration, never sole proof.

### B.7 Education Implementation Patterns

**Grounded tutoring assistant.** Limit content to the course or curriculum, adapt explanation without impersonating an educator, use age-appropriate safety behaviour, cite sources, and hand off persistent confusion or welfare concerns. Avoid engagement mechanics that encourage dependency or unnecessary disclosure.

**Educator content assistant.** Generate drafts for lesson plans, examples, rubrics, or accessible variants. The educator checks accuracy, level, representation, rights, and local context. Do not upload identifiable learner work unless the service and purpose are approved.

**Formative feedback.** Provide suggestions tied to a rubric and show uncertainty. The learner can question feedback and the educator can override it. Do not convert a formative model score into a progression decision without a separately governed assessment design.

**Administrative processing.** Use schema-constrained extraction, validation, access control, and sampled review for admissions or records workflows. Missing or unreadable evidence is routed for clarification, not treated as an adverse fact.

### B.8 Education Failure Modes and Evaluation

| Failure mode | Control response |
|---|---|
| Hallucinated teaching content | Approved retrieval, citations, educator review, learner correction route |
| Unsafe or developmentally unsuitable interaction | Age-aware design, tested safety policy, reporting, trained human escalation |
| Learner overshares sensitive information | Just-in-time warnings, data minimisation, redaction, restricted retention |
| Bias lowers expectations or opportunities | Disaggregated evaluation, educator authority, inclusive content review, challenge route |
| Integrity detector falsely accuses | No sole reliance, corroborating evidence, fair procedure, appeal |
| Tool replaces productive struggle | Learning-objective design, hints before answers, educator-configured support |
| Inaccessible interface or content | WCAG and assistive-technology testing, alternatives, accommodation support |
| Vendor trains on learner data unexpectedly | Contract and tenant controls, supplier review, monitoring, deletion and exit |

Evaluate learning and safety, not engagement alone. Measures may include curriculum-supported answer rate, citation correctness, severe factual error, harmful-content response, safeguarding escalation success, accessibility task completion, educator correction, learner challenge resolution, assessment moderation disagreement, privacy events, and service availability. Learning measures should align with the intended construct and compare with an appropriate non-AI baseline; usage volume is not evidence of learning.

Slice evidence by age, subject, language, disability and access needs, device, and context while protecting privacy and avoiding invalid small samples. Add feedback from learners, relevant guardians, educators, safeguarding specialists, and disability support.

### B.9 Education Adoption Guidance

Begin with educator-facing or low-consequence administrative assistance, then bounded learner support, and only later consider consequential assessment support. Each step requires a defined educational purpose, data and child-rights assessment, supplier review, representative safety and accessibility testing, educator training, learner-facing rules, support and complaint routes, fallback, and a withdrawal plan. Pilot participation should not determine grades or access to support. Reassess when the learner population, course, model, data use, safety controls, or assessment policy changes.

---

## Chapter C: Shared Principles

Both domains share three architectural commitments:

1. **Human authority is absolute** over consequential outcomes (Principle D4).
2. **Sovereignty and data protection** are designed in from the first decision (Principle D5).
3. **Assurance and explainability** scale with consequence (Principles G3, O1).

The two parts must not be collapsed into a single control profile. Defence classification and adversarial mission conditions differ fundamentally from child rights, pedagogy, safeguarding, and academic integrity. What they share is a disciplined architecture: purpose before technology, minimum necessary data and agency, an accountable human decision path, independent protection and fallback, evidence proportionate to consequence, controlled change, and the ability to stop.

---

## References

The following sources were checked in October 2026. Confirm the current version, legal status, national or institutional adoption, and applicability:

### Defence references

- [NATO revised Artificial Intelligence strategy](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2024/07/10/summary-of-natos-revised-artificial-intelligence-ai-strategy)
- [United States Department of Defense Responsible AI Strategy and Implementation Pathway](https://media.defense.gov/2022/Jun/22/2003022604/-1/-1/0/Department-of-Defense-Responsible-Artificial-Intelligence-Strategy-and-Implementation-Pathway.PDF)
- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)
- [NIST SP 800-53 Rev. 5: Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

### Education and child-rights references

- [Digital Personal Data Protection Act, 2023 — Ministry of Electronics and Information Technology](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023)
- [UNESCO Guidance for Generative AI in Education and Research](https://unesdoc.unesco.org/ark:/48223/pf0000386692)
- [UNESCO Recommendation on the Ethics of Artificial Intelligence](https://unesdoc.unesco.org/ark:/48223/pf0000381137)
- [UNICEF Policy Guidance on AI for Children](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children)
- [Web Content Accessibility Guidelines 2.2 — W3C](https://www.w3.org/TR/WCAG22/)
- [Convention on the Rights of the Child — United Nations](https://www.ohchr.org/en/instruments-mechanisms/instruments/convention-rights-child)
- [Family Educational Rights and Privacy Act resources — United States Department of Education](https://studentprivacy.ed.gov/ferpa)
- [Children's Online Privacy Protection Rule — United States Federal Trade Commission](https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa)
- [Regulation (EU) 2016/679, General Data Protection Regulation — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

---

*AIEA Series Guide AIEA-G12: Defence & Education AI. Version 1.0, 2026.*
