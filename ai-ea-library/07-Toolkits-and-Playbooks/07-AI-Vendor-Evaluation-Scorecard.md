# AI Vendor Evaluation Scorecard Toolkit
## Practitioner Toolkit & Diagnostic Playbook
### Document Ref: AIEA-TK-07 | Version 1.0 | 2026

---

## Executive Overview

Evaluating AI vendors (whether for foundation models, MLOps platforms, or AI applications) requires a fundamentally different lens than traditional SaaS procurement. The risks of lock-in, data exposure, and model deprecation are significantly higher, while feature differentiation is often ephemeral.

This toolkit provides a structured, quantitative scorecard for evaluating AI vendors across six critical dimensions. It is designed to be used by Enterprise Architects and Procurement teams to cut through marketing claims and establish objective comparisons.

---

## The AI Vendor Evaluation Scorecard

Evaluate each vendor across the following six dimensions. Score each criterion from 1 (Unacceptable/Missing) to 5 (Industry Leading).

### Dimension 1: Data Sovereignty & Privacy (Weight: 25%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Training Data Use** | Vendor uses customer data for base model training | Vendor requires opt-out for training use | Explicit, default zero-data-retention guarantee | |
| **Data Residency** | Global routing; no geographic guarantees | Regional hosting (e.g., EU, US, APAC) | Dedicated single-tenant sovereign hosting available | |
| **Encryption & Keys** | Standard transit/rest encryption | Customer Managed Keys (CMK) supported | Confidential computing enclaves (e.g., Nitro) | |
| **Regulatory Compliance** | Basic SOC2 | GDPR, HIPAA compliant | ISO 42001, EU AI Act ready, sector-specific certs | |

### Dimension 2: Architectural Flexibility & Lock-in (Weight: 20%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Model Independence** | Proprietary models only; closed ecosystem | Multi-model routing supported | True AI Gateway; BYOM (Bring Your Own Model) | |
| **Portability** | Proprietary APIs and integrations only | Standard REST/GraphQL endpoints | Native support for standard frameworks (LangChain/LlamaIndex) | |
| **Fine-tuning Portability** | Fine-tuned weights locked to vendor platform | Can export adapter weights (LoRA) | Full weight export for deployment anywhere | |
| **Exit Strategy** | Difficult data extraction; proprietary formats | Bulk data export available | Automated migration tools; open data formats | |

### Dimension 3: Safety, Guardrails & Quality (Weight: 20%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Input/Output Filtering** | Basic keyword blocking | Configurable safety thresholds | Advanced intent analysis, PII detection, custom guardrails | |
| **Model Evaluation** | No published evaluation methodology | Standard benchmark scores provided | Transparent eval methodology, red-teaming reports shared | |
| **Explainability** | Black box | Basic attribution | Advanced XAI tools, token-level confidence scores | |
| **Copyright Indemnification** | None | Capped liability for IP infringement | Uncapped IP indemnification for generated content | |

### Dimension 4: Total Cost of Ownership & FinOps (Weight: 15%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Pricing Predictability** | Variable token pricing only; unconstrained | Provisioned throughput options | Guaranteed SLAs with fixed cost caps | |
| **Cost Attribution** | Global account billing | Project-level tags | User-level token attribution and dynamic chargeback | |
| **Cost Optimization** | No built-in optimization | Prompt compression | Native semantic caching, automated routing to cheaper models | |
| **Onboarding & Migration Cost** | Expensive professional services required | Self-serve onboarding | Comprehensive free migration support and tools | |

### Dimension 5: Enterprise Integration (Weight: 10%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Identity & Access** | Local users only | SAML/SSO integration | Fine-grained RBAC, ABAC, SCIM provisioning | |
| **Observability** | Basic usage dashboards | Log export to SIEM | Native OpenTelemetry, integration with Datadog/Splunk | |
| **Data Connectors** | CSV upload only | Basic DB/Storage connectors | 100+ native enterprise connectors (Salesforce, ServiceNow, etc.) | |
| **VPC & Networking** | Public endpoint only | IP Allowlisting | AWS PrivateLink / Azure ExpressRoute native integration | |

### Dimension 6: Vendor Viability & Support (Weight: 10%)

| Criterion | 1-Unacceptable | 3-Acceptable | 5-Leading | Score |
|---|---|---|---|---|
| **Financial Health** | Early stage startup; uncertain runway | Well-funded scale-up | Established enterprise software company or hyper-scaler | |
| **SLA & Uptime** | Best effort | 99.9% financially backed SLA | 99.99% SLA with aggressive penalty credits | |
| **Support Model** | Email only | 24/7 Severity 1 support | Dedicated Technical Account Manager (TAM) and Solution Architect | |
| **Roadmap Transparency** | Reactive updates | Quarterly roadmap sharing | Customer advisory board, early access to new models | |

---

## Evaluation Workflow

1. **Weight Customization**: Adjust the dimension weights based on the specific use case. (e.g., increase Data Sovereignty to 40% for Healthcare workloads; increase TCO to 30% for high-volume consumer tasks).
2. **Vendor Scoring**: Cross-functional team (Architecture, Security, Procurement) scores each vendor.
3. **Calculate Weighted Score**: (Score/5) * Weight for each dimension. Sum for total.
4. **Identify Dealbreakers**: Any score of '1' in a critical dimension (e.g., Training Data Use) should trigger automatic disqualification or require C-level exception.
5. **Final Matrix**: Present the scored matrix alongside the TCO projection.

---

*AIEA Toolkit AIEA-TK-07: AI Vendor Evaluation Scorecard Toolkit. Version 1.0, 2026.*  
*AI Enterprise Architecture Forum (AIEAF).*
