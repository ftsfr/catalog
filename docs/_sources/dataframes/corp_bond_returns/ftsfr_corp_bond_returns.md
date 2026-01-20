# Dataframe: `corp_bond_returns:ftsfr_corp_bond_returns` - ftsfr_corp_bond_returns

## Individual Corporate Bond Monthly Returns

This dataset contains monthly returns for individual corporate bonds from TRACE data.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Bond CUSIP identifier |
| ds | Month-end date |
| y | Monthly return (value-weighted) |

### Data Source

OpenBondAssetPricing.com (TRACE data with MMN adjustments)

### Time Period

2002 - present



## DataFrame Glimpse

```
Rows: 1859498
Columns: 3
$ unique_id          <cat> N5657TAP1
$ ds        <datetime[ns]> 2025-03-31 00:00:00
$ y                  <f32> 0.03522875905036926


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_corp_bond_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_corp_bond_returns](../dataframes/corp_bond_returns/ftsfr_corp_bond_returns.md)                                       |
| Data Sources                   | OpenBondAssetPricing.com                                        |
| Data Providers                 | OpenBondAssetPricing                                      |
| Links to Providers             | https://openbondassetpricing.com/                             |
| Topic Tags                     | Corporate, Bonds, Returns, Credit                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from OpenBondAssetPricing.com                                                    |
| Data available up to (min)     | 2025-03-31 00:00:00                                                             |
| Data available up to (max)     | 2025-03-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/corp_bond_returns/_data/ftsfr_corp_bond_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/corp_bond_returns/ftsfr_corp_bond_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/corp_bond_returns/ftsfr_corp_bond_returns.xlsx)              |
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


