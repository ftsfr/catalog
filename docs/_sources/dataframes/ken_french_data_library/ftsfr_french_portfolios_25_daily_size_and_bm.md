# Dataframe: `ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_bm` - ftsfr_french_portfolios_25_daily_size_and_bm

## Daily Fama-French 25 Portfolios (Size x Book-to-Market)

This dataset contains daily returns for 25 portfolios formed on size and book-to-market.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Portfolio identifier (e.g., "SMALL LoBM", "BIG HiBM") |
| ds | Date |
| y | Daily return (decimal) |

### Portfolio Construction

Portfolios are formed on Size (market equity) and Book-to-Market (book equity / market equity).
5x5 = 25 portfolios at the intersection of 5 size quintiles and 5 B/M quintiles.



## DataFrame Glimpse

```
Rows: 653225
Columns: 3
$ unique_id          <str> 'BIG HiBM'
$ ds        <datetime[ns]> 2025-11-28 00:00:00
$ y                  <f64> 0.024700000000000003


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_french_portfolios_25_daily_size_and_bm                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_french_portfolios_25_daily_size_and_bm](../dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.md)                                       |
| Data Sources                   | ken_french                                        |
| Data Providers                 | Ken French                                      |
| Links to Providers             | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html                             |
| Topic Tags                     | Portfolios, Equity, Factors                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from Ken French Data Library                                                    |
| Data available up to (min)     | 2025-11-28 00:00:00                                                             |
| Data available up to (max)     | 2025-11-28 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/ken_french_data_library/_data/ftsfr_french_portfolios_25_daily_size_and_bm.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Ken French Data Library                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [ken_french_data_library](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/ken_french_data_library                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/ken_french_data_library/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:42:56           |
| OS Compatibility                |  |
| Linked Dataframes               |  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_bm](../dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.md)<br>  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_op](../dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_op.md)<br>  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_inv](../dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_inv.md)<br>  |


