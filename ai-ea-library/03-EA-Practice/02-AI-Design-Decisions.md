# How EA Practice Changes When AI Makes Design Decisions

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [03-Strategic-Runbooks.md](03-Strategic-Runbooks.md) | [../02-AI-Strategy/02-Agentic-AI-Use-Cases.md](../02-AI-Strategy/02-Agentic-AI-Use-Cases.md)

---

## The Inflection Point

For thirty years, Enterprise Architecture was a human-intensive discipline. Architects manually gathered data, modelled relationships, evaluated options, produced artefacts, and governed decisions. Every diagram, every trade-off analysis, every standards review required a human doing most of the work.

That model is giving way to something structurally different.

Agentic AI embedded in EA tools doesn't wait to be asked. It proactively monitors repository patterns, flags inconsistencies, suggests architecture options, and in some implementations, initiates corrective actions without waiting for human direction. **Ardoq's AI agents now handle an estimated 40% of routine EA work** — data collection, capability mapping, quality checks — automatically.

Gartner's prediction for 2028: **55% of EA teams will act as coordinators of autonomous governance automation**, shifting from direct oversight to model curation, certification, agent oversight, and business outcome alignment with machine-led governance.

This isn't a distant future. It is arriving in production EA tools today, and the architects who understand it will shape how it is implemented; those who don't will find it implemented around them.

---

## What AI Is Already Doing in EA Tools (2025–2026)

### Documentation and Repository Population

The most immediate AI contribution in EA tools is automated documentation generation — the work that previously consumed 30–40% of architect time:

- **AI Visual Importer** (Ardoq): imports architecture diagrams, spreadsheets, and documents into the EA repository without manual re-entry
- **AI-assisted modelling**: suggests components, relationships, and metadata based on existing patterns in the repository
- **Conversational AI**: allows stakeholders to query the architecture repository in natural language rather than learning complex query languages

**Practical impact:** Architects spend less time maintaining repository currency and more time interpreting what the repository reveals.

### Inconsistency and Compliance Detection

EA AI agents continuously monitor the repository for:
- **Architectural policy violations** — components or integrations that break defined standards
- **Relationship inconsistencies** — systems declared as isolated that have undocumented dependencies
- **Stale data** — assets in the repository whose attributes haven't been validated recently
- **Compliance gaps** — applications or data flows that don't map to the required regulatory controls

**Salesforce case:** Salesforce developed an internal AI agent that analysed over 100,000 architecture documents to support their enterprise architects. The tool identifies compliance gaps, automates pre-review of designs, and provides intelligent suggestions for standards alignment. By converting static documentation into "architectural intelligence," Salesforce reduced pre-review cycles from weeks to days.

### Pattern Recognition and Architecture Option Generation

Generative AI can now:
- Input design constraints (capacity, compliance requirements, cost targets) and generate multiple architecture pattern options
- Simulate performance of competing topologies before any infrastructure is built
- Identify patterns across historical designs that were successful vs. those that failed
- Recommend architecture choices based on stated business requirements matched against known patterns

**Practical example:** An architect designing a new data platform enters requirements (DPDPA compliance, real-time streaming, 50,000 concurrent users, India data residency, under ₹2 crore/year). The AI generates three architecture patterns meeting these constraints, evaluates each against the enterprise's standard frameworks, and surfaces trade-offs. The architect evaluates the options, applies judgment about organisational context, and makes the decision.

### Gap Analysis and Impact Assessment

Traditional gap analysis between current state and target architectures could take weeks. AI-powered gap analysis:
- Automatically compares current state and target state repositories
- Identifies missing capabilities, redundant components, and integration gaps
- Simulates the impact of proposed changes on dependent systems
- Prioritises gaps by business impact and remediation effort

**Outcome:** Gap analysis that took 4–6 weeks now takes days. The architect's role shifts from data gathering to validating AI-generated findings and applying contextual judgment.

---

## The Four Emerging Roles of the Enterprise Architect (Forrester, 2025)

Forrester's research on "The Future of the Enterprise Architect's Job" identifies four emergent roles:

### 1. Customer/Employee-Centric Value Mapper

