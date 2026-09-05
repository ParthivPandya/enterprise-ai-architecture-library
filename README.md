# AI Enterprise Architecture Library

> A practitioner-grade, research-backed reference for Enterprise Architects, Chief AI Officers, Strategy Leaders, and Governance professionals building and scaling AI in large organisations.

---

## About This Library

This library was built to close the gap between AI hype and enterprise reality. Every section is grounded in real-world case studies, established frameworks, and actionable patterns — not theory. It covers three interlocking disciplines:

- **AI Governance & Responsible AI** — how to govern AI spend, quality, ethics, and risk at scale
- **AI Strategy & Enterprise Adoption** — how to create measurable business value and deploy AI across enterprise functions
- **AI in EA Practice** — how Enterprise Architects must evolve their practice in the age of AI

The library is designed to be read section-by-section or used as a reference. Every document cross-references related documents so you can navigate by topic.

---

## How to Use This Library

| Your Role | Recommended Starting Point |
|---|---|
| Chief AI Officer / CDO | [02-AI-Strategy/01-Business-Value.md](ai-ea-library/02-AI-Strategy/01-Business-Value.md) |
| Enterprise Architect | [03-EA-Practice/01-Driving-Adoption.md](ai-ea-library/03-EA-Practice/01-Driving-Adoption.md) |
| AI Governance / Risk | [01-AI-Governance/02-Governance-Framework.md](ai-ea-library/01-AI-Governance/02-Governance-Framework.md) |
| CTO / CIO | [03-EA-Practice/02-AI-Design-Decisions.md](ai-ea-library/03-EA-Practice/02-AI-Design-Decisions.md) |
| Finance / FinOps | [01-AI-Governance/01-FinOps.md](ai-ea-library/01-AI-Governance/01-FinOps.md) |
| Indian Enterprise Context | [02-AI-Strategy/04-Indian-Enterprise-Context.md](ai-ea-library/02-AI-Strategy/04-Indian-Enterprise-Context.md) |

---

## Section 01 — AI Governance & Responsible AI

| Document | What It Covers |
|---|---|
| [01-FinOps.md](ai-ea-library/01-AI-Governance/01-FinOps.md) | AI spend governance, token economics, cost attribution, model tiering, chargeback frameworks |
| [02-Governance-Framework.md](ai-ea-library/01-AI-Governance/02-Governance-Framework.md) | NIST AI RMF, ISO/IEC 42001, EU AI Act, enterprise governance operating models |
| [03-Responsible-AI.md](ai-ea-library/01-AI-Governance/03-Responsible-AI.md) | Microsoft, IBM, Google RAI implementations, fairness, bias, transparency — as actually deployed |
| [04-Risk-Mitigation.md](ai-ea-library/01-AI-Governance/04-Risk-Mitigation.md) | OWASP LLM Top 10 (2025/2026), red teaming, secure AI patterns, resilience design |

---

## Section 02 — AI Strategy & Enterprise Adoption

| Document | What It Covers |
|---|---|
| [01-Business-Value.md](ai-ea-library/02-AI-Strategy/01-Business-Value.md) | KPIs, OKRs, ROI frameworks, pilot-to-production patterns, the productivity J-curve |
| [02-Agentic-AI-Use-Cases.md](ai-ea-library/02-AI-Strategy/02-Agentic-AI-Use-Cases.md) | 40+ enterprise functions mapped across HR, Finance, IT, Legal, Sales, Operations, and more |
| [03-Education-and-Defence.md](ai-ea-library/02-AI-Strategy/03-Education-and-Defence.md) | AI adoption patterns in education (K-12, HED) and defence (NATO, DoD, Five Eyes) |
| [04-Indian-Enterprise-Context.md](ai-ea-library/02-AI-Strategy/04-Indian-Enterprise-Context.md) | DPDPA/DPDP Rules 2025, IndiaAI Mission, MeitY AI Governance Guidelines, localized hosting |

