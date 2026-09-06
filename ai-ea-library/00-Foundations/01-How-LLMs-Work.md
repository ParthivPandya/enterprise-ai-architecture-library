# How LLMs Actually Work: A Primer for Architects

> *Before you govern something, you have to understand it. This chapter is for every enterprise architect who has been in a room where someone explained "the AI" and walked out knowing less than when they walked in.*

> **Related:** [02-Foundation-Model-Landscape.md](02-Foundation-Model-Landscape.md) | [../03-EA-Practice/02-AI-Design-Decisions.md](../03-EA-Practice/02-AI-Design-Decisions.md)

---

## The Problem With Most Explanations

Most LLM explainers fall into one of two failure modes. The first is for a developer audience — full of embedding dimensions, attention heads, and gradient descent — things an enterprise architect doesn't need to know to make good decisions. The second is for an executive audience — "it's like autocomplete, but really good" — which is technically true but so reductive it will cause you to make bad decisions about context windows, hallucination risk, and model selection.

This chapter is for the people in between: practitioners who need to understand what's actually happening inside these systems well enough to design around their strengths and govern around their weaknesses. You don't need to know how to train a model. You need to know enough to ask the right questions when someone else is building one.

Let me start with an honest observation: understanding how an LLM works did not stop IBM from failing at Watson for Oncology, Amazon from building a biased hiring tool, or Air Canada's chatbot from giving a passenger incorrect information that cost the company a legal judgment. Knowing how the technology works is necessary but not sufficient. You also need the governance architecture this library covers in other sections. But you can't build the governance if you don't understand what you're governing.

---

## What a Token Is and Why It Matters More Than You Think

Everything in LLMs starts with tokens. Not words — tokens. A token is roughly 3–4 characters of text, which works out to approximately ¾ of a word on average. The word "unfortunately" is one token. The sentence "The quick brown fox" is four tokens. A 1,000-word document is approximately 1,300 tokens.

Why does this matter for an architect?

Because **tokens are the unit of everything**: cost, speed, context, and capability. When AWS Bedrock charges you $0.003 per 1,000 input tokens, they're counting tokens. When you wonder why a model "forgot" something you told it earlier in a conversation, it's because the context window — measured in tokens — ran out. When a model gives you a surprisingly verbose answer to a simple question, it's generating output tokens, each of which costs money.

The context window is the number of tokens an LLM can process in a single interaction — input plus output combined. In 2023, GPT-3.5 had an 8,000-token context. By 2025, frontier models have context windows of 128,000 to 1,000,000 tokens. Claude models support up to 200,000 tokens. Google's Gemini 1.5 Pro reached 1 million tokens. This matters because context window size determines whether you can drop an entire contract, a full set of financial statements, or a complete codebase into a single prompt — or whether you need to chunk, summarise, and retrieve.

**The architectural lesson from tokens:**
- Every design decision that adds tokens (more verbose system prompts, larger retrieved chunks, more conversation history retained) costs money and increases latency
- Tokens are not a technical detail — they are a cost driver that belongs in your FinOps model from day one
- Context window limits are real architectural constraints, not suggestions

---

## The "Attention Is All You Need" Paper, Explained Without the Math

In 2017, a team at Google Brain published a paper called "Attention Is All You Need." It is one of the most cited papers in the history of computer science — over 173,000 citations by 2025. Everything you're reading about in this book — GPT, Claude, Gemini, Llama, Mistral — is built on what that paper introduced.

The problem the paper solved was this: how does a computer understand that in the sentence "The bank was steep, not financial," the word "bank" means a riverbank, not a financial institution? Previous approaches processed language word by word, left to right, like reading along a line. They were slow, struggled with long-range relationships, and couldn't be parallelised across GPU hardware.

The transformer architecture — what that paper introduced — works differently. It processes every word (token) in a sentence simultaneously and, for each token, calculates how much "attention" to pay to every other token. The word "bank" in that sentence pays very high attention to "steep" and low attention to "financial" — because that pattern, seen millions of times in training data, associated those words with physical banks rather than financial ones.

This mechanism, called **self-attention**, is what allows LLMs to:
- Understand pronouns ("she picked up the pen and threw **it** away" — "it" refers to "pen")
- Handle long-range dependencies across hundreds of pages of text
- Capture context that changes meaning ("I didn't say **she** stole the money" vs "I didn't say she **stole** the money")

