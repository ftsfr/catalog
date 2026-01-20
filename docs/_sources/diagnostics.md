# Diagnostics

This page provides metadata quality diagnostics for all pipelines, dataframes, and charts in the system.

## Download Report

[Download CSV Report](_static/diagnostics/chartbook_metadata_diagnostics.csv)

## Metadata Completeness Report

```{raw} html

<div style="overflow-x: auto; margin: 20px 0;">
<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 8px; text-align: left;">Name</th>
      <th style="padding: 8px; text-align: center;">Complete</th>
      <th style="padding: 8px; text-align: left;">Object Type</th>
      <th style="padding: 8px; text-align: left;">Identifier</th>
      <th style="padding: 8px; text-align: left;">Pipeline</th>
      <th style="padding: 8px; text-align: left;">Missing Fields</th>
      <th style="padding: 8px; text-align: left;">URL</th>
    </tr>
  </thead>
  <tbody>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">TIPS-Treasury Basis</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>basis_tips_treas</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_tips_treas</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_tips_treasury_basis</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/basis_tips_treas/ftsfr_tips_treasury_basis.html"><code>ftsfr_tips_treasury_basis</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_tips_treas</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/basis_tips_treas/ftsfr_tips_treasury_basis.html">./dataframes/basis_tips_treas/ftsfr_tips_treasury_basis.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Treasury-Secured Financing Basis</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>basis_treas_sf</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_treas_sf</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_treasury_sf_basis</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.html"><code>ftsfr_treasury_sf_basis</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_treas_sf</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.html">./dataframes/basis_treas_sf/ftsfr_treasury_sf_basis.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Treasury-Swap Arbitrage Spreads</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>basis_treas_swap</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_treas_swap</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_treasury_swap_basis</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.html"><code>ftsfr_treasury_swap_basis</code></a>

      </td>
      <td style="padding: 8px;"><code>basis_treas_swap</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.html">./dataframes/basis_treas_swap/ftsfr_treasury_swap_basis.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">CDS-Bond Basis</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>cds_bond_basis</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_bond_basis</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cds_bond_basis_aggregated</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.html"><code>ftsfr_cds_bond_basis_aggregated</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_bond_basis</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.html">./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_aggregated.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cds_bond_basis_non_aggregated</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.html"><code>ftsfr_cds_bond_basis_non_aggregated</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_bond_basis</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.html">./dataframes/cds_bond_basis/ftsfr_cds_bond_basis_non_aggregated.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">CDS Returns</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>cds_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cds_portfolio_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/cds_returns/ftsfr_cds_portfolio_returns.html"><code>ftsfr_cds_portfolio_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/cds_returns/ftsfr_cds_portfolio_returns.html">./dataframes/cds_returns/ftsfr_cds_portfolio_returns.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cds_contract_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/cds_returns/ftsfr_cds_contract_returns.html"><code>ftsfr_cds_contract_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>cds_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/cds_returns/ftsfr_cds_contract_returns.html">./dataframes/cds_returns/ftsfr_cds_contract_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Covered Interest Parity Deviations</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>cip</code></a>

      </td>
      <td style="padding: 8px;"><code>cip</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cip_spreads</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/cip/ftsfr_cip_spreads.html"><code>ftsfr_cip_spreads</code></a>

      </td>
      <td style="padding: 8px;"><code>cip</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/cip/ftsfr_cip_spreads.html">./dataframes/cip/ftsfr_cip_spreads.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Commodities</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>commodities</code></a>

      </td>
      <td style="padding: 8px;"><code>commodities</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_commodities_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/commodities/ftsfr_commodities_returns.html"><code>ftsfr_commodities_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>commodities</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/commodities/ftsfr_commodities_returns.html">./dataframes/commodities/ftsfr_commodities_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Corporate Bond Returns</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>corp_bond_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>corp_bond_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_corp_bond_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/corp_bond_returns/ftsfr_corp_bond_returns.html"><code>ftsfr_corp_bond_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>corp_bond_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/corp_bond_returns/ftsfr_corp_bond_returns.html">./dataframes/corp_bond_returns/ftsfr_corp_bond_returns.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_corp_bond_portfolio_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.html"><code>ftsfr_corp_bond_portfolio_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>corp_bond_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.html">./dataframes/corp_bond_returns/ftsfr_corp_bond_portfolio_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">CRSP Treasury</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>crsp_treasury</code></a>

      </td>
      <td style="padding: 8px;"><code>crsp_treasury</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">crsp_treasury_daily</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/crsp_treasury/crsp_treasury_daily.html"><code>crsp_treasury_daily</code></a>

      </td>
      <td style="padding: 8px;"><code>crsp_treasury</code></td>
      <td style="padding: 8px; font-size: 0.9em;">links_to_data_providers</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/crsp_treasury/crsp_treasury_daily.html">./dataframes/crsp_treasury/crsp_treasury_daily.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">treasury_auctions</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/crsp_treasury/treasury_auctions.html"><code>treasury_auctions</code></a>

      </td>
      <td style="padding: 8px;"><code>crsp_treasury</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/crsp_treasury/treasury_auctions.html">./dataframes/crsp_treasury/treasury_auctions.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Federal Reserve Yield Curve</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>fed_yield_curve</code></a>

      </td>
      <td style="padding: 8px;"><code>fed_yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_treas_yield_curve_zero_coupon</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.html"><code>ftsfr_treas_yield_curve_zero_coupon</code></a>

      </td>
      <td style="padding: 8px;"><code>fed_yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.html">./dataframes/fed_yield_curve/ftsfr_treas_yield_curve_zero_coupon.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Foreign Exchange Returns</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>foreign_exchange</code></a>

      </td>
      <td style="padding: 8px;"><code>foreign_exchange</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_fx_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/foreign_exchange/ftsfr_fx_returns.html"><code>ftsfr_fx_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>foreign_exchange</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/foreign_exchange/ftsfr_fx_returns.html">./dataframes/foreign_exchange/ftsfr_fx_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">He-Kelly-Manela Factors</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>he_kelly_manela</code></a>

      </td>
      <td style="padding: 8px;"><code>he_kelly_manela</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_he_kelly_manela_factors_monthly</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_monthly.html"><code>ftsfr_he_kelly_manela_factors_monthly</code></a>

      </td>
      <td style="padding: 8px;"><code>he_kelly_manela</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_monthly.html">./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_monthly.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_he_kelly_manela_factors_daily</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.html"><code>ftsfr_he_kelly_manela_factors_daily</code></a>

      </td>
      <td style="padding: 8px;"><code>he_kelly_manela</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.html">./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_factors_daily.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_he_kelly_manela_all</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_all.html"><code>ftsfr_he_kelly_manela_all</code></a>

      </td>
      <td style="padding: 8px;"><code>he_kelly_manela</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_all.html">./dataframes/he_kelly_manela/ftsfr_he_kelly_manela_all.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Ken French Data Library</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>ken_french_data_library</code></a>

      </td>
      <td style="padding: 8px;"><code>ken_french_data_library</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_french_portfolios_25_daily_size_and_bm</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.html"><code>ftsfr_french_portfolios_25_daily_size_and_bm</code></a>

      </td>
      <td style="padding: 8px;"><code>ken_french_data_library</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.html">./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_bm.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_french_portfolios_25_daily_size_and_op</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_op.html"><code>ftsfr_french_portfolios_25_daily_size_and_op</code></a>

      </td>
      <td style="padding: 8px;"><code>ken_french_data_library</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_op.html">./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_op.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_french_portfolios_25_daily_size_and_inv</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_inv.html"><code>ftsfr_french_portfolios_25_daily_size_and_inv</code></a>

      </td>
      <td style="padding: 8px;"><code>ken_french_data_library</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_inv.html">./dataframes/ken_french_data_library/ftsfr_french_portfolios_25_daily_size_and_inv.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">NYU Call Report</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>nyu_call_report</code></a>

      </td>
      <td style="padding: 8px;"><code>nyu_call_report</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_nyu_call_report_leverage</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_leverage.html"><code>ftsfr_nyu_call_report_leverage</code></a>

      </td>
      <td style="padding: 8px;"><code>nyu_call_report</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_leverage.html">./dataframes/nyu_call_report/ftsfr_nyu_call_report_leverage.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_nyu_call_report_holding_company_leverage</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_leverage.html"><code>ftsfr_nyu_call_report_holding_company_leverage</code></a>

      </td>
      <td style="padding: 8px;"><code>nyu_call_report</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_leverage.html">./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_leverage.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_nyu_call_report_cash_liquidity</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_cash_liquidity.html"><code>ftsfr_nyu_call_report_cash_liquidity</code></a>

      </td>
      <td style="padding: 8px;"><code>nyu_call_report</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_cash_liquidity.html">./dataframes/nyu_call_report/ftsfr_nyu_call_report_cash_liquidity.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_nyu_call_report_holding_company_cash_liquidity</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.html"><code>ftsfr_nyu_call_report_holding_company_cash_liquidity</code></a>

      </td>
      <td style="padding: 8px;"><code>nyu_call_report</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.html">./dataframes/nyu_call_report/ftsfr_nyu_call_report_holding_company_cash_liquidity.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">SPX Options</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>options</code></a>

      </td>
      <td style="padding: 8px;"><code>options</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_hkm_option_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/options/ftsfr_hkm_option_returns.html"><code>ftsfr_hkm_option_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>options</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/options/ftsfr_hkm_option_returns.html">./dataframes/options/ftsfr_hkm_option_returns.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_cjs_option_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/options/ftsfr_cjs_option_returns.html"><code>ftsfr_cjs_option_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>options</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/options/ftsfr_cjs_option_returns.html">./dataframes/options/ftsfr_cjs_option_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">JP Morgan EMBI Sovereign Bond Returns</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>sovereign_bonds</code></a>

      </td>
      <td style="padding: 8px;"><code>sovereign_bonds</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_embi_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/sovereign_bonds/ftsfr_embi_returns.html"><code>ftsfr_embi_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>sovereign_bonds</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/sovereign_bonds/ftsfr_embi_returns.html">./dataframes/sovereign_bonds/ftsfr_embi_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">US Treasury Returns</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>us_treasury_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>us_treasury_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_treas_bond_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/us_treasury_returns/ftsfr_treas_bond_returns.html"><code>ftsfr_treas_bond_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>us_treasury_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/us_treasury_returns/ftsfr_treas_bond_returns.html">./dataframes/us_treasury_returns/ftsfr_treas_bond_returns.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_treas_bond_portfolio_returns</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.html"><code>ftsfr_treas_bond_portfolio_returns</code></a>

      </td>
      <td style="padding: 8px;"><code>us_treasury_returns</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.html">./dataframes/us_treasury_returns/ftsfr_treas_bond_portfolio_returns.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">WRDS Bank Regulatory Premium</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>wrds_bank_premium</code></a>

      </td>
      <td style="padding: 8px;"><code>wrds_bank_premium</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_bank_total_assets</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/wrds_bank_premium/ftsfr_bank_total_assets.html"><code>ftsfr_bank_total_assets</code></a>

      </td>
      <td style="padding: 8px;"><code>wrds_bank_premium</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/wrds_bank_premium/ftsfr_bank_total_assets.html">./dataframes/wrds_bank_premium/ftsfr_bank_total_assets.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">WRDS CRSP-Compustat</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>wrds_crsp_compustat</code></a>

      </td>
      <td style="padding: 8px;"><code>wrds_crsp_compustat</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_CRSP_monthly_stock_ret</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.html"><code>ftsfr_CRSP_monthly_stock_ret</code></a>

      </td>
      <td style="padding: 8px;"><code>wrds_crsp_compustat</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.html">./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_ret.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">ftsfr_CRSP_monthly_stock_retx</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_retx.html"><code>ftsfr_CRSP_monthly_stock_retx</code></a>

      </td>
      <td style="padding: 8px;"><code>wrds_crsp_compustat</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_retx.html">./dataframes/wrds_crsp_compustat/ftsfr_CRSP_monthly_stock_retx.html</a>

      </td>
    </tr>

  </tbody>
</table>
</div>

```

