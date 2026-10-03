# AI Maturity Self-Assessment Instrument

| Metadata | Description |
|---|---|
| **Purpose** | Provide an evidence-based self-assessment of the organisational capabilities needed to select, govern, build and operate AI responsibly. |
| **Audience** | Organisational leaders, enterprise architects, AI and data leaders, risk and compliance functions, security teams, product owners and internal assurance teams. |
| **Use When** | Establishing a capability baseline, comparing business units, selecting improvement actions or checking whether a proposed AI operating model is supportable. |
| **Outputs** | Scored response set, evidence references, disagreements, capability heatmap inputs and prioritised gaps. |
| **Content classification** | Scoring rules and evidence requirements are **Normative** for adopters. Interpretation guidance is **Informative**. |

> This instrument is a diagnostic aid, not a certification, audit opinion or prediction of AI outcomes.

## 1. Scoring scale — Normative

Score each statement using the strongest level fully supported by evidence.

| Score | Meaning | Evidence expectation |
|---|---|---|
| **0 — Not evidenced** | The capability is absent, unknown or supported only by assertion. | No reliable evidence |
| **1 — Local** | The practice occurs in isolated teams or depends on individual effort. | One or more local examples |
| **2 — Repeatable** | A defined practice is used across the relevant scope with accountable ownership. | Procedure plus sampled operating evidence |
| **3 — Adaptive** | The practice is measured and improved using operational evidence. | Repeated evidence of review and controlled improvement |

Policies, purchased tools and job titles do not establish maturity unless their operation is evidenced. Use **Not assessed** when evidence cannot be accessed; do not convert it to zero or omit it from disclosure.

## 2. Assessment statements — Normative

### A. Strategy and value

| ID | Statement |
|---|---|
| A1 | AI uses begin with a defined organisational outcome, accountable owner and feasible non-AI alternative. |
| A2 | Value evidence includes quality, risk, adoption and full operating cost. |
| A3 | Portfolio decisions compare uses consistently and can stop or constrain uses whose evidence no longer supports them. |

### B. Governance and accountability

| ID | Statement |
|---|---|
| B1 | AI systems, including externally supplied and embedded capabilities, are inventoried with accountable owners. |
| B2 | Risk classification, decision rights, exceptions and evidence requirements are applied consistently. |
| B3 | Operational incidents and control findings produce governed changes to policy, patterns or systems. |

### C. Data and knowledge

| ID | Statement |
|---|---|
| C1 | Data and knowledge sources have ownership, provenance, quality rules, access controls and retention treatment. |
| C2 | Retrieval and generated outputs preserve user entitlements and source traceability. |
| C3 | Operational quality signals lead to controlled correction of data products and knowledge sources. |

### D. Architecture and engineering

| ID | Statement |
|---|---|
| D1 | AI solutions use explicit boundaries for channels, orchestration, models, data, tools and policy. |
| D2 | Reusable interfaces and patterns reduce duplication without forcing unsuitable uniformity. |
| D3 | Model, supplier and component changes can be evaluated, substituted or withdrawn safely. |

### E. Evaluation and assurance

| ID | Statement |
|---|---|
| E1 | Acceptance criteria cover use-specific quality, safety, security and important failure modes. |
| E2 | Evaluations are reproducible and independently challenged in proportion to consequence. |
| E3 | Operational cases and incidents improve controlled evaluation suites. |

### F. Security, privacy and resilience

| ID | Statement |
|---|---|
| F1 | Identity, least privilege, data minimisation and supplier boundaries are designed and tested. |
| F2 | Prompt injection, data disclosure, unsafe tool use and service failure are assessed. |
| F3 | Operators can contain, recover and learn from significant AI-related events. |

### G. People and operating model

| ID | Statement |
|---|---|
| G1 | Business, technical and control responsibilities are understood and accepted. |
| G2 | People have the domain and AI literacy needed for their decisions and oversight duties. |
| G3 | Cross-functional learning improves shared methods while preserving local domain accountability. |

### H. Platform, operations and economics

| ID | Statement |
|---|---|
| H1 | Approved model access, identity, policy, telemetry and cost attribution are available for relevant uses. |
| H2 | Monitoring links material risks to indicators, decision boundaries and response actions. |
| H3 | Architecture choices consider attributable cost, operational burden, reuse and exit. |

## 3. Evidence guide — Informative

| Dimension | Useful evidence | Weak evidence on its own |
|---|---|---|
| Strategy and value | Decision records, comparable outcome reviews, stop decisions | Idea lists, benefit claims |
| Governance | Inventory samples, classifications, approvals, exception records | Policy publication |
| Data | Data contracts, lineage, permission tests, quality issue closure | Data-platform purchase |
| Architecture | Reviewed views, interfaces, substitution tests | Reference diagram without adoption evidence |
| Evaluation | Versioned datasets, criteria, results, defect records | Demonstration or generic benchmark |
| Security and privacy | Threat models, access tests, exercises, incident learning | Unverified supplier statement |
| People | Accepted role decisions, observed review, competence evidence | Organisation chart |
| Platform and operations | Service contracts, traces, alert tests, cost records | Tool catalogue |

## 4. Assessment procedure — Normative

1. **Define scope:** State the organisational boundary and decision the assessment supports.
2. **Choose respondents:** Include business, architecture, data, delivery, operations and independent control perspectives.
3. **Collect evidence:** Reference source records; do not copy sensitive evidence unnecessarily.
4. **Score independently:** Each respondent records a score, evidence and uncertainty before discussion.
5. **Reconcile:** Discuss differences and adopt the lowest score fully supported across the agreed scope.
6. **Record exceptions:** Keep dissent and “Not assessed” responses visible.
7. **Produce the heatmap:** Apply the [Scorecard and Heatmap](Scorecard-and-Heatmap.md) rules.
8. **Select actions:** Use the [Score-to-Roadmap](Score-to-Roadmap.md) method.

## 5. Response sheet — Normative

| Field | Entry |
|---|---|
| Scope and decision | |
| Statement ID | |
| Proposed score | |
| Evidence references | |
| Evidence scope and limitations | |
| Respondent role | |
| Dissent or uncertainty | |
| Agreed score | |

## 6. Interpretation rules — Normative

- Do not average scores from materially different business units before showing their separate profiles.
- Do not infer that a high platform score compensates for weak accountability or evaluation.
- Treat a zero in a capability essential to a proposed use as a constraint requiring action or a narrower use.
- Compare scores only when scope, statements and scoring rules are equivalent.
- Reassess affected statements after material organisational, architectural or risk change.

## 7. Completion checklist — Normative

- [ ] Scope and decision are explicit.
- [ ] All relevant perspectives contributed.
- [ ] Every numeric score has evidence.
- [ ] “Not assessed” is visible and explained.
- [ ] Dissent and uneven capability remain visible.
- [ ] Sensitive evidence is referenced with controlled access.
- [ ] Scores are not represented as certification or performance guarantees.
- [ ] Actions follow risk and dependency rather than score alone.

## Related links

- [WG4 reference set](README.md)
- [Scorecard and Heatmap](Scorecard-and-Heatmap.md)
- [Facilitation Playbook](Facilitation-Playbook.md)
- [Score-to-Roadmap](Score-to-Roadmap.md)
- [Enterprise AI Readiness Assessment Toolkit](../../07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md)

