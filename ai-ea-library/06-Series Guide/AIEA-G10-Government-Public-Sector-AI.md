# AIEA Series Guide
## AIEA-G10: Government & Public Sector AI
### Document Number: AIEA-G10 | Version 1.0 | 2026

| Metadata | Detail |
|---|---|
| Document type | Independent sector reference guide |
| Audience | Public-sector enterprise and solution architects, service owners, policy and programme teams, procurement specialists, records officers, accessibility specialists, data and AI teams, legal advisers, auditors, and oversight functions |
| Use when | Exploring, procuring, designing, approving, operating, or reviewing AI used in public administration or public-service delivery |
| Scope | Citizen-facing and internal services, decision support, casework, document processing, regulatory analytics, and planning across Indian and global public-sector contexts |
| Last verified | October 2026 |
| Standing | Independent guidance, not law, legal advice, procurement authority, certification, or a declaration of compliance |

---

## Preface

This document is an independent AIEA Series Guide supplementing the core AIEA Reference Framework. It provides architectural patterns, governance controls, and reference use cases for applying AI in **government and public-sector** contexts — central and state departments, public-service delivery, regulators, and public-sector undertakings.

Public-sector AI carries heightened obligations: decisions affect citizens' rights and access to services; transparency and fairness are not optional; and sovereignty and inclusion requirements are often stricter than in the private sector. India's IndiaAI Mission is government-led, making public-sector architecture a first-class concern.

This guide is intended for Enterprise Architects and AI Governance Leads in public-sector programmes. It extends [AIEA-101](../05-Standards/AIEA-101-Introduction-Core-Concepts.md), and complements [AIEA-G03: Indian Enterprises](AIEA-G03-Indian-Enterprises.md) and [AIEA-G06: Sovereign AI](AIEA-G06-Sovereign-AI.md).

---

## Chapter 1: The Public-Sector Context

### 1.1 What Makes Public-Sector AI Different

| Dimension | Public-Sector Implication |
|---|---|
| Accountability | Decisions may be subject to public scrutiny, information-access law, administrative review, audit, or judicial review according to jurisdiction |
| Fairness & inclusion | Must work across languages, literacy levels, and access conditions |
| Transparency | Consequential processes need understandable notice and reasons consistent with applicable law and procedure |
| Sovereignty | Data location, control, and infrastructure requirements may be set by law, policy, classification, or procurement |
| Procurement | Transparent, auditable procurement; vendor lock-in is a public risk |
| Scale & continuity | Population-scale systems with long operational lifetimes |

### 1.2 Service Archetypes

- **Citizen-facing assistance:** multilingual information and grievance assistants.
- **Eligibility and benefits:** decision support for scheme eligibility.
- **Document and case processing:** extraction, classification, and triage.
- **Regulatory and compliance:** monitoring, detection, and analytics.
- **Policy and planning:** forecasting and simulation for public planning.

### 1.3 Public-Value and Accountability Test

An AI proposal should begin with the public purpose, not the availability of a model. Record:

1. the statutory, policy, or service basis for the activity;
2. the people and groups affected, including those unlikely to use a digital channel;
3. the decision or service step that AI would influence;
4. why a rules-based, process, staffing, or non-AI digital change is insufficient;
5. the expected public value and the harms that could arise;
6. who remains accountable and who can stop the system; and
7. how a person can obtain assistance, correction, review, or an alternative channel.

Do not use AI to obscure a policy choice. If a service rule is contested, incomplete, or discriminatory, automating it can scale the problem. Policy ownership, service design, data stewardship, and technical delivery therefore remain separate but jointly accountable disciplines.

---

## Chapter 2: Reference Architecture

### 2.1 Sovereignty-First Design

Public-sector AI should default to sovereign or clearly governed infrastructure (see [AIEA-G06](AIEA-G06-Sovereign-AI.md)). The [AI Gateway](../11-Architecture-Diagrams/README.md) pattern (Principle D1) is essential to preserve the ability to substitute models and providers over long programme lifetimes.

