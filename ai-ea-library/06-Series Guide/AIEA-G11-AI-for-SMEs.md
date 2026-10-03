# AIEA Series Guide
## AIEA-G11: AI for Small and Medium Enterprises (SMEs)
### Document Number: AIEA-G11 | Version 1.0 | 2026

| Metadata | Detail |
|---|---|
| Document type | Independent, proportionate reference guide |
| Audience | Owners, founders, directors, heads of technology and operations, product managers, security and privacy leads, and practitioners carrying combined architecture, engineering, and governance responsibilities |
| Use when | Selecting, buying, piloting, launching, or reviewing AI in a small or medium enterprise with constrained budget and specialist capacity |
| Scope | Employee productivity, customer service, document and knowledge work, forecasting, workflow automation, and externally supplied AI services |
| Last verified | October 2026 |
| Standing | Independent guidance, not law, legal advice, certification, investment advice, or proof of compliance |

---

## Preface

This document is an independent AIEA Series Guide supplementing the core AIEA Reference Framework. It adapts AI Enterprise Architecture for **small and medium enterprises** — organisations that need the benefits of AI and responsible governance, but without the large architecture teams, budgets, or tooling the full standard assumes.

The guiding idea is **proportionate architecture**: apply the smallest set of AIEA practices that still achieves accountability, safety, and value. SMEs get an assessment and governance capability they would otherwise have to buy.

This guide is written for founders, heads of technology, and the single-hatted "architect + engineer + governance lead" common in smaller organisations. It is the lightweight path into [AIEA-101](../05-Standards/AIEA-101-Introduction-Core-Concepts.md).

---

## Chapter 1: Proportionate Architecture

### 1.1 The SME Constraint Set

| Constraint | Consequence |
|---|---|
| Few or no dedicated architects | Governance must be lightweight and template-driven |
| Limited budget | Prefer managed/API AI over bespoke infrastructure |
| Small data / platform teams | Rely on data contracts and vendor controls, not large pipelines |
| High regulatory exposure per headcount | Applicable data-protection, consumer, employment, intellectual-property, and sector obligations do not disappear with team size |

### 1.2 The Minimum Viable AI Governance (MVG)

An SME can begin a responsible AI governance practice with just **five artefacts**:

1. An [AI System Card](../12-Templates/AI-System-Card-Template.md) per system.
2. A [Pre-Deployment Launch Gate](../12-Templates/Pre-Deployment-Launch-Gate.md) checklist.
3. A [DPDPA Compliance Checklist](../12-Templates/DPDPA-Compliance-Checklist.md) if personal data is processed.
4. A simple risk tag (Minimal / Limited / High).
5. A named human owner.

These five artefacts are a minimum operating set for the core AIEA principles (G1, G2, D2, O1) at SME scale. They are not proof of legal compliance or adequate assurance for every use case; higher-consequence uses need additional controls and competent advice.

### 1.3 Proportionate Risk Tiers

Classify the **use**, not merely the model. One service can be low consequence for an internal agenda and high consequence in recruitment, credit, health, safety, education, or essential services.

| SME tier | Typical use | Minimum posture |
|---|---|---|
| Tier 0: prohibited or not justified | Covert monitoring, unlawful discrimination, unsupported safety decisions, or a use with no credible control | Do not deploy; seek qualified advice or redesign |
| Tier 1: internal assistance | Drafting, summarising non-sensitive material, coding assistance, brainstorming | Approved account, usage rules, data restriction, user review, basic record in the AI inventory |
| Tier 2: business process | Knowledge search, document extraction, forecasting, customer-service drafting | System Card, vendor review, representative evaluation, access control, monitoring, fallback |
| Tier 3: consequential | Material effect on a person, safety, finance, employment, regulated activity, or critical operation | Specialist review, formal impact and threat assessment, independent approval, human decision authority, appeal or correction route where relevant, stronger evidence and logs |

If classification is unclear, choose the more controlled tier. Price indicates neither risk nor quality.

---

## Chapter 2: Reference Architecture (Lean)

### 2.1 Buy, Don't Build

| Need | SME Pattern |
|---|---|
| Model access | Managed API via a thin [AI Gateway](../11-Architecture-Diagrams/README.md) (even a hosted one) |
| Knowledge grounding | Managed RAG / vector service |
| Monitoring | Built-in provider dashboards + a lightweight cost cap |
| Data | Data contracts with SaaS sources; avoid custom pipelines |

