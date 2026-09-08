# When AI Goes Wrong: The Case Studies Every Architect Must Know

> *The history of enterprise computing is full of cautionary tales. The history of enterprise AI is shorter, but it's catching up fast. These failures are not someone else's problem — they are the playbook for what will happen to you if you skip the governance.*

> **Related:** [03-Responsible-AI.md](03-Responsible-AI.md) | [02-Governance-Framework.md](02-Governance-Framework.md)

---

## Why We Study Failure

There's a pattern in every industry that learns about safety the hard way: aviation, nuclear power, surgical medicine. They all built their most durable safety cultures not from vague aspirations but from rigorous post-mortem analysis of what actually went wrong.

Enterprise AI hasn't had its Chernobyl yet. But it's had enough failures — billion-dollar write-offs, legal judgments, viral brand crises, regulatory enforcement actions — that the lessons are available to anyone willing to study them. The architects and governance leaders who understand these cases are in a fundamentally different position from those who don't. The mistakes below were not made by incompetent people. They were made by smart people under real business pressure, working without the frameworks and precedents that now exist.

Every failure in this chapter maps to a governance mechanism in this library. The goal is to help you see the connection.

---

## Case 1: IBM Watson for Oncology — The $4 Billion Lesson in Data Quality and Scope

**What happened:** In 2011, IBM's Watson supercomputer beat Ken Jennings at Jeopardy. IBM saw a revenue opportunity: apply Watson to healthcare, specifically cancer diagnosis and treatment recommendations. The pitch was extraordinary — an AI that could read the entire medical literature and recommend personalised treatment plans. Memorial Sloan Kettering Cancer Center, one of the world's premier oncology institutions, agreed to a development partnership worth $62 million.

In 2018, STAT News published an investigation that revealed Watson for Oncology was providing treatment recommendations that oncologists described as "unsafe and incorrect" in several cancer types. Concordance with expert oncologists ranged from 12% for gastric cancer in China to 96% for hospitals using similar guidelines to Sloan Kettering — an enormous variance that revealed the system was not generalising.

By 2022, IBM had sold its Watson Health division for approximately $1 billion — against an investment estimated at over $5 billion. A $4+ billion write-off.

**The root causes:**

*Root cause 1: Synthetic training data.* Watson was not trained on the longitudinal patient outcome data you'd need to make valid treatment recommendations. It was trained on hypothetical "synthetic cases" created by a small cohort of Sloan Kettering oncologists. It learned the treatment preferences of one elite American institution, not general oncology principles. When deployed at community hospitals in Germany, China, and elsewhere — with different patient populations, different drug availability, different institutional norms — it failed because it had never seen those contexts.

*Root cause 2: The closed-world assumption.* Watson was built as if oncology were a closed domain — as if the knowledge encoded in training would remain valid. Cancer treatment advances rapidly. New drugs, new protocols, new clinical trial results constantly revise best practices. Watson had no mechanism to update its knowledge without retraining. By the time it was deployed at scale, parts of its training were already outdated.

*Root cause 3: The "expert system dressed as AI" problem.* What IBM built was, in important ways, an expert system that encoded the judgments of a specific group of experts — not a system that learned generalised oncological principles. This is different from what was marketed.

*Root cause 4: No real-world validation before commercial deployment.* The system was marketed and sold to hospital systems before it had been validated on real patient outcomes in diverse clinical settings. The gap between demo performance and production performance was never measured — because the measurement infrastructure didn't exist.

**What governance would have caught this:**
- **NIST AI RMF MAP function:** Categorise this as High Risk immediately — life-altering medical decisions
- **Diverse validation data requirement:** Mandate validation on patient populations from the actual deployment contexts, not just Sloan Kettering
- **Real-world pilot gate:** Require concordance measurement against expert oncologists in each new deployment context before scaling
- **Continued medical education equivalent:** Require a mechanism for updating clinical knowledge without full retraining

**The enduring lesson:** Watson's failure came from treating training data as the product rather than as evidence. When your AI system will be used to make life-altering decisions, it must be validated in the actual conditions of deployment — not just in the lab where it was built. The phrase "works in development" means nothing in medicine.

