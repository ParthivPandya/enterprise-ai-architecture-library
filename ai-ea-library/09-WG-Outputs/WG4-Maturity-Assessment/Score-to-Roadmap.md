# From Score to Roadmap

| Metadata | Description |
|---|---|
| **Purpose** | Convert an AI maturity heatmap into a dependency-ordered set of capability improvements. |
| **Audience** | Enterprise architects, capability owners, organisational sponsors, governance functions, platform leaders and product owners. |
| **Use When** | Interpreting a completed scorecard, choosing improvement actions or checking that a proposed AI use has adequate organisational foundations. |
| **Outputs** | Decision constraints, root causes, prioritised action packages, dependency map, acceptance evidence and accountable owners. |
| **Content classification** | Conversion and prioritisation rules are **Normative** for adopters. Example action patterns are **Informative**. |

> “Roadmap” here means a logical map of capability dependencies and choices. It is not a calendar, delivery report or promise of completion.

## 1. Conversion principles — Normative

1. Begin with the organisational decision, not the weakest colour.
2. Treat scores as evidence summaries, not precise quantities.
3. Address root causes that appear across several statements.
4. Resolve safety, rights, security and accountability constraints before wider autonomy or reach.
5. Prefer actions that demonstrate operation over documents that state intent.
6. Preserve local variation where a common service would be unsuitable.
7. Define acceptance evidence and ownership for every action package.
8. Do not assume that every dimension must reach the maximum level.

## 2. Conversion workflow — Normative

### Step 1: State the intended capability

Describe the decision or capability the organisation wants to support, such as governed internal assistance, trusted enterprise retrieval or bounded workflow action.

### Step 2: Identify essential statements

Mark assessment statements whose capability is necessary for that use. A critical weakness or “Not assessed” result in an essential statement becomes a decision constraint.

### Step 3: Analyse causes

For each constraint, ask why the capability is not evidenced. Distinguish:

- unclear accountability;
- missing or unsuitable process;
- absent information or data stewardship;
- architecture or platform limitation;
- skills and decision-authority gap;
- ineffective control operation; and
- missing evidence despite possible practice.

### Step 4: Group action packages

Combine actions that address the same root cause or reusable capability. Do not create one action per question when a common cause spans several dimensions.

### Step 5: Map dependencies

Order packages by logical prerequisites. For example, an evaluation service depends on use-specific criteria and accountable owners; safe tool automation depends on identity, tool contracts, evaluation and interruption.

### Step 6: Prioritise

Use the matrix below. Record the reasoning rather than relying on an unexplained total.

### Step 7: Define acceptance evidence

State what observable evidence will show that the capability works across the intended scope.

## 3. Prioritisation matrix — Normative

Rate each consideration **Low**, **Medium** or **High** with a rationale.

| Consideration | Question |
|---|---|
| Decision criticality | Does the package remove a constraint on the stated organisational decision? |
| Risk reduction | Does it reduce credible safety, rights, security, privacy or operational harm? |
| Dependency value | Is it a prerequisite for several justified capabilities? |
| Reuse value | Can several teams use it without losing domain fit? |
| Evidence strength | Is the need supported by reliable assessment evidence? |
| Feasibility | Are ownership, authority and prerequisites available? |
| Reversibility | Can the approach change if assumptions prove wrong? |

Decision criticality and risk reduction take precedence over convenience. A package with weak evidence should normally begin with focused discovery rather than broad implementation.

## 4. Action package template — Normative

| Field | Required content |
|---|---|
| Capability outcome | Observable organisational ability, not a tool purchase |
| Related statements | Assessment IDs and evidence |
| Root cause | Reason the capability is weak or unknown |
| Scope | Included units, uses and exclusions |
| Actions | Changes to accountability, process, information and technology |
| Owner | Role with authority to deliver and operate the capability |
| Dependencies | Other packages or decisions required first |
| Acceptance evidence | Records and observed operation that demonstrate the outcome |
| Risks and safeguards | Possible harm from the change and its controls |
| Reconsideration trigger | Evidence or context that would change the approach |

## 5. Common action patterns — Informative

| Observed gap | Weak response | Stronger capability action |
|---|---|---|
| AI estate is unknown | Publish an inventory policy | Define scope and ownership, discover uses, reconcile procurement and technical evidence, sample completeness |
| Classification varies | Add a form | Establish decision logic, train reviewers, reperform samples and capture disagreement |
| Data provenance is weak | Buy a catalogue | Assign stewards, define source contracts, test lineage and connect issues to operating decisions |
| Evaluation is ad hoc | Adopt a generic benchmark | Define use criteria, curate representative cases, version results and investigate failures |
| Tool permissions are broad | Add prompt instructions | Create narrow tool contracts, least-privilege identities, confirmations, limits and stop tests |
| Value is asserted | Add a dashboard | Define outcome, baseline, evidence source, quality guardrails and full-cost decision record |
| Incidents remain local | Request lessons learned | Establish safe reporting, cross-functional review and controlled changes to tests and patterns |

## 6. Dependency patterns — Informative

```text
Accountability and inventory
        -> classification and decision rights
        -> data and architecture boundaries
        -> use-specific evaluation
        -> shared model access and telemetry
        -> bounded action and wider reuse
        -> cross-estate learning
```

This is a reasoning aid, not a universal sequence. An urgent control weakness may require containment before foundational improvement.

## 7. Roadmap view — Normative

| Package | Outcome | Priority rationale | Dependencies | Acceptance evidence | Owner |
|---|---|---|---|---|---|
| | | | | | |

Keep this reference view focused on capability logic. Organisations may govern implementation through their established delivery mechanisms.

## 8. Quality checklist — Normative

- [ ] The roadmap serves a stated organisational decision.
- [ ] Essential gaps and unknowns are visible.
- [ ] Root causes were analysed before actions were chosen.
- [ ] Packages cover people, process, information and technology where relevant.
- [ ] Dependencies explain the order.
- [ ] Acceptance evidence demonstrates operation.
- [ ] Owners have authority for the capability outcome.
- [ ] Actions do not imply certification or guaranteed performance.
- [ ] The roadmap does not use dates or completion tracking.

## Related links

- [WG4 reference set](README.md)
- [Self-Assessment Instrument](Self-Assessment-Instrument.md)
- [Scorecard and Heatmap](Scorecard-and-Heatmap.md)
- [Facilitation Playbook](Facilitation-Playbook.md)
- [Maturity Model and Adoption Roadmap](../WG2-EA-AI-Native/Maturity-Model-and-Adoption-Roadmap.md)
