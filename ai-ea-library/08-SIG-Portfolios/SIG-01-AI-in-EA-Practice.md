# SIG-01 Portfolio: AI in Enterprise Architecture Practice
## Methods, Tooling, and Competencies for Modern Enterprise Architects
### Special Interest Group Dedicated Portfolio Document | Document Ref: AIEA-SIG-01
#### Version 1.0 | 2026

---

## 1. SIG Charter & Mission

The **AI in EA Practice Special Interest Group (SIG-01)** is dedicated to the systematic evolution of the Enterprise Architecture discipline itself. As artificial intelligence transforms organizational operating models, architects cannot remain passive observers or bureaucratic reviewers. 

### Mission Statement
> *"To empower enterprise, domain, and solution architects with AI-augmented methods, intelligent toolchains, and modern competencies—transforming the architecture practice from static document custodians into active, continuous orchestrators of the intelligent enterprise."*

### Domain Scope
- **Methods**: AI-Augmented Architecture Development Method (AI-ADM), Architecture as Code (AaC), empirical model benchmarking, and continuous architecture governance.
- **Tools**: LLM-assisted modeling workbenches (Mermaid, PlantUML), vector knowledge graphs, LLMOps observability stacks (Arize Phoenix, Langfuse), and automated architecture linters.
- **Skills**: Prompt engineering for architects, statistical evaluation literacy, runtime guardrail design, and unit economic FinOps modeling.

---

## 2. Practical Implementation Scenarios

To demonstrate how SIG-01 assets are operationalized in complex organizations, consider these practical enterprise scenarios:

### Scenario 1.1: Automated Microservice Architecture Topology Mining
- **Enterprise Context**: A Tier-1 retail conglomerate managing 3,500 backend microservices with severe architectural drift and undocumented API dependencies.
- **Practical Application**:
  - The EA team leveraged **[WP-01: Modernizing EA with AI](WP-01-Modernizing-EA-with-AI.md)** and **[Enterprise AI Metamodel Catalog](../07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md)**.
  - Deployed an AI ingestion agent to scan OpenAPI YAML specs, Terraform states, and Git repositories, auto-populating a living Neo4j architecture graph.
  - Integrated **[AIEA-TK-09: Architecture Review Checklist](../07-Toolkits-and-Playbooks/09-AI-Architecture-Review-Checklist.md)** to identify and flag 24 un-governed data egress points routing sensitive PII to external models.
- **Outcome**: Reduced architecture dependency discovery time from 16 weeks of manual interviews to 48 hours of automated semantic synthesis.

### Scenario 1.2: Accelerating TOGAF ADM Cycles for an Insurance Core Migration
- **Enterprise Context**: A commercial property & casualty insurer initiating an 18-month core policy administration migration.
- **Practical Application**:
  - Conducted **[Workshop 2: Prompt Engineering & RAG Architecture for Architects](../03-EA-Practice/04-Hands-on-Workshops.md)** to upskill 35 domain architects.
  - Applied the AI-ADM phase accelerations codified in **[AIEA-TK-06: EA Practice Evolution Playbook](../07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md)**.
  - Used AI agents to ingest 2,000 legacy policy rule documents, automatically synthesizing target-state capability maps and transition architecture roadmaps.
- **Outcome**: Compressed Phase B (Business Architecture) and Phase C (Information Systems Architecture) delivery from 6 months to 7 weeks.

---

## 3. Dedicated Portfolio of the 8 Core Asset Types

