# AI Architecture Review Checklist: Enterprise Architecture Gate Review Framework
## Practitioner Toolkit & Playbook
### Document Ref: AIEA-TK-09 | Version 1.0 | 2026

---

## Executive Summary & Purpose

The **AI Architecture Review Checklist** is a rigorous, gate-based evaluation instrument designed for Enterprise Architecture Review Boards (EARBs), Chief AI Architects, and Solution Architects. Traditional software review checklists fail when applied to probabilistic AI systems because they do not account for non-deterministic behavior, dynamic prompt vulnerability, data lineage degradation, or unpredictable runtime token economics.

This checklist provides standard evaluation gates from ideation to production deployment, supplemented with three detailed practical scenarios to contextualize evaluation decisions.

---

## Architecture Review Gates Overview

```
[ Gate 0: Strategy & Value ] ──► [ Gate 1: Data & Privacy ] ──► [ Gate 2: Model & Architecture ] 
                                                                             │
[ Gate 4: Operations & FinOps ] ◄── [ Gate 3: Guardrails & Safety ] ◄────────┘
```

| Gate | Focus Area | Key Architectural Concern | Sign-Off Stakeholder |
| :--- | :--- | :--- | :--- |
| **Gate 0** | Business & Strategic Alignment | Problem-model fit, ROI justification, Buy vs. Build | Lead Enterprise Architect / AI Strategist |
| **Gate 1** | Data, Privacy & Sovereignty | Data lineage, PII handling, DPDP/GDPR compliance | Chief Data Architect / DPO |
| **Gate 2** | Model & Inference Architecture | Latency budgets, context window sizing, fallback tiers | Principal AI / Solution Architect |
| **Gate 3** | Guardrails, Safety & Ethics | Prompt injection defenses, hallucination limits, HITL | Responsible AI Officer / SecOps |
| **Gate 4** | Production LLMOps & FinOps | Tracing telemetry, drift detection, token circuit breakers | Cloud FinOps Lead / SRE Lead |

---

## Three Practical Review Scenarios

To assist review committees in applying these criteria realistically, this checklist provides three reference application scenarios:

### Practical Scenario A: Tier-1 Bank Loan Underwriting Assistant
- **Context**: A multi-agent system analyzing corporate borrower balance sheets, synthesizing credit committee memos, and recommending risk ratings.
- **Risk Profile**: High (Direct financial and regulatory impact; subject to Fair Lending regulations and auditability requirements).
- **Key Architectural Challenge**: Complete explainability, mathematical grounding, zero tolerance for fabricated financial covenants.

### Practical Scenario B: Healthcare Clinical Note Summarizer
- **Context**: A clinical assistant transcribing physician-patient consults, extracting ICD-10 diagnostic codes, and generating discharge summaries for Electronic Health Record (EHR) ingestion.
- **Risk Profile**: Extreme / Critical (Patient safety, HIPAA / DPDP sensitive health data processing).
- **Key Architectural Challenge**: Strict PII/PHI de-identification at line rate, strict medical terminology fidelity, mandatory physician sign-off.

### Practical Scenario C: Global E-Commerce Autonomous Support Concierge
- **Context**: Customer-facing conversational agent resolving order tracking inquiries, processing product returns, and issuing refunds up to $50.
- **Risk Profile**: Medium-High (Direct public exposure, transactional write permissions).
- **Key Architectural Challenge**: Prompt injection immunity, deterministic guardrails around financial refunds, sub-second latency SLA.

---

## Gate 0: Strategic Alignment & Concept Fit

| Item ID | Review Criterion | Verification Artifact Required | Scenario A (Banking) | Scenario B (Healthcare) | Scenario C (E-Commerce) | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G0.1** | **Problem-Model Appropriateness**: Is generative/probabilistic AI actually required, or is a deterministic rule-engine/classical ML superior? | Architecture Decision Record (ADR) justifying GenAI | Verified: Unstructured credit notes require semantic extraction | Verified: Natural clinician dialogue requires speech-to-text + LLM | Verified: Natural language intent parsing required | [ ] |
| **G0.2** | **Buy vs. Build vs. Tune Evaluation**: Clear analysis comparing commercial SaaS, managed Foundation Models, open-source weights, or fine-tuning. | Model Selection Matrix & TCO Model | Selected: Self-hosted LLM (Llama-3-70B on sovereign cloud) | Selected: HIPAA-compliant dedicated instance (Claude on AWS Bedrock) | Selected: Multi-model router (GPT-4o mini + Claude 3.5 Haiku) | [ ] |
| **G0.3** | **Value Realization & ROI Baseline**: Identified measurable KPI improvements (e.g., labor hour reduction, NPS, churn, throughput). | Business Value Tree & Benefits Realization Plan | Target: Underwriting cycle reduced from 14 days to 48 hours | Target: Clinician documentation burden reduced by 2.2 hrs/day | Target: Tier-1 deflection rate increased by 42% | [ ] |
| **G0.4** | **Human-in-the-Loop (HITL) Definition**: Clear architectural boundaries defining autonomous execution vs mandatory human verification. | User Workflow & Decision Boundary Diagram | Mandatory: Credit officer must approve all generated memos | Mandatory: Attending physician must sign off discharge summary | Autonomous: Refunds < $50; Human review for disputes > $50 | [ ] |

