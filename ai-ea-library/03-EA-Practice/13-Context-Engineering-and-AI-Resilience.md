# Context Engineering and AI Resilience

> **Document type:** Informative Guide  
> **Primary audience:** AI Architects, Application Architects, LLMOps Teams  
> **Use when:** Designing context assembly, memory, retrieval, fallback, and continuity  
> **Last verified:** October 2026  
> **Authority:** Independent practitioner guidance  

---

## 1. From Prompt Engineering to Context Engineering

A prompt is only one input to an enterprise AI interaction. Runtime behaviour can also depend on policy, identity, conversation history, retrieved documents, tool results, memory, model configuration, and output constraints. **Context engineering** is the architecture discipline of selecting, ordering, constraining, and evidencing those inputs.

```text
System policy
User identity and purpose
Conversation state
Retrieved enterprise knowledge
Tool observations
Agent memory
Model and generation configuration
Output schema and validation
```

The context assembly pipeline is an application component and security boundary, not string concatenation hidden inside product code.

## 2. Context Layers

| Layer | Purpose | Typical Risk |
|---|---|---|
| System policy | Defines role, constraints, and escalation | Override or leakage |
| Identity context | Carries user, role, purpose, jurisdiction | Impersonation or over-sharing |
| Task context | Describes the current goal and expected output | Ambiguity or scope expansion |
| Retrieved context | Grounds output in approved sources | Poisoning, stale content, access bypass |
| Conversation state | Preserves local interaction continuity | Accidental retention or prompt injection persistence |
| Episodic memory | Stores selected prior events | Incorrect or sensitive durable memory |
| Procedural memory | Stores approved methods or workflows | Obsolete procedure |
| Tool observations | Returns external state | Untrusted content or hidden side effects |

## 3. Context Contract

Define a context contract for each AI application:

| Field | Question |
|---|---|
| Permitted sources | Which repositories or tools may contribute context? |
| Authority order | Which source wins when instructions conflict? |
| Identity filtering | How are access rights applied before retrieval? |
| Freshness | How old may each source be? |
| Token budget | How much context is allocated to each layer? |
| Sensitive data | What may enter model context, logs, or memory? |
| Retention | What is ephemeral, session-bound, or durable? |
| Provenance | How does output link back to source segments? |
| Failure behaviour | What happens when authoritative context is absent? |

## 4. Memory Architecture

### 4.1 Memory classes

- **Working memory:** current task state; expires with the workflow.
- **Conversation memory:** selected interaction history; session or user scoped.
- **Episodic memory:** prior events useful to future decisions.
- **Semantic memory:** durable facts derived from governed sources.
- **Procedural memory:** approved workflows, policies, and operating procedures.

Do not store model-generated text as durable truth without validation. Durable memory writes SHOULD pass schema, provenance, sensitivity, and authority checks.

### 4.2 Memory write gate

```text
Candidate memory
    ▼
Purpose check
    ▼
PII / sensitivity check
    ▼
Source and confidence validation
    ▼
Human approval where consequential
    ▼
Versioned memory store + expiry
```

## 5. Context Poisoning Controls

| Attack or Failure | Control |
|---|---|
| Indirect prompt injection in documents | Separate instructions from data; scan and label untrusted text |
| Malicious memory write | Allow-list writable fields; validate source and purpose |
| Stale policy | Effective dates, owner, and automated freshness alerts |
| Cross-user context leak | Identity-aware retrieval and tenant isolation |
| Retrieval flooding | Per-source quotas, ranking diversity, deduplication |
| Citation laundering | Verify that cited passages actually support the statement |
| Tool-output injection | Treat tool results as untrusted data and validate schema |

## 6. Context Economics

Larger context can increase cost and latency without improving quality. Allocate a measurable budget:

| Budget | Example Measure |
|---|---|
| System and policy | Maximum fixed tokens |
| Conversation | Summarisation threshold |
| Retrieval | Maximum chunks and per-source quota |
| Tools | Maximum observation size |
| Output | Maximum tokens and required schema |
| Total | Cost and latency SLO |

Evaluate answer quality across context sizes. Do not assume the largest window is the best architecture.

## 7. Resilience Model

AI resilience includes model, context, tool, provider, and control-plane failure.

### 7.1 Failure modes

| Failure | Degraded Mode |
|---|---|
| Primary model unavailable | Approved secondary model or deterministic workflow |
| Retrieval unavailable | Clearly disclose that grounded answer is unavailable; do not guess |
| Vector index stale | Use last verified snapshot within freshness policy or stop |
| Tool unavailable | Queue reversible work; route to human |
| Safety/policy service unavailable | Fail closed for high-risk action |
| Observability unavailable | Stop high-risk automation or switch to supervised mode |
| Cost limit reached | Use lower-cost approved model, reduce non-essential context, or queue |
| Region unavailable | Activate approved regional recovery architecture subject to data constraints |

### 7.2 Service objectives

Define:

- **RTO:** time to restore an acceptable service mode
- **RPO:** acceptable loss of conversation, memory, index, and evidence state
- **Quality degradation limit:** lowest acceptable quality in fallback
- **Control degradation rule:** controls that may never be bypassed
- **Manual capacity:** volume humans can safely absorb during fallback

An application is not resilient if the model endpoint survives but grounding, identity, policy, or audit evidence is unavailable.

## 8. Resilience Test Scenarios

1. Primary model times out during a multi-step agent workflow.
2. Retrieval returns no authoritative source.
3. A poisoned document ranks first.
4. Memory store is available but stale.
5. Policy engine is unavailable.
6. Secondary model produces a different output schema.
7. Regional failover conflicts with residency policy.
8. Manual fallback exceeds human capacity.
9. Trace export fails during a high-risk action.
10. Provider changes a model behind a stable alias.

Record expected behaviour, actual behaviour, evidence, and corrective action.

## 9. Architecture Review Checklist

- [ ] Context layers and authority order are explicit
- [ ] Retrieval is identity- and purpose-aware
- [ ] Durable memory has write validation and expiry
- [ ] Untrusted context cannot issue executable instructions
- [ ] Citations are tested for entailment, not only presence
- [ ] Token, cost, and latency budgets are defined
- [ ] Fallback preserves mandatory controls
- [ ] RTO/RPO cover memory, retrieval, policy, and evidence—not only the model
- [ ] Secondary models and schemas are regression-tested
- [ ] Manual fallback capacity is measured

## References

1. NIST, [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1).
2. OWASP, [Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).
3. NIST, [Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final), used here as general resilience reference.
4. MITRE, [ATLAS](https://atlas.mitre.org/).

