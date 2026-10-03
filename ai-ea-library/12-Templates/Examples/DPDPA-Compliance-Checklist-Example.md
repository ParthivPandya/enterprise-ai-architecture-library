# India DPDP Act/Rules Alignment Checklist — Completed Example

> **Illustrative architecture review only:** this fictional checklist does not provide legal advice, certify compliance or guarantee that obligations are satisfied. The Act permits phased commencement and does not impose blanket data localisation; applicable provisions, Rules, notifications, transfer restrictions and separate sectoral requirements must be verified on the assessment date. Source template: [DPDPA-Compliance-Checklist.md](../DPDPA-Compliance-Checklist.md).

| Field | Value |
|---|---|
| **System** | AI-SYS-EX-001 |
| **Completed by** | Privacy Architecture role |
| **Date** | 2026-09-15 (illustrative) |
| **Data Fiduciary** | Example retail bank (fictional) |
| **Applicable commencement and Rules verified as at** | Not verified; open action |
| **SDF designation applies?** | Not determined; formal assessment required |

`[x]` means design evidence exists for review, not that compliance is guaranteed. `[ ]` is an open action and blocks launch where material.

## 0. Applicability and Commencement

- [x] Proposed processing activities and data flows documented for applicability review.
- [ ] Territorial applicability confirmed by qualified legal and privacy functions.
- [ ] Provisions, Rules, notifications and directions in force on the assessment date identified.
- [ ] Sector-specific, contractual and other legal requirements assessed separately.
- [x] Material commencement or rule change defined as a reassessment trigger.

## 1. Lawful Processing

- [ ] Processing basis confirmed for each personal-data purpose — privacy and legal decision pending.
- [x] Draft purpose register separates guidance, security logging and service measurement.
- [x] Data minimisation design excludes identity documents and screening indicators from the model.
- [ ] Production configuration verified against the approved purpose and field allow-list.

## 2. Notice and Consent

- [x] Draft plain-language AI and data-use notice prepared for supported English journeys.
- [ ] Applicable language and accessibility review completed.
- [ ] Consent requirement and withdrawal handling confirmed; consent is not assumed to be the basis for every purpose.
- [x] Versioned notice-event schema designed; production retention test pending.

## 3. Data Principal Rights

- [x] Existing bank request channel mapped to conversation and audit records.
- [ ] Correction and erasure behaviour tested across provider logs, backups and derived records.
- [x] Grievance route included in proposed support content.
- [ ] Nomination handling assessed for this processing context.

## 4. Security and Breach

- [x] Encryption, role-based access, redaction and incident runbook included in the design.
- [ ] High and Medium red-team fixes independently retested.
- [x] Proposed conversation retention is 30 days; final schedule and deletion evidence pending.
- [ ] Breach assessment and notification workflow exercised with this system's data map.

## 5. Cross-Border and Residency

- [x] Architecture record states that the Act has no blanket localisation requirement.
- [ ] Current notified transfer restrictions confirmed by qualified functions.
- [ ] Vendor subprocessors, support access and all processing locations contractually evidenced.
- [ ] Sector-specific localisation, contractual and other applicable restrictions assessed separately.
- [x] Proposed residency and transfer constraints recorded in [DC-EX-001](Data-Contract-Example.md).

## 6. Significant Data Fiduciary

- [ ] Designation status and resulting obligations confirmed.
- [ ] Data Protection Officer requirement assessed.
- [ ] Data Protection Impact Assessment requirement and scope confirmed.
- [ ] Independent data-audit requirement assessed and, if applicable, scheduled.

## 7. Sign-off

| Role | Name | Date |
|---|---|---|
| System Owner | Customer Onboarding AI System Owner role — pending named assignee | Pending |
| Privacy / DPO | Privacy leadership role — review not complete | Pending |

**Assessment outcome:** incomplete; do not treat completed checks as proof of compliance or launch approval.
