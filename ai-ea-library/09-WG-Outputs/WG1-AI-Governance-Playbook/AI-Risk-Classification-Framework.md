# AI Risk Classification Framework

| Metadata | Description |
|---|---|
| **Purpose** | Route an AI use case to proportionate governance using repeatable decision logic. |
| **Audience** | Business and system owners, architects, risk teams, data stewards, security and privacy functions, procurement teams and independent reviewers. |
| **Use When** | Proposing an AI use, changing its purpose or operating boundary, adding data or tool permissions, onboarding a supplier or responding to new evidence of harm. |
| **Outputs** | Classification tier, rationale, decisive risk factors, required review depth and reassessment triggers. |
| **Content classification** | Decision rules and required records are **Normative** for adopters. Examples and tailoring notes are **Informative**. |

> **Important:** This framework supports internal triage. It does not determine legal classification, remove the need for specialist assessment or establish that a use is permitted.

## 1. Classification tiers — Normative

| Tier | Meaning | Governance route |
|---|---|---|
| **Restricted** | The intended use conflicts with an applicable prohibition, lacks a defensible purpose, enables unacceptable manipulation or cannot reduce severe harm to an acceptable level. | Do not proceed in the stated form. Remove the restricted condition or obtain an appropriately authorised determination before any use. |
| **Critical** | Failure or misuse could materially affect safety, fundamental rights, access to essential services, employment, legal position or large-scale sensitive information. | Full impact assessment, independent evaluation, relevant control-function review and explicit residual-risk acceptance. |
| **Controlled** | The system influences meaningful decisions, handles confidential data, communicates externally, creates material operational action or has significant scale, but has bounded and reversible consequences. | Documented assessment, full applicable controls, scenario testing and independent challenge of important claims. |
| **Standard** | The use is assistive, bounded, reversible, low sensitivity and does not determine consequential outcomes. | Core controls, fit-for-purpose evaluation, accountable owner and a feedback and correction route. |

Classification sets a minimum governance route. Applicable law, contract, sector policy or enterprise risk appetite may require stronger treatment.

## 2. Information required — Normative

The classifier shall not rely on the label “copilot”, “assistant” or “automation”. Record:

- intended and excluded purposes;
- users and people affected by outputs or actions;
- consequence if the system is wrong, unavailable, manipulated or misunderstood;
- degree of human review and the reviewer’s real authority;
- personal, confidential, regulated or safety-relevant data involved;
- external communication, content generation or decision influence;
- tools, transactions, physical actions and permissions available;
- reach, repetition and whether effects can be reversed;
- model, supplier and downstream dependencies; and
- known uncertainty, novelty and evidence gaps.

Unknown information is itself a risk factor. It should not be treated as a favourable answer.

## 3. Decision logic — Normative

Apply the rules in order and stop at the highest applicable tier.

### Gate A — Restricted condition

Classify as **Restricted** if any of the following is true:

- the use is prohibited by an applicable rule or binding organisational policy;
- the purpose depends on deception, coercion, unlawful discrimination or exploitation;
- required rights to use the data, model or output cannot be established;
- severe harm cannot be bounded, detected or meaningfully remediated; or
- no accountable person has authority to accept the residual risk.

### Gate B — Critical consequence

Classify as **Critical** if the system determines or materially shapes:

- diagnosis, treatment, physical safety or operation of critical infrastructure;
- employment, education, insurance, credit, housing, justice or essential public services;
- legal rights or similarly consequential eligibility;
- biometric identification, surveillance or inference about sensitive traits;
- autonomous high-value transactions or irreversible physical or digital actions; or
- processing whose breach or corruption could affect many people or expose highly sensitive data.

Nominal human review does not reduce the tier when reviewers lack time, information, competence or authority to disagree.

### Gate C — Controlled exposure

Classify as **Controlled** if any of these applies:

- confidential or personal data is processed beyond a tightly bounded low-impact task;
- outputs are sent to customers, citizens, suppliers or the public;
- the system recommends decisions with meaningful financial, contractual or operational effect;
- tools can write data, change configurations, initiate communications or create commitments;
- errors may propagate across connected processes; or
- evaluation evidence is limited for the operating context.

### Gate D — Standard use

Classify as **Standard** only when all are true:

- use is assistive and the user remains the effective decision-maker;
- data sensitivity and permissions are low and controlled;
- outputs are readily checked before use;
- errors are reversible with limited effect;
- access and reach are bounded; and
- core governance controls can detect and correct misuse.

## 4. Risk factor worksheet — Normative

| Factor | Low | Elevated | High | Evidence |
|---|---|---|---|---|
| Consequence | Minor, reversible inconvenience | Material operational or financial effect | Safety, rights or essential-service effect | |
| Human oversight | Informed review before use | Sampling or pressured review | No effective intervention | |
| Data | Public or non-sensitive | Confidential or personal | Highly sensitive or large-scale | |
| Autonomy | Read-only suggestion | Bounded write action | Broad or irreversible action | |
| Exposure | Small internal group | Broad internal or limited external | Public or population-scale | |
| Explainability need | Output easily checked | Rationale needed for decision | Outcome must support formal challenge | |
| Security misuse | Limited capability | Valuable data or tools | Privileged tools or safety impact | |
| Evidence | Established tests in context | Some gaps or novel conditions | Material unknowns | |

The worksheet informs judgement; it is not an arithmetic score. A single high-consequence factor can determine the tier.

## 5. Classification workflow — Normative

1. **Describe** the use in operational terms, including excluded uses.
2. **Collect** evidence for every factor and mark unknowns.
3. **Apply** Gates A to D in order.
4. **Challenge** assumptions with data, security, domain and affected-person perspectives.
5. **Record** the tier, decisive factors, dissent and unresolved uncertainty.
6. **Route** the system to the controls and decision authority required by the [AI Governance Playbook](AI-Governance-Playbook.md).
7. **Reassess** when a recorded trigger occurs.

Required triggers include a new purpose, user group, model, data category, tool permission, deployment channel, supplier condition, material incident or evidence that expected safeguards are ineffective.

## 6. Worked examples — Informative

| Use | Likely tier | Reasoning |
|---|---|---|
| Drafting internal meeting summaries from non-sensitive notes, with user review | Standard | Assistive, reversible and readily checked |
| Customer-service assistant using account data and sending externally reviewed replies | Controlled | Personal data and external communication require stronger controls |
| Ranking applicants for employment decisions | Critical | Material influence over a consequential opportunity |
| Agent with unrestricted payment and identity-system access | Critical, or Restricted until bounded | Privileged autonomous action can create severe and difficult-to-reverse harm |

These examples are not universal determinations. Changed data, permissions, users or legal context can change the result.

## 7. Reviewer checklist — Normative

- [ ] The real workflow, not the product label, was classified.
- [ ] Indirectly affected people and downstream uses were considered.
- [ ] Human oversight was tested for effectiveness.
- [ ] Unknowns were recorded rather than scored as low risk.
- [ ] The highest applicable gate determined the result.
- [ ] The rationale and dissent can be understood by an independent reader.
- [ ] Reassessment triggers are specific to meaningful change or evidence.
- [ ] Legal classification, where relevant, is performed separately by competent advisers.

## Related links

- [WG1 reference set](README.md)
- [AI Governance Playbook](AI-Governance-Playbook.md)
- [Governance Control Library](Governance-Control-Library.md)
- [AI Architecture Review Checklist](../../07-Toolkits-and-Playbooks/09-AI-Architecture-Review-Checklist.md)
