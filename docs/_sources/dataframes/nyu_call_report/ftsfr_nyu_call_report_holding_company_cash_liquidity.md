# Dataframe: `nyu_call_report:ftsfr_nyu_call_report_holding_company_cash_liquidity` - ftsfr_nyu_call_report_holding_company_cash_liquidity

## Holding Company Cash Liquidity

Quarterly cash liquidity ratios aggregated at the bank holding company level.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Bank holding company identifier (BHC ID) |
| ds | Date |
| y | Cash liquidity ratio (Cash/Assets) |



## DataFrame Glimpse

```
Rows: 832902
Columns: 3
$ unique_id          <str> '962742'
$ ds        <datetime[ns]> 1982-03-31 00:00:00
$ y                  <f64> 0.034363177805800754


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_nyu_call_report_holding_company_cash_liquidity                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_nyu_call_report_holding_company_cash_liquidity](../dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.md)                                       |
| Data Sources                   | nyu_call_report                                        |
| Data Providers                 | NYU Stern                                      |
| Links to Providers             | https://pages.stern.nyu.edu/~pschnabl/data/data_callreport.htm                             |
| Topic Tags                     | Banking, Liquidity, Regulation                                          |
| Type of Data Access            | Public                                  |
| How is data pulled?            | Downloaded from NYU Stern website                                                    |
| Data available up to (min)     | 2020-03-31 00:00:00                                                             |
| Data available up to (max)     | 2020-03-31 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/nyu_call_report/_data/ftsfr_nyu_call_report_holding_company_cash_liquidity.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | NYU Call Report                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [nyu_call_report](../index.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/nyu_call_report                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/nyu_call_report/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 19:39:13           |
| OS Compatibility                |  |
| Linked Dataframes               |  [nyu_call_report:ftsfr_nyu_call_report_leverage](../dataframes/nyu_call_report/ftsfr_nyu_call_report_leverage.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_holding_company_leverage](../dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_leverage.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_cash_liquidity](../dataframes/nyu_call_report/ftsfr_nyu_call_report_cash_liquidity.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_holding_company_cash_liquidity](../dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.md)<br>  |


