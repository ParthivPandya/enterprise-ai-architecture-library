# Responsible AI: Frameworks as Actually Implemented

> **Related:** [02-Governance-Framework.md](02-Governance-Framework.md) | [04-Risk-Mitigation.md](04-Risk-Mitigation.md)

---

## The Gap Between Principle and Practice

Most organisations have an AI ethics statement. Far fewer have operationalised it. The World Economic Forum's 2025 Responsible AI Playbook found that insufficient investment in responsible AI talent and tools is the primary factor preventing organisations from operationalising their stated principles.

This document focuses on what responsible AI looks like *in practice* — the structures, processes, reviews, and cultural mechanisms that actual enterprises use, not the principles they publish.

**The maturity arc (Accenture/Stanford HAI, 2025):**

| Stage | Characteristics |
|---|---|
| **Reactive** | Ethics as crisis response. No proactive structure. |
| **Compliant** | Ethics as checkbox. Policies exist, not enforced. |
| **Active** | Review boards, training, pre-deployment gates active. |
| **Integrated** | Responsible AI embedded in product development lifecycle. |
| **Leading** | Innovation enabled *because of* governance maturity; competitive differentiator. |

IDC's Worldwide Responsible AI Survey (Microsoft commissioned): 91% of organisations using AI expect more than a 24% improvement in customer experience, business resilience, sustainability, and operational efficiency — but organisations that use responsible AI solutions *consistently* reported these improvements, versus those without governance structures who experienced more AI-related incidents and rollbacks.

---

## Microsoft: Responsible AI Standard (v2)

**Framework name:** Microsoft Responsible AI Standard  
**Current version:** v2 (2025 Transparency Report published June 2025)  
**What it covers:** Entire lifecycle of AI development — design, data collection, training, deployment, post-release monitoring

### Six Principles with Operational Meaning

| Principle | What It Means in Practice |
|---|---|
| **Fairness** | Systematic fairness testing before release; expanded in 2024 to cover images, audio, video, not just text |
| **Transparency** | Model cards, system cards, capability documentation for all released AI products |
| **Inclusiveness** | Diverse user testing; accessibility standards in AI-generated interfaces |
| **Reliability & Safety** | Red team testing for harmful outputs; human oversight requirements for high-stakes decisions |
| **Privacy & Security** | Data minimisation in training; PII scanning in outputs; privacy reviews for new capabilities |
| **Accountability** | Named system owners; Sensitive Use review process for any deployment that could disproportionately affect people |

### The Sensitive Use Review Process

This is Microsoft's most operationally distinctive mechanism. Any AI capability that could affect users in high-stakes ways — hiring, healthcare, finance, law enforcement, emotional impact — must pass a Sensitive Use review before release. The review:
- Is conducted by the Responsible AI team (cross-functional: ethics, legal, product, engineering)
- Requires the product team to demonstrate how risks are mapped, measured, and managed
- Can result in redesign, delay, or rejection of the feature

**Case Study — Memory in Microsoft 365 Copilot:** The memory feature (retaining user information across conversations) triggered a Sensitive Use review because of privacy implications. The review required the team to demonstrate explicit user control, clear consent flows, and audit mechanisms before release.

**Case Study — Foundry Agent Service Memory:** When Microsoft released long-term memory for AI agents in fall 2025, the team ran a full NIST MAP-MEASURE-MANAGE sequence and published the case study publicly as a model for agentic system governance.

### 2024 Update Highlights
- Expanded risk measurement and mitigation beyond text to images, audio, and video modalities
- Added specific agentic system safeguards (semi-autonomous systems with tool access)
- Proactive, layered approach to EU AI Act compliance integrated into product development

---

## IBM: AI Ethics Board

**Structure:** Cross-functional, enterprise-wide committee  
**Mandate:** Evaluates AI initiatives for ethical, legal, and reputational risk before major deployments  
**Trigger:** Any AI system with material impact on employees, customers, or third parties

### How IBM's Ethics Board Works in Practice

- **Composition:** Representatives from Legal, HR, Supply Chain, Privacy, Security, Product, and the business unit sponsoring the AI initiative
- **Input:** Risk assessment submitted by the AI system owner using IBM's AI Fairness 360 toolkit and related documentation
- **Process:** 30-day review cycle for standard deployments; expedited track for regulated-industry use cases
- **Output:** Approval, conditional approval with required modifications, or rejection with documented reasoning

### IBM AI Tools Stack (Open-Source)

IBM has published three major open-source toolkits as part of their responsible AI programme:

| Toolkit | Purpose | Key Capability |
|---|---|---|
| **AI Fairness 360** | Bias detection and mitigation | 70+ fairness metrics; pre/in/post-processing bias fixes |
| **AI Explainability 360** | Model interpretability | LIME, SHAP, rule-based explanation methods |
| **AI Robustness 360** | Adversarial robustness testing | Attack simulation; robustness benchmarking |

These are production-grade, widely adopted, and represent the clearest example of responsible AI tooling that any enterprise can adopt independently of IBM products.

---

## Google: Principles and Operational Evolution

**Published Principles (2018, updated 2025):** Be socially beneficial; avoid creating or reinforcing unfair bias; be built and tested for safety; be accountable to people; incorporate privacy design; uphold high standards of scientific excellence; be made available for uses that accord with these principles.

**Restrictions (hard prohibitions):** AI will not be designed or deployed for weaponisation; mass surveillance beyond legal norms; technologies that violate internationally accepted norms and human rights.

