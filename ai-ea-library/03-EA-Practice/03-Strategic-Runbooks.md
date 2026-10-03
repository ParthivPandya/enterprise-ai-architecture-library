# Strategic Runbooks for Architects

> Playbooks for evaluating, onboarding, operating, and retiring AI services

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [02-AI-Design-Decisions.md](02-AI-Design-Decisions.md) | [../01-AI-Governance/02-Governance-Framework.md](../01-AI-Governance/02-Governance-Framework.md)

---

## Why Architects Need Runbooks

80% of enterprise AI initiatives never reach production (VADIX, 2026). They die between the pilot demo and the operations runbook — caught in compliance reviews, security objections, cost overruns, or organisational fatigue. The operating model, not the model quality, is the differentiator between AI programmes that scale and those that stall.

This document provides the actual runbooks: practical, gate-by-gate playbooks that enterprise architects can use immediately. Four runbooks cover the complete AI service lifecycle:

1. **Runbook 1: AI Use Case Evaluation** — should we build this at all?
2. **Runbook 2: AI Vendor / Service Onboarding** — is this vendor safe to use?
3. **Runbook 3: AI System Production Launch** — is this system ready for production?
4. **Runbook 4: AI System Retirement** — how do we safely decommission an AI system?

Each runbook uses a **traffic-light gate format**: Green (proceed), Amber (proceed with conditions), Red (stop). Every gate must be resolved before moving to the next stage.

---

## Runbook 1: AI Use Case Evaluation

**Purpose:** Determine whether an AI use case is worth building before significant resources are invested.

**Trigger:** Any team proposes a new AI use case, GenAI feature, or AI agent deployment.

**Owner:** Enterprise Architect (with input from Business Sponsor, Data team, Security, Legal)

**Time to complete:** 1–2 weeks

---

### Stage 1A: Business Case Gate

| Check | Criteria | Status |
|---|---|---|
| Problem clarity | Can the problem be stated in one sentence without jargon? | 🟢/🟡/🔴 |
| Baseline established | Is there a quantified "current state" baseline to measure against? | 🟢/🟡/🔴 |
| KPI defined | Is there a single measurable primary KPI? | 🟢/🟡/🔴 |
| Business owner committed | Is there a named business owner who will be measured against the KPI? | 🟢/🟡/🔴 |
| Financial model drafted | Cost estimate + value estimate with reasonable assumptions? | 🟢/🟡/🔴 |

**Gate rule:** Any RED = stop and remediate. More than two AMBER = stop and remediate.

---

### Stage 1B: Feasibility Gate

| Check | Criteria | Status |
|---|---|---|
| Data availability | Does the required data exist, is it accessible, and is it good quality? | 🟢/🟡/🔴 |
| Technical fit | Is AI the right approach, or would a simpler solution (rules engine, search) achieve the same outcome? | 🟢/🟡/🔴 |
| Integration feasibility | Can the AI system connect to the required systems via available APIs? | 🟢/🟡/🔴 |
| Skills availability | Does the team have (or can acquire) the skills to build and maintain this? | 🟢/🟡/🔴 |
| Precedent | Has a similar use case been built internally or externally with demonstrated success? | 🟢/🟡/🔴 |

**Gate rule:** Any RED in Data Availability = stop (data is the most common killer of AI use cases). Other REDs = escalate for decision.

---

### Stage 1C: Risk Triage Gate

| Check | Criteria | Status |
|---|---|---|
| Risk tier classification | Classified against EU AI Act tiers? (Prohibited/High/Limited/Minimal) | 🟢/🟡/🔴 |
| NIST AI 600-1 applicable? | Does this involve an LLM? If yes, apply the Generative AI Profile checklist | 🟢/🟡/🔴 |
| Data protection impact | Does it process personal data? If yes, DPIA required | 🟢/🟡/🔴 |
| DPDPA applicability | Does it process Indian residents' personal data? If yes, DPDPA compliance required | 🟢/🟡/🔴 |
| Third-party model risk | If using a foundation model from a vendor, is the vendor on the approved list? | 🟢/🟡/🔴 |
| Bias/fairness implications | Does this system affect hiring, credit, admissions, or other decisions affecting individuals? | 🟢/🟡/🔴 |

**Gate rule:** Prohibited = immediate stop. High Risk = extended review track. Personal data without DPIA readiness = stop until DPIA is scoped.

---

### Stage 1D: Build/Buy/Fine-Tune Decision

This is the architectural decision that determines everything downstream. Apply this decision tree:

