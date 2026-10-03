# Enterprise AI Metamodel Catalog & ArchiMate 3.2 Mapping Guide
## Practitioner Toolkit & Modeling Reference
### Document Ref: AIEA-TK-02 | Version 1.0 | 2026

---

## Executive Overview

Enterprise Architecture relies on a shared semantic model. When architects model traditional systems, they map Business Actors, Application Services, Data Objects, and Technology Nodes. When modeling Artificial Intelligence, classical metamodels break down because they lack constructs for non-deterministic model checkpoints, token gateways, vector embeddings, prompt templates, and autonomous agent loops.

This toolkit defines the **AIEA Core AI Metamodel** and provides an independent **ArchiMate 3.2 mapping guide** for modelling AI-enabled architectures in enterprise tools. It is not an official publication of, or endorsed mapping from, The Open Group. Validate notation and exchange behaviour against the current ArchiMate specification and the selected modelling tool.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    THE AIEA CORE ENTERPRISE METAMODEL                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  BUSINESS LAYER                                                         │
│  ┌────────────────────┐            ┌────────────────────┐               │
│  │Business Capability │ ─────────> │   AI Use Case      │               │
│  └────────────────────┘            └─────────┬──────────┘               │
│                                              │                          │
│  APPLICATION LAYER                           ▼                          │
│  ┌────────────────────┐            ┌────────────────────┐               │
│  │ AI System (System  │ ─────────> │ AI Building Block  │               │
│  │ Card Accountable)  │            │ (AI-ABB: RAG/Agent)│               │
│  └─────────┬──────────┘            └─────────┬──────────┘               │
│            │                                 │                          │
│  DATA & SEMANTIC LAYER                       ▼                          │
│  ┌────────────────────┐            ┌────────────────────┐               │
│  │  Data Contract     │ ─────────> │ Vector Collection  │               │
│  │  (Source Lineage)  │            │ (Chunks / Embeds)  │               │
│  └────────────────────┘            └─────────┬──────────┘               │
│                                              │                          │
│  TECHNOLOGY LAYER                            ▼                          │
│  ┌────────────────────┐            ┌────────────────────┐               │
│  │ Accelerated Node   │ ─────────> │ Model Checkpoint   │               │
│  │ (GPU Cluster/VPC)  │            │ (vLLM / SaaS API)  │               │
│  └────────────────────┘            └────────────────────┘               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Chapter 1: Core AI Metamodel Entity Dictionary

The AIEA Metamodel establishes ten normative entities that MUST be tracked within the Enterprise Architecture Repository:

| Entity Name | Layer | Definition | Mandatory Attributes |
|---|---|---|---|
| **AI Use Case** | Business | Business operational scenario enabled by AI | `use_case_id`, `business_kpi`, `roi_estimate`, `risk_tier` |
| **AI System** | Application | Governed production software system containing AI | `system_id`, `system_owner`, `system_card_uri`, `lifecycle_status` |
| **AI-ABB** | Application | Architecture Building Block (Capability specification) | `abb_id`, `pattern_type` (RAG, Agent, Gateway), `sla_latency` |
| **AI-SBB** | Application | Solution Building Block (Concrete software component) | `sbb_id`, `vendor_platform` (e.g., Qdrant, LiteLLM), `version` |
| **Model Checkpoint** | Technology | Specific weights and version of an ML/LLM model | `model_name`, `provider`, `context_window`, `license_type` |
| **Prompt Template** | Application | Version-controlled prompt instructions and delimiters | `prompt_id`, `version`, `commit_hash`, `guardrail_profile` |
| **Vector Collection** | Data | Indexed embedding store of chunked enterprise data | `collection_name`, `embedding_model`, `dimensions`, `distance_metric` |
| **Data Contract** | Data | Binding specification between data source and AI | `contract_id`, `upstream_owner`, `refresh_sla`, `dpdpa_consent_basis` |
| **Agent Tool** | Application | Programmatic API or sandbox callable by an agent | `tool_id`, `openapi_spec_uri`, `reversibility` (Reversible/Irreversible) |
| **Compute Node** | Technology | Physical or virtual accelerated hardware cluster | `node_id`, `gpu_type` (e.g., H100), `memory_vram`, `hosting_region` |

---

## Chapter 2: ArchiMate 3.2 Notation Mapping Specification

Architects modeling AI architectures MUST apply the following standardized ArchiMate element types and stereotypes:

```
┌───────────────────────┬──────────────────────────┬──────────────────────┐
│ AIEA Entity           │ ArchiMate 3.2 Base Type  │ Stereotype Tag       │
├───────────────────────┼──────────────────────────┼──────────────────────┤
│ AI Use Case           │ Business Service         │ «AI_UseCase»         │
│ AI System             │ Application Component    │ «AI_System»          │
│ AI Gateway            │ Application Interface    │ «AI_Gateway»         │
│ Autonomous Agent      │ Application Component    │ «Agentic_System»     │
│ Model Checkpoint      │ Technology Artifact      │ «Model_Checkpoint»   │
│ Vector Database       │ Data Object              │ «Vector_Store»       │
│ Prompt Template       │ Application Artifact     │ «Prompt_Template»    │
│ Data Contract         │ Contract                 │ «Data_Contract»      │
│ GPU Node / Cluster    │ Device / Node            │ «Accelerated_Compute»│
│ Guardrail Filter      │ Application Service      │ «Safety_Guardrail»   │
└───────────────────────┴──────────────────────────┴──────────────────────┘
```

### Standard Relationship Types:
- `AI System` **realizes** `AI Use Case`
- `AI System` **composed of** `AI-ABB`
- `AI-ABB` **assigned to** `AI-SBB`
- `AI-SBB (Gateway)` **accesses** `Model Checkpoint`
- `AI-SBB (RAG)` **reads** `Vector Collection`
- `Vector Collection` **derived from** `Data Object` via `Data Contract`
- `Model Checkpoint` **deployed on** `Compute Node`

---

## Chapter 3: Enterprise Architecture Repository JSON Schema

To integrate AI systems into programmatic architecture repositories (CMDBs / EA catalogs), systems MUST emit metadata conforming to the **AIEA Metamodel JSON Schema**:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AIEA_System_Metamodel_Record",
  "type": "object",
  "required": ["system_id", "system_name", "risk_tier", "system_owner", "architecture_pattern"],
  "properties": {
    "system_id": { "type": "string", "pattern": "^SYS-AI-[0-9]{4}$" },
    "system_name": { "type": "string" },
    "risk_tier": { "type": "string", "enum": ["Prohibited", "High", "Significant", "Limited", "Minimal"] },
    "system_owner": { "type": "string" },
    "architecture_pattern": { "type": "string", "enum": ["RAG", "Multi-Agent", "Fine-Tuning", "Predictive-ML", "Classifier"] },
    "models_consumed": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": { "type": "string" },
          "provider": { "type": "string" },
          "hosting": { "type": "string", "enum": ["Public-SaaS", "Private-VPC", "Air-Gapped-OnPrem"] }
        }
      }
    },
    "data_contracts_active": { "type": "array", "items": { "type": "string" } },
    "gateway_routed": { "type": "boolean", "default": true },
    "last_architecture_review_date": { "type": "string", "format": "date" }
  }
}
```

---

*AIEA Toolkit AIEA-TK-02: Enterprise AI Metamodel Catalog. Version 1.0, 2026.*  
*AIEA Reference Library.*
