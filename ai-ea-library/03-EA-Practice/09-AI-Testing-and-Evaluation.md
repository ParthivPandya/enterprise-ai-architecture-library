# AI Testing and Evaluation: The Quality Gate Every AI System Must Pass

> **Document type:** Informative Guide
> **Threshold note:** Numerical thresholds are examples unless tied to an approved risk decision, user need, regulation, contract, or measured baseline. Define thresholds for each system and context.

> *You wouldn't deploy a traditional application without a test suite. You wouldn't release a financial system without an audit trail. Yet most enterprises deploy AI systems with no systematic evaluation beyond "it seemed to work in the demo." This chapter is about building the test infrastructure that makes AI deployments defensible.*

> **Related:** [05-LLMOps.md](05-LLMOps.md) | [08-AI-Reference-Architectures.md](08-AI-Reference-Architectures.md) | [../01-AI-Governance/04-Risk-Mitigation.md](../01-AI-Governance/04-Risk-Mitigation.md)

---

## Why AI Testing Is Different

Traditional software testing verifies deterministic behaviour: given input X, expect output Y. AI systems — particularly LLMs — are probabilistic. The same input can produce different outputs on different calls. The "correct" output is often a matter of degree, not binary correctness. And the failure modes are not crashes or exceptions — they are subtle: hallucinations, bias, tone drift, scope creep, and confidently wrong answers.

This means traditional testing methods (unit tests, integration tests, end-to-end tests) are necessary but radically insufficient. AI systems require an additional evaluation layer that measures quality, safety, and reliability across distributions of inputs — not individual test cases.

**The three testing dimensions for AI:**

| Dimension | Question | Methods |
|---|---|---|
| **Functional Quality** | Does the system produce good outputs? | Automated evals, human review, golden dataset comparison |
| **Safety and Security** | Can the system be made to produce harmful outputs? | Red teaming, adversarial testing, guardrail verification |
| **Operational Reliability** | Does the system perform consistently under real conditions? | Load testing, latency profiling, drift monitoring, regression testing |

---

## The Evaluation Framework

### Level 1: Offline Evaluation (Before Deployment)

Offline evaluation tests the AI system against curated datasets before any user sees it. This is the minimum viable quality gate.

#### Golden Datasets

A golden dataset is a curated set of (input, expected output, evaluation criteria) tuples that represent the system's intended behaviour. Every production AI system MUST have one.

**How to build a golden dataset:**

1. **Collect representative queries** — sample from actual user queries (if available from a pilot), or have domain experts write 200–500 representative queries covering the full scope of the system's intended use
2. **Create reference outputs** — domain experts write or validate the "ideal" response for each query. For open-ended tasks (summarisation, generation), define evaluation rubrics instead of exact matches
3. **Include edge cases** — deliberately include:
   - Queries outside the system's scope (should be declined or redirected)
   - Ambiguous queries (should request clarification or caveat)
   - Adversarial queries (should be handled safely)
   - Queries requiring specific factual accuracy (should cite or ground)
4. **Version and maintain** — golden datasets are living documents. Update them as the system's scope changes, new failure modes are discovered, or domain knowledge evolves

**Size guidance:**
- **Minimum viable:** 100 test cases covering core functionality
- **Production-grade:** 500–1,000 test cases with edge cases and adversarial inputs
- **Enterprise-standard:** 2,000+ test cases segmented by use case, user type, and risk level

#### Automated Evaluation Harnesses

Automated evals run the golden dataset through the AI system and score the outputs programmatically. Key tools:

| Tool | What It Does | Best For |
|---|---|---|
| **HELM** (Stanford) | Comprehensive benchmark suite with standardised metrics | Broad model comparison, initial model selection |
| **Eleuther LM Harness** | Open-source evaluation for language models | Open-weight model evaluation |
| **Promptfoo** | Prompt-level testing with assertions | Prompt engineering QA, regression testing |
| **Ragas** | RAG-specific evaluation (faithfulness, relevance, context recall) | RAG pipeline quality |
| **DeepEval** | LLM-as-a-judge evaluation with custom metrics | Custom enterprise eval criteria |
| **Arize Phoenix** | Evaluation + observability in a single platform | Teams wanting eval + monitoring together |

