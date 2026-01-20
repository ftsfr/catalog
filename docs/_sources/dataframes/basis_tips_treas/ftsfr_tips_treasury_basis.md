# Dataframe: `basis_tips_treas:ftsfr_tips_treasury_basis` - ftsfr_tips_treasury_basis

## TIPS-Treasury Arbitrage Basis

Measures the spread between TIPS-implied risk-free rates and nominal Treasury yields.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Tenor identifier (arb_2, arb_5, arb_10, arb_20) |
| ds | Date |
| y | Arbitrage spread in basis points |

### Methodology

TIPS-implied risk-free rate:
$$
\text{TIPS-implied RF} = 10000 × (e^{r_{real} + ln(1 + π)} - 1)
$$

Arbitrage spread:
$$
\text{Arb} = \text{TIPS-implied RF} - \text{Nominal Treasury}
$$

### Interpretation

- Positive: TIPS appear cheap relative to nominals
- Negative: TIPS appear expensive

### Data Sources

- Federal Reserve: GSW zero-coupon Treasury and TIPS yields
- Bloomberg: Treasury inflation swaps



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/basis_tips_treas/_data/ftsfr_tips_treasury_basis.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_tips_treasury_basis                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_tips_treasury_basis](basis_tips_treas/ftsfr_tips_treasury_basis.md)                                       |
| Data Sources                   | Federal Reserve, Bloomberg                                        |
| Data Providers                 | Federal Reserve, Bloomberg                                      |
| Links to Providers             | https://federalreserve.gov, https://bloomberg.com                             |
| Topic Tags                     | Tips, Treasury, Arbitrage, Basis, Fixed Income                                          |
| Type of Data Access            | Public,Bloomberg Terminal                                  |
| How is data pulled?            | Fed yields from public source, inflation swaps from Bloomberg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/basis_tips_treas/_data/ftsfr_tips_treasury_basis.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/basis_tips_treas/ftsfr_tips_treasury_basis.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/basis_tips_treas/ftsfr_tips_treasury_basis.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | TIPS-Treasury Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_tips_treas](../pipelines/basis_tips_treas_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_tips_treas                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_tips_treas/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:17:19           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_tips_treas:ftsfr_tips_treasury_basis](../dataframes/basis_tips_treas/ftsfr_tips_treasury_basis.md)<br>  |


