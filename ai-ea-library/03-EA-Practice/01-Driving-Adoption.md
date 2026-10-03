# EA's Role in Driving AI Adoption

> **Related:** [02-AI-Design-Decisions.md](02-AI-Design-Decisions.md) | [03-Strategic-Runbooks.md](03-Strategic-Runbooks.md) | [../01-AI-Governance/02-Governance-Framework.md](../01-AI-Governance/02-Governance-Framework.md)

---

## The EA Positioning Problem

When AI arrives in an enterprise, it often bypasses Enterprise Architecture entirely. A business unit sponsors a GenAI pilot with a vendor. The vendor integrates directly with a few APIs. Results are demo'd to the CEO. Procurement is announced. EA is brought in to "bless" the architecture — after the key decisions are already made.

This pattern is expensive, insecure, and ungovernable at scale. The architecture decisions made in a 90-day pilot define the boundaries of what can be done for the next 3–5 years.

**The EA mandate in AI adoption:** Be present at the problem definition stage, not the solution approval stage. Enterprise architects who show up after vendor selection has occurred have forfeited their strategic role.

---

## Why AI Cannot Be "Bolted On"

Traditional IT integration — even complex ERP implementations — maintained system determinism: given input X, the system produces output Y. AI breaks this.

The architectural implications of non-determinism:
- **Testing and QA** change fundamentally — you cannot write deterministic test cases for probabilistic outputs
- **Integration contracts** must account for variable response formats and occasional failures
- **Data flows** become bidirectional — data used for inference creates training signals for future models
- **Governance** must be continuous, not point-in-time
- **Rollback** is not a simple "revert to previous version" — model behaviour cannot be rolled back to a prior state without reverting to a prior model

**Enterprise architects must build these realities into their AI architecture patterns before deployment, not discover them in production.**

---

## Applying TOGAF ADM to AI Adoption

TOGAF's Architecture Development Method provides the most widely adopted structured approach for AI adoption. Here is how each ADM phase applies:

### Preliminary Phase: AI Readiness Assessment
Before any AI project begins, assess organisational readiness:

- **Architecture capability**: Does the EA team have AI literacy? Can they evaluate LLM architectures, RAG systems, and agentic designs?
- **Data readiness**: Are data sources accessible, quality-assured, and governed? (The most common killer of AI projects)
- **Governance readiness**: Is there an AI governance framework, or does one need to be built?
- **Infrastructure readiness**: What cloud, compute, and networking capacity is available? What's the connectivity to AI provider APIs?

**Deliverable:** AI Architecture Readiness Report — red/amber/green across dimensions, with remediation plan for red items.

### Phase A: Architecture Vision — AI Strategy Alignment

This is the "why" phase. The question is not "what AI technology should we use?" but "what business problems should AI solve, and what does success look like?"

Enterprise architects drive this by:
- Facilitating business capability analysis — where do AI capabilities create the most strategic value?
- Translating business intent into architectural requirements (latency, scale, data needs, governance)
- Identifying and categorising AI opportunity backlog (quick wins, strategic bets, exploratory)
- Establishing the AI architecture principles that will guide all subsequent decisions

**AI Architecture Principles (examples):**
1. Every AI system must have an identified owner accountable for its outputs
2. No AI system is deployed to production without a documented rollback plan
3. Personal data processed by AI systems must comply with applicable data protection law from day one
4. AI cost governance (FinOps) is a first-class requirement, not an afterthought
5. Human oversight is preserved for all AI-assisted decisions that materially affect individuals

### Phase B: Business Architecture — AI Use Case Mapping

Map AI capabilities to the business capability model. For each business capability:
- Is AI potentially applicable?
- What is the current maturity of that capability?
- What would an AI-enhanced version of this capability look like?
- What is the priority (based on strategic value and feasibility)?

**Output:** AI Opportunity Heat Map — business capabilities plotted by strategic value (vertical) and feasibility (horizontal). Top-right quadrant = prioritised AI investments.

### Phase C: Information Systems Architecture — Data and Application

**Data Architecture for AI:**
- Data lineage: where does training data come from? What transformations are applied? (Required for DPDPA DPIA and NIST MAP)
- Data quality: AI systems trained on poor-quality data produce poor-quality outputs. Data quality standards must be higher for AI training than for traditional analytics.
- Feature stores: enterprise AI at scale requires centralised, governed feature stores — not every team reinventing data preparation
- Vector databases: RAG architectures require vector storage; this is new infrastructure that must be designed, governed, and secured

**Application Architecture for AI:**
- Integration patterns: REST API vs. event-driven vs. streaming for AI inference calls
- Caching layer: semantic caching reduces cost and latency for high-traffic AI applications
- Fallback and circuit breaker patterns: what happens when the AI API is unavailable?
- Multi-model architecture: not every AI application uses one model; design for model-as-a-service at the enterprise level

### Phase D: Technology Architecture

**Infrastructure decisions for AI:**
- Cloud provider selection and AI service availability by region (critical for India data residency)
- GPU / dedicated AI inference hardware requirements (for on-premises or private cloud)
- Network capacity: LLM inference calls can generate significant data volume; model responses much larger than traditional API responses
- Edge AI requirements: where latency or connectivity constraints require on-device inference

**Key architectural decisions:**
- Build vs. buy vs. fine-tune: for each AI use case, what's the right relationship with foundation models?
- Single-provider vs. multi-provider: most enterprises are moving to multi-provider architectures; design the abstraction layer
- Private vs. public deployment: for sensitive data, does the AI need to run in a private model environment?

### Phase E: Opportunities and Solutions

Where business architecture meets technology: which AI use cases are ready to build now, and in what sequence?

