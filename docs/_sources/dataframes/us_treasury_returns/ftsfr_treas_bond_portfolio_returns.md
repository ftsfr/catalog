# Dataframe: `us_treasury_returns:ftsfr_treas_bond_portfolio_returns` - ftsfr_treas_bond_portfolio_returns

## Treasury Bond Portfolio Returns

This dataset contains portfolio returns grouped by maturity buckets.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Maturity group (1-10, representing 6-month intervals from 0-5 years) |
| ds | Month-end date |
| y | Average monthly return for the maturity group |

### Maturity Groups

| Group | Maturity Range |
|-------|----------------|
| 1 | 0 to 6 months |
| 2 | 6 months to 1 year |
| 3 | 1 year to 1.5 years |
| 4 | 1.5 to 2 years |
| 5 | 2 to 2.5 years |
| 6 | 2.5 to 3 years |
| 7 | 3 to 3.5 years |
| 8 | 3.5 to 4 years |
| 9 | 4 to 4.5 years |
| 10 | 4.5 to 5 years |

### Data Source

CRSP US Treasury Database via WRDS



## DataFrame Glimpse

```
Rows: 6689
Columns: 3
$ unique_id          <str> '10'
$ ds        <datetime[ns]> 2025-11-30 00:00:00
$ y                  <f64> 0.007496000431622939


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_treas_bond_portfolio_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_treas_bond_portfolio_returns](../dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.md)                                       |
| Data Sources                   | CRSP Treasury Database                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Treasury, Bonds, Portfolios, Returns                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS CRSP Treasury Database                                                    |
| Data available up to (min)     | 2025-11-30 00:00:00                                                             |
| Data available up to (max)     | 2025-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/us_treasury_returns/_data/ftsfr_treas_bond_portfolio_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | US Treasury Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [us_treasury_returns](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/us_treasury_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/us_treasury_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:00:02           |
| OS Compatibility                |  |
| Linked Dataframes               |  [us_treasury_returns:ftsfr_treas_bond_returns](../dataframes/us_treasury_returns/ftsfr_treas_bond_returns.md)<br>  [us_treasury_returns:ftsfr_treas_bond_portfolio_returns](../dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.md)<br>  |


