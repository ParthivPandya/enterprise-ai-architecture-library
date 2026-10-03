# AIEA Reference Framework
## Part 7: A Practitioner's Approach to Developing AI Enterprise Architecture Following the AI-ADM
### Document Number: AIEA-701 | Version 1.0 | 2026

---

## Preface

This document is Part 7 of the AIEA Reference Framework — AI Enterprise Architecture Standard. It serves as the companion Practitioner’s Guide to the AI Architecture Development Method (AI-ADM), mirroring the pragmatic, real-world guidance of the TOGAF® Series Guides.

While Part 2 (AI-ADM) describes the formal, normative phases of architecture development, this Practitioner’s Guide answers how enterprise architects execute the method amidst organizational politics, shifting corporate budget cycles, competing vendor claims, and fast-evolving AI technologies.

This guide is written for practicing Enterprise Architects, Lead AI Architects, Chief AI Officers, and Solution Architects who must deliver tangible business outcomes and defensible governance in complex operating environments.

---

## Part 1: The Business & Budget Cycle for AI Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│               THE ENTERPRISE AI ARCHITECTURE & BUDGET CYCLE             │
├───────────────────┬───────────────────┬─────────────────────────────────┤
│ 1. BUDGET         │ 2. BUDGET         │ 3. BUDGET                       │
│    PLANNING       │    PREPARATION    │    ALLOCATION                   │
│ Support Strategy  │ Support Portfolio │ Support Project                 │
│ (3–5 Year Horizon)│ (Annual Planning) │ (Initiative Scoping)            │
│ • Sovereign vs    │ • Quick-Wins vs   │ • Token consumption sizing      │
│   Cloud Capex     │   Agentic Bets    │ • Vector DB compute tiers       │
│ • Enterprise SLAs │ • Theme Grouping  │ • Evaluation golden sets        │
├───────────────────┴───────────────────┴─────────────────────────────────┤
│ 4. BUDGET CONTROL & ARCHITECTURE TO SUPPORT SOLUTION DELIVERY           │
│ (Operational Execution)                                                 │
│ • AI Gateway token throttling • Semantic cache cost avoidance           │
│ • Automated FinOps showback/chargeback attribution                      │
└─────────────────────────────────────────────────────────────────────────┘
```

### Chapter 1: The AI Business & Investment Cycle

Enterprise Architecture does not exist in an academic vacuum; it must synchronize with the enterprise capital allocation process. AI investments differ from traditional IT capital investments in three distinct ways:

1. **Non-Linear Operating Costs (OpEx Volatility):** Model inference scales directly with token consumption and user engagement rather than static user seats.
2. **Rapid Technological Obsolescence:** Model capabilities double every 12–18 months, rendering multi-year software licensing models hazardous.
3. **Dual Compute Regimes:** Enterprises must balance upfront Capital Expenditures (CapEx for private GPU clusters and sovereign appliances) against ongoing Operational Expenditures (OpEx for managed frontier GPAI APIs).

#### 1.1 Budget Planning & Architecture to Support Strategy

During enterprise strategic planning (typically 3–5 year horizons), the Lead AI Architect collaborates with the CAIO and CFO to establish architectural boundaries:

- **Compute Commitment Modeling:** Determining the threshold where dedicated reserved GPU instances (AWS Reserved Instances, Azure Dedicated Host, or on-prem DGX SuperPODs) deliver a lower Total Cost of Ownership (TCO) than on-demand API tokens.
- **Enterprise Foundation Model Agreements:** Establishing multi-tenant master enterprise agreements (MSAs) with model providers that guarantee zero data retention for training, SOC2 Type II compliance, and volume token discount tiers.
- **Sovereignty CapEx Allocations:** Securing capital allocation for private VPC hosting or on-prem air-gapped infrastructure where legal jurisdictions mandate domestic data storage.

#### 1.2 Budget Preparation & Architecture to Support Portfolio

During annual budget preparation, architects categorize and prioritize candidate AI initiatives into the **AIEA Three-Tier Portfolio Allocation Model**:

| Portfolio Tier | Strategic Focus | Delivery Horizon | Target Budget Share | Target Payback Period |
|---|---|---|---|---|
| **Tier 1: Quick-Win Copilots** | Task augmentation, internal document search, automated drafting | 60–90 days | 40% of AI Budget | < 6 months |
| **Tier 2: Operational RAG & Workflows** | Enterprise knowledge synthesis, customer service automation, invoice audit | 90–180 days | 40% of AI Budget | 6–12 months |
| **Tier 3: Strategic Agentic Bets** | Autonomous loan underwriting, drug discovery, automated architecture synthesis | 12–36 months | 20% of AI Budget | 18–36 months |

#### 1.3 Budget Allocation & Architecture to Support Projects

When an AI initiative receives approval to proceed to Phase A, the architect MUST calculate the **Comprehensive AI Project Cost Sizing Formula**:

$$\text{Project Cost} = C_{\text{Dev}} + C_{\text{Data}} + C_{\text{Eval}} + \sum_{m=1}^{12} \left[ (T_{\text{In}} \cdot P_{\text{In}} + T_{\text{Out}} \cdot P_{\text{Out}}) \cdot (1 - R_{\text{Cache}}) + C_{\text{Vector}} + C_{\text{Obs}} \right]$$

Where:
- $T_{\text{In}}, T_{\text{Out}}$: Monthly input and output token volumes
- $P_{\text{In}}, P_{\text{Out}}$: Cost per million tokens for selected models
- $R_{\text{Cache}}$: Expected semantic caching hit ratio (typically 0.20 to 0.45)
- $C_{\text{Vector}}$: Vector database memory and hosting cost
- $C_{\text{Eval}}$: Automated adversarial red-teaming and benchmark evaluation runs
- $C_{\text{Obs}}$: Observability, telemetry logging, and guardrail interception overhead

#### 1.4 Budget Control & Architecture to Support Solution Delivery

During live delivery and operation, the enterprise AI Gateway enforces financial governance programmatically:
- **Header-Enforced Chargeback:** Every API call without a verified `X-Cost-Center` and `X-Project-ID` header is rejected with HTTP 400.
- **Quota Throttling:** Applications exceeding 90% of their monthly token allocation receive warning notifications; at 100%, non-critical workloads are automatically demoted to low-cost Small Language Models (SLMs) or throttled.

---

## Part 2: The Four Purposive Levels of AI Architecture Work

Enterprise architects do not produce a single monolithic architecture. They work across four distinct levels of purpose:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              THE FOUR PURPOSIVE LEVELS OF AI ARCHITECTURE               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  LEVEL 1: ARCHITECTURE TO SUPPORT STRATEGY                              │
│  Scope: Enterprise-wide │ Horizon: 3–5 Years │ Decision: CapEx vs OpEx  │
│  Outputs: Sovereign AI boundaries, Model independence principles        │
│                                │                                        │
│                                ▼                                        │
│  LEVEL 2: ARCHITECTURE TO SUPPORT PORTFOLIO                             │
│  Scope: Business Domain │ Horizon: 12–18 Months │ Decision: Use Cases   │
│  Outputs: Thematic roadmaps, Opportunity scoring, Gap analysis          │
│                                │                                        │
│                                ▼                                        │
│  LEVEL 3: ARCHITECTURE TO SUPPORT PROJECT                               │
│  Scope: Named AI System │ Horizon: 3–6 Months │ Decision: Tech Stack    │
│  Outputs: Logical System Design, Threat Model, System Card (Draft)      │
│                                │                                        │
│                                ▼                                        │
│  LEVEL 4: ARCHITECTURE TO SUPPORT SOLUTION DELIVERY                     │
│  Scope: Engineering Pod │ Horizon: Sprints/Weeks │ Decision: Implementation│
│  Outputs: Prompt templates, Guardrails, Evals, CI/CD Gate Policies      │
└─────────────────────────────────────────────────────────────────────────┘
```

