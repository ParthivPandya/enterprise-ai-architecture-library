# AI Observability and Monitoring: Keeping AI Systems Reliable in Production

> **Document type:** Informative Guide
> **Threshold note:** Alert and service-level thresholds are examples. Calibrate them from system risk, user impact, baseline distributions, contracts, and operational capacity.

> *Deploying an AI system without observability is like flying without instruments — you know you're in the air, but you don't know your altitude, speed, or heading until you crash. This chapter builds the instrumentation that keeps AI systems healthy, accurate, and accountable in production.*

> **Related:** [05-LLMOps.md](05-LLMOps.md) | [09-AI-Testing-and-Evaluation.md](09-AI-Testing-and-Evaluation.md) | [../01-AI-Governance/01-FinOps.md](../01-AI-Governance/01-FinOps.md)

---

## Why AI Observability Is Different From Application Monitoring

Traditional application monitoring answers: "Is the system up? Is it fast? Is it throwing errors?" These questions remain necessary for AI systems — but they are radically insufficient.

An AI system can be up, fast, and error-free while producing confidently wrong answers, exhibiting increasing bias, or haemorrhaging tokens to a runaway agent loop. Traditional monitoring would show all green. Users would be getting harmful outputs.

AI observability adds three dimensions that traditional monitoring doesn't cover:

| Dimension | Traditional Monitoring | AI Observability |
|---|---|---|
| **Correctness** | Error rate, HTTP status codes | Hallucination rate, groundedness score, answer quality |
| **Fairness** | Not applicable | Disparate impact across demographic groups over time |
| **Cost Behaviour** | Infrastructure cost (fixed) | Token consumption (variable, per-request, potentially unbounded) |

---

## The AI Observability Stack

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE AI OBSERVABILITY STACK                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  LAYER 4: BUSINESS INTELLIGENCE                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │ Portfolio dashboard │ ROI tracking │ Compliance status │ Trends  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  LAYER 3: AI-SPECIFIC OBSERVABILITY                                      │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │ Quality metrics │ Drift detection │ Fairness monitoring          │   │
│  │ Hallucination rate │ Retrieval quality │ Agent step analysis      │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  LAYER 2: LLM OPERATIONS                                                │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │ Token consumption │ Model latency │ Cache hit rate │ Cost/query  │   │
│  │ Model version tracking │ Prompt version tracking                 │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  LAYER 1: INFRASTRUCTURE (Traditional)                                   │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │ CPU/GPU utilisation │ Memory │ Network │ Uptime │ Error rate      │   │
│  │ API latency (p50/p95/p99) │ Throughput │ Availability             │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Metrics Taxonomy

### Infrastructure Metrics (Layer 1)

Standard SRE metrics applied to AI systems:

| Metric | Definition | Alert Threshold | Tool |
|---|---|---|---|
| **API availability** | % of requests returning non-error responses | < 99.5% over 5 min | Datadog, Prometheus |
| **Latency p50** | Median response time | > 2s (adjust per SLA) | OpenTelemetry |
| **Latency p95** | 95th percentile response time | > 5s | OpenTelemetry |
| **Latency p99** | 99th percentile response time | > 10s | OpenTelemetry |
| **Error rate** | % of requests returning errors | > 1% over 5 min | Prometheus, Grafana |
| **GPU utilisation** | % of GPU compute used (self-hosted) | > 90% sustained | NVIDIA DCGM, Prometheus |
| **Queue depth** | Number of requests waiting for inference | > 100 sustained | Custom metrics |

### LLM Operations Metrics (Layer 2)

| Metric | Definition | Alert Threshold | Why It Matters |
|---|---|---|---|
| **Tokens per request (input)** | Average input tokens per API call | > 2× baseline | Prompt bloat or injection |
| **Tokens per request (output)** | Average output tokens per API call | > 2× baseline | Verbose outputs, cost risk |
| **Cost per query** | Total inference cost per user query | > budget cap | FinOps control |
| **Cost per session** | Total cost for a user's interaction session | > session budget | Agentic cost control |
| **Cache hit rate** | % of requests served from semantic cache | < 20% (if expected > 30%) | Cache configuration issue |
| **Model version** | Which model version is serving traffic | Unexpected change | Model update without approval |
| **Prompt version** | Which system prompt version is active | Unexpected change | Prompt drift |
| **Rate limit hits** | Number of requests hitting provider rate limits | > 0 sustained | Capacity planning needed |

### AI Quality Metrics (Layer 3)

These are the metrics that traditional monitoring completely misses:

#### Hallucination / Groundedness Monitoring

