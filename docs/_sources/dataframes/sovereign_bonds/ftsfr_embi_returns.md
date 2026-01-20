# Dataframe: `sovereign_bonds:ftsfr_embi_returns` - ftsfr_embi_returns

## JP Morgan EMBI Returns

Daily returns for emerging market sovereign bond indices.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Index identifier (e.g., EMBI_Global, EMBI_Brazil) |
| ds | Date |
| y | Daily return (percentage) |

### Methodology

Returns are calculated from total return index levels:

$$
r_t = (P_t / P_{t-1} - 1) \times 100
$$

### Aggregate Indices

- EMBI_Global: JP Morgan EMBI Global Total Return
- EMBI_Global_Diversified: JP Morgan EMBI Global Diversified
- GBI_EM_Composite: Local currency EM bonds
- CEMBI_Corporate: EM corporate bonds

### Country Indices

Brazil, Mexico, Russia, Turkey, South Africa, Indonesia, Colombia, China

### Data Source

Bloomberg JP Morgan EMBI index data



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/sovereign_bonds/_data/ftsfr_embi_returns.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_embi_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_embi_returns](../dataframes/sovereign_bonds/ftsfr_embi_returns.md)                                       |
| Data Sources                   | Bloomberg JP Morgan EMBI                                        |
| Data Providers                 | Bloomberg, JP Morgan                                      |
| Links to Providers             | https://bloomberg.com, https://www.jpmorgan.com                             |
| Topic Tags                     | Sovereign Bonds, Emerging Markets, Embi, Fixed Income, Returns                                          |
| Type of Data Access            | Bloomberg Terminal                                  |
| How is data pulled?            | Pulled from Bloomberg via xbbg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/sovereign_bonds/_data/ftsfr_embi_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/sovereign_bonds/ftsfr_embi_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/sovereign_bonds/ftsfr_embi_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | JP Morgan EMBI Sovereign Bond Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [sovereign_bonds](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/sovereign_bonds                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/sovereign_bonds/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:47:23           |
| OS Compatibility                |  |
| Linked Dataframes               |  [sovereign_bonds:ftsfr_embi_returns](../dataframes/sovereign_bonds/ftsfr_embi_returns.md)<br>  |


