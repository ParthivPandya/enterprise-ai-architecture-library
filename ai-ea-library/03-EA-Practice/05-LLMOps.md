# LLMOps: Shipping AI to Production and Keeping It There

> *85% of AI models never make it to production. Of those that do, most degrade within months and no one notices until someone complains. This chapter is about the engineering discipline that closes both gaps.*

> **Related:** [../01-AI-Governance/04-Risk-Mitigation.md](../01-AI-Governance/04-Risk-Mitigation.md) | [06-Prompt-Engineering-for-Enterprise.md](06-Prompt-Engineering-for-Enterprise.md) | [../03-EA-Practice/03-Strategic-Runbooks.md](03-Strategic-Runbooks.md)

---

## MLOps and LLMOps: What's the Difference and Why It Matters

MLOps brought DevOps discipline to traditional machine learning — version control, CI/CD, automated testing, and monitoring applied to model development and deployment. It took the field from "data scientists running notebooks and emailing CSV files to engineers" to reproducible, automated model deployment pipelines.

LLMOps extends MLOps for a fundamentally different problem set. Traditional ML models are deterministic, compact, and version-controllable in the way software is. Foundation models are probabilistic, enormous, and accessed through APIs rather than deployed as code artifacts. The differences are not cosmetic — they require new tooling, new evaluation approaches, and new operational practices.

| Dimension | Traditional MLOps | LLMOps |
|---|---|---|
| Model artifact | Python model file (MB range) | API call or multi-GB weight file |
| Versioning | Version the weights | Version the prompt + model version pin |
| Evaluation | Accuracy / F1 against test set | LLM-as-judge, human preference, task-specific metrics |
| Monitoring | Concept drift, data drift | Hallucination rate, output quality, cost drift, prompt injection attempts |
| Iteration cycle | Retrain model (hours to weeks) | Adjust prompt (minutes) or swap model version |
| Cost driver | Compute for training | Tokens per inference |
| Failure mode | Silent accuracy degradation | Hallucination, jailbreak, cost explosion |

In practice, most enterprises need both. Traditional ML workloads (fraud detection models, demand forecasting, recommendation engines) need MLOps. LLM-powered features (chatbots, document analysis, code assistants) need LLMOps. Building one practice without the other leaves gaps.

---

## The MLOps Maturity Ladder

A useful mental model for where your organisation sits and what to build next:

**Level 0 — Manual Process**
Data scientists work in Jupyter notebooks. Model deployment means emailing a pickle file to the engineering team. No pipeline automation, no version control for models, no monitoring. This is where 85% of ML projects die — they never leave the notebook.

**Level 1 — ML Pipeline Automation**
Automated training pipelines with experiment tracking. Models are versioned and stored in a registry. CI/CD is partially implemented — code is tested, but model deployment is still partly manual. This is the minimum viable MLOps state for any production deployment.

**Level 2 — CI/CD Pipeline Automation**
Full automation from code commit to production deployment. Every change triggers: data validation, model training, model evaluation against baseline, integration tests, and automated deployment if all gates pass. Champion/challenger model comparison is automated. Netflix operates at this level — pushing 300 model updates daily across recommendation infrastructure, each automatically validated, tested, and monitored.

**Level 3 — Automated Monitoring and Retraining**
Production models are continuously monitored for drift. When drift crosses a threshold, retraining is triggered automatically. In LLMOps, this extends to automated prompt regression testing, hallucination rate monitoring, and cost anomaly detection.

Most enterprises are at Level 0 or 1. Level 2 is the production standard to aim for. Level 3 is for organisations with the data infrastructure and team maturity to manage automated retraining safely.

---

## The LLMOps Stack: What You Actually Need

There is no single platform that covers the full LLMOps stack. Most enterprise deployments use 3–5 specialised tools. Here's how to think about the categories:

### Experiment Tracking and Prompt Management
When you're building with LLMs, "experiment" means "different prompt + model version combination." You need to track what prompt you tried, with which model, at which temperature, against which test cases, and what the results were.

**Tools:**
- **LangSmith** (LangChain): prompt versioning, trace logging, evaluation harnesses. The most widely used choice for teams building on LangChain.
- **Promptflow** (Microsoft): native Azure integration, strong for teams standardised on Azure OpenAI.
- **MLflow** (open-source): extended to track LLM experiments; broader MLOps coverage beyond LLMs.

**The practice:** Every prompt that goes into production should be version-controlled in a prompt registry, with the associated model version, parameter settings, evaluation results, and the name of the person who approved it. Prompts that aren't version-controlled are silent configuration changes waiting to break your production system.

### Evaluation Frameworks
Traditional ML evaluation is simple: run the model against a held-out test set, compute accuracy/F1/AUC. LLM evaluation is harder because the outputs are open-ended text, and "correct" is often a matter of quality rather than binary right/wrong.

