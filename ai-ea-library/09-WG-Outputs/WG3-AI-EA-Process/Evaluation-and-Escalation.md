# Evaluation and Escalation for AI-Assisted Architecture Work

| Metadata | Description |
|---|---|
| **Purpose** | Provide repeatable criteria for accepting, correcting, rejecting or escalating AI-produced architecture work. |
| **Audience** | Architects, architecture reviewers, repository owners, domain specialists, security and privacy functions and governance decision-makers. |
| **Use When** | Reviewing AI-assisted analysis or artefacts, handling conflicting evidence, responding to sensitive output or deciding whether a fallback is required. |
| **Outputs** | Evaluation record, disposition, corrected artefact, escalation packet and learning for prompts or controls. |
| **Content classification** | Acceptance, rejection and escalation rules are **Normative** for adopters. Examples and optional scoring are **Informative**. |

## 1. Evaluation rule — Normative

AI output shall be treated as an unverified draft until a competent reviewer accepts it. Evaluation must reflect the consequence of use: a wording suggestion can receive light review; a dependency claim supporting a major decision requires authoritative verification.

## 2. Quality dimensions — Normative

| Dimension | Review question | Evidence |
|---|---|---|
| Factual fidelity | Does each material claim match an authoritative source? | Citation sampling and source comparison |
| Completeness | Are required domains, affected groups and known constraints represented? | Checklist and source coverage |
| Coherence | Do entities, relationships and views agree with each other? | Metamodel and cross-view checks |
| Relevance | Does the output answer the stated architecture decision? | Decision-to-output trace |
| Uncertainty | Are gaps, assumptions and conflicts explicit? | Open-question and assumption sections |
| Fairness and inclusion | Are materially affected perspectives or uneven effects omitted? | Stakeholder and impact review |
| Security and privacy | Does the output expose data or recommend unsafe boundaries? | Information-handling and threat review |
| Operability | Are ownership, monitoring, failure and recovery addressed? | Operating-model and runbook review |
| Reversibility | Can the proposed choice be changed or withdrawn? | Dependency and exit analysis |
| Usability | Can the intended reader understand and act on it? | Peer review against output purpose |

## 3. Critical rejection conditions — Normative

Reject the output rather than editing around it when it:

- invents a material system, requirement, obligation, measure or source;
- exposes information beyond the authorised boundary;
- silently changes the meaning of an approved policy or decision;
- recommends bypassing required professional, safety or governance authority;
- conceals conflicting evidence that could alter the decision;
- produces code, commands or tool actions outside the approved task; or
- cannot be traced sufficiently for its intended consequence.

Rejection does not necessarily prohibit all AI assistance. It means the output cannot support the decision in its present form.

## 4. Evaluation procedure — Normative

1. **Confirm context:** Verify task, audience, sources, service and consequence.
2. **Check structure:** Ensure all requested sections and evidence fields exist.
3. **Sample claims:** Verify every critical claim and a risk-based sample of remaining claims.
4. **Cross-check views:** Compare business, data, application, technology, security and operational implications.
5. **Challenge omissions:** Ask what evidence or affected perspective is absent.
6. **Test use:** Determine whether a reader could make an unsafe inference from the presentation.
7. **Record disposition:** Accept, accept after correction, reject or escalate.
8. **Update safeguards:** Improve the prompt, source set, evaluation case or process when a repeatable weakness appears.

## 5. Optional rating scale — Informative

| Rating | Meaning |
|---|---|
| 0 — Unsupported | No adequate evidence or a critical rejection condition |
| 1 — Weak | Material gaps require reconstruction |
| 2 — Usable with correction | Core structure is useful but identified issues must be corrected |
| 3 — Accepted | Evidence and review are sufficient for the stated use |

Do not average away a zero in factual fidelity, security, privacy or decision authority. The disposition follows the most consequential weakness, not the mean.

## 6. Escalation routes — Normative

| Trigger | Immediate action | Escalate to | Required packet |
|---|---|---|---|
| Source conflict affecting a decision | Pause reliance and preserve both sources | Source owners and accountable architect | Conflicting extracts, provenance and decision impact |
| Possible legal or regulatory interpretation | Mark as unresolved; do not represent as advice | Qualified legal or compliance function | Question, jurisdiction, facts and cited source |
| Sensitive-data exposure | Stop further sharing and contain access | Privacy, security and data owner | Data involved, recipients, service, containment evidence |
| Safety or rights concern | Stop the affected use where authorised | Accountable owner and relevant domain authority | Scenario, affected people, evidence and interim control |
| Architecture decision beyond delegated authority | Withhold recommendation | Architecture decision body or authorised executive | Options, trade-offs, evidence and dissent |
| Repeated unreliable output | Withdraw the workflow | Service owner, platform and governance functions | Failure samples, model or service version and controls tried |
| Supplier behaviour change | Isolate affected reliance where feasible | Procurement, service owner and architecture | Change evidence, dependencies and exit options |

## 7. Fallback patterns — Normative

| Failure | Fallback |
|---|---|
| Source retrieval fails | Use the authoritative repository directly and record unavailable automation |
| Output cannot cite evidence | Return to manual extraction or a deterministic query |
| Comparison is biased by missing data | Defer ranking and request the missing evidence |
| Confidentiality boundary is uncertain | Use an approved local process or remove sensitive content |
| Model service is unavailable | Use the documented manual procedure; do not bypass policy through an unapproved service |
| Repository change is ambiguous | Create a review queue; do not automate merge or deletion |
| Domain interpretation is disputed | Present alternatives and route to the authorised specialist |

Fallback shall preserve the essential business or architecture decision without silently reducing control.

## 8. Escalation packet template — Normative

| Field | Content |
|---|---|
| Architecture decision | Decision affected and consequence |
| AI-assisted task | Prompt purpose, service and output version |
| Evidence | Sources and relevant extracts |
| Trigger | Observed condition and how it was detected |
| Containment | Action already taken |
| Uncertainty | Facts not yet established |
| Options | Safe alternatives and trade-offs |
| Authority needed | Specific decision or specialist interpretation required |

## 9. Reviewer checklist — Normative

- [ ] Review depth matches the consequence of use.
- [ ] Critical claims were checked against authoritative evidence.
- [ ] A critical rejection condition was not averaged away.
- [ ] Corrections do not conceal the original failure pattern.
- [ ] Escalation goes to a role with actual authority or expertise.
- [ ] The fallback maintains confidentiality and essential control.
- [ ] The final disposition and rationale are recorded.
- [ ] Repeated failures improve prompts, sources, tests or service choice.

## Related links

- [WG3 reference set](README.md)
- [AI in the EA Lifecycle Playbook](AI-in-EA-Lifecycle-Playbook.md)
- [Reusable Prompt and Workflow Library](Reusable-Prompt-and-Workflow-Library.md)
- [AI Architecture Review Checklist](../../07-Toolkits-and-Playbooks/09-AI-Architecture-Review-Checklist.md)

