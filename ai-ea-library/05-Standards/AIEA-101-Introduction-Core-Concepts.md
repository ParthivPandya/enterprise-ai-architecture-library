# AIEA® Standard
## Part 1: Introduction and Core Concepts
### Document Number: AIEA-101 | Version 1.0 | 2026

---

## Preface

This document is Part 1 of the AIEA Standard — AI Enterprise Architecture Standard. It provides the executive overview, foundational concepts, core definitions, and structural context necessary to understand and apply the complete AIEA Standard.

This document should be read by all practitioners using the AIEA Standard before engaging with any other Part of the documentation set.

---

# Chapter 1: Introduction

## 1.1 Executive Overview

Artificial Intelligence has moved from experimental technology to operational enterprise infrastructure. By 2026, AI systems are embedded in financial decisioning, clinical support, customer service, supply chain management, regulatory compliance, and the design of enterprise architecture itself. The scale and pace of this embedding has outpaced the governance frameworks needed to manage it.

Enterprise Architecture practice — the discipline of aligning technology with business strategy through structured methods, principles, and governance — is the natural home for AI governance at the enterprise level. Yet the dominant EA frameworks were designed before AI became a first-class architectural concern. They provide the structural foundation, but not the AI-specific extension.

The AIEA Standard is that extension.

**What the AIEA Standard provides:**
- A structured methodology for AI architecture development (the AI-ADM)
- A governance framework aligned with NIST AI RMF, EU AI Act, ISO/IEC 42001, and DPDPA
- A content framework of AI-specific deliverables, artifacts, and building blocks
- A capability model for establishing and maturing an enterprise AI architecture function
- Reference models for AI system types, integration patterns, and technical standards

**What the AIEA Standard does not provide:**
- Vendor recommendations or product endorsements
- Data science or machine learning engineering guidance
- A replacement for TOGAF (it extends TOGAF)
- A compliance certification programme (it provides the methodology; certification is separate)

## 1.2 Structure of This Document

This document is organised as follows:

- **Chapter 1:** Introduction — context, scope, intended audience
- **Chapter 2:** The AIEA Documentation Set — overview of all six Parts
- **Chapter 3:** Core Concepts — the foundational concepts of AI Enterprise Architecture
- **Chapter 4:** AI Architecture Principles — the enduring principles governing AI architecture decisions
- **Chapter 5:** The AIEA Architecture Repository — structure and content
- **Chapter 6:** Relationship to Existing Frameworks — TOGAF, NIST, ISO, EU AI Act
- **Appendix A:** Referenced Documents
- **Appendix B:** Abbreviations

## 1.3 Scope of the AIEA Standard

The AIEA Standard applies to:

- **All AI systems deployed within an enterprise** — whether built internally, acquired through procurement, or consumed as API services
- **All phases of the AI system lifecycle** — from strategy and design through deployment, operation, and retirement
- **All architectural domains** — Business, Data, Application, Technology, Security, and Governance as they relate to AI
- **All enterprise sizes and sectors** — the framework scales from small AI programmes to large-scale multi-system portfolios

The AIEA Standard applies regardless of the AI system type: rule-based systems, machine learning models, large language models, computer vision systems, agentic AI systems, or any combination thereof.

## 1.4 Conditions of Use

The AIEA Standard is published under an open framework licence for internal organisational use. Organisations may:
- Use the standard internally without cost or licence fee
- Adapt the methodology, templates, and checklists for internal use
- Reference the standard in internal documentation

Organisations may not:
- Publish derivative works commercially without a licence agreement
- Claim AIEA certification without completing the AIEA Certification Programme
- Use the AIEA® trademark on tools, training materials, or products without written approval

## 1.5 Integration with TOGAF

For organisations using TOGAF 10, the AIEA Standard integrates at the following points:

| TOGAF Element | AIEA Integration |
|---|---|
| Preliminary Phase | AI Readiness Assessment added |
| Phase A: Architecture Vision | AI Strategy Alignment extended |
| Phase B: Business Architecture | AI Capability Mapping added |
| Phase C: Information Systems | AI Data Architecture domain added |
| Phase D: Technology Architecture | AI Model and Inference Architecture added |
| Phases E–F: Solutions and Migration | AI Implementation Planning extended |
| Phase G: Implementation Governance | AI Deployment Governance extended |
| Phase H: Change Management | AI Model Lifecycle Management added |
| Architecture Repository | AI System Registry and AI Content extended |
| Architecture Governance | AI Governance Framework overlaid |

