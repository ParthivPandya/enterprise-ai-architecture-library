# AIEA Reference Framework
## Part 3: AI Architecture Content Framework
### Document Number: AIEA-301 | Version 1.0 | 2026

---

## Preface

This document defines the AI Architecture Content Framework — the structural model for all AI architectural work products. It specifies every deliverable, artifact, and building block that AI architecture work may produce, along with the templates and standards for their creation.

The Content Framework answers the question: *What do we produce when we do AI architecture work, and what does each product look like?*

---

## Chapter 1: Overview of the Content Framework

### 1.1 Content Categories

The AIEA Content Framework uses three categories of architectural work product:

**AI Architecture Deliverable:** A formally reviewed, approved, and signed-off work product. Deliverables are contractually specified — they represent the commitments of the architecture function to its stakeholders. Every deliverable is archived in the AIEA Repository.

**AI Architecture Artifact:** An architectural work product that describes a specific aspect of the AI architecture. Artifacts are classified as catalogs (lists), matrices (relationships), and diagrams (pictures). Artifacts are the substance of deliverables.

**AI Architecture Building Block (AI-ABB):** A reusable component that can be combined with other building blocks to deliver AI architectures. Building blocks exist at two levels:
- *Architecture Building Blocks (ABBs):* Required capabilities — what must be done
- *Solution Building Blocks (SBBs):* Implementation components — how it will be done

### 1.2 Content Lifecycle

AI architecture content has a defined lifecycle:

```
Create → Review → Approve → Publish → Use → Update → Archive
           ↑_________________________________|
                  (iterative updates)
```

All content in the AIEA Repository is versioned. Major version changes require Architecture Board review. Minor version changes require System Owner approval.

---

## Chapter 2: AI Architecture Deliverables

### 2.1 Deliverable: AI Architecture Vision Document

**AI-ADM Phase:** Phase A  
**Owner:** Lead AI Architect  
**Approver:** AI Architecture Board  
**Format:** Structured document  

**Purpose:** Establishes the high-level direction for an AI use case — business case, risk classification, technology approach, and architectural intent — before detailed design work begins.

**Mandatory Sections:**

1. Executive Summary (max 1 page)
2. Business Case (problem, value, KPIs, financials)
3. AI System Risk Classification (with justification)
4. Technology Approach Decision Record (Build/Buy/Fine-Tune)
5. Architecture Vision Statement (what the system will and will not do)
6. Stakeholder Map and Concerns Register
7. Scope Statement and Assumptions
8. Key Risks and Preliminary Mitigations
9. Next Steps and Approval Request

**Quality Criteria:**
- Business case includes quantified baseline KPI and target
- Risk classification uses the AIEA Risk Classification Framework
- Technology approach decision is documented with evaluated alternatives
- Scope statement explicitly lists what is out of scope
- Named business sponsor has reviewed and signed

---

### 2.2 Deliverable: AI System Card

**AI-ADM Phase:** Phase F (draft), Phase I (final)  
**Owner:** AI System Owner  
**Approver:** AI Governance Lead  
**Format:** Structured document  
**Review Cadence:** On each major system change; at least annually

**Purpose:** The AI System Card is the single authoritative documentation of an AI system — what it does, how it performs, what its limitations are, and who is accountable. It is the primary artifact in the AIEA Governance Repository and the primary evidence document for regulatory compliance.

**AI System Card Template:**

