# AI-Native Reference Architecture

| Metadata | Description |
|---|---|
| **Purpose** | Provide a technology-neutral decomposition for AI-enabled enterprise solutions and their control boundaries. |
| **Audience** | Enterprise, solution, data, security and platform architects; engineering leads; governance reviewers; and service owners. |
| **Use When** | Creating solution architecture, defining shared AI platform services, reviewing supplier designs or identifying reusable building blocks. |
| **Outputs** | Context view, selected components, trust boundaries, interface contracts, control placement and architecture decisions. |
| **Content classification** | Component responsibilities and boundary rules are **Normative** for adopters. Deployment examples are **Informative**. |

## 1. Logical structure — Normative

```text
People and Channels
        |
Experience and Interaction
        |
Workflow and Agent Orchestration ---- Human Decision Points
        |
Policy Enforcement and AI Gateway
     /          |             \
Model Services  Knowledge      Enterprise Tools and APIs
                and Retrieval
     \          |             /
        Data Products and Records
                |
Platform, Identity, Security and Operations

Governance, Evaluation and Observability apply across every layer.
```

The structure is logical. Components may share infrastructure, but their responsibilities and trust boundaries shall remain distinguishable.

## 2. Layer responsibilities — Normative

| Layer | Responsibilities | Required contracts |
|---|---|---|
| People and channels | Establish user identity, context, accessibility and permitted interaction | User role, consent or notice where applicable, channel constraints |
| Experience and interaction | Collect input, show provenance and limitations, request confirmation, support challenge | Input schema, disclosure, error and feedback behaviour |
| Workflow and agent orchestration | Manage state, task decomposition, approvals, retries and tool selection | State model, step limits, approval points, failure path |
| Policy enforcement and AI gateway | Authenticate, authorise, route, filter, limit and record model requests | Identity, model policy, quota, logging and provider route |
| Model services | Generate, classify, predict, embed or moderate | Capability, version, context limits, data terms and service behaviour |
| Knowledge and retrieval | Ingest, index, filter, retrieve and cite enterprise information | Source authority, access filter, freshness and citation format |
| Enterprise tools and APIs | Read or change enterprise systems through bounded functions | Tool schema, permission, validation, transaction and idempotency rules |
| Data products and records | Provide governed operational, analytical and reference data | Steward, semantics, quality, lineage, access and retention |
| Platform and operations | Supply runtime, secrets, networking, deployment, monitoring and recovery | Environment, service identity, resilience and support model |
| Governance and evaluation | Classify, test, approve and retain evidence | Risk record, evaluation criteria, control and decision records |

## 3. Primary flows — Normative

### 3.1 Grounded assistance

1. Authenticate the user and pass relevant entitlements.
2. Validate and classify the request.
3. Retrieve only authorised source material.
4. Assemble the prompt with source identifiers and policy instructions.
5. Route to an approved model.
6. Check the response for policy, grounding and format;
7. present sources, limitations and a feedback route; and
8. retain an appropriately minimised trace.

### 3.2 Bounded action

1. Establish the user’s goal and the system’s delegated authority.
2. Build a plan using only approved tools.
3. validate every tool call against identity, schema and policy;
4. require confirmation at consequential boundaries;
5. execute with transaction and repetition limits;
6. verify the result against the source system;
7. report actions and unresolved exceptions; and
8. preserve an action trace suitable for investigation.

## 4. Trust boundaries — Normative

| Boundary | Principal risk | Required controls |
|---|---|---|
| Channel to experience | Impersonation, malicious input, misleading disclosure | Authentication, input handling, rate limits, clear user information |
| Experience to orchestration | Prompt injection and untrusted state | Structured messages, policy separation, state validation |
| Orchestration to model | Data leakage and unapproved model use | Gateway, routing policy, data minimisation, provider controls |
| Retrieval to source | Permission loss, stale or poisoned content | Entitlement filtering, provenance, freshness and ingestion checks |
| Orchestration to tool | Excessive or malformed action | Allow-list, schema validation, least privilege, confirmation |
| Provider to enterprise | Supplier change, retention and service dependency | Contract controls, monitoring, version record and exit design |
| Telemetry to operators | Sensitive trace exposure | Redaction, role-based access, retention and audit |

Identity and policy context shall propagate across boundaries. A downstream component shall not infer authority merely because an upstream component called it.

## 5. Architecture variants — Informative

| Variant | Suitable use | Key caution |
|---|---|---|
| Direct model assistance | Low-impact drafting or transformation without enterprise data | User may over-rely on fluent output |
| Retrieval-augmented assistant | Questions grounded in controlled documents | Permission filtering and source freshness are part of correctness |
| Guided workflow assistant | Multi-step work with human decisions | State and hand-offs must remain understandable |
| Bounded agent | Repetitive actions through narrow tools | Tool permissions and interruption dominate risk |
| Specialised predictive service | Stable classification or forecasting task | Data drift and decision integration require monitoring |

Do not select a more autonomous variant merely to demonstrate technical capability.

## 6. Required architecture artefacts — Normative

- context view showing users, affected parties, systems and suppliers;
- data-flow view covering prompts, retrieval, outputs, logs and retained state;
- identity and permission model from channel through model and tools;
- component and deployment view with trust boundaries;
- decision record for model, retrieval and orchestration choices;
- threat model including prompt, model, data, tool and supply-chain risks;
- evaluation plan linked to business and safety requirements;
- operational view with alerts, intervention, recovery and retirement; and
- dependency inventory covering models, datasets, services and policy artefacts.

## 7. Review checklist — Normative

- [ ] The system boundary includes embedded and external AI services.
- [ ] Components have one clear responsibility and explicit contracts.
- [ ] Identity and data entitlements survive retrieval and tool calls.
- [ ] Model access is mediated by approved policy enforcement.
- [ ] Generated instructions cannot directly expand tool authority.
- [ ] Evaluation and telemetry are designed, not added after deployment.
- [ ] Sensitive traces are minimised and protected.
- [ ] Failure paths preserve essential business operation.
- [ ] Model and supplier changes can be evaluated and reversed.
- [ ] Human decision points match consequence and uncertainty.

## Related links

- [WG2 reference set](README.md)
- [AI-Native Principles and Guardrails](AI-Native-Principles-and-Guardrails.md)
- [Value Realisation Model](Value-Realisation-Model.md)
- [Enterprise AI Capability Map](../../11-Architecture-Diagrams/SVG/Enterprise-AI-Capability-Map.svg)
- [AI Governance Playbook](../WG1-AI-Governance-Playbook/AI-Governance-Playbook.md)