The AI-ADM (Part 2 of this standard) maps directly to the TOGAF ADM phases and extends them with AI-specific inputs, outputs, steps, and artifacts.

---

# Chapter 2: The AIEA Documentation Set

## 2.1 Structure of the Documentation Set

The AIEA Standard is a documentation set — a portfolio of documents that together constitute the complete standard. No single document is self-sufficient. The documents are closely linked and cross-referenced.

```
┌─────────────────────────────────────────────────────────────────┐
│              AIEA® STANDARD DOCUMENTATION SET                   │
├────────────────┬────────────────┬───────────────────────────────┤
│   PART 1       │   PART 2       │   PART 3                      │
│ Introduction & │   AI-ADM       │ Content Framework             │
│ Core Concepts  │ (Methodology)  │ (Deliverables/Artifacts/BBs)  │
├────────────────┼────────────────┼───────────────────────────────┤
│   PART 4       │   PART 5       │   PART 6                      │
│ Capability &   │ Reference      │ Definitions &                 │
│ Governance     │ Models         │ Glossary                      │
└────────────────┴────────────────┴───────────────────────────────┘
                         ↑
              Supplemented by AIEA Series Guides
          (Sector, Regulatory, and Practice guidance)
```

## 2.2 The AIEA Series Guides

The core standard is supplemented by a growing library of AIEA Series Guides providing practical guidance for specific contexts:

| Series Guide | Coverage |
|---|---|
| AIEA-G01: AI Architecture in Financial Services | BFSI-specific patterns, RBI/SEBI requirements |
| AIEA-G02: AI Architecture in Healthcare | Clinical AI, CDSCO/NHA requirements |
| AIEA-G03: AI Architecture for Indian Enterprises | DPDPA, IndiaAI Mission, MeitY Guidelines |
| AIEA-G04: Responsible AI in Practice | Fairness, bias, explainability — operational guidance |
| AIEA-G05: Agentic AI Architecture | Multi-agent system design and governance |
| AIEA-G06: Sovereign AI Architecture | On-premises and private cloud AI deployment |
| AIEA-G07: AI FinOps | Cost governance for enterprise AI programmes |
| AIEA-G08: LLMOps for Enterprise | Production operations for LLM-based systems |

---

# Chapter 3: Core Concepts

## 3.1 What is AI Enterprise Architecture?

AI Enterprise Architecture (AIEA) is the discipline of aligning an organisation's AI capabilities, investments, data assets, and governance structures with its business strategy and values — through a structured set of methods, principles, artifacts, and governance processes.

AIEA extends classical Enterprise Architecture in four dimensions:

**Dimension 1: The AI System Domain**
Classical EA addressed Business, Data, Application, and Technology domains. AIEA adds the AI System Domain — encompassing foundation models, training pipelines, inference infrastructure, agentic orchestration, and human-AI interfaces.

**Dimension 2: The Governance Imperative**
Classical EA governance concerned technology standards and project compliance. AIEA governance adds AI-specific obligations: risk classification, fairness evaluation, explainability requirements, regulatory compliance (EU AI Act, DPDPA), and responsible AI controls.

**Dimension 3: The Lifecycle Extension**
Classical systems have deterministic lifecycles: design, build, test, deploy, maintain, retire. AI systems add model-specific lifecycle elements: data acquisition, training, evaluation, fine-tuning, continuous monitoring, and model retirement — each with distinct architecture governance requirements.

**Dimension 4: The Accountability Chain**
Classical EA maps technology to business ownership. AIEA maps the complete AI accountability chain: from data source through training decisions, model behaviour, inference context, output validation, and consequential action — to the named human accountable for each.

## 3.2 What is an AI System?

For the purposes of this standard, an AI system is any system that:

- Uses machine learning, statistical inference, or large language model technology to process inputs and generate outputs or take actions
- Operates within an enterprise context — whether customer-facing, operational, or internal
- Has one or more consequential outputs — decisions, recommendations, content, or autonomous actions — that affect people, processes, or systems

This definition is intentionally broad. It includes:
- LLM-based chatbots and assistants
- ML models for prediction and classification
- Computer vision systems
- Agentic AI systems with tool-use capability
- Recommendation engines and personalisation systems
- AI-assisted decision support systems
- Automated process systems incorporating AI components

