# AIEA Reference Framework
## Part 6: Definitions and Glossary
### Document Number: AIEA-601 | Version 1.0 | 2026

---

## Preface

This document is Part 6 of the AIEA Reference Framework — AI Enterprise Architecture Standard. It provides the definitive, normative dictionary of terms, abbreviations, taxonomy definitions, and cross-framework mappings used across the entire AIEA documentation set (Parts 1 through 6 and associated Series Guides).

Consistent terminology is the prerequisite for clear architectural communication, contract drafting, regulatory compliance, and audit defense. When terms defined in this document are used within any AIEA architectural artifact, they carry the specific meanings established herein.

This document MUST be referenced by all enterprise architects, system owners, legal counsel, and auditors interpreting or implementing the AIEA Reference Framework.

---

## Chapter 1: Normative Definitions

The terms defined in this chapter are normative for all parts of the AIEA Reference Framework. Cross-references to other defined terms are indicated in **bold**.

---

### A

**Agentic AI System**  
An autonomous or semi-autonomous software system that utilizes one or more **foundation models** to perceive operational context, decompose complex goals into discrete sub-tasks, execute actions via external tools and APIs, observe outcomes, and dynamically iterate its plan to achieve defined objectives.

**AI Architecture Board (AIAB)**  
The permanent, cross-functional governance body chartered by enterprise executive leadership to review, authorize, govern, and audit all enterprise AI architectures, system deployments, and regulatory compliance evidence.

**AI Architecture Building Block (AI-ABB)**  
A technology-agnostic description of a required enterprise AI architectural capability (e.g., "Semantic Retrieval Capability," "Model Gateway Capability"). ABBs describe *what* the architecture must achieve.

**AI Architecture Development Method (AI-ADM)**  
The 12-phase, iterative lifecycle methodology defined in Part 2 of the AIEA Reference Framework for developing, deploying, governing, and evolving AI-enabled enterprise architectures.

**AI Gateway**  
A dedicated runtime middleware component positioned between enterprise client applications and upstream **foundation model** inference providers that enforces protocol normalization, dynamic routing, semantic caching, rate limiting, FinOps cost attribution, and real-time safety guardrails.

**AI Opportunity Statement**  
A standardized deliverable produced during **Phase 0** of the AI-ADM that formally articulates a proposed AI use case, baseline KPIs, target value hypothesis, preliminary risk tier, and nominated business sponsor.

**AI Solution Building Block (AI-SBB)**  
A concrete, technology-specific implementation component that fulfills an **AI-ABB** (e.g., "Qdrant Vector Database on AWS EKS," "LiteLLM Gateway Cluster"). SBBs describe *how* a capability is implemented.

**AI System Card**  
The authoritative, single-source governance document defined in Part 3 that records an AI system's identity, intended use, risk classification, architectural topology, training/evaluation provenance, performance benchmarks, human oversight design, and named **System Owner**.

**Alignment**  
The process of conditioning a model's behavior to ensure its outputs reliably adhere to human intent, enterprise policies, ethical principles, and safety boundaries.

---

#### B

**Batch Inference**  
The non-real-time execution of model inference over large, pre-collected datasets (e.g., nightly document indexing, customer churn classification) optimized for high throughput rather than low latency.

**Bias (Algorithmic)**  
Systematic and repeatable errors in model predictions or outputs that create unfair disparities or disadvantages for specific demographic groups, classes, or entities.

---

#### C

**Chunking**  
The algorithmic segmentation of unstructured documents into discrete, semantically coherent text segments suitable for mathematical embedding and retrieval within a **RAG** architecture.

**Context Window**  
The maximum quantity of information (measured in **tokens**) that a foundation model can process in a single inference call, encompassing system prompts, user queries, retrieved context, and generated completions.

**Cross-Encoder Re-Ranking**  
A secondary retrieval stage wherein a specialized neural model scores query-document pairs simultaneously, capturing full multi-attention interaction to produce a significantly more accurate relevance ranking than initial dense vector search.

---

#### D

**Data Contract**  
A formal, auditable agreement between an upstream enterprise data producer and a downstream AI system that specifies data schema, delivery SLAs, freshness guarantees, quality thresholds, provenance metadata, and permitted regulatory uses.

