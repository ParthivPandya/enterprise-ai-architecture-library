# Agentic AI Prioritisation Method

| Metadata | Description |
|---|---|
| **Purpose** | Compare agentic AI use cases using value, feasibility, risk, reuse and operational evidence without rewarding autonomy for its own sake. |
| **Audience** | Portfolio decision-makers, business owners, enterprise architects, product leaders, governance functions, platform teams and finance partners. |
| **Use When** | Selecting use cases, comparing agentic and non-agentic alternatives or deciding whether to increase a system’s reach or action authority. |
| **Outputs** | Eligibility decision, evidence-based scorecard, sensitivity view, authority recommendation and documented portfolio decision. |
| **Content classification** | Eligibility gates and decision rules are **Normative** for adopters. Criteria examples and sector indicators are **Informative**. |

## 1. Eligibility gates — Normative

A use case shall not enter comparative scoring unless all gates pass.

| Gate | Pass condition |
|---|---|
| Purpose | The organisational outcome, affected people and accountable owner are clear |
| Necessity | An agentic pattern offers a plausible advantage over rules, workflow, search or conventional automation |
| Authority | Permitted data, tools, transactions and human decisions can be bounded |
| Acceptability | No known prohibited or unacceptable condition remains |
| Evidence | The problem, baseline and principal assumptions have identifiable evidence |
| Operability | A safe fallback, intervention owner and authoritative system of record exist |

A failed gate results in **Do not proceed in the stated form** or **Return for evidence and redesign**, not a low score hidden in an average.

## 2. Scoring scale — Normative

Score each criterion from 0 to 3.

| Score | Meaning |
|---:|---|
| 0 | Unsupported or materially adverse |
| 1 | Weak evidence or substantial unresolved constraint |
| 2 | Credible evidence with manageable limitations |
| 3 | Strong, relevant evidence across the proposed scope |

Every score shall cite evidence and uncertainty. Organisations may apply weights that reflect their risk appetite and strategy, but shall document them before comparing uses.

## 3. Criteria — Normative

| ID | Criterion | Evidence question | Direction |
|---|---|---|---|
| V1 | Outcome value | Is there a material, attributable workflow or service outcome? | Higher is favourable |
| V2 | Agentic advantage | Does dynamic planning or tool choice add value over simpler approaches? | Higher is favourable |
| F1 | Process readiness | Are rules, exceptions, owners and systems sufficiently understood? | Higher is favourable |
| F2 | Data and tool readiness | Are data, APIs, permissions and authoritative records fit for use? | Higher is favourable |
| F3 | Evaluation feasibility | Can representative trajectories and outcomes be tested? | Higher is favourable |
| R1 | Consequence exposure | Could failure materially affect safety, rights, money, service or trust? | Higher means greater concern |
| R2 | Autonomy exposure | Are actions broad, difficult to reverse or able to expand? | Higher means greater concern |
| R3 | Uncertainty | Are environment, model behaviour or requirements poorly understood? | Higher means greater concern |
| S1 | Reuse potential | Can governed components support other justified uses? | Higher is favourable |
| O1 | Operational fit | Are monitoring, intervention, fallback and support practical? | Higher is favourable |
| E1 | Economic evidence | Are full costs and outcome evidence credible enough for comparison? | Higher is favourable |

Keep favourable and concern scores separate; do not subtract risk into invisibility.

## 4. Decision view — Normative

Calculate two transparent summaries if a compact comparison is needed:

```text
Enablement score = weighted mean of V1, V2, F1, F2, F3, S1, O1 and E1
Exposure score   = weighted mean of R1, R2 and R3
```

Because the scale is ordinal, use the summaries only to organise discussion. Retain each criterion and evidence. The portfolio decision shall consider:

| Enablement | Exposure | Typical disposition |
|---|---|---|
| Strong | Lower | Candidate for bounded implementation |
| Strong | Higher | Consider only with stronger authority limits and independent review |
| Weak | Lower | Prefer simpler alternatives or focused discovery |
| Weak | Higher | Do not proceed in the stated form |

No numeric boundary is universal. Define local boundaries before scoring and validate them against organisational risk appetite.

## 5. Authority recommendation — Normative

Prioritisation shall recommend an authority pattern separately from business priority.

| Pattern | Agent may | Human role |
|---|---|---|
| Read and propose | Retrieve, analyse and draft | Verify before use |
| Prepare action | Create a staged transaction | Confirm or reject |
| Execute bounded action | Invoke narrow, reversible tools within limits | Monitor and handle exceptions |
| Co-ordinate workflow | Route tasks and request decisions | Make consequential decisions |

Do not infer that a highly valuable use warrants broader autonomy.

## 6. Sector indicator menu — Informative

Select only indicators that relate to the actual outcome. Define each measure and source before use.

| Context | Outcome indicators | Quality and risk guardrails |
|---|---|---|
| Financial services | Correctly completed case, reconciled transaction, avoidable rework | Incorrect decision influence, unauthorised action, complaint, data exposure |
| Health and care | Administrative completion, access to authoritative guidance, service continuity | Safety event, unsupported advice, privacy event, missed escalation |
| Public services | Correct routing, accessible completion, consistent policy explanation | Exclusion, due-process concern, untraceable policy interpretation |
| Manufacturing and utilities | Verified maintenance action, restored service, reduced manual diagnosis | Unsafe command, asset mismatch, uncontained outage, stale telemetry |
| Retail and consumer services | Resolved enquiry, correct fulfilment action, approved product explanation | Misleading claim, inappropriate personalisation, unauthorised refund or change |
| Technology operations | Verified incident triage, approved remediation, recovered service | Privilege escalation, harmful change, duplicate action, incomplete rollback |

These are candidate indicators, not benchmarks or promised results.

## 7. Prioritisation workflow — Normative

1. Define the outcome and compare non-agentic alternatives.
2. Apply every eligibility gate.
3. Gather business, architecture, data, security, operational and financial evidence.
4. Score independently across relevant roles.
5. Reconcile differences by examining evidence, not negotiating a preferred total.
6. Run sensitivity analysis on uncertain scores and optional weights.
7. Select an authority pattern and required control depth.
8. Record **Proceed**, **Redesign**, **Gather evidence** or **Do not proceed in the stated form**.
9. Identify evidence changes that require the decision to be revisited.

## 8. Decision record — Normative

| Field | Content |
|---|---|
| Use case and owner | |
| Outcome and baseline | |
| Non-agentic alternatives | |
| Eligibility gates | |
| Criterion scores and evidence | |
| Sensitivity and dissent | |
| Authority pattern | |
| Required controls and fallback | |
| Decision and rationale | |
| Reconsideration triggers | |

## 9. Quality checklist — Normative

- [ ] Every gate passed before scoring.
- [ ] Agentic advantage was compared with simpler alternatives.
- [ ] Scores cite evidence and uncertainty.
- [ ] Exposure remains visible separately from enablement.
- [ ] Optional weights were set before comparison.
- [ ] Sector indicators are defined locally and are not treated as benchmarks.
- [ ] Authority is no broader than the use requires.
- [ ] The disposition and dissent are recorded.

## Related links

- [WG5 reference set](README.md)
- [Scaling Agentic AI](Scaling-Agentic-AI-White-Paper.md)
- [TOGAF ADM Phase Mapping](TOGAF-ADM-Phase-Mapping.md)
- [Agentic AI Use Cases](../../02-AI-Strategy/02-Agentic-AI-Use-Cases.md)
- [Agentic reference use cases](../../10-Use-Cases-and-Case-Studies/README.md)