## 3.3 The Four Architectural Concerns of AI Systems

Every AI system, regardless of type, presents four architectural concerns that must be addressed:

**Concern 1: Capability** — What can the system do? What are its performance boundaries? What failure modes does it have?

**Concern 2: Governance** — Who is accountable for the system's outputs? How is compliance with applicable regulations ensured? How is the system tested for safety and fairness?

**Concern 3: Integration** — How does the system connect to enterprise data, processes, and other systems? How are its outputs consumed? What happens when it is unavailable?

**Concern 4: Economics** — What does the system cost to build, operate, and govern? What is the measurable business value it delivers? Is the investment sustainable?

The AI-ADM (Part 2) structures the architecture development process to address all four concerns at each phase.

## 3.4 The AI Architecture Development Method (AI-ADM)

The AI Architecture Development Method is the core of the AIEA Standard. It describes a systematic, iterative method for developing AI-enabled enterprise architectures.

The AI-ADM consists of twelve phases, organised in three cycles:

**Cycle 1: Foundation (Phases 0–A)**
Establishes the baseline, strategic context, and architecture vision before any AI system is designed.

**Cycle 2: Architecture Development (Phases B–F)**
Develops the complete architecture across Business, Data, Application, Technology, and Governance domains.

**Cycle 3: Implementation and Evolution (Phases G–I)**
Plans, governs, and evolves the AI architecture through deployment and beyond.

**Continuous Processes**
Two processes operate continuously across all phases: AI Requirements Management and AI Risk Management.

```
                    ┌─────────────────────────────┐
                    │    PRELIMINARY PHASE         │
                    │    AI Architecture Readiness │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │           CYCLE 1: FOUNDATION            │
              │  Phase 0: AI Strategy & Vision           │
              │  Phase A: AI Architecture Vision         │
              └────────────────────┬────────────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │      CYCLE 2: ARCHITECTURE DEVELOPMENT   │
              │  Phase B: AI Business Architecture       │
              │  Phase C: AI Data Architecture           │
              │  Phase D: AI Application Architecture    │
              │  Phase E: AI Technology Architecture     │
              │  Phase F: AI Governance Architecture     │
              └────────────────────┬────────────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │    CYCLE 3: IMPLEMENTATION & EVOLUTION   │
              │  Phase G: AI Solutions & Roadmap         │
              │  Phase H: AI Migration Planning          │
              │  Phase I: AI Implementation Governance   │
              │  Phase J: AI Architecture Change Mgmt    │
              └────────────────────┬────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  CONTINUOUS PROCESSES        │
                    │  Requirements Management     │
                    │  Risk Management             │
                    └─────────────────────────────┘
```

## 3.5 AI Enterprise Architecture Services

Activities described in the AI-ADM are provided through a service delivery model. The AIEA Standard defines six service categories:

### 3.5.1 AI Enterprise Support Services
Services that enable informed enterprise decisions about AI investments, risks, and governance. Delivered to C-level and senior leadership. Outputs: AI capability assessments, portfolio analysis, strategic recommendations.

### 3.5.2 AI Design Support Services
Services that enable informed design decisions for AI systems. Delivered to programme-level decision-makers. Outputs: AI architecture designs, compliance assessments, technology evaluations.

### 3.5.3 AI Development Support Services
Services that enable informed development decisions during AI system construction. Delivered to project teams. Outputs: AI architecture guidance, review gates, compliance certification.

### 3.5.4 AI Requirements Elicitation Services
Services that capture and structure AI-related business requirements, constraints, and value expectations. Delivered to product and business teams. Outputs: AI business requirements, use case catalogues, value frameworks.

### 3.5.5 AI Governance Services
Services that ensure AI systems comply with the enterprise AI governance framework and applicable regulations. Delivered to all stakeholders. Outputs: Risk assessments, compliance reports, audit evidence, incident responses.

### 3.5.6 AI Architecture Capability Development Services
Services that build and mature the enterprise AI architecture capability. Delivered to the AI architecture function. Outputs: Capability assessments, training programmes, process improvement plans.

## 3.6 Deliverables, Artifacts, and Building Blocks

The AIEA Content Framework (Part 3) defines three categories of architectural work product:

**AI Architecture Deliverable:** A formally reviewed and approved output of an AI architecture project or phase. Deliverables are contractually specified and archived in the AIEA Repository.

*Examples: AI Architecture Vision Document, AI System Card, AI Governance Framework, AI Data Architecture Definition*

