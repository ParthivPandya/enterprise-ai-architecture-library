# AI Maturity Scorecard and Heatmap

| Metadata | Description |
|---|---|
| **Purpose** | Convert self-assessment evidence into a transparent capability profile without hiding material gaps in one aggregate number. |
| **Audience** | Assessment participants, enterprise architects, capability owners, governance functions and organisational decision-makers. |
| **Use When** | Summarising the [Self-Assessment Instrument](Self-Assessment-Instrument.md), comparing bounded scopes or identifying constraints for a specific decision. |
| **Outputs** | Statement scorecard, dimension heatmap, evidence-confidence view, constraint summary and interpretation notes. |
| **Content classification** | Calculation, colour and disclosure rules are **Normative** for adopters. Presentation suggestions are **Informative**. |

## 1. Scorecard structure — Normative

Keep statement-level results available. A dimension result is a navigation aid, not a substitute for evidence.

| Statement | Agreed score | Evidence confidence | Key evidence | Limitation | Essential to decision? |
|---|---:|---|---|---|---|
| A1 | | High / Medium / Low | | | Yes / No |
| A2 | | High / Medium / Low | | | Yes / No |
| A3 | | High / Medium / Low | | | Yes / No |

Repeat for statements B1–H3.

Evidence confidence means:

| Confidence | Rule |
|---|---|
| **High** | Multiple relevant records and sampled operation support the score across the assessed scope |
| **Medium** | Relevant evidence exists but has limited scope, depth or independent challenge |
| **Low** | Evidence is indirect, old, incomplete or materially disputed |

Confidence does not raise or lower the score automatically. It tells the reader how cautiously to use it.

## 2. Dimension calculation — Normative

For each dimension:

1. confirm that all three statements have an agreed score;
2. calculate the **median** of the three scores;
3. also report the **minimum** score;
4. list any “Not assessed” statement rather than calculating a complete dimension result; and
5. mark the dimension as a decision constraint when an essential statement scores below the capability needed for the stated decision.

The median reduces distortion from one unusually high statement. The minimum keeps a material weakness visible.

```text
Dimension display = median score / minimum score
Example format = 2 / 1
```

Do not calculate an enterprise-wide average unless every combined scope uses the same instrument and evidence boundary. Even then, retain separate profiles.

## 3. Heatmap rules — Normative

| Median score | Label | Display colour |
|---:|---|---|
| 0 | Not evidenced | Red |
| 1 | Local | Amber |
| 2 | Repeatable | Light green |
| 3 | Adaptive | Dark green |
| Not assessed | Unknown | Grey |

Colour shall never be the only way information is conveyed. Show the numeric score and text label for accessibility.

Add a visible marker when:

- the minimum is lower than the median;
- evidence confidence is Low;
- material dissent remains; or
- the dimension is essential to the decision.

## 4. Heatmap template — Normative

| Dimension | Median | Minimum | Label | Confidence | Essential gap | Interpretation |
|---|---:|---:|---|---|---|---|
| Strategy and value | | | | | | |
| Governance and accountability | | | | | | |
| Data and knowledge | | | | | | |
| Architecture and engineering | | | | | | |
| Evaluation and assurance | | | | | | |
| Security, privacy and resilience | | | | | | |
| People and operating model | | | | | | |
| Platform, operations and economics | | | | | | |

## 5. Deterministic calculation example — Informative

If the three Governance and Accountability statements score 1, 2 and 2:

- ordered scores are 1, 2, 2;
- median is 2;
- minimum is 1;
- display is **2 / 1 — Repeatable, with a Local weakness**.

The dimension must not be presented simply as green if the score of 1 is essential to the decision. The underlying statement and evidence determine the action.

## 6. Constraint summary — Normative

After calculating the heatmap, create a constraint table:

| Decision or intended capability | Essential statement | Observed score | Needed capability | Risk if unresolved | Evidence needed |
|---|---|---:|---|---|---|
| | | | | | |

“Needed capability” is a qualitative description tied to the decision, not an arbitrary demand for the maximum score. A bounded internal assistant may not require the same operating capability as an externally facing action-taking system.

## 7. Comparison rules — Normative

Comparisons are valid only when:

- instrument version, scope and interpretation are equivalent;
- evidence was assessed with the same scoring rules;
- organisational differences are explained;
- “Not assessed” responses remain visible; and
- readers are not encouraged to interpret ordinal scores as precise quantities.

Do not claim that a move from 1 to 2 represents twice the capability. The scale describes observable practice, not a continuous measurement.

## 8. Executive summary format — Informative

Use a concise summary:

1. **Decision supported:** the organisational choice this assessment informs.
2. **Strongly evidenced capabilities:** dimensions with reliable operating evidence.
3. **Decision constraints:** essential low statements or unknowns.
4. **Cross-cutting themes:** repeated causes across dimensions.
5. **Recommended action packages:** links to dependency-led improvements.
6. **Limitations:** excluded scope, weak evidence and unresolved dissent.

Avoid league tables, celebratory labels and unsupported predictions.

## 9. Quality checklist — Normative

- [ ] Every score traces to the response sheet.
- [ ] Median and minimum are calculated correctly.
- [ ] Unknowns are grey and not silently scored zero.
- [ ] Text and numbers accompany colour.
- [ ] Essential weaknesses remain visible.
- [ ] Confidence and dissent are disclosed.
- [ ] Comparisons use equivalent scope and rules.
- [ ] The summary avoids certification and performance claims.
- [ ] Improvement actions are derived from statements and dependencies.

## Related links

- [WG4 reference set](README.md)
- [Self-Assessment Instrument](Self-Assessment-Instrument.md)
- [Facilitation Playbook](Facilitation-Playbook.md)
- [Score-to-Roadmap](Score-to-Roadmap.md)

