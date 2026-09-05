# AI Standards for the Indian Enterprise Context

> **Related:** [../01-AI-Governance/02-Governance-Framework.md](../01-AI-Governance/02-Governance-Framework.md) | [01-Business-Value.md](01-Business-Value.md)

---

## India's Distinctive AI Regulatory Approach

India has taken a deliberately different path from the EU on AI regulation. While the EU AI Act is a binding, comprehensive law with risk tiers and enforcement mechanisms, **India has chosen a "light-touch," innovation-first approach** — governing AI primarily through existing laws (DPDPA), sector-specific regulators, and voluntary guidelines rather than a standalone AI law.

IT Secretary S. Krishnan at the November 2025 IndiaAI Governance Guidelines launch: *"India has consciously chosen not to lead with regulation but to encourage innovation while studying global approaches."*

This creates a specific compliance and strategy landscape for Indian enterprises and multinationals operating in India:

| Dimension | India | EU |
|---|---|---|
| Primary AI law | No standalone AI law (as of 2026) | EU AI Act (binding, 2024) |
| Data protection | DPDPA 2023 + DPDP Rules 2025 | GDPR (since 2018) |
| AI governance approach | Voluntary guidelines + sectoral regulation | Mandatory risk classification |
| AI governance body | AIGG (AI Governance Group) + AISI (AI Safety Institute) proposed | EU AI Office |
| Penalty ceiling | INR 250 crore (~$30M USD) for DPDPA violations | EU AI Act: up to €35M or 7% of global turnover |

**Enterprise implication:** Indian enterprises face fewer mandatory AI-specific obligations than EU counterparts, but the DPDPA creates substantial data governance requirements for any AI system processing personal data — and MeitY's Governance Guidelines establish a clear preferred standard that regulators and enterprise customers will expect compliance with.

---

## Digital Personal Data Protection Act 2023 (DPDPA) — AI Implications

### The Timeline

| Date | Event |
|---|---|
| August 11, 2023 | DPDPA receives Presidential assent |
| November 14, 2025 | MeitY notifies DPDP Rules 2025 — the clock starts |
| November 2026 | Phase 1 obligations apply (Consent Manager registration, breach notification) |
| May 13, 2027 | Full compliance deadline for all entities |

### What the DPDPA Means for AI Systems

Every AI system processing personal data of Indian residents (Data Principals) faces these obligations:

**Obligation 1: Lawful Basis for Processing**
AI systems must have a lawful basis for processing personal data. The two available bases:
- **Consent** — freely given, informed, specific, and revocable. Must be in plain language. Applies to most non-government AI deployments.
- **Legitimate Uses** — defined in Schedule I (national security, employment, medical emergency, etc.). Narrower than GDPR's "legitimate interests."

**AI challenge:** Training modern AI systems requires large datasets, often assembled from multiple sources. The DPDPA's consent requirement and purpose limitation provisions can conflict with the broad, open-ended nature of AI training. Every training dataset for an India-facing AI system must have documented, lawful provenance.

**Obligation 2: Purpose Limitation**
Data collected for one purpose cannot be used for a different purpose without new consent. **This directly affects:** using customer transaction data to train AI models, using employee data to build HR prediction models, using support chat data to fine-tune AI assistants.

**Practical fix:** Explicitly include AI model training as a stated purpose in consent notices. Separate consent for secondary AI training uses.

**Obligation 3: Data Minimisation**
Only personal data necessary for the specified purpose should be processed. For AI systems, this means:
- Audit training datasets for unnecessary personal data fields
- Remove PII where aggregate or anonymised data achieves the same training outcome
- Use synthetic data generation for sensitive domains (healthcare, finance)

**Obligation 4: Security Safeguards (Rule 6)**
Technical and organisational security measures must be implemented. Specifically relevant to AI:
- Encryption of personal data at rest and in transit
- Access controls — only personnel who need the data for the specified purpose
- The DPDP Rules explicitly state: "technical measures, including algorithmic software used for processing personal data, do not pose risks to the rights of data principals"

**Obligation 5: Data Principal Rights**
Indian residents have rights over their data — including the right to erasure (Right to Be Forgotten). **AI challenge:** Machine unlearning — removing a specific individual's data from a trained model — is an active research area but not yet a solved engineering problem. Enterprise architecture must account for this from day one of AI system design.

**MeitY's Safe & Trusted AI pillar explicitly selected Machine Unlearning as one of its eight priority research areas (Round 1 EoI, 2024).**

**Obligation 6: Breach Notification**
Data breaches must be reported to the Data Protection Board. AI-specific breaches that trigger this obligation include: training data leakage, model inversion attacks that extract personal data, prompt injection attacks that expose PII.

### Significant Data Fiduciaries (SDFs) — Enhanced Obligations

