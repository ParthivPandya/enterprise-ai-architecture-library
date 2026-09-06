# AIEA® Series Guide
## AIEA-G01: AI Architecture in Financial Services (BFSI)
### Document Number: AIEA-G01 | Version 1.0 | 2026

---

## Preface

This document is an official AIEA Series Guide supplementing the core AIEA Standard. It provides sector-specific architecture guidance, regulatory compliance patterns, and technical reference designs for Banking, Financial Services, and Insurance (BFSI) enterprises.

In financial services, AI systems operate under extraordinary regulatory scrutiny, severe legal liability, and zero-tolerance expectations for fraud, bias, and unauthorized data leakage. This guide translates global banking regulations into concrete architectural controls and deployment patterns.

This guide MUST be read by Enterprise Architects, Chief Risk Officers (CROs), Financial Solution Architects, and Compliance Officers in the BFSI sector.

---

# Chapter 1: Regulatory Landscape & Compliance Architecture

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

## 1.1 Federal Reserve / OCC SR 11-7 Alignment (Model Risk Management)

All AI and ML models utilized in credit underwriting, risk forecasting, or market trading MUST comply with the **Three Lines of Defense** mandated by SR 11-7:

1. **First Line (Model Development & Architecture):** Delivery pods design, build, and benchmark models, documenting complete provenance in the **AI System Card**.
2. **Second Line (Model Validation & AIAB):** An independent Model Risk Management (MRM) team mathematically stress-tests models, auditing training data distributions, conceptual soundness, and out-of-time validation performance.
3. **Third Line (Internal Audit):** Independent verification that the AI architecture governance framework operates effectively.

## 1.2 EU AI Act Classification in BFSI

Under the EU AI Act (Annex III, Section 5), AI systems used to evaluate creditworthiness, establish credit scores, or price life/health insurance are classified as **High-Risk AI Systems**. These systems legally require:
- Complete logging of all algorithmic inputs, weights, and inference outputs for at least six months.
- Comprehensive technical documentation and risk mitigation procedures.
- Guaranteed human oversight capable of overriding or reversing automated credit rejections.

## 1.3 Indian Regulatory Context (RBI & SEBI Mandates)

Indian BFSI institutions MUST incorporate the following non-negotiable architectural constraints:
- **Financial Data Localisation (RBI 2018 Directive):** All end-to-end transaction data and customer identifiers processed by AI models MUST reside exclusively on servers physically located within India. Foreign multi-tenant cloud API inference is prohibited unless private, domestic Indian VPC instances are deployed.
- **Explainability for Adverse Actions (RBI Fair Practices Code):** Automated credit denials MUST provide unambiguous, human-readable explanations of the primary adverse factors.
- **SEBI Algorithmic Governance:** Algorithmic trading and automated investment advisory agents MUST maintain air-gapped kill-switches and audit trails preventing runaway market volatility.

---

# Chapter 2: Reference Architecture Patterns for Financial Services

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

## 2.1 Pattern 1: High-Throughput Streaming Fraud Detection

### Architectural Specifications:
- **Throughput & Latency SLA:** Processing $\ge 15,000$ transactions/sec with P99 inference latency $\le 35\text{ms}$.
- **Feature Store Integration:** Real-time lookup of customer behavioral aggregates (velocity of spend, geographic impossibility, device fingerprint shifts) via in-memory Redis cluster.
- **Model Topology:** Dual-stage inference:
  - *Stage 1 (Filter):* Ultra-fast tree ensemble (LightGBM/XGBoost) filtering 98% of benign transactions in $< 5\text{ms}$.
  - *Stage 2 (Deep Analysis):* Temporal Graph Neural Network (GNN) analyzing complex money-mule networks for suspicious multi-account flows.

## 2.2 Pattern 2: Explainable Credit Underwriting & Decisioning

### Architectural Specifications:
- **No Black-Box Neural Deployments:** Standalone raw LLM completions MUST NEVER directly approve or deny a loan application. Deep learning models MUST be paired with an explainability proxy.
- **SHAP Feature Attribution:** Every credit score is accompanied by local Shapley additive explanations (TreeSHAP) quantifying the exact positive or negative dollar impact of each input variable (debt-to-income ratio, credit history length, delinquent accounts).
- **Adverse Action Notice Engine:** If the algorithmic score falls below the approval threshold, a template engine synthesizes an adverse action disclosure citing the top 4 adverse factors, compliant with the US Equal Credit Opportunity Act (ECOA) and Indian Fair Lending guidelines.

---

# Chapter 3: Security & Customer Data Isolation

## 3.1 Zero-Retention Private VPC Hosting

Financial institutions MUST NOT route customer transaction history or PII through public multi-tenant SaaS model endpoints. Architectures MUST enforce:

1. **Private Endpoints (AWS PrivateLink / Azure Private Link):** Traffic between enterprise banking cores and model inference endpoints remains strictly on private, encrypted fiber backbones without traversing the public Internet.
2. **Cryptographic Tenant Isolation:** Vector database collections storing customer financial contracts MUST employ tenant-specific Customer Managed Keys (CMK) managed in enterprise Hardware Security Modules (HSMs).
3. **Automated Token Masking:** PCI-DSS Cardholder Data (PAN, CVV) and Indian Aadhaar numbers MUST be irreversibly tokenized or redacted by ingress gateway filters before prompts reach reasoning layers.

---

*AIEA Series Guide AIEA-G01: AI Architecture in Financial Services. Document AIEA-G01, Version 1.0, 2026.*  
*AI Enterprise Architecture Forum (AIEAF).*
