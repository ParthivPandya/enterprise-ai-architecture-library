# AIEA® Standard
## Part 2: AI Architecture Development Method (AI-ADM)
### Document Number: AIEA-201 | Version 1.0 | 2026

---

## Preface

This document describes the AI Architecture Development Method (AI-ADM) — the core methodology of the AIEA Standard. The AI-ADM provides a systematic, iterative approach to developing, governing, and evolving AI-enabled enterprise architectures.

The AI-ADM is designed to be adapted. Not every enterprise will execute every phase in every AI initiative. The method defines what must be done; each organisation determines the appropriate scope and sequence for its context.

---

# Chapter 1: Overview of the AI-ADM

## 1.1 Purpose

The AI-ADM exists to answer a deceptively simple question: *How do you go from "we should use AI" to AI systems that deliver measurable business value, are properly governed, and can be managed and evolved sustainably?*

The distance between those two points is where most AI programmes fail. Not because the technology doesn't work — but because the journey from idea to governed production capability is not structured. The AI-ADM structures that journey.

## 1.2 Key Characteristics

**Iterative:** The AI-ADM is not a waterfall. Phases may be revisited, repeated, or run in parallel as understanding evolves. An enterprise with five AI systems in development will be executing different phases simultaneously for different systems.

**Risk-proportionate:** The depth and rigour of each phase scales with the risk classification of the AI system under development. A minimal-risk internal tool requires less governance effort than a high-risk customer-facing decisioning system.

**Living method:** The AI-ADM produces a living architecture — the AIEA Repository — that is continuously updated, not a point-in-time document that is produced once and filed away.

**Business-value anchored:** Every phase of the AI-ADM begins with a business question and ends with a business answer. Technology decisions derive from business requirements, not the reverse.

## 1.3 Adapting the AI-ADM

The AIEA Standard RECOMMENDS but does not mandate specific phase sequences. Architects SHOULD adapt the method based on:

- The risk classification of the AI system
- The organisation's existing EA capability and processes
- The integration requirements with TOGAF ADM (if applicable)
- The regulatory context and compliance obligations

## 1.4 The Preliminary Phase: AI Architecture Readiness

Before the AI-ADM begins, the enterprise must assess and establish the architectural capability to execute it. The Preliminary Phase is not an AI-ADM phase — it is the prerequisite for all phases.

### Preliminary Phase Objectives
- Assess the enterprise's current AI architecture maturity
- Establish or confirm the AI architecture operating model
- Define the scope of the AI architecture programme
- Confirm the AI Architecture Principles (Part 1, Chapter 4)
- Establish the AIEA Repository baseline
- Identify and engage key stakeholders

### Preliminary Phase Inputs
- Enterprise business strategy and priorities
- Current IT landscape and EA repository
- Existing AI systems inventory (if any)
- Applicable regulatory requirements (EU AI Act, DPDPA, sector regulations)
- Organisational policies and constraints

### Preliminary Phase Outputs
| Deliverable | Description |
|---|---|
| AI Architecture Readiness Assessment | Current maturity level and gaps |
| AI Architecture Operating Model | Roles, processes, tools, and governance |
| AI Architecture Principles (confirmed) | Agreed principles for this enterprise |
| Tailoring of AI-ADM | How the method will be adapted for this enterprise |
| AIEA Repository Initial Baseline | Inventory of current AI systems |

---

# Chapter 2: Phase 0 — AI Strategy and Opportunity

## 2.1 Objective

Phase 0 establishes the strategic context for AI investment. It translates business strategy into an AI opportunity portfolio — a prioritised set of AI use cases with a clear link to business value and strategic objectives.

This phase is analogous to TOGAF's Architecture Vision phase, but operates at the portfolio level before any specific AI system is designed.

## 2.2 Inputs

- Enterprise business strategy and strategic objectives
- Current AI capability assessment (from Preliminary Phase)
- Business unit priorities and pain points
- Competitive landscape and industry AI benchmarks
- Regulatory environment assessment

## 2.3 Steps

### Step 0.1: Define AI Strategic Intent
Establish the organisation's strategic intent for AI — what role AI will play in delivering the business strategy. Is AI a cost-reduction tool, a revenue enabler, a risk management mechanism, or a competitive differentiator? This intent governs all subsequent prioritisation.

### Step 0.2: Conduct AI Opportunity Discovery
Structured facilitation across business units to surface AI opportunities. Each opportunity is documented as an AI Opportunity Statement:

