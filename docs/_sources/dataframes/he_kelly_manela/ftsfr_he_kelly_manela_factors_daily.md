# Dataframe: `he_kelly_manela:ftsfr_he_kelly_manela_factors_daily` - ftsfr_he_kelly_manela_factors_daily

## Daily Intermediary Capital Risk Factors

This dataset contains daily observations of the intermediary capital risk factors from He, Kelly, and Manela (2017).

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Factor identifier |
| ds | Date |
| y | Factor value |

### Factors

- `intermediary_capital_ratio`: Capital ratio of primary dealers
- `intermediary_capital_risk_factor`: Innovation in capital ratio (the risk factor)
- `intermediary_value_weighted_investment_return`: Value-weighted investment return
- `intermediary_leverage_ratio_squared`: Squared leverage ratio



## DataFrame Glimpse

```
Rows: 19063
Columns: 3
$ unique_id          <str> 'intermediary_leverage_ratio_squared'
$ ds        <datetime[ns]> 2018-12-11 00:00:00
$ y                  <f64> 239.92717840644252


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_he_kelly_manela_factors_daily                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_he_kelly_manela_factors_daily](../dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.md)                                       |
| Data Sources                   | he_kelly_manela                                        |
| Data Providers                 | Asaf Manela                                      |
| Links to Providers             | https://asaf.manela.org/papers/hkm/intermediarycapitalrisk/                             |
| Topic Tags                     | Factors, Intermediary, Capital                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from Asaf Manela's website                                                    |
| Data available up to (min)     | 2018-12-11 00:00:00                                                             |
| Data available up to (max)     | 2018-12-11 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/he_kelly_manela/_data/ftsfr_he_kelly_manela_factors_daily.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | He-Kelly-Manela Factors                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [he_kelly_manela](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/he_kelly_manela                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/he_kelly_manela/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:40:48           |
| OS Compatibility                |  |
| Linked Dataframes               |  [he_kelly_manela:ftsfr_he_kelly_manela_factors_monthly](../dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_monthly.md)<br>  [he_kelly_manela:ftsfr_he_kelly_manela_factors_daily](../dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.md)<br>  [he_kelly_manela:ftsfr_he_kelly_manela_all](../dataframes/he_kelly_manela/ftsfr_he_kelly_manela_all.md)<br>  |