---

## Gate 1: Data, Privacy & Sovereignty

| Item ID | Review Criterion | Verification Artifact Required | Scenario A (Banking) | Scenario B (Healthcare) | Scenario C (E-Commerce) | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G1.1** | **Data Classification & Boundary**: Training, fine-tuning, and RAG retrieval data clearly classified according to enterprise data policy. | Data Inventory & Classification Matrix | Classified as Restricted Financial Data; isolated tenant | Classified as Confidential PHI; strictly isolated VPC | Classified as Internal Order Metadata; public catalog | [ ] |
| **G1.2** | **Zero Data Retention (ZDR) Guarantees**: Contractual and technical verification that foundation model vendors do NOT train on enterprise prompts. | Vendor Contract Addendum / Enterprise Agreement | On-premise air-gapped deployment; zero external transmission | Signed BAA (Business Associate Agreement) with AWS Bedrock | Enterprise ZDR clause confirmed with OpenAI / Azure | [ ] |
| **G1.3** | **PII/PHI Sanitization at Ingress**: In-flight tokenization or redaction of identifiers before context is submitted to model inference. | Pipeline Schema & Presidio/NeMo Tokenizer Config | Customer names, tax IDs tokenized via internal vault | Deep real-time NER stripping 18 HIPAA identifiers | Customer credit cards, emails hashed prior to vector DB | [ ] |
| **G1.4** | **RAG Access Control Propagation**: Vector database queries dynamically filter results based on the querying user's IAM entitlements. | Vector DB Filter Architecture & Test Suite | Vector search applies ACL filters matching loan officer portfolio | Vector search restricted to patient's assigned care team | Catalog search is public; order history filtered by Customer_ID | [ ] |
| **G1.5** | **Data Residency & Cross-Border Compliance**: Model compute and vector storage reside within sanctioned geographic jurisdictions (DPDP, GDPR). | Infrastructure Topology & Cloud Region Proof | Local sovereign data center (e.g., Mumbai / Frankfurt) | Cloud region pinned to US-East-1 (HIPAA zone) | Multi-region local routing (EU data in Dublin, US in Virginia) | [ ] |

---

## Gate 2: Model & Inference Architecture

| Item ID | Review Criterion | Verification Artifact Required | Scenario A (Banking) | Scenario B (Healthcare) | Scenario C (E-Commerce) | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G2.1** | **Latency Budget & SLA**: End-to-end latency budget (P50, P95, P99) defined including retrieval, reranking, inference, and guardrails. | Latency Waterfall Breakdown Diagram | SLA: P95 < 12 seconds (Batch / Asynchronous UI) | SLA: P95 < 4 seconds (Real-time consult workflow) | SLA: P95 < 1.2 seconds (Synchronous customer chat) | [ ] |
| **G2.2** | **Context Window Sizing & Chunking**: Optimal token chunking strategy documented (chunk size, overlap, semantic splitting). | RAG Benchmark & Retrieval Precision Report | Hybrid search (BM25 + Dense vector); 512 token chunks, 10% overlap | Document-aware hierarchical chunking by medical section | 256 token chunks for product FAQ; direct SQL for order status | [ ] |
| **G2.3** | **Graceful Degradation & Fallback Tier**: Documented fallback paths if primary model encounters rate limits, downtime, or context overflow. | Resilience Failure Mode Analysis (FMEA) | Secondary replica of self-hosted model; manual memo queue | Fallback to raw transcribed text + audio playback | Fallback to rule-based IVR menu + live agent routing | [ ] |
| **G2.4** | **Deterministic Grounding & Citations**: System architecture enforces strict source citations for all factual assertions. | Prompt Engineering Spec & Output Schema Parser | Output schema enforces `[Document_ID, Page, Line]` citations | Mandatory link to exact audio snippet and EHR timestamp | Output links to verified public shipping policy URL | [ ] |
| **G2.5** | **Agentic Tool-Calling Constraints**: If using agents, all tool definitions have strict parameter typing, validation, and idempotency keys. | OpenAPI Tool Spec & Tool Execution Policy | Tool access restricted to Read-Only financial warehouse | Tool access restricted to FHIR Read APIs | Refund tool has strict parameterized cap ($50 max, 1 per order) | [ ] |

---

## Gate 3: Guardrails, Safety & Responsible AI

