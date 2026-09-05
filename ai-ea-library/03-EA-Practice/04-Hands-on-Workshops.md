# Hands-On Workshops: Moving Beyond Discussion-Only Sessions

> **Related:** [01-Driving-Adoption.md](01-Driving-Adoption.md) | [03-Strategic-Runbooks.md](03-Strategic-Runbooks.md) | [../02-AI-Strategy/02-Agentic-AI-Use-Cases.md](../02-AI-Strategy/02-Agentic-AI-Use-Cases.md)

---

## The Problem With Most AI Workshops

Most enterprise AI workshops produce the same output: a deck of slides, a list of potential use cases, and a room full of people who felt included but didn't commit to anything. The goal, as Design Sprint Academy puts it, is "outcomes not good vibes, decisions not fake alignment, validation not opinions."

The workshops in this document are built on three principles:

1. **Decisions, not discussions.** Every workshop ends with a named decision that someone is accountable for.
2. **Hands-on, not watch-the-demo.** Participants build, test, or red-team something real — not watch a vendor presentation.
3. **Business problem first.** No workshop starts with AI technology. It starts with a business problem, a KPI, and a human who is accountable for that KPI.

This document provides six workshop designs — from half-day to multi-day — covering the full range of EA-led AI work.

---

## Workshop 1: AI Use Case Discovery Sprint

**Format:** Half-day (4 hours)  
**Participants:** 8–12 people — Business stakeholders (2–3), Data team lead, Security/Legal rep, Enterprise Architect (facilitator), Product/Operations leads  
**Goal:** Identify, score, and prioritise 3–5 AI use cases ready for business case development  
**Output:** Scored use case backlog with named owners, not a brainstorm list

---

### Pre-Work (Day before, 30 min)