**AI Architecture Artifact:** An architectural work product that describes a specific aspect of the AI architecture. Artifacts are classified as:
- Catalogs: lists of AI systems, risks, principles, or data assets
- Matrices: showing relationships between AI systems, business capabilities, or data flows
- Diagrams: visual representations of AI architectures, data flows, or governance structures

*Examples: AI System Inventory Catalog, AI Risk Register, AI Data Flow Diagram, AI Capability Map*

**AI Architecture Building Block (AI-ABB):** A reusable architectural component that can be combined with other building blocks to deliver AI architectures and solutions.

*Architecture Building Blocks (ABBs):* Describe required AI capability. Example: "Conversational AI Capability," "Predictive Analytics Capability."

*Solution Building Blocks (SBBs):* Specific implementations. Example: "GPT-4-based customer service agent on Azure OpenAI," "Scikit-learn fraud detection model on AWS SageMaker."

## 3.7 Architecture Abstraction for AI Systems

The AIEA Standard uses four abstraction levels, consistent with TOGAF:

### 3.7.1 Contextual Abstraction (Why)
Establishes the strategic context for AI investment. Answers: Why is this AI system needed? What business outcomes does it support? What is the compliance and risk context?

### 3.7.2 Conceptual Abstraction (What)
Defines what the AI system must do in terms of capabilities and behaviours, without specifying how. Answers: What data does the system consume? What decisions or outputs does it produce? What human oversight is required?

### 3.7.3 Logical Abstraction (How)
Defines how the AI architecture is structured — models, pipelines, integration patterns, and governance layers — independent of specific technologies. Answers: What model architecture is appropriate? How does data flow through the system? How is the system monitored?

### 3.7.4 Physical Abstraction (With What)
Maps the logical architecture to specific technologies, platforms, and vendors. Answers: Which foundation model provider? Which cloud region? Which vector database? Which observability stack?

## 3.8 AI Architecture Principles

Architecture Principles are general rules and guidelines, intended to be enduring, that govern AI architecture decisions. The AIEA Standard defines three categories of AI architecture principles:

**Category 1: AI Governance Principles**
Principles that govern accountability, transparency, and compliance across all AI systems.

**Category 2: AI Design Principles**
Principles that govern technical design decisions for AI systems.

**Category 3: AI Operations Principles**
Principles that govern how AI systems are operated, monitored, and evolved.

Full AI Architecture Principles are defined in Chapter 4 of this document.

## 3.9 AI Interoperability

Interoperability in AI Enterprise Architecture concerns three dimensions:

**Data Interoperability:** AI systems must consume data from and produce data to enterprise systems in standard formats with documented schemas, contracts, and lineage.

**Model Interoperability:** AI system designs SHOULD NOT be directly coupled to a single model provider's API syntax. An abstraction layer (AI Gateway) MUST be used in production deployments that enables model substitution without application redesign.

**Governance Interoperability:** The governance evidence produced by an AI system (audit logs, evaluation results, risk assessments) MUST be in formats that satisfy all applicable regulatory frameworks simultaneously, rather than producing separate compliance artefacts for each.

## 3.10 The AI Enterprise Continuum

Analogous to TOGAF's Enterprise Continuum, the AIEA Standard defines the AI Enterprise Continuum as a classification system for AI architectural solutions from the most generic to the most specific:

```
Foundation          Enterprise          Organisation         Deployed
AI Concepts    →    AI Patterns    →    AI Standards   →     AI Systems
(Generic)           (Industry)          (Enterprise)         (Specific)
```

- **Foundation AI Concepts:** Universal AI architecture concepts independent of any organisation or industry
- **Enterprise AI Patterns:** Industry-standard patterns adapted for enterprise contexts (RAG, agentic, fine-tuning)
- **Organisation AI Standards:** Enterprise-specific standards, principles, and approved patterns
- **Deployed AI Systems:** Specific AI systems deployed in the enterprise

## 3.11 The AIEA Architecture Repository

The AIEA Architecture Repository is the structured store of all AI architecture content produced during AI-ADM execution. It contains five sub-components:

| Repository Component | Contents |
|---|---|
| **AI Architecture Landscape** | Current, transition, and target AI system portfolio |
| **AI Reference Library** | Reusable AI architecture patterns, building blocks, and templates |
| **AI Standards Library** | Enterprise AI standards, approved vendors, and technology decisions |
| **AI Requirements Repository** | AI business requirements, constraints, and value frameworks |
| **AI Governance Repository** | Risk registers, compliance evidence, incident logs, audit records |