Three evaluation approaches, used in combination:

**LLM-as-Judge:** Use another LLM (often a stronger one) to evaluate your model's outputs against defined criteria — faithfulness to source, coherence, relevance, safety. This scales to thousands of samples without human review time.

**Human preference evaluation:** For high-stakes use cases, human evaluators compare pairs of outputs and select the better one. Gold standard, but expensive. Use selectively for calibrating your LLM-as-judge model and for pre-production validation of major changes.

**Task-specific automatic metrics:** For specific task types — summarisation (ROUGE), factual accuracy (against a knowledge base), code correctness (by running the code) — automated metrics provide fast, consistent feedback.

**Tools:** Giskard (AI quality and security testing), Promptfoo (prompt regression testing), Galileo (production evaluation and monitoring), DeepEval (comprehensive LLM evaluation framework).

**The golden test set:** Every production LLM system should have a curated set of 100–500 representative test cases — real inputs with ideal outputs, maintained and updated as the system evolves. Run this against every model or prompt change before production deployment. Your canary deployment is only as good as your ability to detect when things get worse.

### Observability and Monitoring
Once in production, you need to see what's happening. LLM observability covers different ground than traditional application monitoring:

**What to monitor in production:**
- **Latency** (p50, p95, p99 per endpoint)
- **Token cost** (input tokens, output tokens, total cost per request — attribute to business unit, feature, and user where possible)
- **Error rate** (API failures, timeout rates, guardrail trigger rates)
- **Hallucination rate** (using an automated factuality check against your knowledge base)
- **Output quality drift** (LLM-as-judge scoring on a sample of production traffic)
- **Prompt injection attempts** (flagged by your input validation layer)
- **User feedback signals** (thumbs up/down, correction rates, escalation rates)

**Tools:** Langfuse (open-source observability, full trace logging), OpenTelemetry (standard telemetry for integration into existing observability stacks), Helicone (cost tracking and logging), Datadog AI observability extensions.

**The thing most teams skip:** Sampling production traffic for quality evaluation. Cost monitoring and latency monitoring are easy — they come from API response metadata. Quality monitoring requires actually looking at what the model said and whether it was any good. Build a pipeline that samples 1–5% of production traffic, runs it through LLM-as-judge evaluation, and surfaces quality trend data to the team weekly.

### Model Registry and Versioning
For teams self-hosting open-weight models or fine-tuning on domain data, a model registry is essential — it tracks which model version is running in which environment, with what configuration, trained on what data, with what evaluation results.

**Tools:** MLflow Model Registry (open-source, widely used), Hugging Face Hub (for open-weight models), AWS SageMaker Model Registry (for teams on AWS), Azure ML Model Registry.

**The critical practice:** No model goes to production without a registry entry that includes: model version, training data snapshot, evaluation results on the golden test set, the name of the approver, and a rollback plan.

### Deployment Infrastructure
How the model is served in production:

**API-based (most common for frontier models):** Your application calls the provider API. Infrastructure complexity is at the application layer — the gateway, caching, rate limiting. The provider handles model serving.

**Self-hosted (for open-weight models):** You deploy model weights on GPU infrastructure. Options: AWS Bedrock (managed hosting for select open-weight models), Azure AI model catalog, on-premises GPU servers (NVIDIA A100/H100).

**Serving frameworks:** vLLM (high-throughput LLM serving with continuous batching — the standard for self-hosted inference), Ollama (for development and edge deployment), TGI (Hugging Face Text Generation Inference).

**The architecture requirement:** Whatever your deployment model, your application should call a model abstraction layer — not the provider API directly. LiteLLM is the most widely used choice: it provides a unified API across all major providers, handles fallback routing, implements rate limiting and retry logic, and provides request/response logging. If you build directly on the OpenAI SDK and then want to add a fallback to Anthropic, or switch to Azure OpenAI for compliance reasons, you have to rewrite calling code everywhere. With LiteLLM as the abstraction layer, you change one configuration.

---

## CI/CD for LLMs: The Pipeline in Practice

A production-grade LLM CI/CD pipeline has these stages:

```
Code / Prompt Change
        ↓
[Stage 1: Static Validation]
- Prompt linting (format checks, length limits)
- Security scan (does prompt reveal system configuration?)
- Policy compliance check (does prompt violate content policy?)
        ↓
[Stage 2: Unit Tests]
- Known-answer test cases (does the model still answer specific questions correctly?)
- Format compliance tests (does output match required JSON schema?)
- Safety tests (does model refuse prohibited requests?)
        ↓
[Stage 3: Golden Test Set Evaluation]
- Full golden test set run
- LLM-as-judge scoring
- Human review of borderline cases (if any)
- Baseline comparison: score must be >= previous version score (within defined tolerance)
        ↓
[Stage 4: Integration Tests]
- End-to-end test against staging environment
- Latency validation (p95 must be within SLA)
- Downstream system integration tests (does the output work for whatever uses it?)
        ↓
[Stage 5: Red Team Prompt Library]
- Automated run of adversarial prompt library
- Any critical-severity failures = pipeline blocked
- High-severity failures reviewed and accepted/rejected
        ↓
[Stage 6: Canary Deployment]
- Deploy to 5% of traffic
- 72-hour monitoring period
- Automated promotion gate: no critical incidents, quality metrics stable
        ↓
Full Production (progressive rollout: 5% → 25% → 50% → 100%)
```

**The drift detection trigger:** Beyond code changes, the pipeline should also trigger on **data drift**. If the distribution of inputs to your LLM system is shifting — users are asking different types of questions, or the documents being processed have different characteristics — the model's performance profile will change even if no code changed. Implement statistical drift detection on input distributions and trigger a full golden test set re-evaluation when drift is detected.

---

## The Top Production Failure Modes (And How to Prevent Them)

**Failure Mode 1: Silent quality degradation**
The model is updated by the provider without notification (or with 90-day notice that nobody action'd). The model's behaviour changes subtly — outputs are longer, or shorter, or use different phrasing, or handle edge cases differently. KPIs don't immediately alert because the change is gradual. Users start complaining six weeks later.

**Prevention:** Always pin model versions in production. Never use `gpt-4` — use `gpt-4-0125-preview`. Monitor output quality continuously, not just at deployment.

**Failure Mode 2: Prompt regression on edge cases**
A prompt is improved for the common case but breaks a specific edge case that wasn't in the test set. The regression isn't caught until a user finds it.

**Prevention:** Treat prompt changes with the same discipline as code changes. Every reported failure becomes a test case. Your golden test set grows over time to cover every failure you've seen in production.

**Failure Mode 3: Cost explosion from prompt or usage changes**
A new product feature adds 2,000 tokens of context per request. Nobody modelled the cost impact. At 100,000 daily requests, that's 200 million additional tokens per day — potentially a 10x increase in inference cost.

**Prevention:** Cost impact analysis is a required field in every prompt change review. Model the per-request cost impact before merge. See [01-AI-Governance/01-FinOps.md](../01-AI-Governance/01-FinOps.md).

**Failure Mode 4: Guardrail bypass in production**
The red team test library is run at deployment. Six weeks later, a jailbreak technique discovered on a public forum is circulating in your user community and bypassing your content filters.

**Prevention:** Subscribe to AI security disclosure channels (OWASP, MITRE ATLAS). Every new jailbreak technique is added to the red team library within 48 hours. Run the library on a weekly schedule in production, not just at deployment.

**Failure Mode 5: RAG knowledge base staleness**
A policy document changes. The vector database isn't updated. Users ask the AI about the policy and get the old answer. Nobody realises for three months.

**Prevention:** Implement document freshness monitoring on your vector database. When a source document changes, trigger an automatic re-indexing job. Set a maximum acceptable staleness threshold (e.g., 24 hours for compliance-sensitive documents) and alert when exceeded.

---

## The LLMOps Team Structure

LLMOps is a cross-functional discipline. These are the roles that need to exist — they don't all need to be full-time:

| Role | Responsibilities | Can Be Part-Time In |
|---|---|---|
| LLMOps Engineer | Pipeline automation, deployment, monitoring infrastructure | <3 production LLM systems |
| Prompt Engineer | Prompt design, versioning, evaluation | |
| AI Evaluation Lead | Evaluation framework, golden test set maintenance, quality metrics | Can share with QA Lead |
| ML Engineer | Fine-tuning, custom model work (if applicable) | If using API-only, may not need |
| Security Engineer | Red team library, security monitoring, OWASP coverage | Can share with CISO team |
| Product Manager (AI) | Use case prioritisation, stakeholder communication, KPI ownership | Typically shared role |

The smallest sustainable LLMOps team for 3–5 production LLM systems is 2–3 full-time engineers supported by a part-time product manager and access to security resources.

---

*Sources: MLops in 2026 DataCamp/Medium February 2026, MLOps Infrastructure CI/CD Pipelines Introl Blog March 2026, LLMOps for Production AI Enterprise Guide Ailoitte June 2026, ThirstySprout MLOps Best Practices 2025, Galileo MLOps Operationalizing ML Blog, CaliberFocus MLOps LLMOps Services, MLcon LLMOps track curriculum, Netflix ML infrastructure blog, S&P Global AI abandonment survey 2025, Gartner AI model failure analysis.*
