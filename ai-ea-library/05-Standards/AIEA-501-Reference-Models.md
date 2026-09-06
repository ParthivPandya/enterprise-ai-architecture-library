# AIEA® Standard
## Part 5: AI Reference Models and Technical Standards
### Document Number: AIEA-501 | Version 1.0 | 2026

---

## Preface

This document is Part 5 of the AIEA Standard — AI Enterprise Architecture Standard. It defines the technical reference architectures, integration patterns, security standards, and infrastructure blueprints required to implement production-grade AI systems across the enterprise.

While Part 2 (AI-ADM) describes the method for developing architectures and Part 4 defines organizational capability and governance, Part 5 provides the technical foundation: the structural patterns and technical standards that ensure interoperability, security, scalability, and maintainability.

Analogous to the TOGAF Technical Reference Model (TRM), the AIEA Technical Reference Model (AI-TRM) and its associated reference architectures provide a common vocabulary and taxonomy for technical architecture decisions.

This document MUST be read by Enterprise Architects, AI Solution Architects, Lead Software Engineers, Infrastructure Architects, and Cybersecurity professionals designing AI systems.

---

# Chapter 1: The AI Technical Reference Model (AI-TRM)

## 1.1 Model Overview

The AI Technical Reference Model (AI-TRM) provides a vendor-neutral, layered architecture model defining all technical capabilities required to operate an enterprise AI platform. 