### 2.2 Inclusion by Design

| Requirement | Architectural Response |
|---|---|
| Multilingual access | Language support and evaluation across relevant languages |
| Low-literacy / assisted access | Voice and assisted-interaction channels |
| Offline / low-connectivity | Edge and asynchronous patterns where connectivity is limited |
| Accessibility | Standards-compliant interfaces |

### 2.3 Architecture Views

#### Service and accountability view

Map the resident, business, caseworker, authorised decision-maker, service owner, records authority, grievance or appeal function, supplier, and oversight body. Show where notice is given, where human judgement occurs, and where a non-digital or assisted route remains available. An AI component is never the accountable decision-maker.

#### Decision view

For every consequential workflow, document:

```
application/evidence -> validation -> policy or legal rules -> AI assistance
                     -> authorised human decision -> reasons and notice
                     -> correction/reconsideration/appeal -> outcome and learning
```

Separate deterministic eligibility rules from probabilistic ranking, extraction, prediction, or generation. Record which inputs are legally or procedurally relevant, how missing or disputed data is handled, what the model may recommend, and what it cannot decide. A human checkpoint is not meaningful if staff are expected to accept outputs routinely or lack time and authority to disagree.

#### Data and records view

Identify the source and lawful authority for each dataset; purpose; data quality; classification; sharing; retention; correction route; provenance; and whether the data represents people unevenly. Keep operational observability distinct from indiscriminate surveillance. Logs should be sufficient to reconstruct a material action without collecting excessive personal data.

For a consequential interaction, the record may need the request or case identifier, material source data, model and configuration version, retrieved evidence, output, confidence or uncertainty where meaningful, human action, reason, notices issued, and later correction or appeal. Apply the relevant records schedule rather than allowing a vendor's default retention to decide public-record lifecycle.

#### Deployment and supply-chain view

Show model hosting, data stores, integration services, identity, encryption and key control, administrative access, support locations, subprocessors, telemetry destinations, model-update path, content-safety services, and exit route. Define degraded operation if a supplier, network, language service, or model is unavailable. Portability includes prompts, evaluation sets, indexes, embeddings where transferable, records, configuration, and documentation, not only application source code.

