# AIEA Series Guide
## AIEA-G09: Manufacturing & Industrial AI
### Document Number: AIEA-G09 | Version 1.0 | 2026

| Metadata | Detail |
|---|---|
| Document type | Independent sector reference guide |
| Audience | Enterprise architects, plant and OT architects, control and safety engineers, manufacturing leaders, data and AI teams, cyber-security teams, and assurance functions |
| Use when | Selecting, designing, procuring, integrating, assuring, or operating AI that consumes industrial data or may influence plant activity |
| Scope | Discrete and process manufacturing, utilities and heavy industry; plant, edge, enterprise, and supplier interfaces; advisory and tightly governed control-support use cases |
| Last verified | October 2026 |
| Standing | Independent guidance, not a standard, certification, safety case, legal opinion, or substitute for site-specific engineering judgement |

---

## Preface

This document is an independent AIEA Series Guide supplementing the core AIEA Reference Framework. It provides architectural patterns, governance controls, and reference use cases for applying AI in **manufacturing and industrial** settings — discrete and process manufacturing, heavy industry, and the extended industrial supply chain.

Manufacturing AI operates where the digital and physical worlds meet: predictive maintenance, quality inspection, process optimisation, and increasingly agentic coordination across plant systems. This introduces concerns absent from purely digital AI — operational technology (OT) safety, cyber-physical risk, and real-time constraints.

This guide is intended for Enterprise Architects, Plant/Operations Technology Architects, and AI Governance Leads supporting industrial operations. It extends, and should be read alongside, [AIEA-101](../05-Standards/AIEA-101-Introduction-Core-Concepts.md), [AIEA-501](../05-Standards/AIEA-501-Reference-Models.md), and [AIEA-G05: Agentic AI](AIEA-G05-Agentic-AI-Architecture.md).

---

## Chapter 1: The Industrial AI Landscape

### 1.1 Where AI Creates Value in Manufacturing

| Value Area | Typical AI Capability | Primary KPI |
|---|---|---|
| Predictive maintenance | Anomaly detection on sensor/telemetry data | Unplanned downtime, MTBF |
| Quality inspection | Computer vision defect detection | Defect escape rate, scrap |
| Process optimisation | ML control-parameter recommendation | Yield, energy per unit |
| Supply & demand | Forecasting and planning | Inventory turns, stockouts |
| Worker assistance | LLM assistants over SOPs and manuals | Time-to-resolution, safety incidents |
| Industrial agents | Agentic coordination across plant systems | Cycle time, OEE |

### 1.2 The IT/OT Divide

Industrial AI must respect the boundary between **Information Technology (IT)** and **Operational Technology (OT)**. OT systems (PLCs, SCADA, DCS) run physical processes where a wrong action has physical consequences. AI that influences OT must treat every actuating action as potentially irreversible (AIEA-101 Principle D4).

```
┌───────────────────────────┐        ┌───────────────────────────┐
│  IT / Enterprise Zone     │        │  OT / Plant Floor Zone    │
│  Analytics, LLM assist,   │  ───▶  │  PLC / SCADA / DCS         │
│  planning, dashboards     │  read  │  sensors / actuators       │
│  (model training/serving) │ ◀───   │  (real-time control)       │
└───────────────────────────┘ telemetry └───────────────────────┘
      AI recommends / predicts            Humans/safety systems actuate
```

---

## Chapter 2: Reference Architecture

### 2.1 The Industrial AI Stack

- **Edge layer:** sensor acquisition, local inference for latency-critical detection.
- **Plant data layer:** historian, time-series store, unified namespace.
- **AI platform layer:** feature pipelines, model serving, [AI Gateway](../11-Architecture-Diagrams/README.md) for LLM assistance.
- **Enterprise layer:** planning, governance, cross-plant analytics.

### 2.2 Design Principles (Industrial Overlay)

