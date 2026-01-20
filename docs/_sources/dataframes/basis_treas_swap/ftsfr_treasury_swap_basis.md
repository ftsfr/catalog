# Dataframe: `basis_treas_swap:ftsfr_treasury_swap_basis` - ftsfr_treasury_swap_basis

## Treasury-Swap Basis

Treasury-Swap arbitrage spreads in basis points.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Tenor identifier (e.g., Arb_Swap_1, Arb_Swap_10) |
| ds | Date |
| y | Basis spread in basis points |

### Methodology

$$
\text{Basis} = (\text{Treasury Yield} - \text{Swap Rate}) \times 100
$$

### Interpretation

- Basis > 0: Treasuries yield more than swaps
- Basis < 0: Swaps yield more than Treasuries
- Basis = 0: No arbitrage opportunity

### Series

Arb_Swap_1, Arb_Swap_2, Arb_Swap_3, Arb_Swap_5, Arb_Swap_10, Arb_Swap_20, Arb_Swap_30

### Data Source

Bloomberg Treasury constant maturity yields (USGG series) and USD swap rates (USSW series)



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_swap/_data/ftsfr_treasury_swap_basis.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_treasury_swap_basis                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_treasury_swap_basis](../dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.md)                                       |
| Data Sources                   | Bloomberg Treasury Yields, Bloomberg Swap Rates                                        |
| Data Providers                 | Bloomberg                                      |
| Links to Providers             | https://bloomberg.com                             |
| Topic Tags                     | Treasury, Swap, Basis, Arbitrage, Fixed Income                                          |
| Type of Data Access            | Bloomberg Terminal                                  |
| How is data pulled?            | Pulled from Bloomberg via xbbg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_swap/_data/ftsfr_treasury_swap_basis.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/basis_treas_swap/ftsfr_treasury_swap_basis.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/basis_treas_swap/ftsfr_treasury_swap_basis.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Treasury-Swap Arbitrage Spreads                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_treas_swap](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_treas_swap                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_swap/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:44:05           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_treas_swap:ftsfr_treasury_swap_basis](../dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.md)<br>  |


