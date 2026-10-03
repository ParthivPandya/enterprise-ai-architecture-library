# Value Realisation Model

| Metadata | Description |
|---|---|
| **Purpose** | Connect AI architecture choices to observable business outcomes, risk and full operating cost without inventing benefit claims. |
| **Audience** | Business owners, enterprise architects, product leaders, finance partners, risk teams and service owners. |
| **Use When** | Framing an AI use case, comparing solution options, authorising operational use or deciding whether a capability remains worthwhile. |
| **Outputs** | Outcome map, measurement specification, cost model, evidence record and continue, change or stop decision. |
| **Content classification** | Measurement and decision rules are **Normative** for adopters. Example measures and calculations are **Informative**. |

## 1. Value principles — Normative

1. Measure the business decision or workflow, not model activity alone.
2. Separate observed evidence from forecasts and assumptions.
3. Include quality, risk, adoption and operating cost alongside throughput.
4. Compare with a credible baseline or alternative.
5. Avoid monetising benefits that cannot be traced to an evidence source.
6. Do not treat reduced human review as value when it removes an essential control.
7. Revisit the value case when use, model, data, price or operating burden changes materially.

## 2. Outcome map — Normative

Build the value case from top to bottom.

| Level | Question | Example — Informative |
|---|---|---|
| Enterprise outcome | Which organisational result matters? | More reliable customer support |
| Capability outcome | Which capability changes? | Faster access to approved product guidance |
| Workflow outcome | Which decision or activity improves? | Adviser finds and explains the relevant policy |
| Behaviour indicator | What observable behaviour supports the claim? | Correct source used; avoidable hand-off reduced |
| Quality and risk guardrail | What must not deteriorate? | Incorrect advice, complaints, data exposure |
| Evidence source | Where will credible evidence come from? | Case records, reviewed samples, user feedback |

Model latency, token count and benchmark score are diagnostic measures. They become value measures only when a defensible link to the workflow outcome is shown.

## 3. Measurement specification — Normative

For every measure record:

| Field | Required description |
|---|---|
| Name and intent | What the measure reveals and which decision uses it |
| Definition | Numerator, denominator, inclusion and exclusion rules |
| Evidence source | Authoritative system or reviewed observation |
| Baseline or comparator | Existing process, alternative design or controlled comparison |
| Segmentation | User, case, channel or risk groups needed to expose uneven effects |
| Quality rule | Completeness, validity and reconciliation checks |
| Interpretation | What movement may mean and what it cannot establish |
| Decision boundary | Condition that prompts investigation, correction or withdrawal |
| Owner | Person accountable for interpretation and action |

Decision boundaries must be established from organisational risk appetite, service obligations and validated evidence. This library does not supply universal numeric thresholds.

## 4. Balanced KPI tree — Informative

| Branch | Candidate measures |
|---|---|
| Outcome | Successful resolution, avoided rework, decision quality, service accessibility |
| Experience | Task completion, user correction, escalation, reasoned trust and complaints |
| Quality | Groundedness, factual correctness, completeness, consistency and domain review |
| Risk | Harmful output, privacy event, policy breach, security event and control override |
| Operations | Availability, response time, recovery, unsupported request and manual fallback |
| Economics | Cost per completed outcome, review effort, platform cost and supplier cost |
| Adoption | Eligible use, voluntary use, abandonment and use outside the intended purpose |

Select the smallest set that supports a real decision. A large dashboard can obscure weak evidence.

## 5. Full cost model — Normative

Estimate and observe cost across:

- discovery, architecture and impact assessment;
- data preparation, licensing, curation and retrieval;
- model access, hosting, fine-tuning or inference;
- platform, integration, identity, security and observability;
- evaluation data, tooling and specialist review;
- human oversight, exception handling and customer support;
- governance, assurance, supplier management and incident response;
- change, migration, portability and retirement; and
- expected cost of credible failure scenarios where estimation is defensible.

### Useful calculations — Informative

```text
Cost per accepted outcome =
  total attributable operating cost / number of outcomes meeting acceptance rules

Net observable value =
  evidenced benefit - attributable cost - evidenced loss or remediation cost

Adoption-adjusted outcome =
  eligible cases x appropriate-use proportion x accepted-outcome proportion
```

These formulas organise evidence; they do not make uncertain inputs reliable. Report ranges and assumptions where point estimates would imply false precision.

## 6. Evidence workflow — Normative

1. **Frame:** Define outcome, affected groups, decision owner and alternative.
2. **Specify:** Write measures, evidence sources, guardrails and interpretation before relying on results.
3. **Instrument:** Confirm that the workflow can produce attributable and protected evidence.
4. **Compare:** Use a suitable baseline, matched cases or controlled evaluation.
5. **Review:** Examine quality and risk by meaningful segments, not only aggregate results.
6. **Explain:** Distinguish correlation, contribution and causal evidence.
7. **Decide:** Continue, change, constrain or stop the use based on the whole evidence set.
8. **Retain:** Record the evidence version, assumptions, dissent and decision.

## 7. Value decision record — Normative

| Decision question | Record |
|---|---|
| Is the outcome material and attributable? | Evidence and limitations |
| Does quality meet the use requirement? | Evaluation and observed operation |
| Are harms and uneven effects acceptable? | Segmented evidence and control assessment |
| Is the operating burden sustainable? | Full-cost evidence and sensitivity analysis |
| Is AI better than the feasible alternative? | Comparative evidence |
| What change would invalidate the case? | Data, model, price, behaviour or policy trigger |
| Decision | Continue, change, constrain or stop, with rationale |

## 8. Reader checklist — Normative

- [ ] The value case begins with an organisational outcome.
- [ ] Every claimed benefit has an identified evidence source.
- [ ] Forecasts are labelled and assumptions are visible.
- [ ] Quality, harm and cost are considered together.
- [ ] Measures are segmented where aggregate results can conceal impact.
- [ ] Human review and governance effort are included in cost.
- [ ] No legal, financial or performance guarantee is inferred.
- [ ] The decision can change when underlying evidence changes.

## Related links

- [WG2 reference set](README.md)
- [AI-Native Enterprise Architecture](AI-Native-EA-White-Paper.md)
- [AI-Native Reference Architecture](AI-Native-Reference-Architecture.md)
- [Maturity Model and Adoption Roadmap](Maturity-Model-and-Adoption-Roadmap.md)

