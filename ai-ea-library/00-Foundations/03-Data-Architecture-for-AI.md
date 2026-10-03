# Data Architecture for AI

> *The single most consistent predictor of AI project failure is not the model. It's the data. Bad data, inaccessible data, ungoverned data — these kill more AI projects than every technical problem combined. This chapter covers how to build the data infrastructure that makes AI actually work.*

> **Related:** [01-How-LLMs-Work.md](01-How-LLMs-Work.md) | [../03-EA-Practice/05-LLMOps.md](../03-EA-Practice/05-LLMOps.md) | [../01-AI-Governance/01-FinOps.md](../01-AI-Governance/01-FinOps.md)

---

## Why Data Architecture Is the Bottleneck

A 2025 Gartner survey found that poor data quality costs organisations an average of $12.9 million per year. For AI specifically, the consequences compound: a model trained on inaccurate data doesn't just produce inaccurate outputs — it does so confidently, at scale, with no built-in warning mechanism.

The phrase "garbage in, garbage out" has been true of computing since the 1950s. With AI it becomes "garbage in, convincingly-articulated garbage out at 10,000 requests per hour."

There's a second, subtler problem: most enterprise data was collected for reporting and transaction processing — not for model training or real-time AI inference. Moving from "data we have" to "data AI can use" requires architectural work that most organisations underestimate by a factor of three to five.

Three specific gaps show up in almost every enterprise AI readiness assessment:

**Gap 1: Data silos.** The customer data is in Salesforce. The transaction data is in the data warehouse. The contract data is in SharePoint. The support ticket data is in Zendesk. An AI system that needs to understand the full customer context has to cross all four boundaries — and in most organisations, those boundaries aren't cleanly crossed.

**Gap 2: Data quality.** A field that's "good enough" for a monthly report — where someone will notice if the revenue number looks wrong — is often not good enough for a training dataset where individual errors are invisible but aggregate patterns are learned and amplified.

**Gap 3: Data lineage.** NIST AI RMF MAP function, DPDPA DPIA, ISO 42001 — all of them require you to document where your training data came from, how it was transformed, and what consent or lawful basis exists for its use. Most organisations don't have this documentation because they never needed it before.

---

## The AI Data Stack

Unlike traditional BI data architecture (sources → ETL → warehouse → reports), AI data architecture has additional layers:

```
┌──────────────────────────────────────────────────────┐
│              OPERATIONAL DATA SOURCES                │
│  (CRM, ERP, HRMS, Support, Logs, Documents, APIs)   │
└──────────────────────────┬───────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────┐
│              DATA INGESTION + QUALITY                │
│  (Validation, deduplication, PII detection,          │
│   lineage tagging, consent verification)             │
└──────────────────────────┬───────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
┌────────▼────────┐ ┌──────▼──────┐ ┌───────▼────────┐
│  DATA LAKE /    │ │  FEATURE    │ │  VECTOR        │
│  LAKEHOUSE      │ │  STORE      │ │  DATABASE      │
│  (raw + curated)│ │  (ML feats) │ │  (embeddings)  │
└────────┬────────┘ └──────┬──────┘ └───────┬────────┘
         │                 │                 │
┌────────▼─────────────────▼─────────────────▼────────┐
│              AI / ML WORKLOADS                       │
│  (Training, Fine-tuning, RAG inference, Evaluation)  │
└──────────────────────────────────────────────────────┘
```

Each layer has specific architectural requirements that are distinct from traditional data architecture.

---

## The Data Lake / Lakehouse

The data lake is where raw data lands before transformation. The lakehouse architecture — pioneered by Databricks and adopted by AWS (S3 + Glue), Azure (ADLS + Synapse), and Google (GCS + BigQuery) — adds a table format layer (Delta Lake, Apache Iceberg, Apache Hudi) on top of object storage, giving you ACID transactions, schema evolution, and time travel on data lake economics.

**Why AI needs a lakehouse instead of a warehouse:**

Traditional data warehouses enforce schema at write time. AI workloads often need raw, unstructured data — images, documents, audio, text logs — that warehouses can't store. They also need historical snapshots for training (what did our data look like 18 months ago?), time-travel that lakehouses provide but warehouses typically don't.

