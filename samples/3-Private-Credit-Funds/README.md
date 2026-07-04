# Private Credit Funds

Daniel Roth, Head of Private Wealth Solutions at a private credit manager, wants to make his fund's net asset value (NAV) verifiable enough to offer a liquid, eventually tokenized interest. Evelyn Castellano, Chair of a public pension plan's investment committee, will not commit capital to a fund whose NAV she cannot independently verify down to individual loans.

DGML encodes each loan as a structured document: principal, interest terms, maintenance covenants, fair-value assumptions, collateral — every data element typed, traced to the source page, and anchorable on-chain. Evelyn traces the fund's NAV down to one borrower's covenant breach or a single recovery assumption.

## Documents in this scenario

Two borrowers, each with a primary loan document and a financials document, organized into two docsets so the shared vocabulary applies across each document type:

| Borrower | Loan document | Financials |
|---|---|---|
| Kraken Mare | `Kraken_mare.dgml.xml` | `Kraken_mare_financials.dgml.xml` |
| Aegaeon | `Aegaeon.dgml.xml` | `Aegaeon_financials.dgml.xml` |
