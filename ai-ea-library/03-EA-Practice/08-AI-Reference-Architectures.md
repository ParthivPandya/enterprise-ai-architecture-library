# AI Reference Architectures for the Enterprise

> *Reference architectures are the vocabulary of engineering decisions. They give teams a shared language, a proven starting point, and a framework for discussing trade-offs. This chapter is a set of battle-tested starting points — not to be copied wholesale, but to be adapted with understanding.*

> **Related:** [../00-Foundations/03-Data-Architecture-for-AI.md](../00-Foundations/03-Data-Architecture-for-AI.md) | [../00-Foundations/04-Multi-Agent-Orchestration.md](../00-Foundations/04-Multi-Agent-Orchestration.md) | [../03-EA-Practice/03-Strategic-Runbooks.md](03-Strategic-Runbooks.md)

---

## How to Read These Architectures

Each reference architecture in this chapter covers:
- **The pattern:** What the architecture does and why
- **The component diagram:** The key components and their relationships
- **Key decisions:** The choices you must make to instantiate this pattern
- **Governance requirements:** What the architecture needs to meet enterprise standards
- **When NOT to use it:** Patterns get misapplied — this section prevents that

None of these should be implemented literally without first running through [03-Strategic-Runbooks.md](03-Strategic-Runbooks.md) Runbook 1 (Use Case Evaluation) and Runbook 2 (Vendor Onboarding) for the components involved.

---

## Architecture 1: Enterprise RAG — Knowledge Base Q&A

The most widely deployed enterprise AI architecture. Answers questions grounded in an organisation's own documents — policies, contracts, research, product documentation.

### The Pattern

```
┌─────────────────────────────────────────────────────────┐
│                    INGESTION PIPELINE                    │
│  Documents → Chunking → Embedding → Vector DB Index     │
│  (scheduled, event-triggered, or streaming)             │
└─────────────────────────────────────────────────────────┘
                              ↓ (offline, background)

┌─────────────────────────────────────────────────────────┐
│                    INFERENCE PIPELINE                    │
│                                                         │
│  User Query                                             │
│       ↓                                                 │
│  [Input Validation + Auth]                              │
│       ↓                                                 │
│  [Query Rewriting] ← (optional: clarify ambiguous query)│
│       ↓                                                 │
│  [Query Embedding] → same model as document embedding   │
│       ↓                                                 │
│  [Vector Similarity Search] → top-k chunks             │
│       ↓                                                 │
│  [Re-Ranking] → more precise relevance scoring         │
│       ↓                                                 │
│  [Context Assembly] → chunks + metadata + prompt       │
│       ↓                                                 │
│  [LLM Generation] → grounded answer                    │
│       ↓                                                 │
│  [Output Validation] → PII check, factuality check     │
│       ↓                                                 │
│  [Response + Citations]                                 │
└─────────────────────────────────────────────────────────┘
```

### Key Decisions

**Embedding model:** Use the same model for both document embedding (at ingestion) and query embedding (at inference). Mismatch causes poor retrieval. OpenAI `text-embedding-3-large`, Cohere `embed-multilingual-v3.0` (important for Indian-language documents), or open-source Sentence-BERT/E5.

**Chunk size and overlap:** Start with 512–1,024 token chunks and 10–20% overlap. Tune based on your document types — legal contracts need smaller chunks (clauses are distinct), technical manuals need larger chunks (context crosses paragraphs).

**Retrieval depth (k):** Retrieve more than you think you need (top-15), then re-rank to top-5 for context assembly. This prevents the most relevant chunk being below the retrieval cutoff.

**Access control enforcement:** The query must only retrieve chunks the querying user is authorised to access. Implement metadata filters at the vector database level, not at the application level — filtering after retrieval risks leaking document awareness even if content is withheld.

**Freshness SLA:** How stale can documents be in the vector database? For compliance-sensitive content (policies, regulations), define a maximum staleness (e.g., 4 hours) and alert when the ingestion pipeline lags.

### Governance Requirements

- [ ] Document access controls mirrored in vector database metadata filters
- [ ] Document provenance logged for every retrieved chunk (source, version, date)
- [ ] Query log with user ID, query content (or hash), and retrieved source references
- [ ] Hallucination/groundedness monitoring: does the response reflect only retrieved content?
- [ ] System prompt explicitly instructs model to cite sources and decline unanswerable questions
- [ ] Regular freshness audits on the vector index (stale documents = wrong answers)

### When NOT to Use RAG

