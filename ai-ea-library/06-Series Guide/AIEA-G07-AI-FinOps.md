# AIEA® Series Guide
## AIEA-G07: AI FinOps & Token Economics
### Document Number: AIEA-G07 | Version 1.0 | 2026

---

## Preface

This document is an official AIEA Series Guide supplementing the core AIEA Standard. It establishes the financial engineering methodology, cost attribution models, architectural optimization patterns, and organizational governance required to master **AI FinOps** across the enterprise.

Uncontrolled foundation model API usage, inefficient context window stuffing, and premature GPU cluster leasing are among the leading causes of enterprise AI program cancellations. This guide provides the operational framework to align every dollar of AI spend with measurable business value.

This guide MUST be read by Enterprise Architects, Chief Financial Officers (CFOs), AI FinOps Practitioners, Cloud Economists, and Engineering Leads.

---

# Chapter 1: The AI FinOps Framework

The AIEA FinOps Framework adapts the FinOps Foundation lifecycle specifically for AI token economics and accelerated compute:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        THE AI FINOPS LIFECYCLE                          │
├────────────────────────────────┬────────────────────────────────────────┤
│ 1. INFORM (Visibility)         │ 2. OPTIMIZE (Efficiency)               │
│ • Real-time token telemetry    │ • Semantic caching implementation      │
│ • Business unit attribution    │ • Dynamic model routing (SLM vs LLM)   │
│ • Cost-per-query benchmarking  │ • Context window compression           │
├────────────────────────────────┼────────────────────────────────────────┤
│ 3. OPERATE (Continuous Action) │ 4. GOVERN (Policy & Control)           │
│ • Automated budget thresholding│ • Hard spending quotas at AI Gateway   │
│ • Off-peak batch API scheduling│ • Showback / Chargeback ledgers        │
│ • Reserved instance management │ • Monthly ROI variance reviews         │
└────────────────────────────────┴────────────────────────────────────────┘
```

---

# Chapter 2: The Unit Economics of Enterprise AI

Architects MUST understand the fundamental cost drivers of modern AI workloads:

## 2.1 The Input/Output Token Cost Asymmetry
Across frontier model providers, output tokens are priced **3x to 4x higher** than input tokens due to the autoregressive computational nature of token generation (sequential key-value cache memory generation).

| Model Class | Representative Input Cost / 1M | Representative Output Cost / 1M | Cost Ratio (Out : In) |
|---|---|---|---|
| **Frontier GPAI** (e.g., GPT-4o, Claude 3.5 Sonnet) | $2.50 – $3.00 | $10.00 – $15.00 | 4.0x – 5.0x |
| **Mid-Tier Task Model** (e.g., GPT-4o-mini, Claude 3 Haiku) | $0.15 – $0.25 | $0.60 – $1.25 | 4.0x – 5.0x |
| **Self-Hosted Open Weights** (Llama-3-70B on 4x H100) | ~$0.35 (Amortized) | ~$0.35 (Amortized) | 1.0x (Symmetric) |

**Architectural Rule:** In prompt engineering, minimize verbose model completions. Forcing models to emit compact, minified JSON instead of verbose conversational prose reduces output token costs by up to 65%.

## 2.2 Dedicated GPU vs. Serverless API Crossover Modeling

Architects MUST calculate the break-even token volume before committing to reserved cloud GPU instances:

$$\text{Break-Even Volume} = \frac{\text{Monthly Reserved GPU Cost}}{\text{Blended Cost per Million API Tokens}}$$

```
Monthly Spend ($)
   ▲
   │                           / Commercial API (Pay-as-you-go)
   │                          /
   │                         /
   │                        /   <-- Crossover Point (~75M Tokens / Day)
   │                       X
   │                      / ──────────────────────────────────────────
   │                     /   Dedicated Reserved GPU Cluster (Fixed Cost)
   │                    /
   └───────────────────/─────────────────────────────────────────────► Daily Token Volume
