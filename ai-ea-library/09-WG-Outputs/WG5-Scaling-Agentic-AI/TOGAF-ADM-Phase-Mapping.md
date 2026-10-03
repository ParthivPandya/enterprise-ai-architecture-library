# Agentic AI Mapping to the TOGAF ADM

| Metadata | Description |
|---|---|
| **Purpose** | Map agentic AI architecture concerns to TOGAF ADM phases using explicit inputs, activities and outputs. |
| **Audience** | Enterprise and solution architects, architecture governance bodies, agentic product teams, security and risk functions and operational owners. |
| **Use When** | Applying a TOGAF-aligned method to an agentic initiative or checking that agent-specific concerns are covered across architecture work. |
| **Outputs** | Phase-specific agentic decisions, architecture artefacts, control evidence and traceability to enterprise architecture governance. |
| **Content classification** | Required agentic concerns and artefacts are **Normative** for adopters of this mapping. Explanatory examples are **Informative**. |

> This is independent practitioner guidance. It is not an official publication of or endorsed extension to the TOGAF Standard. Use the applicable authorised TOGAF material for the method itself.

## 1. Cross-phase requirements — Normative

Maintain the following throughout the ADM:

- permitted goal and excluded uses;
- accountable owner and delegated authority;
- affected people and decision consequences;
- data, model, memory, tool and supplier requirements;
- human decision and intervention requirements;
- trajectory evaluation and acceptance evidence;
- security, privacy, resilience and trace requirements;
- cost, portability and retirement requirements; and
- changes that require renewed architecture or governance review.

Requirements shall trace to architecture elements, tests and decisions. A prompt is an implementation artefact, not a substitute for a requirement.

## 2. Phase mapping — Normative

| ADM phase | Agentic inputs | Agentic activities | Agentic outputs |
|---|---|---|---|
| **Preliminary** | Enterprise principles, governance model, risk appetite, existing platform and repository | Define agent taxonomy, decision rights, tool onboarding, evidence rules and reference controls | Agentic principles, governance route, metamodel extensions, approved service boundaries |
| **A — Architecture Vision** | Business concern, affected stakeholders, baseline process, strategic constraints | Test need for agency; compare simpler alternatives; define goal, value, harm and authority boundary | Vision, scope, stakeholder concerns, initial classification, outcome and authority statement |
| **B — Business Architecture** | Capabilities, processes, roles, decisions, policies and service obligations | Map human and agent responsibilities; identify exceptions, separation of duties and fallback work | Capability and process views, accountability model, human-decision points, business measures |
| **C — Information Systems Architectures** | Data products, applications, interfaces, records and information rules | Design memory, retrieval, state, tool contracts, identity propagation and authoritative record interaction | Data lineage, state model, application co-operation view, tool and API catalogue |
| **D — Technology Architecture** | Runtime, networks, identity, model services, observability and operational constraints | Select orchestration, isolation, gateway, policy, secrets, telemetry and recovery mechanisms | Deployment view, trust boundaries, platform services, technology standards and resilience design |
| **E — Opportunities and Solutions** | Architecture gaps, reusable building blocks, portfolio candidates and supplier options | Group work packages; evaluate reuse; compare build, buy and shared-service choices | Solution concept, work packages, dependency map, procurement requirements |
| **F — Migration Planning** | Dependencies, organisational capacity, transition risks and accepted solution concept | Order capability changes by prerequisite; protect coexistence and fallback; define acceptance evidence | Dependency-led transition architectures, prioritised packages, acceptance and withdrawal conditions |
| **G — Implementation Governance** | Contracts, detailed designs, evaluation results, control evidence and deviations | Review conformance; test tools and limits; assess exceptions; verify operational readiness | Conformance decisions, accepted exceptions, evaluation evidence, operational authorisation |
| **H — Architecture Change Management** | Incidents, user challenges, supplier changes, cost and quality evidence | Assess material change; update patterns and requirements; constrain, replace or retire unsafe capability | Change decisions, revised architecture, updated controls, retirement or substitution record |

