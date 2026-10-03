# Enterprise AI Readiness Assessment Toolkit
## Practitioner Toolkit & Diagnostic Playbook
### Document Ref: AIEA-TK-01 | Version 1.0 | 2026

---

## Executive Overview

Before an enterprise allocates capital or initiates architecture work under the AI-ADM, the Lead AI Architect and Chief AI Officer MUST conduct an **Enterprise AI Readiness Assessment**. 

This toolkit provides the formal survey instruments, scoring algorithms, capability gap heatmaps, and executive presentation templates required to diagnose organizational readiness, prevent costly pilot failures, and secure executive alignment.

```
┌─────────────────────────────────────────────────────────────────────────┐
│               THE SIX PILLARS OF ENTERPRISE AI READINESS                │
├───────────────────┬───────────────────┬─────────────────────────────────┤
│ 1. STRATEGIC      │ 2. DATA           │ 3. GOVERNANCE &                 │
│    ALIGNMENT      │    FOUNDATIONS    │    REGULATORY RISK              │
│ Clear KPIs, exec  │ Curated lineage,  │ AIAB chartered, risk tiers      │
│ sponsorship, ROI  │ clean APIs, vector│ defined, DPDPA / EU Act ready   │
├───────────────────┼───────────────────┼─────────────────────────────────┤
│ 4. ARCHITECTURE & │ 5. TALENT &       │ 6. FINOPS &                     │
│    INFRASTRUCTURE │    CULTURE        │    ECONOMIC CONTROL             │
│ AI Gateway, GPU   │ Embedded pods,    │ Token budgeting, chargeback,    │
│ VPC, model agnost.│ prompt literacy   │ ROI variance tracking           │
└───────────────────┴───────────────────┴─────────────────────────────────┘
```

---

## Chapter 1: The Enterprise Diagnostic Survey (30 Criteria)

Architects administer this diagnostic across business and technical leadership. Each criterion is scored from **1 (Non-Existent)** to **5 (Optimized / World-Class)**:

### Pillar 1: Strategic Alignment & Value Intent
1. **Business Problem Anchor:** AI initiatives originate from quantified business problems, not technology curiosity. *(Score: 1–5)*
2. **Executive Sponsorship:** Every active initiative has a named business executive holding P&L accountability. *(Score: 1–5)*
3. **Value Metric Definition:** Initiatives possess baseline KPIs (e.g., cost per claim, processing hours) measured prior to project initiation. *(Score: 1–5)*
4. **Portfolio Balance:** AI investments are balanced across quick-win copilots (60 days) and transformative capabilities (1–3 years). *(Score: 1–5)*
5. **Funding Sustainability:** Project funding accommodates non-linear operational token inference costs, not just upfront build capex. *(Score: 1–5)*

#### Pillar 2: Data Foundations & Semantic Architecture
6. **Data Accessibility:** Target enterprise data is accessible via documented REST/GraphQL APIs or modern lakehouses. *(Score: 1–5)*
7. **Data Quality & Hygiene:** Master data management (MDM) ensures consistent customer/product identifiers with $< 2\%$ duplication. *(Score: 1–5)*
8. **Lineage & Provenance:** Data sources feed into downstream vector stores with auditable cryptographic timestamps. *(Score: 1–5)*
9. **Access Control Filtering:** Enterprise IAM (Active Directory / Okta) can be enforced at document chunk level in retrieval pipelines. *(Score: 1–5)*
10. **Data Contracts:** Upstream data producers adhere to binding schemas and delivery SLAs. *(Score: 1–5)*

#### Pillar 3: Governance, Risk & Regulatory Compliance
11. **Chartered Governance Body:** An AI Architecture Board (AIAB) holds binding review authority over production launches. *(Score: 1–5)*
12. **Risk Classification Schema:** AI systems are classified into formal risk tiers (Prohibited, High, Significant, Limited, Minimal). *(Score: 1–5)*
13. **Regulatory Readiness:** Processes satisfy applicable legal frameworks (EU AI Act, India DPDPA, NIST AI RMF, ISO 42001). *(Score: 1–5)*
14. **System Inventory (System Cards):** The enterprise maintains a living registry of all models and algorithms in production. *(Score: 1–5)*
15. **Adversarial Red Teaming:** High-risk models undergo structured red-teaming for prompt injection and jailbreaking before launch. *(Score: 1–5)*

#### Pillar 4: Architecture & Runtime Infrastructure
16. **Model Independence:** Applications utilize an AI Gateway abstraction layer, preventing vendor SDK lock-in. *(Score: 1–5)*
17. **Semantic Caching:** Common queries are cached to eliminate redundant API token consumption. *(Score: 1–5)*
18. **Failover Resilience:** The architecture supports automated fallback to secondary model providers upon API timeout or outage. *(Score: 1–5)*
19. **Security Sandboxing:** Autonomous agent code-execution tools run in ephemeral, isolated microVMs. *(Score: 1–5)*
20. **Observability Instrumentation:** Real-time telemetry tracks latency, drift, hallucination rates, and token volume. *(Score: 1–5)*

