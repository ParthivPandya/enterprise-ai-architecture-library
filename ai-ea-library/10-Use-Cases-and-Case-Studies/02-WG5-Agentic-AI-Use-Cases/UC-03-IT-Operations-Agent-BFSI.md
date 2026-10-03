# UC-03 — IT Operations Agent (BFSI)

| Field | Value |
|---|---|
| **Document ID** | UC-03 |
| **Document type** | Reference Use Case (forward-looking) |
| **Status** | Agentic architecture pattern for adaptation |
| **Validates** | WG5 — Scaling Agentic AI |
| **Sector** | Banking, financial services and insurance |
| **Scenario** | Bounded triage and remediation of routine infrastructure incidents |
| **Provisional risk tier** | Limited for read-only diagnosis; potentially High as action scope and blast radius increase |
| **Primary accountable role** | IT Operations Automation System Owner |
| **AI role** | Diagnose, recommend and execute explicitly granted reversible runbooks |
| **Lifecycle scope** | Read-only trial, supervised action pilot and controlled production operation |

> This is a prospective reference design, not a report of operational results. Institutions must apply their own resilience, security, outsourcing and change-control obligations before granting any production access.

## 1. Purpose and Context

An operations team receives recurring alerts for temporary storage, stalled non-critical jobs and expiring certificates. A bounded agent could connect diagnosis, approved runbooks and evidence while leaving high-impact authority with an engineer. The model receives no general shell, administrator role or unrestricted network path. The workflow independently checks every tool, target and parameter.

## 2. Actors and Responsibilities

| Actor | Responsibility |
|---|---|
| Service owner | Defines service criticality, maintenance constraints and acceptable remediation |
| On-call engineer | Reviews recommendations, approves gated actions and accepts escalations |
| Operations automation owner | Accountable for agent scope, performance, controls and incidents |
| Runbook and platform owners | Maintain tested procedures, isolated tools, identities and rollback |
| Security, change and resilience functions | Review threats, production scope and continuity |
| Assurance | Reviews permissions, evidence and control operation |

## 3. Trigger and Preconditions

**Trigger:** the event platform creates an incident whose alert signature, affected service and severity match an approved automation policy.

**Preconditions:**

1. Service, environment and incident type are allow-listed; critical or ambiguous events are excluded.
2. Monitoring data is current enough for the runbook.
3. Each tool has a service identity, schema, target limit, timeout and rollback.
4. Change windows, dependency health and freeze periods are machine-checkable.
5. Permissions, approvals, budgets, circuit breakers and immediate engineer takeover are operational.

## 4. Scope and Boundaries

Initial scope is read-only diagnosis. Later stages may permit reversible actions such as restarting one stateless instance or cleaning an approved temporary path. Database mutation, firewall changes, user administration, deletion, payment processing and unrestricted execution are prohibited. Certificate replacement, failover or uncertain reversibility requires separate authorisation.

## 5. Main Success Flow

1. The incident platform sends a signed event with references to approved telemetry.
2. Policy verifies severity, service, environment, change window and eligibility.
3. A bounded context builder retrieves metrics, approved changes, dependencies and the current runbook.
4. The agent proposes a diagnosis and plan using only tools exposed for that incident class.
5. Deterministic checks validate tool, target, parameters, action count and approval.
6. For a permitted reversible action, the broker issues a short-lived credential and runs the tool.
7. A predefined check verifies health; failure triggers safe rollback where possible and escalation.
8. The incident record stores context, plan, policy, approval, tool result, cost and disposition.

## 6. Alternate and Exception Flows

| Condition | Required response |
|---|---|
| Alert text contains instructions or untrusted log content | Treat it as data, not instruction; sanitise context and rely on the system policy |
| Incident is ineligible or telemetry is unreliable | Do not act; assign manual diagnosis with the reason |
| Approval is required | Pause with an exact plan, evidence, impact and expiry; execute only after authorised approval |
| Tool gives an unexpected or partial result | Stop, preserve state and escalate rather than guessing |
| Calls, spend or action oscillation exceed limits | Trip the circuit breaker and revoke the run credential |
| A broader outage is detected | Disable local remediation where it could mask symptoms and invoke major-incident procedures |

## 7. Data Classification and Handling

| Data set | Illustrative classification | Handling requirement |
|---|---|---|
| Alerts, metrics, topology, logs and traces | Confidential; Restricted where sensitive data appears | Service access, redaction, bounded retrieval and no provider training |
| Runbooks and configuration metadata | Confidential internal | Version control, integrity checks and approved publication |
| Credentials and tokens | Restricted secrets | Never place in prompts; broker short-lived credentials at execution time |
| Plans, approvals and tool results | Confidential audit evidence | Tamper-evident incident correlation |
| Aggregate performance and cost | Internal | Remove sensitive service details |

