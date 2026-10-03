# Data Contract — Completed Example

> **Illustrative only:** fictional proposed interface, not a production guarantee. Source template: [Data-Contract-Template.md](../Data-Contract-Template.md).

| Field | Value |
|---|---|
| **Contract name** | Onboarding Assistant State View |
| **Contract ID** | DC-EX-001 |
| **Producer** | Retail Onboarding Workflow |
| **Consumer** | AI-SYS-EX-001 |
| **Version** | 0.3 |
| **Effective date** | Proposed pilot start |
| **Status** | Draft |

## 1. Schema

| Field | Type | Nullable | Description | Synthetic example |
|---|---|---|---|---|
| `case_token` | string | No | Opaque, short-lived case reference | `CASE-EX-0042` |
| `journey_state` | enum | No | Approved state-machine code | `DOCUMENT_RETRY` |
| `allowed_next_steps` | string array | No | Actions permitted by workflow policy | `["UPLOAD_DOCUMENT","REQUEST_SUPPORT"]` |
| `status_reason_code` | enum | Yes | Non-sensitive reason suitable for approved explanation | `IMAGE_UNREADABLE` |
| `content_locale` | string | No | Approved guidance locale | `en-IN` |
| `state_updated_at` | datetime | No | UTC timestamp of authoritative state | `2026-09-15T08:30:00Z` |

Identity numbers, document images, sanctions indicators and internal fraud rules are explicitly excluded.

## 2. Quality Guarantees

- **Completeness:** all non-nullable fields present for 100% of published events; a missing field blocks assistant use.
- **Freshness:** state no older than 30 seconds at read time; stale records force refresh or handoff.
- **Validation:** values must match the published schema and approved enumerations; unknown codes fail closed.
- **Volume expectation:** planning assumption of up to 25,000 state reads per day; validate through load testing.

These are proposed acceptance thresholds, not observed service levels.

## 3. Lineage and Provenance

- **Upstream sources:** authoritative onboarding workflow and approved content-locale configuration.
- **Transformations:** replace the internal case key with a short-lived token; filter fields; map internal reasons to customer-safe codes.
- **Lineage tracking:** schema registry version and workflow event identifier recorded with each response.

## 4. Privacy and Classification

- **Contains PII?** `[x] Yes  [ ] No` — the token can remain linkable inside the controlled environment.
- **Classification:** Restricted.
- **Processing basis:** to be confirmed by the privacy function for the actual journey; this example does not prescribe a basis.
- **Residency constraint:** proposed India region, subject to legal, contractual and sector validation.

## 5. Change Management

- **Breaking changes:** new major version, 30 calendar days' notice where practicable, and consumer contract tests before cutover.
- **Deprecation:** registry notice, owner notification and dual-version period; emergency security changes follow the incident process.

## 6. Sign-off

| Role | Name | Date |
|---|---|---|
| Producer owner | Workflow Product Owner role — pending named assignee | Pending |
| Consumer owner | Onboarding AI System Owner role — pending named assignee | Pending |