**Sequencing principles:**
1. Prioritise quick wins (high value, low complexity) to build confidence and generate funding
2. Build shared infrastructure first — data platform, AI gateway, observability — before use cases
3. Sequence use cases to reuse infrastructure across them (don't build five separate RAG pipelines)
4. Align with compliance readiness — DPDPA Phase 1 in November 2026 means data governance infrastructure must precede AI use cases involving personal data

### Phase F: Migration Planning

The AI migration plan is different from a traditional IT migration because:
- Models must be retrained and evaluated, not just redeployed
- User behaviour changes with AI (trust calibration, prompt learning) require change management that traditional IT migration planning doesn't account for
- Governance infrastructure must be in place before production deployment, not after

### Phase G: Implementation Governance

EA's role in AI implementation goes beyond architectural review:
- **AI system registry**: EA owns and maintains the authoritative registry of all AI systems in the enterprise
- **Architecture review gates**: every AI system passes through an EA-led review before production deployment
- **Standards compliance**: AI systems are verified against enterprise AI architecture standards
- **Vendor management**: EA evaluates new AI vendor capabilities and maintains the approved vendor register

### Phase H: Architecture Change Management

AI architectures degrade faster than traditional IT architectures because:
- Models drift (data distribution changes; model behaviour changes)
- AI provider APIs evolve rapidly (new capabilities, deprecations, pricing changes)
- Regulatory requirements are actively developing (DPDPA Rules 2025 just published; EU AI Act provisions rolling in through 2026)

**Architecture change triggers for AI:**
- Model performance metrics fall below defined thresholds
- New regulatory requirement affecting deployed AI systems
- New business requirement exceeding current AI system scope
- Significant change in AI provider capabilities or pricing

---

## EA's Bridging Function: Business and Technology

The most valuable thing an enterprise architect can do in AI adoption is translate — in both directions:

**Translating technology to business:** What does "LLM with RAG" mean in business terms? What can it do, what can't it do, what does it cost, what does it risk?

**Translating business to technology:** The business wants "AI that understands our contracts." What does that mean architecturally? RAG over a document corpus? Fine-tuned legal model? Multi-agent contract review pipeline? Each answer has different cost, quality, and governance implications.

**The translation outputs that matter most:**
- AI capability descriptions in business language (not "large language model" — "AI that reads, summarises, and answers questions about any document")
- Business case templates that connect AI investment to business outcomes (see [../02-AI-Strategy/01-Business-Value.md](../02-AI-Strategy/01-Business-Value.md))
- Risk explanations that non-technical executives can act on (not "prompt injection" — "a way that users or documents can manipulate what the AI does, potentially bypassing security controls")

---

## The EA-Enabling vs. EA-Governing Tension

Enterprise architects face a permanent tension in AI adoption: **enabling innovation quickly vs. governing risk rigorously**. Both are necessary. Neither alone is sufficient.

The governance failure mode: EA becomes a bottleneck. Every AI experiment requires an 8-week architecture review. Business units route around EA entirely.

The enabling failure mode: EA approves everything quickly without adequate risk assessment. A critical AI system fails publicly. EA is blamed for inadequate governance.

**The resolution:** Risk-proportionate governance.

| AI Risk Level | EA Involvement | Review Time |
|---|---|---|
| Experiments / pilots (non-production data, no customer impact) | Self-service with architecture guardrails | None required |
| Internal tools (production, but limited scope and data sensitivity) | Light-touch review with standardised checklist | 1 week |
| Customer-facing (limited risk, clear human oversight) | Standard architecture review | 2–3 weeks |
| High-risk (personal data, significant decisions, public-facing at scale) | Full architecture board review | 4–6 weeks |
| Regulated / critical (financial decisions, healthcare, legal) | Extended review with external sign-off | 6–12 weeks |

The categories must be defined clearly so teams know from day one which track they're in. Ambiguity creates the worst of both worlds: slow and insecure.

---

## EA Competency Development for AI

A 2025 University of Melbourne paper identified a critical gap: TOGAF, as currently defined, lacks the agility, ethical governance, and lifecycle artefacts required for AI-driven transformation.

The paper recommends creating hybrid roles — "AI-EA strategists" — and embedding AI literacy into EA certifications. Key competency areas:

| Competency Area | What It Covers |
|---|---|
| **AI Architecture Patterns** | RAG, fine-tuning, agentic systems, multi-model architectures |
| **LLM/MLOps** | Model versioning, monitoring, evaluation, deployment pipelines |
| **AI Risk Assessment** | NIST AI RMF application; OWASP LLM Top 10 evaluation |
| **AI Economics** | FinOps for AI; cost-performance trade-offs; build vs. buy analysis |
| **AI Ethics and Governance** | Fairness testing, responsible AI review processes |
| **Regulatory Literacy** | DPDPA, EU AI Act, NIST AI 600-1, sector-specific AI regulations |

**Recommended development path:**
1. AI Literacy (all architects): 8–16 hours of structured learning; hands-on with at least 2 LLM tools
2. AI Architecture Specialisation: Advanced course covering RAG, agents, and LLMOps
3. AI Governance Specialisation: NIST AI RMF implementation, responsible AI frameworks
4. Continuing practice: monthly case study review; quarterly red team participation

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): BDAT Academy TOGAF for AI Adoption 2025, Intelance Future of EA in AI Era 2026, Belski TOGAF ADM for AI Adoption 2025, Staunstender Future of EA in AI Age 2025, University of Melbourne paper Modifying TOGAF for AI 2025, Forrester Enterprise Architecture Management Suite Landscape Q4 2025, Forrester How Agentic AI Elevates EA Role 2025, CIO.com TOGAF for AI 2026.*