### Chapter 2: Walking Through Architecture to Support AI Strategy

#### 2.1 Understanding Context & Boundary Setting
At the strategic level, the architect defines the enterprise AI posture:
- **Adoption Stance:** Is the enterprise a *Fast Follower* (leveraging commercial APIs) or an *Early Innovator* (training proprietary weights)?
- **Data Sovereignty Perimeter:** Defining non-negotiable boundaries where enterprise data must never exit sovereign borders or on-prem facilities.
- **Vendor Plurality Mandate:** Enforcing that no single model provider controls more than 60% of the enterprise token volume.

#### 2.2 Developing the Target State Architecture
The strategic target state is documented as an **AI Architecture Landscape** in the AIEA Repository, identifying transition plateaus over a 36-month timeline.

---

### Chapter 3: Walking Through Architecture to Support AI Portfolio

#### 3.1 Grouping Work Packages into Strategic Themes
Rather than evaluating 50 disjointed AI use cases, the architect groups them into thematic portfolios:
- *Theme A: Customer Experience Augmentation* (Chatbots, voice assistants, sentiment triage)
- *Theme B: Knowledge Worker Productivity* (Contract analysis, code copilots, proposal generation)
- *Theme C: Operational Decision Automation* (Claims adjudication, fraud detection, supply chain forecasting)