“Buy, don't build” is a cost heuristic, not transferred accountability. Managed services reduce infrastructure effort but can introduce concentration, opaque changes, cross-border processing, weak export, and contractual limits. Build or self-host only when risk, differentiation, data boundary, or continuity justifies the operating burden.

### 2.2 The One-Principle Priority List

If an SME does only a few things, do these:
- **Model Independence (D1):** route through a gateway so you can switch providers.
- **Grounded Generation (D2):** ground factual answers; do not let the model invent.
- **Observability (O1) + cost cap (O2):** basic monitoring and a hard budget cap.

### 2.3 Lean Architecture Views

#### Context view

List users, affected customers or workers, data sources, the AI supplier, other SaaS services, the accountable owner, and anyone who reviews or can challenge an outcome. Mark sensitive data and business-critical dependencies. One diagram and a one-page System Card are often sufficient if kept current.

#### Logical view

A reusable SME pattern is:

```
approved user/channel
    -> identity and access
    -> thin policy/gateway layer
    -> prompt/template + approved knowledge
    -> AI provider
    -> output checks and human review
    -> business system
    -> minimal audit, usage, quality, and cost records
```

The policy layer may be an integration platform, API proxy, SaaS control, or small service. Centralise only what the organisation can operate reliably: approved providers, credentials, spend limits, logging, data-loss controls, and routing.

#### Data view

Use a short classification such as public, internal, confidential, and restricted. State allowed and prohibited classes, personal-data use, processing location, retention, provider training, and support for access or deletion. Do not ingest an entire drive or mailbox merely because it is easy.

#### Operational view

Assign supplier notices, change review, reports, credentials, spend, record export, and disablement. Test the non-AI fallback and address single-person dependency.

### 2.4 Low-Cost Architecture Tiers

| Cost tier | Suitable pattern | Controls not to omit |
|---|---|---|
| Existing-suite tier | AI already licensed in productivity or business SaaS | Tenant settings, identity, data-use terms, approved-use policy, inventory, user review |
| Single-service tier | One approved chat, extraction, or support service | Business account, no shared credentials, data restrictions, admin visibility, export and offboarding |
| Integrated tier | API connected to a business workflow | Secrets management, schema validation, evaluation set, rate/spend limit, retries, fallback, supplier-change review |
| Grounded tier | Retrieval over a small approved document set | Source ownership, access filtering, document validity, citation checks, index deletion and refresh |
| Higher-control tier | Dedicated tenancy, regional hosting, self-hosting, or multiple providers | Use only when risk or continuity justifies security, platform, patching, evaluation, and support effort |

Optimise total cost: integration, data, licences, evaluation, review, errors, support, security, switching, and exit. Set budgets and alerts from actual usage; this guide predicts no savings.

### 2.5 SaaS AI Due Diligence

Review the supplier and exact product tier; business controls often differ from consumer terms.

| Risk area | Questions to answer before use |
|---|---|
| Data use | Are prompts, files, metadata, and outputs used to train or improve models? Is opt-out contractual and tenant-wide? |
| Retention and deletion | What is retained, for how long, in which backups, and can the SME trigger and evidence deletion? |
| Location and subprocessors | Where can data and support access occur, and how are changes notified? |
| Identity and administration | Are MFA, SSO where proportionate, role separation, user offboarding, and audit events available? |
| Security | What secure-development, encryption, vulnerability, incident-notification, and assurance evidence is available? |
| Model change | Can the provider replace a model or safety policy without notice, and can a known version be retained or re-evaluated? |
| Reliability | What limits, outages, quotas, support response, status information, and degraded modes apply? |
| Rights and content | What input rights are required, what output terms apply, and how are alleged infringement or harmful content handled? |
| Portability | Can prompts, configurations, files, outputs, logs, and indexes be exported in usable formats? |
| Exit | What happens to data, accounts, integrations, and business operations on termination or supplier failure? |

Record answers, contract links, review date, and unresolved risks in the System Card.

---

## Chapter 3: Governance at SME Scale

| Question | SME Answer |
|---|---|
| Who is accountable? | One named owner per system |
| How much review? | Launch-gate checklist; heavier only for High-risk |
| What about DPDPA? | Determine applicability, complete the checklist, assign internal responsibility, and obtain qualified advice where needed |
| What if it fails? | A one-page [incident report](../12-Templates/AI-Incident-Report-Template.md) and a fix |

### 3.1 Minimum Viable Controls

The five artefacts become effective through a small control routine:

