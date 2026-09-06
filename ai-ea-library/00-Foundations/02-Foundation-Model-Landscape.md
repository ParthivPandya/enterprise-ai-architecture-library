# The Foundation Model Landscape: Navigating the Ecosystem

> *Every six months the landscape shifts enough to invalidate whatever chart you drew last time. This chapter won't give you a static comparison table that's already out of date. It gives you the mental model to evaluate any model, from any provider, at any point in time.*

> **Related:** [01-How-LLMs-Work.md](01-How-LLMs-Work.md) | [../03-EA-Practice/03-Strategic-Runbooks.md](../03-EA-Practice/03-Strategic-Runbooks.md)

---

## Why This Is Harder Than It Looks

In 2023, you could have a sensible conversation about "GPT-4 vs. Claude 2" and make a reasonable model selection decision. By 2025, the Stanford AI Index tracked over 50 significant foundation models released in a single year. The field has moved from a duopoly to a genuine ecosystem — closed-source frontier labs, open-weight models from Meta and Mistral, specialised domain models for medicine and law and code, small models that run on a laptop, and massive multimodal systems that handle text, images, audio, and video simultaneously.

For enterprise architects, the temptation is to compare benchmarks. Resist it. Benchmarks measure what models do in standardised test conditions. Your use case is not a standardised test. What matters is how the model performs on your specific tasks, with your data, at your scale, under your compliance constraints. Benchmarks are a starting point for shortlisting, not a basis for selection.

What follows is a structured way to think about the landscape — the categories, the key players, and the decision framework.

---

## The Ecosystem in Four Categories

### Category 1: Closed-Source Frontier Models (API Access Only)

These are the most capable models available, trained at enormous scale by companies with billion-dollar compute budgets. You access them via API — you never see the weights, and the provider controls the model, updates it, and sets the pricing.

**OpenAI (GPT series)**
The model that started the enterprise GenAI wave. GPT-4 Turbo and GPT-4o (multimodal) remain widely deployed in enterprise. The LLM Suite deployed to 50,000–140,000 JPMorgan employees uses OpenAI models — updated every eight weeks as the bank feeds it more data. OpenAI's enterprise product offers dedicated capacity, audit logging, and data processing agreements suitable for regulated industries.

The thing to know: OpenAI's model versioning has been inconsistent. Models are updated silently in ways that change behaviour, which can break production applications. Always pin to a specific model version in production. Never use the "latest" alias for anything customer-facing.

**Anthropic (Claude series)**
Claude's distinguishing characteristic has always been instruction-following fidelity and long-context reliability — handling 200,000-token contexts without the quality degradation at longer ranges that other models showed. The Claude 4 series (Opus 4.6, Sonnet 4.6 as of 2026) leads several reasoning and complex instruction benchmarks. Anthropic's Constitutional AI training approach produces a model that is noticeably more careful about harmful outputs than some competitors — useful for enterprises with strict responsible AI requirements.

The thing to know: Claude is often the right choice for document-heavy workflows (contracts, regulations, medical records) because of its long-context reliability. Anthropic's safety orientation makes it the preferred choice for enterprises with explicit Responsible AI policies.

**Google (Gemini series)**
Gemini 1.5 Pro introduced the million-token context window — large enough to process an entire codebase or book collection in a single prompt. Google's integration with Workspace (Docs, Sheets, Drive) makes Gemini the natural choice for enterprises already on Google Cloud, where the data locality and IAM integration are production-ready. Gemini Ultra leads on multimodal benchmarks — text, images, audio, and video in a single model.

The thing to know: Google's model naming has been confusing (Bard → Gemini; Ultra/Pro/Nano tiers). Clarify exactly which model you're evaluating. Vertex AI is the enterprise deployment platform — not consumer Gemini.

**The closed-source risk that enterprises underweight:** You are dependent on the provider's roadmap, pricing decisions, and continuity. OpenAI, Anthropic, and Google can change pricing, deprecate models, alter terms of service, or be acquired. This is not hypothetical — OpenAI has deprecated models with 90-day notice. Your architecture must be model-agnostic at the application layer; tight coupling to a specific provider's API syntax is technical debt.

---

### Category 2: Open-Weight Models (Deploy Anywhere)

Open-weight models give you the model weights — you can download them, run them yourself, fine-tune them, and deploy them without ongoing API fees. This changes the governance picture entirely: you control the data, the compute, and the model behaviour.

**Meta Llama (3.1, 4, and beyond)**
Meta's decision to release Llama as open-weight triggered what DataCamp called an "open-weights revolution." Llama 3.1 405B (the largest variant) approaches frontier model performance on many benchmarks. Llama 3 70B punches well above its size. The Llama 4 series (released 2025) extended multimodal capabilities to open-weight models.

