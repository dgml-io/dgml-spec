# DGML Format Specification

This repository is the home of the **DGML format specification** and the community hub for the open standard.

**DGML** (Document Graph Markup Language) is a semantic XML representation of business documents. Tags describe what each element *is* in the document's domain — a contract clause, an invoice line item, a policy definition — not how it appeared on the page. The headline feature is cross-document tag consistency: documents of the same kind share the same semantic vocabulary, making them suitable for reasoning over a corpus rather than a single file.

## Contents

- [`spec.md`](spec.md) — The DGML format specification
- [`spec.html`](spec.html) — The DGML format specification, rendered as HTML
- [`samples/`](samples/) — Samples of DGML files
- [`scripts/`](scripts/) — Maintenance utilities (e.g. regenerating `samples/file-list.json`)
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — How to contribute

## Participate

- **Shape the spec** — open an [Issue](../../issues) or [Discussion](../../discussions) to propose a change, challenge a design decision, or bring a use case the founding organizations haven't encountered.
- **Contribute a sample** — if you have a real-world document type that would make a useful addition to `samples/`, open an Issue to discuss it first.

The Python reference implementation lives in [dgml-io/dgml](https://github.com/dgml-io/dgml).

## License

Apache 2.0. See [`LICENSE`](LICENSE).