## 8. Logical Architecture

```text
Monitoring / incident platform
            |
            v
Eligibility + change-window policy engine
            |
            v
Bounded context builder <---- Metrics / topology / approved runbooks
            |
            v
Agent orchestrator --> AI Gateway --> Approved model
            |
            v
Deterministic action-policy broker <---- Tool/permission matrix
        |                 |
        |                 +----> Human approval workflow
        v
Scoped runbook tools --> Target service --> Health verification / rollback
        |
        +----> Incident record / audit / security, quality and cost monitoring
```

## 9. Controls and Evidence

| Control objective | Design control | Evidence |
|---|---|---|
| Least privilege | Per-tool, per-service allow-list; no inherited administrator role | Permission matrix and identity-access review |
| Reversibility | Action classification, tested rollback and human gate for irreversible actions | Runbook test and approval record |
| Bounded autonomy | Maximum steps, elapsed time, calls and spend per incident | Policy configuration and circuit-breaker events |
| Injection and change safety | Separate untrusted data; check freeze windows and recent changes | Adversarial tests and policy decisions |
| Accountability | Named owner and human takeover | System Card, incident timeline and reviewer action |

## 10. Failure, Fallback and Recovery

Fallback is the existing human incident process; component loss must not prevent alerting or engineer access. Validation failure, anomalous choice, unexpected side effect or budget breach revokes the credential. The broker rolls back only while verified preconditions hold; otherwise it escalates. Re-enablement requires impact and permission review plus replay in a non-production harness.

## 11. Evaluation and Acceptance

Offline evaluation replays representative, synthetic or sanitised incidents without write access. Test runbook selection, refusal, parameters, stale data, conflicts, partial failure, hostile logs and loop termination. Shadow recommendations precede a phase requiring approval for every action.

Measure eligibility precision, diagnosis usefulness, unsafe proposals, correct policy blocks, verification, rollback, escalation, latency and cost by service and incident class. Any unauthorised action, secret exposure or gate bypass stops the pilot.

## 12. Value Hypothesis

**Hypothesis:** connecting approved diagnostics and reversible runbooks will reduce repetitive engineer effort and elapsed resolution time for narrowly eligible incidents without increasing service risk.

| Measure | Baseline to establish | Prospective acceptance target |
|---|---|---|
| Engineer time and elapsed recovery | Current incidents by class | Improvement set after baseline; no saving is asserted |
| Safe automation coverage | Current deterministic coverage | Expand only where precision and rollback evidence pass |
| Incorrect action or rollback | Current automation and manual-change comparison | Service-owner threshold |
| Recurrence and hidden failure | Current post-incident measure | No material deterioration |

Also record alert suppression, delayed escalation, over-reliance and spend. Coverage is not success if severity or recurrence worsens.

## 13. AI-ADM Mapping

| AI-ADM phase | Use-case output |
|---|---|
| Phases 0–A | Toil hypothesis, stakeholders, action risk, boundary and stops |
| Phase B | Incident roles, approvals, takeover and operating-model change |
| Phase C | Telemetry, logs, topology, runbook lineage and quality |
| Phases D–E | Orchestrator, tools, policy checks, gateway, isolation and resilience |
| Phase F | Permissions, security, risk acceptance and audit evidence |
| Phases G–I | Shadow, supervised and limited-autonomy stages with rollback gates |
| Phase J | Review after tool, service, model, policy or incident-pattern change |

## 14. Related Resources

- [AIEA-201 — AI Architecture Development Method](../../05-Standards/AIEA-201-AI-ADM.md)
- [AIEA-G05 — Agentic AI Architecture](../../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)
- [Multi-Agent Orchestration](../../00-Foundations/04-Multi-Agent-Orchestration.md)
- [WG5 — Scaling Agentic AI](../../09-WG-Outputs/WG5-Scaling-Agentic-AI/README.md)
- [Tool / Permission Matrix template](../../12-Templates/Tool-Permission-Matrix-Template.md)
- [Red-Team Log template](../../12-Templates/Red-Team-Log-Template.md)
- [AI Incident Report template](../../12-Templates/AI-Incident-Report-Template.md)
- [Illustrative operations worked example](../03-Case-Studies/CS-02-Agentic-Automation-in-Operations.md)