| Item ID | Review Criterion | Verification Artifact Required | Scenario A (Banking) | Scenario B (Healthcare) | Scenario C (E-Commerce) | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G3.1** | **Prompt Injection & Jailbreak Defenses**: Implemented multi-layered defense (input sanitization, canary tokens, output classifiers). | Threat Model Document & Red Team Pentest Report | Dual-model classifier inspecting prompts before model ingestion | Strict prompt boundary tags; system instructions encrypted | NeMo Guardrails blocking roleplay, jailbreak, and system overrides | [ ] |
| **G3.2** | **Hallucination & Faithfulness Threshold**: Quantitative evaluation pipeline verifying output faithfulness against retrieved context. | Ragas / TruLens Faithfulness Evaluation Suite | Faithfulness score threshold: > 0.96; reject and flag if below | Faithfulness score threshold: > 0.99; highlight uncertain claims | Faithfulness score threshold: > 0.90; fallback to agent | [ ] |
| **G3.3** | **Fairness, Bias & Disparate Impact**: Algorithmic assessment proving model recommendations do not produce discriminatory outcomes. | Disparate Impact Audit Report & Demographics Test | Bias testing across demographic loan applicant segments | Linguistic dialect testing for clinical transcription accuracy | Tone neutrality and sentiment consistency testing | [ ] |
| **G3.4** | **System Persona & Boundary Enforcement**: Model strictly refuses queries outside its defined domain competence. | Persona Boundary Test Suite (Negative test cases) | Refuses investment advice, personal financial planning | Refuses direct diagnosis; acts only as transcriber/summarizer | Refuses political, social, or competitor inquiries | [ ] |
| **G3.5** | **Audit Trail & Non-Repudiation**: Full trace (User prompt, retrieved context, raw prompt, raw output, guardrail flags) captured immutably. | Immutable Audit Architecture & Retention Policy | 7-year retention in WORM compliant financial storage | 6-year HIPAA medical record compliant audit log | 90-day searchable trace storage for customer dispute resolution | [ ] |

---

## Gate 4: Production LLMOps, Observability & FinOps

| Item ID | Review Criterion | Verification Artifact Required | Scenario A (Banking) | Scenario B (Healthcare) | Scenario C (E-Commerce) | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G4.1** | **End-to-End Tracing & Telemetry**: OpenTelemetry-compliant GenAI tracing (token counts, latency, prompt version, model provider). | Observability Architecture Spec (Arize/Langfuse) | OpenTelemetry instrumentation feeding central enterprise Splunk | Dedicated Arize Phoenix instance inside healthcare VPC | Langfuse distributed tracing integrated into Datadog | [ ] |
| **G4.2** | **Continuous Automated Evaluation (CI/CD)**: Regression test suite testing golden datasets before prompt or model updates are released. | CI/CD Evaluation Pipeline Script (GitHub Actions / GitLab) | Automated regression test run against 500 historical loan cases | Test run against 250 multi-specialty anonymized patient charts | Nightly evaluation against 1,000 top customer inquiry variants | [ ] |
| **G4.3** | **Token Consumption & Cost Circuit Breaker**: Automated hard rate-limits and cost caps per tenant, preventing run-away loops. | Cloud FinOps Budget Spec & Auto-shutdown Lambda | Monthly compute budget cap ($25,000); alerts at 80% | Per-clinician daily token ceiling (500,000 tokens) | Global rate limiter: 50 requests/min per IP; $0.08 per session cap | [ ] |
| **G4.4** | **Data & Concept Drift Monitoring**: Automated detection of changes in input prompt distribution or output embedding shift. | Drift Alerting Configuration & Dashboard | Weekly Kolmogorov-Smirnov test on input feature embeddings | Embedding drift monitoring on clinical terminology distribution | Real-time monitoring of unhandled customer intent clusters | [ ] |
| **G4.5** | **Emergency Kill-Switch & Circuit Breaker**: Operational mechanism to instantly disable GenAI capabilities and revert to legacy flow. | Disaster Recovery Runbook & Kill-Switch Validation | Single-click API toggle routing underwriters to manual template | Instant bypass to standard EHR dictation transcriptionist | Instant toggle replacing GenAI widget with rule-based menu | [ ] |

---

## Architectural Sign-Off Matrix & Scoring Rubric

### Scoring Criteria
- **Green (Ready for Production)**: 100% of Mandatory items passed. Any non-mandatory items have approved ADR exemptions.
- **Amber (Conditional Approval)**: Max 2 minor gaps in Gate 4; remediation plan approved within 30 days. No Gate 1 or Gate 3 failures permitted.
- **Red (Rejected / Rework Required)**: Any failure in Gate 1 (Data & Privacy) or Gate 3 (Guardrails & Safety).

### Sign-Off Signatures

| Role | Name | Recommendation (Approve / Reject / Conditional) | Signature | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Enterprise Architecture Review Lead** | | | | |
| **Chief AI / Solution Architect** | | | | |
| **Chief Information Security Officer (CISO)** | | | | |
| **Data Protection Officer (DPO)** | | | | |
| **Business Product Owner** | | | | |
