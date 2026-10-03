# Building an AI Center of Excellence

> *McKinsey reports 88% of organisations use AI somewhere. Only about a third have scaled it. The AI CoE is what closes that gap. Not the technology — the operating structure that makes AI go from scattered pilots to enterprise-wide capability.*

> **Related:** [../02-AI-Strategy/06-AI-Change-Management.md](../02-AI-Strategy/06-AI-Change-Management.md) | [01-Driving-Adoption.md](01-Driving-Adoption.md) | [05-LLMOps.md](05-LLMOps.md)

---

## What an AI CoE Actually Is (and What It Isn't)

An AI Center of Excellence is a cross-functional team that owns AI standards, governance, platform, use-case prioritisation, and the champions network that extends its reach into business units. It is the engine that moves AI from pilot to production and from individual experiments to organisational capability.

It is not a committee. Committees meet, discuss, and defer. A CoE builds, decides, and ships.

It is not a team of data scientists who do AI projects for other teams. That model — a centralised AI team that business units queue up to access — creates a bottleneck that consistently fails at scale. The CoE should be small, focused on enablement and governance, while most AI delivery happens in distributed teams following CoE standards.

It is not optional if you want to scale. IDC's 2025 research on AI Centers of Excellence identified two common failure modes with opposing characteristics: CoEs that are too centralised become bottlenecks; CoEs that are too federated have no standards and allow chaos. The right model is a small central team that sets direction and standards, with business units delivering within those guardrails. Call it the "hub and spoke" or "federated governance" model — the pattern is widely recognised and consistently outperforms alternatives at scale.

---

## Why Most Enterprise AI Programmes Stall Without a CoE

The pattern is consistent enough to be predictable:

**Month 1–3:** An enthusiastic team in one business unit builds a GenAI prototype. It works. Leadership sees a demo. Budget is approved.

**Month 4–6:** Three more business units start their own AI projects. Each team selects different tools, different vendors, different architectural approaches. The IT team is approached by five different teams asking for different API keys, different cloud services, different security approvals.

**Month 7–12:** The first prototype is struggling in production. Nobody designed the monitoring. The cost is 3x what was budgeted. The vendor contract has no data processing agreement. Security raised concerns nobody addressed. Meanwhile, the three new projects are building on similar infrastructure, reinventing what team one already built.

**Month 13–18:** Leadership announces an "AI governance crisis." A new initiative is launched to "establish standards." This initiative is, in everything but name, an AI CoE — built 12 months later than it should have been, attempting to retrofit governance onto systems that already have technical debt baked in.

The CoE exists to prevent this pattern by providing the standards, platform, and governance before the proliferation, not after it.

---

## The Operating Model: Hub and Spoke

```
                    ┌─────────────────────┐
                    │    AI CoE (Hub)      │
                    │  Strategy & Roadmap  │
                    │  Standards & Policy  │
                    │  Shared Platform     │
                    │  Governance & Risk   │
                    │  Champions Network   │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
   ┌──────┴──────┐      ┌──────┴──────┐      ┌──────┴──────┐
   │  Finance BU │      │   HR BU     │      │   Sales BU  │
   │  AI Lead    │      │   AI Lead   │      │   AI Lead   │
   │  (Spoke)    │      │   (Spoke)   │      │   (Spoke)   │
   └─────────────┘      └─────────────┘      └─────────────┘
```

**The Hub (Central CoE):** Sets standards, owns the shared platform, manages governance, runs the champions network. Small — typically 4–8 people at launch, growing to 10–15 at scale. The hub does not build business unit AI solutions; it enables business units to build them well.

**The Spokes (BU AI Leads):** Embedded practitioners in each major business unit, accountable both to their business unit (for delivery) and to the CoE (for standards compliance). They are the bridge. They translate business requirements into AI solutions within the guardrails the hub sets. They feed learnings back to the hub.

**Champions:** Senior, credible practitioners in each team who use AI tools and informally coach their peers. Not a formal role in the organisational chart — a cultural role in the change management programme (see [../02-AI-Strategy/06-AI-Change-Management.md](../02-AI-Strategy/06-AI-Change-Management.md)).

---

## The Roles: What People Actually Do

**AI CoE Director (or Chief AI Officer, CAIO)**
The most senior role. Owns the AI programme strategy, executive relationships, and the business case for the CoE's existence. This person is measured on portfolio ROI, governance compliance rate, and enterprise AI maturity progress. They need credibility in both technology and business — the bridge-builder identity matters more here than technical depth.

*Reporting line:* CTO, CIO, or CEO depending on organisation. Should not report to a line-of-business executive — the independence to govern across business units requires appropriate positioning.

**AI Platform Engineer (1–3 people)**
Builds and operates the shared AI infrastructure: the LLM gateway (LiteLLM or equivalent), the observability stack, the prompt library tooling, the vector database infrastructure for RAG, and the model registry. This person enables every other team to build AI without building their own infrastructure from scratch.