```
Does a commercial AI service (API/SaaS) solve ≥80% of the 
requirement without requiring your data for model training?
        │
       YES ──────────────────────→ Buy (API/SaaS)
        │
        NO
        │
Does the required capability exist in an open-source model 
that can be fine-tuned on your domain data?
        │
       YES ──────────────────────→ Fine-Tune (OSS + your data)
        │
        NO
        │
Is this a proprietary, strategic capability where 
building from scratch provides sustained competitive advantage?
        │
       YES ──────────────────────→ Build (custom ML)
        │
        NO ──────────────────────→ Revisit the use case definition
```

**Cost note:** Build is 10–50x more expensive and slower than Buy. Fine-tune is 3–10x more expensive than Buy. Default to Buy unless there is a compelling reason not to.

---

### Runbook 1 Output

Complete the **AI Use Case Decision Record**:

```
Use Case:
Date:
Decision: [PROCEED TO BUILD / PROCEED TO VENDOR EVALUATION / HOLD / REJECT]
Risk Tier: [Prohibited / High / Limited / Minimal]
Build/Buy/Fine-Tune Decision: [Buy / Fine-Tune / Build]
Primary KPI: [metric] — current: [X] → target: [Y]
Data sources identified: [list]
Estimated build cost: [₹/$ range]
Estimated annual run cost: [₹/$ range]
Estimated annual value: [₹/$ range]
DPIA required: [Yes/No]
Approved by: [EA Lead], [Business Owner], [CISO or delegate]
```

---

## Runbook 2: AI Vendor / Service Onboarding

**Purpose:** Evaluate a specific AI vendor or model provider before approving enterprise use.

**Trigger:** A team requests to use a new AI vendor, API, or model service not currently on the approved list.

**Owner:** Enterprise Architect (with Security, Legal, Privacy, Finance)

**Time to complete:** 2–6 weeks (depending on risk tier)

---

### Dimension 1: Security and Compliance Assessment

| Check | Evidence Required | Status |
|---|---|---|
| SOC 2 Type II | Current (within 12 months) report or letter of compliance | 🟢/🟡/🔴 |
| ISO 27001 | Certificate or equivalent | 🟢/🟡/🔴 |
| Penetration testing | Third-party pen test results within 12 months | 🟢/🟡/🔴 |
| Data encryption | AES-256 at rest; TLS 1.2+ in transit confirmed | 🟢/🟡/🔴 |
| Data Processing Agreement (DPA) | Executed before any personal data is shared | 🟢/🟡/🔴 |
| Data residency | India/EU/local data residency available and configurable? | 🟢/🟡/🔴 |
| Breach notification | Contractual commitment to notify within 72 hours (DPDPA) | 🟢/🟡/🔴 |
| Access control | Role-based access; audit logging for all data access | 🟢/🟡/🔴 |

**Red flags (automatic Red):** No DPA willing to execute. Customer data used to train models by default without opt-out. No audit logs available. Unclear data retention or deletion rights.

---

### Dimension 2: AI-Specific Technical Assessment

| Check | Questions to Ask | Status |
|---|---|---|
| Model transparency | Which model(s) are used? Foundation model disclosed? Version pinning possible? | 🟢/🟡/🔴 |
| Hallucination / accuracy | What benchmarks does the vendor publish? What are failure modes? | 🟢/🟡/🔴 |
| Prompt injection mitigation | What controls exist against prompt injection and jailbreaking? | 🟢/🟡/🔴 |
| Human oversight | Does the product support human-in-the-loop for high-stakes actions? | 🟢/🟡/🔴 |
| Model update notification | How are customers notified when the underlying model changes? | 🟢/🟡/🔴 |
| Output explainability | Can the system provide rationale for its outputs? (Required for high-risk AI) | 🟢/🟡/🔴 |
| Rate limits / reliability | What are the SLAs for uptime and latency? What's the fallback? | 🟢/🟡/🔴 |

---

### Dimension 3: Commercial and Legal Assessment

| Check | Criteria | Status |
|---|---|---|
| IP ownership | Outputs generated using your data — who owns them? | 🟢/🟡/🔴 |
| Indemnification | Does the vendor indemnify against IP infringement in model outputs? | 🟢/🟡/🔴 |
| Liability cap | Is the liability cap commensurate with the risk of the use case? | 🟢/🟡/🔴 |
| Termination and data export | Can you export your data and terminate without penalty? | 🟢/🟡/🔴 |
| Vendor viability | Funding runway, customer retention, and acquisition risk assessed? | 🟢/🟡/🔴 |
| Price stability | Is pricing locked or variable? Token price changes can dramatically affect ROI | 🟢/🟡/🔴 |
| Audit rights | Do you have contractual right to audit the vendor's data handling? | 🟢/🟡/🔴 |

