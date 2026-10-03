# AI Governance Playbook

| Metadata | Description |
|---|---|
| **Purpose** | Provide a practical operating model for governing AI systems from initial proposal through retirement. |
| **Audience** | Enterprise architects, system owners, risk and compliance teams, security teams, data stewards, procurement teams, internal assurance functions and business decision-makers. |
| **Use When** | Establishing governance for a new AI service, reviewing a material change, accepting a third-party AI capability or examining an operational concern. |
| **Outputs** | Accountable owner, risk classification, control plan, evidence pack, recorded decision, monitoring plan and retirement record. |
| **Content classification** | Sections labelled **Normative** define recommended requirements for adopting this playbook. Sections labelled **Informative** explain or illustrate their use. |

> **Important:** This playbook is independent practitioner guidance. It does not provide legal advice, certify compliance or replace review of obligations that apply to a particular organisation, sector or jurisdiction.

## 1. Operating principles — Normative

An adopting organisation **shall**:

1. keep an inventory of AI systems, including embedded and externally supplied AI;
2. assign one accountable business owner and one operational owner to each system;
3. classify risk before data is connected or consequential decisions are enabled;
4. select controls in proportion to intended use, affected people and credible harm;
5. retain evidence for design, evaluation, authorisation and operational decisions;
6. provide a route for people to question, override or appeal consequential outcomes;
7. monitor actual operation and reassess after material change; and
8. retire access, data, credentials and dependencies in a controlled manner.

“Shall” expresses a requirement for use of this playbook. “Should” expresses a strong recommendation, and “may” expresses an option. An organisation may tailor the mechanism, but it should record why an equivalent mechanism meets the intent.

## 2. Governance model — Normative

Governance works best when decision rights remain close to existing enterprise governance rather than forming a disconnected AI process.

| Role | Core accountability | Evidence owned |
|---|---|---|
| Business owner | Defines the permitted purpose, affected users, value hypothesis and acceptable residual risk | Use-case statement, acceptance decision |
| System owner | Maintains the system record and co-ordinates lifecycle activities | System card, dependency record, change record |
| Enterprise or solution architect | Assesses boundaries, integration, failure modes and alternatives | Architecture views, decision records |
| Data steward | Confirms data provenance, quality, access and retention rules | Data sheet, lineage, approval record |
| Security and privacy functions | Assess threats, access, disclosure and personal-data handling | Threat model, privacy assessment, test evidence |
| Independent reviewer | Challenges assumptions and verifies that tests support claims | Review findings, exceptions |
| Operational owner | Runs monitoring, incident handling and service retirement | Runbook, monitoring record, incident record |

No role should approve its own unresolved exception. For higher-risk use, the business owner, relevant control functions and an independent reviewer should participate in the decision.

## 3. Governance pillars — Normative

| Pillar | Required question | Minimum evidence |
|---|---|---|
| Accountability | Who can accept, change, pause and retire the system? | Named roles and decision rights |
| Purpose and people | Is the use legitimate, bounded and understandable to affected people? | Purpose statement, user and impact analysis |
| Data | Are sources suitable, authorised, traceable and appropriately retained? | Data inventory, lineage and quality checks |
| Model and solution | Are capabilities, limitations and dependencies understood? | Model or service record, architecture and evaluation results |
| Security and resilience | Can misuse, leakage, manipulation and service failure be contained? | Threat model, access tests, recovery procedure |
| Human oversight | Can a competent person intervene at the right point? | Oversight design, instructions and sampled records |
| Operations | Are performance, harm indicators, cost and change monitored? | Monitoring plan, alert thresholds and review record |
| Incident and retirement | Can harm be limited and system access removed? | Response runbook and retirement checklist |

## 4. Governance workflow — Normative

Use the following workflow for a new system and repeat the affected steps after material change.

| Step | Action | Exit condition |
|---|---|---|
| 1. Register | Record purpose, owner, users, provider, model, data, integrations and deployment boundary | System record has no unknown owner or boundary |
| 2. Classify | Apply the [AI Risk Classification Framework](AI-Risk-Classification-Framework.md) | Tier, rationale and escalation conditions are recorded |
| 3. Assess | Examine impacts, data, security, architecture, supplier and operational dependencies | Material risks and assumptions are visible |
| 4. Plan controls | Select applicable controls from the [Governance Control Library](Governance-Control-Library.md) | Each risk has an owner, treatment and test |
| 5. Evaluate | Test quality, safety, security, human oversight and failure behaviour against acceptance criteria | Results are reproducible and limitations are documented |
| 6. Decide | Authorise, authorise with conditions, return for revision or decline | Decision-maker, evidence considered and conditions are recorded |
| 7. Operate | Monitor use, outcomes, incidents, changes, provider notices and control effectiveness | Alerts have owners and defined response actions |
| 8. Retire | Disable access, revoke credentials, handle retained data and update dependencies | No unowned live interface or data copy remains |

### Decision record

Every decision should state:

- the system and version considered;
- permitted and excluded uses;
- classification and key risks;
- evidence reviewed and known limitations;
- conditions, exceptions and their owners;
- operational indicators and intervention points; and
- the events that require reassessment.

## 5. Review gate checklist — Normative

The decision-maker should not authorise operational use until all applicable statements can be answered **Yes** or an exception has been explicitly accepted.

- [ ] The intended purpose, users and affected people are defined.
- [ ] The accountable business and operational owners accept their responsibilities.
- [ ] Risk classification has been independently challenged where required.
- [ ] Data sources, rights, provenance, quality and retention are documented.
- [ ] Architecture boundaries, suppliers and material dependencies are recorded.
- [ ] Evaluation covers normal use, foreseeable misuse and important failure modes.
- [ ] Security, privacy and human-oversight controls have been tested.
- [ ] User information does not overstate capability or certainty.
- [ ] Monitoring signals, intervention authority and response procedures are usable.
- [ ] Residual risks, limitations and exceptions are visible to the decision-maker.

The reusable [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md) can hold the detailed evidence.

## 6. Change, incident and retirement — Normative

A **material change** includes a new purpose, user population, decision consequence, model, data source, tool permission, supplier, interface or control boundary. The system owner shall assess which governance steps must be repeated before the change is used operationally.

When an incident or credible near miss occurs:

1. contain the system, affected integration or unsafe action;
2. preserve logs and decision evidence while respecting access and retention rules;
3. assess affected people, operations and data;
4. notify the authorised internal functions and external parties where applicable;
5. correct the immediate cause and examine contributing control weaknesses;
6. validate the correction before restoring affected use; and
7. record learning in controls, tests and operating instructions.

Retirement shall address user access, service accounts, secrets, model endpoints, stored prompts and outputs, derived data, contracts, monitoring, downstream consumers and the inventory record.

## 7. Tailoring guidance — Informative

Small organisations can combine roles, but should preserve separation between building, accepting risk and independent challenge. Low-impact internal assistance may use a concise evidence pack. Consequential decisions, sensitive data, autonomous actions or broad public exposure warrant deeper assessment and more independent review.

The playbook is intentionally technology-neutral. A spreadsheet and document repository can support it when ownership, versioning, access and evidence integrity are controlled.

## Related links

- [WG1 reference set](README.md)
- [Governance Control Library](Governance-Control-Library.md)
- [AI Risk Classification Framework](AI-Risk-Classification-Framework.md)
- [Governance Framework](../../01-AI-Governance/02-Governance-Framework.md)
- [Capability and Governance reference](../../05-Standards/AIEA-401-Capability-Governance.md)