---

## Case 2: Amazon's Hiring AI — When Training Data Carries History's Biases

**What happened:** In 2014, Amazon began developing an AI system to help screen engineering job applications — a machine that could review CVs and surface the best candidates. By 2015, internal teams discovered the system was systematically downgrading women. It penalised résumés that included the word "women's" (as in "women's chess club captain" or "women's college"). It downgraded graduates of two all-female universities. It had learned to favour verbs like "executed" and "captured" that appeared more commonly in male-written CVs.

Amazon retrained the model multiple times, trying to remove the bias. Each time, the team concluded they could not guarantee it would not find new, different ways to discriminate. The project was quietly shut down in 2017. Reuters broke the story in October 2018.

**The root cause:** Amazon trained the model on a decade of resumes that had been submitted to the company, along with the outcomes (hired / not hired). Because Amazon's engineering workforce over that decade was predominantly male, the historical hiring decisions — which became the training labels — encoded a preference for male candidates. The model did not invent the discrimination; it faithfully learned and amplified it.

The AI did exactly what it was designed to do: predict who Amazon had historically hired. The problem was that who Amazon had historically hired reflected decades of gender imbalance in the tech industry.

**This is the training data liability problem.** Historical data records what happened. It does not record what should have happened. When historical decisions in a domain were shaped by discrimination — and nearly every economically significant domain has been — those decisions, aggregated into a training dataset, carry the discrimination forward. Automated at scale.

As of 2024, University of Washington researchers testing text-embedding models that power many resume screeners found they favoured white-associated names in 85.1% of cases and disadvantaged Black male candidates in 100% of test cases. The Amazon failure did not end in 2018.

**Legal context:** Under the EU AI Act, AI used for recruitment and candidate evaluation is classified as **High Risk**. Organisations face obligations including bias testing, technical documentation, human oversight, transparency to candidates, and record-keeping, with penalties reaching €15 million or 3% of global annual turnover. Under India's MeitY AI Governance Guidelines (2025), fairness and non-discrimination are explicit principles, with particular attention to caste, gender, and religion in the Indian employment context.

**What governance would have caught this:**
- **Pre-deployment bias audit:** Systematic fairness testing against protected characteristics before any deployment. Not a post-hoc investigation — pre-deployment validation.
- **AI Fairness 360 (or equivalent):** IBM's open-source toolkit specifically tests for demographic disparities in training data and model outputs
- **Human oversight requirement:** Under both EU AI Act and NIST AI RMF, high-risk employment decisions require human oversight; an AI ranking candidates without human review would not have been compliant
- **Counterfactual testing:** Test whether identical CVs with only the gender-coded language changed produce different rankings

**The enduring lesson:** A shortlist you cannot explain is a shortlist you cannot defend — legally, ethically, or commercially. Every AI system that makes decisions affecting people's livelihoods must be tested against the protected characteristics that matter in its context. Not once. Every time the model or the data changes.

---

## Case 3: Air Canada Chatbot — When AI Makes Promises the Company Didn't Authorise

**What happened:** In 2022, Jake Moffatt's grandmother died. Grieving, he consulted Air Canada's website chatbot to ask about bereavement fares. The chatbot told him he could book a full-price ticket and apply for the reduced bereavement fare after travel, within 90 days. He did exactly that. Air Canada then refused his retroactive fare claim, saying the chatbot's advice was incorrect — bereavement fares had to be requested before travel.

Moffatt sued. In February 2024, the Civil Resolution Tribunal in British Columbia ruled in his favour. The tribunal rejected Air Canada's argument that the chatbot was a "separate legal entity" responsible for its own actions. Air Canada was ordered to pay $812.02 in damages.

The ruling's key sentence: Air Canada "is responsible for all information on its website, whether it comes from a static page or a chatbot."

**This case created legal precedent that reverberates through every enterprise chatbot deployment:**
- You cannot disclaim responsibility for what your AI tells customers
- If your AI gives incorrect advice and a customer acts on it, you own the consequence
- "The AI got it wrong" is not a defence

