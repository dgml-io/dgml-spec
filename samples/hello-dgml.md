# Hello, DGML: the Arcadia Biotech lease

This is a hands-on first encounter with the format: one real DGML output file — a commercial lease agreement — annotated line by line to show every feature described in the [spec](https://github.com/dgml-io/dgml-spec/blob/main/spec.md) as it actually appears in practice. If you only read one thing before the spec itself, read this.

The source file is `Arcadia Biotech.dgml.xml`, one of the documents in the [Non-Traded Real Estate Funds scenario](1-NonTraded-NAV-REITs/README.md) (see [`get-started`](../get-started) for how it was generated), and lives at:

```
1-NonTraded-NAV-REITs/dgml-workspace/docsets/3ym6vmfrczj5/files/ziwoi3co9qc0/Arcadia Biotech.dgml.xml
```

It's a lease for lab space at "Arcadia Biotech Park, Module 4" — 120 lines, one document, small enough to read in full, but it exercises nearly the entire element-level feature surface of DGML: structure, spatial grounding, typed values, and semantic links.

## The document, end to end

Stripped of most attributes for a first look, the shape is:

```xml
<dg:chunk xmlns:dg="…" xmlns:docset="…" xmlns:xsi="…" xmlns:xhtml="…">
  <docset:PropertyIdentifier>                          <!-- property header -->
  <docset:CommercialPressurizedSpaceLeaseAgreement>     <!-- landlord/tenant summary block -->
  <docset:CommercialPressurizedSpaceLeaseAgreement>     <!-- the actual "THIS LEASE IS MADE…" recital -->
  <docset:LeaseTermDefinition>                          <!-- Article 1: premises, term, base rent -->
  <docset:RentEscalationSchedule>                       <!-- Article 2: rent escalations -->
  <docset:TenantImprovementScope>                       <!-- Article 3: TI allowance -->
  <docset:LifeSupportSystemsAndExpenses>                <!-- Article 4: expense stops -->
  <docset:RightOfFirstRefusal>                          <!-- Article 5: ROFR + decommissioning -->
  <docset:LandlordName>                                 <!-- landlord signature block -->
  <docset:TenantName>                                   <!-- tenant signature block -->
</dg:chunk>
```

Worth noticing immediately: **the vocabulary is domain-specific, not generic.** These aren't `<section>` or `<div>` tags — they're `docset:LeaseTermDefinition`, `docset:RentEscalationSchedule`, `docset:TenantImprovementScope`. Every other lease in this docset (`3ym6vmfrczj5`) uses this exact same vocabulary, which is what makes cross-document queries possible: "get `RentEscalationRate` from every lease in this docset" works identically regardless of which property it is.

## Layer 1 — Semantic: what each element means

The domain vocabulary is namespaced under `docset:` (bound to `http://dgml.io/dgml-workspace/LeaseAgreements` in this file's docset) and is what makes the file more than a structural transcription. Examples from the file:

| Element | Value |
|---|---|
| `docset:PremisesAddress` | "Sector F, Module 4, Arcadia Biotech Park, Dome 4, Ares Prime" |
| `docset:PremisesArea` | "6,200 square meters" |
| `docset:LeaseTermDuration` | "Twelve (12) Martian Years" |
| `docset:AnnualRentAmount` | "Three Million Two Hundred Twenty-Four Thousand Martian Credits (M$ 3,224,000.00)" |
| `docset:RentEscalationRate` | "three percent (3.0%)" |
| `docset:TenantImprovementAllowanceAmount` | "Nine Hundred Thirty Thousand Martian Credits (M$ 930,000.00)" |
| `docset:LeaseStructureType` | "NNN Lease" |
| `docset:HazardousMaterialsObligation` | full decontamination-on-exit clause |

None of these are inferred from HTML-like structure — a `<table>` or `<div class="rent">` doesn't tell you which number is the annual rent versus the per-square-meter rate versus the TI allowance. The tag name does. That's the semantic layer: query `AnnualRentAmount` across every lease in the docset and you get exactly the right number back, every time, with no per-document parsing logic.

Structural roles are a separate, generic vocabulary — `dg:structure="section"`, `"header"`, `"ul"`/`"ol"`/`"li"`, `"lim"` (the `1.1.`, `2.1.` clause-number markers, rendered inline with no wrapper), `"p"`. These map directly to HTML tags (this is exactly what [`tools/dgml2html`](../tools/dgml2html) does) and are what make the file renderable — see Layer 4 below.

## Layer 2 — Spatial: every value traced to the page

Almost every element carries `dg:origin`, a pixel-precise bounding box on the source PDF page: `page x1 y1 x2 y2`. From line 35:

```xml
<docset:AnnualRentAmount dg:origin="1 754 1112 1946 1143" xml:id="annualrentamount">
  Three Million Two Hundred Twenty-Four Thousand Martian Credits (M$ 3,224,000.00)
</docset:AnnualRentAmount>
```

This says: page 1, box from (754, 1112) to (1946, 1143). A viewer can highlight exactly that rectangle on the rendered page image — this is how a DGML answer becomes a citation instead of an assertion.

One variation to notice: **multi-line spans use `;`-separated boxes.** Line 24's recital paragraph wraps across three lines of the PDF, so its `dg:origin` is three space-separated boxes joined by `;`: `"1 122 554 2272 586; 1 122 601 2264 632; 1 122 648 1239 679"`.

## Layer 3 — Attestation: the anchoring hooks

Any XML element subtree in this document — a single clause, `docset:RentEscalationRate` at line 42, or the whole `docset:LeaseTermDefinition` section — can be hashed independently and anchored on an external chain, establishing Proof of Origin for that specific data element without revealing the rest of the document. The element is located by its position in the tree, not by any attribute on it — no special marker is needed for an element to be anchorable.

## Semantic links: `xml:id` / `dg:itemprop` / `dg:href`

Beyond containment (the XML tree), the file encodes a relationship graph across elements using `xml:id` as the target and `dg:itemprop`/`dg:href` as a named, directed edge from source to target:

```xml
<docset:LeaseExpirationDate xsi:type="date" dg:value="2096-10-31"
    xml:id="leaseexpirationdate"
    dg:itemprop="relativeTo" dg:href="#commencementdate">
  October 31, 2096
</docset:LeaseExpirationDate>
```

Read as a triple: `leaseexpirationdate --relativeTo--> commencementdate`. Every named link in the file:

| Source | `dg:itemprop` | Target |
|---|---|---|
| `leaseexpirationdate` | `relativeTo` | `commencementdate` |
| `rentescalationmechanism` | `escalates` | `annualrentamount` (edge value `dg:value="P1Y"` — ISO 8601 duration, i.e. "annually") |
| `rentescalationrate` | `escalates` | `annualrentamount` (edge value `dg:value="0.03"` — the rate itself) |
| `baseyear` | `effectiveOn` | `commencementdate` |
| `hazardousmaterialsobligation` | `relativeTo` | `leaseexpirationdate` |
| `signatorysignature` (landlord) | `attestsTo` | `commercialpressurizedspaceleaseagreement` |
| `signatorysignature-2` (tenant) | `attestsTo` | `commercialpressurizedspaceleaseagreement` |

Two links share the same target with different `dg:itemprop` values and different edge `dg:value`s (`rentescalationmechanism`/`rentescalationrate` both `escalates → annualrentamount`) — the graph isn't limited to one edge per element pair. This is what turns the document from a tree into a graph: "what determines this rent amount" is answerable by walking incoming `escalates` edges, without re-parsing prose.

## Typed values: `xsi:type` + `dg:value`

Where a value has a machine-usable normal form, it's expressed twice — the human-readable text as element content, the normalized form as `dg:value`, typed via `xsi:type`:

```xml
<docset:CommencementDate xsi:type="date" dg:value="2084-11-01" …>November 1, 2084</docset:CommencementDate>
<docset:BaseYear xsi:type="gYear" dg:value="2084" …>2084</docset:BaseYear>
<docset:TenantProportionateShare xsi:type="decimal" dg:value="100" …>100%</docset:TenantProportionateShare>
```

Three XML Schema types appear in this file: `date`, `gYear`, `decimal`. A consumer doesn't need to parse "November 1, 2084" — it reads `dg:value="2084-11-01"` directly. The human text stays as element content for the Readable layer (below) and for cases where the source phrasing itself matters.

## Layer 4 — Readable: the same file, rendered

Some content elements carry a `dg:structure` role, and some also carry an optional `dg:style` — plain CSS declarations for the formatting DGML observed on the source page. Neither is exhaustive: the goal is a document a person can read, not a pixel-faithful reproduction of the page, so only enough elements carry these attributes to make the result legible. A header in this file might look like:

```xml
<dg:chunk dg:structure="header" dg:style="font-weight: bold; text-align: left"
    dg:origin="1 122 821 749 852">ARTICLE 1: PREMISES, TERM, AND RENT</dg:chunk>
```

[`tools/dgml2html`](../tools/dgml2html) turns both attributes into a normal HTML page: `dg:structure` picks the tag (`section` → `<section>`, `li` → `<li>`, `lim` markers → inline enumerator text with no wrapper, …), and `dg:style` is copied verbatim into that tag's `style` attribute. Running it (from the repo root):

```bash
python tools/dgml2html/dgml2html "samples/1-NonTraded-NAV-REITs/dgml-workspace/docsets/3ym6vmfrczj5/files/ziwoi3co9qc0/Arcadia Biotech.dgml.xml" -o arcadia-biotech.html
```

opens in any browser as a normal-looking lease document — no CSS authored by hand, no special viewer. The same file an LLM reasons over is one a person can just read.

## What this file demonstrates, in one line each

- **Structure** — domain-specific tags nested under generic `dg:structure` roles that map straight to HTML.
- **Spatial** — `dg:origin` pixel boxes, including multi-line spans, on every content-bearing element.
- **Typed values** — `xsi:type` + `dg:value` giving machine-normal forms alongside human text.
- **Graph** — `xml:id` + `dg:itemprop`/`dg:href` encoding directed, named relationships between elements, including edge-level metadata via `dg:value`.
- **Attestation-ready** — any subtree, located by its position in the tree, is independently hashable and anchorable on-chain.
- **Readable** — `dg:structure` and `dg:style`, applied just enough to be legible, render the whole thing as a normal document with a tiny script and zero bespoke tooling.