```
═══════════════════════════════════════════════════════
AI SYSTEM CARD — [System Name]
AIEA Repository Reference: [Unique ID]
Version: [X.Y] | Last Updated: [Date] | Status: [Active]
═══════════════════════════════════════════════════════

SECTION 1: SYSTEM IDENTITY
  System Name:
  Version:
  System Owner (Accountable):
  Technical Owner (Responsible):
  Business Unit:
  Deployment Date:
  Last Review Date:
  Next Scheduled Review:

SECTION 2: PURPOSE AND SCOPE
  Intended Use:           [What the system does, for whom]
  Out of Scope:           [What the system explicitly does not do]
  User Population:        [Who uses this system]
  Deployment Context:     [Where and how the system operates]

SECTION 3: RISK CLASSIFICATION
  AIEA Risk Tier:         [Prohibited / High / Significant / Limited / Minimal]
  EU AI Act Classification: [If applicable]
  Justification:          [Why this classification]
  Classification Date:    [Date]
  Classification Reviewer: [Name]

SECTION 4: AI SYSTEM DESCRIPTION
  Foundation Model(s):   [Model name, version, provider]
  Architecture Pattern:  [RAG / Agentic / Fine-tuned / Other]
  Data Sources:          [List with provenance]
  Key Capabilities:      [What the system can do well]
  Known Limitations:     [What the system does not do well]
  Failure Modes:         [How the system fails and how often]

SECTION 5: PERFORMANCE BENCHMARKS
  Primary KPI:           [Metric, current value, target]
  Accuracy Benchmark:    [Result on golden test set — date]
  Latency (p50):         [ms]
  Latency (p95):         [ms]
  Cost Per Request:      [₹/$ estimate]
  Last Benchmark Date:

SECTION 6: FAIRNESS AND RESPONSIBLE AI
  Demographic Groups Tested:
  Fairness Metrics Used:
  Fairness Evaluation Results:
  Bias Mitigations Applied:
  Explainability Method:
  Transparency Disclosure: [How users know they are interacting with AI]

SECTION 7: GOVERNANCE AND COMPLIANCE
  NIST AI RMF Assessment Date:
  NIST AI 600-1 Applied (GenAI): [Yes/No]
  EU AI Act Compliance Status: [If applicable]
  DPDPA Compliance Status: [If applicable]
  Last Red Team Exercise Date:
  Open Security Findings:
  Last Governance Review Date:
  Regulatory Filing Status:

SECTION 8: DATA AND PRIVACY
  Personal Data Processed: [Yes/No — if yes, categories]
  Lawful Basis (DPDPA):
  DPIA Completed: [Yes/No/Not Required — date]
  Data Retention Period:
  Data Erasure Mechanism:
  International Data Transfers: [Yes/No — if yes, safeguards]

SECTION 9: OPERATIONS
  Infrastructure:          [Cloud provider, region, services]
  Monitoring Dashboard:    [Link]
  Incident Contact:        [Email/channel]
  Escalation Path:         [Process]
  Rollback Procedure:      [Link to runbook]
  SLA:                     [Uptime, latency commitments]
  Last Incident Date:      [Date and severity]

SECTION 10: HISTORY AND CHANGE LOG
  Version | Date | Author | Changes | Approved By

═══════════════════════════════════════════════════════
```

---

### 2.3 Deliverable: AI Data Architecture Definition

**AI-ADM Phase:** Phase C  
**Owner:** Data Architect  
**Approver:** AI Architecture Board  

**Mandatory Sections:**
1. Data Source Catalog (with quality assessment results)
2. Data Flow Diagram (from source to model input)
3. Data Contract Set (one per data source)
4. Privacy and Compliance Assessment (DPDPA/GDPR)
5. Data Governance Plan (stewardship, access, retention)
6. Data Quality Baseline (pre-deployment measurements)

---

### 2.4 Deliverable: AI Governance Framework

**AI-ADM Phase:** Preliminary Phase / Phase F  
**Owner:** AI Governance Lead  
**Approver:** CAIO / Governance Board  

**Mandatory Sections:**
1. AI Governance Operating Model (roles, responsibilities, decision rights)
2. AI Risk Classification Framework
3. AI Policy Set (permitted uses, restricted uses, prohibited uses)
4. Pre-Deployment Review Process
5. Production Monitoring Standards
6. Incident Response Framework
7. Regulatory Compliance Mapping (NIST AI RMF, EU AI Act, DPDPA, ISO 42001)
8. AI System Registry Governance
9. Maturity Improvement Plan

---

### 2.5 Deliverable: AI Architecture Definition Document

**AI-ADM Phase:** Phases B–F (consolidated)  
**Owner:** Lead AI Architect  
**Approver:** AI Architecture Board  

The Architecture Definition Document is the complete architecture specification for an AI system — consolidating the outputs of Phases B through F into a single reviewed and approved document.

**Mandatory Sections:**
1. Architecture Overview (system context and purpose)
2. Business Architecture (capability map, target operating model, KPIs)
3. Data Architecture (data sources, lineage, contracts)
4. Application Architecture (models, pipelines, prompts, integration)
5. Technology Architecture (infrastructure, LLMOps, CI/CD)
6. Governance Architecture (controls, compliance, monitoring)
7. Architecture Decisions Record (all significant architectural decisions)
8. Gap Analysis (current state vs. target)
9. Implementation Roadmap (from Phase G)

---

## Chapter 3: AI Architecture Artifacts

### 3.1 Catalogs

#### 3.1.1 AI System Inventory Catalog

The master catalog of all AI systems in the enterprise. Minimum fields:

| Field | Description |
|---|---|
| System ID | Unique identifier |
| System Name | Human-readable name |
| System Owner | Accountable executive |
| Technical Owner | Responsible engineer |
| Business Unit | Owning business unit |
| Risk Tier | AIEA risk classification |
| Status | Development / Production / Retired |
| Foundation Model | Primary model(s) used |
| Deployment Date | When system went live |
| Last Review Date | Most recent governance review |
| Next Review Date | Scheduled next review |
| Monitoring Link | Production monitoring dashboard |
| System Card | Link to current System Card |
| Annual Cost | Estimated annual run cost |
| Annual Value | Documented annual business value |

#### 3.1.2 AI Risk Register

For each AI system, a risk register documenting:

| Field | Description |
|---|---|
| Risk ID | Unique identifier |
| System | AI system reference |
| Risk Category | Technical / Data / Operational / Compliance / Reputational |
| NIST AI 600-1 Category | Applicable GenAI risk category (if applicable) |
| Risk Description | What could go wrong |
| Likelihood | High / Medium / Low |
| Impact | High / Medium / Low |
| Risk Score | Likelihood × Impact |
| Treatment Decision | Accept / Mitigate / Transfer / Avoid |
| Treatment Action | Specific control or action |
| Residual Risk | Risk level after treatment |
| Owner | Named individual responsible |
| Review Date | When this risk entry was last reviewed |

#### 3.1.3 AI Data Asset Catalog

All data assets used in AI systems:

| Field | Description |
|---|---|
| Data Asset ID | Unique identifier |
| Data Asset Name | Human-readable name |
| Source System | Where the data originates |
| Data Steward | Named data owner |
| PII Indicator | Does this asset contain personal data? |
| DPDPA Lawful Basis | If personal data: lawful basis |
| Quality Assessment | Completeness, accuracy, freshness scores |
| AI Systems Using | Which AI systems consume this asset |
| Data Contract | Link to data contract |
| Retention Period | How long data is retained |
| Last Quality Check | Date of most recent quality validation |

#### 3.1.4 AI Architecture Principles Catalog

All AI Architecture Principles in effect, with:
- Principle Name
- Statement
- Rationale
- Implications
- Exceptions (documented deviations with approval)
- Owner
- Last Reviewed

#### 3.1.5 AI Vendor and Technology Catalog

Approved AI vendors and technology components:

| Field | Description |
|---|---|
| Vendor / Component | Name |
| Category | Foundation Model / AI Platform / Vector DB / LLMOps / etc. |
| Approval Status | Approved / Conditional / Restricted / Not Approved |
| Approved Use Cases | What this vendor may be used for |
| Restrictions | What this vendor may NOT be used for |
| Data Residency | Supported regions |
| Compliance Certifications | SOC2, ISO27001, etc. |
| Last Assessment Date | When this vendor was last assessed |
| Next Review Date | Scheduled review |
| DPA Status | Data Processing Agreement executed? |

---

### 3.2 Matrices

#### 3.2.1 AI-Business Capability Matrix

Maps AI systems to the business capabilities they support:

```
                    AI System A  AI System B  AI System C
Business Cap 1         ●              ○              ○
Business Cap 2         ●              ●              ○
Business Cap 3         ○              ●              ●
Business Cap 4         ○              ○              ●

● Directly supports    ○ No relationship
```

#### 3.2.2 AI-Data Flow Matrix

Maps AI systems to the data sources they consume and produce:

```
                    AI System A  AI System B  AI System C
CRM Data               IN             IN             ○
ERP Data               ○              IN             IN
Customer Docs          IN             ○              IN
Audit Logs             OUT            OUT            OUT

IN = Consumes  OUT = Produces  ○ = No relationship
```

#### 3.2.3 AI-Risk Matrix

Heat map of AI systems by risk tier and governance compliance status:

```
                    Compliant    Partial    Non-Compliant
High Risk              ✓            !              ✗
Significant Risk       ✓            ✓              !
Limited Risk           ✓            ✓              ✓
Minimal Risk           ✓            ✓              ✓

✓ = Green (Compliant)   ! = Amber (Action Required)   ✗ = Red (Halt)
```

#### 3.2.4 AI-Regulatory Compliance Matrix

Maps AI systems to applicable regulatory requirements and compliance status:

```
                    NIST AI RMF  EU AI Act  DPDPA  ISO 42001
AI System A            ✓            ✓         ✓        ○
AI System B            ✓            ○         ✓        ✓
AI System C            !            ✓         ○        ○

✓ = Compliant   ! = In progress   ○ = Not applicable
```

---

### 3.3 Diagrams

#### 3.3.1 AI System Context Diagram

Shows the AI system in the context of its environment — the actors who interact with it, the systems it connects to, and the data flows in and out. Uses ArchiMate notation.

**Mandatory elements:**
- The AI system (boundary)
- User actors (internal and external)
- Upstream data sources
- Downstream consuming systems
- Foundation model provider
- Human oversight mechanism