```
AI Opportunity Statement Template:
  Business Problem:     [One sentence, quantified]
  Current State KPI:    [Measurable baseline]
  AI Hypothesis:        [What AI will do differently]
  Value Estimate:       [Quantified potential value]
  Data Availability:    [Available / Partial / Unavailable]
  Risk Assessment:      [Preliminary risk level]
  Nominated Owner:      [Named business sponsor]
```

### Step 0.3: Score and Prioritise Opportunities
Apply the AIEA Opportunity Scoring Matrix to each opportunity:

| Criterion | Weight | Score (1–5) |
|---|---|---|
| Strategic Alignment | 25% | — |
| Business Value | 25% | — |
| Feasibility (Data + Technical) | 20% | — |
| Measurability | 15% | — |
| Risk Level (inverse) | 15% | — |

**Portfolio Allocation Guidance:**
- Quick Wins (score ≥ 18): Target delivery in 60–90 days
- Strategic Bets (score 12–17): Target delivery in 90–180 days
- Exploratory (score < 12): Research and validation

### Step 0.4: Define AI Portfolio Governance
Establish portfolio-level oversight: the AI Investment Committee, portfolio KPIs, and the review cadence for portfolio health monitoring.

### Step 0.5: Produce AI Strategy Statement
A concise (one-page) statement of the enterprise AI strategy, including: strategic intent, portfolio priorities, resource commitment, governance model, and success measures.

## 2.4 Outputs

| Deliverable | Description |
|---|---|
| AI Strategy Statement | One-page strategic commitment |
| AI Opportunity Portfolio | Prioritised, scored list of AI use cases |
| AI Portfolio Roadmap | Sequenced delivery plan with dependencies |
| AI Investment Framework | Budget model, approval gates, review cadence |

## 2.5 Transition to Phase A

Phase 0 establishes the portfolio. Phase A takes each prioritised AI use case from the portfolio and develops its Architecture Vision. In practice, Phase A will be executed multiple times — once per AI use case being progressed.

---

# Chapter 3: Phase A — AI Architecture Vision

## 3.1 Objective

Phase A develops a high-level Architecture Vision for a specific AI use case — establishing the business case, governance classification, and architectural approach before detailed design begins.

It answers the question: *Is this AI use case worth building, and do we understand what building it entails?*

## 3.2 Inputs

- AI Opportunity Statement (from Phase 0)
- Enterprise AI Architecture Principles
- Enterprise AI Standards Library
- Applicable regulatory requirements
- Stakeholder requirements and constraints

## 3.3 Steps

### Step A.1: Identify Stakeholders and Concerns
Map all stakeholders for this AI use case:

| Stakeholder Class | Typical Concerns |
|---|---|
| Business Sponsor | Value realisation, cost, timeline |
| End Users | Usability, trust, transparency |
| Data Privacy / Legal | DPDPA/GDPR compliance, consent, liability |
| Security / CISO | Prompt injection, data leakage, access control |
| IT / Engineering | Integration, operability, support burden |
| Compliance | Regulatory classification, audit evidence |
| HR / People | Role change, adoption, training |
| Affected Individuals | Right to explanation, fairness, redress |

### Step A.2: Develop AI Business Case
Complete the AI Business Case using the AIEA Business Case Template:

```
AI Business Case:
  Use Case Name:
  Business Problem:     [Quantified with baseline KPI]
  Proposed AI Solution: [What the system will do — in business terms]
  Primary KPI:          [One measurable outcome]
  Target Performance:   [Current → Target = Improvement]
  Measurement Method:   [How the KPI will be measured]
  Financial Model:
    Build Cost:         [One-time]
    Run Cost:           [Annual]
    Governance Cost:    [Annual overhead]
    Value Estimate:     [Annual, with confidence level]
    3-Year ROI:         [Calculated]
    Payback Period:     [Months]
  Risks:                [Top 3 with mitigations]
  Decision Requested:   [Approve development / Approve pilot]
```

### Step A.3: Classify AI System Risk
Apply the AIEA Risk Classification Framework:

**Level 1: Prohibited**
AI uses that MUST NOT be implemented under any circumstances. Aligned with EU AI Act Article 5:
- Social scoring of individuals by government entities
- Real-time biometric identification in public spaces (except legally authorised exceptions)
- AI that exploits vulnerabilities to manipulate individuals subliminally
- Personality profiling based on social media monitoring