**Data Drift**  
A statistically significant shift in the distribution, characteristics, or vocabulary of real-world input data relative to the baseline data upon which an AI model was trained or calibrated.

**Direct Prompt Injection**  
A cybersecurity exploit wherein an adversary injects malicious natural language instructions into a model's input prompt with the deliberate intent of overriding its system prompt instructions, safety guardrails, or operational constraints.

---

#### E

**Embeddings**  
High-dimensional dense vector representations of textual, visual, or multimodal data wherein semantically similar concepts are positioned near one another in mathematical vector space.

**Evaluation Golden Set**  
A curated, version-controlled benchmark dataset of enterprise-specific prompt-completion pairs representing production test cases, edge cases, and adversarial challenges used for automated regression testing.

**Explainability**  
The degree to which the internal reasoning, input feature contributions, or factual grounding underlying an AI system's output can be made intelligible and verifiable to human operators, affected individuals, or regulators.

---

#### F

**Fallback Router**  
A resilient gateway mechanism that automatically redirects inference traffic to an alternative provider, region, or model checkpoint upon detecting timeouts, latency spikes, rate limits, or upstream service degradation.

**Fine-Tuning**  
The process of updating the internal parameters (weights) of a pre-trained **foundation model** on a specialized domain dataset to adapt its style, vocabulary, task performance, or instruction-following behavior.

**Foundation Model**  
A large-scale AI model trained on broad data at scale that can be adapted to a wide range of downstream tasks (e.g., language synthesis, coding, visual analysis) with minimal task-specific modification.

---

#### G

**General Purpose AI (GPAI)**  
An AI model capable of competently performing a wide spectrum of distinct tasks across language, mathematics, reasoning, and multimodal domains (as defined under Article 3 of the EU AI Act).

**Groundedness**  
The quantitative measure of whether every claim and factual statement in an AI generation is strictly supported by and traceable to retrieved enterprise source context.

**Guardrails**  
Synchronous programmatic, heuristic, or neural filters deployed at input and output boundaries of an AI system to intercept and neutralize toxic content, prompt injections, PII leakage, or off-topic queries.

---

#### H

**Hallucination**  
An ungrounded, fabricated, or factually incorrect generation produced by a model with an authoritative, plausible presentation.

**Human-in-the-Loop (HITL)**  
An architectural control pattern wherein an AI system is structurally prohibited from executing consequential or irreversible actions without affirmative human authorization.

**Hybrid Search**  
A retrieval architecture that simultaneously queries dense vector representations (capturing semantic concepts) and sparse lexical indexes (capturing exact keywords and IDs), merging results via **Reciprocal Rank Fusion**.

---

#### I

**In-Context Learning (ICL)**  
The capability of a foundation model to understand a task, format, or business logic dynamically at runtime using only the instructions and few-shot examples supplied within its prompt **context window**, without parameter weight modification.

**Indirect Prompt Injection**  
An exploit wherein malicious instructions are embedded within untrusted external data (e.g., third-party websites, incoming emails, uploaded PDF resumes) retrieved by an AI system, causing the model to hijack execution upon processing the retrieved data.

---

#### J

**Jailbreak**  
A specialized form of adversarial prompt attack designed to bypass or disable a model's embedded safety filters and content moderation policies.

---

#### K

**Knowledge Graph**  
A structured data fabric representing real-world entities, concepts, and explicit semantic relationships as nodes and edges, providing deterministic factual grounding for AI retrieval.

---

#### L

**Large Language Model (LLM)**  
A deep learning model based on the transformer architecture containing billions of parameters trained on vast corpora of textual data.

**Latency (TTFT & P99)**  
- *Time to First Token (TTFT):* The elapsed duration from prompt dispatch until the initial completion token is emitted by the inference engine.
- *P99 Latency:* The 99th percentile response duration across all production requests.

---

#### M

**Model Drift**  
The progressive degradation of an AI model's predictive accuracy, groundedness, or task performance over time due to shifts in external environment, data semantics, or upstream provider model changes.

**Multi-Agent System**  
A distributed architectural topology comprising multiple specialized **Agentic AI Systems** collaborating, delegating sub-tasks, and sharing context to achieve complex enterprise workflows.

---

#### O

