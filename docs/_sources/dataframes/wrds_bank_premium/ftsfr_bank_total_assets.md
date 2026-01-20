# Dataframe: `wrds_bank_premium:ftsfr_bank_total_assets` - ftsfr_bank_total_assets

## Bank Total Assets

Time series of bank total assets from WRDS Call Report Research data.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Bank RSSD ID |
| ds | Date |
| y | Total assets (bhck2170, in thousands) |

### Source Tables

This pipeline also provides access to:
- wrds_struct_rel_ultimate: Ultimate parent structure
- wrds_call_research: Full call report data
- wrds_bank_crsp_link: Bank to CRSP linkage
- idrssd_to_lei: RSSD to LEI mapping
- lei_main: Legal Entity Identifier data



## DataFrame Glimpse

```
Rows: 1999371
Columns: 3
$ unique_id          <str> '999944'
$ ds        <datetime[ns]> 1993-09-30 00:00:00
$ y                  <f64> 176598.0


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_bank_total_assets                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_bank_total_assets](../dataframes/wrds_bank_premium/ftsfr_bank_total_assets.md)                                       |
| Data Sources                   | WRDS Bank Regulatory Premium                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu                             |
| Topic Tags                     | Banks, Regulatory, Call Reports, Total Assets                                          |
| Type of Data Access            | WRDS                                  |
| How is data pulled?            | WRDS Bank Regulatory Premium database                                                    |
| Data available up to (min)     | 2024-03-31 00:00:00                                                             |
| Data available up to (max)     | 2024-03-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/wrds_bank_premium/_data/ftsfr_bank_total_assets.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/wrds_bank_premium/ftsfr_bank_total_assets.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/wrds_bank_premium/ftsfr_bank_total_assets.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | WRDS Bank Regulatory Premium                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [wrds_bank_premium](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/wrds_bank_premium                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/wrds_bank_premium/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 00:05:52           |
| OS Compatibility                |  |
| Linked Dataframes               |  [wrds_bank_premium:ftsfr_bank_total_assets](../dataframes/wrds_bank_premium/ftsfr_bank_total_assets.md)<br>  |