For Indian enterprises: Llama is available for deployment on-premises, in NIC's MeghRaj Government Cloud, or in India-region private cloud. This matters enormously for DPDPA compliance and data residency requirements. An enterprise that processes sensitive financial or healthcare data and can't send it to a US-based API can still access near-frontier capability by self-hosting Llama.

**Mistral (Mistral 7B, Mixtral, Mistral Large)**
Mistral AI (France) built its reputation on efficiency — Mistral 7B outperformed models twice its size when it launched. The Mixtral architecture (Mixture of Experts) gets large-model capability at smaller-model inference cost by routing each token to a subset of specialised "expert" sub-networks. This is production-relevant: Mixtral 8x7B delivers GPT-3.5-class performance at significantly lower inference cost.

For European enterprises: Mistral is a French company with European data processing infrastructure — directly relevant to EU AI Act compliance and GDPR data residency.

**DeepSeek (R1, V3)**
DeepSeek's January 2025 release sent shockwaves through the industry. R1 matched OpenAI o1 on reasoning benchmarks at a fraction of the training cost, and the model was released as open-weight. V3, released December 2024, demonstrated that Chinese open-weight models had reached genuine frontier capability. DeepSeek proved that the capital advantage of US frontier labs was not as durable as assumed.

Enterprise caution: DeepSeek is a Chinese company. Enterprises in regulated industries (government, defence, financial services) need to carefully evaluate data jurisdiction and supply-chain risk before deploying DeepSeek in sensitive contexts, regardless of the model's technical quality.

**Google (Gemma series)**
Gemma is Google's open-weight offering — designed to be deployable on consumer hardware and fine-tunable. Gemma 2 performs well in its size class and is the natural open-weight choice for organisations standardised on Google Cloud infrastructure.

---

### Category 3: Specialised Domain Models

The open-weight revolution enabled a new category: models fine-tuned on domain-specific data to outperform frontier models in specific tasks, often at a fraction of the inference cost.

**Legal:** Harvey AI (built on Claude, fine-tuned on legal data), Lexis+ AI, Thomson Reuters CoCounsel. These models understand legal terminology, citation formats, and contract structures that general-purpose models handle imperfectly.

**Healthcare:** Med-PaLM 2 (Google, trained on medical datasets), Meditron (EPFL/Yale, open-weight medical model), Hippocratic AI. These models are fine-tuned on clinical literature and demonstrate higher concordance with clinical guidelines than general LLMs.

**Finance:** BloombergGPT (Bloomberg, trained on 700B financial tokens), FinGPT (open-source), various bank-proprietary models. Financial terminology, numerical reasoning, and regulatory language are handled better in domain-specific models.

**Code:** GitHub Copilot (OpenAI Codex), Amazon CodeWhisperer, Tabnine, Codeium. Code-specific models understand syntax, APIs, and programming patterns at a depth general models don't match. DeepSeek Coder and Code Llama are strong open-weight alternatives.

**For enterprise architects:** Domain models are worth evaluating whenever your primary use case is narrow and specialised. A legal department processing contracts will likely get better results from Harvey or a fine-tuned legal model than from a general frontier model, often at lower cost per task.

---

### Category 4: Small / Edge Models

The frontier labs have invested heavily in making powerful models run on constrained hardware — laptops, mobile devices, industrial equipment, and edge compute without cloud connectivity.

**Phi-3 (Microsoft):** Microsoft's Phi-3 Mini demonstrated that careful training data curation can produce remarkable capability in a very small model. Phi-3 Mini (3.8B parameters) performs above its weight class, specifically on reasoning tasks. Suitable for deployment on a laptop CPU.

**Gemma 2B / Llama 3 8B:** Both are capable enough for many enterprise tasks (document classification, summarisation, Q&A with RAG) and small enough to run on single-GPU inference servers without the cost of frontier-model API calls.

**On-device models:** Apple's Private Cloud Compute and on-device models, Samsung's Gauss, and Qualcomm's on-device AI push demonstrate that AI is moving toward edge-native deployment for latency and privacy reasons. For Indian enterprises serving rural markets with inconsistent connectivity, on-device models are not a future consideration — they are a present requirement.

---

## The Build / Buy / Fine-Tune Decision Framework

This is the most consequential architectural decision for any AI use case. Most teams agonise over it unnecessarily because they don't apply a structured framework. Here it is:

```
START: What is the business requirement?
         ↓
Does a commercial API solve ≥80% of the requirement
without requiring your proprietary data for training?
         │
        YES → Use the API (Buy). Stop here.
         │
        NO
         ↓
Does an open-weight model in the right size class
handle your domain well enough with prompting alone?
         │
        YES → Self-host the open-weight model.
              (Consider for data residency or cost reasons)
         │
        NO
         ↓
Do you have domain-specific training data
that would meaningfully improve model performance,
AND is the performance gap worth the fine-tuning cost?
         │
        YES → Fine-tune an open-weight model on your domain data.
         │
        NO
         ↓
Is this capability truly proprietary, strategic,
and defensible as a competitive moat?
         │
        YES → Consider building a custom model.
              (This requires ML team + budget + long timeline)
         │
        NO → Revisit the requirement definition.
             You may be over-engineering.
```

