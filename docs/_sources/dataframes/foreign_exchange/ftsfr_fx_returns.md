# Dataframe: `foreign_exchange:ftsfr_fx_returns` - ftsfr_fx_returns

## Foreign Exchange Returns

Daily returns for USD invested in foreign currencies via overnight repo markets.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Currency identifier (e.g., EUR_return) |
| ds | Date |
| y | Daily annualized return (percent) |

### Methodology

$$
ret_{t,i} = (spot_{t-1,i} / spot_{t,i}) × fret_{t,i}
$$

Where:
- spot: Exchange rate (how much 1 USD is worth in foreign currency)
- fret: Foreign currency return in overnight repo market

### Currencies

AUD, CAD, CHF, EUR, GBP, JPY, NZD, SEK, USD

### Data Source

Bloomberg FX spot rates and OIS interest rates



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/foreign_exchange/_data/ftsfr_fx_returns.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_fx_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_fx_returns](../dataframes/foreign_exchange/ftsfr_fx_returns.md)                                       |
| Data Sources                   | Bloomberg FX                                        |
| Data Providers                 | Bloomberg                                      |
| Links to Providers             | https://bloomberg.com                             |
| Topic Tags                     | Fx, Foreign Exchange, Currency, Returns                                          |
| Type of Data Access            | Bloomberg Terminal                                  |
| How is data pulled?            | Pulled from Bloomberg via xbbg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/foreign_exchange/_data/ftsfr_fx_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/foreign_exchange/ftsfr_fx_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/foreign_exchange/ftsfr_fx_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Foreign Exchange Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [foreign_exchange](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kunj Mehta           |
| Git Repo URL                    | https://github.com/ftsfr/foreign_exchange                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/foreign_exchange/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:12:35           |
| OS Compatibility                |  |
| Linked Dataframes               |  [foreign_exchange:ftsfr_fx_returns](../dataframes/foreign_exchange/ftsfr_fx_returns.md)<br>  |