#### 3.2 Managing "Random Ideas from the Wild" (Shadow AI Triage)
Business leaders frequently present unsolicited vendor pitches or unvetted AI tools. The architect employs the **AIEA Wild Triage Protocol**:

```
Unsolicited AI Idea from the Wild
       │
       ▼
Is there an approved AI-ABB in the Reference Library?
  ├── YES ──> Map to existing Solution Building Block (Self-Service)
  └── NO  ──> Evaluate via AIEA Opportunity Scoring Matrix (Part 2, Step 0.3)
                ├── Score < 12 ──> Reject with documented rationale
                └── Score ≥ 12 ──> Initiate formal Phase 0 Discovery
```

---

### Chapter 4: Walking Through Architecture to Support AI Projects

#### 4.1 Ascertaining Dependencies and "Neighboring Systems"
An AI system cannot succeed in isolation. The project architect must map three categories of dependencies:
1. **Upstream Data Dependencies:** Verifying that source systems (SAP, Salesforce, Postgres) provide clean, structured data governed by a binding **Data Contract**.
2. **Security & Identity Dependencies:** Integrating enterprise IAM (Okta, Azure AD) for row-level and chunk-level security trimming in RAG pipelines.
3. **Downstream Integration Dependencies:** Validating that downstream enterprise applications (CRM, ERP) can consume streaming Server-Sent Events (SSE) or handle asynchronous webhooks.

#### 4.2 Performing Architecture Trade-Off Analyses
The project architect executes a formal trade-off analysis comparing candidate architectures:

```
Example Trade-Off: Legal Contract Analysis System
┌──────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│ Criteria         │ Option A: Direct LLM │ Option B: RAG with   │ Option C: Fine-Tuned │
│                  │ Context Stuffing     │ Hybrid Search        │ Domain SLM (LoRA)    │
├──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ Accuracy         │ Moderate (Lost in mid)│ High (Grounded)      │ High (Domain style)  │
│ Hallucination    │ High                 │ Low (Citations)      │ Moderate             │
│ Cost per Query   │ $0.15 (Large context)│ $0.02 (Chunked)      │ $0.005 (Local infer) │
│ Latency (P95)    │ 8.5 seconds          │ 2.1 seconds          │ 0.8 seconds          │
│ Maintenance      │ Zero                 │ Moderate (Index ops) │ High (Retraining)    │
├──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ DECISION         │ REJECTED             │ SELECTED (BEST FIT)  │ FUTURE PHASE         │
└──────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘
```

---

### Chapter 5: Walking Through Architecture to Support Solution Delivery

#### 5.1 Guiding Engineering Pods Without Micromanagement
The delivery architect does not write Python application code. Instead, the architect establishes **Architectural Constraints & Guardrails**:
- Mandating that all model calls traverse the enterprise AI Gateway.
- Requiring that all vector collections utilize standard HNSW index parameters with cosine distance metric.
- Mandating that every agent tool implements strict JSON Schema parameter validation.