- When the answer requires real-time data (stock prices, live system status): use an API tool instead
- When documents are well-structured and SQL can answer the question: use text-to-SQL instead
- When the knowledge base is very small (< 50 documents): in-context loading may be simpler
- When documents require complex reasoning across multiple sections: consider agent-based approach instead

---

## Architecture 2: Structured Data AI — Text-to-SQL

Users ask questions in natural language; the AI translates to SQL, executes against a database, and returns the results as a human-readable answer. Replaces dashboards for exploratory analysis and empowers non-technical users to query enterprise data.

### The Pattern

```
User: "What were our top 5 products by revenue in Maharashtra last quarter?"
                              ↓
                   [Intent Classification]
                   (Is this a data question? Route accordingly)
                              ↓
                   [Schema Context Assembly]
                   (Inject relevant table schemas, column descriptions,
                    sample values, business glossary definitions)
                              ↓
                   [SQL Generation]
                   (LLM generates SQL with chain-of-thought)
                              ↓
                   [SQL Validation]
                   (Syntax check, safety check — no writes/drops,
                    query cost estimate, result set size limit)
                              ↓
                   [SQL Execution]
                   (Read-only credentials, timeout enforcement)
                              ↓
                   [Result Interpretation]
                   (LLM converts result set to natural language answer)
                              ↓
                   [Response + "Here's the SQL I ran" disclosure]
```

### Key Decisions

**Schema injection strategy:** The LLM cannot see your entire database schema — it's too large. Build a schema selector that injects only the tables relevant to the question (semantic search over table and column descriptions). Maintain a business glossary that maps business terms ("revenue," "active customer," "Maharashtra region") to their SQL equivalents.

**Safety enforcement — the hardest part:** The generated SQL must never modify data. Enforce this at multiple layers: the database credentials used for execution are read-only, the SQL is parsed for DML statements (INSERT, UPDATE, DELETE, DROP) before execution and rejected if found, and the LLM system prompt explicitly prohibits write operations.

**Error recovery:** Generated SQL often fails on the first attempt. Build a retry loop: execute → if error, send the error message back to the LLM with the failed SQL and ask it to correct → retry up to 3 times before escalating to a human.

**Transparency:** Always show the user the SQL that was executed alongside the result. This builds trust (users can verify the query is sensible), enables debugging (users can report "the SQL looks wrong"), and is the audit trail that compliance requires.

### Governance Requirements

- [ ] Read-only database credentials enforced at infrastructure level (not just prompt instruction)
- [ ] SQL whitelist/blacklist parser before execution
- [ ] Query logging with user ID, natural language query, generated SQL, and execution time
- [ ] Row-level security: ensure the database's own access controls apply to AI queries
- [ ] Maximum query execution time (prevent long-running queries from degrading the database)
- [ ] Result set size limit (prevent bulk data extraction via AI)

---

## Architecture 3: Document Intelligence Pipeline

Processes large volumes of documents — contracts, invoices, research papers, regulatory filings — extracting structured data, classifying content, and enabling downstream decision-making.

### The Pattern

```
Document Input (PDF, DOCX, image scan)
        ↓
[Document Pre-Processing]
(OCR if scanned, format normalisation, page segmentation)
        ↓
[Document Classification]
(What type of document is this? Contract / Invoice / Report / Other)
        ↓
┌───────────────────────────────────────────────────────┐
│  Per-Document-Type Extraction Pipeline                │
│                                                       │
│  Contract stream:                                     │
│    → Clause extraction → Risk classification →        │
│      Key term extraction → Obligation calendar        │
│                                                       │
│  Invoice stream:                                      │
│    → Line item extraction → PO matching →             │
│      Approval routing → Exception flagging            │
│                                                       │
│  Research stream:                                     │
│    → Abstract extraction → Citation extraction →      │
│      Key finding tagging → Summary generation         │
└───────────────────────────────────────────────────────┘
        ↓
[Structured Output + Confidence Scores]
(JSON with extracted fields and confidence for each)
        ↓
[Human Review Queue]
(Low-confidence extractions routed for human validation)
        ↓
[System of Record Update]
(Validated data written to downstream systems)
```

### Key Decisions

**OCR quality gates:** Scanned documents with poor OCR quality produce garbage extraction. Set a minimum OCR confidence threshold — documents below threshold are routed to human processing, not AI extraction.

**Confidence thresholds:** Every extracted field should have a confidence score. Define thresholds per field: high-confidence extractions go straight through, low-confidence extractions go to human review. Never auto-populate a system of record from a low-confidence extraction.

