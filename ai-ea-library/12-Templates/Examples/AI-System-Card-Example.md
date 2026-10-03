# AI System Card — Completed Example

> **Illustrative only:** fictional pre-production record. It does not describe a real bank or establish safety or compliance. Source template: [AI-System-Card-Template.md](../AI-System-Card-Template.md).

| Field | Value |
|---|---|
| **System name** | Customer Onboarding Guidance Assistant |
| **System ID** | AI-SYS-EX-001 |
| **Version** | 0.8 |
| **Status** | In development — controlled pilot proposed |
| **Risk classification** | High (provisional; independent approval pending) |
| **System Owner (accountable)** | Head of Retail Onboarding role; named assignee held in the controlled register |
| **Technical Owner** | Digital Platforms Lead role |
| **Date created** | 2026-09-01 (illustrative) |
| **Last reviewed** | 2026-09-15 (illustrative) |
| **Next review due** | Before any pilot launch |

## 1. Purpose and Scope

- **Business purpose:** explain onboarding steps, collect non-sensitive conversation context and guide applicants to secure forms.
- **In-scope use:** supported retail current-account journeys in English; status explanation from approved workflow codes.
- **Out-of-scope / prohibited use:** KYC, sanctions, eligibility or credit decisions; account creation; disclosure of screening logic; collection of identity numbers in chat.
- **Affected stakeholders:** applicants, support colleagues, KYC analysts and onboarding operations.

## 2. Capability and Behaviour

- **System type:** LLM guidance assistant around a deterministic state machine.
- **Model and provider:** enterprise-approved hosted instruction model through the AI Gateway; final provider/version not yet approved.
- **Inputs:** current workflow state, approved help content and tokenised case context.
- **Outputs / actions:** guidance text and a structured request for one of three granted read or handoff tools.
- **Known failure modes:** invented requirements, state mismatch, excessive confidence, sensitive-data echo and prompt injection from uploaded text.
- **Performance boundaries:** not evaluated for unsupported languages, business accounts or accessibility needs outside the pilot scope.

## 3. Data

- **Data sources:** onboarding-state contract [DC-EX-001](Data-Contract-Example.md), approved content library and support-routing service.
- **PII processed?** `[x] Yes  [ ] No` — free-text entry is minimised and redacted.
- **Data residency:** proposed India region; contractual and sector review pending.
- **Retention:** conversation content proposed for 30 days; audit metadata for the period set by the approved schedule.

## 4. Governance and Compliance

- **Applicable frameworks:** internal AI risk framework; NIST AI RMF mapping; India DPDP Act/Rules alignment assessment pending. Listing a framework does not assert conformity.
- **Pre-deployment review:** [NO-GO example](Pre-Deployment-Launch-Gate-Example.md).
- **Explainability:** customer status is generated only from approved status codes and message text.
- **Human oversight:** support handoff on request, uncertainty or exception.
- **Red-team record:** [RT-EX-001](Red-Team-Log-Example.md).

## 5. Operations

- **Monitoring:** state mismatch, unsupported requirements, handoff success, latency, cost, disclosure failures and segment-level error indicators.
- **Dashboard:** proposed restricted onboarding-operations dashboard.
- **Alert thresholds:** any unauthorised progression or restricted-data disclosure stops the pilot; other thresholds require approval before launch.
- **Fallback:** deterministic help content and colleague handoff; workflow state is preserved.
- **Cost attribution:** Retail Onboarding / Assisted Journey.

## 6. Lifecycle

- **Review cadence:** quarterly if launched, and after every material model, workflow or data change.
- **Retirement triggers:** invalid business case, repeated control breach, unsupported provider change or replacement by a safer non-AI route.

## 7. Change Log

| Date | Version | Change | By |
|---|---|---|---|
| 2026-09-15 (illustrative) | 0.8 | Added state-consistency validator and restricted pilot boundary | Architecture review role |
