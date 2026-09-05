# Strategic Runbooks for Architects

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [02-AI-Design-Decisions.md](02-AI-Design-Decisions.md) | [../01-AI-Governance/04-Risk-Mitigation.md](../01-AI-Governance/04-Risk-Mitigation.md)

---

## The Need for AI Runbooks

Ad hoc evaluations of AI services lead to shadow AI, inconsistent security postures, and cost overruns. Enterprise Architects need standardised, repeatable "runbooks" for the lifecycle of an AI service. 

These runbooks serve as the operational bridge between the high-level AI Strategy and the day-to-day execution of engineering teams. They move EA from a theoretical gatekeeper to a practical enabler.

---

## Runbook 1: Evaluating a New AI Service

When a business unit requests a new AI service (e.g., a new LLM API, a SaaS product with embedded GenAI, or a vector database), the EA uses this runbook to perform a rapid but comprehensive evaluation.

### Evaluation Checklist

| Dimension | Key Questions | Red Flags |
|---|---|---|
| **Data Residency & Privacy** | Where is the model hosted? Are prompts used for provider training? Does it comply with the DPDPA? | Provider uses customer data for model training by default; no regional hosting option. |
| **Security & Compliance** | Does the provider hold ISO 42001 or SOC 2 Type II? What is the data retention policy for API inputs? | Lack of enterprise SSO; unable to integrate with existing IAM (Identity and Access Management). |
| **Architecture Integration** | Is it API-first? Does it support standard protocols (e.g., OpenAI compatible endpoints)? | Proprietary protocols; difficult to switch to a competitor later (high vendor lock-in). |
| **Cost & FinOps** | What is the pricing model (per token, per hour, per user)? Are there hard rate limits to prevent budget exhaustion? | Unpredictable pricing; lack of granular billing tags or cost attribution APIs. |
| **Model Quality & SLAs** | What is the guaranteed uptime? Is the model version pinned, or does it silently update? | "Rolling" model updates without version control (breaks deterministic testing). |

**Outcome:** An architecture decision (Approved, Conditionally Approved with Guardrails, or Rejected) documented in an Architecture Decision Record (ADR).

---

## Runbook 2: Onboarding and Deployment

Once an AI service is approved, it must be integrated into the enterprise ecosystem safely.

### Onboarding Steps

1. **Identity Integration:** Bind the AI service to the enterprise Identity Provider (IdP). Implement Least Privilege Access.
2. **Gateway Configuration:** Never allow applications to call the AI provider directly. Route all traffic through an internal AI API Gateway (e.g., Kong, Apigee, or a custom LLM proxy).
    - *Action:* Configure rate limiting, payload logging (for audit), and cost tagging at the gateway layer.
3. **Guardrails Implementation:** Deploy input/output filtering (e.g., NeMo Guardrails or Microsoft Azure AI Content Safety) to detect Prompt Injection and prevent PII leakage.
4. **Monitoring Setup:** Integrate the service with the enterprise observability stack. 
    - *Metrics to track:* Token usage per cost center, latency (Time to First Token), and error rates.
5. **Business Handover:** Provide the requesting team with the approved API endpoints, usage limits, and the required security headers.

---

## Runbook 3: Retiring or Migrating an AI Service

The AI landscape changes rapidly. A model that was state-of-the-art six months ago might be deprecated today. Retiring an AI service is more complex than retiring a traditional API because applications are often tuned to the specific "quirks" of a given model.

### Migration Checklist

1. **Impact Assessment:** Use the EA Repository to identify all applications and business capabilities dependent on the specific model version or service being retired.
2. **Alternative Selection:** Select a replacement model. Use the prompt evaluation sets (which should have been saved during onboarding) to test the new model.
3. **Prompt Tuning Phase:** Allocate time for engineering teams to adjust their prompts. *A prompt that works perfectly on GPT-4 may fail on Claude 3.5 Sonnet, and vice versa.*
4. **Traffic Shadowing:** Route a percentage of live traffic (e.g., 5%) to the new model in a "shadow" mode to compare responses and latency against the old model.
5. **Cutover and Decommissioning:** Gradually increase traffic to the new model. Once at 100%, revoke the API keys for the old service and remove the routing rules from the AI Gateway.

---

## The Concept of the "Golden Prompt" Library

As part of the Strategic Runbooks, the EA practice should maintain a "Golden Prompt" library or repository. 

Instead of every development team figuring out how to prompt the LLM to output valid JSON or how to format a RAG context window, the EA team provides validated, security-tested prompt templates. This ensures consistency, reduces token waste, and centralises security patches (e.g., adding "Do not execute code" to a base prompt).

---

*Sources: TOGAF Architecture Development Method (ADM) for AI 2025, FinOps Foundation AI Guidelines, OWASP LLM Top 10 Migration Strategies.*