**Level 2: High Risk**
AI systems in areas where failure has significant consequences for individuals' rights, health, safety, or livelihoods. Requires full governance track:
- Employment and recruitment AI (CV screening, candidate ranking)
- Education and vocational training AI (assessment, admission)
- Essential services access AI (credit, insurance, utilities)
- Law enforcement AI
- Critical infrastructure management AI
- Healthcare clinical decision support

**Level 3: Significant Risk**
AI systems not in Level 2 but with meaningful impact on individuals or with significant operational risk. Requires standard governance track:
- Customer service AI with consequential outputs (financial advice, legal information)
- Internal HR tools affecting performance assessment
- Procurement and supplier qualification AI
- AI-generated content at scale (misinformation risk)

**Level 4: Limited Risk**
AI systems with transparent, low-impact interactions. Requires basic governance track:
- Simple chatbots with disclosure requirement
- AI content generation tools for internal use
- AI summarisation and analysis tools
- Recommendation engines with human review

**Level 5: Minimal Risk**
AI systems with negligible risk of harm. Self-service checklist only:
- AI spam filters
- AI scheduling assistants
- AI translation for internal documents
- Exploratory AI experiments on non-production data

### Step A.4: Select Build/Buy/Fine-Tune Approach
Apply the AIEA Technology Approach Decision Framework:

```
Decision Tree:
Q1: Does a commercial API solve ≥80% of the requirement
    without requiring proprietary training data?
    YES → Buy (API/SaaS). Proceed to Vendor Onboarding.
    NO  → Continue

Q2: Does an open-weight model perform adequately
    with prompting or RAG, without fine-tuning?
    YES → Self-host open-weight model.
    NO  → Continue

Q3: Is there sufficient domain-specific training data
    to meaningfully improve model performance?
    YES → Fine-tune on domain data.
    NO  → Continue

Q4: Is this a strategically proprietary capability
    that provides defensible competitive advantage?
    YES → Build custom model (specialist team required).
    NO  → Revisit requirement scope.
```

### Step A.5: Develop Architecture Vision Statement
A concise architectural vision for the AI system:
- What it does (in business terms)
- What it does not do (scope boundaries)
- How it fits in the enterprise AI architecture
- Key architectural decisions and their rationale
- Governance path (which review track applies)

### Step A.6: Obtain Architecture Vision Approval
Present the Architecture Vision to the AI Architecture Board for formal approval before proceeding to detailed design phases (B through F).

**Approval criteria:**
- Business case approved by sponsoring executive
- Risk classification completed and accepted
- Technology approach decision documented
- DPDPA / regulatory assessment completed
- Architecture Vision Statement reviewed and approved

## 3.4 Outputs

| Deliverable | Description |
|---|---|
| AI Business Case | Approved financial and value case |
| AI System Risk Classification | Formal risk tier with justification |
| Architecture Vision Statement | High-level architecture direction |
| Technology Approach Decision Record | Build/Buy/Fine-Tune decision with rationale |
| Stakeholder Map and Concern Register | Documented stakeholder concerns |
| Scope Statement | What is in and out of scope |

---

# Chapter 4: Phase B — AI Business Architecture

## 4.1 Objective

Phase B maps AI capabilities to the enterprise's business capability model — establishing exactly which business functions the AI system will change, what the target business state looks like, and what change management is required.

## 4.2 Steps

### Step B.1: Map AI to Business Capabilities
Identify every business capability affected by the AI system:
- Capabilities the AI will augment (human still performs, with AI assistance)
- Capabilities the AI will transform (process redesigned around AI)
- Capabilities the AI will automate (AI performs without human in primary loop)
- Capabilities unchanged (but affected through dependency or data sharing)

### Step B.2: Define Target Business Operating Model
For each affected capability, define the target operating model:

| Element | Current State | Target State |
|---|---|---|
| Who performs the work | [Role] | [Role + AI / AI + human review] |
| Time to complete | [Hours] | [Target time] |
| Error / quality rate | [Baseline] | [Target] |
| Volume capacity | [Current] | [Target] |
| Escalation path | [Current] | [Target] |

### Step B.3: Identify Business Rules and Constraints
Document the business rules that govern the AI system's behaviour:
- Regulatory constraints (what decisions the AI cannot make autonomously)
- Policy constraints (enterprise policies that limit AI scope)
- Commercial constraints (supplier agreements that affect data use)
- Cultural constraints (workforce considerations requiring phased adoption)

