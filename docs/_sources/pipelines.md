# Pipelines 🔌

```{toctree}
:maxdepth: 1

pipelines/basis_tips_treas_README.md

pipelines/basis_treas_sf_README.md

pipelines/basis_treas_swap_README.md

pipelines/cds_bond_basis_README.md

pipelines/cds_returns_README.md

pipelines/cip_README.md

pipelines/commodities_README.md

pipelines/corp_bond_returns_README.md

pipelines/crsp_treasury_README.md

pipelines/fed_yield_curve_README.md

pipelines/foreign_exchange_README.md

pipelines/he_kelly_manela_README.md

pipelines/ken_french_data_library_README.md

pipelines/nyu_call_report_README.md

pipelines/options_README.md

pipelines/sovereign_bonds_README.md

pipelines/us_treasury_returns_README.md

pipelines/wrds_bank_premium_README.md

pipelines/wrds_crsp_compustat_README.md

```


  
  

## TIPS-Treasury Basis

TIPS-Treasury arbitrage spread measuring relative value between TIPS and nominal Treasuries

  
  | Pipeline Name                   | TIPS-Treasury Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_tips_treas](./pipelines/basis_tips_treas_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_tips_treas                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_tips_treas/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:17:19           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_tips_treas:ftsfr_tips_treasury_basis](./dataframes/basis_tips_treas/ftsfr_tips_treasury_basis.md)<br>  |




  
  

## Treasury-Secured Financing Basis

Treasury-SF basis measuring the spread between Treasury yields and SOFR-based secured financing rates

  
  | Pipeline Name                   | Treasury-Secured Financing Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_treas_sf](./pipelines/basis_treas_sf_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_treas_sf                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_sf/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:45:40           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_treas_sf:ftsfr_treasury_sf_basis](./dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.md)<br>  |




  
  

## Treasury-Swap Arbitrage Spreads