## 3.12 AI Content Framework and Enterprise Metamodel

The AIEA Content Framework (Part 3) provides the structural model for AI architectural content. The AI Enterprise Metamodel defines the relationships between the core architectural entities:

```
Business Capability
        │
        ▼
AI Use Case ────────→ AI System ────────→ Foundation Model
        │                   │                    │
        ▼                   ▼                    ▼
Business KPI        Data Sources          Model Provider
        │                   │
        ▼                   ▼
Value Measurement    Data Contract
```

## 3.13 Establishing an AI Architecture Capability

An AI Architecture Capability is the organisational ability to apply AIEA methods and standards consistently and repeatably. Establishing this capability requires:

1. **AI Architecture Function:** Named roles with defined responsibilities (CAIO, AI Architects, AI Governance Lead)
2. **AI Architecture Process:** Repeatable processes for AI-ADM execution, governance review, and repository management
3. **AI Architecture Content:** Templates, standards, and pattern libraries
4. **AI Architecture Tools:** Repository platform, governance tooling, and observability infrastructure
5. **AI Architecture Skills:** Competency framework and development programme

The AI Architecture Capability Maturity Model (Part 4) defines five maturity levels and the path between them.

## 3.14 Risk Management in AI Architecture

Risk management is not a phase of the AI-ADM — it is a continuous process that operates across all phases. The AIEA Standard defines AI risk across five categories:

| Risk Category | Definition | Primary Governance Response |
|---|---|---|
| **Technical Risk** | Model performance failure, hallucination, drift | Evaluation, monitoring, red teaming |
| **Data Risk** | Data quality, privacy breach, provenance failure | Data governance, data contracts |
| **Operational Risk** | Cost explosion, availability failure, dependency failure | FinOps, SLA, fallback architecture |
| **Compliance Risk** | Regulatory violation, licensing breach, audit failure | Governance framework, compliance gates |
| **Reputational Risk** | Harmful output, bias, public incident | Responsible AI programme, incident response |

---

# Chapter 4: AI Architecture Principles

## 4.1 Overview

AI Architecture Principles are enduring rules that inform all AI architecture decisions. They are not policies (which are specific and procedural) or standards (which are specific technical requirements). Principles are the values from which policies and standards derive.

Each principle in this chapter is specified with:
- **Name:** The principle's title
- **Statement:** A concise statement of the principle
- **Rationale:** Why this principle is important
- **Implications:** What the principle means in practice for architects and stakeholders

## 4.2 Governance Principles

### Principle G1: Human Accountability
**Statement:** Every AI system MUST have a named human accountable for its outputs, decisions, and compliance — from first deployment through retirement.

**Rationale:** AI systems make consequential decisions that affect people and organisations. Without named human accountability, incidents cannot be resolved, regulators cannot engage, and governance is ineffective. This principle operationalises the accountability requirement of NIST AI RMF GOVERN function, EU AI Act Article 16, and ISO/IEC 42001 Clause 5.1.

**Implications:** The AI System Registry MUST include a named System Owner for every AI system. The System Owner is accountable — not just responsible — for the system's performance, compliance, and incident response. Changes to System Ownership MUST be documented and approved.

### Principle G2: Governance by Risk, Not by Technology
**Statement:** AI governance requirements MUST be proportionate to the risk level of the AI system, not its technology type.

**Rationale:** A customer recommendation engine using an LLM and a clinical decision support system using an LLM present categorically different risks. Applying identical governance to both creates unnecessary friction for low-risk systems and insufficient protection for high-risk ones.

**Implications:** Every AI system MUST be classified against the Risk Classification Framework (Part 4) before development begins. Governance processes, review requirements, and monitoring intensity MUST be determined by risk classification, not technology type.

### Principle G3: Explainability Proportionate to Consequence
**Statement:** AI systems MUST be capable of explaining their outputs in proportion to the consequence of those outputs for affected individuals.

**Rationale:** Individuals affected by AI decisions have a right to understand the basis of those decisions. Regulators require explainability for high-risk applications. Organisations cannot audit or improve systems they cannot explain.

