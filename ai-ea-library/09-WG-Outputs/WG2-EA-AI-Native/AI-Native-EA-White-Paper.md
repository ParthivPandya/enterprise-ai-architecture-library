# AI-Native Enterprise Architecture

| Metadata | Description |
|---|---|
| **Purpose** | Explain how enterprise architecture changes when AI becomes a reusable organisational capability rather than an isolated application feature. |
| **Audience** | Enterprise and solution architects, technology leaders, product owners, data leaders, governance functions and platform teams. |
| **Use When** | Setting architecture direction, reshaping an EA practice, evaluating an AI-enabled operating model or aligning multiple AI investments. |
| **Outputs** | Shared AI-native vocabulary, architecture decision agenda, capability gaps, platform boundary and governance priorities. |
| **Content classification** | The architecture expectations are **Normative** for adopters. The thesis, examples and observations are **Informative**. |

## 1. Thesis — Informative

An enterprise is AI-native when it can repeatedly combine trusted data, suitable models, governed automation and human judgement to improve how work is performed. This is not achieved by adding a conversational interface to existing systems. It requires architecture that treats model behaviour as probabilistic, data and prompts as operational dependencies, evaluation as a delivery discipline and governance as part of the execution path.

Traditional applications usually encode behaviour in deterministic logic. AI-enabled systems can vary with model version, context, retrieved information and user phrasing. Their architecture must therefore control a wider set of change: data, model, prompt, tool, policy and evaluation artefacts. The EA practice becomes responsible not only for structural alignment but also for the conditions under which generated outputs and automated actions can be trusted.

## 2. Defining characteristics — Normative

An AI-native architecture should exhibit the following characteristics.

| Characteristic | Architecture expectation |
|---|---|
| Value-led | Every use has a named outcome, decision owner and method for measuring value and harm. |
| Composable | Models, retrieval, tools, policies and channels are replaceable components with explicit contracts. |
| Data-grounded | Authoritative enterprise context is accessed through governed data products and retrieval services. |
| Evaluated | Quality, safety, security and operational behaviour are tested against use-specific criteria. |
| Observable | Inputs, decisions, model and tool versions, costs and significant outcomes can be traced appropriately. |
| Human-centred | Interfaces communicate limitations and place human intervention where consequence demands it. |
| Secure by boundary | Identities, data, models and tools are separated by least-privilege trust boundaries. |
| Governed in execution | Policy checks, approvals and limits operate within workflows, not only in documents. |
| Economically transparent | Cost is attributable to a business outcome and architecture choice. |
| Reversible | Providers, models and unsafe capabilities can be changed, isolated or disabled without uncontrolled disruption. |

## 3. How EA responsibilities change — Informative

| Established EA concern | AI-native extension |
|---|---|
| Business capability | Identify where prediction, generation or action changes a capability and its accountabilities |
| Information architecture | Add training, retrieval, prompt, output and feedback lineage |
| Application architecture | Separate experience, orchestration, model access, tools and policy enforcement |
| Technology architecture | Address accelerators, inference, model gateways, vector retrieval and evaluation services |
| Security architecture | Model prompt injection, data leakage, unsafe agency and supply-chain change |
| Governance | Classify use, select controls, evaluate behaviour and retain decision evidence |
| Portfolio management | Compare outcome value, risk, reuse potential, operational burden and exit options |

EA should not own every model or prompt. It should establish reusable boundaries, decision rules and repository content that enable product teams to work consistently.

## 4. Architecture decision agenda — Normative

For each AI-enabled capability, architects shall make the following decisions explicit:

1. **Outcome:** Which human or organisational decision improves, and how will that improvement be observed?
2. **Operating boundary:** Which users, channels, data, actions and excluded uses define the system?
3. **Interaction mode:** Is AI assisting, recommending, deciding or acting?
4. **Grounding:** Which authoritative sources provide context, and how are provenance and access preserved?
5. **Model access:** Is a managed service, hosted model or specialised model appropriate, and what is the exit route?
6. **Orchestration:** How are prompts, tools, state, policies and human approvals co-ordinated?
7. **Evaluation:** Which datasets, scenarios and acceptance rules represent useful and safe behaviour?
8. **Operations:** Which signals reveal drift, misuse, service failure, cost change or user harm?
9. **Governance:** Which risk tier, controls, decision authority and evidence are required?
10. **Evolution:** Which changes can be routine, and which require renewed evaluation or approval?

The answers belong in architecture decisions and system records, not only in implementation code.

## 5. Operating model — Normative

A practical operating model divides responsibility without creating an isolated AI function.

| Capability | Enterprise responsibility | Product responsibility |
|---|---|---|
| Principles and risk rules | Define common guardrails and decision rights | Apply them and record justified exceptions |
| Shared platform | Provide identity, model access, retrieval, policy, evaluation and telemetry capabilities | Configure within approved boundaries |
| Data products | Define stewardship, contracts and access mechanisms | Use only authorised data for the stated purpose |
| Evaluation | Provide methods, tooling and common safety suites | Define domain criteria and investigate failures |
| Operations | Define incident interfaces and enterprise signals | Own service behaviour, user support and intervention |
| Architecture repository | Maintain reference patterns and common building blocks | Maintain system-specific decisions and dependencies |

Central services should reduce duplicated control effort, but must not obscure accountability for an individual use.

## 6. Decision workflow — Normative

1. **Frame the outcome** without assuming AI is the solution.
2. **Compare alternatives**, including rules, search, process change and conventional automation.
3. **Classify the use** by consequence, data, autonomy and exposure.
4. **Select a pattern** from the [AI-Native Reference Architecture](AI-Native-Reference-Architecture.md).
5. **Apply principles and guardrails** before supplier or model choices harden.
6. **Define value and evaluation evidence** together so quality claims relate to the outcome.
7. **Review the architecture** across business, data, application, technology, security and governance views.
8. **Authorise and operate** with observable controls and clear intervention authority.

## 7. Common failure modes — Informative

| Failure mode | Architectural response |
|---|---|
| Model-first procurement | Start with outcome, constraints and evaluation; compare solution classes |
| One platform for every use | Use shared interfaces while allowing proportionate model and deployment choices |
| Uncontrolled retrieval | Treat indexing, permissions, freshness and citations as managed data products |
| Human review in name only | Test whether reviewers can detect error and intervene |
| Governance after build | Put classification, policy and evidence requirements into the delivery workflow |
| Claimed value without baseline | Define the decision, evidence source and counterfactual before relying on benefit claims |
| Provider dependence | Use contracts, abstraction and exportable artefacts to preserve exit options |

## 8. Reader checklist — Normative

- [ ] The AI-native definition is tied to operating capability, not product branding.
- [ ] Every proposed use has a non-AI alternative for comparison.
- [ ] Shared services preserve system-level accountability.
- [ ] Data, prompt, model, tool and evaluation artefacts are governed dependencies.
- [ ] Architecture decisions cover failure, intervention and exit.
- [ ] Value evidence includes quality, risk and operating cost.
- [ ] External requirements are validated independently rather than inferred from this paper.

## Related links

- [WG2 reference set](README.md)
- [AI-Native Principles and Guardrails](AI-Native-Principles-and-Guardrails.md)
- [AI-Native Reference Architecture](AI-Native-Reference-Architecture.md)
- [Value Realisation Model](Value-Realisation-Model.md)
- [Maturity Model and Adoption Roadmap](Maturity-Model-and-Adoption-Roadmap.md)
- [Architecting the AI-First Enterprise](../../08-Domain-Portfolios/WP-02-Architecting-the-AI-First-Enterprise.md)

