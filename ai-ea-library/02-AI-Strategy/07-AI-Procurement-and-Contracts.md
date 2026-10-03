# AI Procurement and Contracts: What Every Enterprise Buyer Must Know

> **Document type:** Informative Guide
> **Primary audience:** Enterprise Architects, Procurement, Legal, Security, and Vendor Management
> **Last verified:** October 2026
> **Authority:** Architecture and procurement guidance, not legal advice. Verify vendor terms, regions, and applicable law before contracting.

> *You've evaluated the technology. You've run the pilot. The vendor has been enthusiastic, the demo was excellent, and now someone sends you a 47-page Master Service Agreement. This chapter is about what happens next — and why getting it wrong is expensive in ways that won't show up for eighteen months.*

> **Related:** [03-Strategic-Runbooks.md](../03-EA-Practice/03-Strategic-Runbooks.md) | [01-FinOps.md](../01-AI-Governance/01-FinOps.md) | [04-Indian-Enterprise-Context.md](04-Indian-Enterprise-Context.md)

---

## Why AI Contracts Are Different

Most enterprise software contracts were designed for a world of software licences, SaaS subscriptions, and professional services. AI contracts introduce dimensions that these templates don't cover well:

**The data ownership question.** When you use an AI API, your prompts — and the outputs — flow through someone else's infrastructure. Who owns the insights derived from your data? Can the vendor use your usage patterns to improve their model? If they do, are you inadvertently training a model that your competitors will also use?

**The model change question.** Software has version numbers and change logs. AI models change in ways that aren't always versioned or disclosed — the GPT-4 you integrated with in February 2024 was not the same system as the GPT-4 in October 2024. What happens to your production system when the underlying model's behaviour changes?

**The intellectual property question.** AI generates text, code, images. Who owns what it generates? If the model produces output that resembles training data it shouldn't have used, who is liable?

**The explainability question.** Regulated industries require that decisions be explainable. If an AI system makes a consequential recommendation (credit denial, medical triage, insurance pricing), can you explain why? Does the vendor's contract give you the data you need to construct that explanation?

These are not hypothetical concerns. The Air Canada chatbot ruling, the New York Times lawsuit against OpenAI, and dozens of regulatory investigations into AI outputs have all turned partly on questions that poorly-drafted contracts left unanswered.

---

## The Total Cost of Ownership Model

Before negotiating any AI contract, build a TCO model. Vendor pricing represents a fraction of the true cost of enterprise AI deployment.

### Direct Costs

**API / inference costs:** The most visible cost. Token-based pricing from LLM providers. Model your expected volume — daily active users × average tokens per session × working days = monthly token budget. Then model at 2x and 5x your initial estimate, because usage always grows faster than forecast.

**Platform / subscription costs:** Fixed monthly or annual fees for enterprise access, dedicated capacity, audit logging, support tiers.

**Fine-tuning costs:** If you're fine-tuning models on your data, training runs are charged separately (per-hour GPU pricing or per-token training pricing).

**Storage costs:** Vector databases, training data storage, model artefacts.

### Indirect Costs

**Integration:** Developer time to integrate the API into your application. Typically 2–4× the direct tool cost for the first integration, 0.5–1× for subsequent similar integrations once patterns are established.

**LLMOps infrastructure:** AI gateway, observability stack, evaluation harness. Treat these as shared infrastructure investments, not per-use-case costs.

**Data preparation:** Cleaning, labelling, and governance documentation of training or RAG data. Often the largest cost item, and almost always underestimated.

**Change management and training:** See [06-AI-Change-Management.md](../02-AI-Strategy/06-AI-Change-Management.md). Budget 10–20% of the total AI programme budget for organisational change.

**Ongoing governance:** AI system registry maintenance, security reviews, compliance audits, red team exercises. Budget 15–25% of annual run cost for governance overhead.

### The TCO Formula

```
Year 1 TCO = 
  Direct costs (API + platform + storage)
  + Integration costs (engineering time × fully loaded rate)
  + Infrastructure (LLMOps + gateway + monitoring)
  + Data preparation (cleaning + labelling + governance documentation)
  + Change management (training + communications + champions)
  + Governance overhead (audits + security reviews + compliance)
  + Executive time (programme management, steering committee)

3-Year TCO = 
  Year 1 TCO
  + Year 2 (direct costs × growth factor + reduced integration + governance)
  + Year 3 (direct costs × growth factor² + innovation investment + governance)
```

