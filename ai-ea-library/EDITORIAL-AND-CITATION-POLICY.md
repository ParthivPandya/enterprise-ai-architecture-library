# Editorial and Citation Policy

> **Document type:** Library Policy  
> **Audience:** Readers and maintainers  
> **Use when:** Writing, reviewing, or interpreting library content  
> **Last verified:** October 2026  

## Editorial Style

- Use British English for narrative prose: organisation, programme, licence, modelling, optimisation.
- Preserve official names, quoted text, API fields, and established framework terms such as *Center of Excellence* or TOGAF catalog names.
- Prefer direct, testable statements over promotional claims.
- Define acronyms on first use in each standalone document.
- Use sentence case for headings.
- Use one H1 title per document; use H2 and below for its internal structure.
- Use `MUST`, `SHOULD`, and `MAY` only in normative framework content or when explicitly quoting an external requirement.

## Citation Rules

Cite a source for:

- Laws, regulations, commencement dates, and regulator guidance
- Standards requirements and clause mappings
- Numerical benchmarks, forecasts, survey findings, and market sizes
- Named-company outcomes
- Product capabilities, pricing, availability, and licence terms
- Comparative model-performance claims
- Safety, medical, financial, or legal conclusions

Prefer sources in this order:

1. Legislation, gazettes, regulators, and official standards-body material
2. Peer-reviewed research or primary technical reports
3. Audited company filings or originating company disclosures
4. Reputable independent research
5. Secondary summaries, clearly identified as secondary

Do not cite an unsourced aggregator when the primary source is available.

## Reference Format

Use numbered references:

```markdown
1. Organisation or author, [*Exact title*](https://example.org/source),
   version or date, relevant page/section, accessed YYYY-MM-DD.
```

Place the reference immediately after the claim when ambiguity is possible. A chapter-end reference list may be used for longer documents.

## Quantitative Claims

For each metric, record:

- Population and sample size
- Geography and sector
- Measurement period
- Definition of the metric
- Whether the result is measured, self-reported, estimated, or modelled
- Whether the source is independent or vendor-sponsored

Use ranges only when the evidence supports a range. Do not apply a universal adjustment factor to public benchmarks; use scenario and sensitivity analysis based on the organisation's baseline.

## Case Studies and Examples

- A **Verified Case Study** requires an attributable source or documented interview record.
- An anonymised real case must state what evidence was reviewed and why identity is withheld.
- A composite scenario is an **Illustrative Worked Example**.
- Illustrative numbers must be labelled as assumptions or acceptance targets.
- Never claim zero incidents, full compliance, certification, or guaranteed savings without auditable evidence.

## Regulatory Content

State:

- Jurisdiction
- Legal instrument and provision
- Role to which it applies
- Commencement/effective date
- Whether it is binding law, draft, guidance, or recommended practice
- Date last verified

Use “supports alignment” rather than “ensures compliance” unless reporting a scoped, independently audited conclusion.

## Volatile Technology Content

Provider regions, model versions, context windows, prices, and licence terms should carry an **as-of date** and a link to current provider documentation. Prefer architecture principles that remain valid when products change.

## Figures, Tables, and Accessibility

- Give every figure a number, descriptive title, alt text, and source/author note.
- Include a textual explanation of the architectural conclusion; do not require readers to infer it only from colour or position.
- Use SVG for scalable architecture views and provide an editable source where practical.
- Do not rely only on box-drawing characters for important diagrams.
- Design tables for narrow screens and print; split overly wide matrices into focused tables.
- Do not use colour alone for risk or status. Pair it with text or symbols.
- Expand acronyms in alt text where the diagram is expected to stand alone.
