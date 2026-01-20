# Dataframe: `cip:ftsfr_cip_spreads` - ftsfr_cip_spreads

## CIP Deviations

Covered Interest Parity deviations in basis points.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Currency code (e.g., EUR, GBP, JPY) |
| ds | Date |
| y | CIP spread in basis points |

### Methodology

$$
CIP = 10000 × [i_d - (360/90)(ln F - ln S) - i_f]
$$

Where:
- i_d: Domestic (foreign currency) interest rate
- i_f: Foreign (USD) interest rate
- F: 3-month forward rate
- S: Spot rate

### Interpretation

- CIP = 0: No arbitrage (parity holds)
- CIP > 0: Borrowing USD is cheaper
- CIP < 0: Borrowing foreign currency is cheaper

### Currencies

AUD, CAD, CHF, EUR, GBP, JPY, NZD, SEK

### Data Source

Bloomberg FX spot rates, forward points, and OIS interest rates



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/cip/_data/ftsfr_cip_spreads.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cip_spreads                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cip_spreads](../dataframes/cip/ftsfr_cip_spreads.md)                                       |
| Data Sources                   | Bloomberg FX                                        |
| Data Providers                 | Bloomberg                                      |
| Links to Providers             | https://bloomberg.com                             |
| Topic Tags                     | Cip, Foreign Exchange, Arbitrage, Currency                                          |
| Type of Data Access            | Bloomberg Terminal                                  |
| How is data pulled?            | Pulled from Bloomberg via xbbg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/cip/_data/ftsfr_cip_spreads.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/cip/ftsfr_cip_spreads.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/cip/ftsfr_cip_spreads.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Covered Interest Parity Deviations                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cip](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kunj Mehta           |
| Git Repo URL                    | https://github.com/ftsfr/cip                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cip/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:14:58           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cip:ftsfr_cip_spreads](../dataframes/cip/ftsfr_cip_spreads.md)<br>  |