**The three-zone pattern for AI data lakes:**

| Zone | What Goes Here | Governance |
|---|---|---|
| **Bronze (Raw)** | Exactly as received from source — no transformation. Timestamped. Immutable. | Highest access restriction; contains raw PII |
| **Silver (Curated)** | Cleaned, deduplicated, validated, PII removed or pseudonymised. Schema enforced. | Standard data governance controls |
| **Gold (Feature-Ready)** | Derived features, aggregations, embeddings, domain-specific transforms. Optimised for AI consumption. | Documented lineage; approved for training use |

**The lineage requirement:** Every dataset used for AI training must have traceable lineage from Gold back to Bronze, including every transformation applied and every consent or lawful basis decision made. This is not optional under DPDPA, NIST AI RMF, or ISO 42001. Tools: Apache Atlas, OpenLineage, Marquez, or cloud-native catalogues (AWS Glue Data Catalog, Azure Purview).

**Data quality gates:** Before data advances from Bronze to Silver, it must pass automated quality checks:
- Completeness: critical fields not null above threshold
- Freshness: data arrived within expected SLA
- Accuracy: statistical distributions within expected ranges
- Consistency: joins to reference data succeed at expected rates
- PII detection: fields containing personal data flagged for governance treatment

Tools: Great Expectations (open-source, the most widely adopted), dbt tests (for SQL-based pipelines), Soda (commercial, enterprise support).

---

## Feature Stores

A feature store is shared infrastructure for managing machine learning features — the derived attributes that models use to make predictions. Without a feature store, every team that builds an ML model reinvents the same feature engineering logic. With one, features computed once are reused across many models.

**The problem a feature store solves:**

Imagine three teams each building AI models that use customer spending patterns as a feature. Without a feature store:
- Team A computes "average monthly spend over 90 days" in their own pipeline
- Team B computes "average monthly spend over 90 days" slightly differently in theirs
- Team C uses a third definition

Each team's feature is subtly different. Models trained on these features aren't comparable. When a business analyst asks "why did Team A's model recommend differently from Team B's?", part of the answer is "because they're using different versions of the same feature." This is called feature drift, and it's endemic in enterprises without feature stores.

**The feature store architecture:**

```
Data Sources → Feature Engineering → Feature Store
                                           │
                          ┌────────────────┼───────────────────┐
                          │                │                   │
                   Offline Store    Online Store        Feature Registry
                   (historical      (low-latency        (metadata, lineage,
                    training)        inference)          documentation)
```

**Offline store:** Historical feature data for model training. Large scale, batch access, low latency not required. Typically built on the data lakehouse.

**Online store:** Current-state feature values for real-time inference. Millisecond latency required. Typically a fast key-value store (Redis, DynamoDB, Bigtable). The online store is populated by streaming pipelines that keep it current.

**Feature registry:** Documentation of every feature — its definition, owner, calculation logic, lineage, expected range, and which models use it. This is what prevents the feature drift problem: when Team B wants to use "average monthly spend," they look it up in the registry, find Team A's definition, and reuse it rather than reinventing.

**Tools:** Feast (open-source, most widely adopted), Tecton (commercial, enterprise support), Hopsworks (open-source), AWS SageMaker Feature Store, Azure Machine Learning Feature Store, Databricks Feature Store.

**When you need a feature store:** If you have more than 3–4 ML models in production sharing overlapping features, or if you're building real-time ML (fraud detection, recommendation engines, personalisation), a feature store pays for itself quickly.

**When you don't (yet):** For LLM-based applications using RAG, a feature store is generally not required. RAG retrieves documents rather than structured features. The feature store becomes relevant when you're building hybrid systems that combine structured ML models with LLMs.

---

## Vector Databases

The vector database is the infrastructure layer that makes RAG possible at scale. When a document is processed for RAG, it's converted into a vector embedding — a mathematical representation of its semantic meaning. The vector database stores these embeddings and enables similarity search: "find me the documents whose meaning is most similar to this query."

**How vector similarity search works:**

Every document chunk is converted to a vector of 768–3,072 numbers (the dimension depends on the embedding model). Similar documents have similar vectors — their vectors point in similar directions in high-dimensional space. A query is converted to a vector and the database finds the documents whose vectors are closest (by cosine similarity or dot product).

