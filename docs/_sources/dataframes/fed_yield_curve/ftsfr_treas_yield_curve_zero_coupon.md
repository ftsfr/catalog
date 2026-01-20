# Dataframe: `fed_yield_curve:ftsfr_treas_yield_curve_zero_coupon` - ftsfr_treas_yield_curve_zero_coupon

## Treasury Zero-Coupon Yield Curve

This dataset contains daily zero-coupon Treasury yields estimated using the
Gurkaynak, Sack, and Wright (2007) model.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Tenor identifier (e.g., SVENY01 = 1 year, SVENY10 = 10 years) |
| ds | Date |
| y | Yield (%) |

### Tenors

Yields are available for maturities from 1 to 30 years (SVENY01 to SVENY30).

### Reference

Gurkaynak, Refet S., Brian Sack, and Jonathan H. Wright. "The US Treasury yield curve: 1961 to the present."
Journal of Monetary Economics 54.8 (2007): 2291-2304.



## DataFrame Glimpse

```
Rows: 376712
Columns: 4
$ unique_id                  <str> 'SVENY30'
$ ds                <datetime[ns]> 2026-01-09 00:00:00
$ y                          <f64> 5.0315
$ __index_level_0__          <i64> 505439


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_treas_yield_curve_zero_coupon                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_treas_yield_curve_zero_coupon](../dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.md)                                       |
| Data Sources                   | federal_reserve                                        |
| Data Providers                 | Federal Reserve                                      |
| Links to Providers             | https://www.federalreserve.gov/data/nominal-yield-curve.htm                             |
| Topic Tags                     | Yield_Curve, Treasury, Interest_Rates                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from Federal Reserve website                                                    |
| Data available up to (min)     | 2026-01-09 00:00:00                                                             |
| Data available up to (max)     | 2026-01-09 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/fed_yield_curve/_data/ftsfr_treas_yield_curve_zero_coupon.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | Federal Reserve Yield Curve                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [fed_yield_curve](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/fed_yield_curve                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/fed_yield_curve/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:45:25           |
| OS Compatibility                |  |
| Linked Dataframes               |  [fed_yield_curve:ftsfr_treas_yield_curve_zero_coupon](../dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.md)<br>  |


