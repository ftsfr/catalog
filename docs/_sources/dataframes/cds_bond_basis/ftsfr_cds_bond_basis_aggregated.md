# Dataframe: `cds_bond_basis:ftsfr_cds_bond_basis_aggregated` - ftsfr_cds_bond_basis_aggregated

## CDS-Bond Basis (Aggregated)

Measures the implied arbitrage return from CDS and corporate bond markets, aggregated by rating category.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Rating category (Investment Grade, High Yield) |
| ds | Date |
| y | Implied risk-free rate (percent) |

### Methodology

Based on Siriwardane, Sunderam, and Wallen's "Segmented Arbitrage":

CDS Basis:
$$
CB_{i, t, \tau} = CDS_{i, t, \tau} - FR_{i, t, \tau}
$$

Implied Risk-Free Rate:
$$
rfr^{CDS}_{i, t, \tau} = y_{t, \tau} - CB_{i, t, \tau}
$$

### Interpretation

- Negative CB: Investor could earn arbitrage profit by going long bond + buying CDS protection
- Positive rfr indicates positive arbitrage opportunity



## DataFrame Glimpse

```
Rows: 368
Columns: 3
$ unique_id          <str> 'Investment Grade'
$ ds        <datetime[ns]> 2023-11-30 00:00:00
$ y                  <f64> 6.191714845203802


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_bond_basis_aggregated                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_bond_basis_aggregated](../dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.md)                                       |
| Data Sources                   | WRDS Markit, Open Source Bond Asset Pricing                                        |
| Data Providers                 | WRDS, openbondassetpricing.com                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu, https://openbondassetpricing.com                             |
| Topic Tags                     | Cds, Bonds, Arbitrage, Basis, Fixed Income, Credit                                          |
| Type of Data Access            | WRDS,Public                                  |
| How is data pulled?            | Markit CDS from WRDS, bonds from Open Source Bond Asset Pricing                                                    |
| Data available up to (min)     | 2023-11-30 00:00:00                                                             |
| Data available up to (max)     | 2023-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/cds_bond_basis/_data/ftsfr_cds_bond_basis_aggregated.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.xlsx)              |
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