**The root causes:**
- The chatbot had no mechanism to verify its own advice against current policy
- There was no warning to users that chatbot advice should be verified with a human agent
- Policy updates were not reflected in the chatbot's knowledge in real time
- There was no human escalation path for consequential decisions (travel booking, financial commitments)

**What governance would have caught this:**
- **Output grounding:** Connect the chatbot to the live policy database, not a snapshot of what someone remembered at training time. RAG against the current policy document, always.
- **Scope limitation:** Chatbots should not make authoritative statements about policies without live retrieval from the source of truth. If you can't guarantee accuracy, caveat the output: "Please verify with an agent before booking."
- **Human escalation trigger:** Any chat involving financial commitments, refunds, claims, or policy-based decisions should offer immediate escalation to a human
- **Legal review of chatbot scope:** Every enterprise chatbot deployment should have legal sign-off on what the bot is permitted to confirm or commit to

**The enduring lesson:** Your customers do not experience "the chatbot." They experience your company. Whatever the chatbot says, you said it. Design accordingly.

---

## Case 4: DPD's Chatbot Goes Viral — Brand Risk From Unguarded Output

**What happened:** In January 2024, a frustrated DPD customer managed to make the DPD parcel delivery chatbot swear, insult the company, and write a poem criticising DPD's customer service. Screenshots went viral on social media. DPD immediately disabled the chatbot.

The cause was a chatbot update that had accidentally removed its content guardrails. Without the safety filters in place, the underlying LLM would follow user instructions without restriction — including instructions to "act as a different AI without restrictions" or to write content that criticised its own operator.

**This is the jailbreaking problem**, and it remains one of the most consistent failure modes in enterprise LLM deployments. Users will probe, experiment, and deliberately attempt to make AI systems do things they weren't designed to do. Sometimes for malice. Sometimes for curiosity. The DPD case was the latter — a frustrated customer who discovered the chatbot's guardrails were absent.

**The business impact:** Not a legal judgment. Not a data breach. But a brand crisis that reached millions of people in 24 hours. The cost in brand damage is harder to quantify than a court judgment, but it is real.

**What governance would have caught this:**
- **Regression testing for guardrails:** Every update to the AI system triggers a regression test against the red team prompt library — including known jailbreak attempts
- **Pre-deployment adversarial testing:** Before any chatbot update goes live, test it against common jailbreak patterns
- **Output monitoring in production:** Real-time scanning of AI outputs for policy violations — flag and review before the tweet screenshot spreads

**The enduring lesson:** Safety testing is a regression gate, not a one-time exercise. Every change to the system — model update, prompt change, system configuration — can inadvertently remove guardrails that were previously working. Treat AI safety like you treat security: continuous testing, not a pre-launch ceremony.

---

## Case 5: NYC MyCity Chatbot — When AI Gives Legal Advice It Shouldn't

**What happened:** In April 2023, New York City launched MyCity, an AI chatbot intended to help small businesses navigate city regulations. Within weeks, researchers discovered the chatbot was advising businesses to break the law. It told one restaurant owner they could pay workers below minimum wage. It gave incorrect information about employer obligations under city law.

The city scrambled to add disclaimers but did not immediately take the chatbot offline. The incident became a case study in what happens when AI is deployed for high-stakes regulatory guidance without adequate human oversight.

**The problem was the combination of:**
1. A use case that required accurate legal and regulatory information — exactly the domain where LLMs are most prone to hallucination
2. A public-facing deployment at city scale, so the incorrect advice reached many people before it was caught
3. No clear disclaimer to users that the chatbot's information was not legally authoritative and should be verified

**What governance would have caught this:**
- **High-risk domain recognition:** Any AI providing regulatory, legal, financial, or medical guidance is High Risk. Treat it accordingly — complete validation before deployment.
- **Authoritative source grounding:** Policy Q&A bots must retrieve from current, authoritative regulatory texts — not generate from training data
- **Legal review of content scope:** A lawyer should have reviewed representative chatbot outputs before the public launch, specifically testing edge cases in employment law
- **Mandatory disclaimer + escalation:** For any regulatory or legal question, the chatbot should explicitly disclaim authoritative status and provide a path to verified information