### Step B.4: Define Business KPIs and Measurement Plan
For each affected business capability, define:
- Primary KPI (the single most important measure of success)
- Baseline measurement (pre-AI state, how and when measured)
- Target value (what success looks like)
- Measurement method (how the KPI will be tracked in production)
- Attribution approach (how AI contribution will be distinguished from other factors)

### Step B.5: Develop AI Change Management Plan
Document the people-change implications:
- Who is affected and how their roles change
- Training requirements by role group
- Communication plan
- Resistance risk assessment
- AI Champions identification

## 4.3 Outputs

| Deliverable | Description |
|---|---|
| AI-Business Capability Map | Visual mapping of AI to business capabilities |
| Target Business Operating Model | How the business will operate with AI |
| Business Rules Catalog | Documented constraints on AI behaviour |
| Business KPI Framework | Metrics, baselines, targets, and measurement plan |
| AI Change Management Plan | People, communication, and training plan |

---

# Chapter 5: Phase C — AI Data Architecture

## 5.1 Objective

Phase C defines the data architecture required to support the AI system — encompassing data sources, data quality requirements, lineage, governance, privacy compliance, and the technical data infrastructure (feature stores, vector databases, data contracts).

Data architecture is the most common cause of AI project failure. Phase C exists to surface and resolve data issues before they become production problems.

## 5.2 Steps

### Step C.1: Data Source Identification and Assessment
Identify all data sources required for:
- Model training and fine-tuning (if applicable)
- RAG knowledge base (if applicable)
- Real-time inference context
- Evaluation and quality testing

For each data source, assess:

| Dimension | Assessment |
|---|---|
| Availability | Does this data exist and can it be accessed? |
| Quality | Does it meet the five-dimension quality standard? |
| Representativeness | Does it represent the deployment population? |
| Freshness | How current is the data? What is the update frequency? |
| Provenance | Where did this data come from? Is lineage documented? |
| Consent/Lawful Basis | Is there a lawful basis under DPDPA/GDPR? |
| PII Content | Does this data contain personal data? How classified? |

### Step C.2: Data Quality Assessment
Apply the AIEA Five-Dimension Data Quality Standard:

| Dimension | Minimum Standard | Measurement Method |
|---|---|---|
| Completeness | ≥ 99% non-null for critical fields | Automated profiling |
| Accuracy | Reconciles to source within 0.1% | Sample validation |
| Consistency | Uniform representation of key entities | Reference data match |
| Freshness | Within defined SLA for each source | Ingestion timestamp |
| Representativeness | KL divergence < threshold from deployment distribution | Statistical test |

**Data Quality Gate:** AI system development MUST NOT proceed to Phase D if any critical data source fails two or more quality dimensions. Data remediation plan MUST be completed first.

### Step C.3: Data Architecture Design
Design the data infrastructure for the AI system:

- **Data Lake Zone Allocation:** Which data lands in Bronze/Silver/Gold zones? What are the transformation rules?
- **Feature Store Requirements:** Are computed features required? If so, define the feature specifications and ownership.
- **Vector Database Design:** If RAG is used, define chunking strategy, embedding model, retrieval configuration, and access controls.
- **Data Contract Specification:** For each data source, produce a Data Contract defining schema, quality SLOs, freshness commitments, and change management process.
- **Data Lineage:** Document the complete lineage from raw source to model input, for every training and inference data flow.

### Step C.4: Privacy and Compliance Assessment
For every data source containing personal data:

- Document the lawful basis under DPDPA (and GDPR if EU-facing)
- Assess whether data processing triggers DPIA obligation
- Identify PII fields and define pseudonymisation or anonymisation requirements
- Document the data subject rights mechanism (access, correction, erasure) for AI-processed data
- For training data: document the basis for using personal data in model training

### Step C.5: Data Governance Framework
Define data governance for the AI system's lifetime:
- Data steward assignment for each data source
- Data access controls and approval process
- Data retention policy (aligned with regulatory requirements)
- Data breach response procedure specific to this AI system
- Training data versioning and snapshot management

## 5.3 Outputs

| Deliverable | Description |
|---|---|
| AI Data Source Catalog | All data sources with quality assessment |
| Data Architecture Design | Technical design of data infrastructure |
| Data Contract Set | Formal contracts for each data source |
| AI Data Lineage Diagram | End-to-end data flow documentation |
| Privacy and Compliance Assessment | DPDPA/GDPR compliance analysis |
| Data Governance Plan | Stewardship, access, retention, breach response |

---

# Chapter 6: Phase D — AI Application Architecture

## 6.1 Objective

