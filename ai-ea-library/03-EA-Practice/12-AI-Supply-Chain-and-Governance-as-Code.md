# AI Supply Chain and Governance as Code

> **Document type:** Informative Guide and Control Pattern  
> **Primary audience:** Enterprise Architects, Security Architects, MLOps/LLMOps Teams, Governance Leads  
> **Use when:** Building, acquiring, changing, or deploying an AI system  
> **Last verified:** October 2026  
> **Authority:** Independent practitioner guidance  

---

## 1. The AI Supply Chain Is Larger Than the Model

An AI system is assembled from models, datasets, prompts, retrieval content, orchestration libraries, tools, policies, evaluation sets, container images, and external services. A software bill of materials alone cannot answer:

- Which data and licence shaped the model?
- Which prompt and policy version produced the output?
- Which retrieval index was active?
- Which tools could the agent call?
- Which evaluation evidence justified release?

Treat the complete dependency graph as an **AI Bill of Materials (AI-BOM)**.

## 2. Minimum AI-BOM

| Component | Required Fields |
|---|---|
| Foundation or task model | Provider, model/version, digest where available, licence/terms, region |
| Fine-tune or adapter | Base model, training data reference, method, owner, artifact digest |
| Dataset | Owner, purpose, provenance, consent/rights, geography, classification, version |
| Prompt package | System/developer prompt versions, owner, approval, digest |
| Retrieval source | Corpus owner, source system, index version, freshness, access policy |
| Tool or agent capability | Endpoint, schema version, identity, permission scope, owner |
| Evaluation set | Purpose, population, limitations, leakage controls, version |
| Policy bundle | Rule version, authority, effective date, test evidence |
| Runtime | Container/image, libraries, accelerator stack, deployment environment |

The AI-BOM MUST link components to the system version recorded in the AI System Card.

## 3. Provenance and Integrity

### 3.1 Provenance questions

For every component, record:

1. Where did it originate?
2. Who had authority to publish it?
3. What licence or contractual terms apply?
4. What transformation produced the current version?
5. How is integrity verified?
6. What evidence was used to approve it?
7. How can it be revoked or replaced?

### 3.2 Integrity chain

```text
Source artifact
   │  hash + provenance
   ▼
Build / training pipeline
   │  signed attestation
   ▼
Evaluation evidence
   │  release decision
   ▼
Registry entry
   │  deployment policy
   ▼
Runtime verification
```

Use signed artifacts and attestations where the delivery toolchain supports them. High-risk deployments SHOULD reject unverified model, prompt, policy, or container versions.

## 4. Supply-Chain Threats

| Threat | Example | Control |
|---|---|---|
| Model substitution | Registry tag silently points to different weights | Digest pinning and signed provenance |
| Poisoned training data | Malicious samples introduce trigger behaviour | Source review, anomaly testing, lineage |
| Evaluation leakage | Test items appear in training or prompt examples | Segregated evaluation store and leakage checks |
| Dependency compromise | Orchestration package update introduces malicious code | Locked dependencies, scanning, staged rollout |
| Prompt tampering | Production prompt changes outside release process | Prompt registry, review, hash verification |
| Retrieval poisoning | Untrusted document changes answers | Source trust tier, ingestion scanning, citation checks |
| Tool drift | Tool behaviour changes without schema change | Contract tests and behavioural canaries |
| Provider change | Hosted model changes behind stable name | Version pinning, regression gate, fallback |

## 5. Governance as Code

Governance as code converts approved rules into machine-testable and machine-enforceable policies. It does not eliminate governance judgement; it automates repeatable decisions and evidence collection.

### 5.1 Good candidates

- Approved model and region allow-lists
- Maximum risk tier by environment
- Required System Card fields
- PII restrictions
- Tool permission limits
- Mandatory evaluation thresholds
- Spend and token caps
- Human-approval conditions
- Retention and logging configuration
- Required provenance and signature checks

### 5.2 Policy lifecycle

```text
Policy authority
   ▼
Human-readable requirement
   ▼
Machine policy + unit tests
   ▼
CI evidence
   ▼
Deployment admission control
   ▼
Runtime monitoring
   ▼
Exception and review record
```

Every machine policy SHOULD link back to its human-readable authority. A passing automated check must not be described as legal compliance; it proves only that the encoded condition passed.

## 6. Evidence Pipeline

| Stage | Evidence |
|---|---|
| Intake | System owner, purpose, risk classification |
| Build | AI-BOM, provenance, vulnerability and licence scans |
| Evaluate | Dataset version, metrics, thresholds, red-team findings |
| Approve | Decision, approver role, exceptions, expiry |
| Deploy | Artifact digest, environment, policy result |
| Operate | Traces, drift, incidents, spend, policy violations |
| Change | Diff, trigger, regression result, renewed decision |

Evidence should be generated from systems of record wherever possible rather than copied manually into a document.

## 7. Exception Handling

An exception is a governed decision, not a bypass.

Record:

- Requirement and policy that failed
- Business justification
- Risk and affected stakeholders
- Compensating control
- Accountable owner
- Scope and expiry
- Monitoring condition
- Closure evidence

Expired exceptions MUST fail closed for high-risk release gates unless a new decision is recorded.

## 8. Implementation Pattern

1. Establish a registry for models, prompts, datasets, policies, and tools.
2. Define the minimum AI-BOM schema.
3. Generate provenance during build and ingestion.
4. Write policy tests alongside human-readable controls.
5. Enforce policies in CI and deployment admission.
6. Re-evaluate at runtime for conditions that can drift.
7. Stream evidence to the Governance Repository.
8. Test revocation and rollback.

## 9. Review Checklist

- [ ] Deployed versions resolve to immutable identifiers
- [ ] Data and model rights are recorded
- [ ] Prompts, policies, tools, and retrieval indexes are versioned
- [ ] Build provenance and evaluation evidence are linked
- [ ] High-risk releases reject unsigned or unknown artifacts
- [ ] Automated controls link to human-readable requirements
- [ ] Policy tests include expected allow and deny cases
- [ ] Exceptions expire and have compensating controls
- [ ] Rollback and component revocation are tested

## References

1. NIST, [Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf).
2. SLSA, [Supply-chain Levels for Software Artifacts](https://slsa.dev/).
3. in-toto, [software supply-chain integrity framework](https://in-toto.io/).
4. SPDX, [software bill of materials specification](https://spdx.dev/).
5. CycloneDX, [machine-readable bill of materials standard](https://cyclonedx.org/).
6. NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

