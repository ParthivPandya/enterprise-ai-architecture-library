# AIEA Alignment and Evidence Workbook
## AI Regulatory and Management-System Evidence Checklists
### Document Number: AIEA-CW01 | Version 1.0 | 2026

---

> **Document type:** Checklist and Evidence Workbook  
> **Primary audience:** Governance, Risk, Privacy, Internal Audit, and AI System Owners  
> **Use when:** Identifying and recording evidence potentially relevant to an AI system  
> **Last verified:** October 2026  
> **Authority:** Independent practitioner aid; not legal advice, certification, or proof of compliance  

## Preface

This Alignment and Evidence Workbook is a companion to the AIEA Reference Framework. Where [AIEA-401](AIEA-401-Capability-Governance.md) defines governance capabilities and [AIEA-101 Chapter 6](AIEA-101-Introduction-Core-Concepts.md) maps AIEA concepts to external frameworks, this workbook helps a team identify, collect, and review evidence for an individual AI system.

It covers four frameworks:

1. **NIST AI RMF 1.0** — Govern, Map, Measure, Manage
2. **EU AI Act 2024** — selected obligations by role, risk classification, and commencement date
3. **ISO/IEC 42001:2023** — AI Management System clauses
4. **India DPDP Act 2023 and Rules 2025** — selected personal-data obligations with phased commencement

> This workbook is an architecture and governance aid, **not legal advice**. A checked item shows only that identified evidence was reviewed; it does not establish legal compliance or certification. Confirm applicability, role, effective date, jurisdiction, and interpretation with qualified counsel or an accredited auditor. Use alongside the reusable templates in [12-Templates](../12-Templates/README.md), especially the [Pre-Deployment Launch Gate](../12-Templates/Pre-Deployment-Launch-Gate.md) and [DPDP Alignment Checklist](../12-Templates/DPDPA-Compliance-Checklist.md).

### How to Use
Copy this workbook per AI system (or per release). First record why each framework or provision applies, then complete applicable checks and attach evidence. An item is launch-blocking only when an identified law, contract, organisational policy, or approved risk decision makes it mandatory.

| Field | Value |
|---|---|
| **System** | `<AI-SYS-0000>` |
| **Risk classification** | `<Minimal / Limited / High>` |
| **Completed by** | `<name>` |
| **Date** | `<YYYY-MM-DD>` |
| **Jurisdiction(s)** | `<country / state / sector>` |
| **Organisation role** | `<provider / deployer / data fiduciary / processor / other>` |
| **Applicability basis** | `<law / contract / policy / voluntary alignment>` |
| **Primary source verified** | `<URL and date>` |

---

## Chapter 1: NIST AI RMF 1.0 Checklist

### 1.1 GOVERN

| # | Control | Evidence | Status |
|---|---|---|---|
| GV-1 | A named human is accountable for the system (AIEA Principle G1) | `<link>` | `[ ]` |
| GV-2 | AI policies and principles are documented and applied | `<link>` | `[ ]` |
| GV-3 | Roles and responsibilities (owner, governance lead, operators) defined | `<link>` | `[ ]` |
| GV-4 | Risk tolerance and escalation thresholds set | `<link>` | `[ ]` |
| GV-5 | Governance evidence retained in the repository | `<link>` | `[ ]` |

### 1.2 MAP

| # | Control | Evidence | Status |
|---|---|---|---|
| MP-1 | System registered in the AI System Registry | `<link>` | `[ ]` |
| MP-2 | Context, purpose, and affected stakeholders documented | `<link>` | `[ ]` |
| MP-3 | Risk classification completed and approved | `<link>` | `[ ]` |
| MP-4 | Data sources and lineage mapped (data contracts) | `<link>` | `[ ]` |
| MP-5 | Known limitations and failure modes documented | `<link>` | `[ ]` |

### 1.3 MEASURE

| # | Control | Evidence | Status |
|---|---|---|---|
| MS-1 | Pre-deployment evaluation completed (launch gate) | `<link>` | `[ ]` |
| MS-2 | Red-team exercise completed; no open Critical/High findings | `<link>` | `[ ]` |
| MS-3 | Production monitoring live before first user interaction | `<link>` | `[ ]` |
| MS-4 | Fairness / bias assessed where individuals are affected | `<link>` | `[ ]` |
| MS-5 | Explainability method appropriate to risk tier in place | `<link>` | `[ ]` |