**Implications:** Before any AI system is deployed, the explainability method appropriate to its risk tier MUST be specified. Simple disclosure ("this is AI-generated") suffices for minimal-risk systems. Full feature-attribution explanation is required for systems making decisions that significantly affect individuals' livelihoods, rights, or health.

### Principle G4: Continuous Governance Over Point-in-Time Compliance
**Statement:** AI governance MUST be treated as an ongoing operational function, not a pre-deployment checklist.

**Rationale:** AI systems change after deployment — through model updates, data distribution shifts, new user behaviours, and evolving regulatory requirements. A compliance check at deployment time does not guarantee compliance six months later.

**Implications:** Every production AI system MUST have active monitoring with defined governance triggers. Governance review MUST be triggered by model updates, performance degradation, new regulatory requirements, and production incidents — not only by annual review cycles.

## 4.3 Design Principles

### Principle D1: Model Independence
**Statement:** AI applications MUST be designed with an abstraction layer that permits model substitution without application redesign.

**Rationale:** Foundation model capability, pricing, and availability change faster than enterprise application lifecycles. Applications coupled to a specific model version or provider API create technical debt and vendor lock-in that is expensive to resolve.

**Implications:** An AI Gateway (LiteLLM or equivalent) MUST be implemented as the single interface between enterprise applications and model providers. Application code MUST NOT directly reference provider SDK syntax. Model version pinning MUST be configurable without code changes.

### Principle D2: Grounded Generation Over Generative Hallucination
**Statement:** For AI systems providing factual information, answers MUST be grounded in verified sources through Retrieval-Augmented Generation or equivalent mechanisms.

**Rationale:** Foundation models generate plausible but potentially incorrect information. In enterprise contexts — legal, financial, medical, policy — incorrect information has material consequences. Grounding answers in verified sources dramatically reduces hallucination risk.

**Implications:** AI systems answering factual questions MUST implement RAG or tool-based retrieval from authoritative sources. System prompts MUST instruct models to cite sources and express uncertainty rather than generate unsupported answers. Output validation MUST check for source grounding in high-stakes applications.

### Principle D3: Minimum Sufficient Agency
**Statement:** Agentic AI systems MUST be granted the minimum permissions necessary to accomplish their defined task — no more.

**Rationale:** AI agents with broad permissions can cause widespread harm through single errors, jailbreaks, or unexpected behaviours. The principle of least privilege, applied to AI agents, contains the blast radius of any failure.

**Implications:** Every agentic AI system MUST have a documented permission set that is the minimum required for its function. Every tool or API the agent can call MUST be explicitly granted — not inherited from a broad permission role. Permissions MUST be reviewed at each production deployment and when agent scope changes.

### Principle D4: Reversibility Preference
**Statement:** AI system architecture SHOULD prefer reversible actions over irreversible ones, and MUST require elevated human approval for irreversible AI-initiated actions.

**Rationale:** AI systems make errors. Errors in reversible actions (draft documents, staged changes) can be corrected. Errors in irreversible actions (sent emails, executed transactions, deleted records) cannot. Design must reflect this asymmetry.

**Implications:** Every action an AI system can take MUST be classified as Reversible or Irreversible. Irreversible actions MUST require explicit human approval before execution. Agentic systems MUST prefer reversible alternatives when equivalent reversible options exist.

### Principle D5: Data Sovereignty First
**Statement:** AI system data architecture MUST be designed for the most restrictive applicable data sovereignty requirement from the first design decision.

**Rationale:** Retrofitting data residency, localisation, or sovereignty requirements onto an existing AI architecture is expensive and disruptive. The data sovereignty requirements of the most restrictive applicable jurisdiction MUST drive architecture decisions from inception.

**Implications:** Before any AI system design begins, the applicable data sovereignty requirements MUST be identified. For Indian enterprises: DPDPA SDF designation implications, MeitY AI Governance Guidelines, and India-region infrastructure availability. For EU-facing deployments: GDPR and EU AI Act data localisation. Architecture MUST be verified against these requirements at Phase C (Data Architecture).

## 4.4 Operations Principles

### Principle O1: Observability as a First-Class Requirement
**Statement:** Every production AI system MUST have monitoring instrumentation in place before the first user interaction — not added after.

**Rationale:** AI systems fail in ways that are not visible through standard application monitoring. Quality degradation, hallucination rate increases, cost anomalies, and security incidents require AI-specific instrumentation. Systems deployed without monitoring operate in the dark.