#### 3.3.2 AI Data Flow Diagram

Shows the complete data lineage from source to model input and from model output to consuming systems.

**Mandatory elements:**
- All data sources (with PII indicator)
- Data transformation steps
- Data storage components (vector DB, feature store, data lake zones)
- Model inference point
- Output delivery to consuming systems
- Data retention and deletion points

#### 3.3.3 AI Governance Architecture Diagram

Shows the governance infrastructure — how the AI system is monitored, how alerts flow, and how the governance response chain operates.

**Mandatory elements:**
- AI Gateway (showing all traffic passes through)
- Monitoring and observability components
- Alert routing
- Human escalation path
- Audit log destination
- Governance team touchpoints

#### 3.3.4 AI Infrastructure Diagram

Physical deployment architecture — cloud regions, compute, networking, and AI platform components.

#### 3.3.5 AI Roadmap Diagram

Time-phased visual representation of the AI implementation roadmap — packages, dependencies, and milestones across quarters.

---

## Chapter 4: AI Architecture Building Blocks

### 4.1 Architecture Building Blocks (ABBs)

ABBs describe required capabilities, independent of how they will be implemented.

#### AI Capability ABBs

| ABB Name | Description |
|---|---|
| Conversational AI Capability | Ability to conduct natural language dialogue with users to answer questions and complete tasks |
| Document Intelligence Capability | Ability to extract, classify, and analyse structured information from unstructured documents |
| Predictive Analytics Capability | Ability to forecast future states or outcomes from historical data patterns |
| Recommendation Capability | Ability to personalise suggestions for content, products, or actions based on user context |
| Autonomous Process Capability | Ability to execute multi-step tasks autonomously using tools and external systems |
| Computer Vision Capability | Ability to classify, detect, or extract information from images or video |
| Code Generation Capability | Ability to generate, complete, review, or explain software code |
| Translation Capability | Ability to convert content between human languages |

#### AI Infrastructure ABBs

| ABB Name | Description |
|---|---|
| AI Gateway Capability | Unified access point for all AI model API traffic with attribution, rate limiting, and logging |
| Model Serving Capability | Infrastructure for hosting and serving AI model inference |
| Knowledge Base Capability | Structured, retrievable store of enterprise documents and data for AI consumption |
| Evaluation Capability | Systematic testing of AI system quality against defined benchmarks |
| AI Observability Capability | Real-time monitoring of AI system performance, cost, and quality in production |
| Prompt Management Capability | Version-controlled management of AI system prompts and configurations |

#### AI Governance ABBs

| ABB Name | Description |
|---|---|
| AI Risk Assessment Capability | Systematic identification, scoring, and treatment of AI system risks |
| AI Compliance Monitoring Capability | Continuous monitoring of AI systems against applicable regulatory requirements |
| AI Audit Trail Capability | Immutable, queryable log of all AI system inputs, outputs, and actions |
| Human Oversight Capability | Mechanisms for human review, approval, and override of AI system outputs |
| AI Incident Response Capability | Processes and infrastructure for detecting, containing, and resolving AI incidents |

---

### 4.2 Solution Building Blocks (SBBs)

SBBs are specific implementation components that realise AI-ABBs. The AIEA Reference Frameworks Library (in the AIEA Repository) maintains the approved SBB catalogue for the enterprise.

**SBB categories:**

| Category | Examples |
|---|---|
| Foundation Models | GPT-4o (OpenAI), Claude Sonnet (Anthropic), Gemini Pro (Google), Llama 4 (Meta) |
| AI Platforms | Azure OpenAI Service, AWS Bedrock, Google Vertex AI, Self-hosted vLLM |
| AI Gateways | LiteLLM, Portkey, Kong AI Gateway |
| Vector Databases | pgvector, Weaviate, Qdrant, Pinecone |
| LLMOps / Observability | Langfuse, LangSmith, Helicone |
| Experiment Tracking | MLflow, Weights & Biases |
| Evaluation Frameworks | Giskard, Promptfoo, DeepEval |
| Feature Stores | Feast, Tecton, AWS SageMaker Feature Store |
| Orchestration Frameworks | LangGraph, AutoGen, CrewAI |
| Security Testing | Microsoft PyRIT, OWASP LLM Testing Guide |

**SBB Approval Process:**
Every SBB must pass the AIEA Vendor Onboarding Process (see AIEA-401) before it may be used in a production AI system. Unapproved SBBs MUST NOT be used in production.

---

## Chapter 5: Deliverable Templates — Quick Reference

### 5.1 AI Data Contract Template

