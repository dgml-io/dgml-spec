# DGML Format Specification

This repository is the home of the **DGML format specification** and the community hub for the open standard.

DGML (Document Graph Markup Language) is a semantic XML representation of business documents. Where raw source files give you layout and pixels, DGML gives you meaning: tags that describe what each element is in the document's domain — a contract clause, an invoice line item, a policy definition — not how it appeared on the page.

The headline feature is cross-document tag consistency: documents of the same kind share the same semantic vocabulary — what separates DGML from a raw extraction or structural transcription, and what makes it suitable for reasoning over a corpus rather than a single file.

The second property is complete semantic preservation. Traditional extraction pipelines choose fields upfront and discard the rest — a decision that fails the moment a new use case emerges and needs a field no one thought to extract. DGML preserves the full semantic structure instead — every element, relationship, and typed value — so a document processed once stays fully queryable without returning to the source.

The third is document order with graph semantics. Most graph formats treat documents as unordered collections of facts, but in business documents order is meaning: definitions precede usage, clause sequence governs interpretation, provenance depends on position. DGML preserves document order as a first-class property while also representing relationships across elements and documents as a graph.

The fourth is attestation: Proof of Origin at the data-element level. Every DGMLX package is tamper-evident — any alteration to its content breaks its cryptographic hash. The deeper innovation is that this hashing isn't limited to the whole document: because the semantic tree is structured, any XML element subtree — a single data point, a payment term, a liability cap — can be hashed and anchored on an external chain independently, proving its origin without producing the entire document.

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