### 2.4 Inclusion and Accessibility by Design

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) is an authoritative web accessibility recommendation organised around perceivable, operable, understandable, and robust content. Indian government digital teams should also assess the [Guidelines for Indian Government Websites and Apps (GIGW)](https://guidelines.india.gov.in/) and applicable requirements under the [Rights of Persons with Disabilities Act, 2016](https://www.indiacode.nic.in/handle/123456789/2155). Applicability and conformance must be established for the specific service.

Accessibility is broader than a compliant front end. Test generated text with screen readers and magnification; keyboard-only operation; focus order; captions and transcripts; speech recognition across accents; text-to-speech pronunciation; colour and contrast; cognitive load; plain language; error recovery; and time limits. Do not make a chatbot the only route to a service. Preserve human, telephone, in-person, assisted-digital, and paper channels where needed.

Inclusion evaluation should cover supported languages and scripts, code-switching, regional vocabulary, literacy, disability, device capability, connectivity, and the availability of identity or documentary evidence. Translate source content before promising multilingual service quality. Machine translation confidence alone is not evidence that legal, benefits, health, or grievance content is correct.

---

## Chapter 3: Governance

### 3.1 Decisions Affecting Rights Are High-Risk

Within this guide's independent risk taxonomy, any AI output that can materially affect a person's access to a service, benefit, duty, sanction, liberty, or right is treated as **High-Risk** and requires:

| Control | Requirement |
|---|---|
| Human accountability (G1) | A named public-service owner accountable for outcomes |
| Explainability (G3) | Citizen-understandable explanation of consequential decisions |
| Appeal route | A human appeal / review channel for adverse decisions |
| Fairness evaluation | Tested across demographic and linguistic groups |
| Auditability | Full decision logs retained for audit and oversight |

### 3.2 Transparency and Public Trust

- Publish the purpose and limits of citizen-facing AI systems.
- Disclose AI involvement in interactions and content.
- Maintain a public register of significant AI systems where appropriate.

### 3.3 Regulatory Alignment

Use the [AIEA-CW01 Compliance Workbook](../05-Standards/AIEA-CW01-Compliance-Workbook.md) for DPDPA and cross-framework obligations. Public bodies should pay particular attention to the applicable basis and purpose for processing, notice, data-principal rights, safeguards, and grievance mechanisms at population scale; consent is not the only question and should not be assumed to be the applicable basis.

### 3.4 India and Global Considerations

For India, assess the current text, commencement position, rules, notifications, and applicability of the [Digital Personal Data Protection Act, 2023](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023). The Act addresses digital personal data, obligations of data fiduciaries, rights and duties of data principals, children's data, and specified processing by the State. Architecture and operating procedures should reflect the actual provision and rule that applies rather than a generic “DPDPA compliant” label.

Where relevant, also map the [Right to Information Act, 2005](https://www.indiacode.nic.in/handle/123456789/2065), the [Public Records Act, 1993](https://www.indiacode.nic.in/indiacode/handle/123456789/1921?view_type=search&sam_handle=123456789/1362), sector rules, administrative law, constitutional duties, security classification, and departmental records schedules. Information access, privacy, confidentiality, privilege, national security, and records preservation can pull in different directions; authorised legal and records functions should resolve them.

For programmes with global reach or comparative obligations, useful primary anchors include the [OECD AI Principles](https://oecd.ai/en/ai-principles), the [UNESCO Recommendation on the Ethics of Artificial Intelligence](https://unesdoc.unesco.org/ark:/48223/pf0000381137), and the [EU Artificial Intelligence Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng). These sources have different legal status and territorial reach. A control crosswalk is useful, but one framework's label does not establish compliance with another.

### 3.5 Public Accountability and Contestability

For significant systems, maintain a proportionate public-facing description of purpose, responsible body, categories of data, role of AI, principal limitations, groups affected, human involvement, contact route, and review or complaint route. Withhold security-sensitive or protected detail only under an applicable basis; do not use security as a blanket reason to omit service-level accountability.

A workable appeal or reconsideration route should:

- be visible at the point a person receives an adverse or materially different outcome;
- accept accessible submissions in relevant channels and languages;
- pause or mitigate harm where procedure allows;
- reach a person with authority to change the outcome;
- provide the reviewer with original evidence, AI contribution, rules, and subsequent corrections;
- avoid asking the same model merely to validate its own output; and
- record disposition and feed systemic errors into service correction.

The route may be called an appeal, grievance, reconsideration, correction, complaint, or review depending on the governing regime. The architecture should reflect the legally correct mechanism.

### 3.6 Procurement and Contract Controls

Apply the procurement rules that govern the body and expenditure. In India, relevant anchors may include the Ministry of Finance [General Financial Rules, 2017](https://doe.gov.in/en/general-financial-rules-2017-updated-upto-31st-january-2026), associated procurement manuals, and the [Government e-Marketplace](https://gem.gov.in/). These sources do not make every AI purchase identical; the procuring authority should select the applicable route.

Procurement should define outcomes and assurance evidence rather than naming a fashionable model. Include:

| Contract area | Minimum question |
|---|---|
| Purpose and performance | Which tasks, populations, languages, operating conditions, baselines, acceptance tests, and prohibited uses are in scope? |
| Data | Who may access data, where is it processed, is it used for provider training, what are retention/deletion terms, and how are rights requests supported? |
| Model change | How are model, safety-policy, dependency, or subprocessor changes notified, evaluated, accepted, or rejected? |
| Security | What secure-development, access, vulnerability, incident, assurance, and remote-support evidence is available? |
| Transparency | What documentation, limitations, evaluation results, logs, and explanation support will the authority receive? |
| Accessibility and inclusion | Which standards, languages, assistive technologies, user research, and remediation duties are acceptance criteria? |
| Records and audit | Can required records be exported in usable form and retained independently of the supplier? |
| Intellectual property | What are the rights and restrictions for inputs, outputs, prompts, fine-tunes, indexes, and generated material? |
| Continuity and exit | How will service degrade safely, data be returned/deleted, interfaces be transferred, and another provider be substituted? |
| Accountability | Who bears which operational duties, and what remedies apply when requirements are not met? |

Avoid evaluations based only on a scripted demonstration. Use representative, protected test cases; include failure and refusal scenarios; separate supplier claims from authority-run acceptance; and preserve sufficient artefacts for audit and later challenge.

---

## Chapter 4: Reference Use Cases

| Use Case | Pattern | Risk Tier |
|---|---|---|
| Multilingual citizen grievance assistant | RAG over policy + routing | Limited |
| Scheme eligibility decision support | ML/LLM support + human decision + appeal | High |
| Public document processing | Extraction + classification + human review | Limited/High |
| Regulatory anomaly detection | ML detection + investigator review | High |
| Public planning forecasting | Forecasting models, advisory | Limited |

### 4.1 Implementation Patterns

**Multilingual citizen assistant.** Retrieve only from approved, dated service content; display citations; distinguish general information from case-specific advice; refuse when policy sources conflict; and hand off with conversation context. Redact unnecessary personal data before model calls. Evaluate every supported language independently.

**Eligibility decision support.** Encode authoritative rules separately from AI. Use AI, if justified, for extraction, completeness checks, or decision support, not as an unreviewable policy engine. Present source evidence and uncertainty to the decision-maker. Generate a reasons record from verified rules and facts, not from free-form model reasoning. Preserve correction and review.

**Document and case processing.** Use confidence-aware extraction, schema validation, duplicate detection, and sampled human quality assurance. Never treat unreadable or unsupported documents as negative evidence. Keep the original record and extraction provenance.

**Regulatory anomaly detection.** Use risk signals to prioritise lawful review, not to presume wrongdoing. Assess feedback loops, selective labels, proxies, and disproportionate investigation. Investigators record an independent basis for action.

**Policy and planning forecasting.** Publish assumptions, uncertainty, scenarios, known omissions, and sensitivity where appropriate. Keep forecasts distinct from policy decisions. Monitor whether the model's data-generating conditions still hold.

---

## Chapter 5: Adoption Roadmap

1. **Inform:** citizen information assistants (low risk, high reach).
2. **Assist:** case and document processing with human review.
3. **Decide-support:** eligibility and regulatory support with mandatory appeal routes.
4. **Scale:** population-scale rollout only after fairness, inclusion, and sovereignty are proven.

Treat these as evidence gates. Begin with a service and affected-community assessment, establish a non-AI baseline, and create an evaluation set reflecting languages, accessibility needs, common cases, edge cases, and foreseeable misuse. Pilot in parallel with the existing route; do not quietly remove the alternative channel. Expansion requires service-owner acceptance, accessibility evidence, security and privacy review, operational readiness, records capability, support training, and a rehearsed withdrawal plan.

Front-line staff, specialists, affected communities, civil society, and oversight functions can reveal failures that model tests miss. Participation must not expose testers to adverse decisions.

---

## Chapter 6: Failure Modes and Evaluation

### 6.1 Common Failure Modes

| Failure mode | Public consequence | Control response |
|---|---|---|
| Hallucinated policy or deadline | Lost service, incorrect action, or mistrust | Approved retrieval, citations, expiry checks, refusal and human hand-off |
| Proxy discrimination | Unequal prioritisation or outcome | Feature review, group and intersectional evaluation, alternative design, independent challenge |
| Language-quality gap | Exclusion or materially different advice | Per-language acceptance, human linguistic review, supported-language disclosure |
| Digital-only design | Excludes people without devices, connectivity, literacy, identity evidence, or ability | Equivalent assisted and non-digital routes |
| Automation bias | Nominal human review becomes rubber-stamping | Authority and time to disagree, reasons capture, sampling, reviewer calibration |
| Inaccessible output | Disabled users cannot complete or understand service | WCAG/GIGW testing, assistive-technology and user testing, remediation gate |
| Record loss or opaque version change | Decision cannot be reconstructed or challenged | Authority-controlled records, version capture, change notice, export and retention |
| Appeal loop | Complaint is assessed by the same flawed automation | Independent human review with power to remedy and systemic escalation |
| Vendor lock-in | Service or evidence cannot be moved | Open interfaces, export tests, substitution design, exit rehearsal |
| Excessive logging | Privacy or security harm | Purpose limitation, minimisation, access control, retention schedule, protected audit |

### 6.2 Evaluation Metrics

Set baselines and acceptance thresholds for the service and risk; no universal target is asserted here.

- **Service:** completion, abandonment, repeat contact, hand-off success, waiting burden, unresolved cases, and performance relative to the non-AI route.
- **Decision quality:** extraction error, false positive/negative rates where valid, disagreement with authorised reviewers, reason accuracy, correction rate, appeal rate, appeal disposition, and material error severity.
- **Fairness and inclusion:** outcome and error differences across legally and contextually appropriate groups, languages, regions, disability needs, channel, device, and intersectional cohorts; sample adequacy must accompany each result.
- **Accessibility:** automated findings plus manual and assistive-technology findings, task completion by disabled users, keyboard and screen-reader defects, caption or transcript coverage, and remediation closure.
- **Information quality:** citation correctness, grounded-answer rate, policy-source freshness, unsupported-claim rate, refusal quality, and translation adequacy.
- **Operations:** availability by channel, latency, stale-output rate, human hand-off time, model/configuration change incidents, security events, records completeness, and withdrawal recovery.
- **Accountability:** notice delivery, review-route visibility, time and steps required to seek correction, reviewer independence, records supplied for challenge, and recurrence of systemic issues.

Disclose results as accountability, security, privacy, and procurement permit. Use disaggregated evidence and qualitative research; accuracy alone cannot establish public acceptability.

---

## Chapter 7: References

The following sources were checked in October 2026. Confirm current text, commencement, amendment, local implementation, and programme applicability:

- [Digital Personal Data Protection Act, 2023 — Ministry of Electronics and Information Technology](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023)
- [Ministry of Electronics and Information Technology — Data Protection Framework](https://www.meity.gov.in/data-protection-framework)
- [Right to Information Act, 2005 — India Code](https://www.indiacode.nic.in/handle/123456789/2065)
- [Public Records Act, 1993 — India Code](https://www.indiacode.nic.in/indiacode/handle/123456789/1921?view_type=search&sam_handle=123456789/1362)
- [Rights of Persons with Disabilities Act, 2016 — India Code](https://www.indiacode.nic.in/handle/123456789/2155)
- [General Financial Rules, 2017 — Department of Expenditure](https://doe.gov.in/en/general-financial-rules-2017-updated-upto-31st-january-2026)
- [Guidelines for Indian Government Websites and Apps](https://guidelines.india.gov.in/)
- [Web Content Accessibility Guidelines 2.2 — W3C](https://www.w3.org/TR/WCAG22/)
- [Convention on the Rights of Persons with Disabilities — United Nations](https://www.ohchr.org/en/instruments-mechanisms/instruments/convention-rights-persons-disabilities)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [UNESCO Recommendation on the Ethics of Artificial Intelligence](https://unesdoc.unesco.org/ark:/48223/pf0000381137)
- [Regulation (EU) 2024/1689, the EU Artificial Intelligence Act — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)

---

*AIEA Series Guide AIEA-G10: Government & Public Sector AI. Version 1.0, 2026.*