## What This Report Contains

- **Pipeline Diagnostics**: Checks for missing required fields in pipeline metadata
- **Dataframe Diagnostics**: Validates dataframe documentation completeness
- **Chart Diagnostics**: Ensures all charts have complete metadata

## Required Fields by Object Type

### Pipeline Fields (9 required)
- Pipeline name and description
- Lead developer and contributors
- Git repository URL
- Software modules/dependencies
- README file path

### Dataframe Fields (9 required)
- Data sources and providers
- Topic tags and data access info
- License information
- File paths (Parquet, Excel, docs)
- Date column specification

### Chart Fields (10 required)
- Chart name and description
- Legal clearance information
- Data characteristics (frequency, units, etc.)
- File paths for HTML and Excel outputs
- Associated dataframe reference

## How to Use This Report

1. **Identify Incomplete Metadata**: Rows highlighted in yellow indicate incomplete metadata
2. **Check Missing Fields**: Review the "Missing Fields" column for specific gaps
3. **Update Configuration**: Add missing fields to your pipeline's `chartbook.toml` file
4. **Verify Changes**: Rebuild the documentation to see updated diagnostics

## Summary Statistics


- **Total Objects**: 52
- **Complete**: 32 (61.5%)
- **Incomplete**: 20 (38.5%)
