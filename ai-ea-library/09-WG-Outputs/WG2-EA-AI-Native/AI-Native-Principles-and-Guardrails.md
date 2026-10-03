# AI-Native Principles and Guardrails

| Metadata | Description |
|---|---|
| **Purpose** | Translate AI-native architecture intent into durable decision principles and testable guardrails. |
| **Audience** | Enterprise and solution architects, product and platform teams, data stewards, security teams and governance reviewers. |
| **Use When** | Selecting patterns, reviewing designs, procuring AI services, resolving architecture exceptions or defining platform policy. |
| **Outputs** | Principle decisions, applicable guardrails, verification evidence and documented exceptions. |
| **Content classification** | Principles and guardrails are **Normative** for adopters. Rationale and examples are **Informative**. |

## 1. Interpretation — Normative

A **principle** guides decisions across many solutions. A **guardrail** is a verifiable boundary that implements one or more principles. Adopting organisations may alter implementation details, but shall preserve the stated intent or document an authorised exception with compensating controls.

## 2. Principles — Normative

| ID | Principle | Rationale — Informative | Required implication |
|---|---|---|---|
| P1 | Value before model | A capable model does not establish a worthwhile use. | Record the outcome, owner, evidence source and non-AI alternative before model selection. |
| P2 | Human accountability is not delegated | A system cannot accept organisational or ethical responsibility. | Name a person with authority to approve, intervene and withdraw use. |
| P3 | Proportionate autonomy | Greater action authority creates greater and less reversible exposure. | Grant the least tool and transaction authority needed for the use. |
| P4 | Data is used with context and authority | Available data may still be unsuitable, misleading or unauthorised. | Preserve provenance, permitted use, quality, access and retention controls. |
| P5 | Components remain replaceable | Models, suppliers and economics change independently of business need. | Separate model access, orchestration, data and experience through explicit contracts. |
| P6 | Evaluation is an architecture concern | Generic benchmark quality does not predict behaviour in a specific workflow. | Define use-specific quality, safety and failure tests as architecture requirements. |
| P7 | Trust is earned through evidence | Fluent output can conceal uncertainty and error. | Make provenance, limitations, review and decision evidence available to the relevant user. |
| P8 | Policy travels with execution | Document-only rules cannot stop an unsafe request or action. | Enforce identity, data, content and action policy in the runtime path. |
| P9 | Observability respects purpose | Logs are essential but can create privacy and security risks. | Capture sufficient trace evidence with access, minimisation and retention controls. |
| P10 | Failure is bounded and reversible | AI and connected services will fail in unexpected ways. | Provide limits, interruption, fallback and controlled retirement mechanisms. |

## 3. Baseline guardrails — Normative

| ID | Guardrail | Verification |
|---|---|---|
| G01 | Every production AI interaction shall be attributable to an authenticated workload or user where the context permits identification. | Sample traces and confirm identity propagation and service-account ownership. |
| G02 | The model shall receive only data allowed for the user, purpose and provider boundary. | Test retrieval and prompt assembly with users from different access groups. |
| G03 | Prompts, policies, model configuration and evaluation sets shall be version-controlled. | Trace a sampled output to deployed artefact versions. |
| G04 | Model access shall pass through an approved interface that applies authentication, routing and telemetry. | Inspect network paths and attempt unapproved direct access. |
| G05 | Tool use shall be allow-listed, schema-validated and least-privileged. | Attempt an unlisted tool, invalid parameter and excessive permission. |
| G06 | Consequential or irreversible actions shall require explicit authorised confirmation unless a stronger reviewed control is approved. | Run a representative action and verify the confirmation and recorded decision. |
| G07 | Use-specific evaluation shall be completed before operational exposure and after material behavioural change. | Reproduce evaluation results for the deployed configuration. |
| G08 | User interfaces shall identify AI involvement and communicate material limitations where misunderstanding could cause harm. | Review representative interfaces and user instructions. |
| G09 | Retrieval responses shall preserve source references when the use depends on factual grounding. | Sample outputs and trace statements to authorised source material. |
| G10 | Operational limits shall cover execution steps, transaction scope, data volume and cost where applicable. | Test each limit and confirm safe handling when reached. |
| G11 | A competent operator shall be able to pause the system or remove action authority. | Exercise the stop mechanism and verify downstream access is disabled. |
| G12 | Supplier or model substitution shall not bypass classification, evaluation or approval. | Review a substitution record and compare behaviour and obligations. |

## 4. Context-specific guardrails — Normative

Apply these when the trigger is present.

| Trigger | Additional guardrail |
|---|---|
| Personal or confidential data | Complete privacy and security assessment; minimise prompts and logs; verify deletion and processor boundaries |
| External communication | Apply approved content policy, disclosure, escalation and sampled quality review |
| Software or infrastructure change | Use isolated execution, protected branches, automated tests and authorised release |
| Financial or contractual action | Enforce transaction limits, separation of duties, confirmation and reconciliation |
| Safety-relevant advice | Use authoritative sources, domain review, clear limitation statements and a non-AI route |
| Persistent memory | Define allowed memory content, user visibility, correction, expiry and deletion |
| Multi-agent workflow | Constrain delegation, propagate identity and policy, and retain an understandable action trace |

## 5. Exception workflow — Normative

1. State the guardrail and why the standard mechanism is unsuitable.
2. Describe the affected use, users, data, actions and duration condition.
3. Assess added risk and propose compensating controls.
4. Obtain approval from the accountable owner and relevant control function.
5. Record withdrawal conditions based on architecture or risk change.
6. Test the compensating controls and retain evidence.

An exception shall not be used to bypass an applicable legal prohibition or conceal unresolved risk.

## 6. Architecture review checklist — Normative

- [ ] The outcome and non-AI alternative are documented.
- [ ] Accountable ownership and intervention authority are clear.
- [ ] Data access follows user and purpose permissions.
- [ ] Model and provider dependencies have an exit route.
- [ ] Tools and autonomous actions are bounded.
- [ ] Evaluation criteria represent the real operating context.
- [ ] Users receive the provenance and limitations needed for sound judgement.
- [ ] Traces are useful, protected and no broader than necessary.
- [ ] Failure, supplier change and retirement have controlled paths.
- [ ] Exceptions have evidence, approval and withdrawal conditions.

## 7. Applying the set — Informative

For a retrieval assistant, principles P4, P6, P7 and P8 usually drive the design: access-filtered retrieval, citation checks, evaluation against authoritative content and runtime policy. For an action-taking agent, P2, P3 and P10 become decisive: narrow permissions, confirmations, transaction limits and interruption. The same principles remain stable while guardrail implementation changes with context.

## Related links

- [WG2 reference set](README.md)
- [AI-Native Enterprise Architecture](AI-Native-EA-White-Paper.md)
- [AI-Native Reference Architecture](AI-Native-Reference-Architecture.md)
- [Core Concepts and Architecture Principles](../../05-Standards/AIEA-101-Introduction-Core-Concepts.md)
- [AI Risk Classification Framework](../WG1-AI-Governance-Playbook/AI-Risk-Classification-Framework.md)