Treasury-Swap basis measuring arbitrage opportunities between Treasury yields and swap rates

  
  | Pipeline Name                   | Treasury-Swap Arbitrage Spreads                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [basis_treas_swap](./pipelines/basis_treas_swap_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/basis_treas_swap                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/basis_treas_swap/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:44:05           |
| OS Compatibility                |  |
| Linked Dataframes               |  [basis_treas_swap:ftsfr_treasury_swap_basis](./dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.md)<br>  |




  
  

## CDS-Bond Basis

CDS-Bond basis measuring implied arbitrage returns from the CDS and corporate bond markets

  
  | Pipeline Name                   | CDS-Bond Basis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cds_bond_basis](./pipelines/cds_bond_basis_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Alex Wang, Kausthub Kesheva, Vincent Xu           |
| Git Repo URL                    | https://github.com/ftsfr/cds_bond_basis                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cds_bond_basis/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 23:28:28           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cds_bond_basis:ftsfr_cds_bond_basis_aggregated](./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.md)<br>  [cds_bond_basis:ftsfr_cds_bond_basis_non_aggregated](./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.md)<br>  |




  
  

## CDS Returns

Monthly CDS portfolio returns following He, Kelly, and Manela (2017) methodology

  
  | Pipeline Name                   | CDS Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cds_returns](./pipelines/cds_returns_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kausthub Kesheva           |
| Git Repo URL                    | https://github.com/ftsfr/cds_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cds_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:36:24           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cds_returns:ftsfr_cds_portfolio_returns](./dataframes/cds_returns/ftsfr_cds_portfolio_returns.md)<br>  [cds_returns:ftsfr_cds_contract_returns](./dataframes/cds_returns/ftsfr_cds_contract_returns.md)<br>  |




  
  

## Covered Interest Parity Deviations

CIP deviations measuring arbitrage opportunities in currency markets

  
  | Pipeline Name                   | Covered Interest Parity Deviations                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [cip](./pipelines/cip_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kunj Mehta           |
| Git Repo URL                    | https://github.com/ftsfr/cip                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/cip/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:14:58           |
| OS Compatibility                |  |
| Linked Dataframes               |  [cip:ftsfr_cip_spreads](./dataframes/cip/ftsfr_cip_spreads.md)<br>  |




  
  

## Commodities

Commodity futures returns and basis data from Bloomberg and WRDS

  
  | Pipeline Name                   | Commodities                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [commodities](./pipelines/commodities_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/commodities                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/commodities/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:02:46           |
| OS Compatibility                |  |
| Linked Dataframes               |  [commodities:ftsfr_commodities_returns](./dataframes/commodities/ftsfr_commodities_returns.md)<br>  |




  
  

## Corporate Bond Returns

Corporate bond returns from OpenBondAssetPricing.com (TRACE data), including individual bond returns and credit spread-sorted portfolios

  
  | Pipeline Name                   | Corporate Bond Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [corp_bond_returns](./pipelines/corp_bond_returns_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/corp_bond_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/corp_bond_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 20:11:41           |
| OS Compatibility                |  |
| Linked Dataframes               |  [corp_bond_returns:ftsfr_corp_bond_returns](./dataframes/corp_bond_returns/ftsfr_corp_bond_returns.md)<br>  [corp_bond_returns:ftsfr_corp_bond_portfolio_returns](./dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.md)<br>  |




  
  

## CRSP Treasury

Treasury Securities Data from CRSP

  
  | Pipeline Name                   | CRSP Treasury                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [crsp_treasury](./pipelines/crsp_treasury_README.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/crsp_treasury                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/crsp_treasury/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:10:38           |
| OS Compatibility                |  |
| Linked Dataframes               |  [crsp_treasury:crsp_treasury_daily](./dataframes/crsp_treasury/crsp_treasury_daily.md)<br>  [crsp_treasury:treasury_auctions](./dataframes/crsp_treasury/treasury_auctions.md)<br>  |




  
  

## Federal Reserve Yield Curve

Treasury Zero-Coupon Yield Curve from the Federal Reserve

  
  | Pipeline Name                   | Federal Reserve Yield Curve                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [fed_yield_curve](./pipelines/fed_yield_curve_README.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/fed_yield_curve                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/fed_yield_curve/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:45:25           |
| OS Compatibility                |  |
| Linked Dataframes               |  [fed_yield_curve:ftsfr_treas_yield_curve_zero_coupon](./dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.md)<br>  |




  
  

## Foreign Exchange Returns

Daily FX returns for USD invested in foreign currencies via overnight repo markets

  
  | Pipeline Name                   | Foreign Exchange Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [foreign_exchange](./pipelines/foreign_exchange_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Kunj Mehta           |
| Git Repo URL                    | https://github.com/ftsfr/foreign_exchange                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/foreign_exchange/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:12:35           |
| OS Compatibility                |  |
| Linked Dataframes               |  [foreign_exchange:ftsfr_fx_returns](./dataframes/foreign_exchange/ftsfr_fx_returns.md)<br>  |




  
  

## He-Kelly-Manela Factors

Intermediary Capital Risk Factors from He, Kelly, and Manela (2017)

  
  | Pipeline Name                   | He-Kelly-Manela Factors                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [he_kelly_manela](./pipelines/he_kelly_manela_README.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/he_kelly_manela                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/he_kelly_manela/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:40:48           |
| OS Compatibility                |  |
| Linked Dataframes               |  [he_kelly_manela:ftsfr_he_kelly_manela_factors_monthly](./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_monthly.md)<br>  [he_kelly_manela:ftsfr_he_kelly_manela_factors_daily](./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.md)<br>  [he_kelly_manela:ftsfr_he_kelly_manela_all](./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_all.md)<br>  |




  
  

## Ken French Data Library

Fama-French 25 Portfolios sorted by Size and various characteristics

  
  | Pipeline Name                   | Ken French Data Library                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [ken_french_data_library](./pipelines/ken_french_data_library_README.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/ken_french_data_library                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/ken_french_data_library/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 18:42:56           |
| OS Compatibility                |  |
| Linked Dataframes               |  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_bm](./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.md)<br>  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_op](./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_op.md)<br>  [ken_french_data_library:ftsfr_french_portfolios_25_daily_size_and_inv](./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_inv.md)<br>  |




  
  

## NYU Call Report

Bank-level leverage and liquidity metrics from regulatory call reports

  
  | Pipeline Name                   | NYU Call Report                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [nyu_call_report](./pipelines/nyu_call_report_README.md)              |
| Lead Pipeline Developer         | Jeremiah Bejarano             |
| Contributors                    | Jeremiah Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/nyu_call_report                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/nyu_call_report/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 19:39:13           |
| OS Compatibility                |  |
| Linked Dataframes               |  [nyu_call_report:ftsfr_nyu_call_report_leverage](./dataframes/nyu_call_report/ftsfr_nyu_call_report_leverage.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_holding_company_leverage](./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_leverage.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_cash_liquidity](./dataframes/nyu_call_report/ftsfr_nyu_call_report_cash_liquidity.md)<br>  [nyu_call_report:ftsfr_nyu_call_report_holding_company_cash_liquidity](./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.md)<br>  |




  
  

## SPX Options

Leverage-adjusted SPX option portfolio returns following CJS (2013) and HKM (2017)

  
  | Pipeline Name                   | SPX Options                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [options](./pipelines/options_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Tobias Rodriguez del Pozo           |
| Git Repo URL                    | https://github.com/ftsfr/options                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/options/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 20:48:56           |
| OS Compatibility                |  |
| Linked Dataframes               |  [options:ftsfr_hkm_option_returns](./dataframes/options/ftsfr_hkm_option_returns.md)<br>  [options:ftsfr_cjs_option_returns](./dataframes/options/ftsfr_cjs_option_returns.md)<br>  |




  
  

## JP Morgan EMBI Sovereign Bond Returns

Emerging market sovereign bond returns from JP Morgan EMBI indices

  
  | Pipeline Name                   | JP Morgan EMBI Sovereign Bond Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [sovereign_bonds](./pipelines/sovereign_bonds_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/sovereign_bonds                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/sovereign_bonds/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-16 22:47:23           |
| OS Compatibility                |  |
| Linked Dataframes               |  [sovereign_bonds:ftsfr_embi_returns](./dataframes/sovereign_bonds/ftsfr_embi_returns.md)<br>  |




  
  

## US Treasury Returns

Treasury bond returns from CRSP, including individual bond returns, maturity-sorted portfolios, and auction statistics

  
  | Pipeline Name                   | US Treasury Returns                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [us_treasury_returns](./pipelines/us_treasury_returns_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/us_treasury_returns                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/us_treasury_returns/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:00:02           |
| OS Compatibility                |  |
| Linked Dataframes               |  [us_treasury_returns:ftsfr_treas_bond_returns](./dataframes/us_treasury_returns/ftsfr_treas_bond_returns.md)<br>  [us_treasury_returns:ftsfr_treas_bond_portfolio_returns](./dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.md)<br>  |




  
  

## WRDS Bank Regulatory Premium

WRDS Bank Regulatory Premium database tables including call reports, CRSP linkage, and LEI data

  
  | Pipeline Name                   | WRDS Bank Regulatory Premium                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [wrds_bank_premium](./pipelines/wrds_bank_premium_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    | https://github.com/ftsfr/wrds_bank_premium                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/wrds_bank_premium/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 00:05:52           |
| OS Compatibility                |  |
| Linked Dataframes               |  [wrds_bank_premium:ftsfr_bank_total_assets](./dataframes/wrds_bank_premium/ftsfr_bank_total_assets.md)<br>  |




  
  

## WRDS CRSP-Compustat

CRSP stock returns and Fama-French factor replication from WRDS CRSP and Compustat databases

  
  | Pipeline Name                   | WRDS CRSP-Compustat                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [wrds_crsp_compustat](./pipelines/wrds_crsp_compustat_README.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano, Tobias Rodriguez del Pozo           |
| Git Repo URL                    | https://github.com/ftsfr/wrds_crsp_compustat                        |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/ftsfr_repos/wrds_crsp_compustat/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-17 09:06:32           |
| OS Compatibility                |  |
| Linked Dataframes               |  [wrds_crsp_compustat:ftsfr_CRSP_monthly_stock_ret](./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.md)<br>  [wrds_crsp_compustat:ftsfr_CRSP_monthly_stock_retx](./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_retx.md)<br>  |