Every enterprise AI deployment draws capabilities from these seven structural layers:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              AIEA TECHNICAL REFERENCE MODEL (AI-TRM)                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  7. APPLICATION & EXPERIENCE LAYER                                      │
│     Conversational UI │ Copilots │ Autonomous Agents │ API Consumers    │
├─────────────────────────────────────────────────────────────────────────┤
│  6. AGENTIC ORCHESTRATION & REASONING FABRIC                            │
│     Prompt Pipelines │ Planning Loops │ Tool Sandboxes │ Memory Stores  │
├─────────────────────────────────────────────────────────────────────────┤
│  5. AI GATEWAY & RUNTIME MIDDLEWARE                                     │
│     Model Routing │ Semantic Cache │ Rate Limiting │ Fallbacks │ FinOps │
├─────────────────────────────────────────────────────────────────────────┤
│  4. DATA, RETRIEVAL & SEMANTIC FABRIC                                   │
│     Vector DBs │ Hybrid Search │ Graph DBs │ Feature Stores │ Lineage   │
├─────────────────────────────────────────────────────────────────────────┤
│  3. FOUNDATION MODEL & INFERENCE LAYER                                  │
│     Commercial GPAI APIs │ Open-Weight LLMs │ Fine-Tuned Models │ SLMs  │
├─────────────────────────────────────────────────────────────────────────┤
│  2. MLOPS & MODEL LIFECYCLE PLATFORM                                    │
│     Dataset Versioning │ PEFT/LoRA Training │ Automated Evals │ Registry│
├─────────────────────────────────────────────────────────────────────────┤
│  1. ACCELERATED COMPUTE & INFRASTRUCTURE                                │
│     GPU/TPU Clusters │ Cloud Virtual Fabrics │ On-Prem Bare Metal       │
├─────────────────────────────────────────────────────────────────────────┤
│  CROSS-CUTTING: TRUST, SECURITY & OBSERVABILITY (ALL LAYERS)            │
│  Guardrails │ Prompt Injection Defenses │ Telemetry │ Audit Logging     │
└─────────────────────────────────────────────────────────────────────────┘
```

## 1.2 Layer Definitions

### Layer 1: Accelerated Compute & Infrastructure
Provides the raw compute, memory, and high-speed networking fabrics required for AI workloads:
- **Accelerated Compute:** NVIDIA Hopper/Blackwell clusters, AMD Instinct, Google Cloud TPUs, AWS Trainium/Inferentia.
- **Interconnects & Networking:** NVLink, InfiniBand, RDMA over Converged Ethernet (RoCE) for distributed model training and tensor-parallel inference.
- **Deployment Environments:** Multi-cloud Kubernetes (vLLM, TGI, Triton Inference Server), serverless container runtimes, or sovereign air-gapped bare-metal racks.

### Layer 2: MLOps & Model Lifecycle Platform
Manages the continuous lifecycle of data preparation, fine-tuning, automated testing, and model registry governance:
- **Feature & Dataset Management:** Feature stores (Feast), data version control (DVC), synthetic data generators.
- **Training & Adaptation Pipelines:** Distributed training orchestrators (Ray, PyTorch Distributed), parameter-efficient fine-tuning (PEFT/QLoRA) pipelines.
- **Model Registry & Packaging:** Standardized artifact storage (MLflow, Hugging Face Enterprise, OCI-compliant container registries).

### Layer 3: Foundation Model & Inference Layer
Hosts and executes model checkpoints across diverse modalities:
- **Commercial Closed-Source GPAI:** Multi-modal foundation models consumed via managed APIs (OpenAI, Anthropic Claude, Google Gemini).
- **Open-Weight Enterprise LLMs:** Self-hosted open weights (Llama 3+, Mistral Large, DeepSeek, Qwen) deployed within private enterprise VPCs.
- **Domain & Small Language Models (SLMs):** Specialized low-latency task models (Phi-4, Gemma, embedding models, cross-encoders) optimized for edge or high-throughput batch inference.

### Layer 4: Data, Retrieval & Semantic Fabric
Structures, indexes, and delivers enterprise context to models in real time:
- **Vector Storage:** Distributed vector databases (Qdrant, Milvus, pgvector, Pinecone) supporting HNSW/IVF indexing and scalar filtering.
- **Hybrid Retrieval Engines:** Combined dense vector embeddings and sparse lexical indices (BM25) with reciprocal rank fusion (RRF).
- **Knowledge Graphs:** Enterprise graph databases (Neo4j, AWS Neptune) providing deterministic entity-relationship grounding.

### Layer 5: AI Gateway & Runtime Middleware
The mandatory abstraction layer governing all model interactions (see Chapter 2).

### Layer 6: Agentic Orchestration & Reasoning Fabric
Coordinates multi-step reasoning, tool execution, and dynamic context assembly (see Chapter 4).

### Layer 7: Application & Experience Layer
The presentation and interaction surface through which human operators, external consumers, or enterprise software trigger AI workloads.

---

# Chapter 2: AI Gateway & Model Abstraction Layer Standards

## 2.1 The AI Gateway Imperative

Per **Principle D1 (Model Independence)**, enterprise applications MUST NOT couple directly to proprietary model provider APIs. An enterprise AI Gateway is a mandatory Solution Building Block (AI-SBB) positioned between all consuming applications and upstream model providers.

```
┌─────────────────┐       ┌────────────────────────────────────────────────────────┐       ┌─────────────────┐
│ Enterprise Apps │       │                  ENTERPRISE AI GATEWAY                 │       │ Model Providers │
│ • Customer Bot  │       │                                                        │       │ • Azure OpenAI  │
│ • Internal Search│ ───> │  • Uniform OpenAI-Compatible API Schema                │ ───>  │ • Anthropic API │
│ • Analytics App │       │  • Semantic Cache (Redis / Qdrant)                     │       │ • Google Gemini │
│ • Agent Workers │       │  • Smart Routing (Cost / Latency / Health)             │       │ • Private vLLM  │
└─────────────────┘       │  • Token Budgeting, Rate Limiting & FinOps Headers     │       └─────────────────┘
                          │  • Real-time Guardrails & Redaction                    │
                          └────────────────────────────────────────────────────────┘
```

## 2.2 Mandatory Gateway Capabilities

Every production AI Gateway deployment MUST implement the following seven technical capabilities:

### 2.2.1 Protocol Normalization
The Gateway MUST expose a single, uniform API interface (standardizing on the OpenAI-compatible REST/SSE streaming format). Application developers write to one schema; the Gateway translates requests and responses to match provider-specific syntaxes (Anthropic, Bedrock, Vertex AI, local vLLM).

### 2.2.2 Dynamic Routing & Tiered Fallback
The Gateway MUST support automated, policy-based model routing:
- **Primary / Secondary Failover:** If the primary provider returns HTTP 429 (Rate Limit), 500 (Server Error), or timeouts (> 3000ms), traffic immediately fails over to a secondary provider or internal open-weight instance.
- **Cost-Optimized Routing:** Routing simple queries (classified by a lightweight classifier) to low-cost SLMs, reserving frontier models for complex multi-step reasoning.
- **Latency Optimization:** Routing to the region with the lowest P99 latency.

```
Fallback Policy Example:
  Primary:   gpt-4o (Azure OpenAI East US)
  Timeout:   2500ms
  Fallback1: claude-3-5-sonnet (AWS Bedrock us-east-1)
  Fallback2: llama-3.3-70b-instruct (Self-hosted vLLM private cluster)
  Emergency: Static error response with deterministic fallback template
