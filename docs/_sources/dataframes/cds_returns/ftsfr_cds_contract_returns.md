# Dataframe: `cds_returns:ftsfr_cds_contract_returns` - ftsfr_cds_contract_returns

## CDS Contract Returns

Monthly returns for individual CDS contracts.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Contract identifier (ticker_tenor, e.g., AAPL_5Y) |
| ds | Month-end date |
| y | Monthly return |

### Return Calculation

Returns calculated using the He-Kelly formula at the individual contract level,
then aggregated to monthly frequency.

### Data Source

WRDS Markit CDS data (USD contracts, XR restructuring clause)



## DataFrame Glimpse

```
Rows: 201830
Columns: 3
$ unique_id          <str> 'ZIMMBIO_7Y'
$ ds        <datetime[ns]> 2019-01-01 00:00:00
$ y                  <f64> 0.0020013903135542854


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_contract_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_contract_returns](../dataframes/cds_returns/ftsfr_cds_contract_returns.md)                                       |
| Data Sources                   | Markit CDS                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Cds, Credit, Returns, Fixed Income                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS Markit CDS database                                                    |
| Data available up to (min)     | 2023-12-01 00:00:00                                                             |
| Data available up to (max)     | 2023-12-01 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/cds_returns/_data/ftsfr_cds_contract_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/cds_returns/ftsfr_cds_contract_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/cds_returns/ftsfr_cds_contract_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | CDS Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cds_returns](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kausthub Kesheva           |
| Git Repo URL                    | https://github.com/ftsfr/cds_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cds_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:36:24           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cds_returns:ftsfr_cds_portfolio_returns](../dataframes/cds_returns/ftsfr_cds_portfolio_returns.md)<br>  [cds_returns:ftsfr_cds_contract_returns](../dataframes/cds_returns/ftsfr_cds_contract_returns.md)<br>  |