| Principle | Industrial Implication |
|---|---|
| Model Independence (D1) | Edge and cloud models substitutable; no hard coupling to one vendor runtime |
| Grounded Generation (D2) | Worker assistants ground answers in SOPs, manuals, and maintenance logs |
| Minimum Sufficient Agency (D3) | Industrial agents get narrowly scoped, auditable tool access to plant systems |
| Reversibility (D4) | **No AI-initiated OT actuation without human/safety-system approval** |
| Observability (O1) | Model drift monitored against changing equipment and material conditions |

### 2.3 ISA-95-Aware Architecture Views

[ISA-95/IEC 62264](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) supplies useful models and terminology for enterprise-to-control integration. It does not prescribe an AI architecture, but its levels help prevent an analytics service from being connected to a control function without an explicit boundary decision.

| ISA-95-aligned view | Typical assets | Appropriate AI role | Default integration posture |
|---|---|---|---|
| Levels 0-1: process and sensing | Physical process, sensors, actuators, drives | Deterministic signal processing or separately assured edge inference | Local, bounded, resource-controlled; no dependency on enterprise connectivity for a safe state |
| Level 2: monitoring and supervisory control | PLCs, DCS, SCADA, HMI | Detection and operator decision support | Read-biased interface; write paths mediated by validated control logic and authorised operators |
| Level 3: manufacturing operations | MES/MOM, historian, laboratory and maintenance systems | Quality, scheduling, maintenance and contextual analytics | Governed APIs or brokers; plant identity, asset context, and change control |
| Level 4: business planning and logistics | ERP, supply planning, enterprise data platforms | Forecasting, network optimisation, and management assistance | Aggregated or purpose-limited plant data; no direct route to Level 2 or below |
| External/cloud services | Vendor platforms, foundation models, remote support | Training, non-real-time inference, document assistance | Terminated outside the OT trust boundary; exchange through inspected, authenticated conduits |

Maintain three complementary architecture views:

1. **Context view:** plants, lines, enterprise services, suppliers, remote support, safety systems, owners, and points where information can cause physical consequence.
2. **Logical view:** ingestion, historian, features, model registry, inference, rules, human review, workflow, evidence, lineage, and failure response.
3. **Deployment view:** edge, plant, data-centre, and cloud placement; zones; conduits; identity; update route; time synchronisation; and disconnected dependencies.

The views should distinguish the **basic process control system**, any **safety instrumented system**, and AI services. Shared telemetry does not imply shared authority. Operator recommendations identify source, uncertainty, operating envelope, timestamp, and expiry.

### 2.4 IEC 62443-Aware Zones and Conduits

The [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) treats industrial automation and control system security across asset-owner, service-provider, integration, and product lifecycles. Apply its risk-based zones-and-conduits concepts to AI components rather than treating “the AI platform” as one trusted zone.

- Place model development, model registry, plant inference, engineering workstations, remote support, and safety-related assets in zones justified by risk and required security capability.
- Permit only documented flows through conduits. A historian replication flow, model-package promotion flow, and maintenance-ticket API are separate purposes and should not become a general bridge.
- Use authenticated, signed, versioned model packages and configuration. Promotion into a plant zone follows the same approval discipline as other consequential OT changes.
- Keep cloud or enterprise compromise from creating a direct write path into control. A broker, unidirectional mechanism, staged transfer service, or plant-side API may be appropriate according to the site's risk assessment.
- Inventory third-party libraries, model formats, edge accelerators, remote-management agents, and update services as supply-chain dependencies.

[NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) provides further authoritative OT security guidance, including segmentation, least functionality, monitoring, availability, and safety constraints. Plant-specific requirements remain decisive.

### 2.5 Data and Model Flow

A robust flow is: **event -> quality check -> context -> approved feature -> inference -> policy guard -> decision -> outcome**. Preserve the observation and context needed to reproduce a material recommendation, subject to retention and security rules.