1. **Inventory:** record every approved use, owner, users, supplier, data class, tier, and renewal or review trigger.
2. **Acceptable use:** state which tools and accounts are approved, prohibited data, when human review is required, and which decisions cannot be delegated.
3. **Access:** use organisation-managed accounts, MFA, least privilege, rapid offboarding, and separate administrative access.
4. **Supplier decision:** capture the due-diligence answers above and who accepted residual risk.
5. **Evaluation:** test representative work, known hard cases, harmful requests, unsupported claims, and data leakage before launch.
6. **Human control:** name who checks outputs, what evidence they see, and how they reject, correct, or escalate.
7. **Change and incident:** subscribe to supplier notices; define when a model or feature change triggers re-testing; provide one reporting route and a disable procedure.
8. **Continuity:** retain a manual or previous-system route and export the business records needed to use it.

Roles may be combined, but record responsibilities, decisions, and evidence. For Tier 3, seek a view independent of launch incentives.

### 3.2 Shadow AI

Shadow AI is use of unapproved models, accounts, browser extensions, meeting bots, code assistants, or AI features embedded in existing SaaS. A blanket ban without a usable alternative can drive activity out of sight.

Use a practical response:

- ask teams which tasks they are already trying to improve and what data they use;
- provide at least one approved, affordable tool for low-risk work;
- publish a one-page rule with concrete examples of allowed and prohibited data;
- disable or restrict high-risk integrations through existing tenant and endpoint controls where proportionate;
- monitor administrative discovery, expense, OAuth grants, browser extensions, and data-loss signals in a transparent and lawful manner;
- offer a quick route to request a new tool or use case; and
- respond first with education and containment, escalating deliberate or harmful misuse under normal policy.

Do not collect employee prompts indiscriminately. Monitoring must be lawful, proportionate, communicated, access-controlled, and purposeful.

### 3.3 Jurisdiction and Data Protection

An SME should map the laws and contracts that actually apply to its location, customers, workers, sector, and processing. In India, assess the current text, commencement, rules, and applicability of the [Digital Personal Data Protection Act, 2023](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023). For relevant EU activity, assess the [EU Artificial Intelligence Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) and applicable data-protection law. Do not copy a large-enterprise checklist and mark it complete without understanding the use.