Architects map customer and employee experiences within value streams, building knowledge graphs that connect architectural decisions to measurable business outcomes. The AI handles the data assembly; the architect provides the interpretive layer that connects technical architecture to human experience.

*What this looks like in practice:* Instead of diagramming application dependencies, the architect builds a "business outcome map" — how does the AI-enhanced customer journey connect to specific architecture decisions? Which components, if degraded, immediately impact which revenue streams?

### 2. Digital Twin Strategist

Architects simulate architecture options using AI-powered enterprise digital twins — virtual models of the enterprise that can be tested before changes are made to production.

*What this looks like in practice:* Before proposing a major platform migration, the architect runs the proposed future state through a digital twin simulation. The simulation reveals performance bottlenecks, compliance gaps, and dependency risks that static architecture review would have missed. The architect presents the simulation results, not just the architecture diagram.

**Market context:** The global digital twin market is projected to grow 60% annually and reach $73.5 billion by 2027 (McKinsey). Enterprise architecture is one of the primary use cases.

### 3. Enterprise Knowledge Curator

As AI agents generate, update, and connect architecture data continuously, the architect's role is to curate this knowledge — ensuring it is accurate, relevant, appropriately classified, and connected to business context that the AI cannot supply independently.

*What this looks like in practice:* The architect reviews AI-generated architecture assessments, corrects misclassified components, adds organisational context ("this system is scheduled for retirement in Q3 regardless of its technical quality"), and validates that AI-suggested architecture changes align with business strategy that isn't encoded in the repository.

### 4. Strategic Orchestrator (Human-in-the-Loop)

Architects become the critical human in the loop — the accountability layer between AI-generated recommendations and consequential decisions. As Forrester's Stéphane Vanrechem notes: the enterprise architect is an important human protecting the organisation and being responsible for the decisions and outcomes that agentic AI delivers.

*What this looks like in practice:* An AI agent proposes a change to the enterprise's API gateway configuration based on detected performance degradation. The architect reviews the proposed change, assesses whether it conflicts with any upcoming business initiatives, approves, and documents the decision. The AI executes; the architect is accountable.

---

## New Architecture Patterns Introduced by AI Systems

When AI systems are deployed at enterprise scale, they introduce architectural patterns that didn't exist in the pre-AI era. Enterprise architects must design, govern, and evolve these patterns.

### The Model-as-a-Service (MaaS) Pattern

AI models are increasingly consumed as services rather than built or hosted internally. The architectural implications:

```
Application → [API Gateway] → [Model Router] → Foundation Model (Provider)
                                    ↓
                             [Fallback Model]
                                    ↓
                         [Cost/Quality Monitor]
```

Key design decisions:
- **Model abstraction layer** — applications should not be directly coupled to specific model versions or providers. When GPT-4 is replaced by a newer model, the application should not require changes.
- **Circuit breaker pattern** — if the primary model API is unavailable, what happens? Route to a secondary model, return a cached response, or fail gracefully to a non-AI workflow?
- **Version control for models** — model versions must be tracked alongside application versions. A change in model version is a potential behaviour change that requires testing.

### The RAG Architecture Pattern

Retrieval-Augmented Generation connects a foundation model to an enterprise knowledge base. The architecture must manage:

```
User Query
    ↓
[Query Embedding]
    ↓
[Vector Database] ← [Document Ingestion Pipeline]
    ↓                       ↓
[Retrieval Layer]    [Document Governance]
    ↓                (access control, freshness,
[LLM with Context]    validation, versioning)
    ↓
[Output Validation]
    ↓
Response
```