```

### 2.2.3 Semantic Caching
To reduce latency and eliminate redundant token costs:
- The Gateway MUST implement semantic caching. Queries with a cosine similarity score exceeding the threshold ($\ge 0.96$) against previously answered queries are served directly from cache without calling upstream models.
- Caching policies MUST support cache invalidation tags, time-to-live (TTL) configurations, and strict exclusion of prompts containing PII or sensitive session variables.

### 2.2.4 FinOps Attribution Headers
Every request passing through the Gateway MUST include standard enterprise attribution headers:

| Header Name | Type | Description | Mandatory |
|---|---|---|---|
| `X-Enterprise-BU` | String | Business Unit identifier (e.g., `Retail-Banking`) | YES |
| `X-Cost-Center` | String | Financial cost center code | YES |
| `X-Project-ID` | String | Unique project code registered in AIEA Repository | YES |
| `X-User-Hash` | String | Pseudonymized hash of end user (for quota tracking) | YES |
| `X-Risk-Tier` | String | Risk classification (`High`, `Significant`, `Limited`, `Minimal`) | YES |

The Gateway MUST log input tokens, output tokens, cached tokens, and calculated financial costs against these headers for automated monthly chargeback reporting.

### 2.2.5 Hard Budget Caps and Quota Throttling
The Gateway MUST enforce rate limits and hard spend caps:
- Per-minute request limits (RPM) and token limits (TPM) per application.
- Monthly financial caps per cost center. Upon reaching 80% of budget, automated alerts notify the System Owner. Upon reaching 100%, the Gateway throttles non-essential requests or downgrades models to low-cost alternatives.

### 2.2.6 Real-Time Safety & Guardrail Interception
All input prompts and model completions MUST pass through synchronous guardrail filters:
- **Ingress Inspection:** Prompt injection detection, PII masking, toxic prompt rejection.
- **Egress Inspection:** Sensitive data leakage prevention (credit cards, API keys, source code secrets), hallucination verification, toxicity filtering.

---

# Chapter 3: Enterprise Retrieval-Augmented Generation (RAG) Reference Architecture

## 3.1 Advanced Enterprise RAG Pipeline

Retrieval-Augmented Generation (RAG) is the primary pattern for grounding models in proprietary enterprise data. Naive RAG architectures (simple vector search + prompt stuffing) fail in production due to context loss, chunk fragmentation, and retrieval irrelevance.

The AIEA Standard mandates the **Advanced Enterprise RAG Reference Architecture**:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        ADVANCED ENTERPRISE RAG ARCHITECTURE                                     │
├────────────────────────────────┬────────────────────────────────┬───────────────────────────────┤
│ 1. INGESTION & ENRICHMENT      │ 2. HYBRID RETRIEVAL FABRIC     │ 3. RE-RANKING & GENERATION    │
│                                │                                │                               │
│  Raw Documents (PDF, Docx, DB) │  User Query                    │  Top K Chunks (e.g., 50)      │
│               │                │         │                      │               │               │
│               ▼                │         ▼                      │               ▼               │
│  Structure-Aware Chunking      │  Query Rewriter & HyDE         │  Cross-Encoder Re-Ranker      │
│  (Semantic / Hierarchical)     │         │                      │  (Selects Top 5–8 Chunks)     │
│               │                │    ┌────┴────┐                 │               │               │
│               ▼                │    ▼         ▼                 │               ▼               │
│  Metadata Enrichment           │  Dense     Sparse              │  Context Compression &        │
│  (ACLs, timestamps, source)    │  Vector    Keyword             │  Citation Formatting          │
│               │                │  (HNSW)    (BM25)              │               │               │
│               ▼                │    └────┬────┘                 │               ▼               │
│  Vector + Metadata Store       │         ▼                      │  Foundation Model +           │
│  (Qdrant / Milvus / pgvector)  │  Reciprocal Rank Fusion (RRF)  │  Groundedness Verification    │
└────────────────────────────────┴────────────────────────────────┴───────────────────────────────┘
```

