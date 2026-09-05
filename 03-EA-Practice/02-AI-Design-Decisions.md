# How EA Practice Changes When AI Makes Design Decisions

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [03-Strategic-Runbooks.md](03-Strategic-Runbooks.md)

---

## The Shift from Creator to Orchestrator

Historically, Enterprise Architects spent a significant portion of their time gathering requirements, drawing diagrams (UML, ArchiMate, BPMN), and mapping dependencies manually. 

As AI—specifically Agentic AI and advanced LLMs—enters the EA toolkit, the friction of artifact creation drops to near zero. An architect can prompt an AI: *"Generate a target state architecture for our customer onboarding process using event-driven microservices, compliant with DPDPA, and output it as ArchiMate XML."*

When AI can make initial design decisions and generate the architecture artifacts, the EA's role fundamentally shifts:
- **From Creator to Reviewer:** You are no longer drafting the blueprint; you are inspecting the AI-generated blueprint for structural integrity, compliance, and enterprise context.
- **From Modeler to Prompt Engineer:** The skill shifts from knowing how to draw a box in an EA tool to knowing how to constrain an AI to generate the *right* box.
- **From Documenter to Orchestrator:** Connecting AI agents that analyse codebases, reverse-engineer legacy systems, and propose modernisation paths.

---

## The Risks of AI-Generated Architecture

When an AI proposes a design decision, it does so probabilistically. This introduces unique risks into the architecture practice:

### 1. The "Plausible but Wrong" Architecture (Hallucination)
An LLM might design an elegant microservices architecture that relies on a specific AWS service that is not actually available in the required region (e.g., AWS ap-south-1), or it might invent a connector between two SaaS platforms that doesn't exist.
**The EA's Job:** Verify environmental constraints. AI doesn't know your enterprise's specific vendor agreements or legacy network firewalls unless explicitly told.

### 2. Loss of "Why" (The Black Box Decision)
If an AI decides that a graph database is better than a relational database for a specific module, *why* did it make that choice? Architecture Decision Records (ADRs) require rationale.
**The EA's Job:** Force the AI to show its work. Every AI-generated design must be accompanied by an AI-generated ADR that is then heavily audited by the human architect.

### 3. Context Collapse
AI models often lack the implicit, undocumented knowledge of the enterprise—the "we tried that three years ago and it failed because of company politics" context. 
**The EA's Job:** Inject enterprise context into the prompt chain or RAG (Retrieval-Augmented Generation) pipeline used by the EA tools.

---

## Architecture as Code to Architecture as Prompt

The industry moved from Visio to "Architecture as Code" (Structurizr, PlantUML) to version-control designs. Now, we are moving to "Architecture as Prompt."

| Era | Methodology | EA Focus |
|---|---|---|
| **Manual (Visio/Draw.io)** | Drag and drop, manual lines | Presentation, visual alignment |
| **Code (PlantUML/C4)** | Declarative text-to-diagram | Version control, logical structure |
| **AI (Prompt-to-Architecture)** | Natural language to target state | Constraints, context injection, validation |

### Injecting Constraints via Prompts
To successfully use AI for design decisions, EAs must build robust "System Prompts" for their architecture tools. A good architecture prompt includes:
1. **Current State Context:** (e.g., "We are a Java/Spring Boot shop heavily invested in Azure.")
2. **Regulatory Constraints:** (e.g., "PII data cannot cross the Indian border.")
3. **Architecture Principles:** (e.g., "Favour managed services over self-hosted. Event-driven over synchronous REST.")

---

## Evaluating AI-Suggested Architectures

When an AI proposes a design, use this framework to evaluate it:

1. **The Feasibility Check:** Does this technology actually exist and integrate the way the AI claims?
2. **The Constraint Check:** Does this violate any of our hard constraints (budget, compliance, existing vendor lock-in)?
3. **The Complexity Check:** Did the AI over-engineer the solution? (AI often defaults to complex, trendy architectures like Kubernetes/Kafka when a simple serverless function would suffice).
4. **The Transition Check:** The AI can design the target state, but did it account for the migration path from the current legacy state?

---

## The New EA Toolchain

The EA toolchain is evolving rapidly to incorporate AI decision-making:

- **AI-Augmented EA Repositories:** Tools like LeanIX and Ardoq are embedding AI to automatically map dependencies by reading code repositories and cloud configurations.
- **Generative Design Tools:** Using LLMs to convert meeting transcripts directly into C4 model diagrams.
- **Automated Governance Agents:** AI agents that run in CI/CD pipelines, checking proposed infrastructure-as-code against the EA policies.

**The takeaway:** Do not ban AI from making design decisions. Instead, build the review gates, validation frameworks, and contextual prompts required to harness its speed safely.

---

*Sources: Gartner Hype Cycle for Enterprise Architecture 2025, Forrester: The AI-Empowered Architect 2026, BDAT Academy EA Insights, Structurizr & C4 Model Community AI extensions.*
