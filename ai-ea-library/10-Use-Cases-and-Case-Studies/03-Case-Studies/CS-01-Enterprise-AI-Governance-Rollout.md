# CS-01 — Rolling Out AI Governance at Scale

| Field | Value |
|---|---|
| **Document ID** | CS-01 |
| **Type** | Illustrative Worked Example |
| **Evidence status** | Fictional composite; not an observed deployment |
| **Theme** | Enterprise AI governance rollout |
| **Illustrative horizon** | Twelve-month planning sequence |
| **Intended use** | Workshop, control-design and roadmap discussion |

> This worked example combines plausible enterprise patterns to make the governance approach concrete. It does not describe a real organisation, report measured outcomes or establish compliance. All quantities below are **hypothetical acceptance targets**, to be replaced by an organisation's approved baselines and thresholds.

## 1. Illustrative Situation

An enterprise has AI initiatives distributed across business units but no dependable system inventory, common risk method or consistent production gate. Teams use different model providers and retain uneven evidence. Leadership wants proportionate governance that improves accountability without applying the same process to a low-impact assistant and a consequential decision-support system.

## 2. Worked Rollout Sequence

1. **Discover and classify.** Business units identify production and in-development systems. Owners record purpose, users, data, decisions or actions, model providers and provisional risk.
2. **Create the minimum record.** Every in-scope system receives an AI System Card. High-risk systems also require explicit evaluation, red-team, privacy and human-oversight evidence.
3. **Introduce a launch gate.** New deployments cannot proceed with an open blocking item. Existing systems receive risk-based remediation dates rather than an unsupported declaration of compliance.
4. **Centralise common controls.** An AI Gateway applies model allow-lists, logging, cost attribution and configurable provider controls while applications retain business-specific safeguards.
5. **Connect evidence to delivery.** CI/CD and gateway events update the registry or flag stale records. A governance forum resolves exceptions and records risk acceptance by accountable roles.
6. **Review and improve.** Monitoring, incidents, model changes and scope changes trigger reassessment; unnecessary controls are simplified where evidence shows lower risk.

## 3. Lessons the Example Preserves

- Making the **System Card part of the launch gate** creates a practical reason to keep documentation current.
- A shared **AI Gateway** can improve model visibility, substitution and cost attribution, but it does not replace application controls.
- **Risk-tiering** focuses scrutiny on consequential systems and avoids unnecessary friction for lower-risk work.
- Named human accountability must accompany the registry; a list of systems without owners does not govern them.

## 4. Approaches That Fail in the Worked Scenario

- **One process for every system:** teams face disproportionate review and seek informal workarounds. The corrective pattern is tiered evidence and approval.
- **Monitoring added after launch:** teams cannot reconstruct missing quality and cost baselines. Monitoring becomes a launch prerequisite.
- **A manually maintained spreadsheet:** records drift from deployed reality. Registry updates are connected to gateway and delivery events, with reconciliation alerts.
- **Tooling presented as compliance:** the enterprise treats technical evidence as input to governance, not a guarantee that obligations have been met.

## 5. Hypothetical Acceptance Targets — Not Reported Outcomes

| Measure | Baseline | Hypothetical target for planning |
|---|---|---|
| In-scope production systems with a current System Card | Establish during discovery | At least 95% by the end of the illustrative rollout |
| New high-risk launches with monitoring active before first use | Establish from launch records | 100% |
| Low-risk reviews completed within the service objective | Establish from workflow data | At least 90%, using a locally approved time objective |
| Registry-to-deployment reconciliation exceptions | Establish after integration | Fewer than 5% open beyond the agreed correction window |

These figures are example acceptance thresholds only. A real programme should choose targets after measuring inventory quality, review demand, capacity and risk; it should also report exceptions, control failures and review quality rather than presenting coverage alone as success.

## 6. AI-ADM Interpretation

The sequence supports the **Preliminary Phase** operating model, **Phase F** governance architecture, **Phases G–H** implementation and migration planning, **Phase I** launch and conformance governance, and **Phase J** change triggers. Individual systems still execute the full set of phases appropriate to their scope and risk.

## 7. Related Resources

- [WG1 — AI Governance Playbook](../../09-WG-Outputs/WG1-AI-Governance-Playbook/README.md)
- [AIEA-401 — Capability and Governance](../../05-Standards/AIEA-401-Capability-Governance.md)
- [AI Governance Operating Playbook](../../07-Toolkits-and-Playbooks/04-AI-Governance-Operating-Playbook.md)
- [AI System Card template](../../12-Templates/AI-System-Card-Template.md)
- [Pre-Deployment Launch Gate](../../12-Templates/Pre-Deployment-Launch-Gate.md)