```

- **Below 50M tokens/day:** Serverless managed APIs provide superior financial efficiency with zero idle compute waste.
- **Above 100M tokens/day:** Dedicated reserved GPU infrastructure (vLLM on private Kubernetes clusters) delivers 50%–70% lower TCO.

---

# Chapter 3: Architectural Cost Optimization Techniques

Enterprise AI platforms MUST implement the following four technical optimization patterns at the AI Gateway layer:

```
┌─────────────────────────────────────────────────────────────────────────┐
│               AI ARCHITECTURAL COST OPTIMIZATION STACK                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  USER QUERY                                                             │
│       │                                                                 │
│       ▼                                                                 │
│  [ STEP 1: SEMANTIC CACHE ] ───(Cache Hit $\ge 0.96$)───> Return Free   │
│       │ (Miss)                                             Cached Output│
│       ▼                                                                 │
│  [ STEP 2: QUERY CLASSIFIER & ROUTER ]                                  │
│       ├── Simple Query   ──> Route to Low-Cost SLM ($0.15 / 1M)         │
│       └── Complex Reason ──> Route to Frontier LLM ($3.00 / 1M)        │
│                                       │                                 │
│                                       ▼                                 │
│  [ STEP 3: CONTEXT WINDOW COMPRESSION ]                                 │
│       • Selective chunk pruning • Deduplicate redundant embeddings      │
│                                       │                                 │
│                                       ▼                                 │
│  [ STEP 4: BATCH INFERENCE SCHEDULER ] (If non-real-time)               │
│       • Route to 50% Off-Peak Batch API Tier                            │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3.1 Technique 1: Semantic Caching
- **Implementation:** Vector search against previously answered query-response pairs stored in an in-memory database (Redis).
- **Threshold Policy:** Queries with cosine similarity $\ge 0.96$ return the cached answer with zero upstream token cost.
- **Financial Impact:** Reduces enterprise token expenditure by 25% to 40% in repetitive environments (HR helpdesks, customer support, IT troubleshooting).

## 3.2 Technique 2: Dynamic Multi-Model Tiering
- **Implementation:** A lightweight classification model (e.g., DeBERTa or fine-tuned SLM) analyzes incoming query complexity.
- **Routing:**
  - 70% of routine corporate queries (fact lookups, text reformatting, translation) route to low-cost models.
  - 30% of complex queries (legal synthesis, code generation, multi-hop reasoning) route to frontier models.
- **Financial Impact:** Lowers average blended cost per query from $0.045 to $0.012 (a 73% direct cost reduction).

## 3.3 Technique 3: Context Window Compression
- **Implementation:** Eliminating low-relevance paragraphs from retrieved RAG context using Cross-Encoder re-ranking before context injection. Passing only the top 5 chunks rather than top 20 reduces prompt token overhead by 75% per call.

---

# Chapter 4: Enterprise Cost Governance & Chargeback

## 4.1 Header-Based Cost Attribution

Every transaction passing through the AI Gateway MUST carry mandatory financial tracking headers:

```http
POST /v1/chat/completions HTTP/1.1
Host: ai-gateway.enterprise.com
Authorization: Bearer [GatewayToken]
X-Enterprise-BU: Commercial-Banking
X-Cost-Center: CC-84920
X-Project-ID: PROJ-LOAN-COPILOT
X-User-Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The Gateway logs actual input and output tokens consumed, applies the real-time provider tariff, and writes a financial transaction record to the FinOps data warehouse for automated monthly departmental chargeback.

## 4.2 Key Performance Indicators (KPIs) for AI FinOps

| Metric Name | Calculation | Target Benchmark |
|---|---|---|
| **Cost Per Business Outcome** | $\frac{\text{Total Model Spend}}{\text{Total Successfully Resolved Workflows}}$ | Decreasing quarter-over-quarter |
| **Semantic Cache Hit Ratio** | $\frac{\text{Queries Served from Cache}}{\text{Total Ingress Queries}}$ | $\ge 25\%$ across support workloads |
| **Token Efficiency Ratio** | $\frac{\text{Useful Information Tokens Emitted}}{\text{Total Tokens Generated}}$ | $\ge 0.70$ (Minimizing conversational fluff) |
| **Model Tiering Distribution** | % of queries routed to SLMs vs Frontier | $\ge 60\%$ queries handled by Tier 2/SLM |

---

*AIEA Series Guide AIEA-G07: AI FinOps & Token Economics. Document AIEA-G07, Version 1.0, 2026.*  
*AI Enterprise Architecture Forum (AIEAF).*