---

### Dimension 4: Integration and Operability Assessment

| Check | Criteria | Status |
|---|---|---|
| API quality | REST/GraphQL API with versioning, comprehensive documentation? | 🟢/🟡/🔴 |
| Webhook / event support | Can the vendor push events to your systems? | 🟢/🟡/🔴 |
| Identity integration | SSO/SAML/OAuth2 compatible with your identity provider? | 🟢/🟡/🔴 |
| Monitoring / observability | Does the vendor expose usage metrics and logs in standard formats? | 🟢/🟡/🔴 |
| Sandbox environment | Is a non-production environment available for testing? | 🟢/🟡/🔴 |

---

### Runbook 2 Output

Complete the **AI Vendor Assessment Record**:

```
Vendor / Service:
Date Assessed:
Decision: [APPROVED / APPROVED WITH CONDITIONS / CONDITIONAL APPROVAL (re-assess in 6mo) / REJECTED]
Risk Category: [Low / Medium / High / Critical]

Conditions (if any):
1.
2.
3.

Data handling: [No personal data / Personal data with DPA executed / Personal data - DPA pending]
Data residency: [India / EU / US / Multi-region]
DPA executed: [Yes / No / Pending]
Approved use cases: [list]
Prohibited use cases: [list]
Annual review date:
Approved by: [EA Lead], [CISO], [Legal / Privacy Lead]
```

---

## Runbook 3: AI System Production Launch

**Purpose:** Ensure an AI system is ready for production deployment.

**Trigger:** An AI system completes internal testing and proposes to go live.

**Owner:** Enterprise Architect (with Engineering Lead, Security, Business Owner)

**Time to complete:** 1–2 weeks (on top of build/test cycle)

---

### Gate 3A: Technical Readiness

| Check | Criteria | Status |
|---|---|---|
| Performance benchmarks | System meets latency (p50/p95/p99) and throughput targets under load | 🟢/🟡/🔴 |
| Error handling | Graceful failure tested: what happens if the AI API is unavailable? | 🟢/🟡/🔴 |
| Fallback mechanism | Secondary model or non-AI fallback confirmed working | 🟢/🟡/🔴 |
| Cost budget confirmed | Per-inference cost × expected volume ≤ approved budget | 🟢/🟡/🔴 |
| Monitoring live | Accuracy, latency, cost, and error rate dashboards active pre-launch | 🟢/🟡/🔴 |
| Anomaly alerts configured | Alerts set for cost spikes, latency degradation, error rate increase | 🟢/🟡/🔴 |

---

### Gate 3B: Security and Compliance Readiness

| Check | Criteria | Status |
|---|---|---|
| Red team test completed | Adversarial testing against OWASP LLM Top 10 completed and findings resolved | 🟢/🟡/🔴 |
| Prompt injection defences verified | Input validation layer tested; indirect injection scenarios covered | 🟢/🟡/🔴 |
| Output scanning active | PII detection and harmful content scanning in production pipeline | 🟢/🟡/🔴 |
| Audit logging enabled | All AI interactions logged with user ID, timestamp, input/output summary | 🟢/🟡/🔴 |
| Access controls verified | Only authorised users can access the system; over-provisioned access removed | 🟢/🟡/🔴 |
| DPIA completed | For personal data processing: DPIA finalised and submitted (SDFs: to DPB) | 🟢/🟡/🔴 |
| Incident response plan | Defined contacts, escalation steps, and rollback procedure documented | 🟢/🟡/🔴 |

---

### Gate 3C: Governance and Accountability Readiness

| Check | Criteria | Status |
|---|---|---|
| AI System Card completed | Use case, limitations, performance benchmarks, fairness evaluation, oversight | 🟢/🟡/🔴 |
| AI registry entry created | System catalogued in the enterprise AI system registry | 🟢/🟡/🔴 |
| System owner designated | Named individual accountable for system performance and compliance | 🟢/🟡/🔴 |
| Transparency disclosure | Users informed they are interacting with AI (where applicable) | 🟢/🟡/🔴 |
| Human oversight confirmed | High-consequence actions require human approval; tested in staging | 🟢/🟡/🔴 |
| Rollback plan documented | Specific steps, time estimate, and owner for rolling back the system | 🟢/🟡/🔴 |

---

### Gate 3D: Canary Deployment Plan

Never launch to 100% of users simultaneously. Define:

