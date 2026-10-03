# Data Contract

> Copy this file per data source feeding an AI system. A data contract is the agreement between the data producer and the AI system that consumes it.

| Field | Value |
|---|---|
| **Contract name** | `<name>` |
| **Contract ID** | `<DC-0000>` |
| **Producer (owner of source)** | `<team / system>` |
| **Consumer (AI system)** | `<AI-SYS-0000>` |
| **Version** | `<x.y>` |
| **Effective date** | `<YYYY-MM-DD>` |
| **Status** | `<Draft / Active / Deprecated>` |

## 1. Schema
| Field | Type | Nullable | Description | Example |
|---|---|---|---|---|
| `<field>` | `<string/int/...>` | `<yes/no>` | `<meaning>` | `<value>` |

## 2. Quality Guarantees
- **Completeness:** `<% non-null expected>`
- **Freshness / latency:** `<max age of data>`
- **Accuracy / validation rules:** `<constraints>`
- **Volume expectations:** `<rows/day or range>`

## 3. Lineage and Provenance
- **Upstream source(s):** `<systems of record>`
- **Transformations applied:** `<pipeline steps>`
- **Lineage tracking method:** `<tool / catalogue link>`

## 4. Privacy and Classification
- **Contains PII?** `[ ] Yes  [ ] No`
- **Data classification:** `<Public / Internal / Confidential / Restricted>`
- **Lawful basis (India DPDP Act/GDPR, as applicable):** `<basis>`
- **Residency constraint:** `<region>`

## 5. Change Management
- **Breaking-change policy:** `<notice period, versioning rule>`
- **Deprecation notice:** `<how consumers are informed>`

## 6. Sign-off
| Role | Name | Date |
|---|---|---|
| Producer owner | `<name>` | `<YYYY-MM-DD>` |
| Consumer (AI System Owner) | `<name>` | `<YYYY-MM-DD>` |
