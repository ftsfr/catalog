# Dataframe: `us_treasury_returns:ftsfr_treas_bond_returns` - ftsfr_treas_bond_returns

## Individual Treasury Bond Monthly Returns

This dataset contains monthly returns for individual Treasury bonds.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Treasury record identifier (kytreasno) |
| ds | Month-end date |
| y | Monthly return (compounded from daily returns) |

### Data Source

CRSP US Treasury Database via WRDS

### Time Period

1970 - present (quarterly updates)



## DataFrame Glimpse

```
Rows: 122886
Columns: 3
$ unique_id          <f64> 208490.0
$ ds        <datetime[ns]> 2025-11-30 00:00:00
$ y                  <f64> 0.00914946210717571


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_treas_bond_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_treas_bond_returns](../dataframes/us_treasury_returns/ftsfr_treas_bond_returns.md)                                       |
| Data Sources                   | CRSP Treasury Database                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Treasury, Bonds, Returns                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS CRSP Treasury Database                                                    |
| Data available up to (min)     | 2025-11-30 00:00:00                                                             |
| Data available up to (max)     | 2025-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/us_treasury_returns/_data/ftsfr_treas_bond_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/us_treasury_returns/ftsfr_treas_bond_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/us_treasury_returns/ftsfr_treas_bond_returns.xlsx)              |
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


