# Dataframe: `wrds_crsp_compustat:ftsfr_CRSP_monthly_stock_ret` - ftsfr_CRSP_monthly_stock_ret

## CRSP Monthly Stock Returns

Monthly stock returns from CRSP (including dividends).

### Columns

| Column | Description |
|--------|-------------|
| unique_id | CRSP PERMNO (permanent security identifier) |
| ds | Month-end date |
| y | Monthly return (including dividends) |

### Data Source

CRSP Monthly Stock File via WRDS (CIZ format)

### Universe

- Common stocks (securitysubtype='COM')
- U.S. incorporated companies (usincflg='Y')
- NYSE, AMEX, NASDAQ exchanges



## DataFrame Glimpse

```
Rows: 3810519
Columns: 3
$ unique_id          <i64> 93436
$ ds        <datetime[ns]> 2024-12-31 00:00:00
$ y                  <f64> 0.170008


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_CRSP_monthly_stock_ret                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_CRSP_monthly_stock_ret](../dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.md)                                       |
| Data Sources                   | CRSP                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Stocks, Returns, Crsp                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS CRSP database                                                    |
| Data available up to (min)     | 2024-12-31 00:00:00                                                             |
| Data available up to (max)     | 2024-12-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/wrds_crsp_compustat/_data/ftsfr_CRSP_monthly_stock_ret.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | WRDS CRSP-Compustat                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [wrds_crsp_compustat](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Tobias Rodriguez del Pozo           |
| Git Repo URL                    | https://github.com/ftsfr/wrds_crsp_compustat                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/wrds_crsp_compustat/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:06:32           |
| OS Compatibility                |  |
| Linked Dataframes               |  [wrds_crsp_compustat:ftsfr_CRSP_monthly_stock_ret](../dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.md)<br>  [wrds_crsp_compustat:ftsfr_CRSP_monthly_stock_retx](../dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_retx.md)<br>  |


