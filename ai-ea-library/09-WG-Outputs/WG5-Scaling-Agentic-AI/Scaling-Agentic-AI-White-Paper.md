# Scaling Agentic AI

| Metadata | Description |
|---|---|
| **Purpose** | Provide an industry-neutral framework for moving from isolated agentic uses to a governed portfolio of reusable, bounded capabilities. |
| **Audience** | Enterprise and solution architects, technology leaders, product owners, platform teams, security and governance functions and operational owners. |
| **Use When** | Evaluating agentic use cases, defining shared platform capabilities, increasing action authority or governing multiple agentic systems. |
| **Outputs** | Agent boundary, authority model, shared-capability design, evaluation strategy, operating model and portfolio decision criteria. |
| **Content classification** | Scaling requirements and control boundaries are **Normative** for adopters. The framing and examples are **Informative**. |

## 1. What scaling means — Informative

An agentic AI system interprets a goal, maintains state, selects actions and uses tools to influence an environment. Scaling such systems does not mean maximising autonomy or deploying more agents. It means enabling justified uses to reuse trusted capabilities while preserving purpose, permissions, evidence, intervention and accountability.

The main architectural change is that generated content becomes generated action. A mistaken answer may mislead; a mistaken tool call may change a record, send a message, create a commitment or disrupt an operation. Scale therefore depends on controlled authority more than model sophistication.

## 2. Scaling principles — Normative

1. **Bound the goal:** Every agent shall have a permitted objective and excluded actions.
2. **Minimise authority:** Tools, data and transaction scope shall be no broader than needed.
3. **Separate planning from execution:** Generated intent shall pass deterministic policy and validation before action.
4. **Keep accountable decisions human:** Delegation does not transfer organisational responsibility.
5. **Make state explicit:** Inputs, plan, tool results, approvals and termination shall be understandable.
6. **Design interruption:** Operators shall be able to pause, constrain and revoke action authority.
7. **Evaluate trajectories:** Tests shall examine sequences and outcomes, not only final text.
8. **Reuse controls, not hidden context:** Shared services should standardise identity, policy, tools, telemetry and evidence.
9. **Preserve exit:** Models, orchestrators and suppliers should be replaceable through clear contracts.
10. **Scale from evidence:** Wider reach or authority requires evidence from representative operation and failure testing.

## 3. Six-domain scaling framework — Normative

| Domain | Required capability | Key evidence |
|---|---|---|
| Purpose and portfolio | Comparable selection, named outcome, accountable owner and stop decision | Use-case record and prioritisation decision |
| Authority and governance | Risk classification, delegated authority, approval boundaries and exception handling | Authority matrix, decision record |
| Architecture and platform | Standard identity, tool contracts, state, model access, policy and telemetry | Reference conformance and interface tests |
| Evaluation and safety | Representative trajectories, adversarial cases, permission tests and recovery | Versioned evaluation results |
| Operations and resilience | Monitoring, intervention, reconciliation, incident response and fallback | Exercises, action traces, runbooks |
| Economics and suppliers | Attributable cost, service dependency, portability and exit | Cost record, supplier obligations, substitution evidence |

Weakness in one domain cannot be compensated for by adding more capable models.

## 4. Agent boundary model — Normative

Every agentic system shall define:

| Boundary | Required decision |
|---|---|
| Goal | Permitted outcome and excluded interpretation |
| Actor | User, workload or event allowed to invoke it |
| Context | Data the agent may read and retain |
| Tools | Functions, parameters and systems it may call |
| Transactions | Value, volume, object and repetition limits |
| Human control | Actions requiring review, confirmation or separation of duties |
| Termination | Success, failure, step, cost and safety stop conditions |
| Evidence | Trace required for operation, review and investigation |
| Fallback | Safe non-agentic process or contained failure state |

Natural-language instructions alone are not sufficient enforcement for permissions or transaction boundaries.

## 5. Shared platform capabilities — Normative

| Capability | Enterprise service | System responsibility |
|---|---|---|
| Identity and delegation | Workload identity, user context and token exchange | Request only needed scopes |
| Tool registry | Approved schemas, owners, risk attributes and versions | Select allow-listed tools |
| Policy enforcement | Authorisation, content, transaction and data rules | Supply complete context; handle denial safely |
| Model gateway | Approved routing, credentials and telemetry | Define capability and quality requirements |
| State service | Protected checkpoints and retention controls | Store only necessary state |
| Evaluation | Harness, trace replay and shared safety cases | Provide domain scenarios and acceptance rules |
| Observability | Standard events, correlation and secure access | Emit meaningful goal, action and outcome signals |
| Intervention | Pause, revoke, isolate and recover | Define safe stop and reconciliation |

Shared services should expose clear service contracts. A platform team does not assume the product owner’s accountability for use-specific behaviour.

## 6. Portfolio archetypes — Informative

| Archetype | Example | Typical authority | Dominant concern |
|---|---|---|---|
| Research agent | Gather and summarise approved information | Read-only | Source quality and disclosure |
| Workflow co-ordinator | Route cases and request human decisions | Bounded state change | Handover and process integrity |
| Transaction assistant | Prepare an action for confirmation | Draft or staged write | Validation and authorised approval |
| Bounded operator | Execute narrow, reversible actions | Constrained write | Permissions, limits and reconciliation |
| Multi-agent process | Delegate specialised sub-tasks | Mixed, inherited authority | Policy propagation and understandable state |

The archetype describes architecture, not a product category. A conversational interface may still invoke consequential tools.

## 7. Scaling workflow — Normative

1. **Select:** Apply the [Prioritisation Method](Prioritisation-Method.md) and reject uses with unclear purpose or unacceptable conditions.
2. **Classify:** Assess consequence, data, exposure and action authority.
3. **Design boundaries:** Define tools, permissions, transaction limits, human decisions and fallback.
4. **Reuse safely:** Consume shared identity, policy, tool, evaluation and telemetry services through explicit contracts.
5. **Evaluate:** Test successful, failed, manipulated, interrupted and partially completed trajectories.
6. **Authorise:** Record permitted scope, residual risk and intervention authority.
7. **Operate:** Monitor goals, actions, denials, outcomes, cost and user challenges.
8. **Adapt or withdraw:** Change the system when evidence invalidates assumptions or controls.

## 8. Failure and recovery — Normative

An agent may fail after some tools have succeeded. Architecture shall therefore address idempotency, duplicate action, partial transaction, stale state and compensation. Reconciliation should compare intended actions with authoritative system results. Recovery shall not simply replay a plan when external state may have changed.

For essential processes, provide a non-agentic route or a contained queue that authorised operators can resolve. Fallback must not bypass identity, privacy or safety controls.

## 9. Reader checklist — Normative

- [ ] Scaling is justified by outcomes and reuse, not agent count.
- [ ] Goals, tools, data and transactions are explicitly bounded.
- [ ] Policy enforcement is outside model discretion.
- [ ] Human decisions are placed according to consequence.
- [ ] Evaluation covers trajectories and partial failure.
- [ ] Operators can pause, revoke, reconcile and recover.
- [ ] Shared services preserve use-specific accountability.
- [ ] Cost and supplier dependencies are attributable.
- [ ] Wider authority depends on evidence rather than aspiration.

## Related links

- [WG5 reference set](README.md)
- [Prioritisation Method](Prioritisation-Method.md)
- [TOGAF ADM Phase Mapping](TOGAF-ADM-Phase-Mapping.md)
- [Agentic AI Architecture Guide](../../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)
- [Agentic AI Operating Model](../../11-Architecture-Diagrams/ArchiMate/Agentic-AI-Operating-Model.archimate)

