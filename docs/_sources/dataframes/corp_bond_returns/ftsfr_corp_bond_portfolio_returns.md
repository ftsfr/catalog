# Dataframe: `corp_bond_returns:ftsfr_corp_bond_portfolio_returns` - ftsfr_corp_bond_portfolio_returns

## Corporate Bond Portfolio Returns

This dataset contains portfolio returns grouped by credit spread deciles.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Credit spread decile (1-10) |
| ds | Month-end date |
| y | Value-weighted monthly return for the decile |

### Credit Spread Deciles

| Decile | Description |
|--------|-------------|
| 1 | Lowest credit spread (safest bonds) |
| 2-9 | Intermediate credit spreads |
| 10 | Highest credit spread (riskiest bonds) |

### Data Source

OpenBondAssetPricing.com (TRACE data with MMN adjustments)



## DataFrame Glimpse

```
Rows: 2690
Columns: 3
$ unique_id          <f64> 10.0
$ ds        <datetime[ns]> 2024-12-31 00:00:00
$ y                  <f32> -0.006980137899518013


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_corp_bond_portfolio_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_corp_bond_portfolio_returns](../dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.md)                                       |
| Data Sources                   | OpenBondAssetPricing.com                                        |
| Data Providers                 | OpenBondAssetPricing                                      |
| Links to Providers             | https://openbondassetpricing.com/                             |
| Topic Tags                     | Corporate, Bonds, Portfolios, Returns, Credit                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from OpenBondAssetPricing.com                                                    |
| Data available up to (min)     | 2024-12-31 00:00:00                                                             |
| Data available up to (max)     | 2024-12-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/corp_bond_returns/_data/ftsfr_corp_bond_portfolio_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Corporate Bond Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [corp_bond_returns](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/corp_bond_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/corp_bond_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 20:11:41           |
| OS Compatibility                |  |
| Linked Dataframes               |  [corp_bond_returns:ftsfr_corp_bond_returns](../dataframes/corp_bond_returns/ftsfr_corp_bond_returns.md)<br>  [corp_bond_returns:ftsfr_corp_bond_portfolio_returns](../dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.md)<br>  |


