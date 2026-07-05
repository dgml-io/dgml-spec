# DGML Format Specification

This repository is the home of the **DGML format specification** and the community hub for the open standard.

DGML (Document Graph Markup Language) is a semantic XML representation of business documents. Where raw source files give you layout and pixels, DGML gives you meaning: tags that describe what each element is in the document's domain — a contract clause, an invoice line item, a policy definition — not how it appeared on the page.

The headline feature is cross-document tag consistency: documents of the same kind share the same semantic vocabulary. This is what separates DGML from a raw extraction or a structural transcription, and what makes it suitable for reasoning over a corpus rather than a single file.

A second fundamental property is complete semantic preservation. Traditional extraction pipelines make an irreversible upfront decision: choose the fields to pull, discard everything else. This works when the questions are known in advance. It fails the moment a new use case emerges — a regulatory change, a derivative product, a counterparty due diligence request — that requires a field no one thought to extract. DGML preserves the full semantic structure of the document: every element, every relationship, every typed value. Nothing is discarded. A document processed once remains fully queryable without going back to the source. This is not a feature of the tooling — it is a property of the format.

A third fundamental property is document order with graph semantics. Most graph formats treat documents as unordered collections of facts. But in business documents, order is meaning: definitions precede usage, clause sequence governs interpretation, provenance depends on exact position. DGML preserves document order as a first-class property of the format, while also representing relationships across elements and documents as a graph.

## Contents

- [`spec.md`](spec.md) — The DGML format specification, the reference source
- [`spec.html`](spec.html) — The DGML format specification, derived from `spec.md`, rendered as HTML
- [`spec.pdf`](spec.pdf) — The DGML format specification, derived from `spec.md`, rendered as PDF
- [`samples/`](samples/) — Samples of DGML files
- [`scripts/`](scripts/) — Maintenance utilities (e.g. regenerating `samples/file-list.json`)
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — How to contribute

## Participate

- **Shape the spec** — open an [Issue](../../issues) or [Discussion](../../discussions) to propose a change, challenge a design decision, or bring a use case the founding organizations haven't encountered.
- **Contribute a sample** — if you have a real-world document type that would make a useful addition to `samples/`, open an Issue to discuss it first.

The Python reference implementation lives in [dgml-io/dgml](https://github.com/dgml-io/dgml).

## License

Apache 2.0. See [`LICENSE`](LICENSE).