**Human-in-the-loop design:** Build the human review queue as a first-class feature, not an afterthought. What does the reviewer see? (Document, AI extraction, confidence score, similar past documents.) What can they do? (Confirm, correct, reject.) How is their correction fed back as training signal?

**Structured output enforcement:** Use JSON schema enforcement (tool calling or structured output mode in frontier models) to ensure extracted data fits the downstream system's schema. An extraction that doesn't match the schema is caught at the extraction stage, not discovered as a database error hours later.

### Governance Requirements

- [ ] Document classification logged with document ID, type, and confidence
- [ ] Extraction logged with every field, extracted value, and confidence score
- [ ] Human review queue with SLA (max time from low-confidence flag to human review)
- [ ] Correction-as-training-signal pipeline (with consent and data contract)
- [ ] PII handling: documents containing personal data must follow DPDPA protocols
- [ ] Retention policy: processed documents and extraction results have defined retention periods

---

## Architecture 4: AI-Augmented Customer Service

The agentic customer service system — handles end-to-end customer interactions, resolves what it can, escalates what it can't, and learns from every interaction.

### The Pattern

```
Customer Contact (Chat / Voice / Email)
        ↓
[Intent Classification + Sentiment Analysis]
(What does the customer want? How do they feel?)
        ↓
[Session Context Assembly]
(Customer history, recent transactions, open cases,
 account status — from CRM and system of record)
        ↓
[Agent Selection]
(Route to specialised handler based on intent:
 account query / billing / technical / complaint / other)
        ↓
┌──────────────────────────────────────────────┐
│  Specialised Handler Agent                   │
│  • Tools: CRM lookup, transaction query,     │
│    knowledge base search, action APIs        │
│  • Actions: Answer / Update account /        │
│    Process refund / Schedule callback        │
│  • Human escalation trigger: frustration     │
│    detected, complex issue, complaint        │
└──────────────────────────────────────────────┘
        ↓
[Resolution Check]
(Was the issue resolved? Customer confirmation or
 system verification)
        ↓
   ┌────┴────┐
Resolved  Not Resolved
   ↓           ↓
[Case Close]  [Human Agent Transfer]
[CSAT prompt]  (With full context, AI
               summary, and suggested
               resolution handed off)
```

### Key Decisions

**Escalation triggers are the most important design decision.** Define them explicitly: frustrated language detected, issue unresolved after N turns, specific issue types that always require a human (complaints, legal, medical), customer explicitly requests human. Don't leave escalation to the agent's judgment alone — define the policy and enforce it in the orchestration layer.

**Context handoff when escalating:** When transferring to a human agent, pass the complete context: full conversation transcript, AI's assessment of the issue, what the AI already tried, and a suggested resolution path. A human who receives "here's the full conversation and here's what I think is happening" can resolve the issue in 2 minutes. A human who receives a blind transfer and has to re-ask everything will take 15.

**Containment measurement:** The primary KPI for customer service AI is containment rate — what percentage of contacts are fully resolved without human intervention. Measure it per intent type, not just overall. An 80% overall containment rate that hides 10% containment for billing disputes is hiding a problem.

**Voice AI additional considerations:** If the channel is voice, add: speech-to-text quality gate (low-quality transcription → prefer chat channel), turn-taking management (don't interrupt, detect when customer is still speaking), and voice persona consistency (if you've named the AI "Priya," Priya sounds the same on every call).

### Governance Requirements

- [ ] Full conversation log with timestamps (DPDPA audit requirement)
- [ ] Escalation trigger log: every escalation with the trigger reason
- [ ] Sensitive action double-confirmation: refund processing, account changes confirmed before execution
- [ ] Customer disclosure: user must know they're interacting with AI at the start of the interaction
- [ ] CSAT collection on AI-resolved contacts (separate from human-resolved for attribution)
- [ ] Containment audit: monthly review of AI-resolved contacts to verify resolution quality

---

## Architecture 5: Sovereign / On-Premises AI (India-Specific)

For enterprises that cannot send data to external APIs — government agencies, defence, regulated financial institutions, healthcare with sensitive patient data. Full on-premises or private cloud deployment.

### The Pattern