## 3. Preliminary Phase guidance — Informative

Extend the architecture repository to represent agent, goal, model, memory, tool, policy, human decision, evaluation set and execution trace. Define allowed relationships, such as **agent uses tool**, **tool accesses application** and **human authorises action**. Establish who may approve a new tool or broader permission.

## 4. Phases A and B decision questions — Normative

- Why is dynamic planning or tool selection needed?
- Which organisational outcome changes?
- Who is affected by error, delay, manipulation or unavailable service?
- Which decisions remain human, and can that person meaningfully disagree?
- What actions are excluded regardless of user request?
- What safe process remains when the agent is unavailable?

The Architecture Vision should not promise autonomy. It should describe bounded delegated capability.

## 5. Phase C information and application rules — Normative

Architecture shall distinguish:

| Element | Required treatment |
|---|---|
| Working state | Schema, integrity, access and failure recovery |
| Persistent memory | Purpose, permitted content, correction, expiry and deletion |
| Retrieved knowledge | Provenance, user entitlement, freshness and citation |
| Prompt and policy | Versioning, separation and change control |
| Tool contract | Owner, schema, permissions, validation and error behaviour |
| System of record | Reconciliation and idempotency after action |

Generated state shall not become an authoritative record without validation by the owning system or authorised person.

## 6. Phase D technology controls — Normative

- Use workload identities rather than shared credentials.
- Isolate untrusted content and code execution.
- Apply policy and schema validation outside model discretion.
- Limit steps, retries, transaction scope, data volume and cost where applicable.
- Correlate goals, model calls, tool actions, approvals and outcomes.
- Protect traces as potentially sensitive records.
- Provide pause, credential revocation and safe recovery.
- Design provider and model substitution through explicit interfaces.

## 7. Phases E and F selection — Normative

Use the [Prioritisation Method](Prioritisation-Method.md) to compare agentic opportunities. Group shared capabilities such as identity propagation, tool registry, evaluation and intervention separately from product-specific outcomes. Order packages by dependency rather than date.

Transition architecture shall cover coexistence with manual or deterministic processes, incomplete transactions, data migration, permission migration and the conditions for returning to a safer mode.

## 8. Phase G conformance gate — Normative

- [ ] Deployed goals, tools and permissions match the approved boundary.
- [ ] Human approvals and separation of duties operate as designed.
- [ ] Evaluation covers successful, failed, manipulated and interrupted trajectories.
- [ ] Tool calls are schema-validated, least-privileged and traceable.
- [ ] Operational limits and stop controls have been exercised.
- [ ] Partial actions can be reconciled or compensated.
- [ ] Monitoring and incident routes have accountable owners.
- [ ] Supplier obligations and exit artefacts are available.
- [ ] Residual risks and exceptions have authorised decisions.

## 9. Phase H change triggers — Normative

Re-enter the relevant ADM work when there is a material change to goal, affected users, model, data, memory, tool, permission, transaction boundary, orchestration, supplier, deployment environment or evidence of harm. The architecture function should identify which prior assumptions are invalid rather than restarting every activity mechanically.

## 10. Traceability checklist — Normative

- [ ] Business outcomes trace to measures and accountable owners.
- [ ] Agent goals trace to permitted business activities.
- [ ] Tools and data trace to least-privilege authority.
- [ ] Risks trace to controls, tests and intervention.
- [ ] Human decisions trace to information and authority.
- [ ] Architecture decisions trace to evidence and alternatives.
- [ ] Operational findings trace to change decisions.
- [ ] Retirement traces to revoked access, handled data and updated dependencies.

## Related links

- [WG5 reference set](README.md)
- [Scaling Agentic AI](Scaling-Agentic-AI-White-Paper.md)
- [Prioritisation Method](Prioritisation-Method.md)
- [Agentic AI Architecture Guide](../../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)
- [Agentic AI Operating Model](../../11-Architecture-Diagrams/ArchiMate/Agentic-AI-Operating-Model.archimate)
