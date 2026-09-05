# From Experimentation to Measurable Business Value

> **Related:** [02-Agentic-AI-Use-Cases.md](02-Agentic-AI-Use-Cases.md) | [../03-EA-Practice/03-Strategic-Runbooks.md](../03-EA-Practice/03-Strategic-Runbooks.md)

---

## The Pilot Purgatory Problem

A 2025 MIT NANDA initiative study analysed enterprise AI spending and concluded that **95% of generative AI pilot programs fail to produce measurable financial impact**. The failures stem not from model quality — they stem from poor workflow integration and misaligned organisational incentives.

This is the defining challenge of AI adoption in 2025–2026: the technology works; the organisation doesn't know how to measure it. Enterprises are caught in "pilot purgatory" — launching disjointed projects that never scale to enterprise-wide value.

**The root causes of pilot failure:**

| Cause | Description |
|---|---|
| No baseline | No "before" measurement means no provable "after" |
| Wrong KPIs | Optimising model accuracy when the business wants dollars saved |
| Pilot tunnel vision | Isolated PoC benefits stay isolated; no mechanism to scale |
| Scaling economics mismatch | Pilot economics don't survive contact with production reality |
| One-time measurement | Treating ROI as a post-launch report, not a continuous process |

---

## The AI ROI Framework

Effective AI ROI measurement operates across four pillars:

### Pillar 1: Efficiency Gains
Lower operational costs, reduced manual hours, faster cycle times.

*Measurement approach:* Hours per task (before/after) × FTE cost × volume. Set a pre-deployment baseline for at least one business cycle before activation.

*Leading indicators:* Task completion time, error rates, rework rates
*Lagging indicators:* FTE-equivalent savings, operational cost reduction

### Pillar 2: Revenue Generation
Improved sales velocity, higher conversion, new revenue streams enabled by AI.

*Measurement approach:* Revenue per opportunity, conversion rate, upsell rate, new product revenue (before/after).

*Example:* A retail AI personalisation engine that increases average basket size by 4% generates measurable incremental revenue per transaction — attributable to the AI feature via A/B testing.

### Pillar 3: Risk Reduction
Fewer compliance breaches, lower fraud rates, reduced legal exposure, improved safety outcomes.

*Measurement approach:* Incident frequency and cost (before/after); insurance premium changes; regulatory fine avoidance.

*Note:* Risk reduction is often underrepresented in AI ROI calculations because the counterfactual ("what would have happened?") is difficult to model. Build this into business cases explicitly.

### Pillar 4: Agility / Capability
Faster time-to-market, higher experiment velocity, improved decision quality.

*Measurement approach:* Time from idea to production for AI-assisted vs. baseline projects; decision turnaround time; A/B test velocity.

*Note:* These are leading indicators of competitive advantage. They don't appear on a P&L but they predict future revenue and cost performance.

---

## KPI Selection by AI System Type

Different AI systems require fundamentally different KPIs. Using the wrong KPIs is the second most common measurement failure (after missing baselines).

| AI System Type | Primary KPI | Secondary KPIs |
|---|---|---|
| Customer service AI (chatbot/agent) | Containment rate (% resolved without human) | CSAT, Average Handle Time (AHT), cost per resolution |
| Recommendation engine | Revenue per session, click-through rate | Basket size, repeat purchase rate |
| Document processing (contracts, invoices) | Processing time per document | Error rate, exception rate, cost per document |
| Code generation assistant | Developer velocity (PRs/week) | Code review time, defect density, rework rate |
| Fraud detection AI | False positive rate, detection rate | Loss prevented, compliance alerts |
| Predictive maintenance | Unplanned downtime reduction | MTBF improvement, maintenance cost |
| HR / recruitment AI | Time-to-hire, cost-per-hire | Quality of hire (90-day performance), sourcing ratio |
| Demand forecasting | Forecast accuracy (MAPE) | Inventory holding cost, stockout rate |

---

## The Measurement Lifecycle: From Pilot to Scale

Metrics must evolve as AI systems mature. Using pilot metrics in production **systematically underreports the problems that matter**.

### Stage 1: Pilot (Feasibility)
*Question:* Does this work at all?

*Metrics:* Model accuracy on a held-out test set, time-to-build, data availability assessment

*Gate for next stage:* Model achieves minimum acceptable performance on representative test data; data infrastructure confirmed available

### Stage 2: Production (Reliability)
*Question:* Does this work reliably under real conditions?

*Metrics:* Inference latency (p50, p95, p99), error rate on production data, user adoption, cost per inference, data drift monitoring

*Gate for next stage:* System operates within SLA for 30 consecutive days; adoption rate above target; per-inference cost within budget

### Stage 3: Enterprise Scale (Portfolio ROI)
*Question:* Is this AI investment portfolio creating business value?

*Metrics:* Portfolio ROI (across all AI systems), governance compliance rate, cross-system attribution (when multiple AI systems interact), AI capability maturity index

*Trigger:* Operating multiple production systems with dependencies; AI investment decisions require portfolio-level justification

---

## Business Case Template: One-Page Format

This template is designed for executive alignment. Fill it out *before* building, not after.

