# Dataframe: `commodities:ftsfr_commodities_returns` - ftsfr_commodities_returns

## Commodity Returns

Monthly returns for commodities constructed from GSCI indices and futures data.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Commodity identifier (GSCI ticker with _Return suffix) |
| ds | Date (YYYYMM format) |
| y | Monthly return |

### Methodology

- GSCI excess return indices from Bloomberg
- Returns matched to He-Kelly-Manela commodity factors
- Uses Hungarian algorithm for optimal correlation-based matching

### Commodities Covered

- Energy: Crude Oil, Natural Gas, Heating Oil, Gasoline
- Metals: Gold, Silver, Copper, Aluminum, Nickel, Lead, Zinc
- Agriculture: Corn, Wheat, Soybeans, Sugar, Coffee, Cocoa, Cotton
- Livestock: Lean Hogs, Live Cattle, Feeder Cattle

### Data Sources

- Bloomberg: GSCI indices, commodity futures prices
- WRDS: Futures contract data
- He-Kelly-Manela: Commodity factor reference



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/commodities/_data/ftsfr_commodities_returns.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_commodities_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_commodities_returns](../dataframes/commodities/ftsfr_commodities_returns.md)                                       |
| Data Sources                   | Bloomberg, WRDS, He-Kelly-Manela                                        |
| Data Providers                 | Bloomberg, WRDS, AQR                                      |
| Links to Providers             | https://bloomberg.com, https://wrds-www.wharton.upenn.edu                             |
| Topic Tags                     | Commodities, Futures, Returns, Gsci, Energy, Metals, Agriculture                                          |
| Type of Data Access            | Bloomberg Terminal,WRDS,Public                                  |
| How is data pulled?            | GSCI indices from Bloomberg, matched to HKM commodity factors                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/commodities/_data/ftsfr_commodities_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/commodities/ftsfr_commodities_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/commodities/ftsfr_commodities_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Commodities                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [commodities](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/commodities                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/commodities/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:02:46           |
| OS Compatibility                |  |
| Linked Dataframes               |  [commodities:ftsfr_commodities_returns](../dataframes/commodities/ftsfr_commodities_returns.md)<br>  |