#### Evaluation Metrics Taxonomy

Different AI system types require different metrics. Using the wrong metrics is a common evaluation failure.

**For RAG / Knowledge Q&A Systems:**

| Metric | What It Measures | How to Calculate |
|---|---|---|
| **Faithfulness** | Does the answer reflect only retrieved content? | LLM-as-judge scores answer against retrieved chunks |
| **Answer Relevancy** | Does the answer address the question? | Cosine similarity between question and answer embeddings |
| **Context Recall** | Were the right documents retrieved? | Proportion of relevant golden chunks retrieved |
| **Context Precision** | Were irrelevant documents excluded? | Proportion of retrieved chunks that are relevant |
| **Groundedness** | Can every claim be traced to a source? | Claim-level verification against retrieved content |

**For Conversational AI / Chatbots:**

| Metric | What It Measures | How to Calculate |
|---|---|---|
| **Task Completion** | Did the conversation achieve its goal? | Binary or partial success against defined goals |
| **Coherence** | Is the conversation logically consistent? | LLM-as-judge or human rating (1–5 scale) |
| **Helpfulness** | Was the response useful to the user? | Human rating or proxy (user satisfaction survey) |
| **Safety** | Did the system avoid harmful outputs? | Automated safety classifier + adversarial testing |
| **Containment Rate** | Resolved without human escalation? | Count of conversations resolved vs. escalated |

**For Code Generation:**

| Metric | What It Measures | How to Calculate |
|---|---|---|
| **Pass@k** | Does generated code pass test cases? | Run on k samples; measure % passing |
| **Functional Correctness** | Does code do what was asked? | Automated test execution |
| **Security** | Is generated code free of vulnerabilities? | SAST scan (Semgrep, CodeQL) on generated code |
| **Style Compliance** | Does code follow org standards? | Linter pass rate |

**For Agentic AI Systems:**

| Metric | What It Measures | How to Calculate |
|---|---|---|
| **Task Success Rate** | Did the agent complete the assigned task? | Binary success against defined completion criteria |
| **Step Efficiency** | How many steps did the agent take? | Count vs. optimal path length |
| **Tool Use Accuracy** | Did the agent call the right tools? | Compare tool calls against expected sequence |
| **Hallucinated Actions** | Did the agent attempt actions outside scope? | Audit log review for unauthorized tool calls |
| **Cost Per Task** | Total token spend for task completion | Sum all inference costs across agent steps |

---

### Level 2: Human Evaluation (Before and During Deployment)

Automated metrics are proxies. Human evaluation is the ground truth — but it's expensive and doesn't scale. Use it strategically.

#### When Human Evaluation Is Required

- **Always before first production deployment** of any customer-facing AI system
- **When automated metrics are ambiguous** — scores are borderline or contradictory
- **When the task is subjective** — summarisation quality, tone appropriateness, creative output
- **When the domain is high-stakes** — medical, legal, financial, hiring

#### Human Evaluation Protocol

**Step 1: Select evaluators.** Domain experts, not general annotators. For a legal AI, use lawyers. For a medical AI, use clinicians. Minimum 3 evaluators per sample to measure inter-annotator agreement.

**Step 2: Define the rubric.** Each criterion scored on a Likert scale (1–5) with explicit definitions:
- 5 = Expert-quality, could be used as-is
- 4 = Good, minor improvements possible
- 3 = Acceptable, some corrections needed
- 2 = Below standard, significant issues
- 1 = Unacceptable, harmful or wrong

**Step 3: Blind evaluation.** Evaluators should not know which outputs are AI-generated vs. human-generated (if comparing). They should not see each other's scores until individual assessment is complete.

**Step 4: Calculate agreement.** Use Cohen's kappa (for 2 evaluators) or Fleiss' kappa (for 3+) to measure inter-annotator agreement. If κ < 0.6, the rubric is ambiguous — refine it before proceeding.

**Step 5: Sample size.** Minimum 50 samples for pilot evaluation; 200+ for production readiness assessment.

---

### Level 3: Online Evaluation (During Production)

