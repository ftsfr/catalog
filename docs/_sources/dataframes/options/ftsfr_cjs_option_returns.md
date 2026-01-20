# Dataframe: `options:ftsfr_cjs_option_returns` - ftsfr_cjs_option_returns

## CJS Option Portfolio Returns

Monthly leverage-adjusted returns for 54 SPX option portfolios following Constantinides, Jackwerth, Savov (2013).

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Portfolio identifier (e.g., cjs_C_1000_30 = call, ATM, 30-day) |
| ds | Month-end date |
| y | Monthly leverage-adjusted return |

### Portfolio Construction

- 54 portfolios = 9 moneyness x 3 maturities x 2 option types
- Moneyness: 0.90, 0.925, 0.95, 0.975, 1.0, 1.025, 1.05, 1.075, 1.10
- Maturities: 30, 60, 90 days

### Data Filtration

Following CJS (2013) Appendix B:
- Level 1: Remove duplicates, zero bids
- Level 2: DTM 7-180 days, IV 5-100%, moneyness 0.8-1.2
- Level 3: IV outlier filter, put-call parity filter

### Data Source

WRDS OptionMetrics (SPX options, secid=108105)



## DataFrame Glimpse

```
Rows: 15552
Columns: 3
$ unique_id          <str> 'cjs_P_975_90'
$ ds        <datetime[ns]> 2019-12-31 00:00:00
$ y                  <f64> 0.009070683609718522


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cjs_option_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cjs_option_returns](../dataframes/options/ftsfr_cjs_option_returns.md)                                       |
| Data Sources                   | OptionMetrics                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Options, Spx, Returns, Cjs                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS OptionMetrics database                                                    |
| Data available up to (min)     | 2019-12-31 00:00:00                                                             |
| Data available up to (max)     | 2019-12-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/options/_data/ftsfr_cjs_option_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/options/ftsfr_cjs_option_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/options/ftsfr_cjs_option_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | SPX Options                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [options](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Tobias Rodriguez del Pozo           |
| Git Repo URL                    | https://github.com/ftsfr/options                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/options/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 20:48:56           |
| OS Compatibility                |  |
| Linked Dataframes               |  [options:ftsfr_hkm_option_returns](../dataframes/options/ftsfr_hkm_option_returns.md)<br>  [options:ftsfr_cjs_option_returns](../dataframes/options/ftsfr_cjs_option_returns.md)<br>  |