**Observability (AI Domain)**  
The real-time instrumentation, telemetry collection, tracing, and analysis of model inputs, outputs, token consumption, inference latency, groundedness scores, and safety violations.

---

#### P

**Parameter-Efficient Fine-Tuning (PEFT)**  
A model adaptation technique that freezes the vast majority of pre-trained model weights and trains only a small fraction of supplementary parameters (e.g., via **LoRA** or prefix tuning), reducing memory and compute requirements by up to 90%.

**Prompt Engineering**  
The discipline of structuring, formatting, constraining, and optimizing natural language instructions provided to foundation models to elicit predictable, high-quality outputs.

---

#### Q

**Quantization**  
The mathematical conversion of model weights from high-precision floating point representations (e.g., FP32, FP16) to lower-precision formats (e.g., INT8, INT4, NF4), dramatically reducing memory bandwidth and GPU compute requirements with negligible accuracy loss.

---

#### R

**Reciprocal Rank Fusion (RRF)**  
A robust mathematical rank aggregation algorithm that merges ordered results from multiple disparate search algorithms (e.g., dense vector search + BM25 lexical search) into a single unified relevance ranking.

**Red Teaming (AI Domain)**  
The structured, adversarial probing and stress-testing of an AI system to identify security vulnerabilities, jailbreak vectors, data exfiltration loopholes, and unintended toxic behaviors prior to deployment.

**Retrieval-Augmented Generation (RAG)**  
An architecture pattern that supplements an AI model's internal parametric knowledge by retrieving relevant factual documents from external enterprise databases and injecting them into the model's prompt context window at inference time.

---

#### S

**Safetensors**  
A secure, open file format for storing machine learning model tensors that prohibits arbitrary code execution during deserialization, replacing insecure legacy formats (such as Python `.pickle`).

**Semantic Caching**  
A caching mechanism that computes vector similarity between an incoming query and previously answered queries, returning the cached response if similarity exceeds a strict mathematical threshold, eliminating redundant inference costs.

**Small Language Model (SLM)**  
A highly optimized, task-focused language model typically under 10 billion parameters designed for efficient, low-latency, edge, or on-premises deployment.

**Sovereign AI**  
The deployment of enterprise AI capabilities entirely within sovereign physical borders, private VPCs, or on-premises infrastructure, ensuring exclusive enterprise ownership of model weights, data, and compute fabrics without reliance on foreign cloud providers.

**System Owner**  
The named individual holding direct organizational and legal accountability for an AI system's business outcomes, risk profile, regulatory compliance, and operational lifecycle.

---

#### T

**Token**  
The basic unit of data processed by a foundation model's tokenizer, typically corresponding to roughly 3 to 4 characters of English text.

**Tool Calling (Function Calling)**  
The architectural capability of a foundation model to output structured JSON arguments targeting an external programmatic API or software routine in response to an identified task requirement.

---

#### V

**Vector Database**  
A specialized database engine designed to store, index, and execute ultra-fast approximate nearest neighbor (ANN) searches over high-dimensional mathematical vector embeddings.

---

#### Z

**Zero-Shot Prompting**  
A prompting method wherein a foundation model is requested to perform a task based solely on its instruction, without providing any demonstration examples in the prompt context.

---

## Chapter 2: Abbreviations and Acronyms Register

