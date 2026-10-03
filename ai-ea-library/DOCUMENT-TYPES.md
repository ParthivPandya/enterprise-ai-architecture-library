# Document Types and Authority

> **Document type:** Library Policy  
> **Audience:** Readers and maintainers  
> **Use when:** Interpreting the authority and intended use of a document  

The library separates requirements, guidance, reusable assets, and examples so readers can judge what a document can legitimately establish.

| Type | Purpose | Language | What It Does Not Establish |
|---|---|---|---|
| **Normative Framework** | Defines requirements within AIEA | MUST, SHOULD, MAY | Law, accredited certification, or third-party endorsement |
| **Informative Guide** | Explains concepts and architecture choices | Descriptive and conditional | Mandatory organisational policy |
| **Operational Playbook** | Provides repeatable activities, roles, inputs, and outputs | Action-oriented | Proof that an activity was performed |
| **Reference Model** | Provides reusable conceptual or logical structures | Model and pattern language | A production design without contextual tailoring |
| **Template** | Captures structured evidence | Placeholders and instructions | Complete or correct evidence until filled and reviewed |
| **Checklist** | Supports verification | Questions and gates | Compliance merely because boxes are checked |
| **Worked Example** | Demonstrates application using an illustrative scenario | Explicitly hypothetical assumptions | A real deployment or validated benchmark |
| **Verified Case Study** | Describes an attributable real implementation | Evidence-backed past tense | Universal or guaranteed outcomes |

## Recommended Metadata

Major documents should begin with:

```markdown
> **Document type:** Informative Guide
> **Primary audience:** Enterprise Architects
> **Use when:** Designing an enterprise AI platform
> **Scope:** Global; note jurisdiction-specific sections
> **Last verified:** October 2026
> **Authority:** Independent practitioner guidance
```

## Normative Language

- **MUST**: an absolute requirement within the AIEA Reference Framework
- **SHOULD**: recommended unless a documented reason justifies deviation
- **MAY**: permitted but optional

These terms do not override law, regulation, contract, organisational policy, or an authoritative standard.

## Evidence Labels

Use one of the following labels for quantitative material:

- **Primary-source fact**
- **Third-party survey finding**
- **Company-reported outcome**
- **Illustrative assumption**
- **Acceptance target**
- **Author recommendation**

Do not convert an illustrative assumption or company-reported outcome into a universal benchmark.