Phase D defines the application architecture of the AI system — the models, pipelines, orchestration, human interfaces, and integration patterns that constitute the deployable system.

## 6.2 Steps

### Step D.1: Define AI System Architecture
Specify the complete application architecture:

- **Model Selection:** Which foundation model(s), specialised model(s), or custom model(s)?
- **Inference Pattern:** Real-time API / Batch / Streaming / Edge?
- **Orchestration Pattern:** Single-agent / Multi-agent hierarchical / Sequential pipeline / Hybrid?
- **RAG Configuration:** If applicable — retrieval strategy, re-ranking, context assembly
- **Prompt Architecture:** System prompt design, few-shot examples, output format constraints
- **Tool and API Integration:** What tools, APIs, and external systems does the system use?
- **Human Interface:** How do users interact? What is the UI/UX design?
- **Human Oversight Mechanism:** How does a human review or override AI outputs?

### Step D.2: Integration Architecture
Define how the AI system connects to enterprise systems:

- **AI Gateway Integration:** The system MUST route through the enterprise AI Gateway
- **Upstream integrations:** What data or events trigger the AI system?
- **Downstream integrations:** Where do AI outputs flow? (CRM update, document generation, notification, etc.)
- **Fallback architecture:** What happens if the AI system is unavailable?
- **Circuit breaker design:** When and how does the system degrade gracefully?

### Step D.3: Output Architecture
Define the structure of AI system outputs:

- **Output format specification:** JSON schema, markdown structure, natural language constraints
- **Citation requirements:** Does the system cite sources? In what format?
- **Confidence expression:** Does the system express uncertainty? How?
- **Output validation:** What post-processing validates outputs before delivery?
- **Logging:** What output content is logged and retained?

### Step D.4: Evaluation Architecture
Design the evaluation system that will measure AI quality:

- **Golden test set:** Define 50–500 representative test cases with ground-truth answers
- **Evaluation metrics:** Task-specific metrics (accuracy, ROUGE, code pass rate) + LLM-as-judge
- **Regression test suite:** Define the test library for pre-deployment CI/CD
- **Red team library:** Define the adversarial test cases (from OWASP LLM Top 10)
- **Human evaluation protocol:** When and how human evaluators review outputs

### Step D.5: Prompt Engineering and Management
Define the prompt architecture:

- **System prompt specification:** Complete system prompt with version number
- **Prompt library:** Repository location and review process for all production prompts
- **Prompt change management:** How prompt changes are reviewed, tested, and approved
- **Token budget:** Maximum token budget per request (input + output) with cost implication

## 6.3 Outputs

| Deliverable | Description |
|---|---|
| AI Application Architecture Design | Complete application architecture specification |
| Integration Architecture | Enterprise system integration design |
| Output Architecture Specification | Output format, validation, and logging design |
| Evaluation Architecture | Test set, metrics, and evaluation pipeline design |
| Prompt Architecture Specification | System prompts and prompt management design |
| AI System Design Diagram | ArchiMate diagram of the complete AI system |

---

# Chapter 7: Phase E — AI Technology Architecture

## 7.1 Objective

Phase E defines the technology infrastructure that will host and operate the AI system — compute, networking, storage, AI platform components, observability, and deployment architecture.

## 7.2 Steps

### Step E.1: Infrastructure Selection
Define the infrastructure for AI system deployment:

- **Cloud vs. On-Premises vs. Hybrid:** Decision based on data sovereignty, cost, latency, and compliance requirements
- **Cloud Provider and Region:** For Indian enterprises, assess India-region availability of required AI services
- **Compute Requirements:** GPU requirements (if self-hosting), CPU for inference, memory
- **AI Platform Services:** Which provider-managed AI services (Bedrock, Azure OpenAI, Vertex AI, self-hosted)

### Step E.2: AI Operational Infrastructure
Define the LLMOps / MLOps infrastructure:

| Component | Purpose | Approved Options |
|---|---|---|
| AI Gateway | Unified API access point | LiteLLM, Portkey, Kong AI |
| Experiment Tracking | Prompt and model versioning | LangSmith, MLflow, Promptflow |
| Observability | Production monitoring | Langfuse, OpenTelemetry |
| Vector Database | RAG embedding store | pgvector, Weaviate, Qdrant |
| Feature Store | ML feature management | Feast, Tecton, SageMaker FS |
| Model Registry | Model version control | MLflow, HuggingFace Hub |
| Inference Server | Self-hosted serving | vLLM, TGI |