SIG-01 explicitly provides and maintains production-grade assets across all 8 required categories:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIG-01 CORE ASSET REPOSITORY MAPPING                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. WHITE PAPER  ──► [WP-01: Modernizing EA with AI]                         │
│ 2. PLAYBOOK     ──► [AIEA-TK-06: EA Practice Evolution Playbook]            │
│ 3. REF MODEL    ──► [AIEA-501: AI Technical Reference Model (AI-TRM)]       │
│ 4. CASE STUDY   ──► [AIEA-G05: Agentic AI Architecture Real-World Cases]    │
│ 5. ASSESSMENT   ──► [EA Practice AI Maturity & Competency Framework]        │
│ 6. CHECKLIST    ──► [AIEA-TK-09: AI Architecture Review Checklist]          │
│ 7. WORKSHOP     ──► [Workshop 2: Prompt Engineering & RAG for Architects]   │
│ 8. SLIDE DECK   ──► [AIEA-TK-11: Modernizing EA Technical Slide Deck]       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Asset 1: White Paper
- **Primary Document**: **[WP-01: Modernizing Enterprise Architecture with Artificial Intelligence](WP-01-Modernizing-EA-with-AI.md)**
- **Executive Summary**: Comprehensive technical position paper establishing the necessity of shifting from manual, point-in-time architecture gatekeeping to AI-augmented continuous architecture. Codifies the crisis of velocity, the AI-augmented ADM, and the new architecture workbench.

### Asset 2: Playbooks
- **Primary Playbook**: **[AIEA-TK-06: EA Practice Evolution Playbook](../07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md)**  
  *Covers the 4 modern AI architect personas, architecture-as-code workbenches, team operating rhythms, and daily operating procedures.*
- **Supporting Playbook**: **[Strategic Architecture Runbooks](../03-EA-Practice/03-Strategic-Runbooks.md)**  
  *Step-by-step procedural runbooks for model deprecation, provider failover, and architecture regression testing.*

### Asset 3: Reference Model & Pattern Library
- **Primary Reference Model**: **[AIEA-501: Reference Models (AI-TRM)](../05-Standards/AIEA-501-Reference-Models.md)**  
  *Normative AI Technical Reference Model defining the 5 architectural layers: Infrastructure, Model, Retrieval/RAG, Agent Orchestration, and Governance.*
- **Supporting Catalogs**: 
  - **[AI Reference Architectures](../03-EA-Practice/08-AI-Reference-Architectures.md)** (Multi-Agent Swarm, Hybrid Sovereign Cloud, Enterprise RAG).
  - **[Enterprise AI Metamodel Catalog (AIEA-TK-02)](../07-Toolkits-and-Playbooks/02-Enterprise-AI-Metamodel-Catalog.md)** (ArchiMate 3.2 mapping specifications and JSON schemas).

### Asset 4: Case Studies
- **Primary Case Study**: **[AIEA-G05: Agentic AI Architecture in Practice](../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)**  
  *Detailed architectural analysis of multi-agent autonomous deployments, stateful memory persistence, and tool-use boundaries in production.*
- **Supporting Case Study**: **[AIEA-G08: Enterprise LLMOps at Scale](../06-Series%20Guide/AIEA-G08-LLMOps-Enterprise.md)**  
  *Case study of a global SaaS provider scaling inference pipelines to 50 million daily tokens with automated prompt regression testing.*

### Asset 5: Maturity & Readiness Assessment
- **Primary Assessment**: **[EA Practice AI Maturity Assessment & CoE Framework](../03-EA-Practice/07-AI-Center-of-Excellence.md)**  
  *Evaluates the architecture team across 5 maturity levels: from Level 1 (Ad-Hoc / Disconnected) to Level 5 (Continuous Intelligent Architecture).*
- **Supporting Diagnostic**: **[Architect Competency Evaluation Matrix (AIEA-TK-06)](../07-Toolkits-and-Playbooks/06-EA-Practice-Evolution-Playbook.md)**  
  *Individual skills rubric assessing architects across prompt engineering, statistical evaluation, FinOps, and guardrail design.*

### Asset 6: Checklists
- **Primary Checklist**: **[AIEA-TK-09: AI Architecture Review Checklist](../07-Toolkits-and-Playbooks/09-AI-Architecture-Review-Checklist.md)**  
  *Standardized Gate 0 through Gate 4 review instrument covering Strategy, Data/PII, Model Architecture, Guardrails/Safety, and Production LLMOps.*