| Acronym | Complete Expansion | Architectural Domain |
|---|---|---|
| **ACL** | Access Control List | Security & Data |
| **AIEA** | AI Enterprise Architecture | Governance & Methods |
| **AI-ABB** | AI Architecture Building Block | Content Framework |
| **AI-ADM** | AI Architecture Development Method | Methodology |
| **AI-SBB** | AI Solution Building Block | Content Framework |
| **AI-TRM** | AI Technical Reference Model | Reference Models |
| **AIAB** | AI Architecture Board | Governance |
| **ANN** | Approximate Nearest Neighbor | Data & Search |
| **BPMN** | Business Process Model and Notation | Business Architecture |
| **C2PA** | Coalition for Content Provenance and Authenticity | Trust & Transparency |
| **CAIO** | Chief AI Officer | Leadership |
| **CMM** | Capability Maturity Model | Governance |
| **CDO** | Chief Data Officer | Leadership |
| **CISO** | Chief Information Security Officer | Security |
| **DLP** | Data Loss Prevention | Security |
| **DPO** | Data Protection Officer | Compliance & Legal |
| **DPDPA** | Digital Personal Data Protection Act (India, 2023) | Compliance & Legal |
| **DPIAs** | Data Protection Impact Assessments | Compliance & Legal |
| **DVC** | Data Version Control | MLOps |
| **EAB** | Enterprise Architecture Board | Governance |
| **GPAI** | General Purpose Artificial Intelligence | Technology |
| **HITL** | Human-in-the-Loop | Architecture Patterns |
| **HNSW** | Hierarchical Navigable Small World (Vector Graph) | Data & Search |
| **HyDE** | Hypothetical Document Embeddings | Search & Retrieval |
| **ICL** | In-Context Learning | Technology |
| **IVF** | Inverted File Index | Data & Search |
| **LLM** | Large Language Model | Technology |
| **LLMOps** | Large Language Model Operations | Operations |
| **LoRA** | Low-Rank Adaptation | Model Fine-Tuning |
| **MeitY** | Ministry of Electronics and Information Technology (India) | Compliance & Legal |
| **MLOps** | Machine Learning Operations | Operations |
| **MMR** | Maximal Marginal Relevance | Search & Retrieval |
| **NER** | Named Entity Recognition | Data & Security |
| **NF4** | 4-bit NormalFloat (Quantization) | Infrastructure |
| **NIST AI RMF** | NIST Artificial Intelligence Risk Management Framework | Compliance & Risk |
| **OOD** | Out-of-Distribution | MLOps & Quality |
| **OWASP** | Open Web Application Security Project | Security |
| **PEFT** | Parameter-Efficient Fine-Tuning | Model Fine-Tuning |
| **PII** | Personally Identifiable Information | Security & Privacy |
| **QLoRA** | Quantized Low-Rank Adaptation | Model Fine-Tuning |
| **RACI** | Responsible, Accountable, Consulted, Informed | Governance |
| **RAG** | Retrieval-Augmented Generation | Reference Models |
| **RLHF** | Reinforcement Learning from Human Feedback | Model Alignment |
| **RoCE** | RDMA over Converged Ethernet | Infrastructure |
| **RPM** | Requests Per Minute | Operations & FinOps |
| **RRF** | Reciprocal Rank Fusion | Search & Retrieval |
| **SDF** | Significant Data Fiduciary (under DPDPA) | Compliance & Legal |
| **SLM** | Small Language Model | Technology |
| **SSE** | Server-Sent Events | Integration Patterns |
| **TCO** | Total Cost of Ownership | FinOps & Strategy |
| **TGI** | Text Generation Inference | Infrastructure |
| **TPM** | Tokens Per Minute | Operations & FinOps |
| **TRM** | Technical Reference Model | Reference Models |
| **TTFT** | Time to First Token | Performance Metric |
| **vLLM** | Versatile Large Language Model Serving Engine | Infrastructure |

---

## Chapter 3: Cross-Framework Concept Concordance

The AIEA Reference Framework harmonizes terminology across the major industry enterprise frameworks and regulatory bodies. Architects MUST reference this concordance matrix when translating enterprise artifacts:

| AIEA Reference Framework | TOGAF 10 Standard | NIST AI RMF 1.0 & AI 600-1 | ISO/IEC 42001:2023 | EU AI Act (2024) |
|---|---|---|---|---|
| **AI-ADM Methodology** | TOGAF ADM (Phases A–H) | Core Functions Cycle | AI Management System (Clause 8) | Lifecycle Conformity Assessment |
| **AI Architecture Principles** | Architecture Principles (Part 3) | GOVERN Function (1.1–1.3) | AI Policy & Objectives (Clause 5.2) | Fundamental Rights & AI Ethics |
| **AI System Card** | Architecture Contract / Spec | MAP / MEASURE Profile Record | Documented Information (Clause 7.5) | Technical Documentation (Annex IV) |
| **AI Architecture Board** | Architecture Board | Governance Oversight Body | Top Management / Steering (5.1) | Authorised Representative Oversight |
| **AI Risk Classification** | Architecture Risk Assessment | MAP Function (Categories) | AI Risk Assessment (Clause 6.1.2) | Risk Categorization (Article 6) |
| **AI-ABB / AI-SBB** | ABB / SBB (Content Framework) | Risk Treatment Measures | AI Controls (Annex A) | Quality Management System Measures |
| **Post-Market Telemetry** | Phase H: Architecture Change | MANAGE Function (Continuous) | Monitoring & Measurement (9.1) | Post-Market Monitoring System (72) |
| **Emergency Kill-Switch** | Disaster Recovery / Fallback | MANAGE: Incident Response | Corrective Action (Clause 10.1) | Article 61: Immediate Suspension |
| **AIEA-CMM Maturity** | Architecture Maturity Model | Organizational Profile Tier | Management Review (Clause 9.3) | Maturity of Conformity |