**A calibration example:** An enterprise deploying a document review AI system with 500 monthly users:
- Direct API costs: ₹15 lakh/year at expected volume
- Integration (2 engineers, 3 months): ₹30 lakh one-time
- LLMOps infrastructure: ₹6 lakh/year shared
- Data preparation: ₹10 lakh one-time
- Change management: ₹5 lakh one-time
- Governance overhead: ₹4 lakh/year
- **Year 1 TCO: ₹70 lakh** against ₹15 lakh in direct API costs — a 4.7× multiplier

This is typical. Enterprises that model only direct costs underestimate total investment by 3–6×, leading to mid-programme budget crises.

---

## The Critical Contract Clauses

This section covers the clauses that frequently go wrong in AI vendor contracts and what to negotiate.

### Data Handling and Training

**The clause you'll receive:**
*"Provider may use Customer Data to improve Provider's products and services."*

**Why this is dangerous:** This clause means your confidential prompts, your business logic embedded in system prompts, and your employees' queries are all training data for the vendor's next model — which your competitors will then use. You may be inadvertently funding your competitors' AI advantage.

**What to negotiate:**
*"Provider will not use Customer Data, Customer prompts, or Customer-generated outputs to train, fine-tune, or improve Provider's models or products without Customer's prior written consent."*

Most major providers offer this on enterprise plans (OpenAI Enterprise, Anthropic Business, Google Workspace Enterprise). The key is to explicitly request it and confirm it in the signed agreement — not just the standard terms.

**DPDPA implication:** Under India's DPDPA, using personal data for purposes beyond the stated processing purpose (including AI model training) requires additional consent. Any AI vendor processing Indian residents' personal data must agree to this restriction or obtain separate consent for training use.

### Intellectual Property in Outputs

**The clause you'll receive (vendor-favourable):**
*"Customer is responsible for all outputs generated using the Service. Provider makes no representations regarding the intellectual property status of outputs."*

**What this doesn't address:** If the model generates output that substantially reproduces copyrighted training data — the New York Times sued OpenAI and Microsoft precisely over this — who is liable? The current legal landscape in India, the US, and the EU is unsettled, but enterprise buyers should understand they are assuming liability for output use in the absence of explicit vendor indemnification.

**What to negotiate:**
*"Provider will indemnify Customer against third-party intellectual property claims arising from Provider's model training data, provided Customer uses the Service in accordance with applicable usage policies."*

Many vendors now offer a form of this indemnification (Microsoft Copilot Copyright Commitment, Google's generative AI IP indemnity, Anthropic's indemnification for business customers). Get it in writing in your contract, not just in a public policy that can be changed unilaterally.

### Model Versioning and Stability

**The clause you'll receive:**
*"Provider may update the Service at any time without notice."*

**Why this is dangerous for production systems:** A model update can change output quality, format, safety behaviour, and reasoning patterns. If your production application depends on specific model behaviour — and all production applications do — an undisclosed model update is a silent production incident waiting to happen.

**What to negotiate:**
*"Provider will give Customer 30 days notice before any change to the model version serving Customer API traffic. Provider will maintain the previous model version for 60 days following deprecation notice. Customer may pin traffic to a specific model version."*

**Practical minimum:** At minimum, negotiate model version pinning — the ability to specify which model version your API calls use, regardless of what the vendor deploys as "latest." This is available on all major providers; confirm it is contractually guaranteed, not just a feature that can be removed.

### Uptime and SLA

**The clause you'll receive:**
*"Provider will use commercially reasonable efforts to maintain 99.9% availability."*

**The math problem:** 99.9% uptime = 8.76 hours of downtime per year. For a customer service AI handling 50,000 daily interactions, 8.76 hours of downtime is 18,250 unresolved customer contacts — or, if the downtime happens during peak hours, far more.

**What to negotiate:**
- Define "availability" precisely: API responding within SLA latency threshold (not just "not returning errors")
- Define measurement methodology: third-party monitoring, not vendor self-reporting
- Credit schedule: meaningful credits (20–30% of monthly fee) for SLA violations — not the 10% nominal credit that's standard in many agreements
- Exclusions should be narrow: scheduled maintenance windows with advance notice, not "any maintenance Provider deems necessary"

**Fallback architecture is the real answer:** No SLA eliminates the risk of vendor outage. Design your application with fallback to a secondary model provider or graceful degradation. The contract SLA is a financial backstop, not an operational guarantee.

### Data Residency

**Critical for Indian enterprises:**
*"Customer Data may be processed in any jurisdiction where Provider maintains facilities."*

Under DPDPA, if you are processing personal data of Indian residents, you need control over where that processing occurs. Even if DPDPA doesn't currently mandate data localisation for your data category, this may change — and retrofitting residency requirements into existing contracts is significantly harder than specifying them upfront.