And critically: because attention operates across all tokens simultaneously rather than sequentially, it can be massively parallelised across GPU hardware. This is why LLMs can be trained on trillions of tokens — because you can throw thousands of GPUs at it in parallel.

**The architectural lesson:**
- LLMs are fundamentally context machines. They do not "know" facts in the way a database stores facts. They have statistical patterns about which tokens follow which other tokens, given a context.
- This is why they hallucinate. There is no "facts table" to look up. When a model doesn't have strong statistical signal for an answer, it generates plausible-sounding tokens anyway.
- This is also why RAG (Retrieval-Augmented Generation) works — you're giving the model accurate context to condition its generation on, reducing its reliance on potentially stale or absent training data.

---

## Training, Fine-Tuning, and RAG: Three Different Things

This is where enterprise architects most often get confused, because vendors use these terms interchangeably and imprecisely. They are not the same thing. They solve different problems, at different costs, with different governance implications.

### Pre-Training: Building the Foundation

Pre-training is what creates the foundation model. OpenAI, Anthropic, Google, Meta — they train on trillions of tokens of text: the internet, books, code, scientific papers, Wikipedia. The model learns statistical relationships across all of it. This is expensive — frontier model training runs cost hundreds of millions to over a billion dollars in compute alone. It takes months. You are not doing this.

What pre-training produces is a model that is very good at predicting what text comes next. It knows language, concepts, reasoning patterns, and enormous amounts of factual information — but its knowledge is frozen at the training cutoff date.

**Governance implication:** When you use a foundation model API, you inherit its training decisions — including what data it was trained on, what biases that data contains, and what the provider's policy is on using your prompts to further train their models. Read the fine print.

### Fine-Tuning: Adjusting Behaviour

Fine-tuning takes a pre-trained model and trains it further on a smaller, domain-specific dataset. You might fine-tune a model on your company's contract templates to make it better at drafting contracts in your style. Or fine-tune on medical literature to improve clinical terminology.

Modern fine-tuning techniques like LoRA (Low-Rank Adaptation) and QLoRA make this much cheaper than it used to be — you can fine-tune a capable model on a consumer GPU in hours for a few hundred dollars. But it's still not trivial to do well.

**When fine-tuning is the right choice:**
- You need the model to consistently follow a specific format or style that prompting alone can't reliably achieve
- You have a specialised vocabulary or domain that the base model consistently gets wrong
- You want to reduce latency and cost by using a smaller model that has been made domain-expert through fine-tuning

**When fine-tuning is NOT the right choice:**
- You want the model to have access to specific facts (use RAG)
- You want to update the model's knowledge without retraining (use RAG)
- You want the model to stay current with changing information (fine-tuning bakes in a snapshot)

**Governance implication:** A fine-tuned model is a derived work. If your fine-tuning dataset contains sensitive information (patient records, employee data, customer PII), that information may be embedded in the model weights. This is not theoretical — model inversion attacks can sometimes extract training data. Apply DPDPA and privacy-by-design principles to fine-tuning datasets with the same rigour as to production databases.

### RAG: Grounding Answers in Real Data

Retrieval-Augmented Generation does not modify the model at all. Instead, when a user asks a question, the system first retrieves relevant documents from a knowledge base, then provides both the question and the retrieved documents to the model as context. The model generates an answer grounded in the retrieved documents rather than relying solely on training knowledge.

This is how enterprise search, policy Q&A systems, contract analysis tools, and document assistants work at scale. A lawyer asks about a clause in a contract — the RAG system retrieves the relevant contract clauses and the model answers based on those specific documents.

**Why RAG is so important for enterprise:**
- Your data is always current (you update the knowledge base, not the model)
- You can control exactly what the model has access to (access controls on the document store)
- Answers can be traced to source documents (audit trail)
- You can keep sensitive data on-premises while using a hosted model API

**The catch architects miss:** RAG is only as good as your data. If your knowledge base has stale documents, inconsistent formatting, or poor metadata, the retrieval will fail and the model will hallucinate anyway. The phrase "garbage in, garbage out" applies with a vengeance.

---

## Why LLMs Hallucinate (And What You Can Actually Do About It)