## 3.2 Ingestion & Indexing Standards

### 3.2.1 Chunking Strategy Selection Matrix
Organizations MUST select chunking strategies based on document structure:

| Document Type | Recommended Chunking Pattern | Chunk Size / Overlap | Key Consideration |
|---|---|---|---|
| **Legal Contracts & Policies** | Hierarchical / Parent-Child Chunking | Child: 256 tokens<br>Parent: 1024 tokens | Small child chunks retrieved; entire parent section provided to LLM for context. |
| **Technical Manuals & Specs** | Semantic / Header-Aware Chunking | Boundary-aligned (by `H1`/`H2`) | Preserves full procedural context without cutting mid-step. |
| **Tabular & Financial Reports** | Structured Table-to-Markdown / JSON | Entire table or row-group | Raw text chunking destroys row-column relationships. Tables must be converted to Markdown tables. |
| **Unstructured Knowledge Articles**| Recursive Character Chunking | 512 tokens<br>Overlap: 64 tokens | General baseline for narrative text. |

### 3.2.2 Metadata and Access Control List (ACL) Tagging
Every indexed chunk MUST include structured metadata:
- `document_id` and `chunk_id`
- `source_uri` (with page number or deep-link anchor)
- `ingestion_timestamp` and `document_version`
- `acl_permissions` (Active Directory / Okta security groups permitted to view the chunk)

**Security Rule:** At query time, the retrieval engine MUST apply mandatory pre-filtering or post-filtering based on the authenticated user's security token. Users MUST NEVER receive retrieval context from documents they lack permission to read in the source system.

## 3.3 Retrieval, Fusion & Re-Ranking