#### 5.2 Handover to Operations and Day-2 Governance
Before granting production authorization (Gate 3), the delivery architect validates:
1. Automated CI/CD evaluation test runs pass baseline golden sets.
2. Post-market drift alerts are integrated into PagerDuty / Datadog.
3. The AI System Card is signed by the accountable business System Owner.

---

## Part 3: Enterprise AI Failure Patterns & Anti-Patterns

A mature architecture practice learns from predictable industry failures. Architects MUST actively identify and prevent the **Seven Fatal AI Architecture Traps**:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  THE SEVEN FATAL AI ARCHITECTURE TRAPS                  │
├───────────────────────────────┬─────────────────────────────────────────┤
│ TRAP 1: MODEL-FIRST FALLACY   │ TRAP 2: THE INFINITE POC TRAP           │
│ Selecting LLMs before fixing  │ Building toy prototypes without         │
│ data quality or user needs.   │ security, rate limits, or SLAs.         │
├───────────────────────────────┼─────────────────────────────────────────┤
│ TRAP 3: ARCHITECTURE AFTER    │ TRAP 4: ROGUE SHADOW AI INGESTION       │
│         PROCUREMENT           │ Unvetted SaaS subscriptions exposing    │
│ Engaging EA after signing     │ confidential enterprise IP to vendors.  │
│ multi-year vendor lock-in.    │                                         │
├───────────────────────────────┼─────────────────────────────────────────┤
│ TRAP 5: UNBOUNDED AGENCY      │ TRAP 6: GROUNDING AMNESIA               │
│ Granting write permissions to │ Generating ungrounded answers without   │
│ autonomous agents without HITL│ verifiable source citations.            │
├───────────────────────────────┴─────────────────────────────────────────┤
│ TRAP 7: MISSING THE DAY-2 OPERATIONAL CYCLE                             │
│ Deploying models without drift detection, evals, or retirement plans.   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1. The Model-First Fallacy
- **The Failure:** An executive decrees "we need to build on Model X," prompting engineers to build an architecture around a specific model's proprietary API before defining the business problem, data requirements, or cost constraints.
- **Architectural Remedy:** Enforce **Principle D1 (Model Independence)**. Decouple application code via the AI Gateway. Evaluate models solely on benchmark performance against enterprise golden sets.

#### 2. The Infinite PoC Trap
- **The Failure:** Teams build 30 disjointed Streamlit prototypes that function impressively on clean sample data, but cannot transition to production because they lack enterprise IAM, access control filtering, PII sanitization, or cost predictability.
- **Architectural Remedy:** Mandate that no AI initiative enters development without passing **Gate 0** and committing to standard production building blocks (AI-ABBs).

#### 3. Architecture After Procurement
- **The Failure:** A business unit purchases an AI vendor package with multi-year commitments, only for the Enterprise Architect to discover post-signature that the vendor trains on client data, violates DPDPA cross-border rules, or cannot integrate with corporate Active Directory.
- **Architectural Remedy:** Integrate the AIAB into Corporate Procurement stage-gates. Vendor contracts involving AI processing MUST require AIAB sign-off prior to commercial execution.

#### 4. Rogue Shadow AI Ingestion
- **The Failure:** Employees paste proprietary customer data, intellectual property, or confidential financial forecasts into public consumer AI web interfaces.
- **Architectural Remedy:** Implement enterprise egress proxy filtering blocking unapproved AI endpoints, while simultaneously deploying a sanctioned, safe, enterprise-governed internal assistant backed by an enterprise privacy agreement.

#### 5. The Unbounded Agent Trap
- **The Failure:** An autonomous agent is given access to a database update tool or external email dispatch tool. A single prompt injection attack causes the agent to wipe database records or dispatch fraudulent emails.
- **Architectural Remedy:** Enforce **Principle D3 (Minimum Sufficient Agency)** and **Principle D4 (Reversibility)**. All write actions MUST require explicit human confirmation (HITL). Sandboxed container execution MUST be mandatory.

