# AIEA Series Guide
## AIEA-G01: AI Architecture in Financial Services (BFSI)
### Document Number: AIEA-G01 | Version 1.0 | 2026

---

## Preface

This document is an independent AIEA Series Guide supplementing the core AIEA Reference Framework. It provides sector-specific architecture guidance, regulatory compliance patterns, and technical reference designs for Banking, Financial Services, and Insurance (BFSI) enterprises.

In financial services, AI systems operate under extraordinary regulatory scrutiny, severe legal liability, and zero-tolerance expectations for fraud, bias, and unauthorized data leakage. This guide translates global banking regulations into concrete architectural controls and deployment patterns.

This guide MUST be read by Enterprise Architects, Chief Risk Officers (CROs), Financial Solution Architects, and Compliance Officers in the BFSI sector.

---

## Chapter 1: Regulatory Landscape & Compliance Architecture

Financial institutions must navigate an overlapping web of banking guidelines and AI-specific legislation:

```
┌─────────────────────────────────────────────────────────────────────────┐
│               BFSI AI REGULATORY COMPLIANCE ARCHITECTURE                │
├────────────────────────────────┬────────────────────────────────────────┤
│ GLOBAL / US STANDARDS          │ INDIAN REGULATORY JURISDICTION         │
│ • Fed / OCC SR 11-7            │ • RBI Master Directions on IT & AI Gov │
│   (Model Risk Management - MRM)│ • SEBI Circulars on Algorithmic Systems│
│ • EU AI Act Annex III          │ • India DPDPA (2023) / Financial PII   │
│   (Credit scoring = High Risk) │   Localisation (RBI Circular 2018)     │
│ • PCI-DSS v4.0 (Payment Data)  │ • IRDAI Guidelines for InsurTech AI    │
└────────────────────────────────┴────────────────────────────────────────┘
```

### 1.1 Federal Reserve / OCC SR 11-7 Alignment (Model Risk Management)

All AI and ML models utilized in credit underwriting, risk forecasting, or market trading MUST comply with the **Three Lines of Defense** mandated by SR 11-7:

1. **First Line (Model Development & Architecture):** Delivery pods design, build, and benchmark models, documenting complete provenance in the **AI System Card**.
2. **Second Line (Model Validation & AIAB):** An independent Model Risk Management (MRM) team mathematically stress-tests models, auditing training data distributions, conceptual soundness, and out-of-time validation performance.
3. **Third Line (Internal Audit):** Independent verification that the AI architecture governance framework operates effectively.

### 1.2 EU AI Act Classification in BFSI

Under the EU AI Act, selected systems used to evaluate creditworthiness or establish credit scores, and selected risk-assessment/pricing systems for life and health insurance, can be classified as **high-risk**, subject to the Act's definitions, exclusions, organisation role, and applicable commencement date. Relevant evidence can include:
- Automatically generated logs appropriate to the system's purpose; this does not mean recording model weights for every inference.
- Technical documentation, risk management, data governance, accuracy, robustness, and cybersecurity evidence.
- Human-oversight measures appropriate to the system and decision process.

Confirm the current text and application timeline against [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).

### 1.3 Indian Regulatory Context (RBI & SEBI Mandates)

Indian BFSI institutions must determine which RBI, SEBI, IRDAI, payment-system, outsourcing, cybersecurity, and records requirements apply to the regulated entity and workload:
- **Payment System Data Storage:** The RBI's 2018 direction requires covered payment-system data to be stored in India. The RBI FAQ permits processing abroad provided the data is deleted from foreign systems and brought back to India within the specified period; it is therefore inaccurate to treat every foreign processing service as universally prohibited. See the [RBI direction](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) and [FAQ](https://www.rbi.org.in/scripts/FAQView.aspx?Id=117).
- **Adverse Decisions:** Architecture SHOULD preserve the decision factors, policy basis, notices, and human-review route required by the applicable product, fair-practices, consumer-protection, and credit-information rules.
- **Algorithmic Markets:** Trading and advisory systems SHOULD implement deterministic limits, authorised kill controls, evidence retention, and supervision appropriate to the applicable SEBI framework. Do not describe a control as legally mandatory without citing the specific circular or regulation.