Entities designated as SDFs (based on volume, sensitivity, and risk of data processed) face additional requirements:
- Appoint a Data Protection Officer (DPO)
- Conduct annual Data Protection Impact Assessment (DPIA) and audit
- Ensure personal data (specified by government) is not transferred outside India
- Submit DPIA report to the Data Protection Board

**Who is likely an SDF?** Large enterprises processing high volumes of sensitive personal data — major e-commerce platforms, healthcare providers, financial services firms, social media companies.

**Architecture implication:** If there is any possibility of SDF designation, design AI systems with India data residency from day one. Retrofitting data localisation into existing AI architectures is expensive and disruptive.

---

## IndiaAI Mission — Capacity and Enablement

### Overview

Cabinet approved: **March 7, 2024**  
Budget: **₹10,370 crore total; ₹2,000 crore allocated in Union Budget 2025–26**  
Implementing body: Ministry of Electronics and Information Technology (MeitY)

The IndiaAI Mission is a **capacity-building programme, not a regulation**. It lowers barriers for Indian enterprises and startups to build competitive AI systems. Key pillars for enterprise use:

**Pillar 1: AI Compute Access**
- 10,000+ GPU compute capacity procured and made available to Indian startups, researchers, and enterprises at subsidised rates
- Directly addresses the compute access barrier that disadvantages Indian organisations relative to hyperscaler-backed Western firms

**Pillar 2: IndiaAI Datasets Platform**
- Structured, AI-ready non-personal datasets for AI research and development
- Covers domains including agriculture, health, transport, and governance
- Solves the data access problem for building domain-specific Indian AI models

**Pillar 3: IndiaAI Application Development Initiative**
- Problem statements from Central Ministries and State Departments for AI solutions
- Focus sectors: healthcare, education, agriculture, smart cities, transportation
- Pathway for Indian enterprises to develop government-adopted AI solutions

**Pillar 4: Safe & Trusted AI (Responsible AI Research)**
Round 1 (selected projects): Machine Unlearning, Synthetic Data Generation, AI Bias Mitigation, Privacy-Enhancing Tools, Explainable AI, AI Governance Testing, AI Ethical Certification, Algorithm Auditing Tools.

Round 2 (2025): Watermarking & Labelling, additional responsible AI tools for the Indian context.

**Enterprise relevance:** These research outputs will become the indigenous technical tools referenced in MeitY's AI Governance Guidelines — enterprises should track and adopt them as they become available.

**Pillar 5: IndiaAI FutureSkills**
AI courses integrated into undergraduate, master's, and PhD programmes. Enterprise HR teams can expect AI-literate talent from Indian universities to grow significantly over the next 5 years.

---

## MeitY AI Governance Guidelines (November 2025)

Published November 5, 2025. This is India's AI governance standard — not law, but the framework that sectoral regulators are expected to incorporate and that enterprise customers will reference in vendor assessments.

### Seven Guiding Principles

| Principle | Enterprise Implication |
|---|---|
| **Safety and Reliability** | AI systems must be tested for safety before deployment; maintain human oversight for high-risk decisions |
| **Accountability** | Identifiable human responsibility for each AI system's outcomes; audit trails required |
| **Transparency** | Users must know when AI is involved in decisions affecting them; explainability required for significant decisions |
| **Fairness and Non-discrimination** | AI systems must be evaluated for bias; special attention to caste, gender, religion in Indian context |
| **Privacy** | DPDPA compliance as a baseline; additional privacy-by-design for AI systems |
| **Innovation** | Governance should enable, not prevent, innovation; risk-proportionate approach |
| **Inclusion** | AI benefits should be accessible to all segments of Indian society, including Bharat |

### Key Structural Elements

**AI Governance Group (AIGG):** Inter-ministerial coordination body for AI policy. Enterprises should monitor AIGG outputs for sector-specific guidance.

**AI Safety Institute (AISI):** Proposed testing institute for AI systems. Will likely become the body that evaluates AI systems for conformity with Indian standards.

**Risk Classification Approach:** India's approach classifies AI risks by context and sector rather than by AI system type (contrast with EU AI Act's system-type classification). This means the applicable obligations depend on what sector you're in and who is affected.

**Incident Reporting Mechanism:** The guidelines establish a mechanism for reporting AI incidents. Enterprises should build incident reporting into their AI governance processes.

### Sectoral Regulators — What to Watch

MeitY's approach delegates sector-specific AI governance to existing regulators:

| Sector | Regulator | Key Focus Areas for AI |
|---|---|---|
| Financial Services | RBI + SEBI | Algorithmic trading, credit decisioning, fraud detection |
| Healthcare | CDSCO + NHA | AI-assisted diagnosis, clinical decision support |
| Telecom | TRAI | AI in network management, customer service |
| Insurance | IRDAI | AI underwriting, claims processing |
| Education | MoE | AI in assessments, student data protection |