```
═══════════════════════════════════════════════════════
DATA CONTRACT
Name: [Data Asset Name]
Version: [X.Y] | Date: [Date] | Status: [Active]
Producer: [Team responsible for this data]
Consumers: [AI systems that use this data]
═══════════════════════════════════════════════════════

SCHEMA:
  Field Name | Type | Nullable | Description | PII?
  [field]    | TYPE |  YES/NO  | [desc]      | YES/NO

QUALITY SLOs:
  Completeness: [> X% non-null for critical fields]
  Freshness:    [< X hours lag from source]
  Accuracy:     [Reconciles to source within X%]

PII CLASSIFICATION:
  Contains PII: [YES/NO]
  PII Categories: [List]
  Lawful Basis (DPDPA): [Consent / Contract / Legitimate Use]
  Retention: [X years from collection date]

CHANGE MANAGEMENT:
  Breaking Changes:     [X days notice required]
  Non-Breaking Changes: [X days notice required]
  Change Contact:       [Email]

SIGNATURES:
  Producer Approved By: [Name, Date]
  Consumer Acknowledged: [Name, Date, per consumer]
═══════════════════════════════════════════════════════
```

### 5.2 Architecture Decision Record (ADR) Template

```
═══════════════════════════════════════════════════════
ARCHITECTURE DECISION RECORD
ADR-[Number]: [Short Decision Title]
Date: [Date] | Status: [Proposed/Accepted/Superseded]
Decided By: [Name] | Approved By: [Name]
═══════════════════════════════════════════════════════

CONTEXT:
[What situation triggered this decision? What constraints apply?]

OPTIONS CONSIDERED:
  Option A: [Name] — [Summary] — [Key trade-offs]
  Option B: [Name] — [Summary] — [Key trade-offs]
  Option C: [Name] — [Summary] — [Key trade-offs]

DECISION:
[State the decision in one clear sentence]

RATIONALE:
[Why this option over the alternatives? Quantified where possible]

TRADE-OFFS ACCEPTED:
[What are we giving up by choosing this option?]

CONSEQUENCES:
[What does this decision enable? What does it constrain?]

REQUIREMENTS SATISFIED:
[Which requirements from the AI Requirements Repository does this address?]

REVERSIBILITY:
[How hard is this decision to change later? What would trigger a revisit?]

REVIEW DATE: [When should this decision be reviewed?]
═══════════════════════════════════════════════════════
```

### 5.3 AI Incident Report Template

```
═══════════════════════════════════════════════════════
AI INCIDENT REPORT
Incident ID: INC-[Number]
System: [AI System Name] | System Card: [Reference]
Date/Time Detected: [Timestamp]
Severity: [Critical / High / Medium / Low]
Status: [Open / Contained / Resolved / Closed]
═══════════════════════════════════════════════════════

INCIDENT DESCRIPTION:
[What happened? What outputs or actions were problematic?]

USERS/SYSTEMS AFFECTED:
[How many users? Which systems? What actions were taken?]

DETECTION METHOD:
[How was the incident detected? Monitoring alert / user report / audit?]

ROOT CAUSE CATEGORY (OWASP LLM):
[ ] LLM01: Prompt Injection      [ ] LLM02: Sensitive Information
[ ] LLM03: Supply Chain          [ ] LLM04: Data Poisoning
[ ] LLM05: Insecure Output       [ ] LLM06: Excessive Agency
[ ] LLM07: System Prompt Leakage [ ] LLM08: Vector/Embedding
[ ] LLM09: Misinformation        [ ] LLM10: Unbounded Consumption
[ ] Other: [Specify]

ROOT CAUSE ANALYSIS:
[Detailed technical root cause]

IMMEDIATE CONTAINMENT ACTIONS:
[What was done within Hours 0–4?]

REMEDIATION ACTIONS:
  Action | Owner | Due Date | Status

NOTIFICATION OBLIGATIONS:
  DPDPA Breach Notification Required: [Yes/No]
  EU AI Act Notification Required: [Yes/No]
  Notified Parties: [List]
  Notification Date: [Date]

LESSONS LEARNED:
[What process, standard, or tooling change prevents recurrence?]

RED TEAM LIBRARY UPDATE:
[What adversarial prompt is being added to prevent regression?]

INCIDENT CLOSED:
  Date: [Date] | Closed By: [Name] | Post-Mortem Date: [Date]
═══════════════════════════════════════════════════════
```

---

*AIEA Reference Framework Part 3: AI Architecture Content Framework. Document AIEA-301, Version 1.0, 2026.*
*Next: Part 4 — AI Enterprise Architecture Capability and Governance (AIEA-401)*