#### Pillar 5: Talent, Competency & Culture
21. **Dedicated AI Architecture Roles:** Named Enterprise and Solution AI Architects lead technical designs. *(Score: 1–5)*
22. **Product Team Literacy:** Business analysts and product owners understand prompt engineering and model capability boundaries. *(Score: 1–5)*
23. **Cross-Functional Teaming:** Delivery pods embed architects, data engineers, security specialists, and business SMEs. *(Score: 1–5)*
24. **Responsible AI Training:** Engineers and architects receive mandatory training on bias, fairness, and ethical safety. *(Score: 1–5)*
25. **Change Management:** Formal ADKAR change plans manage employee transition, mitigating job displacement anxiety. *(Score: 1–5)*

#### Pillar 6: FinOps & Economic Governance
26. **Real-Time Cost Attribution:** All inference requests carry mandatory departmental chargeback headers (`X-Cost-Center`). *(Score: 1–5)*
27. **Budget Throttling:** Hard financial caps prevent runaway recursive agent loops or unexpected vendor invoices. *(Score: 1–5)*
28. **Model Tiering Strategy:** Ingress queries are classified so routine tasks route to low-cost SLMs rather than frontier models. *(Score: 1–5)*
29. **TCO Modeling:** Decisions to build, buy, or fine-tune models are backed by 3-year Total Cost of Ownership analyses. *(Score: 1–5)*
30. **Unit Economics Tracking:** The enterprise measures cost per resolved business outcome, ensuring declining unit costs over time. *(Score: 1–5)*

---

## Chapter 2: Scoring Rubric & Readiness Tiers

Calculate the aggregate score across all 30 criteria (Maximum Score: 150 points):

```
AGGREGATE SCORE BANDS:

  125 – 150 Points: TIER 1 — ENTERPRISE AI READY (Advanced)
  • Ready to deploy High-Risk and autonomous agentic systems.
  • Central AI Gateway and AIAB governance fully operational.

  95 – 124 Points:  TIER 2 — FOUNDATION READY (Intermediate)
  • Ready for RAG copilots and task-automation workflows.
  • Must remediate identified gaps in FinOps or Data Contracts before scaling.

  65 – 94 Points:   TIER 3 — EXPERIMENTAL / PILOT ONLY (Emerging)
  • Deploy only Minimal-Risk internal assistive tools.
  • Prohibit production customer-facing or high-stakes autonomous decisioning.

  < 65 Points:      TIER 4 — NOT READY (High Failure Risk)
  • Halt new AI software procurement.
  • Focus capital exclusively on data engineering, IAM, and establishing an AI CoE.
```

---

## Chapter 3: Executive C-Level Pitch Deck Template

When presenting AI readiness findings to the Board or Executive Committee, architects SHOULD utilize this standard 6-slide structure:

```
SLIDE 1: THE STRATEGIC IMPERATIVE
• Industry AI adoption trends and competitive risks of inaction.
• Our enterprise vision: Augmenting capabilities while containing systemic risk.

SLIDE 2: ENTERPRISE READINESS DIAGNOSTIC (RADAR CHART)
• Six-pillar maturity scores visualizing strengths (e.g., Talent) and critical gaps (e.g., FinOps).
• Overall Readiness Tier classification.

SLIDE 3: VALUE CREATION ROADMAP (THE THREE HORIZONS)
• Horizon 1 (60–90 Days): Quick-win internal productivity copilots.
• Horizon 2 (6–12 Months): Core workflow RAG synthesis (Customer service, claims).
• Horizon 3 (1–3 Years): Governed autonomous agentic systems.

SLIDE 4: ARCHITECTURAL GUARDRAILS & RISK CONTAINMENT
• Why our architecture will not repeat industry failure case studies (Air Canada, IBM Watson).
• The AIEA Core Principles: Model independence, human oversight, and data sovereignty.

SLIDE 5: BUDGET ALLOCATION & FINOPS CONTROLS
• Year 1 Capital Investment (Shared Gateway, Vector DB, CoE) vs Operational Token Budgets.
• Clear break-even milestones and automated chargeback governance.

SLIDE 6: IMMEDIATE 90-DAY ACTIONS REQUESTED
• 1. Formal chartering of the AI Architecture Board (AIAB).
• 2. Deployment of the central enterprise AI Gateway.
• 3. Approval to initiate AI-ADM Phase 0 for top two prioritized use cases.
```

---

*AIEA Toolkit AIEA-TK-01: Enterprise AI Readiness Assessment Toolkit. Version 1.0, 2026.*  
*AIEA Reference Library.*