Industrial data quality controls cover units, clock source, calibration, asset, operating mode, maintenance state, material batch, missingness, and range. Do not silently combine unlike assets, recipes, conditions, or failure labels. Model lineage connects deployments to data windows, feature code, evaluation, dependencies, approval, and rollback.

---

## Chapter 3: Governance and Safety

### 3.1 Cyber-Physical Risk

Industrial AI risk extends to physical safety. Risk classification should consider whether an AI output can lead to a physical action, and if so, the system is **High-Risk** by default.

| Control | Requirement |
|---|---|
| OT change control | AI-recommended control changes follow existing OT change management; AI does not bypass it |
| Fail-safe defaults | Loss of AI service degrades to the existing safe control baseline |
| Human authority | A qualified operator can override and disable AI influence at any time |
| Segmentation | AI serving isolated from direct OT write access except via governed interfaces |

### 3.2 Regulatory and Standards Context

- Functional safety regimes (e.g., IEC 61508 / 61511) remain authoritative for safety functions; AI does not replace them.
- Use the [AIEA-CW01 Compliance Workbook](../05-Standards/AIEA-CW01-Compliance-Workbook.md) for cross-cutting AI obligations.

### 3.3 Functional-Safety-Aware Design

[IEC 61508-1](https://webstore.iec.ch/en/publication/5515) provides generic functional-safety requirements for electrical, electronic, and programmable electronic safety-related systems; [IEC 61511-1](https://webstore.iec.ch/en/publication/61289) applies functional-safety lifecycle concepts to safety instrumented systems in the process sector. Access to the complete standards and competent interpretation may be required. This guide does not assign a safety integrity level or claim that a model is suitable for a safety function.

Use these boundary rules unless a competent, documented safety lifecycle establishes otherwise:

- AI availability is not a safety control. Loss, delay, corruption, or withdrawal of AI should leave the process within the pre-existing safe operating strategy.
- Do not credit a general-purpose model, probabilistic recommendation, or cloud service as a risk-reduction layer in a hazard analysis without evidence acceptable to the responsible functional-safety authority.
- Safety interlocks and engineered protection layers retain independent authority. AI cannot suppress alarms, defeat trips, rewrite limits, or conceal degraded instrumentation.
- A proposed closed-loop use requires hazard analysis, defined operating envelope, deterministic guards, validation under foreseeable abnormal conditions, management of change, proof testing where applicable, and a documented route to a safe state.
- Human approval is meaningful only when the operator has time, competence, context, authority, and an interface that does not induce automation bias.

The AI assurance case should link each hazard-relevant claim to evidence: intended use, excluded use, training-data relevance, scenario coverage, uncertainty treatment, cyber-security assumptions, human-factors assessment, fallback behaviour, independent review, and operational monitoring. Changes to models, thresholds, prompts, features, sensors, firmware, or source documents can invalidate that evidence and therefore require impact assessment.

### 3.4 Governance Control Set

| Control | Required decision and evidence |
|---|---|
| Accountable ownership | Named operational owner, technical owner, safety contact, cyber-security contact, and authority to suspend use |
| Intended-use boundary | Approved assets, modes, users, decisions, operating envelope, exclusions, and prohibited actions |
| Hazard and risk linkage | Trace from AI failure modes to existing HAZOP, FMEA, bow-tie, machinery risk, or equivalent site process |
| Data governance | Authorised sources, asset semantics, quality rules, lineage, retention, access, and treatment of vendor data |
| Model release | Versioned evaluation, independent review proportionate to consequence, signed artefact, segregation of duties, and rollback |
| Human factors | Workload, alarm interaction, presentation of uncertainty, confirmation design, competence, and override testing |
| Security | Zone and conduit assessment, threat model, software/model bill of materials where practical, credential control, and update integrity |
| Supplier assurance | Support and vulnerability process, incident notice, component provenance, remote access, end-of-support, portability, and exit |
| Operational evidence | Input/output and decision records proportionate to risk, model/configuration version, health state, override, and outcome |
| Incident response | Safe disablement, evidence preservation, OT escalation, supplier coordination, and criteria for controlled restoration |

---

## Chapter 4: Reference Use Cases

| Use Case | Pattern | Risk Tier |
|---|---|---|
| Predictive maintenance on rotating equipment | Anomaly detection + maintenance workflow | Limited |
| Vision-based surface defect inspection | CV classification + human adjudication | Limited/High |
| Energy optimisation recommendation | ML recommendation, human-applied | High (if actuating) |
| Shop-floor SOP assistant | RAG over manuals | Limited |
| Agentic maintenance triage | Bounded agent, read + ticketing only | Limited |

See the agentic operations pattern in [UC-03](../10-Use-Cases-and-Case-Studies/02-WG5-Agentic-AI-Use-Cases/UC-03-IT-Operations-Agent-BFSI.md) for a transferable bounded-agent design.

### 4.1 Implementation Patterns

#### Pattern A: Predictive maintenance

Ingest vibration, temperature, current, lubricant, work-order, and operating-context data without bypassing the historian or approved plant collection path. Generate a health indication and supporting evidence, then create or enrich a maintenance notification. The planner or authorised maintainer decides the work. Prevent labels such as “failure” from being inferred solely from a work order; verify failure taxonomy and censoring. Evaluate by asset family and operating regime, including lead time, missed-event rate, alert burden, calibration, and maintenance action yield.

#### Pattern B: Visual quality inspection

Place inference where image latency, bandwidth, and data sensitivity require it. Control lighting, camera position, line speed, product variant, and image retention. Route low-confidence, novel, or safety-relevant defects to human adjudication. Retain a representative adjudicated sample to monitor drift and disagreement. A model that reduces visible defects but increases escaped defects is not acceptable merely because aggregate accuracy is high.

#### Pattern C: Grounded worker assistance

Retrieve from approved, versioned SOPs, manuals, permits, and maintenance instructions. Filter retrieval by site, asset, role, language, and document validity. Display citations and document revision beside the answer. Refuse or escalate when the source is absent, conflicting, expired, or outside the user's authorisation. The assistant does not approve permits, isolation, lock-out/tag-out, or deviations from procedure.

#### Pattern D: Process optimisation recommendation

Constrain recommendations to a validated operating envelope and apply deterministic limits before presentation. Simulate or replay against representative normal, transition, and disturbance conditions. Start in shadow mode, then advisory mode; closed-loop authority is a distinct safety and control-engineering decision, not an ordinary model release.

#### Pattern E: Bounded industrial agent

Separate read, propose, approve, and execute permissions. A low-consequence agent may gather evidence, correlate alarms, draft a ticket, or schedule an approved workflow. Tool calls use allow-listed schemas, short-lived credentials, idempotency where possible, rate limits, and complete audit records. Direct arbitrary PLC, DCS, engineering-station, or safety-system access is prohibited.

---

## Chapter 5: Adoption Roadmap

1. **Observe:** start with read-only prediction and inspection; no actuation.
2. **Assist:** worker assistants and recommendations with human application.
3. **Coordinate:** bounded agents for triage and workflow, never direct OT writes without approval.
4. **Optimise:** closed-loop optimisation only where safety systems and human authority fully contain risk.

This is a sequence of assurance states. Movement is based on evidence and plant readiness:

| State | Entry condition | Evidence before expanding |
|---|---|---|
| Observe | Authorised read path and accountable owner | Data-quality profile, baseline process performance, threat model, and safe failure test |
| Assist | Stable observation and clear user decision | Human-factors trial, uncertainty presentation, override procedure, and outcome capture |
| Coordinate | Approved workflow interfaces | Permission tests, duplicate-action controls, exception handling, and recovery exercise |
| Optimise | Explicit control and safety engineering decision | Operating-envelope evidence, abnormal-scenario evaluation, independent protection, management of change, and rollback drill |

Pilot on a bounded asset or line with an understood fallback. Include operators, maintainers, control engineers, safety personnel, cyber-security, data teams, and worker representatives where appropriate. Training covers limits, escalation, degradation, and retained operator accountability.

Before replication to another line or plant, reassess equipment, instrumentation, recipes, environment, workforce practice, network topology, language, and local obligations. A technically identical model may behave differently because the operational context is not identical.

---

## Chapter 6: Failure Modes and Evaluation

### 6.1 Common Failure Modes

| Failure mode | Consequence | Preventive or detective response |
|---|---|---|
| Sensor drift, swapped tags, or unit mismatch | Plausible but incorrect recommendation | Schema and unit validation, calibration status, range checks, cross-sensor consistency |
| Training-serving skew | Plant inference differs from validation | Shared versioned feature logic, replay tests, release fingerprint |
| Context collapse | Model ignores mode, recipe, asset, or maintenance state | Context as mandatory input; abstain when missing |
| Domain shift | Performance degrades after wear, material, seasonal, or process change | Segmented monitoring, outcome review, change-triggered revalidation |
| Automation bias | Operator accepts weak advice | Evidence and uncertainty display, active confirmation, competence and workload testing |
| Alert flooding | Important events are ignored | Alert budget, prioritisation, suppression rules, review of action yield |
| Unsafe coupling | Enterprise or cloud fault reaches control | Segmentation, mediated interfaces, deterministic guards, safe baseline |
| Model or update compromise | Malicious or unintended plant behaviour | Signed packages, provenance, isolated verification, controlled promotion, rollback |
| Hallucinated work instruction | Injury, damage, or non-conforming work | Approved-source retrieval, citations, refusal, no permit or isolation authority |
| Loss of service | Operational disruption | Local fallback, dependency inventory, degraded-mode procedure, recovery test |

### 6.2 Evaluation Metrics

Metrics require site-specific baselines and acceptance thresholds set before the evaluation; this guide does not invent target values.

- **Prediction:** precision and recall by failure class; false alerts per asset operating period; missed critical events; calibration; usable warning lead time; and performance by asset family and mode.
- **Inspection:** defect escape rate, false reject rate, adjudicator disagreement, coverage of product variants, image-quality failure rate, and drift by camera or line.
- **Optimisation:** constraint violations, recommendation acceptance and rejection reasons, realised versus predicted effect, stability during transitions, energy or yield normalised for product mix, and fallback frequency.
- **Worker assistance:** citation correctness, source freshness, grounded-answer rate, refusal quality, unsafe-answer rate, task completion with and without assistance, and user override.
- **Operations:** inference latency and availability at the point of need, stale-output rate, rollback recovery, unauthorised tool-call attempts, cyber-security events, and time to detect degradation.
- **Safety and human factors:** hazard-related near misses involving AI, operator response time, automation-bias observations, alarm burden, override accessibility, and successful safe-state exercises.

Report distributions and safety-relevant worst cases, sliced by plant, asset, mode, material, environment, and other meaningful factors. Each metric needs an owner, source, review trigger, and response.

---

## Chapter 7: References

The following sources were checked in October 2026. Confirm the edition, amendment, national adoption, licence, and applicability required for the site:

- [ISA-95 series: Enterprise-Control System Integration](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard)
- [ISA/IEC 62443 series: Security for Industrial Automation and Control Systems](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [IEC 62264-1:2013: Enterprise-control system integration](https://webstore.iec.ch/en/publication/6675)
- [IEC 61508-1:2010: Functional safety — General requirements](https://webstore.iec.ch/en/publication/5515)
- [IEC 61511-1:2016+A1:2017: Safety instrumented systems for the process industry](https://webstore.iec.ch/en/publication/61289)
- [NIST SP 800-82 Rev. 3: Guide to Operational Technology Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)

---

*AIEA Series Guide AIEA-G09: Manufacturing & Industrial AI. Version 1.0, 2026.*