### 3.3.1 Hybrid Search
Enterprises MUST NOT rely solely on dense vector embeddings. Production RAG systems MUST implement Hybrid Search combining:
1. **Dense Retrieval:** Captures semantic meaning, synonyms, and conceptual relationships (e.g., `text-embedding-3-large`, `bge-en-v1.5`).
2. **Sparse Retrieval:** Captures exact keywords, part numbers, SKU codes, and acronyms (BM25 or SPLADE).
3. **Reciprocal Rank Fusion (RRF):** Merges both ranked lists using the standard RRF formula:
   $$RRF\_Score(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
   where $k=60$ and $r_m(d)$ is the rank of document $d$ in retrieval method $m$.

### 3.3.2 Cross-Encoder Re-Ranking
Hybrid retrieval retrieves an initial candidate pool of 30–50 chunks. Passing all candidates to the LLM increases latency, cost, and hallucination risk ("Lost in the Middle" phenomenon).
- A specialized cross-encoder re-ranking model (e.g., Cohere Rerank 3, BGE-Reranker-Large) MUST score query-document relevance pairs.
- Only the top 5 to 8 re-ranked chunks are passed into the final context window.

## 3.4 Automated Ground Truth Evaluation (RAG Triad)

Every RAG system MUST be continuously evaluated against the **RAG Triad Metrics**:

1. **Context Relevance:** Does the retrieved context contain only information pertinent to the query? (Minimizes noise).
2. **Groundedness:** Is every claim in the generated answer directly supported by the retrieved context? (Hallucination detector).
3. **Answer Relevance:** Does the generated response directly answer the user's initial question?

Systems in High-Risk tiers MUST maintain automated daily synthetic evaluation runs. If groundedness scores drop below 0.90, an automated alert MUST trigger Phase J change review.

---

# Chapter 4: Agentic AI & Multi-Agent Architecture

## 4.1 Agentic Systems Definition

An Agentic AI System is an autonomous or semi-autonomous software entity that utilizes foundation models to perceive its environment, formulate multi-step plans, execute actions via external tools and APIs, evaluate outcomes, and iterate toward a goal.

## 4.2 Core Agent Execution Loop

All agent architectures MUST adhere to a structured execution loop that prevents unbounded recursion:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AIEA REASONING & EXECUTION LOOP                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│     ┌──────────────┐          ┌──────────────┐                          │
│     │  USER GOAL   │ ───────> │  PERCEPTION  │                          │
│     └──────────────┘          └──────┬───────┘                          │
│                                      ▼                                  │
│                             ┌────────────────┐                          │
│                             │ PLAN / REASON  │ <───────────────┐        │
│                             └────────┬───────┘                 │        │
│                                      ▼                         │        │
│                             ┌────────────────┐                 │        │
│                             │ TOOL DISPATCH  │                 │        │
│                             └────────┬───────┘                 │        │
│                                      ▼                         │        │
│                             ┌────────────────┐                 │        │
│                             │ SECURITY GATE  │                 │        │
│                             │ (HITL / ACLs)  │                 │        │
│                             └────────┬───────┘                 │        │
│                                      ▼                         │        │
│                             ┌────────────────┐                 │        │
│                             │ TOOL EXECUTION │                 │        │
│                             │  (Sandboxed)   │                 │        │
│                             └────────┬───────┘                 │        │
│                                      ▼                         │        │
│                             ┌────────────────┐                 │        │
│                             │  OBSERVATION & │ ────────────────┘        │
│                             │   EVALUATION   │ (Iterate or Complete)    │
│                             └────────┬───────┘                          │
│                                      ▼                                  │
│                             ┌────────────────┐                          │
│                             │ FINAL OUTCOME  │                          │
│                             └────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**Guardrail Requirement:** Every agent loop MUST implement a hard limit on execution steps (`max_iterations`, default: 10). When the counter expires without goal completion, the agent MUST gracefully suspend and escalate to a human operator.

## 4.3 Multi-Agent Collaboration Topologies

Complex enterprise workflows requiring multiple skill sets MUST NOT be handled by a single monolithic agent. They MUST employ one of three approved multi-agent topologies:

### 4.3.1 Supervisor-Worker (Hierarchical Orchestrator)
- **Structure:** A central Supervisor agent receives the user goal, decomposes it into sub-tasks, assigns tasks to specialized Worker agents (e.g., SQL Specialist, Document Researcher, Code Auditor), aggregates results, and synthesizes the final output.
- **Suitability:** Most enterprise business processes (e.g., loan underwriting, claims processing, technical support escalation).

### 4.3.2 Sequential Pipeline
- **Structure:** Agents execute in a deterministic assembly-line sequence where the output of Agent $N$ becomes the input to Agent $N+1$.
- **Suitability:** Document translation and verification, code generation and linting, compliance audit reports.

### 4.3.3 Consensus / Critic Pattern
- **Structure:** A primary Generator agent produces a draft solution, which is independently evaluated by a Critic agent against security, business rules, or compliance criteria. If the Critic rejects, the Generator refines the draft until consensus is reached.
- **Suitability:** High-stakes financial analysis, legal drafting, security vulnerability assessment.

## 4.4 Tool Execution Sandboxing & Least-Privilege Access

Per **Principle D3 (Minimum Sufficient Agency)**:
1. **Container Isolation:** Agent code-execution tools (Python interpreters, shell environments) MUST run in ephemeral, air-gapped sandboxes (gVisor, Firecracker microVMs, or hardened Docker containers) with zero access to the host enterprise network.
2. **Explicit Tool Schemas:** All agent-callable tools MUST be registered in the AIEA Tool Registry using standard OpenAPI 3.0 / JSON Schema specifications. Unregistered tools are strictly prohibited.
3. **Write-Action Segregation:** Read-only tools (e.g., search knowledge base, check account status) may be executed autonomously. Write-action tools (e.g., transfer funds, update customer record, send external email) MUST trigger a Human-in-the-Loop approval gate before execution (Principle D4).

---

# Chapter 5: Machine Learning & Fine-Tuning Infrastructure

## 5.1 Model Adaptation Decision Framework

Enterprises MUST NOT jump to fine-tuning or training custom foundation models before evaluating lower-complexity alternatives. Architects MUST follow the hierarchical adaptation ladder:

```
LEVEL 1: PROMPT ENGINEERING & IN-CONTEXT LEARNING (ICL)
• Low cost, zero infrastructure. Test system prompts, few-shot examples, structured output formats.
     │
     ▼ (If accuracy/context insufficient)
LEVEL 2: RETRIEVAL-AUGMENTED GENERATION (RAG)
• Moderate cost. Connects enterprise knowledge without changing model weights. Perfect for dynamic data.
     │
     ▼ (If specialized style, vocabulary, or latency constraints require smaller models)
LEVEL 3: PARAMETER-EFFICIENT FINE-TUNING (PEFT / LoRA)
• High specificity, moderate compute. Trains low-rank adaptation matrices (< 1% of parameters).
     │
     ▼ (Only for domain-specific vocabulary and extreme scale: rare in enterprise)
LEVEL 4: CONTINUED PRE-TRAINING / FULL MODEL TRAINING
• Extreme cost ($1M+), massive GPU clusters. Requires AIAB Board approval and dedicated business case.
```

## 5.2 PEFT / QLoRA Pipeline Architecture

When fine-tuning is justified, enterprises SHOULD employ Parameter-Efficient Fine-Tuning (PEFT) utilizing Quantized Low-Rank Adaptation (QLoRA):

1. **Base Model Freezing:** The foundation model weights are quantized to 4-bit NormalFloat (NF4) and completely frozen during training.
2. **Adapter Training:** Trainable low-rank adapter matrices (rank $r=16$ or $32$, alpha $\alpha=32$) are attached to attention and MLP projection layers.
3. **Dynamic Serving:** The enterprise serves a single base model instance in GPU memory (e.g., Llama-3-70B) and dynamically swaps small (50MB–200MB) LoRA adapter weights based on the incoming request header (`X-Project-ID`), dramatically reducing GPU infrastructure costs.

---

# Chapter 6: AI Security & Safety Technical Architecture

AI systems introduce novel attack vectors that bypass traditional network and application firewalls. Enterprise architectures MUST implement technical controls mapped to the **OWASP Top 10 for LLM Applications (2025/2026)**:

| Threat ID | Vulnerability Name | Architectural Defense Mechanism |
|---|---|---|
| **LLM01** | Prompt Injection (Direct / Indirect) | • System prompt isolation with XML delimiters (`<user_input>`, `<system_context>`)<br>• Dual-LLM architecture: auxiliary classifier checks user input before passing to reasoning engine<br>• Real-time guardrail classifiers (Llama Guard, NeMo Guardrails) |
| **LLM02** | Sensitive Information Disclosure | • Bidirectional regex + Named Entity Recognition (NER) PII scrubbing on ingress and egress<br>• Enterprise Data Loss Prevention (DLP) integration at AI Gateway<br>• Differential privacy noise injection for training datasets |
| **LLM03** | Supply Chain Vulnerabilities | • Mandatory cryptographic signature validation for all model weights<br>• Ban raw pickle (`.pkl`/`.bin`) weights; mandate Safetensors (`.safetensors`) format<br>• Dependency vulnerability scanning for all orchestration frameworks (LangChain, LlamaIndex) |
| **LLM04** | Data and Model Poisoning | • Cryptographic provenance tracking for all training and RAG ingestion documents<br>• Outlier detection algorithms running on feature stores and vector embeddings<br>• Automated data validation pipelines with schema contracts |
| **LLM05** | Insecure Output Handling | • Strict output parsing: models must emit JSON conforming to strict JSON Schemas<br>• Automatic HTML/XSS encoding before rendering model outputs in browser UIs<br>• Parameterized queries: model outputs MUST NEVER be concatenated directly into raw SQL or bash commands |
| **LLM06** | Excessive Agency | • Principle of Least Privilege: minimal tool scopes<br>• Human-in-the-Loop confirmation dialogs for all irreversible tool actions<br>• Hard velocity limits and financial transaction caps on tool invocations |
| **LLM07** | System Prompt Leakage | • Canary tokens embedded in system prompts; alerts trigger if canary appears in output<br>• Post-processing output filter redacting instructions or system metadata |
| **LLM08** | Vector and Embedding Weaknesses | • Multi-tenant vector collection isolation with cryptographic partition keys<br>• Regular re-indexing when embedding models are upgraded to avoid semantic distortion |
| **LLM09** | Misinformation / Hallucination | • RAG Groundedness verification: responses must cite verified chunk IDs<br>• Confidence scoring: models return uncertainty flags when source context is weak |
| **LLM10** | Unbounded Consumption | • Hard maximum limits on `max_tokens` per request<br>• Gateway-level rate limiting (RPM/TPM) and global monthly spend caps<br>• Automated circuit-breakers killing runaway recursive agent loops |

---

# Chapter 7: Enterprise Integration Patterns for AI Systems

Architects MUST select from four standard integration patterns based on workload latency, throughput, and statefulness requirements:

```
PATTERN 1: SYNCHRONOUS INFERENCE (REAL-TIME)
App ──────[ HTTP POST / gRPC ]──────> AI Gateway ──────> Model Provider
App <─────[ Server-Sent Events (SSE) Stream ]────────────┘
• Use Case: Interactive chatbots, IDE copilots, search assistance. SLA: < 2000ms.

PATTERN 2: ASYNCHRONOUS EVENT-DRIVEN (DECOUPLED)
App ───[ Publish Event ]───> Kafka Topic ───> AI Consumer Worker ───> AI Gateway
                                                     │
                                                     ▼ (Publish Completion)
App <──[ WebSocket / Webhook ]──────────────── Outbox Event Topic
• Use Case: Long-running agentic tasks, document processing, bulk analysis. SLA: Seconds to minutes.

PATTERN 3: BATCH EMBEDDING & INFERENCE (OFFLINE)
Data Lake ───[ Spark / Ray Batch Job ]───> Vector DB / Model Inference ───> Parquet / Storage
• Use Case: Nightly catalog vectorization, historical email classification, batch scoring.

PATTERN 4: HUMAN WORKFLOW ORCHESTRATION (HITL)
Agent ───[ Task Pending Approval ]───> Enterprise BPMN (ServiceNow / Jira) ───> Human Approver
Agent <──[ Approval Callback ]───────────────────────────────────────────────────────┘
• Use Case: Financial transactions > $10,000, medical diagnoses, legal filing submissions.
```

---

# Chapter 8: Technology Selection & Architecture Decision Framework

## 8.1 Build vs. Buy vs. Fine-Tune Decision Matrix

Architects MUST evaluate all candidate AI initiatives against the standardized AIEA Decision Matrix during AI-ADM Phase E:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              AIEA BUILD vs. BUY vs. FINE-TUNE EVALUATION MATRIX         │
├───────────────────┬───────────────────┬─────────────────────────────────┤
│ CRITERION         │ COMMERCIAL API    │ SELF-HOSTED OPEN WEIGHTS        │
│                   │ (BUY / CONSUME)   │ (BUILD / HOST)                  │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Proprietary IP    │ Low — vendor API  │ High — full control of weights  │
│ Control           │ terms govern use  │ and offline data sovereignty    │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Time to Market    │ Immediate         │ Weeks to months (requires GPU   │
│                   │ (hours to days)   │ cluster setup and deployment)   │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Infrastructure    │ Zero GPU ops;     │ High GPU ops; vLLM cluster      │
│ Complexity        │ managed service   │ management, scaling, patching   │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Data Residency &  │ Dependent on      │ 100% air-gapped within private  │
│ Sovereignty       │ cloud region SLAs │ VPC or on-prem data center      │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Cost at Scale     │ Expensive at high │ High upfront capex/reservations;│
│ (>50M tokens/day) │ token volumes     │ dramatically cheaper unit cost  │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ Latency Guarantee │ Variable; shared  │ Predictable; dedicated tensor-  │
│ (P99)             │ multi-tenant      │ parallel GPU instances          │
└───────────────────┴───────────────────┴─────────────────────────────────┘
```

## 8.2 Sovereign AI and Private Cloud Hosting Criteria

An AI system MUST be deployed on self-hosted, private cloud, or on-premises infrastructure (rather than commercial multi-tenant SaaS) if ANY of the following conditions are met:

1. **National Sovereignty / Regulatory Mandate:** Data classification rules under national laws (e.g., Indian defence/financial sector rules, EU GDPR strict localisation) prohibit processing data outside domestic territorial borders.
2. **Highly Confidential Trade Secrets:** The data contains core proprietary algorithms, source code, or IP whose accidental exposure would cause existential enterprise harm.
3. **Air-Gapped Operational Requirements:** The target environment (manufacturing plant floor, defence facility, offshore oil rig) operates without continuous public Internet connectivity.
4. **Volume Economics Threshold:** The system consistently processes in excess of **100 million tokens per day**, at which point dedicated reserved GPU instances demonstrate a 60%+ TCO advantage over commercial API token pricing.

---

*AIEA Standard Part 5: AI Reference Models and Technical Standards. Document AIEA-501, Version 1.0, 2026.*  
*Next: Part 6 — Definitions and Glossary (AIEA-601)*