### Step E.3: CI/CD Pipeline for AI
Design the CI/CD pipeline for AI system changes:

```
Code/Prompt Change
    ↓ Static Validation (linting, security scan)
    ↓ Unit Tests (known-answer cases)
    ↓ Golden Test Set Evaluation (quality baseline)
    ↓ Red Team Library Run (security validation)
    ↓ Integration Tests (staging environment)
    ↓ Canary Deployment (5% traffic)
    ↓ Progressive Rollout (5% → 25% → 50% → 100%)
```

### Step E.4: Performance and Capacity Design
Define non-functional requirements:

| Metric | Requirement | How Measured |
|---|---|---|
| Latency (p50) | [target ms] | API response time |
| Latency (p95) | [target ms] | API response time |
| Throughput | [requests/second] | Load testing |
| Availability | [target %] | Uptime monitoring |
| Cost per request | [target cost] | AI Gateway attribution |

### Step E.5: Disaster Recovery and Resilience Design
Define the resilience architecture:

- **Primary / Secondary Model Fallback:** If primary model unavailable, what is the fallback?
- **Region Failover:** If primary region unavailable, can the system fail to a secondary region?
- **Graceful Degradation:** What non-AI fallback exists if all AI infrastructure fails?
- **RPO / RTO:** Recovery Point Objective and Recovery Time Objective for this AI system

## 7.3 Outputs

| Deliverable | Description |
|---|---|
| AI Technology Architecture Design | Infrastructure specification |
| LLMOps Infrastructure Design | AI operational infrastructure specification |
| CI/CD Pipeline Design | Automated deployment pipeline specification |
| Performance Architecture | Non-functional requirements and capacity design |
| Resilience Architecture | Fallback and disaster recovery design |

---

# Chapter 8: Phase F — AI Governance Architecture

## 8.1 Objective

Phase F defines the governance architecture for the AI system — implementing the applicable regulatory requirements, security controls, responsible AI measures, and monitoring infrastructure.

Phase F is the most critical phase for high-risk AI systems. It MUST NOT be abbreviated or deferred.

## 8.2 Steps

### Step F.1: NIST AI RMF Application

Apply NIST AI RMF to this AI system:

**GOVERN function outputs:**
- AI system ownership and accountability assignments
- Applicable policies and their application to this system
- Governance review schedule

**MAP function outputs:**
- AI system context documentation
- Risk identification across all NIST AI 600-1 categories (for GenAI systems)
- Stakeholder impact analysis

**MEASURE function outputs:**
- Evaluation plan (pre-deployment benchmarks)
- Production monitoring plan
- Fairness evaluation methodology

**MANAGE function outputs:**
- Risk treatment decisions for each identified risk
- Incident response procedures for this system
- Risk treatment record for AIEA Repository

### Step F.2: EU AI Act Compliance (if applicable)
For AI systems facing EU markets:

- Confirm risk classification (Step A.3)
- For High Risk systems: Complete technical documentation requirement, conformity assessment, and registration plan
- For General Purpose AI providers: Confirm transparency and copyright compliance
- Implement mandatory human oversight mechanisms
- Configure post-market monitoring as required

### Step F.3: DPDPA Compliance (for Indian enterprises)
- Confirm lawful basis for all personal data processing
- Complete DPIA if required (mandated for SDFs and high-risk processing)
- Implement data principal rights mechanism
- Configure breach notification procedure
- Document retention and deletion schedule

### Step F.4: Security Architecture
Implement the AIEA Security Architecture Framework, derived from OWASP LLM Top 10:

| OWASP LLM Risk | AIEA Control |
|---|---|
| LLM01: Prompt Injection | Input validation layer; context integrity checks; privilege separation |
| LLM02: Sensitive Information Disclosure | PII output scanning; system prompt protection testing |
| LLM03: Supply Chain | SBOM for AI; vendor attestation; model integrity verification |
| LLM04: Data Poisoning | Training data validation; anomaly detection post-fine-tuning |
| LLM05: Insecure Output Handling | Output sanitisation before downstream systems; no auto-execution |
| LLM06: Excessive Agency | Least privilege tool grants; action whitelist; approval gates |
| LLM07: System Prompt Leakage | Leakage testing at deployment and on every update |
| LLM08: Vector/Embedding Weaknesses | Access-controlled vector DB; document validation before indexing |
| LLM09: Misinformation | RAG grounding; source citation; output factuality validation |
| LLM10: Unbounded Consumption | Rate limits; token budgets; loop detection |

