# Maturity Model and Adoption Roadmap

| Metadata | Description |
|---|---|
| **Purpose** | Help an organisation describe its AI-native capability and choose a dependency-led route for strengthening it. |
| **Audience** | Enterprise architecture leaders, technology executives, product and platform leaders, governance functions and capability owners. |
| **Use When** | Comparing observed practices with desired capabilities, selecting improvement packages or checking whether wider reuse is supportable. |
| **Outputs** | Evidence-based capability profile, chosen capability outcomes, dependency map and prioritised improvement packages. |
| **Content classification** | Assessment and sequencing rules are **Normative** for adopters. Capability descriptions and examples are **Informative**. |

> This roadmap is a logical sequence, not a calendar, delivery tracker or promise of organisational performance. Movement depends on verified capability evidence and local priorities.

## 1. Maturity levels — Informative

| Level | Description | Typical evidence |
|---|---|---|
| **1 — Isolated** | AI uses are selected and built separately; ownership and evidence vary by team. | Individual solution documents and local controls |
| **2 — Governed** | Common classification, ownership, architecture review and evaluation expectations are applied. | Inventory, decision records, control evidence |
| **3 — Reusable** | Shared data, model access, evaluation and observability capabilities reduce duplication. | Service contracts, reusable patterns, common telemetry |
| **4 — Adaptive** | Operational evidence informs architecture, policy and portfolio choices across products. | Traceable feedback, comparative evidence, controlled component substitution |

Levels describe capability coherence, not organisational merit. Different dimensions may legitimately sit at different levels.

## 2. Assessment dimensions — Normative

Assess each dimension independently and cite evidence.

| Dimension | Isolated | Governed | Reusable | Adaptive |
|---|---|---|---|---|
| Strategy and value | Technology-led ideas | Outcome and owner recorded | Comparable portfolio evidence | Decisions adapt to observed value and harm |
| Governance | Local judgement | Common classification and controls | Policy integrated into shared services | Control design improves from operational learning |
| Data and knowledge | Project copies | Stewardship and provenance | Governed data and retrieval products | Quality and access signals shape runtime behaviour |
| Architecture | Point integrations | Standard boundaries and decisions | Composable shared building blocks | Components change through controlled evidence |
| Evaluation | Demonstrations | Use-specific acceptance tests | Shared evaluation service and reusable suites | Operational cases enrich controlled evaluation |
| Platform and operations | Team-specific runtime | Minimum security and monitoring | Shared gateway, identity and telemetry | Routing and limits respond to verified conditions |
| People and operating model | Informal specialists | Named roles and decision rights | Federated practice with common methods | Cross-functional learning changes standards and patterns |
| Economics | Supplier bill visibility | Attributable full-cost view | Reuse and unit-cost comparison | Architecture choices respond to outcome economics |

An assessor shall not assign a level from aspiration, tool ownership or policy text alone. Evidence must show repeated practice.

## 3. Scoring rule — Normative

For each dimension:

1. identify the highest level for which every essential characteristic is evidenced;
2. record missing or contradictory evidence;
3. avoid averaging away a weak dimension that creates a critical dependency; and
4. preserve separate dimension results rather than presenting one maturity number as objective truth.

A heatmap is preferable to a single score because it exposes uneven capability. Where a summary is required, use the lowest level among dimensions essential to the intended adoption decision.

## 4. Capability packages — Normative

Choose packages by outcome and dependency, not by fashionable technology.

| Package | Capability outcome | Prerequisites | Completion evidence |
|---|---|---|---|
| A. Know the estate | AI uses, owners, boundaries and dependencies are visible | Executive mandate and repository owner | Sampled inventory is complete enough for decisions |
| B. Govern decisions | Risk, controls, exceptions and approvals are repeatable | Package A | Reperformed classifications and traceable decisions |
| C. Establish trusted data | Data and knowledge sources are authorised, traceable and access-filtered | Packages A and B | Data contracts, lineage and permission tests |
| D. Evaluate behaviour | Quality, safety and failure tests represent actual use | Packages A and B; Package C where grounded data is used | Reproducible evaluation and defect handling |
| E. Provide shared access | Model gateway, identity, policy and telemetry are reusable | Packages B and D | Multiple uses consume controlled interfaces |
| F. Enable bounded action | Tools, approvals, limits and interruption support safe automation | Packages B, D and E | Action traces and exercised stop controls |
| G. Manage value and economics | Outcome, risk and full cost evidence inform choices | Packages A, D and E | Comparable value decision records |
| H. Learn across the estate | Operational evidence improves patterns and controls | Packages B through G as applicable | Approved changes trace to evidence across uses |

Not every organisation needs every package. A narrow portfolio may remain effective with governed practices and limited shared infrastructure.

## 5. Adoption route — Normative

1. **Choose the decision:** State which organisational choice the assessment must support.
2. **Gather evidence:** Interview responsible roles and inspect records, systems and sampled operation.
3. **Profile capabilities:** Apply the dimension rubric and record uncertainty.
4. **Identify constraints:** Find the dimensions that block the desired capability outcome.
5. **Select packages:** Choose the smallest set that resolves those constraints.
6. **Map dependencies:** Order packages so governance, data and evaluation foundations support later reuse or autonomy.
7. **Define acceptance evidence:** State what observable evidence shows each package works.
8. **Review coherence:** Confirm that people, process, information and technology change together.

## 6. Prioritisation matrix — Informative

| Consideration | Question |
|---|---|
| Risk reduction | Which package removes an unmanaged high-consequence exposure? |
| Value enablement | Which package unlocks a credible business outcome? |
| Reuse | Which package benefits several justified uses without forcing uniformity? |
| Dependency | Which missing foundation makes other investment unsafe or wasteful? |
| Evidence | Which package can demonstrate operation rather than only produce policy? |
| Reversibility | Which choice preserves model, supplier and architecture options? |

## 7. Review checklist — Normative

- [ ] Every maturity judgement cites operational evidence.
- [ ] Dimension results remain visible rather than being hidden by an average.
- [ ] Desired capability follows business need and risk.
- [ ] Packages have dependency and completion evidence, not date promises.
- [ ] Shared services are justified by reuse rather than centralisation alone.
- [ ] Greater autonomy is not treated as inherently more mature.
- [ ] Improvement choices preserve human accountability and exit options.
- [ ] The profile is reassessed when material evidence or organisational need changes.

## Related links

- [WG2 reference set](README.md)
- [AI-Native Enterprise Architecture](AI-Native-EA-White-Paper.md)
- [AI-Native Principles and Guardrails](AI-Native-Principles-and-Guardrails.md)
- [Value Realisation Model](Value-Realisation-Model.md)
- [Enterprise AI Readiness Assessment Toolkit](../../07-Toolkits-and-Playbooks/01-AI-Readiness-Assessment-Toolkit.md)
