# Dataframe: `basis_treas_sf:ftsfr_treasury_sf_basis` - ftsfr_treasury_sf_basis

## Treasury-SF Basis

Treasury-Secured Financing basis spreads in basis points.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Tenor identifier (e.g., Treasury_SF_2Y, Treasury_SF_10Y) |
| ds | Date |
| y | Basis spread in basis points |

### Methodology

$$
\text{Basis} = (\text{Treasury Yield} - \text{SOFR OIS Rate}) \times 100
$$

### Interpretation

- Basis > 0: Treasuries yield more than SOFR-based financing
- Basis < 0: SOFR-based financing yields more than Treasuries
- Basis = 0: No spread

### Series

Treasury_SF_2Y, Treasury_SF_5Y, Treasury_SF_10Y, Treasury_SF_20Y, Treasury_SF_30Y

### Data Source

Bloomberg Treasury constant maturity yields (USGG series) and SOFR OIS swap rates (USOSFR series)



## DataFrame Glimpse

```
Error reading file: [Errno 2] No such file or directory: '/Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_sf/_data/ftsfr_treasury_sf_basis.parquet'
```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_treasury_sf_basis                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_treasury_sf_basis](../dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.md)                                       |
| Data Sources                   | Bloomberg Treasury Yields, Bloomberg SOFR OIS Rates                                        |
| Data Providers                 | Bloomberg                                      |
| Links to Providers             | https://bloomberg.com                             |
| Topic Tags                     | Treasury, Sofr, Secured Financing, Basis, Fixed Income                                          |
| Type of Data Access            | Bloomberg Terminal                                  |
| How is data pulled?            | Pulled from Bloomberg via xbbg                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_sf/_data/ftsfr_treasury_sf_basis.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/basis_treas_sf/ftsfr_treasury_sf_basis.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/basis_treas_sf/ftsfr_treasury_sf_basis.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Treasury-Secured Financing Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_treas_sf](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_treas_sf                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_sf/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:45:40           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_treas_sf:ftsfr_treasury_sf_basis](../dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.md)<br>  |