### 2025 Operational Updates

In early 2025, Google expanded its internal Responsible AI processes through:
- **Expanded oversight committees** — additional review layers for model capabilities above a defined risk threshold
- **Integrated model risk reviews** — AI Safety and Alignment teams embedded into the standard model release process, not as a separate gate
- **Harmonisation with global standards** — explicit cross-referencing of EU AI Act, NIST AI RMF, and Singapore Model AI Governance in internal reviews

### DeepMind's Safety Research as Operational Practice

DeepMind's safety research arm (now directly integrated into Google DeepMind) conducts:
- **Specification gaming analysis** — identifying when AI systems achieve goals through unintended means
- **Scalable oversight research** — developing methods to verify AI behaviour as systems become more capable
- **Red teaming** — systematic adversarial testing of frontier models before deployment

---

## Practical Implementation: Building Your Responsible AI Programme

### The Five Components Every Enterprise Needs

**Component 1: Responsible AI Policy**
A brief, specific document that answers:
- What uses of AI are explicitly permitted?
- What uses require additional review?
- What uses are prohibited?
- Who is accountable for each AI system?

Keep it under 4 pages. Policies that are too long are not read and not followed.

**Component 2: AI System Card (for each deployed system)**
Adapted from the model card concept (Google, 2018), an AI System Card documents:
- Intended use and users
- Known limitations and failure modes
- Performance benchmarks across demographic groups
- Fairness evaluation results
- Human oversight mechanisms
- Contact for issues

**Component 3: Pre-Deployment Evaluation Checklist**
Structured review that every AI system must pass before production deployment. Minimum sections:
- Fairness evaluation (does the system perform equitably across demographic groups?)
- Privacy review (what personal data is processed? Is consent obtained?)
- Safety testing (what are the worst-case failure modes? Have they been tested?)
- Transparency check (can users understand why the AI made a decision?)
- Rollback plan (how is the system disabled if it causes harm?)

**Component 4: Ongoing Monitoring**
A responsible AI system doesn't stay responsible on its own. Monitor:
- Output quality and accuracy against baseline
- Fairness metrics across user groups (drift is common as user populations change)
- Incident reports from users and operations teams
- Regulatory changes that affect the system's compliance status

**Component 5: Training and Culture**
Microsoft's 2025 report found that responsible AI culture — not just tools — is the differentiator between organisations that scale responsibly and those that experience incidents.

Minimum training programme:
- **AI Literacy for All Staff** — what AI is, what it isn't, how to use it responsibly (2 hours, annual)
- **Responsible AI for Practitioners** — bias, fairness, privacy, security for developers and data scientists (8 hours, annual)
- **AI Governance for Leaders** — accountability, risk, ethics for decision-makers (4 hours, annual)

---

## Responsible AI Maturity Self-Assessment

Answer yes/no to these questions to gauge your current maturity:

| Question | Maturity Indicator |
|---|---|
| Do you have a published AI use policy with specific permitted and prohibited uses? | Active |
| Do you have named owners for each deployed AI system? | Active |
| Does every AI system have a documented AI System Card? | Active |
| Do you run pre-deployment fairness and safety evaluations? | Active |
| Do you have an AI review board or equivalent? | Integrated |
| Is responsible AI embedded in your product development lifecycle (not as a separate gate)? | Integrated |
| Do you publicly report on your responsible AI programme? | Leading |
| Do you contribute to industry standards and open-source responsible AI tooling? | Leading |

---

## Fairness in Practice: What "Equitable AI" Actually Requires

Fairness is the most frequently stated responsible AI principle and the one most organisations are least equipped to operationalise. Concretely:

**Step 1: Define the relevant demographic groups.** What groups matter for your use case? For a hiring AI: gender, race/ethnicity, age. For a credit model: income group, geography.

**Step 2: Measure disparate outcomes.** Does the system perform significantly differently across these groups? Use AI Fairness 360 or equivalent tooling to run statistical tests.

**Step 3: Identify the source of disparity.** Is it training data? Feature selection? Label quality? The source determines the mitigation.

**Step 4: Apply a mitigation strategy.**
- *Pre-processing:* Rebalance training data; remove proxy features
- *In-processing:* Add fairness constraints to the training objective
- *Post-processing:* Adjust decision thresholds by group

**Step 5: Document and monitor.** Record what you found, what you did, and set up monitoring to alert if disparity re-emerges.

**Key insight:** Fairness is not a one-time assessment. As user populations shift, training data ages, and models drift, fairness characteristics change. Build monitoring into production, not just pre-deployment.

---

## Transparency in Practice: Explainability by Deployment Context

Different contexts require different levels of explanation:

| Context | Required Explanation Level | Appropriate Method |
|---|---|---|
| Low-stakes consumer features | General transparency ("powered by AI") | Disclosure label |
| Customer-facing decisions (recommendations, pricing) | Feature-level explanation ("recommended because...") | LIME / SHAP summary |
| High-stakes decisions (credit, hiring, healthcare) | Full rationale with confidence and uncertainty | Counterfactual + SHAP |
| Regulated decisions (insurance, lending) | Legally auditable rationale | Rule extraction + audit log |

---

*Sources: Microsoft Responsible AI Transparency Report 2025, IBM AI Ethics Board documentation, Google AI Principles 2025, WEF Advancing Responsible AI Innovation Playbook 2025, Accenture/Stanford HAI Responsible AI Maturity Index 2025, IDC Worldwide Responsible AI Survey, AI Fairness 360 documentation.*