Hallucination — the NIST term is "confabulation" — is when an LLM generates information that sounds credible but is factually wrong. The model doesn't know it's wrong. There is no uncertainty signal in a standard LLM output. It generates the most statistically likely next token, and sometimes the most likely next token is incorrect.

Understanding why it happens reveals what you can actually do about it:

**Root cause 1: Absent training signal**
The model was never trained on data about your question. A model trained on internet data through 2024 was never trained on your company's Q3 2026 financial results. So when asked, it will generate something plausible. Fix: RAG — give it the data in context.

**Root cause 2: Conflicting training signal**
The model was trained on contradictory data — multiple sources saying different things. The model averages across them and produces something that sounds authoritative but is an incoherent blend. Fix: ground the model in a single authoritative source for your domain.

**Root cause 3: Out-of-distribution queries**
The model is asked something outside the distribution of its training data — a very specific technical question, a question about a niche domain, or a question about events after its cutoff. Fix: domain-specific fine-tuning or RAG.

**Root cause 4: Overconfident generation**
The model has been trained with RLHF (Reinforcement Learning from Human Feedback) to sound helpful and confident. Humans rate confident-sounding answers higher than uncertain ones. The model has learned to sound sure even when it isn't. Fix: prompt the model explicitly to express uncertainty ("If you are not sure, say so and explain what you do know").

**The enterprise mitigation stack:**
1. **RAG** for factual questions — ground the model in verified sources
2. **Output validation layer** — for critical facts, verify against a source of truth before returning to users
3. **Structured output** — constrain the model's output to a schema; it can't hallucinate fields that don't exist in the schema
4. **Explicit uncertainty prompting** — instruct the model to flag uncertainty
5. **Human review gates** — for high-stakes decisions, a human must review before action
6. **Evaluation harnesses** — test the system continuously with known-answer questions; alert when accuracy drops

---

## The Context Window: Your Most Important Architectural Constraint

Everything the model uses to generate its response must fit inside the context window. The system prompt, the user's question, any retrieved documents, and the conversation history — all of it counts against the limit.

This creates a fundamental architectural tension. You want to give the model as much context as possible so it can answer well. But more context means:
- Higher cost (you pay for every input token)
- Higher latency (longer context takes longer to process)
- Potential degradation of quality ("lost in the middle" problem — models attend less reliably to information in the middle of very long contexts)

**The architectural patterns that manage this tension:**

**Selective retrieval:** Don't dump your entire knowledge base into the context. Retrieve only the 3–5 most relevant chunks. Invest in retrieval quality — a bad retrieval produces worse results than no retrieval.

**Context compression:** Before sending conversation history to the model, summarise earlier turns rather than sending them verbatim. LLMLingua-style compression can reduce context by 3–5x with minimal quality loss.

**Session management:** For long-running conversations (customer support sessions, document review workflows), persist conversation state in a database rather than the model's context window. Retrieve relevant history at each turn.

**Sliding window:** For document processing, process the document in overlapping chunks rather than all at once. Each chunk overlaps with the previous by ~20% to preserve continuity.

---

## The Three Things Every Architect Must Hold In Their Head

After reading this chapter, you should be able to walk into any room and reason clearly about any LLM architecture question. The three things to hold:

**1. LLMs are pattern engines, not fact databases.**
They generate statistically likely text given a context. They do not know, in the sense that a database knows. They generate. This is why governance is not optional — every output needs a verification layer calibrated to the risk of the decision it informs.

**2. Context is everything.**
What you put in the context window determines what you get out. Architects who treat prompt design as someone else's problem are abdicating their responsibility for system behaviour. The system prompt is as consequential as any other configuration decision.

**3. The failure modes are predictable.**
Hallucination happens on absent, conflicting, or out-of-distribution data. Injection happens at boundaries between trusted and untrusted input. Cost explodes when attribution is absent. Performance degrades when data quality degrades. None of these are mysteries. They are engineering problems with engineering solutions — but only if you understand what's happening well enough to design the solutions in.

---

*Sources: "Attention Is All You Need," Vaswani et al., Google Brain, NeurIPS 2017 (173,000+ citations as of 2025). Atlan Transformer Model Architecture Guide 2026. DataCamp How Transformers Work 2026. SaM Solutions LLM Transformer Architecture Explained. Stanford HAI AI Index 2025. NIST AI 600-1 Confabulation risk category. PromptMetrics AI FinOps Context Window Economics.*
