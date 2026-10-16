# Roadmap

This roadmap covers the **DGML format specification** — schema, semantics, and versioning. It does not cover the reference implementation; that roadmap lives in [dgml-io/dgml](https://github.com/dgml-io/dgml).

It reflects our priorities for the next 3–6 months following the public launch. See [SPEC-STATUS.md](SPEC-STATUS.md) for the one-paragraph version of where things stand right now.

## Guiding principle

The spec is stable enough to build on today. It is not frozen. Between now and v1.0, we'd rather take a breaking change that fixes a real problem an implementer hit than lock in a mistake for the sake of stability theater. Every theme below exists to make that trade-off legible instead of ad hoc.

## Themes

### 1. Spec stability

Keep the core structural primitives — docsets, namespaces, `dg:origin`, `dg:itemprop`/`dg:href`, the `dg:` reserved attribute set, and the DGMLX package/attestation model — from changing shape without a documented, versioned migration path.

"Stable" means: if you build against today's spec, a change that breaks you will be called out explicitly, not buried in a diff.

Tracked in [#6](https://github.com/dgml-io/dgml-spec/issues/6).

### 2. Community feedback process

Right now feedback has no defined home or response expectation. This theme is about making "open an issue" actually work: where things go (Issues vs. Discussions), who triages, and how a proposal moves from "raised" to "decided."

Tracked in [#7](https://github.com/dgml-io/dgml-spec/issues/7).

### 3. Format versioning

Define what a version number means for this spec, and what has to be true before we call something `v1.0` and stop making breaking changes without a major version bump.

Note: this is about the spec's own version, distinct from the per-document/per-anchor versioning already defined for blockchain anchoring in spec.md §10 ("Each URI is versioned...") — that mechanism is unrelated and already shipped.

- [ ] Adopt a versioning policy for the spec (what changes warrant a major/minor bump, where it's recorded)
- [ ] Decide the public release numbering scheme going forward (the spec is currently at `0.71` internally; no public releases have been tagged yet)
- [ ] Define the criteria for locking `v1.0` (e.g., independent implementations, real-world document types validated beyond the founding organizations, a quiet period with no open breaking-change proposals)

Tracked in [#8](https://github.com/dgml-io/dgml-spec/issues/8).

## Out of scope for this window

- Formal submission to a standards body (OASIS, ISO, etc.) — premature before v1.0 locks.

## How to influence this roadmap

Open an [Issue](../../issues) or [Discussion](../../discussions). If your use case doesn't fit one of the three themes above, that's useful signal too — say so.
