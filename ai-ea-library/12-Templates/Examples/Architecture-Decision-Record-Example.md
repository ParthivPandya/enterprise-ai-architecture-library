# Architecture Decision Record — Completed Example

> **Illustrative only:** fictional decision for the template scenario. Source template: [Architecture-Decision-Record.md](../Architecture-Decision-Record.md).

| Field | Value |
|---|---|
| **ADR number** | ADR-EX-001 |
| **Title** | Keep onboarding workflow authority outside the language model |
| **Status** | Accepted for the illustrative design; implementation evidence pending |
| **Date** | 2026-09-10 (illustrative) |
| **Deciders** | Onboarding Architecture, Risk, Security and Operations roles |
| **Related system** | AI-SYS-EX-001 |

## Context

The assistant must explain an applicant's current step without deciding identity, eligibility or account creation. A free-form agent that selects arbitrary next steps could contradict KYC controls or turn a model error into an apparent rejection. The design also needs a predictable manual fallback.

## Decision

We will keep journey state and transition authority in the existing deterministic workflow engine. The model will receive only the current approved state, customer-safe reason codes and allowed next steps. It may explain those values or request an explicitly granted read or support-handoff tool. A deterministic validator will discard any response that conflicts with workflow state. No model credential will permit account creation.

## Options Considered

| Option | Pros | Cons |
|---|---|---|
| Deterministic workflow with model guidance (chosen) | Clear authority, testable transitions, safe fallback | More integration and curated content |
| Model-managed journey | Flexible conversation and fewer explicit rules | Unacceptable ambiguity, difficult assurance and wider blast radius |
| Deterministic help only | Lowest model risk and simpler testing | Less adaptable explanation; may not address varied questions |

## Consequences

- **Positive:** model errors cannot authorise progression; status explanations remain traceable; the journey operates without the model.
- **Negative / trade-offs:** every new state needs approved content and schema changes; responses may feel less flexible.
- **Follow-up actions:** implement contract tests for [DC-EX-001](Data-Contract-Example.md), test state conflicts, and maintain the [permission matrix](Tool-Permission-Matrix-Example.md).

## Compliance Notes

This decision supports least privilege, human accountability and data minimisation. It is one design control, not a statement that the system complies with the India DPDP Act, applicable Rules, KYC or other obligations. Qualified functions must assess the complete implementation and operating context.