**Implications:** The AI system monitoring plan (covering accuracy, latency, cost, fairness, and security metrics) MUST be completed and approved as part of the production launch gate. Monitoring dashboards MUST be live before production traffic begins. Anomaly alerts MUST be configured and tested before launch.

### Principle O2: AI FinOps as Infrastructure
**Statement:** AI cost attribution and governance MUST be implemented as shared infrastructure before AI systems are deployed — not as an afterthought.

**Rationale:** AI costs scale with usage in ways that are not visible without attribution infrastructure. Without per-team, per-feature cost attribution, waste accumulates invisibly and FinOps governance is impossible.

**Implications:** An AI Gateway with cost attribution capability MUST be operational before any AI system is deployed to production. Every API call MUST be attributed to a team, product, and feature. Budget alerts and hard caps MUST be configured per team before production launch.

### Principle O3: Every AI System Has an End Date
**Statement:** At the time of deployment, every AI system MUST have a defined review cadence and documented triggers that MUST initiate retirement consideration.

**Rationale:** AI systems accumulate technical debt, regulatory exposure, and performance degradation over time. Without defined retirement triggers, obsolete systems persist indefinitely, consuming resources and creating governance risk.

**Implications:** The AI System Card MUST include a review cadence (quarterly for High Risk, annual for Limited Risk) and retirement triggers (technology superseded, regulatory change, performance below threshold, business case no longer valid). Retirement triggers MUST be monitored actively, not passively.

---

# Chapter 5: The AIEA Architecture Repository

## 5.1 Purpose

The AIEA Architecture Repository is the structured, governed store of all AI architecture content produced by the enterprise. It serves as the single source of truth for AI system inventory, risk status, governance evidence, and architecture decisions.

The repository is not a documentation archive — it is a living system that is continuously updated as AI systems are created, changed, and retired.

## 5.2 Repository Structure

### 5.2.1 AI Architecture Landscape

Contains the current, transition, and target views of the enterprise AI portfolio:

**Current State:** All AI systems currently in production, with their classification, governance status, cost, and performance data.

**Transition State:** AI systems in development or migration, with their planned deployment date and governance completion status.

**Target State:** The approved future AI architecture — what the enterprise AI portfolio should look like in 12–36 months, and why.

### 5.2.2 AI Reference Library

Reusable AI architecture assets:
- AI Architecture Building Blocks (AI-ABBs) — validated, reusable capability definitions
- AI Solution Building Blocks (AI-SBBs) — approved implementation components
- AI Architecture Patterns — reference architectures for common AI system types (RAG, Agentic, Document Intelligence, Customer Service AI)
- AI Design Templates — standard templates for AI System Cards, Data Contracts, Governance Reviews

### 5.2.3 AI Standards Library

Enterprise AI technical standards:
- Approved AI vendors and model providers
- Approved AI frameworks and tools
- AI Security Standards (derived from OWASP LLM Top 10)
- AI Data Standards (data contracts, quality thresholds, lineage requirements)
- AI Interface Standards (API schemas, output formats, citation requirements)

### 5.2.4 AI Requirements Repository

Structured repository of AI-related business requirements:
- Business capability requirements
- Use case definitions with KPIs and baselines
- Regulatory and compliance requirements
- Stakeholder constraints and non-functional requirements

### 5.2.5 AI Governance Repository

The compliance and governance evidence store:
- AI System Risk Assessments
- Pre-Deployment Review Records
- Compliance Gate Evidence Packages
- Red Team Test Records and Findings
- Production Incident Log
- Regulatory Change Tracker

## 5.3 Repository Governance

The AIEA Repository MUST be governed by the following policies:

- **Currency:** Every AI system in production MUST have an up-to-date entry in the Repository, reviewed within the last review cycle period
- **Completeness:** All mandatory fields for each AI system MUST be populated; incomplete records trigger a governance alert
- **Accuracy:** Repository data MUST be validated against production reality at each quarterly governance review
- **Access:** The AI System Inventory MUST be accessible to all named AI System Owners; the Governance Repository requires controlled access
- **Audit:** All changes to the Repository MUST be timestamped, attributed to a named individual, and retained for seven years

---

# Chapter 6: Relationship to Existing Frameworks

## 6.1 Relationship to NIST AI RMF

The NIST AI Risk Management Framework (Govern, Map, Measure, Manage) is the most widely adopted AI risk management methodology in the US and globally. The AIEA Standard implements the NIST AI RMF as the operational methodology within Phase F (AI Governance Architecture) and the continuous Risk Management process.