**The economic reality:** Building from scratch is 10–50x more expensive than buying an API. Fine-tuning is 3–10x more expensive than buying. The vast majority of enterprise AI use cases should be Buy first. Self-hosting open-weight models is worth evaluating when data residency requirements, cost at scale, or regulatory constraints make API access problematic.

---

## Evaluating a Model for Your Use Case: A Practical Protocol

Step 1: Define your golden test set. Before you evaluate any model, create 50–100 representative examples from your actual use case — real inputs with ideal outputs. This becomes your evaluation harness.

Step 2: Run every candidate model against your test set. Don't rely on published benchmarks — measure on your data. Use LLM-as-judge scoring (another model evaluates output quality) for scalable evaluation, supplemented by human review of borderline cases.

Step 3: Measure what matters: accuracy on your test set, latency (p50, p95, p99), cost per query at your expected volume, context window fit for your typical inputs.

Step 4: Check the governance requirements. For your use case, does the provider offer: a signed Data Processing Agreement, data residency in India/EU as needed, audit logging, no training on your data by default?

Step 5: Evaluate the abstraction layer. Can your application code swap the model without being rewritten? If not, architect the abstraction layer before going to production. You will change models.

Step 6: Test adversarially. Run your red team prompt library against each candidate. Does the model comply with your content policy? Does it resist prompt injection? Does it protect system prompt content?

---

## The Multi-Model Reality: Why You Will Run More Than One

In 2025, the median enterprise AI portfolio ran 3–5 different models across different use cases. This is not chaos — it's rational. Different tasks have genuinely different requirements:

| Use Case | Appropriate Model | Why |
|---|---|---|
| Complex reasoning, long documents | Frontier (Claude Opus, GPT-4o) | Accuracy justifies cost |
| Customer support chat | Mid-tier (GPT-4o Mini, Sonnet) | Speed and cost at volume |
| Code completion | Code-specific (Copilot, CodeLlama) | Domain expertise |
| Sensitive data processing | Self-hosted open-weight (Llama 3) | Data residency |
| Edge / offline | Small model (Phi-3, Gemma 2B) | Connectivity constraint |
| Batch document classification | Smaller model with fine-tuning | Cost at bulk volume |

The architectural implication: you need a model abstraction layer and an AI gateway from day one. Not as an aspiration — as a pre-condition for anything you build. LiteLLM or Portkey provide this layer. An application that is directly coupled to the OpenAI SDK is not production-ready — it is one pricing change or API deprecation away from requiring a rewrite.

---

## What Has Changed Since 2024 (And What It Means)

**Open-source caught up.** In 2023, the gap between frontier closed models and the best open-weight models was significant. By 2026, DeepSeek R1 and Llama 4 closed that gap on most standard benchmarks. For enterprises that need on-premises or data-resident deployment, the capability penalty for going open-weight has dropped dramatically.

**Reasoning models changed the calculus.** OpenAI o1/o3 and DeepSeek R1 introduced "reasoning models" — models that spend additional tokens on internal chain-of-thought reasoning before producing an answer. They are slower and more expensive per query but dramatically more accurate on complex multi-step problems. Enterprise use cases involving legal analysis, financial modelling, and architectural trade-off evaluation benefit from reasoning models. Customer service chatbots do not.

**Multimodal is now standard.** In 2023, multimodal was a feature. In 2026, every frontier model handles images as standard input. For enterprises, this opens use cases that were previously impossible: processing scanned documents, quality control from images, reading charts and diagrams. The architectural question is no longer "does the model handle images?" but "how do you manage multi-modal data in your RAG pipeline?"

**Context windows stopped being a constraint for most use cases.** A million-token context window means you can drop an entire codebase, a full year of contracts, or a complete case file into a single prompt. The architectural implication: some use cases that required complex RAG pipelines in 2023 can now be handled with direct in-context processing. Evaluate whether your RAG infrastructure is still necessary for each use case.

---

*Sources: Stanford HAI AI Index 2025, DataCamp Transformer Model Landscape 2026, OpenAI Enterprise Product documentation, Anthropic Claude Enterprise documentation, Meta Llama 4 release notes, Mistral AI model documentation, DeepSeek R1 technical report January 2025, Google Gemini 2.0 release documentation, Microsoft Phi-3 technical report, CNBC JPMorgan LLM Suite reporting September 2025, Gartner AI Model Selection Framework 2026.*