### Step F.5: Responsible AI Assessment
Complete the AIEA Responsible AI Assessment:

- **Fairness evaluation:** Test for demographic disparities across relevant protected characteristics
- **Explainability design:** Implement explainability mechanism appropriate to risk tier
- **Transparency disclosure:** Confirm user-facing AI disclosure is implemented
- **Bias audit:** Document results and any mitigation actions

### Step F.6: Red Team Exercise
Execute a pre-deployment red team exercise:
- Scope: OWASP LLM Top 10 categories + use-case-specific attacks
- Automated phase: 1,000+ adversarial prompts using automated tooling (PyRIT, Giskard, Promptfoo)
- Manual phase: Domain expert adversarial testing
- Document all findings; resolve Critical and High before launch

## 8.3 Outputs

| Deliverable | Description |
|---|---|
| AI System NIST AI RMF Assessment | Complete four-function assessment |
| EU AI Act Compliance Evidence | Technical documentation and conformity evidence |
| DPDPA Compliance Record | Lawful basis, DPIA, and rights mechanism documentation |
| AI Security Architecture | Implemented security controls per OWASP LLM Top 10 |
| Responsible AI Assessment | Fairness, explainability, and bias audit results |
| Red Team Report | Adversarial testing findings and remediation |
| AI System Card (Draft) | System documentation for the AIEA Repository |

---

# Chapter 9: Phase G — AI Solutions and Roadmap

## 9.1 Objective

Phase G identifies the implementation vehicles — projects, workstreams, and dependencies — required to deliver the target AI architecture. It produces the implementation roadmap and resolves cross-system dependencies.

## 9.2 Steps

### Step G.1: Gap Analysis
Compare current state (AIEA Repository: Current) to target state (AI Architecture designs from Phases B–F):
- What AI capabilities are missing?
- What data infrastructure must be built?
- What governance infrastructure is absent?
- What skills and roles are not yet in place?

### Step G.2: Define Implementation Packages
Group the gaps into implementation packages — coherent units of work that can be delivered by a team:
- Shared AI infrastructure packages (AI Gateway, vector database, LLMOps tooling)
- AI system development packages (one per AI system)
- Data infrastructure packages (feature store, data lake zones, data contracts)
- Governance infrastructure packages (AI registry, monitoring, red team library)

### Step G.3: Sequence and Dependencies
Sequence the implementation packages:
- Shared infrastructure MUST precede dependent AI system development
- Data contracts MUST be in place before training or RAG pipelines are built
- Governance infrastructure MUST be in place before production AI deployment
- Identify and resolve cross-package dependencies

### Step G.4: Produce AI Implementation Roadmap
A sequenced, time-phased view of all implementation packages:
- Quarter-by-quarter delivery plan
- Dependency graph
- Resource requirements per package
- Decision points and approval gates

## 9.3 Outputs

| Deliverable | Description |
|---|---|
| AI Gap Analysis | Current-to-target gap with prioritisation |
| AI Implementation Packages | Defined units of work |
| AI Implementation Roadmap | Time-phased delivery plan |
| Resource and Investment Plan | Budget and people requirements |

---

# Chapter 10: Phase H — AI Migration Planning

## 10.1 Objective

Phase H produces the detailed migration plan — how to transition from the current state to the target state without disrupting existing operations.

## 10.2 Key Considerations for AI Migration

**Model migration:** Switching from one foundation model to another requires: parallel evaluation on the golden test set, canary deployment, regression testing of the red team library, and user communication.

**Data migration:** Moving training data to new infrastructure requires: data contract updates, lineage documentation, quality re-validation, and consent re-verification for personal data.

**System retirement:** Retiring a legacy AI system requires the AIEA Retirement Runbook (see Part 3).

## 10.3 Outputs

| Deliverable | Description |
|---|---|
| AI Migration Plan | Detailed step-by-step migration specification |
| Transition Architecture | Intermediate states during migration |
| Rollback Plan | How to reverse each migration step |
| Communication Plan | Stakeholder and user communication schedule |

---

# Chapter 11: Phase I — AI Implementation Governance

## 11.1 Objective

Phase I provides architectural oversight of AI system implementation — ensuring that what is built conforms to what was architected, and that governance gates are executed at each production milestone.

## 11.2 The Production Launch Gate

Before any AI system enters production, it MUST pass the AIEA Production Launch Gate:

**Technical Readiness Checklist:**
- [ ] Performance benchmarks met (latency, throughput, availability)
- [ ] Fallback and circuit breaker mechanisms tested
- [ ] Cost per inference within approved budget
- [ ] Production monitoring dashboards live
- [ ] Anomaly alerts configured and tested

**Security and Compliance Checklist:**
- [ ] Red team exercise completed, Critical/High findings resolved
- [ ] Output scanning live (PII, harmful content)
- [ ] Audit logging enabled
- [ ] Access controls verified
- [ ] DPDPA/GDPR assessment completed
- [ ] Incident response contacts confirmed

**Governance and Accountability Checklist:**
- [ ] AI System Card completed and in AIEA Repository
- [ ] Named System Owner confirmed
- [ ] Transparency disclosure live
- [ ] Human oversight mechanism tested
- [ ] Rollback plan documented and tested
- [ ] 30-day post-launch review scheduled

**Canary Deployment Protocol:**
- Deploy to 5% of users / traffic
- Monitor for 72 hours against all production KPIs
- Promote to 25% → 50% → 100% on successful monitoring
- Rollback trigger: any Critical incident or KPI degradation > 5%

## 11.3 Ongoing Implementation Governance

- Architecture Compliance Reviews (quarterly for High Risk, annual for all)
- Change request assessment against architecture standards
- Deviation documentation and impact assessment

---

# Chapter 12: Phase J — AI Architecture Change Management

## 12.1 Objective

Phase J establishes the procedures for managing change to the AI architecture — ensuring that the architecture evolves in a controlled, documented manner as the enterprise and technology landscape changes.

## 12.2 Change Triggers for AI Systems

AI architectures change more frequently than traditional IT architectures. Change triggers include:

| Trigger Type | Examples | Response |
|---|---|---|
| Model update | Provider updates underlying model; new model version | Regression test + canary deployment |
| Performance drift | Quality metrics fall below baseline | Retrain / prompt refresh / model upgrade |
| Regulatory change | New DPDPA Rules; EU AI Act phase activation | Compliance gap assessment + remediation |
| Scope expansion | New use case added to existing AI system | Phase A–F assessment for expanded scope |
| Security incident | Jailbreak discovered; data leakage | Immediate red team update + governance review |
| Cost anomaly | Spend exceeds approved budget threshold | FinOps review + optimisation |
| Business change | Business process redesign affecting AI workflow | Phase B reassessment |

## 12.3 Change Classification

| Change Class | Description | Governance Required |
|---|---|---|
| **Standard Change** | Pre-approved pattern (known security patch, approved model minor version) | Self-service with documentation |
| **Normal Change** | Defined but not pre-approved (new feature, prompt update) | AI Architecture review + testing |
| **Major Change** | Significant scope, model, or architecture change | Full Architecture Board review |
| **Emergency Change** | Immediate security or safety risk response | CISO + CAIO approval, retrospective review |

---

# Chapter 13: Continuous Process — AI Requirements Management

AI Requirements Management operates throughout all phases, managing the elicitation, validation, prioritisation, and change management of AI system requirements.

**Key requirements categories for AI systems:**
- Business capability requirements (what the AI must achieve)
- Regulatory and compliance requirements (what the AI must not do)
- Data requirements (what data the AI needs)
- Non-functional requirements (performance, cost, availability)
- Governance requirements (audit, explainability, oversight)
- Stakeholder constraints (risk tolerance, budget, timeline)

**Requirements traceability:** Every architecture decision MUST be traceable to one or more requirements. Requirements changes MUST trigger impact assessment on derived architecture decisions.

---

# Chapter 14: Continuous Process — AI Risk Management

AI Risk Management operates throughout all phases, continuously identifying, assessing, treating, and monitoring AI-related risks.

**Risk identification triggers:** New risk categories identified in NIST AI 600-1, OWASP LLM updates, regulatory guidance, internal incidents, or third-party research.

**Risk treatment options:**
- **Accept:** Risk is acknowledged and deemed acceptable; documented in risk register
- **Mitigate:** Technical or process controls reduce the risk to acceptable level
- **Transfer:** Risk is transferred to a third party (insurance, contractual obligation)
- **Avoid:** AI use case is redesigned or abandoned to eliminate the risk

**Risk register:** A live record of all identified risks, their status, treatment decisions, and residual risk level for every AI system in the AIEA Repository.

---

*AIEA Standard Part 2: AI Architecture Development Method. Document AIEA-201, Version 1.0, 2026.*
*Next: Part 3 — AI Architecture Content Framework (AIEA-301)*
