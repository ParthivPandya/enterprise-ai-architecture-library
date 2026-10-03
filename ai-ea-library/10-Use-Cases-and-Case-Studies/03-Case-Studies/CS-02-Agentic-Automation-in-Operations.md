# CS-02 — Agentic Automation in Operations

| Field | Value |
|---|---|
| **Document ID** | CS-02 |
| **Type** | Illustrative Worked Example |
| **Evidence status** | Fictional composite; not an observed deployment |
| **Theme** | Scaling agentic AI in operations |
| **Illustrative horizon** | Nine-month planning sequence |
| **Intended use** | Architecture, permission and rollout workshop |

> This worked example is a fictional scenario built from generally applicable design lessons. It does not report an organisation's experience or measured benefit. Numerical values are **hypothetical acceptance targets**, not outcomes.

## 1. Illustrative Situation

An operations team can diagnose recurring infrastructure incidents in a test environment, but production use stalls because a general-purpose agent would have excessive access. The worked example shows how the team could move from recommendations to a narrowly bounded set of reversible runbooks without giving the model an administrator identity.

## 2. Worked Rollout Sequence

1. **Shadow:** the agent reads sanitised incident context and recommends a runbook; engineers compare the recommendation with their own diagnosis.
2. **Read-only production:** approved diagnostic tools expose structured metrics and configuration without write access.
3. **Supervised action:** one reversible runbook is added at a time. Every proposed action requires engineer approval and uses a single-purpose credential.
4. **Limited autonomy:** only incident signatures and actions that meet approved precision, rollback and blast-radius criteria become eligible for automatic execution.
5. **Continuous control:** action count, elapsed time and spend are capped. Failed verification or abnormal behaviour trips a circuit breaker and returns the incident to the on-call queue.

## 3. Lessons the Example Preserves

- **Read-only first** reveals recommendation quality before production state can change.
- A **tool/permission matrix** turns a vague concern about agent authority into explicit, reviewable grants.
- **Reversibility-based gates** allow automation of a demonstrably safe subset while humans retain irreversible or uncertain actions.
- Structured tool results and independent policy checks are safer than exposing a shell and relying on the model to self-restrict.

## 4. Approaches That Fail in the Worked Scenario

- **A generic inherited role:** the agent sees irrelevant tools and may propose actions outside the incident. The correction is explicit per-tool, per-service grants.
- **Trusting alert text:** attacker-controlled log or ticket content can contain indirect prompt injection. The correction is instruction/data separation, sanitisation and broker-enforced allow-lists.
- **No action or cost budget:** a retry loop can repeat work and inference. The correction is hard per-run call, time and spend limits.
- **Rollback assumed rather than tested:** an action labelled reversible may not be safe in every state. The correction is precondition checks and runbook tests.

## 5. Hypothetical Acceptance Targets — Not Reported Outcomes

| Measure | Baseline | Hypothetical target for planning |
|---|---|---|
| Eligible routine incidents resolved without engineer execution | Establish after shadow classification | At least 40% of the narrowly eligible set |
| Median time to verified recovery for eligible incidents | Establish by incident class | At least 30% improvement |
| Autonomous actions requiring rollback | No pre-pilot autonomous baseline | Less than 1% |
| Unauthorised or out-of-scope actions | Zero-tolerance control | Zero |
| Runs stopped by budget or circuit breaker | Establish during supervised pilot | Reviewed individually; no target that rewards hidden failure |

These are example gates, not claims. A real team must calibrate them to service criticality, sample size and current performance. Faster recovery is not beneficial if recurrence, major incidents, unsafe suppression or engineer rework increases.

## 6. AI-ADM Interpretation

The sequence exercises **Phase B** operating roles, **Phase C** telemetry and log governance, **Phases D–E** agent and broker architecture, **Phase F** permissions and security controls, **Phases G–I** staged rollout and implementation governance, and **Phase J** change review when tools, services, models or incident patterns change.

## 7. Related Resources

- [WG5 — Scaling Agentic AI](../../09-WG-Outputs/WG5-Scaling-Agentic-AI/README.md)
- [AIEA-G05 — Agentic AI Architecture](../../06-Series%20Guide/AIEA-G05-Agentic-AI-Architecture.md)
- [UC-03 — IT Operations Agent](../02-WG5-Agentic-AI-Use-Cases/UC-03-IT-Operations-Agent-BFSI.md)
- [Tool / Permission Matrix template](../../12-Templates/Tool-Permission-Matrix-Template.md)
- [Red-Team Log template](../../12-Templates/Red-Team-Log-Template.md)