**Architectural requirements the EA must ensure:**
- Document access controls mirror the underlying document permissions (a user cannot retrieve via AI what they couldn't access directly)
- Document freshness SLAs (outdated documents in the vector store produce outdated AI answers — define the maximum acceptable staleness)
- Document versioning (when a policy document changes, the vector store must be updated and old embeddings invalidated)
- Audit trail (which documents were retrieved for each query — required for DPDPA and regulated sector compliance)

### The Agentic Orchestration Pattern

Multi-agent systems where AI agents coordinate to complete complex tasks:

```
User Goal
    ↓
[Orchestrator Agent]
    ├── [Researcher Agent] → Web / DB
    ├── [Writer Agent] → Document generation
    ├── [Reviewer Agent] → Quality check
    └── [Publisher Agent] → System of record
```

**Architectural requirements:**
- **Inter-agent communication protocol** — how do agents pass work and context between them? Structured output schemas prevent interpretation failures.
- **Loop detection** — agents can get stuck in cycles. Maximum iteration counts and timeout policies are mandatory.
- **Permission isolation** — each agent has only the permissions required for its specific function. The Orchestrator cannot grant permissions the Researcher doesn't have.
- **Human escalation design** — when does the orchestrator decide an issue is beyond its scope and route to a human? Design this explicitly; don't leave it to the model's judgment.
- **Audit trail** — every agent action must be logged at the tool-call level. This is now a procurement requirement in regulated industries.

---

## The Governance Paradox: Governing Systems That Govern

The deepest tension in AI-augmented EA is this: enterprise architects are increasingly asked to govern AI systems using AI-augmented tools. The tools themselves are AI; the systems being governed are AI. This creates a governance loop that requires careful design.

**The risks:**
- AI governance agents may have blind spots — patterns of risk they cannot recognise because they weren't in their training data
- AI-generated architecture recommendations can be subtly optimised for the patterns in the EA repository, which may not fully represent future requirements or edge cases
- Over-reliance on AI governance automation can create a false sense of assurance — the dashboards look green while actual risk accumulates in unmeasured dimensions

**The architect's response:**
- Treat AI-generated governance outputs as input to human judgment, not as decisions
- Maintain human review for all AI recommendations affecting high-risk systems (regardless of how confident the AI appears)
- Conduct periodic "adversarial reviews" — deliberately test whether the AI governance system would catch known governance failures
- Document explicitly: "This decision was made by [human architect] based on [AI-generated analysis] reviewed on [date]. The AI analysis was checked for [specific risks]."

---

## Skills the Modern EA Must Build

The T-shaped architect — broad business and strategy skills plus deep technical expertise — is now specifically required to span human and AI domains:

| Traditional EA Skill | AI-Era Extension |
|---|---|
| Architecture modelling (ArchiMate, TOGAF) | AI-augmented modelling; digital twin simulation |
| Stakeholder management | Translating AI recommendations for non-technical executives |
| Risk assessment | AI-specific risk (OWASP LLM Top 10, NIST AI RMF) |
| Integration design | MaaS, RAG, and agentic orchestration patterns |
| Governance | AI system governance; agent accountability design |
| Technology radar management | AI model lifecycle; foundation model evaluation |
| Cost estimation | AI FinOps; token economics; build-vs-buy-vs-fine-tune |

**The minimum baseline for 2026:** Every enterprise architect should be able to independently prototype a simple RAG application, evaluate its governance requirements using the NIST AI RMF checklist, and estimate its 12-month operating cost. This is not optional; it is the price of meaningful participation in AI architecture decisions.

---

## Practical Transition: From "Traditional EA" to "AI-Augmented EA"

### What to do immediately

1. **Get hands-on with your EA tool's AI features** — whatever EA platform you use (LeanIX, Ardoq, Sparx, Bizzdesign), every major vendor has shipped AI capabilities in 2025–2026. Use them actively.

2. **Build one RAG prototype** — use your own architecture documents as the corpus. See what happens when a junior stakeholder queries your enterprise's reference architectures. What does the AI get right? What does it get wrong? This is more informative than any briefing paper.

3. **Map your AI system inventory** — every AI system in your enterprise needs to be in your architecture repository. Start with what exists; you may be surprised.

4. **Run an AI architecture review** — take the NIST AI RMF checklist and apply it to one live AI system in your organisation. Document the gaps. This exercise will immediately reveal what governance infrastructure needs building.

---

*Sources: Ardoq Agentic AI Future of EA April 2026, Forrester How Agentic AI Elevates EA Role August 2025, Forrester Future of the Enterprise Architect's Job 2025, CIO.com Agentic AI Makes EA Role More Fluid January 2026, Intelance Future of EA in AI Era 2026, StackAI Role of AI in Enterprise Architecture 2026, Digital Mehmet Enterprise Architecture Tooling 2026, McKinsey Digital Twin Market projections, Poniak Times Agentic AI Transforming EA 2026, Salesforce internal architecture AI case.*
