# Multi-Industry Overlays for AI-Assisted Enterprise Architecture

| Metadata | Description |
|---|---|
| **Purpose** | Show how sector context changes evidence, review and control needs when AI assists enterprise architecture work. |
| **Audience** | Enterprise and domain architects, sector specialists, governance reviewers, data and security architects and architecture practice leaders. |
| **Use When** | Tailoring an AI-assisted EA workflow for a regulated, safety-relevant, public-facing or operationally specialised environment. |
| **Outputs** | Sector overlay, additional evidence needs, review participants, prohibited shortcuts and escalation triggers. |
| **Content classification** | Tailoring method and minimum review rules are **Normative** for adopters. Sector examples are **Informative** and require local validation. |

> Sector examples do not interpret law or guarantee regulatory acceptability. Validate obligations, terminology and decision rights for the relevant organisation and jurisdiction.

## 1. Overlay method — Normative

Begin with the baseline controls in the [AI in the EA Lifecycle Playbook](AI-in-EA-Lifecycle-Playbook.md), then answer:

1. Which outcomes can materially affect safety, rights, access, money or public trust?
2. Which records are authoritative, and who may access them?
3. Which decisions require licensed, statutory or formally delegated authority?
4. Which operational failures must remain contained?
5. Which explanations, records or challenge routes must be preserved?
6. Which suppliers, infrastructure or data locations introduce constraints?
7. Which domain specialist must review the architecture artefact?

Record the overlay as additions or stricter interpretations. Do not silently weaken the baseline workflow.

## 2. Cross-sector comparison — Informative

| Sector context | High-value EA assistance | Dominant risks | Evidence emphasis | Required challenge |
|---|---|---|---|---|
| Financial services | Control traceability, application dependency analysis, policy comparison | Unfair decision influence, financial loss, confidentiality, model and supplier concentration | Product rules, data lineage, control operation, transaction boundaries | Risk, compliance, security and accountable product owner |
| Health and care | Care-pathway mapping, interoperability analysis, evidence synthesis | Patient harm, sensitive records, automation bias, unavailable service | Clinical authority, provenance, safety case, human decision boundary | Clinical safety, privacy, security and service operations |
| Public sector | Service journey analysis, policy-to-capability mapping, accessibility review | Exclusion, due-process failure, opaque policy interpretation, loss of public trust | Authoritative policy, equality and accessibility evidence, decision record | Service owner, legal or policy specialist, accessibility and public-interest review |
| Manufacturing and utilities | Asset dependency mapping, maintenance knowledge retrieval, failure-mode analysis | Physical safety, production interruption, stale telemetry, unsafe action | Asset configuration, engineering authority, sensor quality, recovery procedure | Operational technology security, safety engineering and plant operations |
| Retail and consumer services | Customer-journey analysis, catalogue and supply-chain mapping | Misleading content, discrimination, personalisation misuse, supplier data leakage | Product source, consent and preference, content review, fulfilment record | Consumer protection, privacy, brand and service operations |

## 3. Financial services overlay — Informative

### Architecture focus

- Separate advisory assistance from systems that influence eligibility, pricing or transaction approval.
- Trace data from customer and transaction sources through features, retrieval, prompts and outputs.
- Identify concentration risk across model, cloud, data and operational suppliers.
- Preserve a comprehensible human decision and customer challenge route.

### Checklist

- [ ] Product and decision authority is named.
- [ ] Monetary actions require bounded permissions, confirmation and reconciliation.
- [ ] Architecture evidence distinguishes policy text from AI interpretation.
- [ ] Testing examines uneven outcomes across relevant customer groups.
- [ ] Supplier substitution and service outage have controlled alternatives.

## 4. Health and care overlay — Informative

### Architecture focus

- Distinguish administrative support, professional decision support and direct patient interaction.
- Treat clinical guidance, patient records and device data as separate evidence classes.
- Ensure professionals see provenance, uncertainty and missing context.
- Preserve safe operation when AI or connectivity is unavailable.

### Checklist

- [ ] A qualified domain reviewer approves clinical interpretation.
- [ ] Patient data access follows care context and least privilege.
- [ ] Output cannot be mistaken for authority it does not hold.
- [ ] Safety-relevant alerts and omissions are evaluated.
- [ ] The non-AI care or service route remains usable.

## 5. Public-sector overlay — Informative

### Architecture focus

- Map AI assistance to lawful administrative authority and published policy.
- Include people who may face language, accessibility or digital-access barriers.
- Separate explanation support from formal determination.
- Retain evidence needed to understand and challenge a decision.

### Checklist

- [ ] Policy sources are authoritative and their versions are visible.
- [ ] Accessibility and assisted-service routes are included.
- [ ] AI-generated summaries do not silently narrow policy.
- [ ] The accountable official can examine evidence and disagree.
- [ ] Records support review without exposing unnecessary personal data.

## 6. Manufacturing and utilities overlay — Informative

### Architecture focus

- Model the boundary between enterprise IT, operational technology and physical control.
- Use verified asset configuration and maintenance instructions.
- Separate recommendations from executable control commands.
- Design for intermittent connectivity and stale sensor readings.

### Checklist

- [ ] Asset identity and configuration are verified before advice is used.
- [ ] Write actions are isolated, authorised and interruptible.
- [ ] Safety interlocks do not depend solely on probabilistic output.
- [ ] Simulation or controlled testing covers hazardous failure modes.
- [ ] Operators have clear fallback and recovery procedures.

## 7. Retail and consumer overlay — Informative

### Architecture focus

- Preserve product, price, inventory and fulfilment source authority.
- Make personalisation choices understandable and controllable.
- Prevent generated claims from exceeding approved product information.
- Trace third-party content and data through customer interactions.

### Checklist

- [ ] Product statements can be traced to approved sources.
- [ ] Personalisation uses permitted and relevant data.
- [ ] Sensitive inferences are excluded or separately justified.
- [ ] Returns, complaints and correction signals reach architecture review.
- [ ] Supplier content and model changes are observable.

## 8. Overlay record — Normative

| Field | Required content |
|---|---|
| Baseline workflow | Version and applicable controls |
| Sector decision | Domain process and accountable authority |
| Additional evidence | Authoritative records and specialist assessments |
| Stricter controls | Added review, access, evaluation or fallback requirements |
| Excluded shortcut | AI use that would bypass essential professional or public authority |
| Reviewers | Domain and control functions required |
| Escalation trigger | Consequence, uncertainty or conflict requiring higher authority |

## 9. Reader checklist — Normative

- [ ] The overlay adds context without replacing baseline safeguards.
- [ ] Sector terminology and obligations are locally validated.
- [ ] Licensed or delegated decisions remain with authorised people.
- [ ] The evidence set represents the real operating environment.
- [ ] Service accessibility and non-AI routes are considered.
- [ ] Physical, financial, rights and trust impacts are not reduced to model quality.
- [ ] Supplier and cross-border assumptions are explicit.

## Related links

- [WG3 reference set](README.md)
- [AI in the EA Lifecycle Playbook](AI-in-EA-Lifecycle-Playbook.md)
- [Evaluation and Escalation](Evaluation-and-Escalation.md)
- [AI Risk Classification Framework](../WG1-AI-Governance-Playbook/AI-Risk-Classification-Framework.md)