The [NIST AI Risk Management Framework](https://doi.org/10.6028/NIST.AI.100-1) is voluntary guidance organised around Govern, Map, Measure, and Manage. Its [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) identifies generative-AI risks and actions. SMEs can use these as menus: select evidence proportionate to the use rather than claiming certification.

---

## Chapter 4: Assessment and Roadmap

Use a lightweight version of the WG4 maturity assessment (see [WG4](../09-WG-Outputs/WG4-Maturity-Assessment/README.md)). An SME typically follows:

1. **Pilot one use case** with managed services and the MVG artefacts.
2. **Prove value** against a single KPI before expanding.
3. **Standardise** the five artefacts as the default for every new AI use.
4. **Mature selectively** — add controls only where risk justifies them.

This is a practical decision sequence, not a schedule and not a promise of results:

| Step | Action | Evidence to move on |
|---|---|---|
| Discover | Inventory current approved and shadow use; identify data and affected people | Named owners, tool list, immediate containment of unacceptable use |
| Choose | Select one bounded problem with a manual baseline and reversible deployment | Clear user, task, non-AI alternative, risk tier, and stop condition |
| Control | Configure accounts, data rules, supplier settings, budget, access, and fallback | Completed System Card and supplier review; unresolved risks accepted by the right owner |
| Evaluate | Test representative examples and failure cases against the current process | Recorded quality, safety, privacy, security, cost, and user evidence; launch gate decision |
| Pilot | Run with limited users or decisions and active human review | Issues captured, fallback works, records are usable, users understand limits |
| Operate | Assign recurring ownership for changes, incidents, quality, access, and spend | Review triggers, reporting route, disable procedure, and exported business records |
| Reuse or stop | Reuse the pattern only where context is comparable; stop if value or control is inadequate | Documented decision based on evidence, not sunk cost |

Avoid simultaneous experiments that nobody owns. Bring an accepted low-risk use into ordinary ownership, budgeting, support, and review rather than leaving it as a permanent pilot.

---

## Chapter 5: Implementation Patterns

### 5.1 Internal Productivity Assistant

Use an organisation-managed account and prohibit unapproved restricted inputs. Users verify facts, citations, calculations, and tone. Generated content follows normal approval. Prefer a small prompt-pattern library to an elaborate platform.

### 5.2 Grounded Knowledge Assistant

Start with a narrow, maintained collection. Preserve permissions, remove obsolete versions, show citations, and refuse without evidence. Evaluate support and freshness, not fluency alone. If sources cannot be kept current, ordinary search may be safer.

### 5.3 Document Extraction

Ask the model for a constrained schema, validate type and required fields, retain the source document, and route low-confidence or high-consequence cases to review. Do not turn “not found” into a negative fact. Sample completed work after launch to detect supplier or document drift.

### 5.4 Customer-Service Assistance

Begin with agent drafting rather than unsupervised replies. Ground policy answers, protect customer data, disclose AI interaction when appropriate, and make human escalation easy. Do not allow the model to invent refunds, commitments, legal positions, or account actions. Move to automation only for narrow intents with reliable validation and reversibility.

### 5.5 Bounded Workflow Automation

Separate read, draft, approve, and execute permissions. Allow-list tools and fields, validate arguments, limit volume and spend, use short-lived credentials, and prevent duplicate actions. High-impact actions such as payment, account closure, employment decision, or legal submission require authorised human approval unless a competent review establishes another lawful and safe design.

---

## Chapter 6: Failure Modes and Evaluation

### 6.1 Common Failure Modes

| Failure mode | SME impact | Low-cost response |
|---|---|---|
| Consumer account used for confidential work | Data leakage and no admin control | Approved business account, clear examples, offboarding |
| Supplier silently changes model behaviour | Quality or safety regression | Change notices where available, fixed evaluation set, fallback |
| Fluent but unsupported output | Customer, legal, or operational error | Grounding, citations, human verification, refusal |
| Shared API key or excessive permissions | Misuse, unexpected spend, broad compromise | Secrets store, per-service identity, least privilege, rate limits |
| Unbounded usage | Bill shock or denial of service | Per-user/service caps, alerts, quotas, graceful limit response |
| Stale knowledge index | Confident obsolete guidance | Document owner, validity metadata, refresh and deletion process |
| Automation bias | Reviewer approves without judgement | Clear accountability, evidence display, sampled review, training |
| Lock-in | Costly or impossible exit | Export test, open formats, thin integration, manual fallback |
| Shadow tool proliferation | Unknown data and contract exposure | Sanctioned alternative, discovery, fast approval path |
| No incident route | Repeated harm and lost evidence | Single reporting channel, disable owner, one-page incident record |

### 6.2 Evaluation Metrics

Set thresholds from the use's consequence and current process; this guide supplies measures, not invented targets or outcomes.

- **Quality:** task success on a representative test set, factual or extraction error, citation support, reviewer correction, refusal quality, and severe-error count.
- **Human use:** acceptance and rejection reasons, time spent reviewing, escalation success, override, and signs of automation bias.
- **Customer or worker impact:** complaints, corrections, unresolved cases, accessibility barriers, and outcome differences across relevant groups where lawful and meaningful.
- **Security and privacy:** prohibited-data events, unauthorised access, suspicious tool calls, supplier incidents, deletion completion, and shadow-tool discoveries.
- **Reliability:** availability at the point of work, latency, rate-limit failure, duplicate action, fallback success, and recovery after disablement.
- **Cost:** licence and usage cost, review effort, support effort, cost per successfully completed task, budget variance, and exit cost.
- **Governance:** inventory coverage, overdue owner or supplier reviews, unowned systems, users removed on departure, and incidents closed with corrective action.

Compare with the existing process and include the cost of human checking. Stop or redesign when the evidence does not justify ongoing risk and operating effort.

---

## Chapter 7: References

The following sources were checked in October 2026. Confirm current versions and applicability to the organisation:

- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)
- [NIST AI RMF: Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [NIST Small Business Cybersecurity Corner](https://www.nist.gov/itl/smallbusinesscyber)
- [UK National Cyber Security Centre: Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)
- [UK National Cyber Security Centre: Small Business Guide](https://www.ncsc.gov.uk/collection/small-business-guide)
- [CISA Small and Medium-Sized Business Resources](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/smb-resources)
- [Digital Personal Data Protection Act, 2023 — Ministry of Electronics and Information Technology](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023)
- [Regulation (EU) 2024/1689, the EU Artificial Intelligence Act — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)

---

*AIEA Series Guide AIEA-G11: AI for SMEs. Version 1.0, 2026.*
