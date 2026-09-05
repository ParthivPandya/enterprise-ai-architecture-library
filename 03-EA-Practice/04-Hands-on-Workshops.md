# Hands-on Workshops for AI Architecture

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [02-AI-Design-Decisions.md](02-AI-Design-Decisions.md)

---

## Moving Beyond "Death by PowerPoint"

The fastest way to kill momentum in an enterprise AI initiative is to conduct endless theoretical architecture review boards and conceptual presentations. AI is highly empirical. You cannot "architect" a good prompt or a vector search strategy purely on a whiteboard; you have to build it and see where it fails.

Enterprise Architecture must shift its engagement model from **Discussion-Only Seminars** to **Hands-On Labs**. EAs must facilitate environments where business and technical stakeholders can safely experiment, break things, and learn the architectural realities of AI.

---

## Workshop Format 1: The AI Design Sprint (Ideation to Prototype)

**Target Audience:** Business Leaders, Product Managers, Lead Engineers, Data Architects.
**Goal:** Take a vague business problem ("We need AI to help customer support") and turn it into a concrete architectural hypothesis and a working prototype.

### Agenda (2 Days)

*   **Day 1: Deconstruction & Mapping**
    *   **Morning:** Map the current business process using a simplified ADM Phase B approach. Identify the specific bottlenecks where probabilistic decision-making (AI) is better than deterministic logic.
    *   **Afternoon:** Select the highest-impact use case. Sketch the architecture pattern (e.g., RAG vs. Agentic vs. simple LLM call). Identify the required data sources.
*   **Day 2: Rapid Prototyping**
    *   **Morning:** Using low-code AI builders (e.g., Langflow, Flowise, or Microsoft Copilot Studio), the technical team builds a functional prototype while the business team defines the evaluation metrics.
    *   **Afternoon:** "Demo and Destroy." Test the prototype against edge cases. Document the architectural gaps discovered (e.g., "The vector DB latency is too high," or "We don't have the right metadata on these documents").

**EA Deliverable:** A validated Architecture Vision (Phase A) and a realistic assessment of the Information Systems architecture required (Phase C).

---

## Workshop Format 2: The Architecture Red Team Lab

**Target Audience:** Security Architects, Cloud Engineers, Governance Leads, Developers.
**Goal:** Discover the failure modes of a proposed AI architecture before it reaches production.

### The Setup

Unlike a traditional security review which involves reading a design document, a Red Team Lab is active. The EA team provisions an isolated "sandbox" environment containing a replica of the proposed AI system (e.g., a RAG application hooked up to dummy HR data).

### The Exercises

Participants are split into teams and given specific "attacks" to attempt against the architecture, aligned with the OWASP LLM Top 10:

1.  **The Jailbreak Challenge:** Can you force the LLM to output a restricted system prompt or reveal its underlying instructions? *(Tests the robustness of the system prompt and input guardrails).*
2.  **The Data Exfiltration Challenge:** Can you use Indirect Prompt Injection (via a malicious document uploaded to the RAG system) to trick the LLM into sending data to an external server? *(Tests network egress controls and output parsing).*
3.  **The DoS (Denial of Service) Challenge:** Can you exhaust the API quota or create a computationally expensive query that degrades performance for others? *(Tests API Gateway rate limiting and FinOps controls).*

**EA Deliverable:** A hardened technology architecture (Phase D) and a prioritized list of guardrails required for the Implementation Governance (Phase G).

---

## Workshop Format 3: The FinOps / Token Economics Simulation

**Target Audience:** FinOps Teams, Product Owners, Cloud Architects.
**Goal:** Understand how architecture decisions directly impact the variable costs of AI, and establish the FinOps framework.

### The Simulation

AI costs are highly variable and tied to "Token Economics." In this workshop, participants use a spreadsheet or a custom dashboard to simulate the cost of an AI application at scale.

**Scenarios Modeled:**
*   **Scenario A:** Calling GPT-4 for every user query vs. routing simple queries to a smaller, cheaper model (like Llama 3 8B) and only escalating complex queries to GPT-4.
*   **Scenario B:** The cost impact of a bloated system prompt (e.g., sending 5,000 tokens of context on every single API call).
*   **Scenario C:** The ROI of implementing a Semantic Cache (where repeated questions are answered from a cache without hitting the LLM provider).

**EA Deliverable:** An agreed-upon cost governance framework, including budget alerts, model tiering strategies, and architecture patterns for cost optimization.

---

## Setting up the "EA Sandbox"

To facilitate these workshops, the Enterprise Architecture team must own and maintain an "EA Sandbox" — a pre-approved, secure cloud environment where tools like Jupyter Notebooks, local LLMs (via Ollama), and vector databases are readily available for immediate use during a workshop.

Without the sandbox, you will spend the entire workshop waiting for IT to provision access.

---

*Sources: McKinsey: Rewiring the Enterprise for AI (2025), TOGAF ADM Agile Practices, NIST AI RMF Playbook (Measure Phase).*