#### 6. Grounding Amnesia
- **The Failure:** A customer-facing support bot hallucinates non-existent refund policies, legally binding the enterprise in court (e.g., *Moffatt v. Air Canada*).
- **Architectural Remedy:** Enforce **Principle D2 (Grounded Generation)**. The AI Gateway rejects completions that lack verifiable source chunk citations.

#### 7. Missing the Day-2 Operational Cycle
- **The Failure:** A model is deployed successfully, but silently degrades over six months as real-world customer vocabulary drifts, causing error rates to double without detection.
- **Architectural Remedy:** Mandate automated continuous evaluation against golden sets in Phase J. If groundedness or relevance metrics drop below 0.90, automated alerts trigger an architecture review.

---

## Part 4: Transition Architecture & Multi-State Management

Enterprise transformation requires managing multiple concurrent states across a multi-year journey. The architect documents the roadmap through four standard architecture states:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   AIEA MULTI-STATE TRANSITION ROADMAP                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  CURRENT BASELINE STATE                                                 │
│  • Disjointed internal experiments • Unmanaged direct vendor API keys   │
│  • Zero cost attribution • No System Cards • High compliance risk       │
│                           │                                             │
│                           ▼ (Months 0–6)                                │
│  TRANSITION STATE 1: GOVERNED FOUNDATION                                │
│  • Shared AI Gateway live • Enterprise RAG stack standardized           │
│  • Gate 0–3 reviews mandatory • Core System Cards established           │
│                           │                                             │
│                           ▼ (Months 6–18)                               │
│  TRANSITION STATE 2: HYBRID SEMI-AUTONOMOUS                             │
│  • Supervisor-Worker agentic workflows deployed (HITL enforced)         │
│  • Domain fine-tuning (PEFT/LoRA) running on private GPU VPC            │
│  • Automated red-teaming in CI/CD pipelines                             │
│                           │                                             │
│                           ▼ (Months 18–36)                              │
│  TARGET FUTURE STATE: AUTONOMOUS GOVERNED FABRIC                        │
│  • Self-optimizing multi-agent mesh • Real-time dynamic model routing   │
│  • Continuous automated compliance auditing (EU AI Act / DPDPA)         │
│  • Zero data leakage; verifiable mathematical provenance on all outputs │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Part 5: Appendices & Practitioner Toolkits

### Appendix A: AI Stakeholder & Concern Matrix

Practitioners MUST address the specific architectural concerns of distinct enterprise stakeholder groups:

| Stakeholder Class | Primary Concerns | Primary Architecture Deliverable / View |
|---|---|---|
| **Chief AI Officer (CAIO)** | Strategic alignment, ROI realization, portfolio velocity, enterprise adoption | AI Strategy Roadmap, AI Value Dashboard |
| **Chief Information Security Officer (CISO)** | Prompt injection, data poisoning, PII leakage, supply chain tampering | Threat Model (OWASP LLM), Guardrail Specs |
| **Data Protection Officer (DPO)** | DPDPA compliance, EU AI Act conformity, user consent, right to erasure | Data Contract, PII Flow Diagram, DPIA |
| **Board Audit / Risk Committee** | Catastrophic failure, reputational damage, regulatory penalties, bias | AI Risk Classification Register, Incident Logs |
| **Lead AI Architect** | Interoperability, model independence, technical debt, lifecycle hygiene | AI Technical Reference Model, System Cards |
| **Business Unit Sponsor** | Task efficiency, business KPI uplift, delivery timeline, operating cost | Opportunity Statement, Business Architecture Map |
| **Software Engineering Pod** | Clear API contracts, low latency, reliable SDKs, testing harnesses | OpenAPI Specs, AI Gateway Developer Guides |
| **AI Safety Red Teamer** | Jailbreak resistance, adversarial robustness, toxicity filtering | Red Team Evaluation Findings, Benchmark Evals |

---

### Appendix B: Enterprise AI Viewpoint Library

The AIEA Reference Framework establishes six canonical viewpoints for communicating AI architectures:

```
1. STRATEGY & VALUE VIEWPOINT
   • Target Audience: CAIO, CFO, Business Sponsors
   • Focus: Business capability mapping, expected ROI, OKR alignment, portfolio tiering.

2. DATA LINEAGE & PRIVACY VIEWPOINT
   • Target Audience: DPO, Data Architects, Compliance Officers
   • Focus: Ingestion sources, PII filtering stages, vector storage partitions, consent tracking.

3. AI GATEWAY & MODEL ROUTING VIEWPOINT
   • Target Audience: Solution Architects, Platform Engineers
   • Focus: Protocol translation, semantic cache topology, fallback failover paths, token quotas.

4. AGENTIC ORCHESTRATION VIEWPOINT
   • Target Audience: AI Engineers, Security Architects
   • Focus: Supervisor-worker interactions, state machine loops, tool access sandboxing, HITL gates.

5. SECURITY & THREAT MITIGATION VIEWPOINT
   • Target Audience: CISO, Red Team Leads, Security Operations
   • Focus: OWASP LLM attack surface, prompt injection defenses, egress DLP, audit logging.

6. FINOPS & INFRASTRUCTURE TOPOLOGY VIEWPOINT
   • Target Audience: Infrastructure Architects, FinOps Leads
   • Focus: GPU cluster topologies, networking fabrics (InfiniBand/RoCE), token attribution headers.
```

---

### Appendix C: AI Architecture Contract Template

Before any AI system advances past **Gate 3 (Production Launch)**, this formal contract MUST be executed:

```
═════════════════════════════════════════════════════════════════════════
AIEA PRODUCTION ARCHITECTURE CONTRACT
Contract ID: AC-[SystemID]-2026 | Version: 1.0
System Name: [Name of AI System]
═════════════════════════════════════════════════════════════════════════

1. PARTIES TO THE CONTRACT
   • Approving Body:      AI Architecture Board (Represented by Lead AI Architect)
   • Accountable Owner:   AI System Owner ([Named Business Executive])
   • Responsible Pod:     Technical Delivery Lead ([Named Engineering Manager])

2. SYSTEM SPECIFICATION & RISK TIER
   • Risk Classification: [High Risk / Significant / Limited / Minimal]
   • Approved Intended Use: [Precise single-paragraph boundary]
   • Prohibited Uses:       [Explicit out-of-scope behaviors]
   • AI System Card Ref:    [Unique Repository URI]

3. ARCHITECTURAL COMMITMENTS
   • Gateway Compliance:    All model traffic MUST traverse enterprise AI Gateway.
   • Model Independence:   Application code contains ZERO direct provider SDK dependencies.
   • Human-in-the-Loop:     All write actions > $[Amount] or affecting [Entity] REQUIRE HITL.
   • Groundedness Baseline: System MUST maintain $\ge 0.90$ groundedness score.

4. FINOPS & SLA COMMITMENTS
   • Monthly Spend Cap:     $[Dollar Amount] (Hard quota enforced by AI Gateway)
   • Latency SLA:           P95 $\le$ [X] ms | P99 $\le$ [Y] ms
   • Cost Attribution:      All requests include verified `X-Enterprise-BU` headers.

5. OPERATIONAL GOVERNANCE & RETIREMENT TRIGGERS
   • Review Cadence:        [Quarterly / Annual]
   • Mandatory Retirement:  Triggers on model deprecation, regulatory shift, or 3 Sev-1 incidents.
   • Kill-Switch Procedure: Verified operational; cutover executable within 5 minutes.

SIGNATURES:
Lead AI Architect: ____________________ Date: ______________
AI System Owner:   ____________________ Date: ______________
Technical Lead:    ____________________ Date: ______________
═════════════════════════════════════════════════════════════════════════
```

---

*AIEA Reference Framework Part 7: A Practitioner's Approach to Developing AI Enterprise Architecture. Document AIEA-701, Version 1.0, 2026.*
*Independent AIEA Reference Library guidance. See the [Legal Notice](../LEGAL-NOTICE.md).*
