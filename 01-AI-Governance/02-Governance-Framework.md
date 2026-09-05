# AI Governance Framework: Compliance, Quality, and Accountability

> **Related:** [01-FinOps.md](01-FinOps.md) | [03-Responsible-AI.md](03-Responsible-AI.md) | [04-Risk-Mitigation.md](04-Risk-Mitigation.md)

---

## The Governance Imperative

The AI Incident Database recorded 233 AI-related incidents in 2024 — a 56.4% year-over-year increase and a record high, spanning unauthorised training-data access, synthetic-identity fraud, and model-inversion attacks (Stanford HAI AI Index 2025). The global AI governance market, valued at $308.3 million in 2025, is projected to reach $3.59 billion by 2033 at a 36% CAGR.

Governance has moved from optional to operational. Three forces make it urgent:
1. **Regulatory pressure** — NIST AI RMF cited in US federal procurement; EU AI Act binding law; DPDPA Rules 2025 in India
2. **Customer expectations** — enterprise customers now include AI governance requirements in security questionnaires
3. **Internal accountability** — AI incidents without governance infrastructure result in undocumented decisions, reputational damage, and ungovernable liability

---

## The Governance Stack

No single framework covers everything. Mature organisations layer three tiers:

```
┌─────────────────────────────────────┐
│  BINDING LAW (EU AI Act, DPDPA)     │  ← Hard compliance obligations
├─────────────────────────────────────┤
│  CERTIFIABLE STANDARD (ISO 42001)   │  ← External audit proof
├─────────────────────────────────────┤
│  RISK METHODOLOGY (NIST AI RMF)     │  ← Common vocabulary + practice
└─────────────────────────────────────┘
```

Build to the strongest common denominator, and you satisfy several layers without duplicating work.

---

## NIST AI Risk Management Framework (AI RMF)

### Overview

Published January 2023, updated through 2025. Technically voluntary, but functions as the de facto standard for AI governance in the US. Referenced in Executive Order 14110 (federal agencies and contractors), state-level AI laws, and enterprise procurement requirements.

The framework has **four core functions** applied at the AI system level:

| Function | Question It Answers | Key Activities |
|---|---|---|
| **GOVERN** | Who is accountable? What are the policies? | Define policies, establish roles, build culture |
| **MAP** | What AI systems do we have, and what are their risks? | Inventory systems, categorise risk, context analysis |
| **MEASURE** | How bad are the risks, and can we quantify them? | Evaluate, benchmark, test, monitor |
| **MANAGE** | What do we do about the risks? | Treat, respond, recover, improve |

**Important:** GOVERN spans the entire organisation. MAP, MEASURE, and MANAGE apply at the individual AI system level.

### Generative AI Profile (NIST AI 600-1)

Published July 26, 2024. Extends the base RMF with **12 risk categories specific to LLMs and generative AI**:

| Risk Category | Description | Example Failure |
|---|---|---|
| Confabulation | Model generates plausible but false content | Legal document with invented case citations |
| CBRN Information | Hazardous synthesis information produced | Model assists with dangerous material creation |
| Data Privacy | Training data leakage; PII in outputs | Employee data surfaced in HR chatbot |
| Human-AI Configuration | Users over-trust AI outputs | Clinician accepts hallucinated drug dosage |
| Information Integrity | Disinformation at scale | AI-generated content campaigns |
| Information Security | Prompt injection, model theft | Adversary extracts system prompt |
| Intellectual Property | Copyright violation in generated content | Code trained on GPL code without attribution |
| Obscene Content | Harmful or abusive output generation | CSAM, hate speech |
| Operational Misuse | Capability exceeds intended scope | Automation of attacks |
| Prompt Injection | Input manipulates model behaviour | Indirect injection via document |
| Societal Impacts | Bias reinforcement, discrimination | Hiring tool favours certain demographics |
| Value Chain Risks | Third-party model or data vulnerabilities | Compromised fine-tuning dataset |