| Metric | Definition | How to Measure | Alert Threshold |
|---|---|---|---|
| **Groundedness score** | % of claims in output traceable to retrieved sources | LLM-as-judge or NLI model checking output claims against retrieved chunks | < 0.80 sustained |
| **Citation accuracy** | % of cited sources that actually support the claim | Automated verification: does the cited chunk contain the stated information? | < 0.90 |
| **Refusal rate** | % of queries where system correctly declines to answer | Count of "I don't have enough information" responses | Monitor trend (sudden drop = guardrail issue) |
| **Confabulation rate** | % of outputs containing fabricated facts | Periodic human audit sample (50 outputs/week) | > 5% on audit sample |

#### Retrieval Quality Monitoring (RAG Systems)

| Metric | Definition | Alert Threshold |
|---|---|---|
| **Retrieval relevance** | Average relevance score of top-k retrieved chunks | < 0.70 on rolling 24h |
| **Empty retrieval rate** | % of queries where no relevant chunks are found | > 15% |
| **Stale document rate** | % of retrievals returning documents older than freshness SLA | > 5% |
| **Index coverage** | % of source documents successfully indexed | < 95% |

#### Drift Detection

Model drift means the AI system's behaviour is changing over time — even without any model or prompt updates. Drift has three sources:

| Drift Type | What Changes | How to Detect | Example |
|---|---|---|---|
| **Data drift** | The input distribution changes | Statistical tests (KS test, PSI) on input features over time | Users start asking about a new product not in training data |
| **Concept drift** | The relationship between inputs and correct outputs changes | Quality metric degradation without input distribution change | Regulatory rules change; AI still applies old rules |
| **Performance drift** | Output quality degrades over time | Tracking quality metrics (groundedness, relevance) over time windows | Model provider silently updates model; quality changes |

**Detection approach:**
1. Compute quality metrics on a rolling 7-day window
2. Compare against the baseline established at deployment
3. Alert if any metric deviates > 10% from baseline for > 24 hours
4. Trigger automated evaluation (golden dataset re-run) on drift alert

#### Fairness Monitoring

Fairness is not a one-time check. As user populations change and model behaviour drifts, fairness characteristics can degrade.

| Metric | What It Monitors | Cadence |
|---|---|---|
| **Disparate Impact Ratio** | Outcome equity across demographic groups | Weekly (automated) |
| **Equal Opportunity Delta** | True positive rate gap across groups | Weekly (automated) |
| **Response quality by segment** | Quality scores segmented by user type / geography | Monthly |
| **Sentiment by segment** | User sentiment scores segmented by demographics | Monthly |

---

## Tooling Landscape

| Category | Tools | Best For |
|---|---|---|
| **LLM Observability** | Langfuse, Arize Phoenix, Helicone | Full trace logging, quality scoring, cost tracking |
| **Infrastructure Monitoring** | Datadog, Prometheus + Grafana, New Relic | Traditional SRE metrics extended to AI |
| **Distributed Tracing** | OpenTelemetry, Jaeger | End-to-end request tracing through AI pipelines |
| **Evaluation + Monitoring** | Arize AI, Weights & Biases, TruLens | Combined offline eval and production monitoring |
| **Cost Monitoring** | LiteLLM, Portkey, Helicone | Token-level cost attribution and alerting |
| **Custom Dashboards** | Grafana, Apache Superset | Custom AI operations dashboards |

**Recommended starter stack:**
- **Langfuse** (open-source) — LLM trace logging, prompt management, quality scoring
- **OpenTelemetry** — distributed tracing and infrastructure metrics
- **Grafana** — dashboards and alerting

---

## Alert Design for AI Systems

### Alert Tiers

| Tier | Severity | Response Time | Example | Action |
|---|---|---|---|---|
| **P1 — Critical** | Production safety issue | < 15 minutes | PII leakage detected; safety filter bypass | Disable system, page on-call |
| **P2 — High** | Quality degradation at scale | < 1 hour | Hallucination rate > 10%; groundedness < 0.70 | Investigate, consider rollback |
| **P3 — Medium** | Performance or cost issue | < 4 hours | Latency p95 > SLA; cost/query > 2× budget | Investigate root cause |
| **P4 — Low** | Informational | Next business day | Cache hit rate declining; minor drift detected | Review in weekly AI ops meeting |

### Alert Fatigue Prevention

Alert fatigue kills observability programmes. Prevent it:

1. **Alert on symptoms, not causes** — alert on "user-facing quality degraded" not "GPU utilisation high"
2. **Require actionability** — every alert must have a documented response procedure
3. **Use anomaly detection, not fixed thresholds** — a 20% cost increase on Black Friday is normal; on a Tuesday it's not
4. **Aggregate before alerting** — a single failed request is noise; 50 failed requests in 5 minutes is signal
5. **Review and prune monthly** — delete any alert that fired > 10 times without action taken

---

## Dashboard Templates

### Dashboard 1: AI Operations (For Platform Team)

**Sections:**
- System health: availability, latency p50/p95/p99, error rate (real-time)
- Token economics: tokens/request, cost/query, cache hit rate (hourly)
- Model status: current model version, prompt version, last update date
- Quality signals: groundedness score, retrieval relevance (rolling 24h)
- Active alerts with status

### Dashboard 2: AI Quality (For AI Programme Lead)

**Sections:**
- Quality trends: groundedness, faithfulness, relevance over 30/60/90 days
- Drift indicators: input distribution shift, quality metric trends
- Fairness snapshot: disparate impact ratio by system
- Regression test results: last 5 test runs with pass/fail status
- User satisfaction: CSAT/NPS trend for AI-powered features

### Dashboard 3: AI Portfolio (For CAIO / Board)

**Sections:**
- Portfolio overview: total AI systems in production, pilot, development
- Financial summary: total AI spend YTD vs. budget, cost trend
- Value realisation: ROI by system, value attributed vs. cost
- Risk posture: compliance status, open risk items, last incident date
- Maturity progress: readiness assessment trend over quarters

---

## SRE Practices Adapted for AI

### SLIs, SLOs, and SLAs for AI Systems

Traditional SRE defines Service Level Indicators (SLIs), Objectives (SLOs), and Agreements (SLAs). AI systems require AI-specific SLIs:

| SLI Category | Traditional SLI | AI-Extended SLI |
|---|---|---|
| **Availability** | % of requests returning non-error | % of requests returning non-error AND non-hallucinated |
| **Latency** | Response time | Time to first token + total generation time |
| **Correctness** | (Not typically measured) | Groundedness score, factual accuracy rate |
| **Safety** | (Not typically measured) | % of outputs passing safety classifier |

**Example SLO for an enterprise RAG system:**
- Availability SLO: 99.9% of requests return a grounded response within 5 seconds
- Quality SLO: 95% of responses score ≥ 0.85 on groundedness (measured weekly via sampling)
- Safety SLO: 0.00% of responses contain PII or harmful content
- Cost SLO: 95% of queries cost < ₹2 per query (measured monthly)

### On-Call for AI Systems

AI systems require on-call engineers who understand both software operations AND AI behaviour. The on-call rotation should include:

- **L1 (Platform):** Infrastructure issues — outages, latency, capacity. Standard SRE skills.
- **L2 (AI Operations):** Quality issues — hallucination spikes, drift alerts, safety incidents. Requires AI system knowledge.
- **L3 (AI Engineering):** Root cause — model issues, prompt failures, retrieval degradation. Requires ML engineering skills.

---

## Enterprise Implementation Roadmap

### Phase 1: Instrument (Weeks 1–4)
- [ ] Deploy distributed tracing (OpenTelemetry) on all production AI systems
- [ ] Implement token-level cost tracking per system and per team
- [ ] Set up basic infrastructure monitoring (availability, latency, error rate)
- [ ] Create AI Operations dashboard (Dashboard 1)

### Phase 2: Quality Monitoring (Weeks 5–8)
- [ ] Deploy LLM observability platform (Langfuse or equivalent)
- [ ] Implement groundedness monitoring for all RAG systems
- [ ] Set up drift detection (rolling 7-day baseline comparison)
- [ ] Define and configure P1–P4 alert tiers

### Phase 3: Advanced Monitoring (Weeks 9–16)
- [ ] Implement fairness monitoring (weekly automated disparate impact measurement)
- [ ] Deploy anomaly detection for cost and quality metrics
- [ ] Create AI Quality and AI Portfolio dashboards (Dashboards 2 & 3)
- [ ] Establish AI-specific SLOs for all production systems

### Phase 4: Maturity (Ongoing)
- [ ] Monthly alert review and pruning
- [ ] Quarterly SLO review and adjustment
- [ ] Integration with incident management (PagerDuty, ServiceNow)
- [ ] Correlation of observability data with business outcomes

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): OpenTelemetry AI Semantic Conventions 2025, Langfuse documentation 2026, Arize AI LLM Observability Guide 2026, Google SRE Handbook (adapted for AI), Datadog AI Monitoring documentation, Helicone cost attribution guide 2026, NIST AI RMF MEASURE function requirements.*