### 1.4 MANAGE

| # | Control | Evidence | Status |
|---|---|---|---|
| MG-1 | Risk treatment decisions recorded (accept/mitigate/block) | `<link>` | `[ ]` |
| MG-2 | Incident response process defined and tested | `<link>` | `[ ]` |
| MG-3 | Change triggers for governance re-review defined | `<link>` | `[ ]` |
| MG-4 | Review cadence and retirement triggers set | `<link>` | `[ ]` |

---

## Chapter 2: EU AI Act 2024 Evidence Checklist

> Do not infer territorial scope merely because an output may affect a person in the EU. Determine the organisation's statutory role, where the system/output is placed or used, classification, exclusions, and the commencement date of each provision. Record the analysis below from the current consolidated text and official implementation guidance.

| Applicability Field | Recorded Basis |
|---|---|
| Organisation role | `<provider / deployer / importer / distributor / product manufacturer / other>` |
| Territorial-scope basis | `<Article / facts / legal assessment>` |
| System or model classification | `<prohibited / high-risk / transparency / GPAI / other>` |
| Applicable provision(s) | `<Article / Annex>` |
| Effective date(s) | `<date verified against current official source>` |
| Legal reviewer | `<role and review date>` |

### 2.1 Risk Classification Gate

| # | Question | Answer |
|---|---|---|
| EU-C1 | Is the system a prohibited (unacceptable-risk) practice? | `[ ] Yes → STOP  [ ] No` |
| EU-C2 | Does it fall under a High-Risk category (Annex III use or safety component)? | `[ ] Yes  [ ] No` |
| EU-C3 | Is it a limited-risk system with transparency duties (e.g., chatbot, generated content)? | `[ ] Yes  [ ] No` |
| EU-C4 | Is it a General-Purpose AI (GPAI) model with systemic-risk considerations? | `[ ] Yes  [ ] No` |

### 2.2 High-Risk Obligations (if EU-C2 = Yes)

| # | Obligation | Evidence | Status |
|---|---|---|---|
| EU-H1 | Risk management system established and maintained | `<link>` | `[ ]` |
| EU-H2 | Data governance: training/validation data quality and relevance | `<link>` | `[ ]` |
| EU-H3 | Technical documentation prepared (System Card) | `<link>` | `[ ]` |
| EU-H4 | Automatic logging / record-keeping enabled | `<link>` | `[ ]` |
| EU-H5 | Transparency and instructions for use provided to deployers | `<link>` | `[ ]` |
| EU-H6 | Human oversight designed in (Principle D4 gates) | `<link>` | `[ ]` |
| EU-H7 | Accuracy, robustness, and cybersecurity validated | `<link>` | `[ ]` |
| EU-H8 | Conformity assessment completed (pre-deployment review) | `<link>` | `[ ]` |
| EU-H9 | Post-market monitoring plan in place | `<link>` | `[ ]` |

### 2.3 Transparency Obligations (if EU-C3 = Yes)

| # | Obligation | Evidence | Status |
|---|---|---|---|
| EU-T1 | Users informed they are interacting with an AI system | `<link>` | `[ ]` |
| EU-T2 | AI-generated or manipulated content is labelled | `<link>` | `[ ]` |

### 2.4 GPAI Obligations (if EU-C4 = Yes)

| # | Obligation | Evidence | Status |
|---|---|---|---|
| EU-G1 | Technical documentation of the model maintained | `<link>` | `[ ]` |
| EU-G2 | Copyright / training-data summary policy addressed | `<link>` | `[ ]` |
| EU-G3 | Systemic-risk evaluation and mitigation (if applicable) | `<link>` | `[ ]` |

---

## Chapter 3: ISO/IEC 42001:2023 Checklist

> For organisations pursuing or maintaining a certifiable AI Management System (AIMS).