**Practical implication:** For any LLM system, complete both the base AI RMF and the AI 600-1 profile. Apply AI 600-1 across all 12 categories, then prioritise your top 3–5 for active controls based on your system's risk context.

### Implementation Common Failures

- **The MAP–MEASURE gap**: Organisations complete GOVERN and MAP on paper, then abandon MEASURE because they lack data infrastructure to benchmark risk consistently. Without runtime monitoring, MEASURE is aspirational.
- **Static governance**: Treating AI RMF as a compliance checkbox rather than a continuous improvement cycle. NIST's 2025 updates explicitly frame AI risk management as ongoing.
- **Missing evidence package**: Internal auditors, regulators, and enterprise customers require documentary proof. Compile: governance charter + policy docs, AI system inventory with MAP documentation, pre-deployment evaluation reports and monitoring data, risk treatment decisions and incident logs.

---

## ISO/IEC 42001:2023 — AI Management Systems

ISO 42001 is the certifiable standard for AI management systems. It's to AI governance what ISO 27001 is to information security — a structure organisations can be externally audited against and certified for.

**Why it matters for enterprises:**
- Provides external, independently verifiable proof of governance maturity
- Increasingly required in B2B procurement (especially in regulated sectors and the EU)
- Complements NIST AI RMF: NIST gives you the methodology; ISO 42001 gives you the certifiable management system

**Key requirements of ISO 42001:**
- Leadership commitment (policy, roles, resources)
- Risk assessment and treatment for AI systems
- Objectives, planning, and performance evaluation
- Internal audit and management review
- Continual improvement process

**Implementation approach:** Build your NIST AI RMF implementation first. ISO 42001 maps closely to NIST's four functions and can largely be satisfied by the same documentation and processes. Don't run them as separate programmes.

---

## EU AI Act — Key Enterprise Obligations (2024)

The EU AI Act entered into force August 1, 2024. It is **binding law** across the EU and applies to any organisation offering AI systems to EU markets or deploying AI in EU contexts — regardless of where the organisation is headquartered.

### Risk Classification

| Category | Definition | Requirements |
|---|---|---|
| **Unacceptable Risk** | AI uses banned outright | Social scoring, real-time biometric surveillance in public spaces, subliminal manipulation | Prohibited |
| **High Risk** | Critical infrastructure, employment, education, essential services, law enforcement | Full conformity assessment, logging, human oversight, transparency, registration |
| **Limited Risk** | Chatbots, deepfakes | Transparency obligations (users must know they are interacting with AI) |
| **Minimal Risk** | Most AI applications | No specific obligations (voluntary codes of practice encouraged) |

### GPAI (General Purpose AI) Model Obligations

Applies to foundation model / LLM providers:
- Technical documentation and transparency
- Compliance with EU copyright law
- Information disclosure for downstream deployers
- For "systemic risk" models (frontier scale): adversarial testing, incident reporting, cybersecurity measures

### Enterprise Compliance Priorities

For most enterprises as **deployers** (not providers) of AI:
1. Classify all AI systems in use against the risk taxonomy
2. Identify any High Risk systems — implement full compliance track
3. Ensure transparency disclosures for chatbot / AI interaction interfaces
4. Review AI vendor contracts: providers must supply necessary conformity documentation
5. Implement prohibited use controls (employee monitoring for emotion, social scoring)

**Timeline:** Most provisions applicable from August 2026. GPAI model obligations from August 2025.

---

## Enterprise Governance Operating Model

### Governance Structure

A functional AI governance operating model has five layers:

**Layer 1: Policy (What is allowed)**
- AI use policy — defines permitted uses, risk categories requiring approval, prohibited uses
- Data governance policy — data provenance, consent, retention for AI training
- Third-party AI vendor policy — security, compliance, and contractual requirements