```
┌─────────────────────────────────────────────────────────┐
│         PRIVATE INFRASTRUCTURE (India Data Centre /     │
│         NIC MeghRaj / Private Cloud)                    │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Open-Weight │  │  Vector DB   │  │  Embedding   │  │
│  │  Model       │  │  (Qdrant /   │  │  Model       │  │
│  │  (Llama 4 /  │  │   Weaviate   │  │  (self-      │  │
│  │   Mistral /  │  │   on-prem)   │  │   hosted)    │  │
│  │   Gemma)     │  └──────────────┘  └──────────────┘  │
│  └──────────────┘                                       │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Inference   │  │  LLMOps      │  │  Monitoring  │  │
│  │  Server      │  │  (MLflow +   │  │  (Grafana +  │  │
│  │  (vLLM)      │  │   LangSmith) │  │   Langfuse)  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │           Bhashini Integration                   │    │
│  │  (22 Indian languages: translation + ASR + TTS)  │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Key Decisions

**Model selection for sovereign deployment:** Llama 4 (Meta, open-weight), Mistral Large (European, self-hostable), Gemma 2 (Google, open-weight), and DeepSeek (open-weight, but evaluate supply chain risk for sensitive deployments). All can be run on-premises with NVIDIA A100/H100 GPUs or AMD MI300.

**GPU procurement reality check:** In India, GPU procurement through IndiaAI Mission compute access is available for eligible organisations. For private procurement, plan for 6–12 month lead times for H100 clusters. The MeghRaj Government Cloud (NIC) is offering GPU compute for government agencies.

**Bhashini for multilingual AI:** For government-facing or Bharat-facing deployments, Bhashini integration is not optional — it's the difference between an AI that works for English-speaking urban users and one that works for the country. Bhashini provides: ASR (automatic speech recognition) for 22 languages, translation, and TTS (text-to-speech). Self-hosted models fine-tuned on Bhashini outputs can be run entirely within the private perimeter.

**Performance reality:** On-premises models lag behind frontier models by 6–18 months on capability benchmarks. For most enterprise use cases (document processing, Q&A, code generation, summarisation), the gap is acceptable. For complex multi-step reasoning, the gap may matter — evaluate on your actual use cases.

### Governance Requirements (Indian Sovereign Context)

- [ ] All data remains within India's geographic boundary (NIC DC or India-region private cloud)
- [ ] DPDPA compliance: no personal data leaves the perimeter
- [ ] CERT-In compliance: security incident reporting obligations
- [ ] IndiaAI Safety Institute alignment when guidelines are published
- [ ] Bhashini integration roadmap documented if serving non-English users
- [ ] Air-gap procedures for the most sensitive deployments (model weights loaded offline)

---

## Architecture 6: AI Gateway — The Enterprise Control Plane

The AI gateway is not one of the above use-case architectures — it's the infrastructure that all of them sit behind. Every AI API call in the enterprise passes through it.

### The Pattern

```
Any AI Application
        ↓
┌───────────────────────────────────────────────────────┐
│                    AI GATEWAY                         │
│                                                       │
│  [Authentication & Authorisation]                     │
│  (Which application? Which user? What are they        │
│   allowed to call?)                                   │
│                                                       │
│  [Rate Limiting & Quota Enforcement]                  │
│  (Per-application, per-user, per-team budgets)        │
│                                                       │
│  [Model Router]                                       │
│  (Which model for this request? Cost optimisation?    │
│   Fallback routing? Load balancing?)                  │
│                                                       │
│  [Logging & Attribution]                              │
│  (Every request tagged with app, team, user, cost)    │
│                                                       │
│  [Input/Output Guardrails]                            │
│  (PII detection, harmful content, injection check)    │
│                                                       │
│  [Caching Layer]                                      │
│  (Semantic cache for high-volume repeated queries)    │
└───────────────────────────────────────────────────────┘
         │               │               │
   OpenAI API    Anthropic API    Azure OpenAI
   (US region)  (EU region)      (India region)
```

**Tools to implement:** LiteLLM (open-source, most widely adopted), Portkey (commercial with strong analytics), Helicone (logging-focused), Kong AI Gateway (enterprise, existing Kong users).

**This is the first thing to build.** Every other architecture in this document assumes an AI gateway exists. Without it, you have no cost attribution, no rate limiting, no central logging, no model routing. With it, every subsequent AI deployment inherits all of these capabilities automatically.

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): AWS AI Reference Architectures, Azure OpenAI Solution Architectures, Google Cloud GenAI Reference Architectures, LangChain RAG tutorial and production patterns, Weaviate Enterprise RAG Architecture Guide, Databricks LLM Architecture Best Practices 2026, vLLM production deployment guide, NIC MeghRaj Government Cloud documentation, IndiaAI Mission compute platform specifications, Bhashini API documentation.*