| Parameter | Specification |
|---|---|
| Canary cohort | First 5% of users (randomly selected) |
| Canary duration | 72 hours minimum |
| Promotion criteria | No critical incidents; KPI trending toward target; error rate < [X]% |
| Rollback trigger | Any critical incident; error rate > [Y]%; cost anomaly > [Z]% of budget |
| Full rollout stages | 5% → 25% → 50% → 100% (each with 24-hour hold) |

---

### Gate 3E: 30-Day Post-Launch Review

Schedule and confirm:

- [ ] 30-day post-launch review meeting on calendar (day of launch)
- [ ] Review agenda: adoption rate, quality vs. baseline, cost vs. budget, open incidents, user feedback
- [ ] Decision at 30-day review: continue / optimise / rollback

---

## Runbook 4: AI System Retirement

**Purpose:** Safely decommission an AI system without data loss, compliance breach, or operational disruption.

**Trigger:** System has been replaced, use case is no longer relevant, vendor end-of-life, or persistent performance failure.

**Owner:** Enterprise Architect (with System Owner, Data team, Legal/Privacy, Finance)

**Time to complete:** 4–12 weeks (depending on system complexity)

---

### Stage 4A: Retirement Decision Record

Document why the system is being retired:
- Business reason (use case no longer needed / consolidated into another system)
- Technical reason (replaced by superior system / vendor EOL / architecture deprecation)
- Compliance reason (system cannot meet new regulatory requirements)
- Performance reason (persistent failure to meet KPI; decision taken by business owner)

---

### Stage 4B: Dependency Assessment

Before shutting anything down:

- [ ] Map all systems and processes that depend on this AI system (check the architecture repository)
- [ ] Identify all data flows TO and FROM this system
- [ ] Confirm replacement or alternative path for each dependency
- [ ] Communicate retirement timeline to all dependency owners

---

### Stage 4C: Data Handling

| Action | Who | When |
|---|---|---|
| Identify all personal data processed by the system | Data team | Week 1 |
| Determine retention/deletion obligations (DPDPA, contracts) | Legal/Privacy | Week 1 |
| Export data that must be retained in another system | Engineering | Weeks 2–4 |
| Delete data that must not be retained | Engineering + DBA | After export confirmed |
| Confirm deletion with audit evidence | Data team | Before final shutdown |
| Document machine unlearning status (if applicable) | Engineering | Before final shutdown |

**DPDPA requirement:** Data that no longer has a lawful basis must be erased. The DPDPA's Right to Erasure obligation extends to AI systems — any model trained on personal data must have a documented position on how erasure requests are handled. If full machine unlearning is not yet feasible, document the interim approach and timeline.

---

### Stage 4D: Model and System Decommission

- [ ] Notify vendor of service termination (per contract terms — typically 30–90 days)
- [ ] Revoke all API keys and service credentials
- [ ] Archive model weights (if self-hosted) with access restricted to compliance team
- [ ] Remove system from the enterprise AI registry (mark as RETIRED, not delete — retain record)
- [ ] Archive the AI System Card with retirement date and reason

---

### Stage 4E: Post-Retirement Review

Within 30 days of shutdown, conduct a brief retrospective:
- Did the system deliver on its original business case?
- What would you do differently in the next AI system of this type?
- Are there lessons for the AI Architecture Standards document?
- Were there compliance findings that need to be addressed in other AI systems?

---

## Quick Reference: Runbook Decision Matrix

| Situation | Use Runbook | Owner | Time Required |
|---|---|---|---|
| New AI idea/proposal | Runbook 1: Use Case Evaluation | EA Lead + Business Sponsor | 1–2 weeks |
| New vendor/service requested | Runbook 2: Vendor Onboarding | EA Lead + CISO + Legal | 2–6 weeks |
| System ready for production | Runbook 3: Production Launch | EA Lead + Eng Lead | 1–2 weeks |
| System being shut down | Runbook 4: Retirement | EA Lead + System Owner | 4–12 weeks |

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): Stanford Digital Economy Lab Enterprise AI Playbook 2026, VADIX Enterprise AI Playbook from Pilot to Production, StackAI CIO Playbook Enterprise AI Strategy 2026, Worqlo Enterprise AI Onboarding Checklist 2026, InitializeAI Vendor Evaluation Checklist, Pertama Partners AI Vendor Approval Checklist 2026, AI Agent Square Enterprise AI Agent Evaluation Framework 2026, Vidizmo Enterprise AI Vendor Evaluation Checklist, AppIT 50-Point Technical Assessment Checklist 2026, Gartner Enterprise AI Governance Research.*