*Skills:* Python, cloud infrastructure (AWS/Azure/GCP), API design, LLMOps tooling (LangSmith, Langfuse, MLflow). Experience with ML infrastructure preferred but not required — LLMOps is a new enough discipline that learning-on-the-job is common.

**AI Governance and Risk Lead**
Owns the AI governance programme: the AI system registry, the pre-deployment review process, the NIST AI RMF implementation, DPDPA compliance for AI systems, and the red team programme. Works with Legal, Privacy, Security, and Compliance. This role is the reason the CoE can say "yes" more often than "no" — because governance is proactive, not reactive.

*Skills:* Risk management, compliance frameworks (NIST AI RMF, ISO 42001, DPDPA), some technical literacy to evaluate AI system designs, stakeholder management.

**AI Evaluation / Quality Lead**
Owns the evaluation framework: the golden test set methodology, LLM-as-judge implementation, prompt testing protocols, and quality monitoring. Ensures that every AI system deployed meets defined quality thresholds and that quality doesn't degrade in production.

*Skills:* LLM evaluation methodologies, statistics (for interpreting evaluation results), Python (for building evaluation pipelines), domain knowledge in the highest-priority use cases.

**Business Unit AI Leads (Spokes — 1 per major BU)**
Embedded in their business unit, delivering AI projects within CoE standards. The dual-reporting line is intentional — it creates healthy tension between business speed and governance rigour.

*Skills:* Business domain knowledge first, technical AI implementation second. A finance professional who has learned to build AI solutions is often more effective in this role than an AI engineer who has learned finance.

**AI Champions (Distributed — not direct CoE reports)**
Senior individual contributors across teams who adopt AI early, develop genuine expertise, and informally coach peers. Selected by the CoE Director in collaboration with business unit leaders. Criteria: peer credibility, genuine AI adoption, willingness to share openly about what works and what doesn't.

---

## The CoE Charter: One-Page Version

The CoE charter is the document that establishes mandate, scope, and decision rights. Without it, the team drifts. With it, the team has the authority to make decisions that need to be made.

```
AI CENTER OF EXCELLENCE CHARTER

MANDATE
To accelerate enterprise AI adoption by providing standards, shared platform, 
governance, and expertise — enabling business units to build AI solutions 
faster, more safely, and with measurable business impact.

SCOPE
- All AI systems deployed or procured within [Organisation]
- AI governance policy and standards
- Shared AI infrastructure and tooling
- AI vendor assessment and approval
- AI capability development and champions network

DECISION RIGHTS
The CoE has authority to:
- Approve or reject AI vendor onboarding
- Set and enforce AI architecture standards
- Require pre-deployment review for AI systems above defined risk threshold
- Manage the enterprise AI system registry

The CoE does not have authority to:
- Veto business unit AI investments within approved standards
- Direct product or engineering team priorities
- Override legal or compliance decisions

ACCOUNTABILITIES
- Chief AI Officer: portfolio ROI, governance compliance rate, AI maturity index
- Business Unit AI Leads: use case delivery, BU adoption rate, KPI achievement
- Platform Engineer: platform uptime, developer NPS, infrastructure cost

SUCCESS METRICS (Year 1)
- AI systems in production with documented ROI: [Target]
- Governance compliance rate: ≥ 95% of production systems
- AI platform adoption: ≥ 80% of AI projects using shared infrastructure
- Employee AI literacy completion: ≥ [%] of target roles

REVIEWED ANNUALLY BY: [CTO/CIO + CoE Director]
```

---

## The 6-Month Rollout Plan

Based on patterns from practitioners who have built AI CoEs across Indian and global enterprises:

### Month 1: Foundation

**Week 1–2: Charter and mandate**
- Draft and get executive sign-off on the CoE charter
- Confirm the CoE Director is in place with appropriate authority
- Announce the CoE to the organisation with the CEO or CTO as the messenger (not the CoE Director — the signal needs to be that this has executive backing, not just an IT initiative)

**Week 3–4: Audit**
- Inventory every AI system currently in use — you will find more than expected
- Identify every AI project currently in progress — you will find duplication
- Assess the governance status of each: Does it have an owner? A data processing agreement? Security review? Monitoring?
- This audit is uncomfortable. Do it anyway. You cannot govern what you don't know exists.

**Deliverable:** AI system inventory + gap assessment. Priority remediation list for the most critical governance gaps in existing systems.

### Month 2: Platform Basics

**Stand up shared infrastructure:**
- AI gateway (LiteLLM or equivalent): single access point for all LLM API calls, with per-team attribution
- Prompt library repository: version-controlled, with review process defined
- Observability stack: cost tracking, latency monitoring, error rate dashboards — minimal viable monitoring for all existing production AI systems

**Why the gateway first:** Without it, you have no visibility into spend, no ability to enforce rate limits, and no unified logging. Every subsequent governance programme depends on this infrastructure.

**Deliverable:** AI gateway live. All production API keys migrated to go through the gateway. First cost attribution report generated.

### Month 3: Governance Process

**Stand up the governance programme:**
- Pre-deployment review process documented and communicated
- AI system registry launched (initially populated from Month 1 audit)
- First governance training for Business Unit AI Leads