**What to negotiate:**
*"Customer Data, including Customer prompts containing personal data of Indian residents, will be processed exclusively in [India-region data centres]. Provider will not transfer such data to any other jurisdiction without prior written consent."*

**Practical check:** Before signing, verify that the vendor actually has India-region infrastructure with the AI models you need. As of 2026, AWS Bedrock, Azure OpenAI, and Google Vertex AI have India-region deployments, but not all models are available in all regions. Confirm the specific model version you need is available in the India region in the contract.

### Audit Rights

**Why this matters:** DPDPA requires data principals to be able to exercise rights over their data (access, correction, erasure). You need to be able to audit how a vendor is processing that data to respond to those requests.

**What to negotiate:**
*"Customer has the right to audit Provider's data processing activities related to Customer Data, upon 30 days written notice, not more than once per year. Provider will cooperate with regulatory examinations related to Customer Data processing."*

**Alternative:** A third-party audit certification (SOC 2 Type II, ISO 27001) that you receive annually — acceptable if the certification scope explicitly covers the data processing relevant to your agreement.

### Contract Exit and Data Return

**What to negotiate:**
*"Upon contract termination, Provider will: (a) within 30 days, return all Customer Data in machine-readable format; (b) within 60 days, certify deletion of all Customer Data from Provider's systems; (c) provide written confirmation of deletion upon request."*

**Fine-tuned models:** If you've fine-tuned a model on the vendor's platform using your proprietary data, negotiate in advance: do you own the fine-tuned model weights? Can you export them? If the vendor goes out of business or the platform is discontinued, what happens to your fine-tuned model?

---

## The Vendor Due Diligence Process

Before contract negotiation begins, run the vendor through Runbook 2 from [03-Strategic-Runbooks.md](../03-EA-Practice/03-Strategic-Runbooks.md). Additionally, conduct this AI-specific due diligence:

**Technical due diligence:**
- Request the vendor's AI system card or model card for the specific model you'll be using
- Request the vendor's red team testing methodology and results summary (they won't share full results, but should be able to confirm the programme exists)
- Test the model's performance on your specific use case with your data — not vendor-provided demos
- Verify model version pinning capability in a sandbox environment before signing

**Governance due diligence:**
- Review the vendor's Responsible AI policy or AI principles
- Confirm the existence of an AI governance/ethics review process (IBM, Microsoft, and Anthropic all publish this; smaller vendors often don't have it)
- Request the vendor's incident response history: have there been AI-related security incidents? How were they disclosed and addressed?

**Financial due diligence:**
- For smaller AI vendors: assess funding runway, customer concentration, and acquisition risk. An AI vendor acquired by a competitor may change access terms.
- For pricing: model the 3-year cost at 3 different volume scenarios. Token pricing that's attractive at pilot scale often becomes the largest single IT cost item at enterprise scale.
- Confirm pricing lock-in terms: how much can the vendor change pricing, and with how much notice?

---

## The India-Specific Vendor Landscape

Beyond the global hyperscalers, several vendors are specifically relevant for Indian enterprise AI procurement:

**Sarvam AI:** Indian AI company building foundation models specifically for Indian languages. Sarvam-2B is trained on Indian languages with strong performance on Indic NLP tasks. For enterprises serving multilingual Indian populations, Sarvam's models (available via API and self-hosted) are worth evaluating alongside global alternatives.

**Krutrim (Ola):** India's first AI unicorn, founded by Ola's Bhavish Aggarwal. Building India's own LLM with Indic language focus. Enterprise API access in limited preview as of 2026.

**TCS AI.Cloud, Infosys Topaz, Wipro AI360:** The major Indian IT services firms have all built AI platforms and GenAI service offerings. For enterprises that prefer a single vendor relationship covering implementation and platform, these are credible options — especially where on-premises or sovereign deployment is required.

**Contract consideration for Indian IT vendors:** Indian IT services contracts often bundle AI platform licensing with implementation services in ways that obscure the individual cost components. Require separate line-item pricing for: platform/licences, implementation services, support, and any third-party model API pass-through. Bundled pricing makes it very difficult to benchmark costs or switch components independently later.

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): Thomson Reuters Legal Guide to AI Contracts 2025, Forrester AI Vendor Evaluation Guidance 2025, NASSCOM AI Contract Best Practices for Indian Enterprises 2025, Clifford Chance AI Contracting Guide 2025, New York Times v. OpenAI lawsuit filings, Microsoft Copilot Copyright Commitment documentation, AWS AI Service Terms updated 2025, IAPP AI Contract Guidance 2026, Sarvam AI and Krutrim product documentation 2026.*