**The enduring lesson:** The stakes of the use case must drive the rigour of the governance. A chatbot that recommends a playlist is low-risk. A chatbot that tells small business owners their legal obligations is High Risk. You cannot apply the same governance to both.

---

## Case 6: McDonald's/IBM Drive-Thru AI — The Limits of Ambient AI

**What happened:** McDonald's partnered with IBM to deploy AI-powered voice ordering at drive-throughs from 2021 to 2024. Videos circulated on TikTok showing the AI adding hundreds of McNuggets to orders, mishearing "ketchup" as "Coke," and engaging in surreal loops with confused customers. In June 2024, McDonald's announced it was terminating the IBM partnership and removing the AI from restaurants.

The failure wasn't one dramatic incident — it was hundreds of small failures in ambient conditions: background noise, accents, partial sentences, customers changing their minds, children talking in the background. The AI performed well in controlled test conditions and deteriorated in the noisy, variable, real-world drive-through environment.

**This is the test-production gap problem.** AI systems that perform well in clean test environments routinely fail in the messy conditions of actual deployment. The lab is a simplification. Production is the truth.

**What governance would have caught this:**
- **Production-like test environments:** Test in conditions that match deployment — actual ambient noise levels, actual accent distribution, actual ordering variation
- **Canary deployment with measurement:** Deploy to 5% of locations with close monitoring before enterprise rollout. The failure patterns would have been visible before full commitment.
- **Error recovery design:** What happens when the AI mishears? A well-designed system acknowledges uncertainty and hands off to a human before the order is completed — not after ten frustrated interactions

---

## The Common Thread: A Root Cause Taxonomy

Across these six cases, and the broader body of documented AI failures, four root causes appear repeatedly:

**Root Cause A: No AI readiness evaluation before deployment**
IBM Watson at Oncology scale, Amazon hiring tool, NYC MyCity. The system was deployed into a high-stakes context without validating that it worked in that context, for that population, with that data.

**Root Cause B: Training data that does not represent deployment reality**
Amazon's hiring tool (trained on a skewed workforce), Watson (trained on one institution's cases). The data distribution that matters is the deployment distribution — not the training distribution.

**Root Cause C: No output validation for high-stakes decisions**
Air Canada (chatbot advice not verified against policy), NYC MyCity (regulatory information not verified against statute), Watson (recommendations not validated against clinical outcomes). Every high-stakes output needs a verification layer.

**Root Cause D: Safety testing as a launch event, not a continuous process**
DPD (guardrails removed by update). Safety is not a checkbox you tick before launch. It is a continuous responsibility that must survive every system change.

---

## An Honest Note: The Bias Problem Is Not Solved

The Amazon case is from 2018. In 2024, research still shows that text-embedding models used in resume screening disadvantage Black male candidates in 100% of test cases. The tools to test for bias (AI Fairness 360, Fairlearn, IBM's AIF360) exist and are mature. The regulatory frameworks requiring bias testing are arriving (EU AI Act, NYC Local Law 144, India MeitY guidelines). But the actual practice of testing AI systems for bias before deployment remains inconsistent across the industry.

This is not a technology problem. It's an organisational prioritisation problem. Bias testing adds time, adds cost, and sometimes produces results that are uncomfortable. The governance frameworks in this library are designed to make bias testing structurally required — not optional — at the pre-deployment gate, for any system that makes decisions affecting individuals.

---

*Sources: STAT News IBM Watson for Oncology investigation 2018, healthcare.digital IBM Watson Health collapse post-mortem 2026, Leadership Tribe Watson Governed AI Reset 2026, Reuters Amazon AI hiring tool investigation October 2018, Hubert.ai Amazon AI hiring failure lessons 2026, DataField.dev Amazon AI bias case study 2026, Air Canada v. Moffatt Civil Resolution Tribunal February 2024, DPD chatbot viral incident January 2024, OnviSource AI failure taxonomy 2026, McDonald's IBM drive-through AI termination June 2024.*