**Layer 2: Roles and Accountability**
- **Chief AI Officer (CAIO)** or AI Governance Lead — owns the AI governance programme
- **AI Ethics / Review Board** — cross-functional (Legal, Risk, HR, Engineering, Business) review for high-risk AI deployments. IBM's model: a standing cross-functional Ethics Board reviews all major AI deployments for ethical, legal, and reputational risk before release
- **AI System Owners** — accountable for each deployed AI system's compliance
- **Data Stewards** — accountable for training data quality and consent

**Layer 3: Process (How decisions are made)**

```
AI Idea → Risk Triage → Design Review → Pre-deployment Evaluation → Deployment → Monitoring → Retirement
              ↓               ↓                    ↓                    ↓             ↓
         Risk Score      Architecture         Red Team /           Go/No-Go        Drift
         Assignment      Sign-off             Compliance Gate       Gate           Alerts
```

**Layer 4: Measurement (How compliance is tracked)**
- AI system inventory — all systems catalogued with MAP documentation
- Compliance rate by risk tier — monthly reporting to governance board
- Incident log — structured record of AI incidents, near-misses, and responses
- Model monitoring dashboard — accuracy, drift, fairness metrics per system

**Layer 5: Assurance (External proof)**
- Internal audit cycle (quarterly for high-risk systems, annually for all systems)
- Third-party assessments for high-risk or customer-facing systems
- Evidence package maintenance for regulator or customer review

### Quality Gates Checklist

Use these gates at each stage of the AI development lifecycle:

**Gate 1: Pre-development (Risk Triage)**
- [ ] AI use case aligned to permitted uses policy?
- [ ] Risk tier classification completed (EU AI Act + NIST MAP)?
- [ ] Data sourcing reviewed for consent and provenance?
- [ ] Legal/compliance sign-off obtained?

**Gate 2: Pre-deployment**
- [ ] NIST MEASURE function completed — baseline benchmarks set?
- [ ] AI 600-1 risk categories evaluated for relevance?
- [ ] Red team / adversarial testing completed?
- [ ] Transparency disclosures in place?
- [ ] Human oversight mechanisms verified?
- [ ] Rollback plan documented?

**Gate 3: Post-deployment (30-day review)**
- [ ] Production monitoring established (accuracy, drift, cost)?
- [ ] Incident response contacts assigned?
- [ ] User feedback loop active?
- [ ] Compliance evidence package updated?

**Gate 4: Ongoing (Quarterly)**
- [ ] Model performance still meeting pre-deployment benchmarks?
- [ ] Risk profile unchanged (no scope creep)?
- [ ] Regulatory requirements unchanged?
- [ ] Data sources still compliant?

---

## AI System Registry — Minimum Viable Template

Every organisation needs an inventory of AI systems. Minimum fields:

| Field | Description |
|---|---|
| System ID | Unique identifier |
| System Name | Human-readable name |
| Business Owner | Accountable executive |
| Technical Owner | Responsible engineer |
| Purpose | What the system does and for whom |
| Risk Tier | Unacceptable / High / Limited / Minimal (EU AI Act) |
| NIST RMF Profile | MAP documentation reference |
| Data Sources | Training and inference data provenance |
| Third-party Models | External models, APIs, or components used |
| Deployment Date | When system went live |
| Last Review Date | Date of most recent governance review |
| Next Review Date | Scheduled next review |
| Monitoring Dashboard | Link to production monitoring |
| Incident Log | Link to incident history |

---

## Connecting Governance to Business

AI governance that exists only in a compliance document is governance theatre. Connect it to business rhythm:

- **Quarterly Business Review**: AI portfolio compliance rate as a standing agenda item
- **Investment gate**: Governance sign-off required before AI projects progress from pilot to production
- **Vendor management**: Require AI governance attestation from all AI vendors annually
- **Board reporting**: High-risk AI system status and AI incident summary in quarterly board pack

---

*Sources: NIST AI RMF 1.0, NIST AI 600-1 (July 2024), ISO/IEC 42001:2023, EU AI Act (2024), Stanford HAI AI Index 2025, NeuralTrust NIST AI RMF Guide 2026, Aurascape AI Compliance Frameworks 2026, EPC Group NIST Enterprise Guide.*