The magic: "closest in vector space" means "most semantically similar" — not just keyword-matching, but meaning-matching. A search for "patient discharge timing" will retrieve documents about "hospital bed management" and "length of stay planning" because they're semantically related, even if they share no keywords.

**Choosing a vector database:**

| Option | Best For | Considerations |
|---|---|---|
| **pgvector** (PostgreSQL extension) | Teams already on PostgreSQL; moderate scale | Free; uses existing infrastructure; not optimised for very high scale |
| **Chroma** | Development and small-scale production | Open-source; simple API; limited production features |
| **Weaviate** | Hybrid search (vector + keyword); enterprise | Open-source + cloud; strong filtering capabilities |
| **Qdrant** | High-performance production; Rust-based | Open-source + cloud; excellent performance benchmarks |
| **Pinecone** | Fully managed; fastest time-to-production | Commercial only; no self-hosting; higher cost |
| **Milvus** | Very large scale (billions of vectors) | Open-source; complex to operate; highest throughput |
| **Azure AI Search** | Azure ecosystem | Managed; integrates with Azure OpenAI; built-in access control |
| **Amazon OpenSearch** | AWS ecosystem | Managed; familiar to AWS teams; reasonable performance |

**The decision framework:**
- Already on PostgreSQL and scale is moderate? → pgvector. Don't add a new system if you don't need to.
- Need fully managed with minimal ops? → Pinecone or Azure AI Search (if on Azure).
- Need self-hosted for data residency (India, EU)? → Weaviate, Qdrant, or Milvus.
- Billions of vectors? → Milvus or Qdrant.
- Just starting and want simplicity? → Chroma for development, then migrate to production option.

**The enterprise RAG architecture beyond the vector database:**

The vector database is one component. Production RAG has more moving parts:

```
Documents → Chunking Strategy → Embedding Model → Vector DB
                ↑                                      ↓
         (chunk size,                          Retrieval (top-k,
          overlap,                              filters, re-ranking)
          metadata)                                    ↓
                                            LLM with Context
                                                    ↓
                                            Output + Citation
```

**Chunking strategy matters more than most teams realise.** If your chunks are too small, each chunk lacks enough context to be useful — the model gets fragments without meaning. If chunks are too large, retrieval becomes imprecise — you retrieve a large section when you only needed a paragraph. Common starting points:
- Recursive character splitting: 512–1,024 tokens per chunk, 10–20% overlap
- Semantic chunking: split at natural semantic boundaries (paragraphs, sections) rather than fixed token counts
- Document-specific chunking: contracts split by clause, research papers by section, code by function

**Re-ranking:** The top-k retrieved chunks from vector search are not necessarily the top-k most useful. A re-ranker model (cross-encoder) takes the query and each candidate chunk and scores them for relevance more precisely than vector similarity alone. Re-ranking improves answer quality at the cost of latency. For RAG applications where accuracy matters more than speed, re-ranking is worth it.

---

## Data Quality for AI: A Higher Bar Than You're Used To

"Good enough for reporting" is not good enough for model training. Here's why the bar is higher:

**Bias amplification.** A 1% systematic bias in training data (e.g., a field that's consistently miscoded for a demographic group) becomes a 1% systematic bias in model outputs — applied at inference-time scale across every prediction the model makes. The model doesn't know to compensate. It learns the pattern, including the error.

**Distribution matters, not just accuracy.** A training dataset where 95% of examples are one category and 5% are another will produce a model that's very good at predicting the majority category and poor at the minority — regardless of overall accuracy. For fraud detection (1% of transactions are fraud), credit scoring (minority of applicants default), or medical diagnosis (rare conditions), this is dangerous.

**Freshness matters asymmetrically.** For some models, stale training data is a minor quality issue. For others — fraud detection, demand forecasting, recommendation engines — stale training data produces models that are actively wrong because the patterns have changed.

**The five dimensions of AI data quality:**

| Dimension | What It Means for AI | How to Measure |
|---|---|---|
| **Completeness** | Missing values in features the model relies on | % null for each training feature |
| **Accuracy** | Values reflect reality | Sample validation against source records |
| **Consistency** | Same concept represented uniformly across sources | Reconciliation to reference data |
| **Freshness** | Data age relative to the patterns being modelled | Max age of training examples |
| **Representativeness** | Distribution matches the deployment distribution | KL divergence between train and production distributions |

**The practical implication for architects:** Data quality assessment is a gate, not an assumption. Before any AI use case progresses from concept to development, run a data quality assessment against these five dimensions for the proposed training data. A use case with poor representativeness should be redesigned (acquire more diverse data) or scoped down (restrict to the population where data is representative) before a single model is trained.

---

## Data Contracts: The Governance Layer Nobody Talks About

A data contract is a formal agreement between the team that produces data and the teams that consume it — specifying schema, quality standards, freshness SLAs, and the process for managing changes.

In traditional data pipelines, data contracts are an emerging good practice. For AI pipelines, they are closer to essential.

Why? Because when a source system changes a field — renames a column, changes a data type, starts populating a previously empty field differently — an AI model trained on the old schema breaks in production in ways that may not be immediately obvious. The model doesn't throw an error. It starts making worse predictions, and nobody knows why until someone traces the degradation back to the schema change that happened six weeks ago.

**A minimal data contract covers:**

```yaml
# Example: Customer Transaction Feature Contract
contract_name: customer_transaction_features
version: 2.1
owner: data-engineering@company.com
consumers:
  - fraud-detection-model
  - credit-risk-model

schema:
  - name: transaction_amount_inr
    type: FLOAT
    nullable: false
    description: "Transaction value in Indian Rupees, positive for debit"
    
  - name: merchant_category_code
    type: STRING
    nullable: true
    valid_values: [documented MCC list]

quality_slos:
  completeness: ">= 99.5% non-null for transaction_amount_inr"
  freshness: "<= 15 minutes lag from transaction settlement"
  accuracy: "reconciles to core banking within 0.01% of transaction volume"

change_process:
  breaking_changes: "30 days notice + joint review with all consumers"
  non_breaking_changes: "7 days notice"
  
pii_classification: CONTAINS_PII
lawful_basis: "Contract (transaction processing) + DPDPA Schedule I"
retention: "7 years (tax compliance requirement)"
```

**Tools for data contracts:** Great Expectations (quality assertions), dbt contracts (schema enforcement), Schemata (dedicated data contract platform), custom YAML in the data catalogue.

**The governance payoff:** When every AI system's training and inference data is covered by a data contract, you have the documentation you need for NIST AI RMF MAP, DPDPA DPIA, and ISO 42001. The data lineage is documented. The quality standards are committed. The change process prevents silent schema drift. This is governance infrastructure that pays dividends across every AI programme.

---

## The Data Flywheel: Turning AI Outputs Into Future Training Data

One of the most powerful patterns in AI data architecture is the data flywheel: AI-generated outputs become training data that improves future AI. It's how Google's search ranking, Amazon's recommendations, and TikTok's feed algorithm continuously improve without proportional increases in human labelling effort.

```
User Interaction → AI Output → User Feedback Signal
                                        ↓
                              Training Data Pipeline
                                        ↓
                              Improved Model → Better Output
                                        ↓
                              More User Interactions
```

**In enterprise practice:**

A customer service AI resolves a ticket. The customer rates the resolution. A human agent reviews and corrects the resolution if needed. Both the rating and any correction become training signal for the next model version.

A document summarisation AI produces a summary. The user edits parts of it before sending. The edits identify where the AI's judgment didn't match the user's — training signal for prompt refinement or fine-tuning.

**The governance requirement that trips up the flywheel:** Using user interactions as training data typically requires consent under DPDPA (if personal data is involved) or at minimum a clear description in the privacy notice. Build this requirement into the data flywheel architecture from the beginning — retroactively obtaining consent for data already collected is expensive and often impossible.

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): Gartner Data Quality Cost Report 2025, Databricks Lakehouse Architecture Guide 2026, Feast Feature Store documentation, Weaviate and Qdrant technical documentation, Pinecone Enterprise RAG Guide, AWS SageMaker Feature Store documentation, Great Expectations data quality framework, dbt Data Contracts guide, Atlan Data Lineage for AI 2025, Analyticsvidhya RAG Architecture Patterns 2026, NIST AI RMF MAP function data requirements.*