---

## Section 03 — AI in EA Practice

| Document | What It Covers |
|---|---|
| [01-Driving-Adoption.md](ai-ea-library/03-EA-Practice/01-Driving-Adoption.md) | EA's role bridging business and tech, TOGAF ADM for AI, governance vs enablement |
| [02-AI-Design-Decisions.md](ai-ea-library/03-EA-Practice/02-AI-Design-Decisions.md) | When AI makes architecture decisions: agentic EA tools, the architect's evolving role |
| [03-Strategic-Runbooks.md](ai-ea-library/03-EA-Practice/03-Strategic-Runbooks.md) | Playbooks for evaluating, onboarding, and retiring AI services — gate checklists, templates |
| [04-Hands-on-Workshops.md](ai-ea-library/03-EA-Practice/04-Hands-on-Workshops.md) | Facilitated workshop designs that move beyond slides — labs, red teams, design sprints |

---

## Key Themes Across the Library

**The Governance Gap** — Most organisations have AI but lack AI governance. Frameworks (NIST, ISO, DPDPA) now give structure; what's missing is operationalisation. See Sections 01 and 03.

**The Measurement Problem** — 95% of AI pilots fail to reach production with measurable financial impact (MIT NANDA, 2025). The fix is measurement discipline, not better models. See Section 02-01.

**The Agentic Inflection** — Gartner projects 40% of enterprise applications will embed task-specific AI agents by end of 2026, up from <5% in 2025. The functional mapping is in Section 02-02.

**The Architect's Evolution** — Enterprise architects are shifting from documentation custodians to strategic orchestrators. The new practice is covered in Section 03.

---

## Framework & Standard References

| Framework | Used In |
|---|---|
| NIST AI RMF 1.0 + Generative AI Profile (AI 600-1) | 01-02, 01-04 |
| ISO/IEC 42001:2023 (AI Management Systems) | 01-02 |
| OWASP Top 10 for LLM Applications 2025 / 2026 | 01-04 |
| EU AI Act (2024) | 01-02, 01-03 |
| TOGAF 10 / ADM | 03-01, 03-02, 03-03 |
| India DPDPA + DPDP Rules 2025 | 02-04 |
| IndiaAI Mission + MeitY AI Governance Guidelines 2025 | 02-04 |
| FinOps Foundation Framework | 01-01 |
| MITRE ATLAS | 01-04 |

---

## Glossary of Key Terms

| Term | Definition |
|---|---|
| **AI FinOps** | The discipline of attributing, monitoring, and optimising AI (especially LLM) spend across teams and use cases |
| **Agentic AI** | AI systems that can reason, plan, use tools, and complete multi-step tasks autonomously |
| **DPDPA** | India's Digital Personal Data Protection Act 2023 (Rules notified Nov 2025) |
| **EA** | Enterprise Architecture — the discipline of aligning business processes, IT, and strategy |
| **Hallucination / Confabulation** | LLM generating plausible but factually incorrect output — NIST AI 600-1 risk category |
| **LLMOps** | Operational practices for running LLMs in production (monitoring, routing, versioning) |
| **NIST AI RMF** | NIST AI Risk Management Framework: Govern, Map, Measure, Manage |
| **Prompt Injection** | Attacker-controlled input that manipulates LLM behaviour — top OWASP LLM risk |
| **RAG** | Retrieval-Augmented Generation — LLM answers grounded in retrieved documents |
| **Red Teaming** | Adversarial testing of AI systems to find failure modes before attackers do |
| **SDF** | Significant Data Fiduciary (India DPDPA) — high-risk data processor with enhanced obligations |
| **TOGAF ADM** | Architecture Development Method — TOGAF's phase-by-phase methodology |
| **Token** | Unit of text processed by an LLM; drives API cost |

---

*Library version: 1.0 | Research current as of September 2026 | Built for practitioners, not consultants.*