- **Supporting Checklist**: **[AI Model Testing & Evaluation Checklist](../03-EA-Practice/09-AI-Testing-and-Evaluation.md)**  
  *Operational testing checklist for measuring Ragas faithfulness, hallucination thresholds, and prompt injection resilience.*

### Asset 7: Workshop
- **Primary Workshop**: **[Workshop 2: Prompt Engineering & RAG Architecture for Architects](../03-EA-Practice/04-Hands-on-Workshops.md)**  
  *Full 1-day practical syllabus: System prompt design, vector database indexing, chunking trade-offs, and building text-to-architecture agents.*
- **Supporting Workshop**: **[Workshop 4: AI Center of Excellence Setup & Practice Evolution](../03-EA-Practice/04-Hands-on-Workshops.md)**  
  *Executive workshop defining CoE team topologies, federated governance models, and practice evolution roadmaps.*

### Asset 8: Slide Deck
- **Primary Slide Deck**: **[AIEA-TK-11: Modernizing EA with AI Technical Presentation Deck](../07-Toolkits-and-Playbooks/11-AI-in-EA-Practice-Slide-Deck.md)**  
  *Complete 8-slide presentation deck formatted in Markdown with visual layout cues, data callouts, and detailed presenter notes for Architecture Boards.*

---

## 4. Domain Completeness Audit: Methods, Tools, and Skills

To ensure that SIG-01 provides comprehensive coverage without operational gaps, we review the three core domain pillars:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SIG-01 DOMAIN COMPLETENESS AUDIT                      │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ DOMAIN PILLAR     │ SPECIFIC CAPABILITIES & ASSETS INCLUDED                │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 1. METHODS        │ • AI-Augmented ADM (Preliminary through Phase H)        │
│                   │ • Architecture as Code (Markdown / Git / YAML schemas)  │
│                   │ • Continuous Automated ADR Generation                   │
│                   │ • Empirical Evaluation Metrics (Ragas, Faithfulness)    │
│                   │ • Verified via: WP-01, TK-06, AIEA-201, TK-03          │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 2. TOOLS          │ • AI Observability Platforms (Arize Phoenix, Langfuse) │
│                   │ • Text-to-Diagramming LLMs (Mermaid.js, PlantUML)       │
│                   │ • Enterprise Metamodel Schema & Knowledge Graphs        │
│                   │ • Gate 0-4 Review Checklist (AIEA-TK-09)                │
│                   │ • Verified via: 03-EA-Practice/10, TK-02, TK-09         │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 3. SKILLS         │ • The 4 Architect Personas (Lead, Modeler, Evaluator)   │
│                   │ • Prompt Engineering for Architecture Artifacts         │
│                   │ • AI FinOps & Token Economics Calculation               │
│                   │ • Hands-on Workshop Curriculum (Modules 1-4)            │
│                   │ • Verified via: TK-06, 03-EA-Practice/04, 03-07         │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 5. Getting Started & Practice Evolution Next Steps

1. **Assess Current Maturity**: Execute the **[EA Practice AI Maturity Assessment](../03-EA-Practice/07-AI-Center-of-Excellence.md)**.
2. **Standardize Reviews**: Adopt **[AIEA-TK-09: AI Architecture Review Checklist](../07-Toolkits-and-Playbooks/09-AI-Architecture-Review-Checklist.md)** for all upcoming solution gate reviews.
3. **Conduct Upskilling**: Schedule **[Hands-on Workshop 2](../03-EA-Practice/04-Hands-on-Workshops.md)** for your architecture team.
4. **Present the Technical Strategy**: Present **[AIEA-TK-11: Slide Deck](../07-Toolkits-and-Playbooks/11-AI-in-EA-Practice-Slide-Deck.md)** to the Architecture Review Board.

---
*AIEA® Special Interest Group Portfolios. Published under Open Framework Licence for organizational adoption.*