```
AI Business Case — [Project Name]

PROBLEM STATEMENT
[What specific business problem does this solve? Be concrete. "Improve efficiency" is not a problem statement.]

CURRENT STATE BASELINE
[Quantified current performance: X hours/task, Y errors/month, Z% conversion, etc.]
[How was this measured? When was this measured?]

PROPOSED AI SOLUTION
[What specifically will the AI do? What inputs, what outputs, what actions?]

SUCCESS KPI
[ONE primary metric. What does success look like in 12 months?]
Target: [current baseline] → [target] = [improvement %]

MEASUREMENT PLAN
[How will you measure the KPI? Instrumentation already in place? A/B test or before/after?]

FINANCIAL MODEL
Cost: [build cost] + [run cost/year] = [total 3-year cost]
Value: [efficiency saving or revenue impact] × [volume] × [confidence %] = [annual value]
ROI: [value - cost] / cost = [%] | Payback period: [months]

RISKS
[Top 3 risks and mitigations]

DECISION REQUEST
[Approve build? Approve pilot? Approve spend?]
```

---

## The Productivity J-Curve

A critical pattern for AI programme leaders: AI investments commonly **depress productivity before improving it**. For every $1 of tangible AI tech investment, companies spend up to $10 on intangibles — process redesign, reskilling, organisational transformation — that initially reduce productivity before gains are realised.

**Implications for AI programme management:**

1. **Protect investment through the trough.** Senior sponsors must understand that a performance dip in months 2–4 does not indicate failure — it indicates the learning curve.

2. **Track leading indicators, not just lagging ones.** During the J-curve, lagging financial KPIs look bad. Track adoption rate, user competency, workflow integration progress — these predict when the curve will turn.

3. **Accelerate the trough.** Change management, training, and process redesign investment shortens the trough. Organisations that skip change management extend it.

4. **Set expectation before investment.** Show the J-curve to stakeholders at the investment decision stage. Surprises destroy AI programmes faster than bad technology does.

---

## Building an AI Value Dashboard

An AI Value Dashboard connects AI investments to business outcomes in a single view. Design for the CFO and board, not the data scientist.

**Required dashboard sections:**

**Section 1: Portfolio Summary**
- Total AI investment (YTD)
- Total attributed business value (YTD)
- Portfolio ROI
- Number of AI systems in production / in pilot / in development

**Section 2: By-System Performance**
For each production AI system:
- Primary KPI: current vs. target vs. baseline
- Cost per inference (trend)
- User adoption rate
- Last incident date and severity

**Section 3: Emerging Value**
- Leading indicators from pilots approaching production
- Qualitative value (speed, quality, capability) not yet in financial terms
- Innovation velocity (number of AI experiments run this quarter)

**Section 4: Risk and Compliance**
- Governance compliance rate across AI portfolio
- Open risk items
- Regulatory status

---

## Real-World Benchmarks

Use these as calibration points when building business cases, not as promises:

| Deployment | Company | Outcome | Source |
|---|---|---|---|
| AI coding assistant (GitHub Copilot) | Microsoft enterprise customers | 55% faster task completion | GitHub/Microsoft 2024 |
| Contract review agents | JPMorgan COIN | 360,000 lawyer-hours saved annually | Public disclosure |
| Customer service AI | Klarna | $40M annualised cost savings from CX automation | Google Cloud/Ipsos 2025 |
| IT support AI agents | DBS Bank | 40–60% reduction in ticket volume requiring human intervention | Forrester 2025 |
| Fraud detection | Multiple BFSI | 50–70% reduction in false positives | McKinsey 2025 |
| HR administrative AI | Mid-market enterprises | 30–40% reduction in HR admin overhead | Multiple vendors, Forrester |
| IEP preparation (Education) | Special education teachers | 90% reduction in preparation time | RaiseSummit 2026 |
| Demand forecasting | Retail | 15–30% reduction in inventory holding cost | McKinsey 2025 |

**Important caveat:** These benchmarks come from successful deployments. They are the upper bound, not the expected average. A realistic enterprise business case should apply a 40–60% discount to public benchmarks to account for real-world integration complexity.

---

## OKRs for an AI Programme

**Objective: Deliver measurable business value from AI within 12 months**

| Key Result | Measurement |
|---|---|
| 3 AI systems in production with documented ROI | Count of production systems with completed ROI assessment |
| Portfolio ROI > 150% (value/cost > 1.5x) | Calculated from Value Dashboard |
| 100% of production AI systems with active monitoring | Governance compliance rate |
| AI adoption rate across target user base > 60% | Measured via product analytics |
| Zero critical AI security incidents in 12 months | Incident log |
| AI business case template used for 100% of new AI investments | Process compliance |

---

*Sources: MIT NANDA Enterprise AI Study 2025, Stanford Digital Economy Lab Enterprise AI Playbook 2026, Google Cloud/Ipsos AI ROI Survey 2025, Worklytics AI ROI Guide 2026, McKinsey Global AI Survey 2025, Gartner AI Pilot to Production analysis, Agility-at-Scale AI ROI Framework.*
