# Non-Traded Real Estate Funds

Marguerite Halloran, CFO of a non-traded real estate fund, must publish a monthly net asset value (NAV) — the per-share value of everything the fund owns — that investors rely on to subscribe or redeem. Her valuation advisor, Theo Ellison, won't stand behind the number unless he can trace each property's value back to the underlying signed leases — which today sit in scattered systems he cannot independently verify.

DGML encodes each lease as a structured document: base rent, escalation schedule, free-rent concessions, operating-expense recoveries, renewal options, co-tenancy clauses — every data element typed, traced to the source page, and anchorable on-chain. Theo follows the trail from NAV to clause without a phone call.

## Documents in this scenario

Five properties, each with a primary lease document and a rent roll, organized into two docsets so the shared vocabulary applies across each document type:

| Property | Lease | Rent roll |
|---|---|---|
| Arcadia Biotech Park, Module 4 | `Arcadia Biotech.dgml.xml` | `Arcadia Biotech Rent Roll.dgml.xml` |
| Elysium Dome | `Elysium Dome.dgml.xml` | `Elysium Dome Rent Roll.dgml.xml` |
| Olympus Plaza | `Olympus Plaza.dgml.xml` | `Olympus Plaza Rent Roll.dgml.xml` |
| Olympus Plaza, Zone 2 | `olympus Plaza Zone2.dgml.xml` | `Olynpus Plaza Zone2 Rent Roll.dgml.xml` |
| Hellas Basin | `Hellas Basin.dgml.xml` | `Hellas Basin Rent Roll.dgml.xml` |

## Read one in full

[`../hello-dgml.md`](../hello-dgml.md) walks through `Arcadia Biotech.dgml.xml` line by line — a good starting point for understanding the format itself, independent of this scenario's business story.