| Clause | Requirement | Evidence | Status |
|---|---|---|---|
| 4 | Context of the organisation and AIMS scope defined | `<link>` | `[ ]` |
| 5.1 | Leadership and commitment demonstrated (CAIO sponsorship) | `<link>` | `[ ]` |
| 5.2 | AI policy established and communicated | `<link>` | `[ ]` |
| 6.1 | AI risks and opportunities assessed | `<link>` | `[ ]` |
| 6.2 | AI objectives set and planned | `<link>` | `[ ]` |
| 7.2 | Competence of personnel ensured | `<link>` | `[ ]` |
| 7.5 | Documented information controlled (repository governance) | `<link>` | `[ ]` |
| 8.1 | Operational planning and control implemented | `<link>` | `[ ]` |
| 8.3 | AI system impact assessment conducted | `<link>` | `[ ]` |
| 9.1 | Monitoring, measurement, analysis, evaluation performed | `<link>` | `[ ]` |
| 9.2 | Internal audit conducted on the AIMS | `<link>` | `[ ]` |
| 9.3 | Management review completed | `<link>` | `[ ]` |
| 10.1 | Continual improvement actioned (change management) | `<link>` | `[ ]` |
| 10.2 | Nonconformity and corrective action handled | `<link>` | `[ ]` |

---

## Chapter 4: India DPDP Act 2023 and Rules 2025 Evidence Checklist

> Assess applicability against the Act, Rules, commencement notifications, organisation role, processing context, and sector-specific law. Substantive provisions have phased commencement. See the standalone [DPDP Alignment Checklist template](../12-Templates/DPDPA-Compliance-Checklist.md) for the per-system version.

| Applicability Field | Recorded Basis |
|---|---|
| Data Fiduciary / processor role | `<role and entity>` |
| Territorial-scope basis | `<processing facts and provision>` |
| Significant Data Fiduciary status | `<designated / not designated / verify>` |
| Commenced provision(s) relied upon | `<section / rule / notification / effective date>` |
| Sector-specific requirement | `<RBI / SEBI / IRDAI / health / other / none>` |
| Cross-border restriction or policy | `<notification, sector rule, contract, or organisational policy>` |

### 4.1 Lawful Processing and Notice

| # | Obligation | Evidence | Status |
|---|---|---|---|
| DP-1 | Lawful basis identified for each data category | `<link>` | `[ ]` |
| DP-2 | Clear notice provided; consent free, specific, informed | `<link>` | `[ ]` |
| DP-3 | Purpose limitation and data minimisation enforced | `<link>` | `[ ]` |
| DP-4 | Consent withdrawal mechanism as easy as giving consent | `<link>` | `[ ]` |

### 4.2 Data Principal Rights

| # | Obligation | Evidence | Status |
|---|---|---|---|
| DP-5 | Access and correction supported | `<link>` | `[ ]` |
| DP-6 | Erasure on purpose completion / consent withdrawal supported | `<link>` | `[ ]` |
| DP-7 | Grievance redressal mechanism available | `<link>` | `[ ]` |

### 4.3 Security, Breach, and Residency

| # | Obligation | Evidence | Status |
|---|---|---|---|
| DP-8 | Reasonable security safeguards implemented | `<link>` | `[ ]` |
| DP-9 | Breach detection and notification process defined | `<link>` | `[ ]` |
| DP-10 | Retention limited; data residency captured in data contracts | `<link>` | `[ ]` |

### 4.4 Significant Data Fiduciary (if designated)

| # | Obligation | Evidence | Status |
|---|---|---|---|
| DP-11 | India-based Data Protection Officer appointed | `<link>` | `[ ]` |
| DP-12 | Data Protection Impact Assessment completed | `<link>` | `[ ]` |
| DP-13 | Independent data audit scheduled | `<link>` | `[ ]` |

---

## Chapter 5: Consolidated Launch Decision

| Framework | Applicable? | Applicability/effective date verified? | Required evidence reviewed? |
|---|---|---|---|
| NIST AI RMF | `[ ]` | `[ ]` | `[ ]` |
| EU AI Act | `[ ]` | `[ ]` | `[ ]` |
| ISO/IEC 42001 | `[ ]` | `[ ]` | `[ ]` |
| India DPDP Act and Rules | `[ ]` | `[ ]` | `[ ]` |

**Launch decision:** `<GO / NO-GO / GO with conditions>`
**Approved by:** `<Governance Lead name>` — `<YYYY-MM-DD>`

---

*AIEA Alignment and Evidence Workbook. Document AIEA-CW01, Version 1.0, 2026. Companion to [AIEA-401](AIEA-401-Capability-Governance.md) and [AIEA-101 Chapter 6](AIEA-101-Introduction-Core-Concepts.md).*
