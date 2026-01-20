# Dataframe: `cds_returns:ftsfr_cds_portfolio_returns` - ftsfr_cds_portfolio_returns

## CDS Portfolio Returns

Monthly CDS portfolio returns calculated following He, Kelly, and Manela (2017) methodology.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Portfolio identifier (e.g., 5Y_Q1 = 5-year tenor, quintile 1) |
| ds | Month-end date |
| y | Monthly scaled return |

### Portfolio Construction

- 20 portfolios = 4 tenors (3Y, 5Y, 7Y, 10Y) × 5 credit quintiles
- Credit quintiles based on 5Y spreads: Q1 (safest) to Q5 (riskiest)
- Returns scaled to match 5Y volatility within each quintile

### Return Formula

$$
CDS Return_t = CDS_{t-1}/250 + ΔCDS_t × RD_{t-1}
$$

Where:
- First term: Carry return (daily accrual from previous spread)
- Second term: Spread change × Risky duration

### Data Source

WRDS Markit CDS data (USD contracts, XR restructuring clause, CompositeDepth5Y >= 3)



## DataFrame Glimpse

```
Rows: 5510
Columns: 3
$ unique_id          <str> '7Y_Q5'
$ ds        <datetime[ns]> 2023-12-01 00:00:00
$ y                  <f64> 0.004189412738562569


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_portfolio_returns                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_portfolio_returns](../dataframes/cds_returns/ftsfr_cds_portfolio_returns.md)                                       |
| Data Sources                   | Markit CDS                                        |
| Data Providers                 | WRDS                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu/                             |
| Topic Tags                     | Cds, Credit, Returns, Fixed Income                                          |
| Type of Data Access            | WRDS Subscription                                  |
| How is data pulled?            | Pulled from WRDS Markit CDS database                                                    |
| Data available up to (min)     | 2023-12-01 00:00:00                                                             |
| Data available up to (max)     | 2023-12-01 00:00:00                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/ftsfr_repos/cds_returns/_data/ftsfr_cds_portfolio_returns.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/cds_returns/ftsfr_cds_portfolio_returns.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/cds_returns/ftsfr_cds_portfolio_returns.xlsx)              |
| Linked Charts                  |  None  |

## Pipeline Manifest

| Pipeline Name                   | CDS Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cds_returns](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kausthub Kesheva           |
| Git Repo URL                    | https://github.com/ftsfr/cds_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cds_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:36:24           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cds_returns:ftsfr_cds_portfolio_returns](../dataframes/cds_returns/ftsfr_cds_portfolio_returns.md)<br>  [cds_returns:ftsfr_cds_contract_returns](../dataframes/cds_returns/ftsfr_cds_contract_returns.md)<br>  |