---

## Chapter 2: Reference Architecture Patterns for Financial Services

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 BFSI REFERENCE ARCHITECTURE TOPOLOGY                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PATTERN 1: REAL-TIME TRANSACTION FRAUD DETECTION (STREAMING)           │
│  Transaction Event ──> Kafka Bus ──> In-Memory Feature Store (Feast)    │
│                                           │                             │
│                                           ▼                             │
│                        Graph Neural Net + XGBoost Ensemble              │
│                        (Inference SLA: < 35ms @ P99)                    │
│                                           │                             │
│                                           ▼                             │
│                        Verdict: Approve / Flag / Step-Up Auth           │
├─────────────────────────────────────────────────────────────────────────┤
│  PATTERN 2: GOVERNED CREDIT UNDERWRITING (BATCH / HYBRID)               │
│  Loan Application ──> Document Extraction (OCR / Document AI)           │
│                                │                                        │
│                                ▼                                        │
│  Deterministic Policy Rules Engine (Hard KYC / Income Checks)           │
│                                │                                        │
│                                ▼                                        │
│  Credit Risk Ensemble Model (Proprietary LightGBM / Neural Net)         │
│                                │                                        │
│                                ▼                                        │
│  Local Explainability Layer (TreeSHAP Feature Attribution Engine)       │
│                                │                                        │
│                                ▼                                        │
│  Adverse Action Generator ──> Credit Officer Review Queue (HITL)        │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Pattern 1: High-Throughput Streaming Fraud Detection

#### Architectural Specifications:
- **Throughput & Latency SLA:** Processing $\ge 15,000$ transactions/sec with P99 inference latency $\le 35\text{ms}$.
- **Feature Store Integration:** Real-time lookup of customer behavioral aggregates (velocity of spend, geographic impossibility, device fingerprint shifts) via in-memory Redis cluster.
- **Model Topology:** Dual-stage inference:
  - *Stage 1 (Filter):* Ultra-fast tree ensemble (LightGBM/XGBoost) filtering 98% of benign transactions in $< 5\text{ms}$.
  - *Stage 2 (Deep Analysis):* Temporal Graph Neural Network (GNN) analyzing complex money-mule networks for suspicious multi-account flows.

### 2.2 Pattern 2: Explainable Credit Underwriting & Decisioning

#### Architectural Specifications:
- **No Black-Box Neural Deployments:** Standalone raw LLM completions MUST NEVER directly approve or deny a loan application. Deep learning models MUST be paired with an explainability proxy.
- **SHAP Feature Attribution:** Every credit score is accompanied by local Shapley additive explanations (TreeSHAP) quantifying the exact positive or negative dollar impact of each input variable (debt-to-income ratio, credit history length, delinquent accounts).
- **Adverse Action Notice Engine:** If the algorithmic score falls below the approval threshold, a template engine synthesizes an adverse action disclosure citing the top 4 adverse factors, compliant with the US Equal Credit Opportunity Act (ECOA) and Indian Fair Lending guidelines.

---

## Chapter 3: Security & Customer Data Isolation

### 3.1 Zero-Retention Private VPC Hosting

Financial institutions MUST NOT route customer transaction history or PII through public multi-tenant SaaS model endpoints. Architectures MUST enforce:

1. **Private Endpoints (AWS PrivateLink / Azure Private Link):** Traffic between enterprise banking cores and model inference endpoints remains strictly on private, encrypted fiber backbones without traversing the public Internet.
2. **Cryptographic Tenant Isolation:** Vector database collections storing customer financial contracts MUST employ tenant-specific Customer Managed Keys (CMK) managed in enterprise Hardware Security Modules (HSMs).
3. **Automated Token Masking:** PCI-DSS Cardholder Data (PAN, CVV) and Indian Aadhaar numbers MUST be irreversibly tokenized or redacted by ingress gateway filters before prompts reach reasoning layers.

---

*AIEA Series Guide AIEA-G01: AI Architecture in Financial Services. Document AIEA-G01, Version 1.0, 2026.*  
*AIEA Reference Library.*
