# DGML samples

Real business documents, encoded in DGML, organized by scenario. Each scenario folder pairs a short business story — who needs to trust a number, and who won't take their word for it — with the documents DGML makes independently verifiable.

## Start here

New to DGML? **[`hello-dgml.md`](hello-dgml.md)** is a hello-world walkthrough: one real lease document, annotated line by line, showing every layer of the format — semantic, spatial, attestation, readable — as it actually appears in a real file. Read this before the spec if you want the format to click first, the theory second.

## Scenarios

| Folder | Scenario |
|---|---|
| [`1-NonTraded-NAV-REITs/`](1-NonTraded-NAV-REITs) | A non-traded real estate fund's CFO must publish a verifiable monthly NAV traceable to the underlying signed leases. |
| [`2-Commercial-Mortgage-REITs/`](2-Commercial-Mortgage-REITs) | A commercial mortgage lender's CFO needs to prove loan collateral values are marked honestly, loan by loan. |
| [`3-Private-Credit-Funds/`](3-Private-Credit-Funds) | A private credit manager wants a fund NAV verifiable down to individual loans, for an eventually tokenized interest. |
| [`4-Infrastructure-Funds/`](4-Infrastructure-Funds) | An infrastructure fund's CFO needs decades-long operating performance independently verifiable, asset by asset. |

Each folder holds the source PDFs and a generated `dgml-workspace/` with the resulting `.dgml.xml` files, docset by docset — see [`get-started`](../get-started) for how they were produced.