Participants independently complete:
- One-page "AI Opportunity" submission using the template below
- Current-state KPI data for their area (don't start without it)

```
AI Opportunity Submission (complete before the workshop)

Business problem (1 sentence): 
Current state metric (baseline): 
What AI might do differently: 
Who owns the outcome if this is built: 
What data is available: 
```

---

### Hour 1: Frame the Playing Field (60 min)

**Activity 1: Problem Gallery (25 min)**  
Post all pre-work submissions on the wall (physical or Miro/FigJam). Participants do a silent read-through, adding sticky notes: green = "I see this problem too," orange = "question," red = "potential blocker."

**Activity 2: Pattern clustering (15 min)**  
Facilitator (EA) clusters problems by function (HR, Finance, IT, Customer). Teams form around clusters. *No technology talk yet.*

**Activity 3: Problem refinement (20 min)**  
Each cluster refines their top problem into a 1-sentence problem statement that includes: [who] struggles to [do what] which costs/risks [quantified impact].

---

### Hour 2: Score and Filter (60 min)

**The Scoring Matrix** (5 min setup, 20 min scoring, 15 min discussion, 20 min prioritisation)

Each team scores their use case on 6 criteria (1–5 each):

| Criterion | Score 1 | Score 5 |
|---|---|---|
| Volume | Happens <1x/week | Happens hundreds of times/day |
| Data availability | No usable data | Clean, accessible data today |
| Rule-governed | Almost entirely judgment | Clear, documentable rules |
| Measurability | Hard to define KPI | KPI already tracked |
| Business impact | Nice to have | CEO-level priority |
| Reversibility | Irreversible consequences | Easy to undo |

Post scores on a 2×2 matrix: Value (vertical) × Feasibility (horizontal). Top-right = prioritise. Bottom-left = park.

**Facilitator move:** If everything lands in the top-right, the team hasn't been honest about feasibility. Push back on data availability scores specifically — this is where optimism is most costly.

---

### Hour 3: Stress-Test the Top 3 (60 min)

Take the top 3 use cases and run them through a 20-minute "pre-mortem" each:

*"It's 12 months from now and this AI project completely failed. What went wrong?"*

Write failure modes on sticky notes. Cluster them. For each major failure mode, the group identifies: is this a **showstopper** (red), a **solvable problem** (amber), or **manageable** (green)?

Use cases that produce more than 2 reds are moved to the parking lot or put on hold pending risk mitigation.

---

### Hour 4: Commit (60 min)

**Activity: Business Case Skeleton**  
The owner of each surviving use case drafts a one-page business case skeleton live in the room (using the template from [01-Business-Value.md](../02-AI-Strategy/01-Business-Value.md)):

- Problem statement + KPI + baseline
- Hypothesis: what AI will do + target metric
- Data available (specific, not "we probably have it")
- Owner committed to pursue this
- Decision requested: approve business case development by [date]?

**Room vote:** The group decides — fund the business case development, or not. This is the decision. Name it, document it, sign it.

**No use case leaves the room without a named owner and a next-action date.**

---

## Workshop 2: AI Architecture Decision Workshop

**Format:** Half-day (3–4 hours)  
**Participants:** 6–10 people — Enterprise Architects, Solution Architects, Lead Engineers, Business Sponsor  
**Goal:** Make and document the key AI architecture decisions for a specific use case  
**Output:** Completed Architecture Decision Records (ADRs) for the top 5 decisions

---

### Pre-Work

Architect prepares:
- Current architecture landscape diagram (1 page — application, data, and infrastructure layers)
- Three candidate architecture approaches (e.g., Buy SaaS / Fine-tune OSS / RAG on existing docs)
- Evaluation criteria agreed in advance: cost, latency, data residency, governance complexity, vendor lock-in risk

---

### The Workshop Structure

**Opening (15 min):** Architect presents the use case, the constraints, and the three options. No preference stated — present options neutrally.

**Option Analysis (60 min):** Three groups, one per option. Each group has 20 minutes to make the best case for their option AND identify its biggest risks. No group advocates for their own preferred option — assign randomly.

**Cross-examination (30 min):** Each group presents; the other groups ask hard questions. Facilitator documents the emerging trade-offs on a shared board.

**Decision session (45 min):** Structured around the Architecture Decision Record format:

```
Architecture Decision Record (ADR)

Decision #: 
Date: 
Decision: [State the decision in one sentence]
Status: [Proposed / Accepted / Superseded]

Context: [What situation triggered this decision?]
Options considered: [List the options evaluated]
Decision rationale: [Why this option over the others?]
Trade-offs accepted: [What are we giving up?]
Consequences: [What does this decision constrain or enable?]
Reversibility: [How hard is this to change later? What would trigger a revisit?]
Owner: [Who is responsible for this decision holding?]
Review date: [When should this decision be revisited?]
```

Complete one ADR per major decision before the group leaves the room. Major decisions typically include: build/buy/fine-tune, model provider, data residency approach, human oversight model, cost governance approach.

---

## Workshop 3: AI Red Team Exercise

**Format:** Half-day to full-day (3–6 hours)  
**Participants:** 8–15 people — Security team, Enterprise Architects, Product team, optionally external red teamers  
**Goal:** Identify exploits, failure modes, and governance gaps in a live or near-live AI system before attackers do  
**Output:** Prioritised vulnerability list with ownership and remediation timeline

---

### Setup (30 min)

**Define the target system:** Which AI application is being red-teamed? Document:
- What the system is supposed to do
- What it is explicitly not supposed to do (safety, compliance, privacy constraints)
- What access attackers (or users) would realistically have

**Form red teams:** Divide into 3–4 groups, each assigned a category from the OWASP LLM Top 10 (see [01-AI-Governance/04-Risk-Mitigation.md](../01-AI-Governance/04-Risk-Mitigation.md)):
- **Team A:** Prompt Injection and System Prompt Leakage
- **Team B:** Sensitive Information Disclosure and Data Privacy
- **Team C:** Excessive Agency and Insecure Output Handling
- **Team D:** Supply Chain, Model Poisoning, and Misinformation

---

### Attack Phase (90–120 min)

Each team has live access to the AI system (in a staging or sandboxed environment). Their mission: **find attacks that work**.

Teams document every attack attempt:

```
Attack Log Entry

Team: 
Category: [OWASP LLM category]
Attack type: [Prompt injection / PII extraction / Jailbreak / etc.]
Attack input: [Exact input used]
System response: [What the system actually did]
Expected response: [What it should have done]
Success? [Yes / Partial / No]
Severity: [Critical / High / Medium / Low]
Reproducible? [Yes / No]
```

**Facilitator rules:**
- Teams cannot share attacks with each other during the attack phase
- If a team finds a critical vulnerability, they notify the facilitator privately (don't broadcast)
- Everything is documented — failed attacks are as informative as successful ones

---

### Debrief Phase (60–90 min)

Teams present their findings. For each confirmed vulnerability:
- Demo the attack (show it working in the room)
- Assess the real-world impact: who could exploit this, what would they gain?
- Brainstorm mitigations

**Prioritisation matrix:**

| Severity | Ease of Exploit | Priority |
|---|---|---|
| Critical | Easy | Fix before launch (block launch if not resolved) |
| Critical | Hard | Fix within 30 days |
| High | Easy | Fix within 30 days |
| High | Hard | Fix within 90 days |
| Medium | Any | Fix within 180 days or accept risk |
| Low | Any | Document and monitor |

**Each vulnerability gets an owner and a remediation deadline before the room disperses.**

---

### Red Team Outputs

1. **Vulnerability Register** — complete list of findings with severity, owner, deadline
2. **Red Team Prompt Library** — successful attack inputs added to the regression test suite
3. **Fix Verification Plan** — schedule for re-testing fixed vulnerabilities
4. **Launch Recommendation** — based on findings, what is the red team's recommendation? Launch / Launch with conditions / Hold?

---

## Workshop 4: AI FinOps Attribution Sprint

**Format:** Half-day (4 hours)  
**Participants:** 6–10 people — Engineering leads, Finance, EA, Product owners of AI features  
**Goal:** Map AI spend to business value; identify 20–50% waste in the first session  
**Output:** Attribution model, anomaly baseline, and an optimisation backlog

---

### Hour 1: The Attribution Mapping Exercise

**Step 1 (30 min):** Pull the last 3 months of AI API invoices. On a whiteboard, list every AI vendor and service being paid for.

**Step 2 (30 min):** For each service, ask: *Can you tell, from available data, which product feature or business process generated each dollar of spend?*

Classify:
- 🟢 **Attributed** — we know exactly which feature/team generated this
- 🟡 **Partially attributed** — we have some data but not complete
- 🔴 **Unattributed** — we have no idea

*Typical result:* 50–70% of spend is unattributed in most organisations that haven't done this exercise before. That number will be uncomfortable. That discomfort is the point.

### Hour 2: Build the Attribution Model

Design the target attribution model:
- What API key structure is needed?
- What metadata tags should be applied at the proxy/gateway layer?
- What are the "unit cost" metrics for each major feature? (cost per conversation, cost per document processed, etc.)

Assign ownership: who is building the attribution infrastructure, and by when?

### Hour 3: Waste Identification

For each attributed feature:
- Is the cost-per-unit trending up, down, or flat?
- Is the volume changing?
- Which features have the highest per-unit cost?
- Which features have the lowest business value relative to their cost?

**Common waste patterns found in this exercise:**
- System prompts that haven't been audited for token efficiency (often 15–40% of token spend)
- Identical queries not being cached (add semantic caching → 40–60% cost reduction)
- Frontier models used for tasks where smaller models perform equally well
- Batch-eligible workloads running as real-time inference (2x cost premium)

### Hour 4: Build the Optimisation Backlog

Create a prioritised backlog of cost optimisation initiatives, each with:
- Estimated saving (%)
- Engineering effort (days)
- Priority (saving / effort ratio)
- Owner
- Target completion date

Typical backlog from this session: 5–10 initiatives with combined 30–60% cost reduction potential.

---

## Workshop 5: AI Governance Maturity Assessment

**Format:** Half-day (3 hours)  
**Participants:** 8–15 people — EA lead, CISO, Chief AI Officer or equivalent, Legal/Privacy, HR, business unit leads  
**Goal:** Honest assessment of current AI governance maturity; agree the 90-day improvement plan  
**Output:** Governance maturity scorecard + 90-day roadmap

---

### The Assessment (90 min)

Work through the governance checklist as a group. For each item, the facilitator asks: "Does this exist and is it working?" Ruthlessly honest voting — thumbs up (yes, working), thumbs sideways (exists but not working), thumbs down (doesn't exist).

**Categories:**

**Policy and Accountability**
- [ ] AI use policy (specific permitted/prohibited uses)
- [ ] Named AI system owners for all production systems
- [ ] AI system registry current and complete
- [ ] AI review process for new deployments

**Risk and Compliance**
- [ ] NIST AI RMF applied to at least one system
- [ ] DPDPA compliance assessment completed for AI systems with personal data
- [ ] OWASP LLM risk categories assessed for all GenAI deployments
- [ ] Incident response process for AI failures

**Technical Governance**
- [ ] AI spend attributed by team/feature (FinOps)
- [ ] Production monitoring for all AI systems (accuracy, cost, latency)
- [ ] Anomaly alerts active
- [ ] Rollback plans documented for all production AI systems

**Responsible AI**
- [ ] Fairness evaluation completed for any AI system affecting individuals
- [ ] Transparency disclosures in place for user-facing AI
- [ ] AI training programme for staff

---

### The Planning (60 min)

Take the red items and prioritise them into a 90-day roadmap:

**30 days:** The things that are urgent AND achievable in 30 days (usually: AI system registry, API key governance, incident response contacts)

**60 days:** The things that require more infrastructure but are clearly important (usually: monitoring dashboards, basic FinOps attribution, DPIA for highest-risk systems)

**90 days:** The things that require cross-functional effort (usually: formal NIST AI RMF application, fairness evaluation process, comprehensive red team programme)

Each item gets an owner. The group commits to a 90-day review.

---

## Workshop 6: Enterprise AI Architecture Future-State Design

**Format:** Full day (6–7 hours)  
**Participants:** 10–15 people — EA team, CTO/CIO, Engineering leads, Data team, Business sponsors  
**Goal:** Design the enterprise AI architecture target state for the next 18–24 months  
**Output:** Target Architecture Blueprint with migration backlog

---

### Morning (3 hours): Current State Honesty

**Activity 1 — AI Systems Audit (60 min)**  
Map every AI system currently running in the organisation on a shared canvas. For each system: business function, technology stack, vendor, cost, number of users, governance status. Most organisations discover systems they didn't know existed. This is intentional.

**Activity 2 — Architecture Debt Analysis (60 min)**  
Identify the biggest structural problems:
- Duplicated AI infrastructure (three different RAG implementations for the same type of problem)
- Missing shared services (every team building their own prompt engineering; no reuse)
- Security gaps (systems without monitoring, systems with overly broad permissions)
- Cost inefficiencies (frontier models used for tasks that don't need them)

**Activity 3 — Technology Radar (60 min)**  
Plot AI technologies on the classic Thoughtworks Technology Radar quadrants:
- **Adopt** (already proven, use as standard)
- **Trial** (worth experimenting with, monitored)
- **Assess** (promising, investigate but don't build on yet)
- **Hold** (not recommended for new projects)

Examples in each quadrant for a typical 2026 enterprise:
- *Adopt:* RAG for enterprise search, LLM APIs (OpenAI/Anthropic/Gemini), LangChain/LlamaIndex for orchestration
- *Trial:* Agentic workflows, voice AI for customer service, fine-tuned domain models
- *Assess:* Multi-agent orchestration (early), AI-native coding agents, on-device LLMs
- *Hold:* Custom model training from scratch (for most enterprises), early-generation autonomous agents in production for high-risk decisions

---

### Afternoon (3–4 hours): Target State Design

**Activity 4 — Shared AI Platform Design (90 min)**  
Design the shared AI infrastructure that all teams will use:
- AI Gateway / Proxy (single point of entry for all LLM API calls)
- Shared Vector Database / Knowledge Platform
- LLMOps pipeline (model management, evaluation, monitoring)
- AI FinOps attribution layer
- AI Governance registry

Draw this on a whiteboard. Assign a team to own each component.

**Activity 5 — Migration Sequencing (60 min)**  
What is the order of operations to get from current state to target state?
- What must be built before anything else can proceed? (usually: AI gateway + attribution)
- What can be built in parallel?
- What is the dependency chain?

Output: A sequenced migration plan with quarters (Q1/Q2/Q3/Q4) and owners.

**Activity 6 — Commitment Ceremony (30 min)**  
Every workshop needs a closing ritual that converts intent to commitment. For this one:

Each participant writes on a card: "I commit to [specific action] by [date]. I will be accountable to [person]."

Cards are read aloud, photographed, and distributed. The follow-up review is scheduled before the room disperses.

---

## Facilitator Notes: What Makes These Workshops Fail

**Failure Mode 1: No real decisions made.** Every workshop should end with at least one named decision. If the group "needs more information" to decide everything, the workshop wasn't designed tightly enough. Build in constraints: "We will decide on exactly 3 use cases to pursue, and the decision is final for 90 days."

**Failure Mode 2: Senior people dominate.** Junior engineers often have the clearest view of the real technical constraints; junior business analysts often spot the real operational realities. Use anonymous voting tools (Mentimeter, Slido) for preference exercises. Run writing activities before verbal discussion to give quiet voices equal input.

**Failure Mode 3: Technology demo replaces hands-on work.** If a vendor has given a demo in the first hour, the rest of the workshop is contaminated. The group anchors on what they saw, not what they need. Never allow vendor demos in a use case discovery session.

**Failure Mode 4: No pre-work.** Workshops without pre-work turn the first hour into information gathering that should have happened before. Enforce pre-work. If participants haven't completed it, the workshop starts without them.

**Failure Mode 5: No follow-up.** The half-life of workshop decisions without follow-up is approximately 2 weeks. Send the decision record within 24 hours. Schedule the 30-day follow-up in the room. Assign a named "keeper of commitments" who will chase the owners.

---

*Sources: Design Sprint Academy Enterprise Design Sprint 3.0 Guide 2025, Design Sprint Academy Best AI Workshops Buyer's Guide 2026, Practical DevSecOps AI Red Teaming Guide 2026, PromptMetrics AI FinOps Attribution Guide, Worqlo AI FinOps Cost Attribution Framework, Stanford Digital Economy Lab Enterprise AI Playbook 2026, Forrester EA Maturity Assessment guidance 2025.*
