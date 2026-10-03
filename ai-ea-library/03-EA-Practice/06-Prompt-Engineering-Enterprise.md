# Prompt Engineering for Enterprise Teams

> *Individual prompting skill is not enough. Your organisation needs a shared discipline — a prompt library, an evaluation practice, and engineering standards that survive staff turnover. This chapter covers both the craft and the system.*

> **Related:** [05-LLMOps.md](05-LLMOps.md) | [../00-Foundations/01-How-LLMs-Work.md](../00-Foundations/01-How-LLMs-Work.md)

---

## The Craft That Became an Engineering Discipline

In early enterprise adoption, "prompt engineering" was often treated as an individual productivity skill. It has since become an engineering concern: prompts influence system behaviour, cost, safety, test results, and change control, and therefore need the same versioning and evaluation discipline as other application artifacts.

Structured instructions, examples, retrieval, and output schemas can improve performance for a particular model and task, but there is no universal improvement percentage. Measure prompt changes against a versioned evaluation set using the actual model, data, and workflow. Adoption is affected by usefulness, trust, integration, incentives, and training—not prompt structure alone.

The business case for investing in prompt engineering as an organisational discipline is clear. What follows is how to do it — the techniques, the enterprise practices, and the governance.

---

## The Anatomy of a Good Prompt

Before techniques, structure. Every effective prompt has four components:

**1. Role / Persona**
Who is the AI being asked to be? A senior contract lawyer reviewing for liability? A patient customer service agent? A careful code reviewer who flags security issues?

Role framing is not decorative — it activates relevant training patterns. An LLM responding as a "senior contract lawyer" will use different vocabulary, apply different scrutiny, and notice different issues than one responding without role context.

**2. Task / Goal**
What, specifically, is the AI being asked to do? The more precisely the task is defined, the more precisely the output matches what's needed. "Review this contract" is a bad task definition. "Review this contract for indemnification clauses that are broader than standard market practice, and flag each one with: the clause location, what makes it non-standard, and a suggested redline" is a good task definition.

**3. Context**
What does the AI need to know to do the task well? The relevant document, the applicable policy, the user's situation, the constraints that apply. Context is where RAG inserts retrieved documents. Context is also where you prevent the AI from asking clarifying questions by anticipating and answering them in the prompt itself.

**4. Output Format**
What should the response look like? If you need structured data, specify the format explicitly — JSON schema, markdown table, numbered list. If you need a specific length, specify it. If you need the AI to express uncertainty, say so. Without output format specification, the AI will make its own formatting choices, which are often inconsistent across calls.

---

## The Core Techniques: When to Use Each

### Zero-Shot Prompting
The simplest form: give the AI a task and let it respond from its training knowledge, with no examples.

**When to use:** Well-defined tasks where the model's training data contains abundant relevant patterns. Writing assistance, language translation, code explanation, general summarisation.

**When not to use:** Specialised formats, domain-specific terminology, highly specific output structures. When you need consistent formatting across many calls, zero-shot prompts produce too much variance.

**Example:**
```
You are a senior technical writer. Summarise the following product release notes 
in three bullet points, each under 20 words, suitable for a non-technical audience.

[Release notes here]
```

### Few-Shot Prompting
Provide the AI with examples — input/output pairs — before the actual task. The model generalises from the examples.

**When to use:** Specialised output formats, domain-specific transformations, tasks where you need consistent style or structure that's hard to describe but easy to demonstrate.

**The power:** A few well-chosen examples can communicate format requirements, tone, detail level, and edge case handling that would take paragraphs to describe. Studies show that even randomised labels in few-shot examples improve performance — the pattern of having examples matters, not just the label accuracy.

**Example for contract clause classification:**
```
Classify each clause as: STANDARD | NON-STANDARD | UNUSUAL

Example 1:
Clause: "Either party may terminate this Agreement with 30 days written notice."
Classification: STANDARD
Reason: 30-day notice period is industry standard for service agreements.

Example 2:
Clause: "Client may terminate this Agreement immediately for any reason or no reason."
Classification: NON-STANDARD
Reason: Immediate termination right without cause is unfavourable to vendor.

Example 3:
Clause: "Vendor warrants that all AI outputs are factually accurate and legally compliant."
Classification: UNUSUAL
Reason: AI accuracy warranty is rarely given by vendors; significant liability exposure.

Now classify this clause:
[Clause to classify]
```

### Chain-of-Thought (CoT) Prompting
Instruct the AI to reason through the problem step by step before giving the final answer. On complex reasoning tasks, this dramatically improves accuracy — the model uses the intermediate reasoning tokens to work through the problem rather than jumping to a conclusion.

**When to use:** Multi-step reasoning, legal analysis, financial calculations, architectural trade-off evaluation, any task where "jumping to an answer" frequently produces errors.

**Activation:** Add "Think step by step before giving your answer" or structure the output to require reasoning before conclusion. For the highest-stakes reasoning tasks, use reasoning models (o1, o3, DeepSeek R1) which do extended CoT internally.

