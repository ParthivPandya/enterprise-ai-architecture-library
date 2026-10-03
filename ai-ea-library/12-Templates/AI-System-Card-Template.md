# AI System Card

> Copy this file per production AI system. Every production AI system MUST have a current System Card (AIEA-301). Review cadence: quarterly for High Risk, annual for Limited Risk.

| Field | Value |
|---|---|
| **System name** | `<name>` |
| **System ID** | `<AI-SYS-0000>` |
| **Version** | `<x.y>` |
| **Status** | `<In development / In production / Retired>` |
| **Risk classification** | `<Minimal / Limited / High / Unacceptable>` |
| **System Owner (accountable)** | `<named individual>` |
| **Technical Owner** | `<named individual>` |
| **Date created** | `<YYYY-MM-DD>` |
| **Last reviewed** | `<YYYY-MM-DD>` |
| **Next review due** | `<YYYY-MM-DD>` |

## 1. Purpose and Scope
- **Business purpose:** `<what business outcome this serves>`
- **In-scope use:** `<approved uses>`
- **Out-of-scope / prohibited use:** `<explicitly disallowed uses>`
- **Affected stakeholders:** `<who is impacted by its outputs>`

## 2. Capability and Behaviour
- **System type:** `<LLM assistant / ML classifier / agentic / CV / recommender / ...>`
- **Model(s) and provider(s):** `<model name, version, provider>`
- **Inputs:** `<data consumed>`
- **Outputs / actions:** `<decisions, content, actions produced>`
- **Known failure modes:** `<hallucination, drift, bias, ...>`
- **Performance boundaries:** `<where it should not be relied upon>`

## 3. Data
- **Data sources:** `<list, with Data Contract references>`
- **PII processed?** `[ ] Yes  [ ] No` — if yes, see the India DPDP Act/Rules alignment checklist
- **Data residency:** `<region/jurisdiction>`
- **Retention:** `<policy>`

## 4. Governance and Compliance
- **Applicable frameworks:** `<NIST AI RMF / EU AI Act / ISO 42001 / India DPDP Act and applicable Rules / ...>`
- **Pre-deployment review:** `<link to Launch Gate record>`
- **Explainability method:** `<disclosure / feature attribution / ...>`
- **Human oversight:** `<none / human-in-the-loop / human-on-the-loop>`
- **Red-team record:** `<link>`

## 5. Operations
- **Monitoring metrics:** `<accuracy, latency, cost, fairness, security>`
- **Dashboards:** `<link>`
- **Alert thresholds:** `<defined triggers>`
- **Fallback behaviour when unavailable:** `<describe>`
- **Cost attribution:** `<team / product / feature>`

## 6. Lifecycle
- **Review cadence:** `<quarterly / annual>`
- **Retirement triggers:** `<technology superseded / regulatory change / performance below threshold / business case invalid>`

## 7. Change Log
| Date | Version | Change | By |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<x.y>` | `<summary>` | `<name>` |
