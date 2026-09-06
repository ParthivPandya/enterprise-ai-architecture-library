# AI Enterprise Architecture Library

![Enterprise AI Architecture](enterprise_ai_architecture.jpg)
> A practitioner-grade, research-backed reference for Enterprise Architects, Chief AI Officers, Strategy Leaders, and Governance professionals building and scaling AI in large organisations — written to be used, not just read.

---

## About This Library

This library was built to close the gap between AI hype and enterprise reality. Every section is grounded in real-world case studies, established frameworks, and actionable patterns. It comprises two primary components:

### 1. The Core Architecture Library (Parts 0–4)
- **Part 0 — Foundations:** How AI actually works, and the model landscape you're navigating
- **Part 1 — AI Governance & Responsible AI:** How to govern AI spend, quality, ethics, risk, and failure at scale
- **Part 2 — AI Strategy & Enterprise Adoption:** How to create measurable business value across industries and contexts
- **Part 3 — AI in EA Practice:** How Enterprise Architects must evolve their practice, tools, and teams
- **Part 4 — Future of AI:** Sovereign AI, geopolitics, and organizational transformation

### 2. The Official [AIEA® Standard](ai-ea-library/05-Standards/README.md) (Parts 1–7 & Series Guides)
A comprehensive, formal standard for AI Enterprise Architecture extending TOGAF 10 with normative precision:
- **Part 1 (AIEA-101):** [Introduction and Core Concepts](ai-ea-library/05-Standards/AIEA-101-Introduction-Core-Concepts.md)
- **Part 2 (AIEA-201):** [AI Architecture Development Method (AI-ADM)](ai-ea-library/05-Standards/AIEA-201-AI-ADM.md)
- **Part 3 (AIEA-301):** [AI Architecture Content Framework](ai-ea-library/05-Standards/AIEA-301-Content-Framework.md)
- **Part 4 (AIEA-401):** [AI Enterprise Architecture Capability & Governance](ai-ea-library/05-Standards/AIEA-401-Capability-Governance.md)
- **Part 5 (AIEA-501):** [AI Reference Models & Technical Standards](ai-ea-library/05-Standards/AIEA-501-Reference-Models.md)
- **Part 6 (AIEA-601):** [Definitions and Glossary](ai-ea-library/05-Standards/AIEA-601-Definitions-Glossary.md)
- **Part 7 (AIEA-701):** [A Practitioner's Approach to Developing AI Enterprise Architecture](ai-ea-library/05-Standards/AIEA-701-Practitioners-Guide.md)
- **Series Guides (06-Series Guide):** [AIEA-G01: Financial Services](ai-ea-library/06-Series%20Guide/AIEA-G01-Financial-Services.md) | [AIEA-G02: Healthcare](ai-ea-library/06-Series%20Guide/AIEA-G02-Healthcare.md) | [AIEA-G03: Indian Enterprises](ai-ea-library/06-Series%20Guide/AIEA-G03-Indian-Enterprises.md) | [AIEA-G04: Responsible AI](ai-ea-library/06-Series%20Guide/AIEA-G04-Responsible-AI-in-Practice.md) | [AIEA-G05: Agentic AI](ai-ea-library/06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md) | [AIEA-G06: Sovereign AI](ai-ea-library/06-Series%20Guide/AIEA-G06-Sovereign-AI.md) | [AIEA-G07: AI FinOps](ai-ea-library/06-Series%20Guide/AIEA-G07-AI-FinOps.md) | [AIEA-G08: LLMOps](ai-ea-library/06-Series%20Guide/AIEA-G08-LLMOps-Enterprise.md)

### 3. [Practitioner Toolkits & Playbooks](ai-ea-library/07-Toolkits-and-Playbooks/README.md) (Section 07)
Actionable execution toolkits, diagnostic surveys, modeling catalogs, and operating playbooks:
- **Toolkit 01 (AIEA-TK-01):** [AI Readiness Assessment Toolkit](ai-ea-library/07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md)
- **Toolkit 02 (AIEA-TK-02):** [Enterprise AI Metamodel Catalog](ai-ea-library/07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md)
- **Toolkit 03 (AIEA-TK-03):** [Architecture Principles Catalog](ai-ea-library/07-Toolkits-and-Playbooks/03-Architecture-Principles-Catalog.md)
- **Playbook 04 (AIEA-TK-04):** [AI Governance Operating Playbook](ai-ea-library/07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md)
- **Playbook 05 (AIEA-TK-05):** [AI Strategy Execution Playbook](ai-ea-library/07-Toolkits-and-Playbooks/05-AI-Strategy-Execution-Playbook.md)
- **Playbook 06 (AIEA-TK-06):** [EA Practice Evolution Playbook](ai-ea-library/07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md)
---

## Repository Structure & Hierarchy

```text
AI Enterprise Architecture/
├── README.md                      <-- Root Master Portal
└── ai-ea-library/
    ├── 00-Foundations/            <-- Practitioner Book (Part 0: How LLMs work, models, data, agents)
    ├── 01-AI-Governance/          <-- Practitioner Book (Part 1: FinOps, governance, safety, risks)
    ├── 02-AI-Strategy/            <-- Practitioner Book (Part 2: Value, use cases, industry playbooks)
    ├── 03-EA-Practice/            <-- Practitioner Book (Part 3: ADM integration, runbooks, CoE)
    ├── 04-Future/                 <-- Practitioner Book (Part 4: Future of work, sovereign AI)
    ├── 05-Standards/              <-- The Core AIEA® Standards Specification (Parts 1–7)
    │   ├── README.md              <-- AIEA-001 Official Standard Overview & Charter
    │   ├── AIEA-101-...           <-- Part 1: Introduction and Core Concepts
    │   ├── AIEA-201-...           <-- Part 2: AI-ADM Method
    │   ├── AIEA-301-...           <-- Part 3: Content Framework
    │   ├── AIEA-401-...           <-- Part 4: Capability and Governance
    │   ├── AIEA-501-...           <-- Part 5: Reference Models and Technical Standards
    │   ├── AIEA-601-...           <-- Part 6: Definitions and Glossary
    │   └── AIEA-701-...           <-- Part 7: A Practitioner's Approach to Developing AI-EA
    ├── 06-Series Guide/           <-- Specialized Implementation Manuals (AIEA-G01 to G08)
    │   ├── AIEA-G01-...           <-- Financial Services (BFSI)
    │   ├── AIEA-G02-...           <-- Healthcare & Life Sciences
    │   ├── AIEA-G03-...           <-- Indian Enterprise Context (DPDPA)
    │   ├── AIEA-G04-...           <-- Responsible AI in Practice
    │   ├── AIEA-G05-...           <-- Agentic AI Architecture & Swarms
    │   ├── AIEA-G06-...           <-- Sovereign AI Architecture
    │   ├── AIEA-G07-...           <-- AI FinOps & Token Economics
    │   └── AIEA-G08-...           <-- LLMOps for Enterprise
    └── 07-Toolkits-and-Playbooks/ <-- Practitioner Toolkits & Playbooks (AIEA-TK-01 to TK-06)
        ├── README.md              <-- Catalog Overview & Workflow Map
        ├── 01-AI-Readiness-...    <-- 30-Question Diagnostic & Scoring Rubric
        ├── 02-Enterprise-AI-...   <-- ArchiMate 3.2 Metamodel & JSON Schema
        ├── 03-Architecture-...    <-- 15 Normative Principles & Audit Tests
        ├── 04-AI-Governance-...   <-- AIAB Charters & Statutory Runbooks
        ├── 05-AI-Strategy-...     <-- Capability Heatmaps & 3-Year TCO/NPV
        └── 06-EA-Practice-...     <-- 4 Architect Personas & Modern Tooling
```

---

## How to Use This Library

| Your Role | Recommended Starting Point |
|---|---|
| Chief AI Officer / CDO | [02-AI-Strategy/01-Business-Value.md](ai-ea-library/02-AI-Strategy/01-Business-Value.md) |
| Enterprise Architect | [03-EA-Practice/01-Driving-Adoption.md](ai-ea-library/03-EA-Practice/01-Driving-Adoption.md) |
| AI Governance / Risk | [01-AI-Governance/02-Governance-Framework.md](ai-ea-library/01-AI-Governance/02-Governance-Framework.md) |
| CTO / CIO | [03-EA-Practice/07-AI-Center-of-Excellence.md](ai-ea-library/03-EA-Practice/07-AI-Center-of-Excellence.md) |
| Finance / FinOps | [01-AI-Governance/01-FinOps.md](ai-ea-library/01-AI-Governance/01-FinOps.md) |
| Indian Enterprise Context | [02-AI-Strategy/04-Indian-Enterprise-Context.md](ai-ea-library/02-AI-Strategy/04-Indian-Enterprise-Context.md) |
| New to AI | [00-Foundations/01-How-LLMs-Work.md](ai-ea-library/00-Foundations/01-How-LLMs-Work.md) |
| Evaluating AI vendors | [03-EA-Practice/03-Strategic-Runbooks.md](ai-ea-library/03-EA-Practice/03-Strategic-Runbooks.md) |
| Conducting AI Readiness Audit | [07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md](ai-ea-library/07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md) |
| Enterprise AI Metamodeling | [07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md](ai-ea-library/07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md) |
| AI Architecture Principles | [07-Toolkits-and-Playbooks/03-Architecture-Principles-Catalog.md](ai-ea-library/07-Toolkits-and-Playbooks/03-Architecture-Principles-Catalog.md) |
| AI Governance Operating Cadence | [07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md) |
| Strategy & Business Case TCO/NPV | [07-Toolkits-and-Playbooks/05-AI-Strategy-Execution-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/05-AI-Strategy-Execution-Playbook.md) |
| EA Team Skills & Tooling Evolution | [07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md) |

---

## Part 00 — Foundations

| Document | What It Covers |
|---|---|
| [01-How-LLMs-Work.md](ai-ea-library/00-Foundations/01-How-LLMs-Work.md) | Tokens, transformers, attention, hallucination, context windows — explained for architects, not data scientists |
| [02-Foundation-Model-Landscape.md](ai-ea-library/00-Foundations/02-Foundation-Model-Landscape.md) | The ecosystem map: GPT, Claude, Gemini, Llama, Mistral, DeepSeek — evaluation framework and build/buy/fine-tune decision tree |
| [03-Data-Architecture-for-AI.md](ai-ea-library/00-Foundations/03-Data-Architecture-for-AI.md) | Data lakes/lakehouses, feature stores, vector DB selection guide, data quality for AI, data contracts, the data flywheel |
| [04-Multi-Agent-Orchestration.md](ai-ea-library/00-Foundations/04-Multi-Agent-Orchestration.md) | Agent topology patterns (sequential, hierarchical, debate, network), LangGraph vs AutoGen vs CrewAI, governance non-negotiables |

---

## Part 01 — AI Governance & Responsible AI

| Document | What It Covers |
|---|---|
| [01-FinOps.md](ai-ea-library/01-AI-Governance/01-FinOps.md) | AI spend governance, token economics, cost attribution, model tiering, chargeback frameworks — with FinOps maturity model |
| [02-Governance-Framework.md](ai-ea-library/01-AI-Governance/02-Governance-Framework.md) | NIST AI RMF 1.0 + AI 600-1, ISO/IEC 42001, EU AI Act, enterprise governance operating model, quality gate checklists |
| [03-Responsible-AI.md](ai-ea-library/01-AI-Governance/03-Responsible-AI.md) | Microsoft, IBM, Google RAI implementations — fairness, bias, transparency as actually deployed |
| [04-Risk-Mitigation.md](ai-ea-library/01-AI-Governance/04-Risk-Mitigation.md) | OWASP LLM Top 10 (2025/2026), red teaming methodology, secure AI architecture patterns, AI incident response |
| [05-When-AI-Goes-Wrong.md](ai-ea-library/01-AI-Governance/05-When-AI-Goes-Wrong.md) | Six real failure case studies: IBM Watson ($4B loss), Amazon hiring AI, Air Canada legal ruling, DPD viral crisis, NYC MyCity, McDonald's drive-thru |

---

## Part 02 — AI Strategy & Enterprise Adoption

| Document | What It Covers |
|---|---|
| [01-Business-Value.md](ai-ea-library/02-AI-Strategy/01-Business-Value.md) | KPIs, OKRs, ROI frameworks, the productivity J-curve, pilot-to-production patterns, the AI Value Dashboard |
| [02-Agentic-AI-Use-Cases.md](ai-ea-library/02-AI-Strategy/02-Agentic-AI-Use-Cases.md) | 45+ enterprise functions mapped across HR, Finance, IT, Legal, Sales, Operations, Customer Service |
| [03-Education-and-Defence.md](ai-ea-library/02-AI-Strategy/03-Education-and-Defence.md) | AI adoption patterns in K-12, higher education, and defence (NATO, DoD, Five Eyes) — with case studies |
| [04-Indian-Enterprise-Context.md](ai-ea-library/02-AI-Strategy/04-Indian-Enterprise-Context.md) | DPDPA + DPDP Rules 2025, IndiaAI Mission, MeitY AI Governance Guidelines, localized hosting patterns |
| [05-Industry-Playbooks.md](ai-ea-library/02-AI-Strategy/05-Industry-Playbooks.md) | Deep playbooks for BFSI (HDFC, SBI, JPMorgan), Healthcare (Watson lessons, imaging AI), Manufacturing (predictive maintenance, quality control) |
| [06-AI-Change-Management.md](ai-ea-library/02-AI-Strategy/06-AI-Change-Management.md) | The people side: resistance types, ADKAR for AI, the change plan structure, measuring real adoption not login rates |
| [07-AI-Procurement-and-Contracts.md](ai-ea-library/02-AI-Strategy/07-AI-Procurement-and-Contracts.md) | TCO model, critical contract clauses (data training, IP, model versioning, SLA, data residency, exit), India-specific vendor landscape |

---

## Part 03 — AI in EA Practice

| Document | What It Covers |
|---|---|
| [01-Driving-Adoption.md](ai-ea-library/03-EA-Practice/01-Driving-Adoption.md) | EA's role bridging business and tech, TOGAF ADM for AI phase-by-phase, risk-proportionate governance model |
| [02-AI-Design-Decisions.md](ai-ea-library/03-EA-Practice/02-AI-Design-Decisions.md) | When AI makes architecture decisions: agentic EA tools (Ardoq, Salesforce), the four evolving architect roles (Forrester) |
| [03-Strategic-Runbooks.md](ai-ea-library/03-EA-Practice/03-Strategic-Runbooks.md) | Four complete gate-by-gate runbooks: Use Case Evaluation, Vendor Onboarding, Production Launch, System Retirement |
| [04-Hands-on-Workshops.md](ai-ea-library/03-EA-Practice/04-Hands-on-Workshops.md) | Six facilitated workshop designs: Discovery Sprint, Architecture Decision, Red Team, FinOps Sprint, Governance Maturity, Future-State Design |
| [05-LLMOps.md](ai-ea-library/03-EA-Practice/05-LLMOps.md) | Shipping AI to production: MLOps maturity ladder, the full LLMOps stack, CI/CD pipeline for LLMs, production failure modes |
| [06-Prompt-Engineering-Enterprise.md](ai-ea-library/03-EA-Practice/06-Prompt-Engineering-Enterprise.md) | The craft and the system: all 8 core techniques with enterprise examples, prompt library governance, team training programme |
| [07-AI-Center-of-Excellence.md](ai-ea-library/03-EA-Practice/07-AI-Center-of-Excellence.md) | Hub-and-spoke operating model, full role definitions, CoE charter template, 6-month rollout plan, two failure modes to avoid |
| [08-AI-Reference-Architectures.md](ai-ea-library/03-EA-Practice/08-AI-Reference-Architectures.md) | Six production architectures: Enterprise RAG, Text-to-SQL, Document Intelligence, Customer Service AI, Sovereign On-Premises, AI Gateway |

---

## Part 04 — Future of AI

| Document | What It Covers |
|---|---|
| [01-Future-of-Work-with-AI.md](ai-ea-library/04-Future/01-Future-of-Work-with-AI.md) | Three job trajectories (augmentation/transformation/disruption), new skills that matter, India workforce specifics, reskilling investment model |
| [02-Sovereign-AI-and-Geopolitics.md](ai-ea-library/04-Future/02-Sovereign-AI-and-Geopolitics.md) | The AI Cold War, data sovereignty, standards wars (US/EU/China/India approaches), Global South AI moment, what architects must do |

---

## Section 07 — Practitioner Toolkits & Playbooks

| Toolkit Document | Reference | What It Covers |
|---|---|---|
| [01-AI-Readiness-Assessment-Toolkit.md](ai-ea-library/07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md) | AIEA-TK-01 | 30-question diagnostic survey across 6 pillars, quantitative scoring rubric, radar chart mapping, and C-level board pitch deck template |
| [02-Enterprise-AI-Metamodel-Catalog.md](ai-ea-library/07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md) | AIEA-TK-02 | ArchiMate 3.2 mapping specification, entity dictionary (AI-ABBs, Checkpoints, Prompt Templates), and CMDB/EA repository JSON schema |
| [03-Architecture-Principles-Catalog.md](ai-ea-library/07-Toolkits-and-Playbooks/03-Architecture-Principles-Catalog.md) | AIEA-TK-03 | Complete catalog of all 15 normative principles with statements, rationales, implications, anti-patterns, and compliance audit tests |
| [04-AI-Governance-Operating-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md) | AIEA-TK-04 | AIAB meeting rhythms and standing agendas, architectural variance request workflows, and statutory regulatory filing runbooks (EU AI Act, DPDPA) |
| [05-AI-Strategy-Execution-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/05-AI-Strategy-Execution-Playbook.md) | AIEA-TK-05 | Translating corporate OKRs to AI use cases, capability heatmapping matrix, 3-year TCO/NPV financial model template, and 90-day pilot-to-production schedule |
| [06-EA-Practice-Evolution-Playbook.md](ai-ea-library/07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md) | AIEA-TK-06 | Evolving the EA practice: the four modern AI architect personas, architecture-as-code workbench, competency skills matrix, and day-in-the-life operating procedures |

---

## Framework & Standard References

| Framework | Covered In |
|---|---|
| NIST AI RMF 1.0 + Generative AI Profile (AI 600-1) | 01-02, 01-04, 03-03 |
| ISO/IEC 42001:2023 | 01-02 |
| OWASP Top 10 for LLM Applications 2025/2026 | 01-04 |
| EU AI Act 2024 | 01-02, 01-03, 01-05 |
| TOGAF 10 / ADM | 03-01, 03-02 |
| India DPDPA 2023 + DPDP Rules 2025 | 02-04 |
| IndiaAI Mission + MeitY AI Governance Guidelines 2025 | 02-04 |
| FinOps Foundation Framework | 01-01 |
| MITRE ATLAS | 01-04 |
| MLOps Maturity Model (Google/Microsoft/Zarour 2025) | 03-05 |
| ADKAR Change Management Framework | 02-06 |
| Transformer Architecture (Vaswani et al., 2017) | 00-01 |

---

## Key Case Studies in This Library

| Organisation | Case | Document |
|---|---|---|
| IBM Watson for Oncology | $4B write-off, synthetic data failure | 01-05 |
| Amazon | Hiring AI gender bias, shut down 2017 | 01-05, 01-03 |
| Air Canada | Chatbot legal liability, court-ordered compensation | 01-05 |
| DPD | Guardrail removal causing viral brand crisis | 01-05 |
| NYC MyCity | AI giving illegal regulatory advice | 01-05 |
| McDonald's/IBM | Drive-thru voice AI failure, partnership terminated | 01-05 |
| JPMorgan COIN + LLM Suite | 360,000 hours saved; 140,000-employee AI deployment | 02-02, 02-05 |
| HDFC Bank (India) | EVA chatbot, fraud detection, 30% fraud reduction | 02-05 |
| SBI YONO (India) | AI-driven digital lending, 20% rise | 02-05 |
| Klarna | AI = 700 FTE equivalent, $40M savings | 02-02 |
| Microsoft | Responsible AI Standard v2, Sensitive Use Review | 01-03 |
| DBS Bank | IT operations AI, MTTR reduction | 02-02 |
| DeepMind | Diabetic retinopathy AI (Aravind Eye, India) | 02-05 |
| Tata Steel (India) | Computer vision quality control on hot rolling mill | 02-05 |
| US Air Force | Predictive maintenance, 20–30% downtime reduction | 02-05 |
| Salesforce | 100,000+ architecture documents, AI EA agent | 03-02 |
| Arizona State University | 200 AI projects across 80% of academic units | 02-03 |

---

## Glossary of Key Terms

| Term | Definition |
|---|---|
| **Agentic AI** | AI systems that can reason, plan, use tools, and complete multi-step tasks with limited human input |
| **AI CoE** | AI Center of Excellence — cross-functional team that owns AI standards, platform, and governance |
| **AI FinOps** | Discipline of attributing, monitoring, and optimising AI (especially LLM) spend across teams and use cases |
| **Confabulation** | NIST term for LLM generating plausible but factually incorrect output (also: hallucination) |
| **Context Window** | Maximum tokens (input + output) an LLM can process in a single interaction |
| **DPDPA** | India's Digital Personal Data Protection Act 2023 (DPDP Rules notified November 2025) |
| **EA** | Enterprise Architecture — aligning business processes, IT, and strategy |
| **Few-Shot Prompting** | Providing input/output examples in the prompt to guide model behaviour |
| **Fine-Tuning** | Training a pre-trained foundation model further on domain-specific data |
| **LLMOps** | Operational practices for running LLMs in production: monitoring, routing, versioning, evaluation |
| **MeitY** | Ministry of Electronics and Information Technology, India — publisher of AI Governance Guidelines |
| **NIST AI RMF** | NIST AI Risk Management Framework: four functions — Govern, Map, Measure, Manage |
| **Prompt Injection** | Attacker-controlled input that manipulates LLM behaviour — OWASP LLM01 |
| **RAG** | Retrieval-Augmented Generation — LLM answers grounded in retrieved documents |
| **Red Teaming** | Adversarial testing of AI systems to find failure modes before attackers do |
| **SDF** | Significant Data Fiduciary (India DPDPA) — high-risk data processor with enhanced obligations |
| **Self-Attention** | The mechanism inside transformers that allows each token to relate to every other token |
| **Token** | ~3–4 characters of text; the unit of LLM input, output, cost, and context |
| **TOGAF ADM** | TOGAF's Architecture Development Method — phase-by-phase EA methodology |
| **Zero-Shot Prompting** | Giving the AI a task without examples, relying on its training knowledge |

---

*Library version: 1.0 | 33 documents | ~95,000 words | Research current as of September 2026 | Built for practitioners, not consultants.*
