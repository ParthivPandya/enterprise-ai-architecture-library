# Pre-Deployment Launch Gate

> Copy this file per AI system before production launch. This is the go/no-go gate. A system MUST NOT go to production with an open blocking item. Owned operationally by WG1 (AI Governance Playbook).

| Field | Value |
|---|---|
| **System** | `<AI-SYS-0000>` |
| **Version** | `<x.y>` |
| **Risk classification** | `<Minimal / Limited / High>` |
| **Target launch date** | `<YYYY-MM-DD>` |
| **Gate reviewer** | `<name>` |
| **Decision** | `<GO / NO-GO / GO with conditions>` |

## 1. Accountability
- [ ] Named System Owner recorded (Principle G1)
- [ ] System Card complete and current

## 2. Governance & Compliance
- [ ] Risk classification completed and approved (Principle G2)
- [ ] Applicable frameworks mapped (NIST AI RMF / EU AI Act / ISO 42001 / India DPDP Act and applicable Rules)
- [ ] Explainability method appropriate to risk tier defined (Principle G3)
- [ ] India DPDP Act/Rules alignment checklist reviewed (if applicable); completed checks are not proof of compliance

## 3. Safety & Security
- [ ] Red-team exercise completed; no open Critical/High findings
- [ ] Tool/permission matrix reviewed; least privilege confirmed (agentic systems)
- [ ] Irreversible actions require human approval (Principle D4)
- [ ] Grounding / RAG in place for factual systems (Principle D2)

## 4. Operations
- [ ] Monitoring live before first user interaction (Principle O1)
- [ ] Cost attribution via AI Gateway operational (Principle O2)
- [ ] Alert thresholds configured and tested
- [ ] Fallback behaviour defined and tested
- [ ] Review cadence and retirement triggers set (Principle O3)

## 5. Conditions (if GO with conditions)
| Condition | Owner | Due |
|---|---|---|
| `<condition>` | `<name>` | `<YYYY-MM-DD>` |

## 6. Sign-off
| Role | Name | Decision | Date |
|---|---|---|---|
| System Owner | `<name>` | `<GO/NO-GO>` | `<YYYY-MM-DD>` |
| Governance Lead | `<name>` | `<GO/NO-GO>` | `<YYYY-MM-DD>` |
