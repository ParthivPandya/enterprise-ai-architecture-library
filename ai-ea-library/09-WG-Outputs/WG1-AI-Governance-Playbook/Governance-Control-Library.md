# Governance Control Library

| Metadata | Description |
|---|---|
| **Purpose** | Provide a testable, technology-neutral set of controls for governing enterprise AI systems. |
| **Audience** | Control owners, system owners, architects, risk and compliance teams, security and privacy functions, procurement teams and assurance reviewers. |
| **Use When** | Building a control plan, reviewing a supplier, preparing an authorisation decision, testing an operational system or investigating an incident. |
| **Outputs** | Applicable-control register, control owners, test procedures, evidence references, findings and approved exceptions. |
| **Content classification** | The control requirements and test rules are **Normative** for adopters. Framework mappings and examples are **Informative**. |

> **Important:** These mappings are informative, not legal interpretations, conformity assessments or compliance guarantees. Confirm obligations with qualified specialists.

## 1. How to use the library — Normative

For each AI system:

1. select controls using the [risk classification](AI-Risk-Classification-Framework.md), architecture and applicable obligations;
2. assign a control owner;
3. tailor tests without weakening the objective;
4. record **Pass**, **Fail**, **Not applicable** or **Exception accepted**, with durable evidence references; and
5. repeat tests after material change to model, data, purpose, permission or supplier.

A control passes only when current, attributable evidence demonstrates operation. A policy alone is insufficient.

## 2. Core controls — Normative

| ID | Control requirement | Test procedure | Typical evidence |
|---|---|---|---|
| GOV-01 | The system shall have an accountable business owner and operational owner. | Inspect the system record; confirm each owner accepts decision rights and escalation duties. | Approved system card, role acknowledgement |
| GOV-02 | Permitted and excluded purposes shall be explicit. | Compare user journeys, interfaces and instructions with the approved purpose; sample for unapproved use. | Purpose statement, usage policy, access scope |
| GOV-03 | The system shall be classified before operational use. | Reperform the classification from source evidence and compare the outcome and rationale. | Completed classification worksheet |
| GOV-04 | Decisions and exceptions shall be traceable. | Sample authorisation and exception records for evidence, decision-maker, rationale and conditions. | Decision log, exception register |
| DAT-01 | Data sources shall have recorded provenance, authority and intended use. | Trace a sample of input and retrieval data to source, steward and approved use. | Data inventory, lineage, source approval |
| DAT-02 | Data quality shall be assessed against the use case. | Reperform relevant completeness, accuracy, currency and representativeness checks. | Quality rules, test results, issue record |
| DAT-03 | Personal and confidential data shall be minimised and protected. | Inspect fields, prompts, logs and outputs; verify access, masking, retention and deletion controls. | Data-flow view, access test, retention rule |
| MOD-01 | Model and service dependencies shall be identifiable. | Trace the deployed version to provider, configuration, licence terms and known limitations. | Model or service card, bill of materials |
| MOD-02 | Evaluation shall cover defined acceptance criteria and credible failure modes. | Re-run a controlled sample, including boundary and misuse cases; compare with acceptance rules. | Evaluation set, results, reviewer record |
| MOD-03 | Generated content shall communicate uncertainty and provenance where relevant. | Sample outputs and user interfaces for citations, confidence cues and limitations appropriate to the use. | Interface captures, output samples |
| HUM-01 | Consequential outcomes shall have effective human oversight. | Observe a representative workflow; verify the reviewer has context, competence, time and authority to intervene. | Procedure, training record, sampled decisions |
| HUM-02 | Affected people shall have an accessible enquiry or challenge route where appropriate. | Follow the published route and verify receipt, triage, correction and escalation handling. | User notice, case record, service procedure |
| SEC-01 | Access to models, data and tools shall follow least privilege. | Review role assignments and attempt prohibited actions using a controlled test account. | Access matrix, test result, access review |
| SEC-02 | Prompt injection, data disclosure and unsafe tool use shall be assessed. | Execute approved adversarial scenarios across direct and indirect input channels. | Threat model, security test report |
| SEC-03 | Autonomous actions shall be bounded and interruptible. | Verify allow-listed tools, parameter validation, transaction limits, step limits and stop controls. | Tool policy, execution trace, stop test |
| OPS-01 | Operational signals shall cover quality, safety, security, use and cost. | Trace each material risk to an indicator, threshold, owner and response action. | Monitoring specification, alert test |
| OPS-02 | Incidents and near misses shall be contained, investigated and learned from. | Sample an exercise or event from detection through correction and evidence retention. | Runbook, exercise or incident record |
| OPS-03 | Material change shall trigger impact assessment and proportionate re-evaluation. | Sample changes to model, data, purpose, permissions and supplier; verify governance treatment. | Change record, evaluation comparison |
| SUP-01 | Supplier responsibilities and change notification shall be documented. | Inspect contractual and operating records for data use, security, service change, incident and exit provisions. | Due-diligence record, contract schedule |
| RET-01 | Retirement shall remove access and address retained data and dependencies. | Sample a retired service; verify credentials, endpoints, data, monitoring and inventory treatment. | Retirement record, revocation evidence |

