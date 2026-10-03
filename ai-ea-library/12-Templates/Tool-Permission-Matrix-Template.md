# Tool / Permission Matrix

> Copy this file per agentic AI system. Implements the Minimum Sufficient Agency principle (AIEA-101 Principle D3): every tool an agent can call is explicitly granted and justified.

| Field | Value |
|---|---|
| **Agent system** | `<AI-SYS-0000>` |
| **Version** | `<x.y>` |
| **Owner** | `<name>` |
| **Last reviewed** | `<YYYY-MM-DD>` |

## 1. Granted Tools

| Tool / API | Operation(s) | Scope / Limits | Reversible? | Human Approval Required | Justification |
|---|---|---|---|---|---|
| `<tool name>` | `<read / write / execute>` | `<data/records in scope>` | `<Yes/No>` | `<None / for irreversible>` | `<why the agent needs it>` |

## 2. Explicitly Denied
| Capability | Reason |
|---|---|
| `<e.g. send external email>` | `<not required for task>` |

## 3. Irreversible Actions
List every action that cannot be undone. Each MUST require elevated human approval (Principle D4).

| Action | Approver Role | Approval Mechanism |
|---|---|---|
| `<e.g. execute payment>` | `<role>` | `<mechanism>` |

## 4. Review
- **Review trigger:** `<each production deployment / scope change>`
- **Reviewed by:** `<name>`
- **Least-privilege confirmed?** `[ ] Yes`
