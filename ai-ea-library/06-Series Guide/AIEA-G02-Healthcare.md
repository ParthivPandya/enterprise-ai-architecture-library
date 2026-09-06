# AIEA® Series Guide
## AIEA-G02: AI Architecture in Healthcare & Life Sciences
### Document Number: AIEA-G02 | Version 1.0 | 2026

---

## Preface

This document is an official AIEA Series Guide supplementing the core AIEA Standard. It establishes the architectural blueprints, clinical safety frameworks, interoperability standards, and regulatory compliance patterns for Artificial Intelligence in healthcare provider, payer, biotechnology, and medical device organizations.

In healthcare, AI systems operate in life-critical contexts where algorithmic error, model hallucination, or data bias can directly cause patient morbidity or mortality. This guide translates clinical guidelines and medical device regulations into rigorous enterprise architecture controls.

This guide MUST be read by Healthcare Enterprise Architects, Chief Medical Information Officers (CMIOs), Clinical AI Engineers, and Healthcare Compliance Officers.

---

# Chapter 1: Healthcare Regulatory Landscape & SaMD Classification

Clinical AI systems are governed by a convergence of healthcare data privacy laws and medical device safety regulations:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              HEALTHCARE AI REGULATORY COMPLIANCE MATRIX                 │
├────────────────────────────────┬────────────────────────────────────────┤
│ MEDICAL DEVICE & CLINICAL      │ PATIENT DATA PRIVACY                   │
├────────────────────────────────┼────────────────────────────────────────┤
│ • US FDA SaMD (Software as a   │ • HIPAA Security & Privacy Rules       │
│   Medical Device) & GMLP       │ • India DPDPA (Health Data as PII)     │
│ • EU AI Act Annex III          │ • EU GDPR Article 9 (Special Category  │
│   (Medical AI = High Risk)     │   Health Data)                         │
│ • CDSCO Medical Device Rules   │ • ABDM (Ayushman Bharat Digital        │
│   (India)                      │   Mission) Health Data Policies        │
└────────────────────────────────┴────────────────────────────────────────┘
```

## 1.1 US FDA Software as a Medical Device (SaMD) Framework

AI systems intended to diagnose, treat, prevent, or cure human disease are classified as **Software as a Medical Device (SaMD)** under FDA oversight:

- **Good Machine Learning Practice (GMLP):** The FDA, Health Canada, and UK MHRA enforce ten guiding principles for AI development, requiring rigorous data representative of the target patient population, clear separation between training and test sets, and human-in-the-loop clinical validation.
- **Predetermined Change Control Plans (PCCP):** Machine learning models that dynamically adapt or update in production MUST have an FDA-approved PCCP defining the boundaries of permissible algorithmic modification before deployment.

## 1.2 EU AI Act & Medical Device Regulation (MDR)

Under the EU AI Act, AI systems acting as safety components of medical devices or systems falling under EU MDR 2017/745 are classified as **High-Risk AI Systems (Annex III)**. Deploying organizations MUST maintain:
- Auditable risk management files throughout the medical device lifecycle.
- Post-Market Clinical Follow-up (PMCF) to monitor for algorithmic drift in clinical outcomes.
- Mandatory adverse event reporting to national competent authorities within 72 hours of any severe medical incident.

## 1.3 Indian Clinical Context: CDSCO & ABDM

In India, healthcare AI architectures MUST comply with:
- **Central Drugs Standard Control Organisation (CDSCO):** Regulatory approval for AI diagnostic software under the Medical Device Rules.
- **Ayushman Bharat Digital Mission (ABDM):** AI systems accessing Indian patient health records MUST integrate via ABDM's Milestone 1–3 standards (ABHA ID generation, consent manager integration via Health Information User/Provider protocols, and LOINC/SNOMED CT coding).

---

# Chapter 2: Clinical AI Reference Architecture Patterns

```
┌─────────────────────────────────────────────────────────────────────────┐
│              CLINICAL AI REFERENCE ARCHITECTURE TOPOLOGY                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PATTERN 1: CLINICAL DECISION SUPPORT SYSTEM (CDSS)                     │
│  EHR Patient Data ──> HL7 FHIR Adapter ──> De-Identification Engine     │
│                                                   │                     │
│                                                   ▼                     │
│  Clinical Knowledge Graph (SNOMED / RxNorm) ──> Hybrid Clinical RAG     │
│                                                   │                     │
│                                                   ▼                     │
│  Frontier Medical LLM (Med-PaLM / BioNeMo) ──> Grounded Clinical Rec    │
│                                                   │                     │
│                                                   ▼                     │
│  Safety Gate: Clinician Affirmative Review (HITL) ──> EHR Chart Update  │
├─────────────────────────────────────────────────────────────────────────┤
│  PATTERN 2: MEDICAL IMAGING INFERENCE PIPELINE (DICOM / PACS)           │
│  CT / MRI Scanner ──> DICOM Router ──> PACS Ingestion (Orthanc)         │
│                                              │                          │
│                                              ▼                          │
│  Segmentation & Detection Model (TensorRT) ──> Secondary Radiologist View│
└─────────────────────────────────────────────────────────────────────────┘
```

## 2.1 Pattern 1: Governed Clinical Decision Support System (CDSS)

### Architectural Specifications:
- **Non-Autonomous Principle (Principle D4):** Clinical decision systems MUST operate in an advisory capacity only. The architecture MUST prohibit direct automated order entry without an affirmative electronic signature from an authenticated, licensed physician.
- **Deterministic Grounding:** Recommendations MUST be strictly grounded in verified clinical guidelines (e.g., UpToDate, PubMed Central, NICE Guidelines) via hybrid retrieval.
- **Contraindication Verification:** Prior to presenting any therapeutic recommendation, a deterministic rules engine validates the patient's active medication list against a drug-drug interaction database (RxNorm) to prevent lethal contraindications.

## 2.2 Pattern 2: Medical Imaging Inference & PACS Integration

### Architectural Specifications:
- **DICOM Protocol Standards:** Medical imaging AI (radiology, pathology, ophthalmology) MUST ingest and emit images conforming to the DICOM 3.0 standard.
- **PACS Interoperability:** Model inference runs as an asynchronous microservice connected to the enterprise Picture Archiving and Communication System (PACS) via C-STORE and DICOMweb (WADO-RS / STOW-RS).
- **Secondary Review Architecture:** Algorithmic heatmaps (Grad-CAM overlays) are displayed as secondary annotations in the radiologist's viewer; original raw DICOM pixel data is never overwritten.

---

# Chapter 3: Health Data Architecture & Interoperability Standards

## 3.1 HL7 FHIR Integration Architecture

Healthcare AI architectures MUST NOT ingest raw proprietary relational database dumps. Systems MUST communicate via **HL7 FHIR Release 4 / Release 5**:

```json
// Example: Standard FHIR Observation Payload for AI Diagnostic Ingestion
{
  "resourceType": "Observation",
  "id": "glucose-reading-ai-01",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "2339-0",
      "display": "Glucose [Mass/volume] in Blood"
    }]
  },
  "subject": { "reference": "Patient/104928" },
  "valueQuantity": {
    "value": 185.0,
    "unit": "mg/dL",
    "system": "http://unitsofmeasure.org"
  }
}
```

## 3.2 Protected Health Information (PHI) De-Identification

All patient data routed to foundation models MUST undergo automated de-identification complying with HIPAA Safe Harbor (redacting all 18 specified identifiers) or Expert Determination statistical validation:
- Named Entity Recognition (NER) models trained on clinical corpora (BioBERT/ClinicalBERT) redact patient names, dates, phone numbers, and institutional affiliations in memory before token dispatch.
- Synthetic patient identifiers are mapped via a secure salt-hashed lookup table stored within an air-gapped enterprise vault.

---

# Chapter 4: Adverse Event Reporting & Clinical Kill-Switch

Any healthcare AI deployment exhibiting diagnostic discrepancies exceeding clinical variance thresholds MUST execute the **Clinical Incident Protocol**:

1. **Immediate Clinical Isolation:** The AI Gateway diverts EHR requests to baseline deterministic standard-of-care templates.
2. **Statutory Vigilance Reporting:** Submission of formal Medical Device Vigilance reports to the FDA (MedWatch) or CDSCO within statutory timeframes (24 hours for life-threatening events).
3. **Model Audit Committee Review:** Full retrospective audit of all clinical decisions influenced by the affected model version over the preceding 90 days.

---

*AIEA Series Guide AIEA-G02: AI Architecture in Healthcare & Life Sciences. Document AIEA-G02, Version 1.0, 2026.*  
*AI Enterprise Architecture Forum (AIEAF).*