## 3. Control selection by risk — Normative

All systems use GOV-01, GOV-02, GOV-03, DAT-01, MOD-01, SEC-01, OPS-03 and RET-01. Other controls are selected from actual risk, not tier alone.

| Classification | Expected control depth |
|---|---|
| Standard | Core controls, fit-for-purpose evaluation, owner review and operational feedback route |
| Controlled | Full applicable set, documented independent challenge and tested monitoring alerts |
| Critical | Full applicable set, independent evaluation, scenario-based resilience testing and explicit residual-risk acceptance |
| Restricted | Use shall not proceed unless the restricted condition is removed or a competent authority confirms a lawful and ethically defensible route |

Local law, sector rules, contracts or organisational policy may require stronger treatment.

## 4. Framework orientation — Informative

The table indicates broad subject relationships. It deliberately avoids claiming one-to-one equivalence.

| Control family | NIST AI RMF | ISO/IEC 42001 subject | EU AI Act subject | DPDPA subject |
|---|---|---|---|---|
| Governance and accountability | GOVERN | Leadership, policy, roles, documented information | Provider/deployer responsibilities, quality management | Accountability and grievance arrangements |
| Purpose, impact and classification | MAP, GOVERN | Context, risk and impact assessment | Risk classification and risk management | Lawful purpose, notice and data-principal interests |
| Data controls | MAP, MEASURE | Data for AI systems, operational controls | Data and data governance | Personal-data processing, accuracy and retention |
| Model evaluation and transparency | MEASURE | Performance evaluation and AI system impact | Technical documentation, transparency, accuracy | Notice, access and correction considerations |
| Human oversight and challenge | MANAGE | Operational planning and control | Human oversight | Rights and grievance considerations |
| Security, resilience and incidents | MANAGE, GOVERN | Information security, corrective action | Robustness, cybersecurity and serious-incident duties | Reasonable security safeguards and breach response |
| Suppliers and retirement | GOVERN, MANAGE | Externally provided processes, lifecycle controls | Value-chain responsibilities | Processor and retention considerations |

Use the authoritative source text and current professional advice when deciding what applies.

## 5. Test record — Normative

Each test record should contain:

| Field | Required content |
|---|---|
| System and version | Unambiguous system, model, configuration and environment |
| Control | Control ID, tailored wording and rationale |
| Tester | Competent person independent of the evidence where risk warrants it |
| Procedure | Steps, sample, test data and expected result |
| Result | Pass, Fail, Not applicable or Exception accepted |
| Evidence | Durable references with access classification |
| Finding | Gap, consequence and affected requirement |
| Decision | Corrective action or accepted exception with accountable decision-maker |
| Re-test trigger | Relevant change or event, rather than a calendar promise |

## 6. Assurance checklist — Normative

- [ ] Applicability decisions reflect the actual use and architecture.
- [ ] Evidence demonstrates operation, not merely documented intent.
- [ ] Samples include unsuccessful and boundary cases.
- [ ] Test data is controlled and does not expose unnecessary personal information.
- [ ] Findings distinguish root cause from observed symptom.
- [ ] Exceptions state scope, compensating controls and withdrawal conditions.
- [ ] No control mapping is represented as certification or legal approval.
- [ ] Re-evaluation triggers are connected to change and operational signals.

## Related links

- [WG1 reference set](README.md)
- [AI Governance Playbook](AI-Governance-Playbook.md)
- [AI Risk Classification Framework](AI-Risk-Classification-Framework.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