**The RBI FREE-AI Committee Report (2025)** is particularly significant for financial services enterprises — it specifically addresses AI in financial services and will shape RBI's AI governance expectations.

---

## Localized Hosting and Data Residency Architecture

### The Data Localisation Landscape in India

India's data localisation requirements are sector-specific and evolving:

| Sector | Current Requirement | Status |
|---|---|---|
| Payment data | RBI: payment system data must be stored exclusively in India | Enforced |
| Financial data | RBI guidance for other financial data: mirroring in India | Guidance, not hard law |
| DPDPA (SDFs) | Government can mandate that specified personal data not be transferred outside India | Anticipated for SDFs |
| General personal data | DPDPA: transfers to permitted countries/territories allowed (permissive default) | Active |

### Architecture Patterns for Indian Data Residency

**Pattern 1: India-Region First**
Deploy all AI infrastructure in available India cloud regions:
- AWS ap-south-1 (Mumbai) + ap-south-2 (Hyderabad)
- Azure Central India + South India + West India
- Google Cloud asia-south1 (Mumbai) + asia-south2 (Delhi)

For Bedrock / Azure OpenAI / Vertex AI, verify model availability in India regions — not all frontier models are available in all regions. As of 2026, availability is improving but not universal.

**Pattern 2: Data Residency Envelope**
For enterprises where some data is India-resident and some global:
- Indian personal data processed only in India-resident infrastructure
- Non-personal / anonymised data can flow globally for model training
- Clear data classification at ingestion point — personal vs. non-personal label attached before routing

**Pattern 3: On-Premises / Private Cloud (Sovereign AI)**
For the highest sensitivity (government, defence, critical infrastructure):
- Open-source models (Llama 3, Mistral, Gemma) deployed on-premises or on Government Cloud (NIC/MeghRaj)
- No data leaves the perimeter
- Fine-tuned on Indian domain data (IndiaAI Datasets Platform)

**Bhashini Integration:** For AI systems serving Bharat (rural, non-English populations), integrate Bhashini — MeitY's translation and language understanding platform covering 22 scheduled languages. This is not optional for government-facing AI or systems targeting Tier 2/3 cities.

---

## State-Level AI Initiatives: Enterprise Opportunity Map

| State | Initiative | Enterprise Opportunity |
|---|---|---|
| **Tamil Nadu** | TNAIM (₹13.93 crore, 5-year plan) | AI governance solutions; civic AI; healthcare AI |
| **Karnataka** | Shiksha Co-pilot (education AI); GCC Policy (500 new centres) | EdTech AI; GCC AI services |
| **Andhra Pradesh** | Smart city AI; governance AI | Infrastructure AI; civic services |
| **Telangana** | T-Hub AI; WE Hub AI | Startup ecosystem AI partnerships |
| **Maharashtra** | Financial sector AI; smart infrastructure | BFSI AI; logistics AI |

---

## Compliance Roadmap for Indian Enterprises

### Immediate Actions (Now — November 2026)

- [ ] Audit all AI systems processing Indian personal data — catalogue data types, lawful basis, and processing purpose
- [ ] Review and update all privacy notices to include AI processing disclosures
- [ ] Implement consent management for personal data used in AI training
- [ ] Assess SDF designation likelihood — begin enhanced controls if applicable
- [ ] Review AI vendor contracts — suppliers must meet DPDPA obligations for data they process

### Phase 1 (By November 2026)

- [ ] Consent Manager registration process (if applicable)
- [ ] Data breach notification process operational
- [ ] DPO appointed (SDFs)

### Phase 2 (By May 2027 — Full Compliance)

- [ ] Annual DPIA conducted and submitted (SDFs)
- [ ] Data localisation controls implemented (SDFs / high-sensitivity sectors)
- [ ] Security safeguards (Rule 6) fully implemented across all AI systems
- [ ] Machine unlearning / data erasure process documented (even if manual interim process)
- [ ] Algorithmic transparency process for significant decisions (credit, hiring, admissions)
- [ ] Grievance redressal mechanism live and tested

---

*Sources: IAPP India DPDPA Rules and AI Governance Guidelines Note 2026, MeitY DPDP Rules 2025 notification, MeitY India AI Governance Guidelines November 2025, IndiaAI Mission Cabinet approval March 2024, IndiaAI.gov.in EoI Round 1 and 2, ReedSmith India Data Protection and AI 2026, Saikrishna & Associates India AI Governance Guidelines Analysis, DPDPA AI Compliance Guide 2026, India AI Rulebook IndiaAI Mission Analysis.*
