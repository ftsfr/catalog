# Dataframe: `cds_bond_basis:ftsfr_cds_bond_basis_non_aggregated` - ftsfr_cds_bond_basis_non_aggregated

## CDS-Bond Basis (Non-Aggregated)

Bond-level implied arbitrage returns from CDS and corporate bond markets.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Bond CUSIP |
| ds | Date |
| y | Implied risk-free rate (percent) |

### Data Sources

- Markit CDS data from WRDS
- Corporate bond data from Open Source Bond Asset Pricing (openbondassetpricing.com)



## DataFrame Glimpse

```
Rows: 532356
Columns: 3
$ unique_id          <cat> 988498AR2
$ ds        <datetime[ns]> 2023-11-30 00:00:00
$ y                  <f64> 4.7417995836925755


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_bond_basis_non_aggregated                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_bond_basis_non_aggregated](../dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.md)                                       |
| Data Sources                   | WRDS Markit, Open Source Bond Asset Pricing                                        |
| Data Providers                 | WRDS, openbondassetpricing.com                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu, https://openbondassetpricing.com                             |
| Topic Tags                     | Cds, Bonds, Arbitrage, Basis, Fixed Income, Credit                                          |
| Type of Data Access            | WRDS,Public                                  |
| How is data pulled?            | Markit CDS from WRDS, bonds from Open Source Bond Asset Pricing                                                    |
| Data available up to (min)     | 2023-11-30 00:00:00                                                             |
| Data available up to (max)     | 2023-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/cds_bond_basis/_data/ftsfr_cds_bond_basis_non_aggregated.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | CDS-Bond Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cds_bond_basis](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Alex Wang, Kausthub Kesheva, Vincent Xu           |
| Git Repo URL                    | https://github.com/ftsfr/cds_bond_basis                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cds_bond_basis/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 23:28:28           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cds_bond_basis:ftsfr_cds_bond_basis_aggregated](../dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.md)<br>  [cds_bond_basis:ftsfr_cds_bond_basis_non_aggregated](../dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.md)<br>  |