| NIST AI RMF Function | AIEA Implementation |
|---|---|
| GOVERN | AI Architecture Principles (Chapter 4) + Governance Repository |
| MAP | AI System Risk Classification (Part 4) + AI System Inventory |
| MEASURE | Pre-Deployment Evaluation Gate + Production Monitoring |
| MANAGE | AI Incident Response + Risk Treatment Records |

## 6.2 Relationship to EU AI Act

The EU AI Act (2024) is binding law for organisations deploying AI in EU markets. The AIEA Standard integrates EU AI Act obligations at Phase F and the Governance Framework:

| EU AI Act Requirement | AIEA Implementation |
|---|---|
| Risk classification | AI System Risk Classification (Part 4, Chapter 2) |
| Conformity assessment (High Risk) | Pre-Deployment Review Gate (Part 4, Chapter 3) |
| Technical documentation | AI System Card (Part 3, Section 3.2) |
| Human oversight | Principle D4 + Human Oversight Design Pattern |
| Transparency | Principle G3 + Output Disclosure Standards |
| Post-market monitoring | Production Monitoring Framework (Part 4, Chapter 4) |

## 6.3 Relationship to ISO/IEC 42001:2023

ISO/IEC 42001 is the certifiable AI Management System standard. The AIEA Standard's Governance Framework (Part 4) satisfies the following ISO 42001 clauses:

| ISO/IEC 42001 Clause | AIEA Implementation |
|---|---|
| 5.1 Leadership and commitment | AI Architecture Principles + CAIO role definition |
| 6.1 Risk assessment | AI Risk Classification Framework |
| 7.5 Documented information | AIEA Repository governance |
| 9.1 Monitoring, measurement | Production Monitoring Framework |
| 9.2 Internal audit | AI Governance Review cycle |
| 10.1 Continual improvement | AI Architecture Change Management (Phase J) |

## 6.4 Relationship to India DPDPA

For Indian enterprises, the AIEA Standard includes DPDPA-specific guidance:
- Data Architecture (Phase C) includes DPDPA lawful basis assessment
- Governance Framework includes DPDPA compliance track
- AI System Card includes PII processing disclosure
- Retirement Runbook includes DPDPA data erasure obligations

---

# Appendix A: Referenced Documents

| Standard | Title | Relevance |
|---|---|---|
| TOGAF 10 | The Open Group Architecture Framework 10th Edition | EA methodology foundation |
| NIST AI RMF 1.0 | AI Risk Management Framework | Risk governance methodology |
| NIST AI 600-1 | Generative AI Profile | GenAI-specific risk categories |
| ISO/IEC 42001:2023 | AI Management Systems | Certifiable governance standard |
| EU AI Act 2024 | Regulation on Artificial Intelligence | Binding EU regulatory framework |
| OWASP LLM Top 10 2025/2026 | LLM Application Security Risks | Security standard for AI |
| DPDPA 2023 | Digital Personal Data Protection Act (India) | Indian data protection law |
| MeitY AI Guidelines 2025 | India AI Governance Guidelines | Indian AI governance standard |
| ISO/IEC 25010 | Systems and Software Quality | Quality model for AI systems |
| ArchiMate 3.2 | ArchiMate Modelling Language | Notation for AIEA diagrams |
| IEEE 7000-2021 | Model Process for Addressing Ethical Concerns | Ethical AI design standard |

# Appendix B: Abbreviations

| Abbreviation | Expansion |
|---|---|
| AIEA | AI Enterprise Architecture |
| AI-ADM | AI Architecture Development Method |
| AI-ABB | AI Architecture Building Block |
| AI-SBB | AI Solution Building Block |
| CAIO | Chief AI Officer |
| DPDPA | Digital Personal Data Protection Act (India) |
| EU AI Act | European Union Artificial Intelligence Act |
| GPAI | General Purpose Artificial Intelligence |
| LLM | Large Language Model |
| LLMOps | LLM Operations |
| NIST AI RMF | NIST Artificial Intelligence Risk Management Framework |
| RAG | Retrieval-Augmented Generation |
| SDF | Significant Data Fiduciary (DPDPA) |

---

*AIEA Standard Part 1: Introduction and Core Concepts. Document AIEA-101, Version 1.0, 2026.*
*Next: Part 2 — AI Architecture Development Method (AIEA-201)*
