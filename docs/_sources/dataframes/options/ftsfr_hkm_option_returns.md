# Dataframe: `options:ftsfr_hkm_option_returns` - ftsfr_hkm_option_returns

## HKM Option Portfolio Returns

Monthly leverage-adjusted returns for 18 SPX option portfolios following He, Kelly, Manela (2017).

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Portfolio identifier (e.g., hkm_C_1000 = call, ATM) |
| ds | Month-end date |
| y | Monthly leverage-adjusted return |

### Portfolio Construction

- 18 portfolios = 9 moneyness levels x 2 option types (call/put)
- Moneyness: 0.90, 0.925, 0.95, 0.975, 1.0, 1.025, 1.05, 1.075, 1.10
- Returns averaged across 30, 60, 90-day maturities

### Data Source

WRDS OptionMetrics (SPX options, secid=108105)



## DataFrame Glimpse

```
Rows: 5184
Columns: 3
$ unique_id          <str> 'hkm_P_975'
$ ds        <datetime[ns]> 2019-12-31 00:00:00
$ y                  <f64> 0.008315441172204544


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_hkm_option_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_hkm_option_returns](../dataframes/options/ftsfr_hkm_option_returns.md)                                       |
| Data Sources                   | OptionMetrics                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Options, Spx, Returns, Hkm                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS OptionMetrics database                                                    |
| Data available up to (min)     | 2019-12-31 00:00:00                                                             |
| Data available up to (max)     | 2019-12-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/options/_data/ftsfr_hkm_option_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/options/ftsfr_hkm_option_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/options/ftsfr_hkm_option_returns.xlsx)              |
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