**Example:**
```
You are a compliance officer reviewing an AI deployment proposal.

Analyse the following AI system against the EU AI Act risk classification framework. 
Think through each step:
1. What does the system do, and who does it affect?
2. Does it fall into any "Unacceptable Risk" categories? If yes, why.
3. Does it fall into any "High Risk" categories? If yes, which Annex III category?
4. What compliance obligations apply at this risk level?
5. What is your overall assessment and recommendation?

AI System Description:
[System description]
```

### Role Prompting
Assign the AI a specific persona with defined expertise, responsibilities, and perspective.

**When to use:** Any task where the right answer depends on a specific professional perspective — legal review, security assessment, financial analysis, clinical commentary.

**Important:** Role prompting is a signal, not a guarantee. The AI is not actually a lawyer or a doctor. In high-stakes domains, AI output with role prompting is input to a human professional's judgment — not a substitute for it.

**For enterprise use:** Define roles precisely. "You are a lawyer" is too broad. "You are a senior contract lawyer in India specialising in technology transactions, with deep familiarity with the IT Act, DPDPA, and standard SaaS agreement structures in the Indian market" is specific enough to be useful.

### Structured Output / Format Constraints
Specify the exact output format the AI should produce. JSON schemas, markdown tables, fixed-format reports.

**When to use:** Whenever the output will be processed programmatically, inserted into a document template, or needs to be consistent across many calls.

**Example with JSON schema:**
```
Analyse this contract clause and return your analysis in exactly this JSON format:
{
  "clause_type": "string",
  "risk_level": "LOW | MEDIUM | HIGH | CRITICAL",
  "risk_description": "string (max 100 words)",
  "suggested_action": "ACCEPT | NEGOTIATE | REJECT",
  "redline_suggestion": "string or null if accepting"
}

Return only the JSON object with no additional text, preamble, or explanation.

Clause: [clause text]
```

**Why it matters for enterprise:** Unstructured outputs require downstream parsing — a fragile, maintenance-heavy process. JSON outputs with a fixed schema can be directly ingested by downstream systems without parsing. This is the difference between an AI prototype and a production AI feature.

### Retrieval-Augmented Generation (RAG) as a Prompting Pattern
RAG combines retrieval with prompting: retrieve relevant documents, then inject them into the prompt context. From a prompt engineering perspective, how you structure the RAG context matters enormously.

**Effective RAG prompt structure:**
```
SYSTEM:
You are [role]. Answer questions based only on the provided documents.
If the answer is not in the documents, say "I cannot find this information 
in the provided documents" — do not guess or use external knowledge.

CONTEXT:
[Document 1 — title, source, date]
[Relevant chunk content]

[Document 2 — title, source, date]
[Relevant chunk content]

USER QUESTION:
[User query]

INSTRUCTIONS:
- Answer based only on the context above
- Cite the specific document and section for each claim
- If documents conflict, note the conflict and present both positions
```

**The "only on the provided documents" instruction is critical.** Without it, the model will supplement retrieved context with its training knowledge — potentially mixing accurate retrieved information with hallucinated "facts." Grounded generation requires explicit instruction.

### Prompt Chaining
Breaking a complex task into a sequence of simpler prompts, where the output of each step becomes input to the next.

**When to use:** Multi-stage tasks — research → synthesis → draft → review. Any task that is too complex to do well in a single prompt. Any task where intermediate quality checks are needed.

**Example (contract due diligence):**
```
Step 1: Extract all clauses related to liability and indemnification
Step 2: Classify each extracted clause by risk level
Step 3: For each HIGH or CRITICAL risk clause, draft a redline suggestion
Step 4: Produce a summary table of issues for the deal lead
```

Each step's output is reviewed (or at least inspected) before being passed to the next step. This allows quality control at intermediate stages and prevents a bad first step from propagating through the entire analysis.

---

## Enterprise Prompt Engineering: The System-Level Practices

Individual prompt skill is insufficient at scale. Your enterprise needs:

### 1. The Prompt Library

A curated, version-controlled repository of production-ready prompts for your organisation's recurring AI tasks. Every prompt in the library has:

- **Name and description:** What task it's for, when to use it
- **Current version and change log:** What changed in each version, and why
- **Test results:** Performance on the golden test set for this prompt
- **Approved by:** Who reviewed and approved this prompt for production
- **Known limitations:** What edge cases it doesn't handle well
- **Last reviewed:** When it was last tested against the current model version

The prompt library is not a Google Doc. It's a version-controlled repository (Git) with the same review and merge process as application code. Prompt changes go through code review. Prompts have owners. Prompts are retired when superseded.

### 2. Prompt Governance Policy

Answers the questions:
- Who can create prompts for production use?
- Who reviews and approves prompts before production deployment?
- What evaluation must a prompt pass before production use?
- How are prompts tested when the underlying model changes?
- How long can a prompt go without re-evaluation before it's considered stale?
- What happens when a prompt is found to produce harmful or non-compliant outputs?

This policy is lightweight for internal tools and more stringent for customer-facing applications. A prompt that populates an internal reporting template has different governance requirements than a prompt that gives customers advice about their financial situation.

### 3. Evaluation Harnesses for Prompts