---

## Chapter 4: Master Topical Index and Document Map

This index maps core architectural topics across the six publications of the AIEA Reference Framework:

```
TOPIC                                   PRIMARY REFERENCE                CROSS-REFERENCE
─────────────────────────────────────────────────────────────────────────────────────────────
Accountability & System Ownership        AIEA-101: 3.1, 4.2 (Principle G1) AIEA-401: Chapter 8
AI Architecture Board (AIAB)             AIEA-401: Chapter 3               AIEA-101: 5.3
AI Center of Excellence (CoE)            AIEA-401: Chapter 2               AIEA-101: 3.13
AI FinOps & Token Economics              AIEA-501: 2.2.4                   AIEA-101: 4.4 (Principle O2)
AI Gateway Architecture                  AIEA-501: Chapter 2               AIEA-101: 4.3 (Principle D1)
AI System Card Template                  AIEA-301: Section 2.2             AIEA-401: Gate 3 Review
Agentic AI Architecture & Topologies     AIEA-501: Chapter 4               AIEA-101: 4.3 (Principle D3)
Chunking & Embedding Strategies          AIEA-501: Section 3.2             AIEA-201: Phase C
Conformity Assessment (EU AI Act)        AIEA-401: Section 4.3             AIEA-101: Section 6.2
Data Contracts & Lineage                 AIEA-301: Section 2.3             AIEA-201: Phase C
Emergency Kill-Switch Procedures         AIEA-401: Section 7.3             AIEA-101: Section 3.9
Guardrails & Input/Output Defense        AIEA-501: Chapter 6 (OWASP LLM)   AIEA-401: Gate 2
Human-in-the-Loop (HITL) Controls        AIEA-501: Section 7.4             AIEA-101: Principle D4
Hybrid Search (Dense + Sparse)           AIEA-501: Section 3.3             AIEA-201: Phase C
India DPDPA Compliance                   AIEA-401: Section 4.4             AIEA-101: Section 6.4
Maturity Model (AIEA-CMM)                AIEA-401: Chapter 5               AIEA-101: Section 3.13
Model Independence Principle             AIEA-101: Section 4.3 (D1)        AIEA-501: Chapter 2
NIST AI RMF Implementation               AIEA-401: Section 4.1             AIEA-101: Section 6.1
PEFT / QLoRA Fine-Tuning                 AIEA-501: Section 5.2             AIEA-201: Phase E
Post-Market Monitoring & Telemetry       AIEA-401: Section 7.1             AIEA-201: Phase J
RACI Matrix for AI-ADM                   AIEA-401: Section 8.2             AIEA-201: Chapter 1
RAG Reference Architecture               AIEA-501: Chapter 3               AIEA-101: Principle D2
Re-Ranking (Cross-Encoder / RRF)         AIEA-501: Section 3.3.2           AIEA-201: Phase C
Red Teaming Methodology                  AIEA-401: Gate 2, Section 6.3     AIEA-501: Chapter 6
Risk Classification Tiers                AIEA-101: 4.2 (G2), AIEA-301: 2.2 AIEA-401: Section 3.2
Sovereign AI Deployment Criteria         AIEA-501: Section 8.2             AIEA-101: Principle D5
Technical Reference Model (AI-TRM)       AIEA-501: Chapter 1               AIEA-101: Section 3.10
```

---

*AIEA Reference Framework Part 6: Definitions and Glossary. Document AIEA-601, Version 1.0, 2026.*
*Complete AIEA Reference Framework documentation set. See the [Standards index](README.md) for all Parts and companion material.*