**The pre-deployment review process is the most politically sensitive thing the CoE does.** Done wrong, it becomes a bottleneck that business units resent and route around. Done right, it's a service that helps teams ship faster by catching problems before they become crises.

**Design it risk-proportionately:** Experiments and internal tools with non-sensitive data get a self-service checklist (1 page, <1 day). Customer-facing applications with personal data get a structured review (1–2 weeks). High-risk applications in regulated domains get a full governance board review (4–6 weeks).

**Deliverable:** Pre-deployment review process documented and used for the first new AI deployment.

### Month 4: First Delivery

**Own the first cross-BU AI deployment:**
The CoE needs to deliver something tangible, not just govern others' work. Identify the highest-value AI use case that requires the shared infrastructure you've built — typically something like an enterprise search tool, a policy Q&A assistant, or an HR document chatbot. Build it using your own standards. Document what you did, what you learned, and what the ROI looks like.

This first delivery serves three purposes: validates your platform, demonstrates CoE value to the organisation, and produces a reference implementation that business units can learn from.

**Deliverable:** First CoE-led AI deployment in production with monitoring and documented business case.

### Month 5: Champions Network

**Launch the AI Champions programme:**
- Identify 1–2 champions per major business unit (15–30 people total)
- Run a 1-day champions bootcamp: AI basics, the shared platform, the governance process, and how to coach peers
- Launch monthly "AI Champions office hours" — open sessions where anyone can bring questions, show what they're building, or ask for help
- Champions are recognised publicly (not financially rewarded — recognition is the mechanism)

**Deliverable:** Champions network active, office hours calendar published, first round of peer coaching happening organically.

### Month 6: Measurement and Scale

**The 6-month review:**
- What did we build? How many production systems? What was the governance compliance rate?
- What did we spend? Platform cost + CoE team cost + investment in governed projects
- What was the return? Documented ROI from first delivery + attributed value from projects that used shared infrastructure
- What did we learn? Where did the process fail? Where was adoption slow?

**The scale plan:**
Based on 6-month learnings, build the 12-month plan:
- Which BUs are ready for embedded AI Leads?
- Does the platform need capabilities that projects couldn't find?
- Which governance gates need adjustment (too slow, or not catching real problems)?
- What does the next wave of use cases look like, and what infrastructure does it require?

**Deliverable:** 6-month review deck shared with executive sponsors. 12-month scale plan approved.

---

## The Two Failure Modes to Avoid

**Failure Mode 1: The Governance Chokepoint**
The CoE becomes so focused on governance that it blocks rather than enables. Every AI idea requires a 6-week review. Business units route around the CoE entirely. The governance framework exists on paper; reality is ungoverned.

**How to prevent:** Governance must be proportionate to risk. Most AI projects should be able to proceed with a self-service checklist that takes one hour. Reserve extended review for genuinely high-risk systems. Measure the CoE on how much AI it enables, not just what it blocks.

**Failure Mode 2: The Technology Team Without Business Connection**
The CoE is staffed entirely by technical people, speaks only in technical terms, and can't connect AI capability to business outcomes. It builds impressive infrastructure that business units don't adopt because they don't understand how it helps them.

**How to prevent:** The CoE Director must be bilingual — genuinely fluent in both technology and business. At least one CoE team member should come from a business function, not from IT. Every CoE communication should lead with business outcomes, not technical capabilities.

---

## The CoE's Job When Things Go Wrong

When an AI system fails — a chatbot gives wrong legal advice, a fraud detection model generates a discrimination complaint, a cost anomaly runs $200K over budget — the CoE's response defines its credibility.

The response to AI failures must be:
- **Fast:** The CoE lead knows about production AI incidents within hours, not weeks
- **Honest:** Post-mortems that identify root causes without defensive rationalisation
- **Structural:** Every failure produces a change to standards, process, or tooling — not just a "lessons learned" document that nobody reads

The organisations that build the most trustworthy AI programmes are the ones that treat failures as governance input, not reputation problems to manage. The Air Canada chatbot case (see [../01-AI-Governance/05-When-AI-Goes-Wrong.md](../01-AI-Governance/05-When-AI-Goes-Wrong.md)) could have been a six-month initiative to improve the chatbot. It became a public legal case because the failure was treated as a customer service problem rather than a governance failure.

---

*Source leads (not publication-grade citations; verify exact title, edition, URL, page/section, methodology, and date under the [Editorial and Citation Policy](../EDITORIAL-AND-CITATION-POLICY.md)): McKinsey State of AI 2025 scaling analysis, IDC AI CoE Research 2025, Tredence AI CoE Blueprint 2025, Xebia AI CoE Microsoft Playbook 2025, Layer3 Labs AI CoE Structure Guide 2026, Appinventiv AI CoE Framework 2026, AI Assembly Lines AI CoE Staffing Guide 2026, Karunjay Medium AI CoE 6-month rollout case study, Gartner AI CoE Operating Model research 2025.*