For each production prompt, maintain:
- A minimum test set of 50–100 representative examples
- Automated evaluation scoring (LLM-as-judge, or task-specific metric)
- A baseline score that new versions must meet or exceed
- A regression alert when production quality drops below the baseline

This is exactly parallel to unit tests for code — and should be run with the same cadence.

### 4. The Prompt Engineering Training Programme

Everyone who uses AI tools professionally should know the basics. Build a tiered programme:

**Tier 1 — AI Users (all staff):** Zero-shot prompting structure, how to write a clear task, format specification, when to retry vs. when to escalate. 2-hour course, annual recertification.

**Tier 2 — AI Power Users (team leads, senior professionals):** Few-shot prompting, chain-of-thought, RAG basics, output validation. 4-hour workshop + 30-day mentored practice.

**Tier 3 — Prompt Engineers (dedicated practitioners):** Full prompt engineering curriculum — all techniques, evaluation methodology, prompt library management, adversarial testing. Ongoing professional development.

---

## Common Enterprise Prompt Engineering Mistakes

**Mistake 1: The System Prompt Kitchen Sink**
The system prompt contains everything — role, policy, examples, restrictions, formatting instructions, disclaimers. It's 2,000 tokens long, poorly organised, and the model can't hold it all in attention simultaneously. Result: inconsistent behaviour, high cost.

**Fix:** Keep system prompts focused. Put policies in retrieval (RAG), not in the system prompt. A system prompt over 500 tokens should be audited for what's actually necessary.

**Mistake 2: No Negative Examples in Few-Shot**
The few-shot examples only show correct outputs. The model doesn't see what to avoid.

**Fix:** Include at least one "negative example" showing an output that looks plausible but is wrong, with explanation of why it's wrong.

**Mistake 3: Inconsistent Output Format Specification**
"Return a JSON object" — but you don't specify the schema. The model returns JSON, but the keys are different in every call.

**Fix:** Always provide the exact JSON schema with field names, types, and (for string fields) length limits. Test that the model reliably produces schema-compliant output before production.

**Mistake 4: No Uncertainty Handling**
The prompt doesn't tell the model what to do when it doesn't know the answer. The model generates a plausible-sounding answer. The user trusts it. It's wrong.

**Fix:** Explicitly instruct the model to express uncertainty: "If you are not confident in your answer, say so and explain what you do know. Do not guess."

**Mistake 5: No Version Control**
The production prompt lives in a config file. Someone edits it directly in production to fix a bug. Nobody knows what changed. Six weeks later, the model's outputs have shifted and nobody can trace why.

**Fix:** Every production prompt is version-controlled in the prompt library. Changes go through a review and deployment process. Rollback is possible in minutes.

---

## A Worked Example: Building an Enterprise Prompt for Policy Q&A

Scenario: A financial services firm wants an AI that answers employee questions about HR policy, grounded in the official policy documents.

**Starting prompt (naive):**
```
Answer HR policy questions.
```

**Iteration 1 — Add role and grounding:**
```
You are an HR policy assistant. Answer questions based on the company's official 
HR policy documents. If you don't know the answer, say so.

[HR policy documents here]
```

Better. But still produces answers that blend policy with general assumptions, don't cite sources, and occasionally make up details.

**Iteration 2 — Add grounding constraint, citation requirement, uncertainty handling:**
```
ROLE: You are a precise HR policy assistant for [Company Name].

RULES:
1. Answer ONLY based on the provided policy documents below.
2. Cite the specific policy name and section for every claim.
3. If the answer is not in the provided documents, say: "I cannot find 
   this in our current policies. Please contact HR at hr@company.com."
4. Do not add information from general knowledge or assumptions.
5. If policies are ambiguous, present both interpretations and recommend 
   the employee confirm with HR.

POLICIES:
[Policy Document 1 — Name, version, effective date]
[Content]

[Policy Document 2 — Name, version, effective date]
[Content]

QUESTION: {employee_question}

FORMAT: Answer in 2-4 sentences. End with: "Source: [policy name], Section [X]."
```

**Iteration 3 — Add edge case handling and escalation:**
Add examples of the correct response for: a question that is in policy, a question that isn't in policy, and a question that is ambiguous. Add explicit instruction for sensitive topics (performance management, termination) to recommend direct HR contact.

**Evaluation before production:**
- Test against 100 representative HR questions from previous Help Desk tickets
- Measure: correct answer rate, citation accuracy, appropriate escalation rate
- Red team: try to get the model to reveal other employees' HR matters, make up policies, or give legal advice
- Baseline score established; any subsequent prompt version must meet or exceed it

This iterative process — not a one-time cleverness exercise — is what prompt engineering actually looks like in enterprise practice.

---

## References

1. NIST, [Generative AI Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1).
2. OpenAI, [prompt engineering guidance](https://platform.openai.com/docs/guides/prompt-engineering), provider-specific and subject to change.
3. Anthropic, [prompt engineering guidance](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview), provider-specific and subject to change.
4. Google Cloud, [prompt design strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies), provider-specific and subject to change.

Use provider guidance as implementation input, not independent evidence of business outcomes.
