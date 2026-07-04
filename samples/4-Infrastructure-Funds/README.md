# Infrastructure Funds

Margit Dahl, CFO of an infrastructure fund, wants to give institutional investors a way to value, transfer, or borrow against positions in toll roads, regulated utilities, and renewable-energy assets. Conrad Boyle, Head of Real Assets at a public pension plan, will not increase, transfer, or finance his stake without independently verified operating performance across decades-long horizons.

DGML encodes each concession agreement and operating report as a structured document: tariff mechanisms, performance obligations, debt-service covenants, capital expenditure commitments, ESG metrics — every data element typed, traced to the source page, and anchorable on-chain. Conrad traces a valuation down to a single toll road's traffic figures.

## Documents in this scenario

The largest sample set: ten asset sets (`deal1`–`deal10`), each with a loan agreement, a quarterly report, and a valuation memo, organized into three docsets so the shared vocabulary applies across each document type — this is also the scenario used in [`get-started`](../../get-started) to demonstrate automated document clustering, since it's large enough for the clusterer to have real groupings to find.

| Docset | Contents |
|---|---|
| Loan agreements | `deal1_loan_agreement.dgml.xml` … `deal10_loan_agreement.dgml.xml` |
| Quarterly reports | `deal1_quarterly_report.dgml.xml` … `deal10_quarterly_report.dgml.xml` |
| Valuation memos | `deal1_valuation_memo.dgml.xml` … `deal10_valuation_memo.dgml.xml` |
