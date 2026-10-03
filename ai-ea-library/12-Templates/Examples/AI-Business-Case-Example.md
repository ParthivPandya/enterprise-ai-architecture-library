# AI Business Case — Completed Example

> **Illustrative only:** all figures are hypothetical planning assumptions for a fictional organisation, not forecasts or achieved results. Source template: [AI-Business-Case-Template.md](../AI-Business-Case-Template.md).

| Field | Value |
|---|---|
| **Initiative name** | Customer Onboarding Guidance Assistant |
| **Sponsor** | Retail Banking Executive role |
| **Author** | Enterprise Architecture role |
| **Date** | 2026-09-01 (illustrative) |
| **Decision sought** | Fund a time-boxed, controlled pilot |

## 1. Problem and Opportunity

- **Problem statement:** applicants abandon journeys or contact support when document and status guidance is unclear. The actual baseline must be established before pilot approval.
- **Opportunity:** test whether state-aware guidance improves completion and reduces avoidable support while preserving KYC and fair-access controls.
- **Why AI:** language generation may explain approved workflow states more flexibly than a fixed FAQ. A deterministic-only alternative remains the benchmark and fallback.

## 2. Proposed Solution

- **Use case:** answer onboarding questions from approved content, guide secure data entry and create support handoffs.
- **AI system type:** LLM assistant constrained by a deterministic workflow.
- **Pilot scope:** opted-in internal testers followed, if gates pass, by a small supported customer cohort; no autonomous decisions or account creation.

## 3. Value

| Value driver | Planning baseline assumption | Hypothetical pilot target | How measured |
|---|---|---|---|
| Eligible journey completion | 62% | At least 68% | Like-for-like funnel cohort |
| Avoidable support contact | 18 per 100 journeys | No more than 13 | Categorised support records |
| Median active completion time | 24 minutes | No more than 20 minutes | Journey telemetry |
| KYC exception detection | Approved control baseline | No material degradation | Authoritative control metrics |

- **Primary KPI:** eligible journey completion, subject to control-quality guardrails.
- **Expected annual benefit:** not claimed. A range may be modelled only after baseline and pilot evidence.

## 4. Cost

| Cost category | Illustrative Year 1 estimate | Illustrative ongoing estimate |
|---|---:|---:|
| Build and integration | ₹4.0m | ₹1.0m |
| Model and inference | ₹0.8m | ₹1.2m |
| Data and platform | ₹1.5m | ₹0.9m |
| Governance, evaluation and monitoring | ₹1.7m | ₹1.1m |
| **Total** | **₹8.0m** | **₹4.2m** |

These sample estimates exclude tax, contingency and internal opportunity cost and must not be used for procurement.

## 5. Risk

- **Key risks:** misleading guidance, personal-data disclosure, unfair journey effects, prompt injection, weak handoff and provider dependency.
- **Risk classification:** High (provisional).
- **Mitigations:** deterministic state authority, secure fields, human alternatives, red-team testing, subgroup monitoring, circuit breaker and no-go launch gate.

## 6. Recommendation

Fund only the evaluation and controlled-pilot package. Do not approve production scale until baselines, privacy and security evidence, accessibility testing, vendor due diligence and stop thresholds are accepted. Stop if unauthorised progression, restricted-data disclosure or material degradation in KYC controls occurs.