Once deployed, AI systems must be continuously evaluated against production traffic.

#### A/B Testing for AI Systems

Deploy AI changes as experiments, not releases:

- **Control group:** Current production system
- **Treatment group:** New model version, prompt change, or pipeline modification
- **Split:** 5–10% of traffic to treatment initially; increase upon validation
- **Metrics:** Primary KPI (task completion, user satisfaction) + guardrail metrics (safety, cost, latency)
- **Duration:** Minimum 2 weeks or 1,000 interactions, whichever is longer
- **Statistical rigour:** Use sequential testing or Bayesian methods to avoid peeking bias

#### Shadow Testing

Run the new AI system in parallel with the current system, without serving the new outputs to users:

1. Production traffic is duplicated to both systems
2. Both systems generate outputs
3. Only the current system's output is served to users
4. The new system's outputs are logged and evaluated offline

**Use shadow testing when:** The change is significant enough that you're not comfortable exposing even 5% of users to it before evaluation.

#### Canary Evaluation

A lightweight version of A/B testing for model updates:

1. Deploy new model to 5% of traffic
2. Monitor key metrics (latency p95, error rate, safety flags, user satisfaction) for 24–72 hours
3. If no regressions: expand to 25%, then 50%, then 100%
4. If any metric degrades >5% from baseline: automatic rollback

---

## The Evaluation Pipeline: CI/CD for AI

AI evaluation MUST be integrated into the deployment pipeline, not performed as a separate manual step.

```
Code Commit / Prompt Change / Model Update
            │
            ▼
   ┌─────────────────────┐
   │  Unit Tests          │  ← Standard software tests for non-AI code
   │  (pytest, jest)      │
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  Golden Dataset Eval │  ← Run golden dataset through system
   │  (Promptfoo / Ragas) │  ← Score against thresholds
   │                      │  ← FAIL if faithfulness < 0.85
   │                      │  ← FAIL if safety_score < 0.99
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  Adversarial Test    │  ← Run red team prompt library
   │  (PyRIT / Giskard)   │  ← FAIL if jailbreak rate > 0.5%
   │                      │  ← FAIL if PII leakage > 0.0%
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  Regression Check    │  ← Compare against last deployment
   │  (DeepEval)          │  ← FAIL if any metric regresses > 5%
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  Cost Estimation     │  ← Estimate production cost at scale
   │  (Token calculator)  │  ← WARN if cost > budget threshold
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │  Deployment Gate     │  ← All checks passed?
   │                      │  ← YES → Deploy to canary (5%)
   │                      │  ← NO → Block deployment, alert team
   └─────────────────────┘
```

### Threshold Definitions

Define pass/fail thresholds for every metric. These are enterprise-specific, but here are calibrated starting points:

| Metric | Minimum Threshold | Notes |
|---|---|---|
| Faithfulness (RAG) | ≥ 0.85 | Below 0.85 = unacceptable hallucination rate |
| Answer Relevancy | ≥ 0.80 | Below 0.80 = system not addressing user questions |
| Safety Score | ≥ 0.99 | Below 0.99 = safety controls need hardening |
| Jailbreak Resistance | ≥ 99.5% | Less than 0.5% of adversarial prompts succeed |
| PII Leakage | = 0.00% | Any PII leakage is a deployment blocker |
| Latency p95 | ≤ 5 seconds | Adjust based on use case SLA |
| Regression Delta | ≤ -5% | No metric may regress more than 5% from last deployment |

---

## Regression Testing: The Most Neglected Practice

Every model update, prompt change, or pipeline modification can silently degrade quality. Regression testing catches this.

### What Must Be Regression Tested

| Change Type | Regression Test Scope |
|---|---|
| **Model version update** (e.g., GPT-4o → GPT-4o-mini) | Full golden dataset + adversarial library |
| **System prompt change** | Full golden dataset + red team prompts |
| **RAG pipeline change** (chunking, embedding, retrieval) | Retrieval metrics on golden dataset |
| **Guardrail configuration change** | Full adversarial library |
| **Context window / max_tokens change** | Quality metrics on long-form queries |

### Building a Regression Library

Your regression library grows over time from three sources:

1. **Golden dataset** — the baseline test suite
2. **Red team prompt library** — adversarial inputs that have historically caused failures
3. **Production incidents** — every production issue generates a new test case: "the input that caused the problem, and the expected correct behaviour"

**Rule:** Every production AI incident MUST result in at least one new regression test case added within 48 hours.

---

## LLM-as-a-Judge: Using AI to Evaluate AI

For many evaluation criteria (coherence, helpfulness, tone), an LLM can serve as an automated evaluator — "LLM-as-a-Judge."

### When to Use LLM-as-Judge

- **Use when:** The evaluation criterion is well-defined and the judge model is more capable than the system being evaluated
- **Don't use when:** The evaluation requires domain expertise the judge model doesn't have, or when the stakes are too high for any automated assessment (regulatory, medical, legal)

### Best Practices

1. **Use a stronger model as judge** — if your system uses GPT-4o-mini, use GPT-4o or Claude Opus as the judge
2. **Provide explicit rubrics** — give the judge model the same rubric you'd give a human evaluator
3. **Calibrate against human judgment** — before trusting LLM-as-Judge, verify that it agrees with human evaluators on 100+ samples (target κ > 0.7)
4. **Use pairwise comparison** — "Which of these two outputs is better?" is easier for LLMs to judge than absolute scoring
5. **Randomise order** — LLMs have position bias (tend to prefer the first or last option). Randomise output order and average scores

---

## Enterprise Implementation Roadmap

### Phase 1: Foundation (Weeks 1–4)
- [ ] Identify the top 3 production AI systems that need evaluation infrastructure
- [ ] For each system, create a golden dataset (minimum 100 test cases)
- [ ] Select and deploy an automated evaluation tool (Promptfoo recommended for most teams)
- [ ] Define pass/fail thresholds for each metric

### Phase 2: Integration (Weeks 5–8)
- [ ] Integrate golden dataset evaluation into CI/CD pipeline
- [ ] Build initial red team prompt library (100+ adversarial prompts)
- [ ] Implement automated regression testing on model/prompt changes
- [ ] Set up evaluation dashboards for AI programme leadership

### Phase 3: Maturity (Weeks 9–16)
- [ ] Implement A/B testing infrastructure for AI changes
- [ ] Deploy canary evaluation for model updates
- [ ] Establish human evaluation protocol for quarterly quality reviews
- [ ] Build LLM-as-Judge calibration pipeline

### Phase 4: Continuous (Ongoing)
- [ ] Every production incident adds a regression test case within 48 hours
- [ ] Quarterly golden dataset refresh with new edge cases
- [ ] Monthly adversarial library update with new attack patterns
- [ ] Semi-annual human evaluation calibration

---

## Common Failure Modes in AI Testing

**Failure 1: Testing on the training distribution only.** If your golden dataset looks exactly like the examples the system was optimised for, you're testing the best case. Include out-of-distribution queries, edge cases, and adversarial inputs.

**Failure 2: Treating evaluation as a launch ceremony.** Evaluation is not something you do before launch and then stop. Model behaviour drifts, user behaviour changes, and new attack vectors emerge. Evaluation is continuous.

**Failure 3: Optimising for automated metrics at the expense of user experience.** A system with 0.95 faithfulness and 0.90 relevancy can still produce terrible user experiences if it's robotic, unhelpful, or fails on the specific queries your users care about most. Automated metrics are proxies. Human evaluation is the ground truth.

**Failure 4: No regression testing on prompt changes.** A "minor" prompt edit can cascade into unexpected behaviour changes. Treat every prompt change as a code change that requires testing.

**Failure 5: Using the same model as system and judge.** An LLM evaluating its own outputs has inherent bias. Always use a different (preferably stronger) model as the judge.

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): Stanford HELM Benchmark documentation 2025, Ragas RAG Evaluation Framework 2025, Promptfoo documentation 2026, DeepEval documentation 2026, Arize Phoenix evaluation guide 2026, Microsoft PyRIT documentation, Eleuther AI LM Evaluation Harness, Google Vertex AI Model Evaluation, NIST AI 600-1 evaluation requirements.*