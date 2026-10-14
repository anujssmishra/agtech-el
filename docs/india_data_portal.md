# India Data Portal: what it holds, and what matters for this project

Checked 14 October 2026 through the portal's public catalogue (<https://ckandev.indiadataportal.com>).

**About the portal**
- **Who runs it:** the India Data Portal (IDP) is built by the Bharti Institute of Public Policy at the Indian
  School of Business. It republishes data from government departments in cleaned form.
- **Access:** it is **free and open**, not part of the IIM Lucknow subscription. Public datasets download as CSV
  with no login; a test download of the state-level NFHS file worked.
- **Merging:** files carry Local Government Directory (LGD) codes for states, districts, blocks, panchayats and
  villages, so they can be merged with each other.

**Licence and citation**
- The catalogue lists 92 entries, one of them a test upload, so 91 datasets. 68 of the 91 are under the Open Data
  Commons Attribution Licence; the other 23 state no licence.
- The portal allows free use for any purpose with citation.
- Cite both the portal and the original source, for example: *India Data Portal (Bharti Institute of Public
  Policy, ISB), "National Family Health Survey (NFHS)", accessed 14 October 2026; original source: Ministry of
  Health and Family Welfare and IIPS.*

## For this project: farmers and digital access

### Farmer characteristics

| Dataset | Lowest level | Years | What it gives |
|---|---|---|---|
| Agricultural Census (Non Crop) | Sub-district (also state, district) | 2010-11, 2015-16 | Number and area of holdings by size class and social group; land owned, leased in and leased out; irrigation by source |
| Input Survey | District | 2011-12, 2016-17 | Holdings; **education of farm holders** (illiterate to graduate); soil testing; certified seed; machinery; fertiliser and manure use |
| Census 2011 Primary Census Abstract (PCA Demography) | Village (also sub-district, district, state) | 2011 | Population by literacy, social group, sex and rural/urban; workers by type, including **cultivators and agricultural labourers** |
| Socio Economic Caste Census (SECC) | District | 2011 | Rural households by main income source (cultivation, casual labour and others); landless manual labour; Kisan Credit Card limit of ₹50,000 or more; irrigated land; farm machinery; income bands; literate adults |
| NABARD All India Rural Financial Inclusion Survey (NAFIS) | State | 2016-17 | Average land size; monthly income of agricultural households; saving, debt and microfinance |
| Crop insurance (PMFBY) | District | 2018–2022 | Insured farmers by sex, social group, farm size (marginal, small, other) and loanee status; area and sum insured |
| Periodic Labour Force Survey (PLFS) | State | 2018-19; quarterly 2018–2024 (22 states) | Share of workers in agriculture; labour force participation |
| Mission Antyodaya: Village Agriculture Report | Village | 2020 | Farm and non-farm households in each village; farmer collectives; custom hiring centres; seed centres; warehouses |

Other farm data on the portal include crop area, production and yield; land use; agricultural wages; cost of
cultivation; MSP; mandi (APMC) arrivals and prices; fertiliser sales; soil health cards; and Pashu Aadhaar
livestock registrations.

### Digital access and literacy

| Dataset | Lowest level | Years | What it gives |
|---|---|---|---|
| National Family Health Survey (NFHS) | District (also state) | 2015-16, 2019-21, 2023-24 | **Women and men who have ever used the internet** (asked from 2019-21); women who use a mobile phone; literacy. State files split rural and urban |
| Census 2011 Household Amenities | District, rural and urban | 2011 | Households with a **computer with or without internet**, mobile phone, landline, TV or radio; use of banking services |
| Mission Antyodaya | Village (also panchayat, block, district, state) | 2019–2020 | Whether each village has **broadband or internet**, a Common Service Centre, telephone services, or a banking correspondent with internet |
| UIDAI | State | 2022 | Aadhaar saturation |
| Direct Benefit Transfer (DBT) | District | 2019-20 to 2023-24 | Total DBT payments and number of transactions, summed over all schemes |
| NPCI | India only | 2016–2023 | UPI volumes; national figures, not by state |

### Points to watch

- **Census 2011 and SECC 2011 are 15 years old.** They suit baselines from before PM-KISAN and the app boom, not
  current levels.
- **NFHS-6 district figures are totals only**, with no rural/urban split.
- **NFHS low-sample estimates.** Some NFHS district values rest on 25–49 cases (the portal's notes list which).
  Men's indicators are thinner than women's.
- **NFHS measures use, not skills.** It records whether a person has *ever used* the internet; Census 2011 records
  what households *own*.
- **NFHS internet use moved a lot.** For rural women in Uttar Pradesh it rose from 24.5% in 2019-21 to 67.3% in
  2023-24, which makes district change in internet use a usable measure of exposure.
- **DBT is not scheme-specific.** The district totals are not PM-KISAN alone.
- **NPCI (UPI) data are national only.**
- **PLFS quarterly files cover 22 states.**
- **Mission Antyodaya records facilities, not use.** It shows what exists in a village (for example, broadband
  available), not whether people use it.

### Not on the portal, and where to get it instead

These are available through DATAFUL or Indiastat, both covered by the IIM Lucknow subscription
(`docs/institute_resources.md`):
- NSS 77th round (2019) survey of agricultural households: farm household income, land and debt by state;
- NSS 78th round (2020-21) digital skills by state, rural/urban, age and sex;
- the Comprehensive Modular Survey: Telecom (2025): internet use and digital skills by state;
- PM-KISAN beneficiaries by state and instalment.

## Full catalogue

91 datasets and 280 files, grouped by the portal's sector. For each file: geographic level, years, coverage, number of rows and the variables. Identifier columns (state, district, block, village names and codes) are left out of the variable lists.

### Food and Agriculture

#### Agricultural Census Crop

The Agricultural Crop Census in India is a large-scale statistical exercise conducted periodically to collect comprehensive data on the cultivation of different crops across the country. This census aims to provide detailed information on the area under cultivation, production, yield, cropping patterns, and other related agricultural practices.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/agricultural-census-crop>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| District Level AgCensus Crop | District | 2010-11, 2015-16 | 36 states/UTs, 677 districts | 1,476,778 | 11: year, social_group, farm_size_class, farm_size_category, crop_name, crop_code, crop_type, hold_no, irr_ar, unirr_ar, total_ar |
| State Level AgCensus Crop | State | 2010-11, 2015-16 | 35 states/UTs | 165,560 | 11: year, social_group, farm_size_class, farm_size_category, crop_name, crop_code, crop_type, hold_no, irr_ar, unirr_ar, total_ar |
| Tehsil Level AgCensus Crop | Block | 2010-11, 2015-16 | 36 states/UTs, 730 districts, 6,045 sub-districts | 6,495,760 | 11: year, social_group, farm_size_class, farm_size_category, crop_name, crop_code, crop_type, hold_no, irr_ar, unirr_ar, total_ar |

#### Agricultural Census Non Crop

This dataset offers a comprehensive insight into agricultural land holding across India. It categorizes farms based on their size and ownership structures, detailing areas that are owned, leased, or operated in various combinations.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/agricultural-census-non-crop>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| District level AgCensus Non Crop | District | 2010-11, 2015-16 | 36 states/UTs, 655 districts | 40,800 | 83: year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot … |
| State level AgCensus Non Crop | State | 2010-11, 2015-16 | 35 states/UTs | 2,400 | 83: year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot … |
| Tehsil level AgCensus Non Crop | Block | 2010-11 , 2015-16 | 36 states/UTs, 728 districts, 5,418 sub-districts | 322,340 | 83: year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot … |

<details><summary>All 83 variables: District level AgCensus Non Crop</summary>

year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot, wls_no, wls_ar, wooh_no, wooh_ar, po_poh_no, p_owoh_owar, p_owoh_oar, p_owoh_totar, p_lsoh_no, p_lsoh_ar, p_lsoh_oar, p_lsoh_totar, p_owlsoh_no, p_owlsoh_owar, p_owlsoh_lsar, p_owlsoh_oar, p_owlsoh_totar, fixd_money, fixd_prod, shr_prd, unsurf_mortg, othr_term, tot, net_swn_ar, crt_flw_ar, net_clt_ar, unclt_excl_fall_lnd, fall_othr_curr_fall, cult_waste_lnd, tot_unclt, not_avl_cult, w_ir_no, w_ir_ar, w_unir_no, w_unir_ar, p_ir_no, p_ir_totar, p_ir_ar, h_ir_no, h_ir_ntar, canal_no, canal_ar, tank_no, tank_ar, well_no, well_ar, tube_no, tube_ar, othr_no, othr_ar, ex_hol_irr_no, net_irr_ar, wl_pselc_n, wl_psdsl_n, wl_ps_t, wl_wops_t, wl_n_use, twl_elc_n, twl_dsl_n, twl_t, op_ar_ent_vill_res_no, op_ar_ent_vill_res_ar, op_ar_par_vill_res_no, op_ar_par_vill_res_ar, op_ar_ent_out_vill_res_no, op_ar_ent_out_vill_res_ar, ophol_oprat_out_teh_no, ophol_oprat_out_teh_ar, gca_irr_ar, gca_unirr_ar, gca_tot

</details>

<details><summary>All 83 variables: State level AgCensus Non Crop</summary>

year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot, wls_no, wls_ar, wooh_no, wooh_ar, po_poh_no, p_owoh_owar, p_owoh_oar, p_owoh_totar, p_lsoh_no, p_lsoh_ar, p_lsoh_oar, p_lsoh_totar, p_owlsoh_no, p_owlsoh_owar, p_owlsoh_lsar, p_owlsoh_oar, p_owlsoh_totar, fixd_money, fixd_prod, shr_prd, unsurf_mortg, othr_term, tot, net_swn_ar, crt_flw_ar, net_clt_ar, unclt_excl_fall_lnd, fall_othr_curr_fall, cult_waste_lnd, tot_unclt, not_avl_cult, w_ir_no, w_ir_ar, w_unir_no, w_unir_ar, p_ir_no, p_ir_totar, p_ir_ar, h_ir_no, h_ir_ntar, canal_no, canal_ar, tank_no, tank_ar, well_no, well_ar, tube_no, tube_ar, othr_no, othr_ar, ex_hol_irr_no, net_irr_ar, wl_pselc_n, wl_psdsl_n, wl_ps_t, wl_wops_t, wl_n_use, twl_elc_n, twl_dsl_n, twl_t, op_ar_ent_vill_res_no, op_ar_ent_vill_res_ar, op_ar_par_vill_res_no, op_ar_par_vill_res_ar, op_ar_ent_out_vill_res_no, op_ar_ent_out_vill_res_ar, ophol_oprat_out_teh_no, ophol_oprat_out_teh_ar, gca_irr_ar, gca_unirr_ar, gca_tot

</details>

<details><summary>All 83 variables: Tehsil level AgCensus Non Crop</summary>

year, social_group, farm_size_class, farm_size_category, hol_no, hol_ar, wow_soh_no, wow_soh_ar, pow_pls_no, powls_owar, powls_lsar, powls_tot, wls_no, wls_ar, wooh_no, wooh_ar, po_poh_no, p_owoh_owar, p_owoh_oar, p_owoh_totar, p_lsoh_no, p_lsoh_ar, p_lsoh_oar, p_lsoh_totar, p_owlsoh_no, p_owlsoh_owar, p_owlsoh_lsar, p_owlsoh_oar, p_owlsoh_totar, fixd_money, fixd_prod, shr_prd, unsurf_mortg, othr_term, tot, net_swn_ar, crt_flw_ar, net_clt_ar, unclt_excl_fall_lnd, fall_othr_curr_fall, cult_waste_lnd, tot_unclt, not_avl_cult, w_ir_no, w_ir_ar, w_unir_no, w_unir_ar, p_ir_no, p_ir_totar, p_ir_ar, h_ir_no, h_ir_ntar, canal_no, canal_ar, tank_no, tank_ar, well_no, well_ar, tube_no, tube_ar, othr_no, othr_ar, ex_hol_irr_no, net_irr_ar, wl_pselc_n, wl_psdsl_n, wl_ps_t, wl_wops_t, wl_n_use, twl_elc_n, twl_dsl_n, twl_t, op_ar_ent_vill_res_no, op_ar_ent_vill_res_ar, op_ar_par_vill_res_no, op_ar_par_vill_res_ar, op_ar_ent_out_vill_res_no, op_ar_ent_out_vill_res_ar, ophol_oprat_out_teh_no, ophol_oprat_out_teh_ar, gca_irr_ar, gca_unirr_ar, gca_tot

</details>

#### Agriculture Marketing

The Agricultural Marketing package is a collection of datasets and resources providing daily agricultural market information from wholesale markets across India. It includes commodity- and variety-wise price, arrival, and related market data collected from Agricultural Produce Market Committees (APMCs), supporting market analysis, research, and evidence-based policymaking.
*Source:* Ministry of Agriculture and Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/agriculture-marketing>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| APMC Arrivals And Prices (Old Source) | Market Center | 2021-2025 | 39 states/UTs, 708 districts | 22,642,741 | 15: report_date, market_center, market_code, latitude, longitude, commodity_type, commodity_name, variety, origin, arrival_quantity, arrivals_unit, min_price … |
| APMC Arrivals And Prices (New Source) | Market Center | 2025-2026 | 31 states/UTs, 568 districts | 3,861,467 | 17: date, market_center_name, market_center_code, category, year_of_establishment, latitude, longitude, commodity_name, commodity_id, variety, grade, arrival_quantity … |

<details><summary>All 15 variables: APMC Arrivals And Prices (Old Source)</summary>

report_date, market_center, market_code, latitude, longitude, commodity_type, commodity_name, variety, origin, arrival_quantity, arrivals_unit, min_price, max_price, modal_price, price_unit

</details>

<details><summary>All 17 variables: APMC Arrivals And Prices (New Source)</summary>

date, market_center_name, market_center_code, category, year_of_establishment, latitude, longitude, commodity_name, commodity_id, variety, grade, arrival_quantity, arrival_units, min_price, max_price, modal_price, price_unit

</details>

#### Agriculture Marketing

The Agricultural Marketing Information Network (AGMARKNET) dataset provides daily price and arrival information for more than 300 different commodities and over 1500 varieties of agricultural produce from wholesale markets across India. This comprehensive dataset is collected from Agricultural Produce Market Committees (APMCs) and covers 4549 markets as of January 16, 2025.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/apmc-arrivals-and-prices>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| APMC arrivals and prices (Agmarknet) | Market Center | 2019-2025 | 32 states/UTs, 616 districts | — | not previewable on the portal (download to inspect) |

#### Area and Production Statistics (NHB)

The "Area and Production Statistics (NHB)" dataset offers extensive insights into the agricultural landscape of India, providing comprehensive statistics on the cultivation area, production quantities, and yields of various crops.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/area-and-production-statistics-nhb>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Area and Production Statistics (NHB) | State | 2013-2019 | 35 states/UTs | 1,274 | 4: year, crop_category, area, production |

#### Area, Production, Yield (APY)

This package contains two district-level datasets on agricultural Area, Production and Yield in India, drawn from different government sources. Crop-wise Area, Production & Yield is sourced from DES (Directorate of Economics & Statistics) and covers a wider range of crops, including horticultural crops such as fruits, vegetables and spices, alongside field crops.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/area-production-yield-apy>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Crop Wise Area Production Yield | District | 1997-2023 | 34 states/UTs, 740 districts | 455,359 | 11: year, crop_name, crop_code, crop_type, season, area, area_unit, production, production_unit, yield, yield_unit |
| Crop-wise Area, Production & Yield (UPAG) | District | 2013-2014 to 2024-2025 | 34 states/UTs | 156,189 | 8: year, season, crop_category, crop_name, crop_code, area, production, yield |

#### Cold Chains

Cold chains offer significant advantages in enhancing perishable products' shelf life, quality, and market reach. Leveraging datasets from the NHB, "Integrated Cold Chain Availability," and from the Ministry of Food Processing Industries, "Approved Cold Chain Projects District Level Aggregates," stakeholders can identify existing cold chain infrastructure and future projects, optimizing the supply chain.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/cold-chains>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Integrated Cold Chain Availability Component Details | District | 1999-2024 | 33 states/UTs, 417 districts | 5,040 | 12: project_code, year_of_subsidy_sanct, agency, supported_by, beneficiary_name, project_address, current_status, component_category, component, units, capacity, capacity_unit |
| Integrated Cold Chain Availability Cost Report | District | 1999-2024 | 33 states/UTs, 417 districts | 4,486 | 9: project_code, year_of_subsidy_sanct, agency, supported_by, beneficiary_name, project_address, current_status, project_cost, amount_sanct |
| Approved Cold Chain Projects | Point | 2009-2023 | 26 states/UTs, 174 districts | 371 | 12: project, sector, approval_date, completion_date, physical_progress, project_cost, approved_amount, released_amount, milk_storage_processing, capacity_of_cold_storage, iqf, reefer_carrier_and_tanker |

#### Cost of Cultivation

The "Cost of Cultivation" compiles cost statistics for cultivating various crops across the country, detailing expenses from seeds to labor. It's a valuable resource for agriculture research and policymaking, aiding in crop selection, resource allocation, and policy decisions.
*Source:* Directorate of Economics and Statistics, Department of Agriculture Cooperation and Farmers Welfare, Ministry of Agriculture and Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/cost-of-cultivation>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Cost of Cultivation | State | 1996-2021 | 20 states/UTs | 3,880 | 63: year, crop_name, crop_code, crop_type, cul_cost_a1, cul_cost_a2, cul_cost_b1, cul_cost_b2, cul_cost_c1, cul_cost_c2, cul_cost_c2rev, cul_cost_a2fl … |

<details><summary>All 63 variables: Cost of Cultivation</summary>

year, crop_name, crop_code, crop_type, cul_cost_a1, cul_cost_a2, cul_cost_b1, cul_cost_b2, cul_cost_c1, cul_cost_c2, cul_cost_c2rev, cul_cost_a2fl, prod_cost_a1, prod_cost_a2, prod_cost_b1, prod_cost_b2, prod_cost_c1, prod_cost_c2, prod_cost_c2rev, prod_cost_c3, prod_cost_a2fl, main_product_value, by_product_value, mat_lab_input_seed, mat_lab_input_fertilizer, mat_lab_input_manure, mat_lab_input_hmn_lab, mat_lab_input_ani_lab, seed_rate_per_unit, fert_rate_per_unit, manure_rate_per_unit, hmn_lab_rate_per_unit, ani_lab_rate_per_unit, implicit_rate, num_holdings_sample, num_tehsils_sample, derived_yield, hmn_lab_hrs_family, hmn_lab_hrs_attached, hmn_lab_hrs_casual, opr_cost_hmn_lab_family, opr_cost_hmn_lab_attached, opr_cost_hmn_lab_casual, opr_cost_ani_lab_hired, opr_cost_ani_lab_owned, opr_cost_mch_lab_hired, opr_cost_mch_lab_owned, opr_cost_seed, opr_cost_fertilizer, opr_cost_manure, opr_cost_insecticides, opr_cost_irrigation_chrg, opr_cost_misc, opr_cost_interest_on_wrk_cap, opr_cost, fix_cost_owned_land_rental, fix_cost_leased_land_rent, fix_cost_land_rev_tax_cess, fix_cost_depr_impl_farm_build, fix_cost_interest_fix_cap, fix_cost, opr_cost_crop_insurance, opr_cost_contractor_pay

</details>

#### Daily Fertilizer Sales

The dataset provides information on the daily sales of different types of fertilizers by retail outlets in India. This dataset is valuable for farmers, policymakers, researchers, and other stakeholders in the agriculture sector. Farmers can use the information to plan their fertilizer purchases and ensure that they have access to the fertilizers they need.
*Source:* Ministry of Chemicals and Fertilizers. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/daily-fertilizer-sales>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Daily Fertilizer Sales | Point of Sale | 2015-2021 | 36 states/UTs, 765 districts | — | not previewable on the portal (download to inspect) |

#### Fertilizer Sales

The "Fertilizer Sales" dataset, provided by the Ministry of Chemicals and Fertilizers, offers a comprehensive glimpse into the sale and distribution of fertilizers across India.
*Source:* Ministry of Chemicals and Fertilizers. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/fertilizer-sales>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Daily Fertilizer Sales | District | 2015-21 | 36 states/UTs, 765 districts | 0 | 14: date, retailer_name, retailer_id, attached_devices, active, opening_stock_reported, opening_stock, no_of_invoices_generated, no_of_sale_transaction, quantity_sold, n_quantity, p_quantity … |

<details><summary>All 14 variables: Daily Fertilizer Sales</summary>

date, retailer_name, retailer_id, attached_devices, active, opening_stock_reported, opening_stock, no_of_invoices_generated, no_of_sale_transaction, quantity_sold, n_quantity, p_quantity, k_quantity, s_quantity

</details>

#### Food and Fertilizer Subsidy

This dataset provides information related to total annual subsidy provided by Union and State Governments (combined) for food distribution and fertiliser sales. This information is avilable at all India level from 1990 to 2016. The datasource is India Public Finance Statistics (IPFS), Ministry of Finance
*Source:* Indian Public Finance Statistics. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/food-and-fertilizer-subsidy>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Food and Fertiliser Subsidy | India | 1995-2017 | — | 24 | 3: year, food_subsidy, fertiliser_subsidy |

#### Food and Public Distribution

The "Food and Public Distribution" package provides comprehensive datasets that focus on various aspects of food security and public distribution systems in India. The datasets within this package include detailed information on the distribution and transaction of ration cards, as well as monthly food distribution data.
*Source:* Ministry of Consumer Affairs, Food & Public Distribution. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/food-and-public-distribution>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Monthly Food Distribution Data | District | 2017-2023 | 34 states/UTs, 709 districts | 63,425 | 29: month, total_rice_alloc_non_epos, total_wheat_alloc_non_epos, total_coarse_grain_alloc_non_epos, total_fortified_rice_alloc_non_epos, total_alloc_non_epos, total_rice_alloc_epos, total_wheat_alloc_epos, total_coarse_grain_alloc_epos, total_fortified_rice_alloc_epos, total_alloc_epos, total_rice_alloc … |
| Ration Card Distribution and Transaction Data | State | 2017-2023 | 35 states/UTs | 216 | 16: year, no_of_ration_cards, no_trans_inter_district_aay, no_trans_inter_district_phh, total_inter_trans, no_trans_intra_district_aay, no_trans_intra_district_phh, total_intra_trans, total_transaction, qty_distributed_inter_district_aay, qty_distributed_inter_district_phh, total_inter_qty … |

<details><summary>All 29 variables: Monthly Food Distribution Data</summary>

month, total_rice_alloc_non_epos, total_wheat_alloc_non_epos, total_coarse_grain_alloc_non_epos, total_fortified_rice_alloc_non_epos, total_alloc_non_epos, total_rice_alloc_epos, total_wheat_alloc_epos, total_coarse_grain_alloc_epos, total_fortified_rice_alloc_epos, total_alloc_epos, total_rice_alloc, total_wheat_alloc, total_coarse_grain_alloc, total_fortified_rice_alloc, total_alloc, total_rice_dist_non_epos, total_wheat_dist_non_epos, total_coarse_grain_dist_non_epos, total_fortified_rice_dist_non_epos, total_dist_non_epos, dist_pct_non_epos, total_rice_dist_epos, total_wheat_dist_epos, total_coarse_grain_dist_epos, total_fortified_rice_dist_epos, total_dist_epos, dist_pct_epos, total_dist_epos_all

</details>

<details><summary>All 16 variables: Ration Card Distribution and Transaction Data</summary>

year, no_of_ration_cards, no_trans_inter_district_aay, no_trans_inter_district_phh, total_inter_trans, no_trans_intra_district_aay, no_trans_intra_district_phh, total_intra_trans, total_transaction, qty_distributed_inter_district_aay, qty_distributed_inter_district_phh, total_inter_qty, qty_distributed_intra_district_aay, qty_distributed_intra_district_phh, total_intra_qty, total_qty

</details>

#### Input Survey

The Input Survey dataset, managed by the Department of Agriculture, Cooperation & Farmers Welfare (DAC&FW), is an essential tool that captures data related to agricultural inputs across India. This survey delves into various aspects of farming, detailing the usage of seeds, fertilizers, pesticides, machinery, irrigation methods, and other critical agricultural resources.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/input-survey>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Input Survey - Composite | District | 2011-12, 2016-17 | 36 states/UTs, 674 districts | 3,861,572 | 22: year, crop_name, crop_type, crop_code, fertilizer, area_type, size_group, size_category, num_holdings, holdings_treated_with_manure, area_hyv, area_other … |
| Input Survey - Non Crop | District | 2011-12, 2016-17 | 36 states/UTs, 674 districts | 6,463 | 179: year, size_group, size_category, num_of_holdings_t1, area_of_holding_t1, num_of_parcel_with_in_vlg_resd_t1, num_of_parcel_outside_vlg_but_within_tehsil_t1, num_of_par_outs_tehsil_but_within_dist_t1, total_num_of_parcel_t1, avg_num_of_parcel_per_holding_t1, avg_area_per_parcel_t1, avg_area_per_holding_t1 … |
| Input Survey - Crop | District | 2011-12, 2016-17 | 34 states/UTs, 657 districts | 1,692,520 | 22: year, crop_name, crop_type, crop_code, fertilizer, area_type, size_group, size_category, nitrogen_pct, phosphorus_pct, potassium_pct, holdings_growing_crop … |

<details><summary>All 22 variables: Input Survey - Composite</summary>

year, crop_name, crop_type, crop_code, fertilizer, area_type, size_group, size_category, num_holdings, holdings_treated_with_manure, area_hyv, area_other, area_total, area_hyv_treated_with_manure, area_other_treated_with_manure, area_total_treated_with_manure, manure_qty_hyv, manure_qty_other, manure_qty_total, area_hyb, area_hyb_treated_with_manure, manure_qty_hyb

</details>

<details><summary>All 179 variables: Input Survey - Non Crop</summary>

year, size_group, size_category, num_of_holdings_t1, area_of_holding_t1, num_of_parcel_with_in_vlg_resd_t1, num_of_parcel_outside_vlg_but_within_tehsil_t1, num_of_par_outs_tehsil_but_within_dist_t1, total_num_of_parcel_t1, avg_num_of_parcel_per_holding_t1, avg_area_per_parcel_t1, avg_area_per_holding_t1, cropped_once_irrigated_area_t2a, cropped_twice_one_crop_irrigated_area_t2a, cropped_twice_both_crops_irrigated_area_t2a, cropped_more_one_crop_irrigated_area_t2a, cropped_more_two_crops_irrigated_area_t2a, crop_more_than_two_crops_irrig_area_t2a, net_irrigated_area_t2a, gross_irrigated_area_t2a, cropped_once_unirrigated_area_t2b, cropped_more_once_unirrigated_area_t2b, net_unirrigated_area_t2b, gross_unirrigated_area_t2b, current_fallow_land_t2b, other_uncultivated_area_t2b, total_operated_area_t2b, other_uncultivated_num_t2b, hold_took_inst_credit_t8, num_opr_hold_took_credit_frm_pacs_t8, num_opr_hold_took_credit_frm_pldb_sldb_t8, num_opr_hold_took_credit_frm_cbb_t8, num_opr_hold_took_credit_frm_rrbb_t8, pacs_stl_credit_t8, pacs_mtl_credit_t8, pacs_ltl_credit_t8, pldb_sldb_stl_credit_t8, pldb_sldb_mtl_credit_t8, pldb_sldb_ltl_credit_t8, cbb_stl_credit_t8, cbb_mtl_credit_t8, cbb_ltl_credit_t8, rrbb_stl_credit_t8, rrbb_mtl_credit_t8, rrbb_ltl_credit_t8, amt_shrt_term_loan_t8, amt_med_term_loan_t8, amt_long_term_loan_t8, total_amt_inst_credit_taken_t8, stl_val_qty_fert_given_t8, stl_val_qty_other_inputs_t8, stl_in_cash_t8, total_stl_t8, num_of_holds_using_cert_seeds_t9a, num_of_holds_using_notified_seeds_t9a, num_of_holds_using_hybrid_seeds_t9a, num_of_holds_taken_found_prgm_t9a, cert_seeds_frm_dept_of_agri_t9a, cert_seeds_frm_seed_corp_t9a, cert_seeds_frm_state_univ_farms_t9a, cert_seeds_frm_coop_fed_t9a, cert_seeds_frm_pvt_seed_cmp_t9a, cert_seeds_frm_pvt_deed_d_r_t9a, total_purchased_cert_seeds_t9a, encount_seed_quality_prb_varietal_impurity_t9a, encount_seed_quality_prb_germination_fail_t9a, encount_seed_quality_prb_physical_impurities_t9a, encount_seed_quality_prb_insect_damage_t9a, encount_seed_quality_prb_other_prb_t9a, total_holder_encount_seed_qlt_prb_t9a, num_opr_holding_performed_soil_test_t9d, total_area_covered_under_soil_test_t9d, excl_num_holdings_adopted_pest_cont_method_t9d, agro_economic_cultral_practices_t9d, mechanical_control_t9d, biological_method_t9d, chemical_method_t9d, other_method_t9d, no_efforts_t9d, num_holding_prfrm_soil_test_in_lst_5_yr_t9d, hand_opr_impl_seed_fert_drill_t7, hand_opr_impl_pedal_opr_thresher_t7, hand_opr_impl_winnowing_fan_t7, hand_opr_impl_maize_sheller_t7, hand_opr_impl_chaf_cutter_t7, hand_opr_impl_sprayer_duster_t7, hand_opr_impl_handhoe_t7, hand_opr_impl_wheelhoe_t7, hand_opr_impl_bladehoe_t7, hand_opr_impl_paddy_transplanter_t7, hand_opr_impl_cono_weeder_t7, hand_opr_impl_paddy_drum_seeder_t7, hand_opr_impl_others_t7, animal_opr_impl_wooden_plough_t7, animal_opr_impl_mold_board_plough_t7, animal_opr_impl_disc_harrow_t7, animal_opr_impl_cultivator_triphali_t7, animal_opr_impl_seed_cum_fert_drill_t7, animal_opr_impl_levelling_karah_t7, animal_opr_impl_seed_planter_t7, animal_opr_impl_cane_cruser_t7, animal_opr_impl_bund_former_t7, animal_opr_impl_potato_ground_nut_digger_t7, animal_opr_impl_puddler_t7, animal_opr_impl_others_t7, power_opr_impl_sprayer_duster_t7, power_opr_impl_diesel_eng_pumpset_t7, power_opr_impl_electric_pumpset_t7, power_opr_impl_tiller_t7, power_opr_impl_agr_tractors_t7, power_opr_impl_tractor_drawn_board_plough_t7, power_opr_impl_tractor_drawn_disc_harrow_t7, power_opr_impl_tractor_drawn_seedcum_fert_drill_t7, power_opr_impl_tractor_drawn_planter_t7, power_opr_impl_tractor_drawn_leveler_t7, power_opr_impl_tractor_drawn_potato_digger_t7, power_opr_impl_threshers_t7, power_opr_impl_chaf_cutter_t7, power_opr_impl_cane_crusher_t7, pwr_opr_impl_comb_harvest_tract_pow_t7, power_opr_impl_combine_harvester_self_propelled_t7, power_opr_impl_cultivator_t7, power_opr_impl_rotovator_t7, power_opr_impl_cage_wheel_t7, power_opr_impl_self_propelled_reaper_t7, power_opr_impl_power_maize_sheller_t7, power_opr_impl_ground_nut_decorticator_t7, power_opr_impl_tractor_mounted_reaper_t7, power_opr_impl_raised_bed_planter_t7, power_opr_impl_zero_till_seed_cum_fert_drill_t7, power_opr_impl_strip_till_drill_t7, power_opr_impl_sugarcane_cutter_planter_t7, power_opr_impl_vegitable_transplanter_t7, power_opr_impl_aero_blast_sprayer_t7, power_opr_impl_weeder_self_propelled_t7, power_opr_impl_pnematic_planter_t7, power_opr_impl_self_propelled_rice_transplanter_t7, power_opr_impl_strew_combines_t7, power_opr_impl_disc_plough_t7, power_opr_impl_others_t7, misc_sprinkler_used_for_irrigation_prpse_t7, misc_drip_irrigation_set_t7, hand_opr_impl_paddy_weeder_t7, hand_opr_impl_tree_pruner_chaff_t7, hand_opr_impl_buding_grafting_knives_t7, hand_opr_impl_garden_fork_t7, animal_opr_impl_steel_plough_t7, animal_opr_impl_olpad_thresher_t7, animal_opr_impl_bullock_cart_t7, animal_opr_impl_persian_wheel_t7, animal_opr_impl_soil_scoop_t7, animal_opr_impl_reaper_t7, power_opr_impl_combine_harvester_trailed_type_t7, misc_hydraulic_ram_t7, misc_chain_washer_pump_t7, misc_bio_gas_t7, misc_others_t7, holders_edu_qual_illiterate_t10, holders_edu_qual_upto_class_v_t10, holders_edu_qual_middle_t10, holders_edu_qual_secondary_t10, holders_edu_qual_sr_secondary_t10, holders_edu_qual_tech_diploma_t10, holders_edu_qual_graduate_and_above_t10, age_group_18_to_30_yr_t11, age_group_31_to_40_yr_t11, age_group_41_to_50_yr_t11, age_group_51_to_60_yr_t11, age_group_61_to_65_yr_t11, age_group_66_and_above_t11, average_age_t11, family_group_upto_3_memb_t12, family_group_4_to_6_memb_t12, family_group_7_to_9_memb_t12, family_group_10_to_12_memb_t12, family_group_13_to_15_memb_t12, family_group_16_to_19_memb_t12, family_group_20_and_above_memb_t12, average_group_size_t12

</details>

<details><summary>All 22 variables: Input Survey - Crop</summary>

year, crop_name, crop_type, crop_code, fertilizer, area_type, size_group, size_category, nitrogen_pct, phosphorus_pct, potassium_pct, holdings_growing_crop, holdings_treated_with_chem_fert, all_crop_area_hyv, all_crop_area_other, all_crop_area_total, hyv_area_treated_with_chem_fert, other_area_treated_with_chem_fert, total_area_treated_with_chem_fert, fert_qty_hyv, fert_qty_other, fert_qty_total

</details>

#### Land Use Statistics

The Land Use Statistics (LUS) package is a comprehensive collection of official agricultural land use data published by the Directorate of Economics and Statistics, Government of India. It captures how land is utilized across different categories such as cropped area, irrigated land, fallow land, forests, and non agricultural uses.
*Source:* Ministry of Agriculture and Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/land-use-statistics>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Area Under Crops | District | 1998 - 2024 | 36 states/UTs, 742 districts | 1,194,875 | 9: year, area_category, food_category, crop_type, sub_crop_type, crop_name, crop_code, season, area |
| Classification of Area | District | 1998 - 2024 | 36 states/UTs, 742 districts | 181,626 | 5: year, land_use_metrics, area_classification, area_sub_classification, area |
| Crop Wise Irrigated Area | District | 1998 - 2024 | 36 states/UTs, 742 districts | 605,000 | 8: year, food_category, crop_type, sub_crop_type, crop_name, crop_code, season, area |
| Sources of Irrigation | District | 1998 - 2024 | 36 states/UTs, 742 districts | 181,500 | 5: year, irrigated_area_type, area_classification, area_sub_classification, irrigated_area |

#### Minimum Support Price (MSP)

The Minimum Support Price (MSP) is a government-initiated price guarantee, established by the Government of India, to ensure that farmers receive a fair price for their produce, safeguarding them against any sharp fall in market prices. It acts as a safety net, offering an assured return to farmers for specific crops, thus incentivizing them to produce more of these commodities.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/minimum-support-price-msp>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Minimum Support Prices | India | 1998-2025 | — | 819 | 4: year, crop, season, min_support_price |

#### Pradhan Mantri Krishi Sinchai Yojana (PMKSY)

The Pradhan Mantri Krishi Sinchai Yojana (PMKSY) is an initiative launched by the Government of India to ensure comprehensive and sustainable water management for agricultural practices. Introduced with the vision of "Har Khet Ko Paani" (Water for Every Field), the program aims to expand cultivable areas under irrigation, improve on-farm water use efficiency, and ensure the judicious use of water resources.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pradhan-mantri-krishi-sinchai-yojana-pmksy>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| PMKSY MIPMS Physical and Financial Report | District | 2015-2024 | 36 states/UTs, 738 districts | 54,383 | 19: fin_year, month, fin_target_drip, fin_target_sprinkler, total_fin_target, fin_achivement_drip, fin_achivement_sprinkler, total_fin_achievements, p_achievements, phy_target_drip, phy_target_sprinkler, total_phy_target … |

<details><summary>All 19 variables: PMKSY MIPMS Physical and Financial Report</summary>

fin_year, month, fin_target_drip, fin_target_sprinkler, total_fin_target, fin_achivement_drip, fin_achivement_sprinkler, total_fin_achievements, p_achievements, phy_target_drip, phy_target_sprinkler, total_phy_target, phy_achivement_drip, phy_achivement_sprinkler, total_phy_achievements, percnt_achievements, oth_src_phy_achievement_drip, oth_src_phy_achievement_sprinkler, total_oth_src_phy_achievement

</details>

#### Public Distribution System (PDS)

The Public Distribution System (PDS) is a governmental food security program in India, managed by the Ministry of Consumer Affairs, Food, and Public Distribution. It distributes essential commodities like rice, wheat, and kerosene at subsidized rates to eligible beneficiaries through a network of fair price shops.
*Source:* National Food Security Portal, Department of Food & Public Distribution. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/public-distribution-system-pds>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| PDS District Wise Monthly Wheat and Rice | District | 2017-2021 | 36 states/UTs, 717 districts | 28,338 | 5: date, total_rice_allocated, total_wheat_allocated, total_rice_distributed, total_wheat_distributed |

#### Soil Health Card

The Soil Health Card dataset package compiles nationwide soil test results generated under India’s flagship initiative to assess and improve soil fertility. The package integrates data on soil nutrients, chemical properties, micro-nutrient deficiencies, and soil health indicators for millions of farm holdings across all states and union territories.
*Source:* Ministry of Agriculture and Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/soil-health-card>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Soil Nutrient Analysis | Village | 2023 - 2025 | 32 states/UTs, 738 districts, 6,585 sub-districts | 10,853,209 | 5: year, nutrient_type, nutrient_name, nutrient_level, value |

### Economy

#### Agricultural Wages

The Agricultural Wages dataset provides a detailed monthly and annual analysis of wages earned by agricultural laborers in various regions of India. Each entry is localized to a specific Agriculture Market Center, identified not only by its name and code but also by its precise geographical coordinates (latitude and longitude).
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/agricultural-wages>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Agricultural Wages | District | 2010-2020 | 21 states/UTs, 529 districts | 776,112 | 10: month, center_name, center_code, latitude, longitude, labour_category, labour_type, gender, monthly_average_wage, annual_average_wage |

#### Census Housing

India's census housing datasets offer a deep dive into the nation's living conditions. They classify dwellings by type and construction material, shedding light on construction quality. The data also details ownership versus tenancy and essential amenities like water and electricity. Insights into housing size and special housing types, such as hostels, further enrich the picture.
*Source:* Ministry of Home Affairs. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/census-housing>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Census House Wall Material | State | 2011 | 35 states/UTs | 35 | 21: year, total_no_of_census_houses_rural, grass_thatch_bamboo_wood_mud_rural, plastic_polythene_rural, hand_made_tiles_rural, machine_made_tiles_rural, burnt_brick_rural, stone_slate_rural, gi_metal_asbestos_sheet_rural, concrete_rural, any_other_material_rural, total_no_of_households_urban … |
| Census House Condition and Usage | State | 2011 | 35 states/UTs | 35 | 13: year, resi_good_rural, resi_livable_rural, resi_dilapidated_rural, resi_cum_other_use_good_rural, resi_cum_other_use_livable_rural, resi_cum_other_use_dilapidated_rural, resi_good_urban, resi_livable_urban, resi_dilapidated_urban, resi_cum_other_use_good_urban, resi_cum_other_use_livable_urban … |
| Census House Floor Material | State | 2011 | 35 states/UTs | 35 | 25: year, no_of_census_houses, no_of_census_houses_rural, no_of_census_houses_urban, no_of_mud_houses, no_of_mud_houses_rural, no_of_mud_houses_urban, no_of_wood_or_bamboo_houses, no_of_wood_or_bamboo_houses_rural, no_of_wood_or_bamboo_houses_urban, no_of_burnt_brick_houses, no_of_burnt_brick_houses_rural … |
| Census House Utilization | State | 2011 | 35 states/UTs | 35 | 23: year, total_no_vac_houses_rural, occup_house_resid_rural, occp_houses_resid_cum_other_rural, occup_house_shop_office_rural, occup_house_school_college_rural, occup_house_hotel_lodge_rural, occup_house_hosp_rural, occup_houses_fact_rural, occp_house_worship_rural, occup_houses_other_rural, no_locked_census_house_rural … |
| Census Household Amenities | District | 2011 | 35 states/UTs, 640 districts | 1,280 | 144: census_year, hh_category, cond_house_all_total, cond_house_all_good, cond_house_all_livable, cond_house_all_delapidated, cond_house_res_total, cond_house_res_good, cond_house_res_livable, cond_house_res_delapidated, cond_house_res_oth_total, cond_house_res_oth_good … |

<details><summary>All 21 variables: Census House Wall Material</summary>

year, total_no_of_census_houses_rural, grass_thatch_bamboo_wood_mud_rural, plastic_polythene_rural, hand_made_tiles_rural, machine_made_tiles_rural, burnt_brick_rural, stone_slate_rural, gi_metal_asbestos_sheet_rural, concrete_rural, any_other_material_rural, total_no_of_households_urban, grass_thatch_bamboo_wood_mud_urban, plastic_polythene_urban, hand_made_tiles_urban, machine_made_tiles_urban, burnt_brick_urban, stone_slate_urban, gi_metal_asbestos_sheet_urban, concrete_urban, any_other_material_urban

</details>

<details><summary>All 13 variables: Census House Condition and Usage</summary>

year, resi_good_rural, resi_livable_rural, resi_dilapidated_rural, resi_cum_other_use_good_rural, resi_cum_other_use_livable_rural, resi_cum_other_use_dilapidated_rural, resi_good_urban, resi_livable_urban, resi_dilapidated_urban, resi_cum_other_use_good_urban, resi_cum_other_use_livable_urban, resi_cum_other_use_dilapidated_urban

</details>

<details><summary>All 25 variables: Census House Floor Material</summary>

year, no_of_census_houses, no_of_census_houses_rural, no_of_census_houses_urban, no_of_mud_houses, no_of_mud_houses_rural, no_of_mud_houses_urban, no_of_wood_or_bamboo_houses, no_of_wood_or_bamboo_houses_rural, no_of_wood_or_bamboo_houses_urban, no_of_burnt_brick_houses, no_of_burnt_brick_houses_rural, no_of_burnt_brick_houses_urban, no_of_stone_houses, no_of_stone_houses_rural, no_of_stone_houses_urban, no_of_cement_houses, no_of_cement_houses_rural, no_of_cement_houses_urban, no_of_houses_with_mosaic_or_floor_tiles, no_of_houses_with_mosaic_or_floor_tiles_rural, no_of_houses_with_mosaic_or_floor_tiles_urban, no_of_houses_with_any_other_material, no_of_houses_with_any_other_material_rural, no_of_houses_with_any_other_material_urban

</details>

<details><summary>All 23 variables: Census House Utilization</summary>

year, total_no_vac_houses_rural, occup_house_resid_rural, occp_houses_resid_cum_other_rural, occup_house_shop_office_rural, occup_house_school_college_rural, occup_house_hotel_lodge_rural, occup_house_hosp_rural, occup_houses_fact_rural, occp_house_worship_rural, occup_houses_other_rural, no_locked_census_house_rural, total_no_vac_houses_urban, occup_house_resid_urban, occp_houses_resid_cum_other_urban, occup_house_shop_office_urban, occup_house_school_college_urban, occup_house_hotel_lodge_urban, occup_house_hosp_urban, occup_houses_fact_urban, occp_house_worship_urban, occup_houses_other_urban, no_locked_census_house_urban

</details>

<details><summary>All 144 variables: Census Household Amenities</summary>

census_year, hh_category, cond_house_all_total, cond_house_all_good, cond_house_all_livable, cond_house_all_delapidated, cond_house_res_total, cond_house_res_good, cond_house_res_livable, cond_house_res_delapidated, cond_house_res_oth_total, cond_house_res_oth_good, cond_house_res_oth_livable, cond_house_res_oth_delapidated, mor_grass, mor_plastic, mor_hand_tiles, mor_machine_tiles, mor_burnt_brick, mor_stone_slate, mor_gi_metal, mor_concrete, mor_oth, mow_grass, mow_plastic, mow_mud, mow_wood, mow_stone_unpack, mow_stone_pack, mow_gi_metal, mow_burnt_brick, mow_concrete, mow_oth, mof_mud, mof_wood, mof_burnt_brick, mof_stone, mof_cement, mof_mosaic, mof_oth, none_dwell_room, one_dwell_room, two_dwell_room, three_dwell_room, four_dwell_room, five_dwell_room, six_above_dwell_room, hh_size_one, hh_size_two, hh_size_three, hh_size_four, hh_size_five, hh_size_six_eight, hh_size_nine_plus, h_owned, h_rented, h_any_others, mc_none, mc_one, mc_two, mc_three, mc_four, mc_five_plus, sdw_tap_treated, sdw_tap_untreated, sdw_covered_well, sdw_uncovered_well, sdw_handpump, sdw_tube_bore, sdw_spring, sdw_river, sdw_tank, sdw_others, idw_within_premise, idw_near_premise, idw_away_premise, sl_electricity, sl_kerosine, sl_solar, sl_other_oil, sl_any_other, no_light, hhs_lf_within_premise, fl_sewer_piped, fl_septic, fl_other, pl_slab, pl_no_slab, soil_disp_open_drain, sl_ns_rem_human, sl_ns_rem_animal, hhs_lf_outside_premise, public_l, open_l, hhs_bath_f, hhs_bath_noroof, hhs_no_bath_f, wwo_close_drainage, wwo_open_drainage, wwo_no_drainage, fc_firewood, fc_crop_residue, fc_cowdung, fc_coal_types, fc_kerosone, fc_lpg, fc_electricity, fc_biogas, fc_other, fc_no_cooking, kf_total, kf_inside_house, kf_has_i_k, kf_no_i_k, kf_outside_house, kf_has_o_k, kf_no_o_k, kf_no_cooking, hhs_bank_services, avl_radio, avl_tv, avl_comp_int, avl_comp_no_int, avl_landline, avl_mobile, avl_landline_mobile, avl_bicycle, avl_scooter, avl_car, avl_tv_comp_ph_car, avl_none, num_cen_house, num_vacant_cen_house, num_occup_cen_house, occup_res, occup_res_cum_otheruse, occup_shop_off, occup_sch_coll, occup_hot_lodg_guesthoose, occup_hosp_dispen, occup_fact_workshop_workshed, occup_worship_place, occup_oth_non_residen, occup_lockd_cen_house

</details>

#### Company Registrations

The Ministry of Corporate Affairs (MCA) curates a rich collection of datasets that illuminate the corporate landscape of India. Within this trove, one can discern the distribution of Indian companies across states, reflecting the pulse of the nation's domestic corporate sector. Equally revealing is the dataset on foreign company registrations, showcasing the global interest and investment in India's diverse regions.
*Source:* Ministry of Corporate Affairs. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/company-registrations>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Indian Company Registrations | State | 2016-2023 | 36 states/UTs | 1,014,639 | 13: registration_date, cin, roc, company_name, company_status, company_type, company_class, company_category, act_description, company_address, company_email, authorized_capital … |
| Foreign Company Registrations | State | 2016-2023 | 19 states/UTs | 602 | 9: registration_date, fcin, roc, company_name, company_status, act_description, office_type, company_email, company_address |
| Limited Liability Partnership(LLPs) Company Registrations | State | 2016-2023 | 37 states/UTs | 271,252 | 11: incorporation_date, roc, llp_name, llpin, llp_status, designated_partners, total_partners, obligation_of_contribution, act_description, company_email, company_address |
| Foreign Company Registrations New | Company | 2023-2024 | — | 531 | 5: fcin, company_name, registration_date, act_code, act_description |
| Indian Company Registrations New | Company | 2023-2024 | — | 379,386 | 7: cin, company_class, company_name, registration_date, company_type, act_code, act_description |
| Limited Liability Partnership(LLPs) Company Registrations New | Company | 2023-2024 | — | 181,371 | 5: llpin, llp_name, registration_date, act_code, act_description |

<details><summary>All 13 variables: Indian Company Registrations</summary>

registration_date, cin, roc, company_name, company_status, company_type, company_class, company_category, act_description, company_address, company_email, authorized_capital, paidup_capital

</details>

#### Consumer Price Index (CPI)

The Consumer Price Index (CPI) is a statistical measure that tracks the average change over time in the prices paid by consumers for a basket of goods and services. It serves as a key indicator of inflation, reflecting the cost of living and the purchasing power of a currency.
*Source:* Ministry of Statistics and Programme Implementation. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/consumer-price-index-cpi>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Consumer Price Index | State | 2013-2024 | 36 states/UTs, 486 districts | 300,518 | 5: date, commodity_group, sector, cpi, inflation_rate |

#### Direct Benefit Transfer

Direct Benefit Transfer (DBT) is an initiative by the Government of India to ensure the direct transfer of subsidies, grants, and benefits into the bank accounts of beneficiaries, eliminating intermediaries and reducing leakages. Launched in 2013, DBT covers a plethora of schemes across various ministries and departments, ranging from fuel subsidies to scholarships and social welfare programs.
*Source:* Direct Benefit Transfer Mission. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/direct-benefit-transfer>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| DBT District Wise | District | 2019-2023 | 36 states/UTs, 765 districts | 1,000 | 3: fy, total_dbt_transfer, no_of_dbt_transactions |
| DBT State Wise | State | 2019-2023 | 36 states/UTs | 180 | 5: fy, state_score, rank, total_dbt_transfer, no_of_dbt_transactions |

#### Goods and Services Tax

*Source:* Goods and Services Tax Network. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/goods-and-services-tax>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Tax collection on GST Portal | State | 07/2017 to 01/2026 | 28 states/UTs | 3,570 | 5: date, cgst, sgst, igst, cess |
| IGST Settlements | State | 08/2017 to 02/2026 | 28 states/UTs | 3,795 | 3: date, regular_settlement, adhoc_settlement |
| GSTR3B Return Filings | State | 07/2017 to 01/2026 | 28 states/UTs | 3,811 | 6: date, no_of_tax_payers_eligible_to_file, no_of_tax_payers_filed_by_due_date, no_of_tax_payers_filed_after_due_date, total_returns_filed, filing_percentage |
| GSTR1 Return Filings | State | 07/2017 to 01/2026 | 28 states/UTs | 3,768 | 6: date, no_of_tax_payers_eligible_to_file, no_of_tax_payers_filed_by_due_date, no_of_tax_payers_filed_after_due_date, total_returns_filed, filing_percentage |
| GST Registration Statistics | State | 2023 | 38 states/UTs | 36 | 10: date, normal_tapayers, composition_taxpayers, input_service_distributor, casual_taxpayers, tax_collector_at_source, tax_deductor_at_source, non_residential_taxpayers, oidar, uin_holders |
| E-WAY Bills Generated | State | 07/2018 to 02/2026 | 28 states/UTs | 10,143 | 5: date, type_of_supplies, num_of_supplier, num_of_eway_bill, asset_value |

#### Investments

It provides detailed information on various mutual fund schemes, including their performance metrics, asset management details, and fund mobilization statistics. This dataset is particularly useful for financial analysts, investors, and policymakers who seek to understand the dynamics of the mutual fund industry in India.
*Source:* Association of Mutual Funds in India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/investments>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Mutual Funds Report | All India | 2019-2024 | — | 3,115 | 13: month, scheme_name, scheme_type, scheme_category, no_of_schemes, no_of_folios, fund_mobilized, repurchase_redemption, net_inflow_outflow, net_aum, avg_net_aum, no_of_segregated_portfolios … |

<details><summary>All 13 variables: Mutual Funds Report</summary>

month, scheme_name, scheme_type, scheme_category, no_of_schemes, no_of_folios, fund_mobilized, repurchase_redemption, net_inflow_outflow, net_aum, avg_net_aum, no_of_segregated_portfolios, net_aum_in_segregated_portfolios

</details>

#### National Payments Corporation of India (NPCI)

The National Payments Corporation of India (NPCI) is an umbrella organization overseeing the retail payments and settlement systems in India, founded with the support of the Reserve Bank of India (RBI) and the Indian Banks' Association (IBA). It aims to foster innovation in payment systems, ensuring they are reliable, secure, and accessible to all citizens.
*Source:* National Electronic Toll Collection, NPCI. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/national-payments-corporation-of-india-npci>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| NETC FASTag Acquirer Bank Transactions Approved/BD/TD Statistics | Bank | 01-09-2021 to 31-07-2022 | — | 100 | 6: month, acquirer_bank, transaction_volume, approved_percent, bd_percent, td_percent |
| NETC FASTag Issuer Bank Approved Transactions Statistics | Bank | 01-09-2021 to 31-07-2022 | — | 273 | 5: month, issuer_bank, transaction_volume, approved_percent, deemed_approved_percent |
| Product Wise Declined (Business/Technical) Transactions | Bank | 2021-2023 | — | 2,300 | 7: date, product, issuer_bank, total_volume, approved_transaction_volume, business_decline_transactions, technical_decline_transactions |
| UPI Product Statistics | India | 2016-2023 | — | 89 | 4: date, num_of_banks_live_on_upi, volume, value |
| UPI Transactions - P2P and P2M | India | 04/2021-08/2022 | — | 41 | 7: month, total_vol, total_val, p2p_vol, p2p_val, p2m_vol, p2m_val |

#### Survey of Industries

The "Survey of Industries" package offers annual data on the economic landscape of different industries. It includes sector-wise analysis, economic indicators, regional insights, policy impacts, comparative assessments, and forecasts. This dataset is valuable for policymakers, economists, analysts, and businesses for understanding industry dynamics and making informed decisions.
*Source:* Ministry of Statistics & Programme Implementation. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/survey-of-industries>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Annual Economic Landscape of Industries | State | 2011-2020 | 36 states/UTs | 324 | 15: year, factories, fixed_capital, productive_capital, invested_capital, workers, total_persons_engages, wages_to_wages, total_emoluments, total_input, total_output, depriciation … |

<details><summary>All 15 variables: Annual Economic Landscape of Industries</summary>

year, factories, fixed_capital, productive_capital, invested_capital, workers, total_persons_engages, wages_to_wages, total_emoluments, total_input, total_output, depriciation, net_value_added, rent_paid, interest_paid

</details>

#### Unincorporated Non-Agriculture Enterprises Excluding Construction (NSSO)

The Unincorporated Non-Agriculture Enterprises Excluding Construction (NSSO) offers detailed information on informal non-agricultural businesses in India, excluding construction. It covers aspects like enterprise size, sector distribution, employment, productivity, and financial performance.
*Source:* Ministry of Statistics & Programme Implementation. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/unincorporated-nonagriculture-enterprises-excluding-construction-nsso>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Non-Agricultural Enterprise Analysis | State | 2016 | 36 states/UTs | 1,296 | 93: year, sector, enterprise_type, activity, no_enterprises, msme_micro, msme_small, msme_medium, msme_total, non_msme, female_employees, male_employees … |

<details><summary>All 93 variables: Non-Agricultural Enterprise Analysis</summary>

year, sector, enterprise_type, activity, no_enterprises, msme_micro, msme_small, msme_medium, msme_total, non_msme, female_employees, male_employees, total_employees, formal_ann_salary, informal_ann_salary, all_ann_salary, less_than_4hours, hours_4to7, more_than_8hours, wh_not_reported, gross_value_added, per_employee_gva, per_enterprise_gva, within_hh, fixed, temporary_kiosk, no_fixed, mobile, total_outsidehh, ent_notreported, avg_gva_lessthan4hr, avg_gv_4to8hr, avg_gva_above8hr, avg_gva_all, proprietary_male, proprietary_female, proprietary_same_hh, proprietary_diff_hh, proprietary_shg, proprietary_trust, proprietary_others, proprietary_nr, perennial, seasonal, casual, operation_nr, own_management, usual_discharge, road_river_nala, not_generated_lw, local_civicauthority, authorised_ground, own_system, road_side, noprovision_thers, not_generated_sw, no_assistance, financial_loan, subsidy, machinery_equipment, skill_devlopment, marketing, raw_material, other_assistance, no_problems, power_cuts, shortage_raw_materials, fall_demand, high_cost_credit, non_recovery_financial_dues, non_available_labours, non_available_skilled_labour, labour_disputes, problems_others, not_registered, establishment_act, local_body, sales_tax_act, provident_fund_act, esc_act, stock_exchange, other_industry_act, donation_grants, major_receipt_others, not_any, data_collected, data_not_collected, no_accounts, st, sc, obc, social_groups_other, unknown

</details>

#### Union Budget

The Union Budget package is a comprehensive collection of datasets provided by the Ministry of Finance, offering a detailed view of the financial management and fiscal planning of the Government of India. This package encapsulates various components of the Union Budget, which is the annual financial statement presented by the government, detailing its revenue and expenditure for the upcoming fiscal year.
*Source:* Ministry of Finance. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/union-budget>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Capital Receipts | India | 2015-2026 | — | 3,257 | 7: year, major_head, estimate_type, major_category, minor_category, sub_category, value |
| Budget At A Glance | India | 2015-2026 | — | 497 | 4: year, particular, estimate_type, value |
| Non Tax Receipts | India | 2015-2026 | — | 2,762 | 7: year, major_head, estimate_type, major_category, minor_category, sub_category, value |
| Outlay on Major Schemes | India | 2015-2026 | — | 3,589 | 5: year, scheme, scheme_type, estimate_type, value |
| Tax Receipts | India | 2015-2026 | — | 2,519 | 7: year, major_head, estimate_type, major_category, minor_category, sub_category, value |
| Ministry-wise Expenditure | India | 2015-2026 | — | 7,956 | 9: year, ministry, department, estimate_type, head_type, gross, recoveries, receipts, net |

#### VAHAN Vehicle Registrations

The "VAHAN Vehicle Registrations" dataset provides comprehensive data on vehicle registrations across India, offering insights into various aspects such as vehicle norms, manufacturers, fuel types, categories, and classes.
*Source:* Ministry of Road Transport and Highways. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/vahan-vehicle-registrations>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| VAHAN Vehicle Registrations | Regional Transport Office | 2019-2025 | 34 states/UTs | — | not previewable on the portal (download to inspect) |

### Financial Inclusion

#### Debt and Investment (NSSO)

The "Debt and Investment" provides comprehensive data on household debt, investments, and asset holdings in India. This package is instrumental for understanding the economic behavior, financial health, and investment patterns of Indian households across various demographic and socio-economic segments.
*Source:* National Sample Survey Organisation. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/debt-and-investment-nsso>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Debt, Investment, and Asset Analysis | State | 2013 | 36 states/UTs | 324 | 12: year, sector, occupation, no_of_hh, fxd_cap_exp, hh_reporting_fxd_cap_exp, land_purchase_exp, hh_reporting_land_purchase, avg_value_assets, avg_amount_of_debt, incidence_of_indebtedness, debt_asset_ratio |

#### Mudra Loans

The Pradhan Mantri Mudra Yojana (PMMY), commonly known as Mudra Loans, is an initiative launched by the Government of India to facilitate micro-credit to non-corporate, non-farm small and micro enterprises. Introduced under the Micro Units Development & Refinance Agency Ltd.
*Source:* Ministry Of Home Affairs. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/mudra-loans>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| State Performance | State | 2015-2023 | 36 states/UTs | 284 | 10: year, shishu_accounts, shishu_sanction_amt, shishu_disbursment_amt, kishore_accounts, kishore_sanction_amt, kishore_disbursment_amt, tarun_accounts, tarun_sanction_amt, tarun_disbursment_amt |
| Overall Performance | India | 2015-2023 | — | 105 | 14: year, category, shishu_accounts, shishu_sanction_amt, shishu_disbursment_amt, shishu_outstanding_amt, kishore_accounts, kishore_sanction_amt, kishore_disbursment_amt, kishore_outstanding_amt, tarun_accounts, tarun_sanction_amt … |
| Bank Performance | India | 2015-2023 | — | 1,150 | 13: year, bank_type, bank_name, sponser_bank, shishu_accounts, shishu_sanction_amt, shishu_disbursment_amt, kishore_accounts, kishore_sanction_amt, kishore_disbursment_amt, tarun_accounts, tarun_sanction_amt … |

<details><summary>All 14 variables: Overall Performance</summary>

year, category, shishu_accounts, shishu_sanction_amt, shishu_disbursment_amt, shishu_outstanding_amt, kishore_accounts, kishore_sanction_amt, kishore_disbursment_amt, kishore_outstanding_amt, tarun_accounts, tarun_sanction_amt, tarun_disbursment_amt, tarun_outstanding_amt

</details>

<details><summary>All 13 variables: Bank Performance</summary>

year, bank_type, bank_name, sponser_bank, shishu_accounts, shishu_sanction_amt, shishu_disbursment_amt, kishore_accounts, kishore_sanction_amt, kishore_disbursment_amt, tarun_accounts, tarun_sanction_amt, tarun_disbursment_amt

</details>

#### NABARD All India Rural Financial Inclusion Survey (NAFIS)

The NABARD All India Rural Financial Inclusion Survey (NAFIS) provides data on the financial inclusion status of rural households in India. The data was collected in 2016-17 and includes information on bank account ownership, credit access, insurance coverage, financial literacy and household economic status.
*Source:* National Bank for Agriculture and Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/nabard-all-india-rural-financial-inclusion-survey-nafis>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| NABARD All India Rural Financial Inclusion Survey 2016 (NAFIS) | State | 2016-17 | 29 states/UTs | 30 | 9: year, consm_exp, prop_saving, avg_saving_yr, prop_hh_indebt, prop_hh_microfin, avg_land_size, hh_income_monthly, agri_hh_income_monthly |

#### NRLM (National Rural Livelihoods Mission)

The package offers a powerful lens into the rural self-help group (SHG) ecosystem in India, capturing detailed data on member demographics, financial inclusion, and institutional support. It includes indicators on gender, caste, religion, disability, and poverty levels, alongside insights into Aadhaar linkage, bank account access, and SECC integration.
*Source:* Ministry of Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/nrlm-national-rural-livelihoods-mission>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| SHG And Member Profile | SHG | 2016-2023 | 34 states/UTs, 739 districts, 212,305 panchayats | 8,055,306 | 11: shg_name, shg_code, shg_type, total_mem_details, mem_with_aadhar, mem_with_bankac, mem_with_aadharseededac, mem_with_secc_tin_no, mem_without_aadhar, mem_without_bankac, mem_without_aadharseedac |
| SHG Financial and Member Profile Details | SHG | nan | 33 states/UTs, 740 districts, 242,220 panchayats | 9,318,153 | 28: shg_name, shg_id, date_of_formation, shg_type, promoted_by, bank_name, bank_branch_name, date_of_opening_of_account, total_members, female, male, scheduled_caste … |
| SHG Loan Details Block Level | Block | nan | 34 states/UTs, 751 districts, 6,938 sub-districts | 6,938 | 2: shg_count, loan_amount |

<details><summary>All 28 variables: SHG Financial and Member Profile Details</summary>

shg_name, shg_id, date_of_formation, shg_type, promoted_by, bank_name, bank_branch_name, date_of_opening_of_account, total_members, female, male, scheduled_caste, scheduled_tribe, other_backwards_class, other_social_category, self_disabled, family_member_disabled, hindu, christian, muslim, sikh, buddhist, jain, parsi, apl, bpl, pip_category_pop, pip_category_poor

</details>

#### Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)

The Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY) is a government-backed life insurance scheme launched by the Government of India. Designed to be affordable, it offers a life insurance cover of ₹2 lakh with an annual premium of just ₹330 for individuals aged between 18 to 50 years. The scheme is available to people with a savings bank account who give their consent to join and enable auto-debit.
*Source:* Ministry of Finance. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pradhan-mantri-jeevan-jyoti-bima-yojana-pmjjby>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Pradhan Mantri Jeevan Jyoti Bima Yojana Monthly Claims | India | 2019-2023 | — | 49 | 4: month, claims_received, claims_disbursed, gross_enrollment |

#### Prime Minsters Employment Generation Programme (PMEGP)

The Prime Minister's Employment Generation Programme (PMEGP) is a flagship initiative by the Government of India to stimulate employment generation through micro-enterprise establishments in the non-farm sector.
*Source:* Ministry of Micro, Small and Medium Enterprises. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/prime-minsters-employment-generation-programme-pmegp>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| PMEGP State Wise | State | 2016-2023 | 31 states/UTs | 894 | 12: year, bank_name, mm_claim_prj, mm_claimed, claims_under_process_kvic_prj, claims_under_process_kvic_mm, referred_for_rectification_prj, referred_for_rectification_mm, mm_disbursed_corp_bank_prj, mm_disbursed_corp_bank, mm_released_prj, mm_released |
| PMEGP Bank Wise | Bank | 2016-2023 | — | 740 | 14: year, bank_name, mm_claimed_nos_of_prj, mm_claimed_mm, mm_recommended_for_mm_release_nos_of_prj, mm_recommended_for_mm_release_mm, mm_claims_under_process_nos_of_prj, mm_claims_under_process_mm, refer_to_kvic_field_ofc_for_rectif_nos_of_prj, refer_to_kvic_field_ofc_for_rectif_mm, mm_disbursed_nos_of_prj, mm_disbursed_mm_inv … |

<details><summary>All 14 variables: PMEGP Bank Wise</summary>

year, bank_name, mm_claimed_nos_of_prj, mm_claimed_mm, mm_recommended_for_mm_release_nos_of_prj, mm_recommended_for_mm_release_mm, mm_claims_under_process_nos_of_prj, mm_claims_under_process_mm, refer_to_kvic_field_ofc_for_rectif_nos_of_prj, refer_to_kvic_field_ofc_for_rectif_mm, mm_disbursed_nos_of_prj, mm_disbursed_mm_inv, mm_released_no_of_project, mm_released_mm_inv

</details>

#### Reserve Bank of India

The Reserve Bank of India (RBI) is the central banking institution of India, responsible for the issuance and supply of the Indian Rupee and the regulation of the money market. In the context of data and information, RBI plays a pivotal role by regularly publishing a plethora of economic indicators, reports, and research.
*Source:* Reserve Bank of India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/reserve-bank-of-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| RBI Daily Digital Payments | India | 2020-2025 | — | 1,919 | 49: date, rtgs_vol, rtgs_val, neft_vol, neft_val, aeps_vol, aeps_val, upi_vol, upi_val, imps_vol, imps_val, nach_credit_vol … |
| Money Stock M3 | India | 2001-2024 | — | 625 | 14: date, m3, currency_with_public, demand_deposits_with_banks, time_deposits_with_banks, other_deposits_with_rbi, reserve_bank_crd_to_gov_src, other_banks_crd_to_gov_src, reserve_bank_crd_to_comm_sctr_src, other_banks_crd_to_comm_sctr_src, net_foreign_exchange_assets_src, gov_currency_liab_to_public_src … |
| Population-group Wise Deposits | District | 2019-2022 | 36 states/UTs, 717 districts | 14,037 | 6: year, region, population_group, no_of_offices, no_of_accounts, deposit_amount |
| Bank-group Wise Deposits | District | 2009-10 to 2017-18 | 36 states/UTs, 717 districts | 51,579 | 5: year, bank_group, population_group, number_of_deposits, deposits |
| Bankwise ATM POS Card Statistics 2022 onwards | All India | 2022-2025 | — | 3,183 | 29: date, bank_category, bank_name, atms_crms_onsite, atms_crms_offsite, pos, micro_atms, bharat_qr, upi_qr, credit_cards, debit_cards, cc_pay_trns_at_pos_vol … |
| Credit by Scheduled Commercial Banks | District | 2010-2023 | 36 states/UTs, 764 districts | 1,716,034 | 9: year, region, population_group, bank_group, occupation_group, occupation_sub_group, no_of_accounts, credit_limit, amount_outstanding |
| ECS Transaction Metrics | Bank | 2013 to 2020 | — | 7,562 | 9: month, center_name, bank_name, ecs_credit_users, ecs_credit_vol, ecs_credit_val, ecs_debit_users, ecs_debit_vol, ecs_debit_val |
| Internet Banking Statistics | Bank | 2022-2025 | — | 9,630 | 5: month, bank_name, no_of_transactions, amt_of_transactions, active_users |
| Bank Wise RTGS Inward and Outward | Bank | 2008-2025 | — | 78,590 | 18: month, bank_name, inward_interbank_volume, inward_costumer_volume, inward_total_volume, inward_percentage_volume, inward_interbank_amt, inward_costumer_amt, inward_total_amt, inward_percentage_amt, outward_interbank_volume, outward_costumer_volume … |
| Mobile Banking Statistics | Bank | 2013-2025 | — | 45,222 | 5: month, bank_name, no_of_transactions, amt_of_transactions, no_of_active_costumers |
| NEFT Transaction Metrics | Bank | 2008-2025 | — | 72,746 | 6: month, bank_name, no_of_debit_transactions, amt_of_debit_transactions, no_of_credit_transactions, amt_of_credit_transactions |
| Bank Outlets and ATM's | Point | 1900-2023 | 34 states/UTs, 753 districts, 5,989 sub-districts | 1,280,386 | 19: region, center, branch, address, longitude, lattitude, bank_group, population_group, domestic_overseas, type, status_type, bank … |
| Bankwise ATM POS Card Statistics 2011-2022 | All India | 2011-2022 | — | 7,389 | 18: date, bank_name, atms_onsite, atms_offsite, pos_online, pos_offline, cc_outstanding_cards_eom, cc_trans_atm, cc_trans_pos, cc_amt_atm, cc_amt_pos, dc_outstanding_cards_eom … |

<details><summary>All 49 variables: RBI Daily Digital Payments</summary>

date, rtgs_vol, rtgs_val, neft_vol, neft_val, aeps_vol, aeps_val, upi_vol, upi_val, imps_vol, imps_val, nach_credit_vol, nach_credit_val, nach_debit_vol, nach_debit_val, netc_vol, netc_val, bbps_vol, bbps_val, cts_vol, cts_val, credit_card_at_pos_and_e_commerce_vol, credit_card_at_pos_and_e_commerce_val, debit_card_at_pos_and_e_commerce_vol, debit_card_at_pos_and_e_commerce_val, ppis_card_at_pos_and_e_commerce_vol, ppis_card_at_pos_and_e_commerce_val, nfs_through_atms_vol, nfs_through_atms_val, aeps_through_micro_atms_or_bcs_vol, aeps_through_micro_atms_or_bcs_val, credit_card_at_pos_vol, credit_card_at_pos_val, credit_card_at_e_commerce_vol, credit_card_at_e_commerce_val, debit_card_at_pos_vol, debit_card_at_pos_val, debit_card_at_e_commerce_vol, debit_card_at_e_commerce_val, ppis_card_at_pos_vol, ppis_card_at_pos_val, ppis_card_at_e_commerce_vol, ppis_card_at_e_commerce_val, government_securities_clearing_vol, government_securities_clearing_val, forex_clearing_vol, forex_clearing_val, rupee_derivatives_vol, rupee_derivatives_val

</details>

<details><summary>All 14 variables: Money Stock M3</summary>

date, m3, currency_with_public, demand_deposits_with_banks, time_deposits_with_banks, other_deposits_with_rbi, reserve_bank_crd_to_gov_src, other_banks_crd_to_gov_src, reserve_bank_crd_to_comm_sctr_src, other_banks_crd_to_comm_sctr_src, net_foreign_exchange_assets_src, gov_currency_liab_to_public_src, net_non_monetary_liab_bnk_sctr_src, net_non_monetary_liab_rbi_src

</details>

<details><summary>All 29 variables: Bankwise ATM POS Card Statistics 2022 onwards</summary>

date, bank_category, bank_name, atms_crms_onsite, atms_crms_offsite, pos, micro_atms, bharat_qr, upi_qr, credit_cards, debit_cards, cc_pay_trns_at_pos_vol, cc_pay_trns_at_pos_val, cc_pay_trns_online_vol, cc_pay_trns_online_val, cc_pay_trns_other_vol, cc_pay_trns_other_val, cc_cash_withdraw_atm_val, cc_cash_withdraw_atm_vol, dc_pay_trns_at_pos_vol, dc_pay_trns_at_pos_val, dc_pay_trns_online_vol, dc_pay_trns_online_val, dc_pay_trns_other_vol, dc_pay_trns_other_val, dc_cash_withdraw_atm_val, dc_cash_withdraw_atm_vol, dc_cash_withdraw_pos_val, dc_cash_withdraw_pos_vol

</details>

<details><summary>All 18 variables: Bank Wise RTGS Inward and Outward</summary>

month, bank_name, inward_interbank_volume, inward_costumer_volume, inward_total_volume, inward_percentage_volume, inward_interbank_amt, inward_costumer_amt, inward_total_amt, inward_percentage_amt, outward_interbank_volume, outward_costumer_volume, outward_total_volume, outward_percentage_volume, outward_interbank_amt, outward_costumer_amt, outward_total_amt, outward_percentage_amt

</details>

<details><summary>All 19 variables: Bank Outlets and ATM's</summary>

region, center, branch, address, longitude, lattitude, bank_group, population_group, domestic_overseas, type, status_type, bank, micrcode, license_number, ifsccode, part_1_code, closed_reason, license_date, actual_open_date

</details>

<details><summary>All 18 variables: Bankwise ATM POS Card Statistics 2011-2022</summary>

date, bank_name, atms_onsite, atms_offsite, pos_online, pos_offline, cc_outstanding_cards_eom, cc_trans_atm, cc_trans_pos, cc_amt_atm, cc_amt_pos, dc_outstanding_cards_eom, dc_trans_atm, dc_trans_pos, dc_amt_atm, dc_amt_pos, micro_atms, bharat_qr

</details>

#### SHG Financial and Member Profile Details

This dataset provides an extensive and nuanced profile of Self-Help Groups (SHGs) across diverse geographic and socio-economic contexts. It includes detailed information on the SHG's location, specifying the state, district, block, Gram Panchayat, and village, alongside a unique SHG identifier and its name.
*Source:* Ministry of Rural Development. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/shg-financial-and-member-profile-details>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| SHG Financial and Member Profile Details | SHG | Cross-section | 33 states/UTs, 740 districts, 242,220 panchayats | — | not previewable on the portal (download to inspect) |

### Commerce

#### Export Trade Statistics

This package comprises multiple datasets detailing India's trade statistics from 2017 onwards, segmented by exports with various regions worldwide: Africa, Antarctica, Asia, Europe, America, Oceania, and Unspecified regions. The datasets, sourced from the official government database, offer monthly frequency data including the type of products traded, their monetary values in both USD and INR, and quantities.
*Source:* Directorate General of Commercial Intelligence and Statistics. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/export-trade-statistics>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Exports to Asian Countries | Country | 2015-2025 | — | 5,541,809 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to African Countries | Country | 2015-2025 | — | 2,826,373 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to Unspecified Countries | Country | 2015-2025 | — | 65,061 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to Oceanic Countries | Country | 2015-2025 | — | 481,293 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to European Countries | Country | 2015-2025 | — | 2,928,093 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to Antartica Countries | Country | 2015-2025 | — | 55 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Exports to American Countries | Country | 2015-2025 | — | 1,833,987 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |

<details><summary>All 14 variables: Exports to Asian Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to African Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to Unspecified Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to Oceanic Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to European Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to Antartica Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Exports to American Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

#### Exports and Imports (India)

The "Exports and Imports of India" dataset provides a comprehensive view of trade exports and imports of India across the globe. This dataset covers the periodical monthly data of exports in terms of value in both USD and INR and also in terms of quantity.
*Source:* Directorate General of Commercial Intelligence and Statistics. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/exports-imports-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Exports and Imports (India) | Country | 2007-2025 | — | — | not previewable on the portal (download to inspect) |

#### Exports and Imports (Port-level)

The Port Level Import-Export Dataset offers comprehensive data on both imports and exports at the principal commodity level, recorded through various ports across different states of India. It includes detailed information about the volume, value, and commodity types of imports and exports, with values provided in both USD and INR.
*Source:* Directorate General of Commercial Intelligence and Statistics. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/export-imports-port-level>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Exports and Imports (Port-level) | Port | 2018-2025 | 29 states/UTs | — | not previewable on the portal (download to inspect) |

#### Import Trade Statistics

This package comprises multiple datasets detailing India's trade statistics over the last five years, segmented by imports with various regions worldwide: Africa, Antarctica, Asia, Europe, North America, Oceania, South America, and Unspecified regions.
*Source:* Directorate General of Commercial Intelligence and Statistics. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/import-trade-statistics>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Imports from African Countries | Country | 2015-2025 | — | 149,183 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, commodity_qt … |
| Imports from Antarctica Countries | Country | 2015-2025 | — | 74 | 14: date, country_name, alpha_3_code, country_code, region, region_code, sub_region, sub_region_code, hs_code, commodity, unit, value_qt … |
| Imports from European Countries | Country | 2015-2025 | — | 2,901,433 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Imports from Asian Countries | Country | 2015-2025 | — | 3,188,530 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Imports from Oceanic Countries | Country | 2017-2025 | — | 97,854 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Imports from Unspecified Countries | Country | 2015-2025 | — | 18,295 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |
| Imports from American Countries | Country | 2015-2025 | — | 704,114 | 14: date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt … |

<details><summary>All 14 variables: Imports from African Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, commodity_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from Antarctica Countries</summary>

date, country_name, alpha_3_code, country_code, region, region_code, sub_region, sub_region_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from European Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from Asian Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from Oceanic Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from Unspecified Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

<details><summary>All 14 variables: Imports from American Countries</summary>

date, country_name, alpha_3_code, country_code, region_name, region_code, subregion_name, subregion_code, hs_code, commodity, unit, value_qt, value_rs, value_dl

</details>

#### Port Level Exports and Imports

The Port Level Exports and Imports package enables efficient analysis of import and export data at the port level. It allows users to retrieve and process trade data, handle missing values, and generate reports on trade volume and value by port. Designed for trade analysts and businesses, it simplifies monitoring of commodity flows and provides insights into global trade activities.
*Source:* Directorate General of Commercial Intelligence and Statistics. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/port-level-exports-and-imports>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Exports at Principal Commodity Level | State | 2018-2023 | 29 states/UTs | 6,912,492 | 9: date, country, port, pc_code, commodity, units, quantity, dollars_value, inr_value |
| Imports at Principal Commodity Level | State | 2018-2023 | 28 states/UTs | 3,365,711 | 9: date, country, port, pc_code, commodity, units, quantity, dollars_value, inr_value |

#### Price Monitoring

The Price Monitoring package offers a detailed view into the dynamic pricing landscape of essential commodities in India, encompassing both retail and wholesale levels. This comprehensive dataset not only includes daily retail prices from various states but is also set to integrate wholesale price data and additional information from diverse sources.
*Source:* Department of Consumer Affairs. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/price-monitoring>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Daily Retail Prices Of Essential Commodities | State | 2015-2023 | 34 states/UTs | 1,901,416 | 3: date, commodity, price |
| India Level Daily Wholesale Price | All India | 2015 - 2024 | — | 72,732 | 6: date, commodity, average_price, maximum_price, minimum_price, modal_price |
| State Level Daily Wholesale Price | State | 2015 - 2024 | 34 states/UTs | 2,015,860 | 3: date, commodity, price |

#### Trends in Prices of Specific Commodities

This collection will have datasets for various commodities like coffee, tea, rubber, jute, silk, cardamom etc. These datasets will provide valuable information about prices, production of such commercial commodities.
*Source:* Spices Board India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/trends-in-prices-of-specific-commodities>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Large Cardamom Prices | Market Center | 2015-2023 | 2 states/UTs | 3,284 | 4: date, market, type, price |

### Socio Economic

#### Census PCA Demography

*Source:* Registrar General of India and Ministry of Home Affairs (MHA). *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/census-pca-demography>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Census PCA Demography - States | State | 2011 | 36 states/UTs | 9,630 | 11: year, rural_urban, level, gender, age, social_group, literacy, working_status, worker_type, occupation, population |
| Census PCA Demography - Districts | District | 2011 | 36 states/UTs, 729 districts | 188,910 | 11: year, rural_urban, level, gender, age, social_group, literacy, working_status, worker_type, occupation, population |
| Census PCA Demography - Blocks | Village | 2011 | 36 states/UTs, 729 districts, 7,127 sub-districts | 1,700,721 | 11: year, rural_urban, level, gender, age, social_group, literacy, working_status, worker_type, occupation, population |
| Census PCA Demography - Subdistricts | Sub District | 2011 | 36 states/UTs, 729 districts | 1,184,295 | 11: year, rural_urban, level, gender, age, social_group, literacy, working_status, worker_type, occupation, population |

#### Mission Antyodaya

Mission Antyodaya is an initiative launched by the Department of Rural Development under the Ministry of Rural Development, Government of India, aimed at creating poverty-free Gram Panchayats in a time-bound manner. The mission strives to ensure the holistic development of villages by focusing on various parameters such as health, nutrition, education, sanitation, and livelihood.
*Source:* Ministry of Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/mission-antyodaya>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Block Level Infrastructure | Block | 2020 | 32 states/UTs, 711 districts, 7,104 sub-districts | 7,113 | 88: date, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km … |
| District Level Infrastructure | District | 2019 | 32 states/UTs, 706 districts | 713 | 88: year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km … |
| Panchayat Level Infrastructure | Panchayat | 2020 | 32 states/UTs, 711 districts, 7,104 sub-districts, 267,126 panchayats, 648,245 villages | 267,343 | 88: year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km … |
| State Level Infrastructure | State | 2020 | 33 states/UTs | 32 | 88: year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km … |
| Village Level Infrastructure | Village | 2020 | 32 states/UTs, 711 districts, 253,692 panchayats | 632,621 | 41: year, tot_pop, pop_male, pop_female, tot_hh, bank, bank_distance, bc_w_internet, atm, internet_bb, all_weather_road, cc_road … |
| Village Agriculture Report | Village | 2020 | 32 states/UTs, 711 districts, 7,106 sub-districts, 253,689 panchayats, 625,928 villages | 632,583 | 11: year, tot_hh, farm_activity_hhs, non_farm_activity_hhs, govt_seed_centres, watershed_dev_projects, community_rainwater_harvesting, farmers_collectives, food_grain_warehouses, primary_processing_facilities, custom_hiring_centres |
| Village Basic Facilities | Village | 2020 | 32 states/UTs, 711 districts, 7,106 sub-districts, 253,682 panchayats | 632,611 | 26: year, banks, atm, all_weather_road_connectivity, internal_pucca_roads, public_transport, common_service_centre, domestic_electricity_hrs, pds, market_facilities, piped_tap_water, telephone_services … |
| Village Level Drinking water | Village | 2020 | 32 states/UTs, 711 districts, 7,106 sub-districts, 7,106 panchayats | 632,396 | 4: year, total_households, avail_piped_tap_water, hhs_piped_water_conn |
| Rural Housing Report | Village | 2020 | 32 states/UTs, 711 districts, 7,106 sub-districts, 253,688 panchayats | 632,668 | 7: year, hh_kutcha_wall_roof, perct_hh_kutcha_wall_roof, pmay_house, pmay_permanent_wait_list, any_state_housing_scheme, any_state_housing_permanent_wait_list |

<details><summary>All 88 variables: Block Level Infrastructure</summary>

date, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km, bc_w_internet, atm, internet_bb, all_weather_road, cc_road_full, cc_road_partial, cc_road_not, pub_trans_bus, pub_trans_van, pub_trans_auto, pub_trans_no, railway, csc_panchayat, csc_seperate, csc_not, elec_domes_1hrs, elec_domes_4hrs, elec_domes_8hrs, elec_domes_12hrs, elec_domes_no, elec_msme, pds, mandi, reg_mkt, weekly_haat, mkt_na, tap_100, tap_50, tap_l50, tap_one_hab, tap_na, tel_ll, tel_mob, tel_both, tel_na, clean_energy_hhs, solar_wind_elect, kuccha_hhs, po_sub_po, panch_bhawan, pib_na, pib_av_upd, pib_av_not_upd, prim_school, middle_school, high_school, high_second_school, degree_clg, school_college_na, public_library, indoor_sports, outdoor_sports, both_sports, no_sports, vocational, chc, phc, subcentre, no_health, subcentre_l1km, subcentre_2km, subcentre_5km, subcentre_10km, subcentre_g10km, veterinary, veterinary_l1km, veterinary_2km, veterinary_5km, veterinary_10km, veterinary_g10km, closed_drain, pucca_slab_drain, pucca_uncovered_drain, kuchha_drain, no_drain, pcomm_pasture

</details>

<details><summary>All 88 variables: District Level Infrastructure</summary>

year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km, bc_w_internet, atm, internet_bb, all_weather_road, cc_road_full, cc_road_partial, cc_road_not, pub_trans_bus, pub_trans_van, pub_trans_auto, pub_trans_no, railway, csc_panchayat, csc_seperate, csc_not, elec_domes_1hrs, elec_domes_4hrs, elec_domes_8hrs, elec_domes_12hrs, elec_domes_no, elec_msme, pds, mandi, reg_mkt, weekly_haat, mkt_na, tap_100, tap_50, tap_l50, tap_one_hab, tap_na, tel_ll, tel_mob, tel_both, tel_na, clean_energy_hhs, solar_wind_elect, kuccha_hhs, po_sub_po, panch_bhawan, pib_na, pib_av_upd, pib_av_not_upd, prim_school, middle_school, high_school, high_second_school, degree_clg, school_college_na, public_library, indoor_sports, outdoor_sports, both_sports, no_sports, vocational, chc, phc, subcentre, no_health, subcentre_l1km, subcentre_2km, subcentre_5km, subcentre_10km, subcentre_g10km, veterinary, veterinary_l1km, veterinary_2km, veterinary_5km, veterinary_10km, veterinary_g10km, closed_drain, pucca_slab_drain, pucca_uncovered_drain, kuchha_drain, no_drain, pcomm_pasture

</details>

<details><summary>All 88 variables: Panchayat Level Infrastructure</summary>

year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km, bc_w_internet, atm, internet_bb, all_weather_road, cc_road_full, cc_road_partial, cc_road_not, pub_trans_bus, pub_trans_van, pub_trans_auto, pub_trans_no, railway, csc_panchayat, csc_seperate, csc_not, elec_domes_1hrs, elec_domes_4hrs, elec_domes_8hrs, elec_domes_12hrs, elec_domes_no, elec_msme, pds, mandi, reg_mkt, weekly_haat, mkt_na, tap_100, tap_50, tap_l50, tap_one_hab, tap_na, tel_ll, tel_mob, tel_both, tel_na, clean_energy_hhs, solar_wind_elect, kuccha_hhs, po_sub_po, panch_bhawan, pib_na, pib_av_upd, pib_av_not_upd, prim_school, middle_school, high_school, high_second_school, degree_clg, school_college_na, public_library, indoor_sports, outdoor_sports, both_sports, no_sports, vocational, chc, phc, subcentre, no_health, subcentre_l1km, subcentre_2km, subcentre_5km, subcentre_10km, subcentre_g10km, veterinary, veterinary_l1km, veterinary_2km, veterinary_5km, veterinary_10km, veterinary_g10km, closed_drain, pucca_slab_drain, pucca_uncovered_drain, kuchha_drain, no_drain, pcomm_pasture

</details>

<details><summary>All 88 variables: State Level Infrastructure</summary>

year, villages_surveyed, tot_pop, pop_male, pop_female, tot_hh, bank, bank_dist_l1km, bank_dist_2km, bank_dist_5km, bank_dist_10km, bank_dist_g10_km, bc_w_internet, atm, internet_bb, all_weather_road, cc_road_full, cc_road_partial, cc_road_not, pub_trans_bus, pub_trans_van, pub_trans_auto, pub_trans_no, railway, csc_panchayat, csc_seperate, csc_not, elec_domes_1hrs, elec_domes_4hrs, elec_domes_8hrs, elec_domes_12hrs, elec_domes_no, elec_msme, pds, mandi, reg_mkt, weekly_haat, mkt_na, tap_100, tap_50, tap_l50, tap_one_hab, tap_na, tel_ll, tel_mob, tel_both, tel_na, clean_energy_hhs, solar_wind_elect, kuccha_hhs, po_sub_po, panch_bhawan, pib_na, pib_av_upd, pib_av_not_upd, prim_school, middle_school, high_school, high_second_school, degree_clg, school_college_na, public_library, indoor_sports, outdoor_sports, both_sports, no_sports, vocational, chc, phc, subcentre, no_health, subcentre_l1km, subcentre_2km, subcentre_5km, subcentre_10km, subcentre_g10km, veterinary, veterinary_l1km, veterinary_2km, veterinary_5km, veterinary_10km, veterinary_g10km, closed_drain, pucca_slab_drain, pucca_uncovered_drain, kuchha_drain, no_drain, pcomm_pasture

</details>

<details><summary>All 41 variables: Village Level Infrastructure</summary>

year, tot_pop, pop_male, pop_female, tot_hh, bank, bank_distance, bc_w_internet, atm, internet_bb, all_weather_road, cc_road, pub_trans, railway, csc_avail, elec_domes, elec_msme, pds, avl_market, tap_water, telepone, clean_energy_hhs, solar_wind_elect, kuccha_hhs, po_sub_po, panch_bhawan, pib, prim_school, middle_school, high_school, high_second_school, degree_clg, public_library, rec_sports, vocational, subcentre, subcentre_dist, veterinary, veterinary_dist, drainage, pcomm_pasture

</details>

<details><summary>All 26 variables: Village Basic Facilities</summary>

year, banks, atm, all_weather_road_connectivity, internal_pucca_roads, public_transport, common_service_centre, domestic_electricity_hrs, pds, market_facilities, piped_tap_water, telephone_services, post_office_subpost_office, primary_school, middle_school, high_school, higher_secondary_school, vocational_centre_iti_rseti_ddu_gky, veterinary_hospital_clinic, drainage_facilities, soil_testing_centre, govt_seed_centre, fertilizer_shop, community_waste_disposal, community_bio_gas_or_recycle_of_waste_for_production_use, aanganwadi_centre

</details>

#### Mission Antyodaya 2020

The Mission Antyodaya dataset offers an extensive overview of village-level infrastructure, socio-economic indicators, and resource availability across India. This comprehensive dataset, collected under the Mission Antyodaya initiative, aims to uplift the most underprivileged rural communities by providing detailed insights into various aspects of rural life.
*Source:* Ministry of Rural Development. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/mission-antyodaya-2020>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Mission Antyodaya 2020 | Village | 2020 | 32 states/UTs, 711 districts, 253,692 panchayats | — | not previewable on the portal (download to inspect) |

#### Pradhan Mantri Gram Sadak Yojana (PMGSY)

The Pradhan Mantri Gram Sadak Yojana (PMGSY) is an initiative launched by the Government of India in December 2000. Its primary objective is to provide all-weather road connectivity to unconnected villages and areas across the country. The scheme prioritizes regions with a population of 500 in plain areas and 250 in hilly or tribal regions.
*Source:* Ministry of Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pradhan-mantri-gram-sadak-yojana-pmgsy>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| PMGSY Financial and Physical Report | Block | 1960-2021 | 30 states/UTs, 673 districts, 5,172 sub-districts | 407,633 | 25: habitation_name, road_name, packages, upgrade_or_new, surface_type, physical_status, financial_status, contractor_name, company_name, sanctioned_year, work_award_date, completion_date … |

<details><summary>All 25 variables: PMGSY Financial and Physical Report</summary>

habitation_name, road_name, packages, upgrade_or_new, surface_type, physical_status, financial_status, contractor_name, company_name, sanctioned_year, work_award_date, completion_date, length, pavement_cost, no_of_cross_drainage_works, cross_drainage_work_cost, long_span_bridge_cost, long_span_bridge_state_cost, protection_work, other_works, completed_length, expenditure_till_date, total_cost, population, sc_st_population

</details>

#### Socio Economic Caste Census

The Socio Economic Caste Census (SECC) is a comprehensive exercise undertaken by the Government of India to gather detailed information about the socio-economic status and caste demographics of Indian households.
*Source:* Ministry of Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/socio-economic-caste-census>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Socio Economic Caste Census 2011 | District | 2010-11 | 36 states/UTs, 631 districts | 3,786 | 67: category, tot_hh, hh_considered_deprivation, one_room_kucha_walls_and_roof, no_adult_16_59, female_head_no_adult_16_59, disabled_no_able_bodied, sc_st_hh, no_literate_adult_25_plus, landless_hh_manual_labor, no_deprivation, own_motor_vehicle … |

<details><summary>All 67 variables: Socio Economic Caste Census 2011</summary>

category, tot_hh, hh_considered_deprivation, one_room_kucha_walls_and_roof, no_adult_16_59, female_head_no_adult_16_59, disabled_no_able_bodied, sc_st_hh, no_literate_adult_25_plus, landless_hh_manual_labor, no_deprivation, own_motor_vehicle, own_mech_agri, kcc_credit_limit_50k, govt_employee_member, non_agri_ent, member_earning_gt_10k, paying_income_tax, paying_prof_tax, three_room_pucca_wall_roof, own_refrigerator, own_landline_phone, irr_equip_gt_2_nd_half_acre, hh_irr5_acre_mul_season, owned_hh, rented_hh, other_hh, kuccha_0_room, kuccha_1_room, kuccha_2_room, kuccha_3_room, kuccha_3_room_plus, pucca_0_room, pucca_1_room, pucca_2_room, pucca_3_room, pucca_3_room_plus, semi_kuccha_0_room, semi_kuccha_1_room, semi_kuccha_2_room, semi_kuccha_3_room, semi_kuccha_3_room_plus, semi_pucca_0_room, semi_pucca_1_room, semi_pucca_2_room, semi_pucca_3_room, semi_pucca_3_room_plus, hh_considered_inclusion, hh_without_shelter, hh_destitute, hh_manual_scavenger, hh_primitive_tribal, hh_bonded_labourers, hh_with_inclusion_criteria, mon_inc_lt_5k, mon_inc_5k_10k, mon_inc_gt_10k, cultivation, casual_labor, domestic_service, foraging_rag_picking, non_agri_own_enterprise, begging_charity, other_income, govt_jobs, public_sector_jobs, private_sector_jobs

</details>

### Climate and Weather

#### Climate Data

Climate data in India is crucial given the country's diverse topography and climatic zones, which range from the arid deserts of Rajasthan to the wettest places on earth in Meghalaya. The India Meteorological Department (IMD), under the Ministry of Earth Sciences, is the primary agency responsible for meteorological observations, weather forecasting, and seismology.
*Source:* India Meteorological Department. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/climate-data>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Rainfall Data | Point | 1969 - 2020 | 33 states/UTs, 174 districts | 132,288 | 7: date, station_name, station_code, average_rainfall, standard_deviation, highest_rainfall, lowest_rainfall |
| Daily Rainfall Data - District Level | District | 2009-2023 | 37 states/UTs, 625 districts | 3,216,270 | 5: date, actual, rfs, normal, deviation |
| Daily Rainfall at State Level | State | 2009-2024 | 36 states/UTs | 202,234 | 5: date, actual, rfs, normal, deviation |
| Temperature | Point | 1969 - 2020 | 33 states/UTs, 174 districts | 264,576 | 8: date, station_name, station_code, parameter, average_temperature, standard_deviation, highest_temperature, lowest_temperature |

#### Climate Vulnerability Indicators

Climate Vulnerability Indicators dataset carries out vulnerability assessment for India based on various indicators related to infrastructure, agriculture, employment, disease, and the environment. Climate change is a serious threat to socio-economic development globally and in India.
*Source:* Department of Science and Technology. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/climate-vulnerability-indicators>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Climate Vulnerability Indicators State wise | State | 2019 | 36 states/UTs | 36 | 26: year, climate_vul_in, geo_land_area, forest_land_area, agri_land_area, waste_land_area, irrigated_area, population_density, literacy_rate, gdp_const_price, households_below_poverty, infant_mortality … |
| Climate Vulnerability Indicators District Wise | District | 2021 | 28 states/UTs | 699 | 74: year, climate_vul_in, mar_small_land, area_crop_insur, area_rainfed_agri, area_forest_per_hun_population, women_workforce, avg_days_employement, road_density, health_centre, infant_mortality, household_electricity … |

<details><summary>All 26 variables: Climate Vulnerability Indicators State wise</summary>

year, climate_vul_in, geo_land_area, forest_land_area, agri_land_area, waste_land_area, irrigated_area, population_density, literacy_rate, gdp_const_price, households_below_poverty, infant_mortality, poverty_rate, income_from_natural_resources, out_peren_trees_to_total_agri_out, mar_small_op_land_holding, yield_variability, area_under_pmfby_wbcis, rainfed_agriculture, forest_land_area_per_population, women_workforce, employed_under_mgnrega, road_rail_density, health_workers_per_population, vector_diseases_per_population, water_diseases_per_population

</details>

<details><summary>All 74 variables: Climate Vulnerability Indicators District Wise</summary>

year, climate_vul_in, mar_small_land, area_crop_insur, area_rainfed_agri, area_forest_per_hun_population, women_workforce, avg_days_employement, road_density, health_centre, infant_mortality, household_electricity, household_drinking_water, yield_variability, per_capita_income, livestock, area_forest_cover, out_total_horticulture_agriculture, unirrigated_area, groundwater_extracted, households_kisan_creditcard, shg_per_population, doctors_per_population, population_below_poverty, income_tertiary_sector, area_forest_per_thous_population, horticulture_agriculture, irrigated_area, groundwater_available, population_multi_hazard, rural_banks, vector_diseases, water_diseases, agricultural_labour, agri_output_horti_output, irrgated_area_sown_area, road_length, household_banking_services, area_insured, sown_area_horticulture, household_sanitation, female_literacy, net_agri_geo_area, unirrigated_sown_area, household_highest_earning, household_no_land, net_irrigated_sown_area, drainage_density, natural_resource_management, anganwadi, agri_area_under_slope, total_crop, main_local_market, water_scarcity, soil_fertility, crop_divsi_in, road_connect, market_access, income_divsi_agri, water_available, area_water_bodies, fair_price_shops, toal_female_workforce, groundwater_development, crop_intensity, area_commer_crops, variability, water_fish_culture, forest_depend_tribal, minor_forest_produce, depend_ratio_below_poverty, establishment, health_care, household_health_scheme

</details>

#### Groundwater

The "Groundwater" package offers a rich and comprehensive collection of datasets detailing groundwater levels and quality across India. Compiled by the Central Ground Water Board (CGWB) and augmented by contributions from State Groundwater Boards and the Central Pollution Control Board (CPCB), this package provides critical data for hydrologists, environmental scientists, policymakers, and researchers focusing on …
*Source:* Central Ground Water Board, Water Resources Information System (WRIS). *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/groundwater>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| CGWB - Changes in Depth to Water Level | Other | 2013-2022 | 33 states/UTs, 568 districts | 550,850 | 9: date, station_name, latitude, longitude, basin, sub_basin, source, currentlevel, level_diff |
| State Groundwater Boards - Changes in Depth to Water Level | Other | 2013-2021 | 11 states/UTs, 150 districts | 358,558 | 9: date, station_name, latitude, longitude, basin, sub_basin, source, currentlevel, level_diff |

#### Groundwater Level

The Groundwater Level, sourced from the Ministry of Jal Shakti, offers a comprehensive view of groundwater levels across India. It includes manually collected data from monitoring wells, high-frequency telemetric readings, and long-term records observation wells dating back to 1969.
*Source:* India Water Resources Information System. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/cgwb-changes-in-depth-to-water-level>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Groundwater Level | Station | 1965-2025 | — | — | not previewable on the portal (download to inspect) |

### Crime

#### Accidental Deaths in India

The Accidental Deaths in India dataset package, published by the National Crime Records Bureau (NCRB) as part of its annual Accidental Deaths and Suicides in India (ADSI) series, presents a detailed statistical overview of accidental fatalities across the country.
*Source:* National Crime Records Bureau. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/accidental-deaths-in-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Incidence and Rate of Accidental Deaths due to Forces of Nature and Other Causes | State | 2018 - 2024 | 36 states/UTs | 214 | 5: year, forces_of_nature, other_causes, percentage_share_in_total_deaths, projected_mid_year_population_in_lakh |
| Gender - wise Distribution of Accidental Deaths due to Forces of Nature | State | 2018 - 2024 | 36 states/UTs | 10,458 | 4: year, forces_of_nature, gender, number_of_deaths |
| Other Causes-wise Number of Cases, Persons Injured & Persons Died | State | 2018-2024 | 36 states/UTs | 45,033 | 6: year, cause, gender, no_of_cases, injured, died |
| The Place of Occurrence Wise Fire Accidental Deaths | State | 2018-2024 | 36 states/UTs | 9,711 | 6: year, cause, gender, no_of_cases, injured, died |
| Age and Gender Wise Distribution of Accidental Deaths | State | 2018-2024 | 36 states/UTs | 3,870 | 4: year, age_category, gender, number_of_deaths |

#### Crime Statistics

"Crime Statistics" is a comprehensive collection of datasets focused on various dimensions of crime within a region, state, and district provided by the National Crime Records Bureau (NCRB). This dataset collection is invaluable for researchers, policymakers, law enforcement agencies, and social welfare organizations.
*Source:* National Crime Records Bureau. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/crime-statistics>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Districtwise Crime Against Children 2016 | District | 2016 | 35 states/UTs, 679 districts | 817 | 25: year, registration_circles, murder, infancticide, rape, assault_on_women, insult_the_modesty_of_women, kidnapping_and_abduction, foeticide, abetment_of_suicide_of_child, exposure_and_abandonment, procuration_of_minor_girls … |
| Crime Against STs 2016 | District | 2016 | 35 states/UTs, 679 districts | 817 | 17: year, registration_circles, protection_of_civil_rights_act, murder, attempt_to_commit_murder, rape, attempt_to_commit_rape, assault_on_women, insult_to_the_modesty_of_women, kidnapping_and_abduction, dacoity, robbery … |
| Districtwise Crime Against STs 2017 onwards | District | 2017-2022 | 36 states/UTs, 923 districts | 5,468 | 40: year, registration_circles, murder, atmpt_commit_murder, simple_hurt, grievous_hurt, acid_attack, atmpt_acid_attack, other_grievous_hurt, assault_on_adult_women, sexual_harassment, atmpt_disrobe … |
| Crimes Against SC 2016 | District | 2016 | 35 states/UTs, 680 districts | 817 | 17: year, registration_circles, protection_of_civil_rights, murder, attempt_to_commit_murder, rape, attempt_to_commit_rape_rape, assault_on_women, insult_to_the_modesty, kidnapping_and_abduction, dacoity, robbery … |
| Districtwise Crimes Against SC 2017 onwards | District | 2017-2022 | 36 states/UTs, 751 districts | 5,323 | 40: year, registration_circles, murder, atmpt_commit_murder, simple_hurt, grievous_hurt, acid_attack, atmpt_acid_attack, other_grievous_hurt, assault_on_adult_women, sexual_harassment, atmpt_disrobe … |
| Districtwise crime against women 2016 | District | 2016 | 36 states/UTs, 684 districts | 817 | 21: year, registration_circles, rape, attempt_to_commit_rape, kidnapping_and_abduction, dowry_deaths, assault_on_women, insult_to_the_modesty_of_women, cruelty_by_husband_relatives, importation_of_girls_from_foreign, abetment_of_suicides_of_women, dowry_prohibition … |
| Districtwise Crime Against Women 2017 onwards | District | 2017-2022 | 36 states/UTs, 751 districts | 5,322 | 44: year, registration_circles, murder_with_rape_gang_rape, dowry_deaths, abetment_to_suicide_of_women, miscarriage, acid_attack, attempt_to_acid_attack, cruelty_by_husband_or_his_relatives, kidnapping_and_abduction, kidnapping_abduction_in_order_to_murder, kidnapping_for_ransom … |
| Districtwise Cyber Crimes 2017 onwards | District | 2017-2022 | 36 states/UTs, 752 districts | 5,322 | 43: year, registration_circles, tampering_computer_source_documents, ransom_ware, offences_other_than_ransom_ware, dishonestly_recv_stolen_cmp_resrc_or_comm_device, identity_theft, cheating_by_personation_by_using_computer_resource, violation_of_privacy, cyber_terrorism, pub_or_trans_obscene_material_in_electronic_form, pub_or_trans_mtrl_cont_sxly_explct_act_elect_frm … |
| Districtwise IPC crimes 2016 | District | 2016 | 35 states/UTs, 684 districts | 817 | 36: year, registration_circles, murder, attempt_to_commit_murder, culpable_homicide_not_amounting_to_murder, attempt_to_commit_culpable_homicide, rape, attempt_to_commit_rape, kidnapping_and_abduction, dacoity, mkng_preparation_and_assembly_for_comm_dacoity, robbery … |
| Districtwise Missing Persons 2017-2020 | District | 2017-2020 | 36 states/UTs, 731 districts | 3,478 | 23: year, registration_circles, male_below_5_years, male_5_to_14_years, male_14_to_18_years, male_18_to_30_years, male_30_to_45_years, male_45_to_60_years, male_60_years_and_above, female_below_5_years, female_5_to_14_years, female_14_to_18_years … |
| Districtwise Missing Persons 2021 onwards | District | 2021-2022 | 36 states/UTs, 753 districts | 1,841 | 17: year, registration_circles, male_below_12_years, male_12_years_to_16_years, male_16_years_to_18_years, male_children, male_18_years_and_above, female_below_12_years, female_12_years_to_16_years, female_16_years_to_18_years, female_children, female_18_years_and_above … |
| IPC Crime by Juveniles | District | 2017-2022 | 36 states/UTs, 750 districts | 5,322 | 119: year, registration_circles, murder, culpable_homicide_not_amounting_to_murder, hit_and_run, other_accidents, death_due_to_neglnc_relating_to_rail_acdnt, death_due_to_med_neglnc, death_due_to_neglnc_of_civic_body, death_due_to_other_negligence, dowry_death, abetment_of_suicide … |
| SLL Crime by Juveniles | District | 2017-2022 | 36 states/UTs, 746 districts | 5,305 | 74: year, registeration_circles, dowry_prohibition, traffic_prevention, prevention_of_women_against_domestic_voilence, indecent_representation_of_women_prohibition, protection_of_children_from_sexual_offences, juvenile_justice_care_and_protectione_of_children, prohibition_of_child_marriage, pre_natal_diagnotics_tech_reg_and_prev_of_misuse, child_labour_prohibition_and_regulation, medical_termination_of_pregnancy … |
| Districtwise SLL crimes 2016 | District | 2016 | 36 states/UTs, 684 districts | 817 | 58: year, registration_circles, arms_act, ndps_act, gambling, excise, prohibition, explosives_and_explosive_substances, immoral_traffic_prevention, indian_railways, registration_of_foreigners, protection_of_civil_rights … |
| Districtwise Crime Against Children 2017 onwards | District | 2017-2022 | 36 states/UTs, 751 districts | 5,321 | 53: year, registration_circles, murder_with_rape, other_murder, abetment_suicide_of_child, attempt_to_commit_murder, infanticide, foeticide, exposure_and_abandonment, simple_hurt, grievous_hurt, missing_child_kidnapped … |
| Districtwise IPC crimes 2017 onwards | District | 2017-2022 | 36 states/UTs, 749 districts | 5,322 | 119: year, registration_circles, murder, clpbl_hmcrd_not_amt_murder, hit_and_run, acdnt_other_than_hit_and_run_, deaths_negl_rel_rail_acdnt, deaths_due_med_negnc, deaths_neg_civic_bodies, deaths_other_negnc, dowry_deaths, abetment_of_suicide … |
| Districtwise SLL crimes 2017 onwards | District | 2017-2022 | 36 states/UTs, 752 districts | 5,321 | 74: year, registration_circles, dowry_prohibition, immoral_traffic_prevention, women_protection_from_domestic_voilence, indecent_representation_of_women_prohibition, protection_of_children_from_sexual_offences, juvenile_justice_care_and_protection_of_children, prohibition_of_child_marriage, pre_natal_diag_technq_reg_n_prev_of_misuse, child_labour_prohibition_regulation, medical_termination_of_pregnancy … |
| Districtwise Crime Against Children 2024 onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 57: year, registration_circles, rape_children, attempt_commit_rape, assault_children_outrage_modesty, sexual_harassment_girls, assault_girls_disrobe, voyeurism, stalking, insult_modesty_women, kidnap_abduct_inducing_girls_compel_marriage, foeticide … |
| Districtwise Crime Against SC 2024 onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 41: year, registration_circles, rape_women, rape_children, attempt_commit_rape, assault_women, assault_children, sexual_harassment_women, sexual_harassment_children, assault_criminal_force_women_disrobe_354b, sc_st_ipc_bns_voyeurism, sc_st_ipc_bns_stalking … |
| Districtwise Crime Against ST 2024 onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 41: year, registration_circles, rape_women, rape_children, attempt_commit_rape, assault_women, assault_children, sexual_harassment_women, sexual_harassment_children, assault_criminal_force_women_disrobe_354b, sc_st_ipc_bns_voyeurism, sc_st_ipc_bns_stalking … |
| Districtwise Crime Against Women 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 51: year, registration_circles, rape_women, rape_girls, sexual_intercourse_employing_deceitful_means, murder_rape_gang, attempt_commit_rape_women, attempt_commit_rape_girls, assault_outrage_modesty_women, assault_women_outrage_modesty_girls, sexual_harassment_women, sexual_harassment_girls … |
| Districtwise Cyber Crimes 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 51: year, registration_circles, tampering_computer_source_documents, ransom_ware, offences_other_than_ransom_ware, dishonestly_recv_stolen_computer_resource, identity_theft, cheating_personation_using_computer_resource, violation_privacy, cyber_terrorism, pub_trans_obscene_material_electronic, publish_transmit_sexually_explicit_mtrl … |
| Districtwise IPC Crime by Juveniles 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 132: year, registration_circles, offences_women_child_rape, attempt_commit_rape, sexual_intercourse_employing_deceitful_means, disclosure_identity_victim, assault_criminal_force_woman_outrage_modesty, office_premises, work_premises, public_transport_system, public_places_pathway, shelter_homes_women_children … |
| Districtwise IPC crimes 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 132: year, registration_circles, offences_women_child_rape, attempt_commit_rape, sexual_intercourse_employing_deceitful_means, disclosure_identity_victim, assault_criminal_force_woman_outrage_modesty, office_premises, work_premises, public_transport_system, public_places_pathway, shelter_homes_women_children … |
| Districtwise SLL Crime by Juveniles 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 76: year, registration_circles, dowry_prohibition, immoral_traffic_prevention, protection_women_domestic_violence, indecent_representation_women_prohibition, protection_children_sexual_offences, juvenile_justice_care_protection_children, prohibition_child_marriage, pre_natal_diagnostic_techniques_reg_prev, child_labour_prohibition_regulation, medical_termination_pregnancy … |
| Districtwise SLL crimes 2024 Onwards | District | 2024 | 36 states/UTs, 771 districts | 964 | 76: year, registration_circles, dowry_prohibition, immoral_traffic_prevention, protection_women_domestic_violence, indecent_representation_women_prohibition, protection_children_sexual_offences, juvenile_justice_care_protection_children, prohibition_child_marriage, pre_natal_diagnostic_techniques_reg_prev, child_labour_prohibition_regulation, medical_termination_pregnancy … |

<details><summary>All 25 variables: Districtwise Crime Against Children 2016</summary>

year, registration_circles, murder, infancticide, rape, assault_on_women, insult_the_modesty_of_women, kidnapping_and_abduction, foeticide, abetment_of_suicide_of_child, exposure_and_abandonment, procuration_of_minor_girls, importation_of_girls_from_foreign_country, buying_of_minors_for_prstn, selling_of_minors_for_prstn, prohibition_of_child_marriage, transplantation_of_human_organs, child_labour_prohibition_and_regulation, immoral_traffic_prevention, justice_care_and_protection_of_children, protection_of_children_from_sexual_offences, attempt_to_commit_murder, unnatural_offences, human_trafficking, other_crimes_committed_against_children

</details>

<details><summary>All 17 variables: Crime Against STs 2016</summary>

year, registration_circles, protection_of_civil_rights_act, murder, attempt_to_commit_murder, rape, attempt_to_commit_rape, assault_on_women, insult_to_the_modesty_of_women, kidnapping_and_abduction, dacoity, robbery, arson, grievous_hurt, riots, other_ipc_crimes, sc_st_prevention_of_atrocities

</details>

<details><summary>All 40 variables: Districtwise Crime Against STs 2017 onwards</summary>

year, registration_circles, murder, atmpt_commit_murder, simple_hurt, grievous_hurt, acid_attack, atmpt_acid_attack, other_grievous_hurt, assault_on_adult_women, sexual_harassment, atmpt_disrobe, voyeurism, stalking, assault_of_children_pocso, inslt_women_modesty, missing_children_kidnpd, other_kidnp_abduc, kidnp_begging, kidnp_murder, kidnapping_for_ransom, kidnp_marriage, procur_minor_girls, kidnp_abduc_sec_365_to_369, rape_of_women, rape_of_children, atmpt_rape, rioting, robbery, dacoity_with_murder, dacoity, arson, criminal_intimidation, other_ipc_crimes, intimitate_humiliate, occupy_land_blngs_sts, prvnt_obstruct_usage_pub_passage, frc_leave_place_res_soc_boycott, other_offences, protection_of_civil_rights

</details>

<details><summary>All 17 variables: Crimes Against SC 2016</summary>

year, registration_circles, protection_of_civil_rights, murder, attempt_to_commit_murder, rape, attempt_to_commit_rape_rape, assault_on_women, insult_to_the_modesty, kidnapping_and_abduction, dacoity, robbery, arson, grievous_hurt, riots, other_ipc_crimes_crimes, sc_st_prevention_of_atrocities

</details>

<details><summary>All 40 variables: Districtwise Crimes Against SC 2017 onwards</summary>

year, registration_circles, murder, atmpt_commit_murder, simple_hurt, grievous_hurt, acid_attack, atmpt_acid_attack, other_grievous_hurt, assault_on_adult_women, sexual_harassment, atmpt_disrobe, voyeurism, stalking, assault_of_children, insult_modesty, missng_children_kidnapped, other_kidnapping_abduction, kidnp_abduction_purpose_begging, kidnp_abduction_murder, kidnp_for_ransom, kidnp_abduction_marriage, procur_minor_girls, other_kidng_abduction, rape_women_abv_18_yrs, rape_children_blw_18_yrs, attempt_rape, rioting, robbery, dacoity_with_murder, dacoity, arson, criminal_intimidation, other_ipc_crimes, intimidate_humiliate, occupy_disposes_land_blngs_scs, prvnt_usage_pub_place_passage, frc_leave_place_res_soc_boycott, other_offences, protection_of_civil_rights

</details>

<details><summary>All 21 variables: Districtwise crime against women 2016</summary>

year, registration_circles, rape, attempt_to_commit_rape, kidnapping_and_abduction, dowry_deaths, assault_on_women, insult_to_the_modesty_of_women, cruelty_by_husband_relatives, importation_of_girls_from_foreign, abetment_of_suicides_of_women, dowry_prohibition, indecent_representation_of_women, protection_of_women_from_domestic_violence, immoral_traffic_prevention, acid_attack, attempt_to_acid_attack, deaths_caused_with_intent_to_cause_miscarriage, causing_miscarriage_without_consent_of_women, human_trafficking, un_natural_offences

</details>

<details><summary>All 44 variables: Districtwise Crime Against Women 2017 onwards</summary>

year, registration_circles, murder_with_rape_gang_rape, dowry_deaths, abetment_to_suicide_of_women, miscarriage, acid_attack, attempt_to_acid_attack, cruelty_by_husband_or_his_relatives, kidnapping_and_abduction, kidnapping_abduction_in_order_to_murder, kidnapping_for_ransom, kidnp_and_abductn_of_women_above_18_for_marrg, kidnp_and_abductn_of_girls_below_18_for_marrg, procuration_of_minor_girls, importation_of_girls_from_foreign, kidnapping_and_abduction_of_women_others, human_trafficking, selling_of_minor_girls, buying_of_minor_girls, rape_women_above_18, rape_girls_below_18, attempt_to_commit_rape_above_18, attempt_to_commit_rape_girls_below_18, assault_on_womenabove_18, assault_on_women_below_18, insult_to_the_modesty_of_women_above_18, insult_to_the_modesty_of_women_below_18, dowry_prohibition, procuring_inducing_children_for_the_sake_of_prostitution, detaining_a_prsn_in_premises_where_prost_is_carried, prostitution_in_or_in_the_vicinity_of_public_places, seducing_or_soliciting_for_purpose_of_prostitution, other_sections_under_itp_act, protection_of_women_from_domestic_violence, publshng_or_transmitting_of_sexually_explicit_mtrl, other_women_centric_cyber_crimes, child_rape, sexual_assault_of_children, child_sexual_harassment, use_of_child_for_pornography, offences_of_pocso_act, pocso_act_unnatural_offences, indecent_representation_of_women

</details>

<details><summary>All 43 variables: Districtwise Cyber Crimes 2017 onwards</summary>

year, registration_circles, tampering_computer_source_documents, ransom_ware, offences_other_than_ransom_ware, dishonestly_recv_stolen_cmp_resrc_or_comm_device, identity_theft, cheating_by_personation_by_using_computer_resource, violation_of_privacy, cyber_terrorism, pub_or_trans_obscene_material_in_electronic_form, pub_or_trans_mtrl_cont_sxly_explct_act_elect_frm, pub_or_trans_mtrl_dpct_chl_sxly_explct_elect_frm, presrv_and_retention_of_info_by_intermediaries, other_sections_it_act, interception_or_monitoring_or_decryption_of_info, un_athryz_access_atmpt_access_prct_comp_sys, abetment_to_commit_offences, attempt_to_commit_offences, other_sections_of_it_act, abetment_of_suicide_online, cyber_stalking_bullying_of_women_children, data_theft, credit_card_debit_card_fraud, atms_fraud, online_banking_fraud, otp_frauds, other_frauds, cheating, forgery, defamation_morphing, fake_profile, currency_counterfeiting, stamps_counterfeiting, cyber_blackmailing_threatening, fake_news_on_social_media, other_offences, total_offences_under_ip, gambling_act, lotteries_act, copy_right_act, trade_marks_act, other_sll_crimes

</details>

<details><summary>All 36 variables: Districtwise IPC crimes 2016</summary>

year, registration_circles, murder, attempt_to_commit_murder, culpable_homicide_not_amounting_to_murder, attempt_to_commit_culpable_homicide, rape, attempt_to_commit_rape, kidnapping_and_abduction, dacoity, mkng_preparation_and_assembly_for_comm_dacoity, robbery, criminal_trespass_or_burglary, theft, unlawful_assembly, riots, criminal_breach_of_trust, cheating, forgery, counterfeiting, arson, grievous_hurt, dowry_deaths, assault_on_women, insult_to_the_modesty_of_women, cruelty_by_husband_or_his_relatives, importation_of_girls_from_foreign_country, causing_death_by_negligence, offences_against_state, offences_promoting_enmity_between_diff_grp, extortion, disclosure_of_identity_of_victims, incidence_of_rash_driving, human_trafficking, unnatural_offence, other_ipc_crimes

</details>

<details><summary>All 23 variables: Districtwise Missing Persons 2017-2020</summary>

year, registration_circles, male_below_5_years, male_5_to_14_years, male_14_to_18_years, male_18_to_30_years, male_30_to_45_years, male_45_to_60_years, male_60_years_and_above, female_below_5_years, female_5_to_14_years, female_14_to_18_years, female_18_to_30_years, female_30_to_45_years, female_45_to_60_years, female_60_years_and_above, trangender_below_5_years, trangender_5_to_14_years, trangender_14_to_18_years, trangender_18_to_30_years, trangender_30_to_45_years, trangender_45_to_60_years, transgender_60_years_and_above

</details>

<details><summary>All 17 variables: Districtwise Missing Persons 2021 onwards</summary>

year, registration_circles, male_below_12_years, male_12_years_to_16_years, male_16_years_to_18_years, male_children, male_18_years_and_above, female_below_12_years, female_12_years_to_16_years, female_16_years_to_18_years, female_children, female_18_years_and_above, transgender_below_12_years, transgender_12_years_to_16_years, transgender_16_years_to_18_years, transgender_children, transgender_18_years_and_above

</details>

<details><summary>All 119 variables: IPC Crime by Juveniles</summary>

year, registration_circles, murder, culpable_homicide_not_amounting_to_murder, hit_and_run, other_accidents, death_due_to_neglnc_relating_to_rail_acdnt, death_due_to_med_neglnc, death_due_to_neglnc_of_civic_body, death_due_to_other_negligence, dowry_death, abetment_of_suicide, attempt_to_commit_muder, attempt_to_commit_culpable_homicie, attempt_to_commit_suicide, miscarriage_infanticide_foeticide_and_abandonment, voluntarily_causing_simple_hurt, volutarily_hurt_by_dangerous_weapons_or_means, vlntry_cusng_hrt_force_deter_pblic_srvnt_on_duty, cusng_hrt_by_act_endngrng_lyf_sfty_of_others, other_simple_hurt, vlntry_cusng_grvus_hrt_dangerous_wepon_or_mean, acid_attack, attempt_to_acid_attack, vlntrly_csng_gvus_hrt_force_deter_pblc_servnt_on_duty, causing_grvus_hrt_by_act_endangering_life_safety, other_grievous_hurt, wrongful_restraint_confinement, assault_on_women, sexual_harassment_at_work, sexual_harassment_in_public_transport_system, sexul_hrsmt_in_shelter_homes_for_women_and_children, sexual_harassment_at_other_places, assault_criminal_force_women_intent_disrobe, voyeurism, stalking, missing_children_deemed_as_kidnapped, other_kidnapping_and_abduction, kidnapping_and_abduction_for_the_purpose_of_begging, kidnapping_and_abduction_in_order_to_murder, kidnapping_foe_ransom, kdnppig_nd_abdctn_of_wmn_compel_for_marriage, procuration_of_minor_girls, importation_of_girls_form_foreign_country, other_kidnapping_and_abduction_, human_trafficking, exploitation_of_trafficked_person, selling_of_minors_for_prostitution, buying_of_minors_for_prostitution, rape, attempt_to_commit_rape, unnatural_offences, offences_affecting_the_human_body, offence_against_state_sedition, offence_against_state_other, offnc_against_public_tanquillity_unlawful_assmbly, rioting_communal_religious, rioting_sectarian, rioting_industrial, rioting_political, rioting_caste_conflict, rioting_agrarian, rioting_students, rioting_vigilants, money_dispute_rioting, water_dispute_rioting, land_property_dispute_rioting, family_dispute_rioting, enmity_rivalry_rioting, electricity_power_supply_dispute_rioting, rioting_while_in_andolan_morcha, rioting_at_tacks_on_police_personnel_or_ovt_servants, other_rioting, promoting_enmity_between_groups, imputation_assertions_prejudicial_to_national_integration, affray, auto_motor_vehicle_theft, other_thefts, day_time, night, extortion_and_blackmailing, robbery, attempt_to_commit_dacoity_robbery, dacoity, dacoity_with_murder, mkng_prptn_and_assembly_for_committing_dacoity, criminal_misappropriation, criminal_breach_of_trust, dishonestly_receiving_dealing_in_stolen_property, counterfeit_coin, counterfeiting_government_stamp, counterfeiting_of_seal_or_mark, counterfeit_currency_and_bank_notes, bank, atms, credit_card_debit_card, other_frauds, cheating, forgery, mscllns_ipc_crimes_offences_relating_electn, disbdnc_ordr_duly_promulgated_by_public_servant, harbouring_an_offender, offences_relating_adulteration_sale_food_drugs, rash_driving_on_public_way, causing_hurt_by_rash_negligent_driving_on_public, grvus_hurt_by_rash_negligent_driving_on_public, obstruction_on_public_way, sale_of_obscene_books_objects, obscene_acts_songs_at_public_places, offences_relating_religion, cheating_by_impersonation, offences_related_to_mischief, arson, criminal_trespass, cruelty_by_husband_or_his_relatives, circulate_false_fake_news_rumours, criminal_intimidation, insult_to_the_modesty_of_women, other_ipc_crimes

</details>

<details><summary>All 74 variables: SLL Crime by Juveniles</summary>

year, registeration_circles, dowry_prohibition, traffic_prevention, prevention_of_women_against_domestic_voilence, indecent_representation_of_women_prohibition, protection_of_children_from_sexual_offences, juvenile_justice_care_and_protectione_of_children, prohibition_of_child_marriage, pre_natal_diagnotics_tech_reg_and_prev_of_misuse, child_labour_prohibition_and_regulation, medical_termination_of_pregnancy, prevention_of_atrocities_against_sc, prevention_of_atrocities_against_st, protection_of_civil_rights_against_sc, protection_of_civil_rights_against_st, prevention_of_damage_to_public_property, unlawful_activities, official_secrets, arms_act, legal_licensed_arms, illegal_licensed_arms, other_arms, explosive_act, explosive_substance, it_act, copy_right_act, trade_mark_act, lotteries_regulation, chit_funds_act, negotiable_instruments, benami_transaction_prohibition, mine_and_minerals_dev_and_regulation, prevention_of_corruption, liquor_narcotic_drugs_related_acts_prohibition, prohibiton_act, possesion_of_drugs_for_personal_use, possesion_of_drugs_for_tafficking, forest_act_and_forest_conservation, wildlife_protection_act, environment_protection_act, air_and_water_prevention_and_control_of_pollution, cigarette_and_otehr_tobbacco_products, noise_pollution, national_green_tribunal, registration_of_foreigners, passport_act, emigration_act, citizenship_act, indian_railway_act, railway_property_unlawful_possession, indian_telegraph_act, telegraph_wire_unlawful_possession, cinematography_act, cable_television_network_regulation, essential_commodities_act, prevention_of_food_adulteration, food_safety_and_standards, macoca_control_f_organised_crime, gambeling_act, electricity_act, antiques_and_art_tresures, representation_of_the_people, bonded_labour_system_abolition_against_sc, bonded_labour_system_abolition_against_st, bonded_labour_system_abolition_against_others, prevention_of_insults_to_national_honour, defacement_of_public_property, transplantation_of_human_organs, mental_health, motor_vehicle, city_town_police_act, other_local_state_act, other_sll_crime

</details>

<details><summary>All 58 variables: Districtwise SLL crimes 2016</summary>

year, registration_circles, arms_act, ndps_act, gambling, excise, prohibition, explosives_and_explosive_substances, immoral_traffic_prevention, indian_railways, registration_of_foreigners, protection_of_civil_rights, passport_act, essential_commodities, antiquities_and_art_treasures, dowry_prohibition, indecent_representation_of_women_prohibition, copyright_act, commission_of_sati_prevention, sc_st_poa_act, forest_act, prohibition_of_child_marriage, protection_of_women_from_domestic_violence, information_technology, official_secrets, electricity, wildlife_protection, bonded_labour_system_abolition, environmental_protection, air_prevention_and_control_of_pollution, water_prevention_and_control_of_pollution, national_security_act, unlawful_activities_prevention, young_persons_harmful_publication, railway_property_unlawful_possession, prevention_of_damage_to_public_property, transplantation_of_human_organs, trade_mark_act, prevention_of_insults_to_national_honour, state_emblem_prohibition_of_improper_use, lotteries_regulation, citizenship_act, foreigners_act, place_of_worship_special_provisions, religious_institution_prevention_of_misuse, representation_of_the_people, emigration_act, juvenile_justice_care_and_protection_of_children, infant_substitutes_regulation, anti_hijacking, atomic_energy, wepns_of_mass_drstn_proh_of_unlawful_activities, supprn_of_unlawful_acts_agnst_sfty_of_civil_aviat, safety_of_maritime_navigation, mnl_scavengers_construction_of_dry_latrines, prntl_diag_technq_reg_and_prev_of_misuse, mar_zn_of_ind_reg_of_fishing_by_for_vsl, other_sll_crimes

</details>

<details><summary>All 53 variables: Districtwise Crime Against Children 2017 onwards</summary>

year, registration_circles, murder_with_rape, other_murder, abetment_suicide_of_child, attempt_to_commit_murder, infanticide, foeticide, exposure_and_abandonment, simple_hurt, grievous_hurt, missing_child_kidnapped, other_kidnp_abductn_sec_363, kidnp_abductn_purpose_begging, kidnp_abductn_order_to_murder, kidnp_for_ransom, kidnp_abductn_minor_girls, procuratn_minor_girls, import_girls_frm_frgn_cnt, other_kidnp_abductn, humn_traffick_children, sell_minors_prost_boys, sell_minors_prost_girls, buy_minors_prost_boys, buy_minors_prost_girls, rape, atmpt_to_commit_rape, assault_women_intnt_outrage_modsty, insult_to_modesty_women, other_ipc_crimes, sec_4_6_pocso_act_girls, sec_4_6_pocso_act_boys, sec_8_10_pocso_act_girls, sec_8_10_pocso_act_boys, sec_12_pocso_act_girls, sec_12_pocso_act_boys, sec_14_15_pocso_girls, sec_14_15_pocso_boys, sec_377_pocso_act_girls, sec_377_pocso_act_boys, sec_17_22_pocso_act_girls, sec_17_22_pocso_act_boys, offences_care_takers, other_offences_juveniles, procur_induc_children_sake_prost, detain_prsn_whr_prost_carried, other_immoral_traffic, child_labour, prohib_child_marriage, transplantn_human_organs, pub_trns_mat_depict_child_sexul_explicit, other_cyber_crimes_agnst_children, other_sll_crimes

</details>

<details><summary>All 119 variables: Districtwise IPC crimes 2017 onwards</summary>

year, registration_circles, murder, clpbl_hmcrd_not_amt_murder, hit_and_run, acdnt_other_than_hit_and_run_, deaths_negl_rel_rail_acdnt, deaths_due_med_negnc, deaths_neg_civic_bodies, deaths_other_negnc, dowry_deaths, abetment_of_suicide, atmpt_cmmt_murder, atmpt_cmmt_clpb_hmcrd, atmpt_cmmt_suicide, miscarr_infant_foetic_aband, vlntrly_caus_simple_hurt, vlntrly_caus_dangers_weapons, vlntrly_caus_pub_srvnt_duty, hrt_endgrng_lf_safety, other_simple_hurt, vlntrly_caus_grvus_hurt, grvus_hrt_dangerous_wepn, acid_attack, atmpt_acid_attack, grvus_hrt_pub_srvnt_duty, grvus_hrt_lf_safety, other_grievous_hurt, wrngful_rest_cnfm, assault_on_women, sex_hrrsmt_work_office_prms, sex_hrrsmt_pub_trnsprt_sys, sex_hrrsmt_shelter_homes, sex_hrrsmt_other_places, intnt_disrbe, voyeurism, stalking, missing_child_kidnpd, other_kidnp_abduc, kidnp_abdctn_begging, kidnp_abdctn_murder, kidnapping_for_ransom, kidnp_abdctn_marrg, proc_minor_girls, import_girls_frgn_cntry, other_kidnp_abduc_sec_365_369, human_trafficking, exp_traf_person, sell_minors_prost, buy_minors_prost, rape, atmpt_rape, unnatural_offences, ofnc_agnst_state_sedition, ofnc_agnst_state_other, ofnc_agnst_pub_trnqul, rioting_communal_religious, rioting_sectarian, rioting_industrial, rioting_political, rioting_caste_conflict, rioting_agrarian, rioting_students, rioting_vigilants, rioting_money_dispute, rioting_water_dispute, rioting_land_property_dispute, rioting_family_disputes, rioting_enmity_rivalry, riot_elec_pwr_disp, riot_andolan_morcha, riot_polc_prsnl_gvt_srvnt, other_rioting, prmt_enmty_grps, impt_asrtns_prjudc_intgrtn, affray, auto_motor_vehicle_theft, other_thefts, day_time_burglary, night_burglary, extortion_and_blackmailing, robbery, atmpt_dacoity_robbery, dacoity, dacoity_with_murder, mkng_prprtn_assmbly_cmmttng_dcty, criminal_misappropriation, criminal_breach_of_trust, dsh_hon_rec_deal_stl_prop, counterfeit_coin, cntrfte_govt_stamp, cntrft_seal_mark, cntrft_curr_bank_notes, bank_frauds, atm_fraud, credit_debit_card_fraud, other_frauds, cheating, forgery, ofnc_elections, disbnc_ordr_prmlgtd_pblc_srvnt, harboring_offender, sale_food_drugs, rash_driving_pub_way, csng_hrt_rsh_nglgnt_drvng_pblc_wy, grvus_hrt_rsh_nglgnt_drvng, obstruction_pub_way, sale_obscene_books_objects, obscene_acts_songs_public_places, ofnc_religion, cheating_impersonation, ofnc_mischief, arson, criminal_trespass, crlty_husbnd_relatives, crcl_false_fake_news_rumours, criminal_intimidation, insult_modesty_women, other_ipc_crimes

</details>

<details><summary>All 74 variables: Districtwise SLL crimes 2017 onwards</summary>

year, registration_circles, dowry_prohibition, immoral_traffic_prevention, women_protection_from_domestic_voilence, indecent_representation_of_women_prohibition, protection_of_children_from_sexual_offences, juvenile_justice_care_and_protection_of_children, prohibition_of_child_marriage, pre_natal_diag_technq_reg_n_prev_of_misuse, child_labour_prohibition_regulation, medical_termination_of_pregnancy, prevention_of_atrocities_against_scs, prevention_of_atrocities_against_sts, protection_of_civil_rights_against_scs, protection_of_civil_rights_against_sts, prevention_of_damage_to_public_property_act, unlawful_activities_act, official_secrets_act, legal_license_arms, illegal_license_arms, other_arms, explosives_act, explosive_substances, information_technology_act, copy_right_act, the_trade_marks_act, lotteries_regulation_act, chit_funds_act, negotiable_instruments_act, benami_transaction_prohibition_act, mines_and_minerals_development_and_regulation, prevention_of_corruption, liquor_narcotic_drugs_prohibition, excise_act, possession_of_drugs_for_personal_use_consumption, possession_of_drugs_for_trafficking, forest_act_and_forest_conservation, wildlife_protection, environmental_protection, air_water_prevention_pollution_control, cigarette_and_tobacco_products, noise_pollution, national_green_tribunal, registration_of_foreigners_and_foreigners, passport_act, emigration_act, citizenship_act, indian_railways_act, railway_property_unlawful_possession, indian_telegraph, telegraph_wire_unlawful_possession, cinematograph_act, cable_television_networks_regulation, essential_commodities, prevention_of_food_adulteration, food_safety_standards, macoca_control_of_organised_crimes, gambling_act, electricity_act, antiques_and_art_treasures, representation_of_the_people, bonded_labour_against_sc, bonded_labour_against_st, bonded_labour_against_others, prevention_of_insults_to_national_honour, defacement_of_public_property, transplantation_of_human_organ, mental_health_act, motor_vehicle_act, city_town_police_acts, other_state_local_acts, other_sll_crimes, transgender_persons_protection_of_rights_act

</details>

<details><summary>All 57 variables: Districtwise Crime Against Children 2024 onwards</summary>

year, registration_circles, rape_children, attempt_commit_rape, assault_children_outrage_modesty, sexual_harassment_girls, assault_girls_disrobe, voyeurism, stalking, insult_modesty_women, kidnap_abduct_inducing_girls_compel_marriage, foeticide, infanticide, exposure_abandonment, hiring_employing_engaging_child_commit_offence, procuration_girls, procuration_boys, kidnapping_abducting_child_steal, selling_children_prostitution_girls, selling_children_prostitution_boys, buying_children_prostitution_girls, buying_children_prostitution_boys, murder_rape_pocso, other_murder, abetment_suicide_child, attempt_commit_murder, hurt_grievous, missing_children_deemed_kidnapped, kidnapping_abduction_children, kidnapping_abduction_begging, kidnapping_abduction_murder, kidnapping_abduction_ransom, importation_girls, importation_boys, other_kidnapping_abduction, otheripc_bns_crimes, pocso_376_ipc_64_68_girls, pocso_376_ipc_64_68_boys, unsafe_10_pocso_354_ipc_74_girls, unsafe_10_pocso_354_ipc_74_boys, unsafe_12_pocso_509_ipc_75_girls, unsafe_12_pocso_509_ipc_75_boys, unsafe_14_15_pocso_girls, unsafe_14_15_pocso_boys, unsafe_17_22_pocso_girls, unsafe_17_22_pocso_boys, offences_care_takers_charge_juvenile_homes, other_offences, procuring_inducing_children_prostitution, detaining_premises_where_prostitution_is_carried, other_ipt, child_labour, prohibition_child_marriage, transplantation_human_organs, publish_transmit_material_depict_child_sexually, other_cyber_crimes_children, other_sll_crimes

</details>

<details><summary>All 41 variables: Districtwise Crime Against SC 2024 onwards</summary>

year, registration_circles, rape_women, rape_children, attempt_commit_rape, assault_women, assault_children, sexual_harassment_women, sexual_harassment_children, assault_criminal_force_women_disrobe_354b, sc_st_ipc_bns_voyeurism, sc_st_ipc_bns_stalking, insult_modesty_women, kidnap_abduct_inducing_girls_compel_marriage, procuration_girls, procuration_boys, sc_st_ipc_bns_murder, attempt_commit_murder, grievous_hurt, acid_attack_124_bns, attempt_acid_attack, other_hurt_grievous, missing_children_deemed_kidnapped, children_kidnapped, kidnapping_abduction_adults, kidnapping_abduction_137_138_bns_begging, kidnapping_abduction_137_138_bns_murder, kidnapping_ransom, other_kidnapping_abduction_140_142_97, rioting_190_189_191_bns, sc_st_ipc_bns_robbery, dacoity_murder, sc_st_ipc_bns_dacoity, sc_st_ipc_bns_arson, other_ipc_bns_crimes, intentionally_insult_intimidate_humiliate, occupy_disposes_land_belongs_scs_sts, prevent_deny_obstruct_usage_public_place, force_leave_place_residence_social_boycott, other_offences, protection_civil_rights

</details>

<details><summary>All 41 variables: Districtwise Crime Against ST 2024 onwards</summary>

year, registration_circles, rape_women, rape_children, attempt_commit_rape, assault_women, assault_children, sexual_harassment_women, sexual_harassment_children, assault_criminal_force_women_disrobe_354b, sc_st_ipc_bns_voyeurism, sc_st_ipc_bns_stalking, insult_modesty_women, kidnap_abduct_inducing_girls_compel_marriage, procuration_girls, procuration_boys, sc_st_ipc_bns_murder, attempt_commit_murder, grievous_hurt, acid_attack_124_bns, attempt_acid_attack, other_hurt_grievous, missing_children_deemed_kidnapped, children_kidnapped, kidnapping_abduction_adults, kidnapping_abduction_137_138_bns_begging, kidnapping_abduction_137_138_bns_murder, kidnapping_ransom, other_kidnapping_abduction_140_142_97, rioting_190_189_191_bns, sc_st_ipc_bns_robbery, dacoity_murder, sc_st_ipc_bns_dacoity, sc_st_ipc_bns_arson, other_ipc_bns_crimes, intentionally_insult_intimidate_humiliate, occupy_disposes_land_belongs_sts, prevent_deny_obstruct_usage_public_place, force_leave_place_residence_social_boycott, other_offences, protection_civil_rights

</details>

<details><summary>All 51 variables: Districtwise Crime Against Women 2024 Onwards</summary>

year, registration_circles, rape_women, rape_girls, sexual_intercourse_employing_deceitful_means, murder_rape_gang, attempt_commit_rape_women, attempt_commit_rape_girls, assault_outrage_modesty_women, assault_women_outrage_modesty_girls, sexual_harassment_women, sexual_harassment_girls, assault_criminal_force_disrobe_women, assault_criminal_force_disrobe_girls, voyeurism_women, voyeurism_girls, stalking_women, stalking_girls, insult_modesty_women, insult_modesty_women_girls, dowry_deaths, cruelty_husband_relatives, kidnap_abduct_inducing_women_compel_marriage, kidnap_abduct_inducing_girls_compel_marriage, miscarriage, procuration_minor_girls, selling_girls_prostitution, buying_girls_prostitution, abetment_suicides_women, acid_attack, attempt_acid_attack, kidnapping_abduction_women, kidnapping_abduction_women_murder, kidnapping_ransom, importation_girls_foreign_country, women_others, dowry_prohibition, procuring_inducing_children_prostitution, detaining_premises_where_prostitution_is_carried, prostitution_vicinity_public_places, seducing_soliciting_prostitution, other_itp, protection_women_domestic_violence, publish_transmit_sexually_explicit_mtrl, other_women_centric_cyber_crimes, protection_children_sexual_violence_pocso, pocso_10, pocso_12, pocso_14_15, pocso_17_22, indecent_representation_women

</details>

<details><summary>All 51 variables: Districtwise Cyber Crimes 2024 Onwards</summary>

year, registration_circles, tampering_computer_source_documents, ransom_ware, offences_other_than_ransom_ware, dishonestly_recv_stolen_computer_resource, identity_theft, cheating_personation_using_computer_resource, violation_privacy, cyber_terrorism, pub_trans_obscene_material_electronic, publish_transmit_sexually_explicit_mtrl, publish_transmit_material_depict_child_sexually, preservation_retention_information_intermediaries, other_67_it, inter_ception_monitoring_decryption_information, un_authorized_access_attempt_protected_computer, breach_confidentiality_privacy, publication_elec_signatures_fraudulent, abetment_commit_offences, attempt_commit_offences, other_it, abetment_suicide_107_108_bns_305, cyber_stalking_bullying_women_children, sexual_intercourse_deceitful_means, organized_cyber_crimes, publishing_false_misleading_information_india_bns, data_theft, credit_card_debit, fraud_atms, online_banking_fraud, otp_frauds, gaming_app_website_fraud, marketing_investment_fraud, fraud_call_vishing, wallet_upi_fraud, other_frauds, cheating_420_ipc, offences_ipc_bns_it_forgery, defamation_morphing, fake_profile, counterfeiting_currency, counterfeiting_stamps, cyber_blackmailing_threatening, fake_news_social_media, other_offences_bns_ipc_it, offences_sll_it_gambling, offences_sll_it_lotteries, copy_right, trade_marks, other_sll_crimes

</details>

<details><summary>All 132 variables: Districtwise IPC Crime by Juveniles 2024 Onwards</summary>

year, registration_circles, offences_women_child_rape, attempt_commit_rape, sexual_intercourse_employing_deceitful_means, disclosure_identity_victim, assault_criminal_force_woman_outrage_modesty, office_premises, work_premises, public_transport_system, public_places_pathway, shelter_homes_women_children, other_place, assault_criminal_force_women_disrobe, offences_women_child_voyeurism, offences_women_child_stalking, insult_modesty_women, dowry_death, cruelty_husband_relatives, kidnp_abduc_inducing_women_marriage, offences_miscarriage, offences_women_child_foeticide, offences_women_child_infanticide, exposure_abandonment, hiring_employing_engaging_child_commit_offence, procuration_children, kidnapping_abducting_child_steal, selling_child_prostitution, buying_child_prostitution, murder, murder_group, murder_life_convict, culpable_homicide_not_amounting_murder, hit_run, other_accidents, deaths_due_negligence_rail_accidents, deaths_due_medical_negligence, deaths_due_negligence_civic_bodies, deaths_due_other_negligence, abetment_suicide, attempt_commit_murder, attempt_commit_culpable_homicide, organised_crime, petty_organised_crime, offences_affecting_human_body_terrorist, voluntarily_causing_grievous_hurt, grvus_hurt_persistent_vegetative_state, grievous_hurt_caused_group_more, vlntrly_causing_hurt_grvus_dang_weapons, vlntrly_hurt_grvus_criminal_force_deter, acid_attack, attempt_acid_attack, endangering_life_personal_safety_others, other_hurt, wrongful_restraint_confinement_341_348_ipc, missing_children, children, adults, kidnapping_abduction_begging, kidnapping_abduction_murder, kidnapping_ransom_364a_ipc, importation_girls_below_21_yrs, boys_18_yrs, other_kidnapping_abduction, endangering_sovereignty_unity_integrity_india, other_offences_state, unlawful_assembly, communal_religious, ethnic_community_group_clash_agitations, rioting_sectarian, rioting_industrial, rioting_political, caste_conflict, rioting_agrarian, rioting_students, money_dispute, water_dispute, land_property_dispute, family_disputes, enmity_rivalry, electristate_ut_power_supply_disputes, sudden_quarrel_provocation, rioting_while_aandolan_morcha, rioting_attacks_police_personnel_other_government, other_rioting, promoting_enmity_between_groups_ground_religion, assertions_prejudicial_national_integration, offences_public_tranquillity_affray, household_theft, vehicle_theft, theft_vehicles, theft_idol_icon_place_worship, theft_government_property, theft_servant_employee, other_thefts, offences_property_snatching, extortion_384_389_ipc, offences_property_robbery, unsafe_395_397_ipc_dacoity, dacoity_murder, attempt_commit_dacoity_robbery, making_preparation_assembly_committing_dacoity, criminal_misappropriation, criminal_breach_trust, dishonestly_receiving_dealing_stolen_property, day_burglary, night_burglary, counterfeit_coin, counterfeiting_government_stamp, counterfeiting_seal_mark, counterfeit_currency_bank_notes, fraud_bank, fraud_atm, credit_card_debit, other_frauds, forgery_fraud_cheating, cheating_fraud_forgery, abetment_outside_india_offence, offences_elections, disobedience_duly_promulgated_public_servant, harbouring_offender, rash_driving_public_way, obstruction_public_way, sale_obscene_books_objects, obscene_songs_public_places, offences_religion, cheating_impersonation, offences_mischief, miscellaneous_ipc_bns_crimes_arson, criminal_trespass, circulate_false_fake_news_rumours, other_ipc_bns_crimes

</details>

<details><summary>All 132 variables: Districtwise IPC crimes 2024 Onwards</summary>

year, registration_circles, offences_women_child_rape, attempt_commit_rape, sexual_intercourse_employing_deceitful_means, disclosure_identity_victim, assault_criminal_force_woman_outrage_modesty, office_premises, work_premises, public_transport_system, public_places_pathway, shelter_homes_women_children, other_place, assault_criminal_force_women_disrobe, offences_women_child_voyeurism, offences_women_child_stalking, insult_modesty_women, dowry_death, cruelty_husband_relatives, kidnp_abduc_inducing_women_marriage, offences_miscarriage, offences_women_child_foeticide, offences_women_child_infanticide, exposure_abandonment, hiring_employing_engaging_child_commit_offence, procuration_children, kidnapping_abducting_child_steal, selling_child_prostitution, buying_child_prostitution, murder, murder_group, murder_life_convict, culpable_homicide_not_amounting_murder, hit_run, other_accidents, deaths_due_negligence_rail_accidents, deaths_due_medical_negligence, deaths_due_negligence_civic_bodies, deaths_due_other_negligence, abetment_suicide, attempt_commit_murder, attempt_commit_culpable_homicide, organised_crime, petty_organised_crime, offences_affecting_human_body_terrorist, voluntarily_causing_grievous_hurt, grvus_hurt_persistent_vegetative_state, grievous_hurt_caused_group_more, vlntrly_causing_hurt_grvus_dang_weapons, vlntrly_hurt_grvus_criminal_force_deter, acid_attack, attempt_acid_attack, endangering_life_personal_safety_others, other_hurt, wrongful_restraint_confinement_341_348_ipc, missing_children, children, adults, kidnapping_abduction_begging, kidnapping_abduction_murder, kidnapping_ransom_364a_ipc, importation_girls_below_21_yrs, boys_18_yrs, other_kidnapping_abduction, endangering_sovereignty_unity_integrity_india, other_offences_state, unlawful_assembly, communal_religious, ethnic_community_group_clash_agitations, rioting_sectarian, rioting_industrial, rioting_political, caste_conflict, rioting_agrarian, rioting_students, money_dispute, water_dispute, land_property_dispute, family_disputes, enmity_rivalry, electristate_ut_power_supply_disputes, sudden_quarrel_provocation, rioting_while_aandolan_morcha, rioting_attacks_police_personnel_other_government, other_rioting, promoting_enmity_between_groups_ground_religion, assertions_prejudicial_national_integration, offences_public_tranquillity_affray, household_theft, vehicle_theft, theft_vehicles, theft_idol_icon_place_worship, theft_government_property, theft_servant_employee, other_thefts, offences_property_snatching, extortion_384_389_ipc, offences_property_robbery, unsafe_395_397_ipc_dacoity, dacoity_murder, attempt_commit_dacoity_robbery, making_preparation_assembly_committing_dacoity, criminal_misappropriation, criminal_breach_trust, dishonestly_receiving_dealing_stolen_property, day_burglary, night_burglary, counterfeit_coin, counterfeiting_government_stamp, counterfeiting_seal_mark, counterfeit_currency_bank_notes, fraud_bank, fraud_atm, credit_card_debit, other_frauds, forgery_fraud_cheating, cheating_fraud_forgery, abetment_outside_india_offence, offences_elections, disobedience_duly_promulgated_public_servant, harbouring_offender, rash_driving_public_way, obstruction_public_way, sale_obscene_books_objects, obscene_songs_public_places, offences_religion, cheating_impersonation, offences_mischief, miscellaneous_ipc_bns_crimes_arson, criminal_trespass, circulate_false_fake_news_rumours, other_ipc_bns_crimes

</details>

<details><summary>All 76 variables: Districtwise SLL Crime by Juveniles 2024 Onwards</summary>

year, registration_circles, dowry_prohibition, immoral_traffic_prevention, protection_women_domestic_violence, indecent_representation_women_prohibition, protection_children_sexual_offences, juvenile_justice_care_protection_children, prohibition_child_marriage, pre_natal_diagnostic_techniques_reg_prev, child_labour_prohibition_regulation, medical_termination_pregnancy, sc_st_prevention_atrocities_scs, sc_st_prevention_atrocities_sts, protection_civil_rights_scs, protection_civil_rights_sts, prevention_damage_public_property, unlawful_activities, official_secrets, legal_licensed_arms, illegal_unlicensed_arms, other_arms, arms_explosive_explosives, explosive_substances, information_technology, copy_right, trade_marks, lotteries_regulation, chit_funds, negotiable_instruments, benami_transaction_prohibition, mines_minerals_development_regulation, prevention_corruption, liquor_narcotic_drugs_prohibition, liquor_narcotic_drugs_excise, possession_drugs_personal_consumption, possession_drugs_trafficking, forest_conservation, wildlife_protection, environmental_protection, air_water_prevention_control_pollution, cigarette_other_tobacco_products, noise_pollution, national_green_tribunal, registration_foreigners, foreigner_passport, foreigner_passport_emigration, foreigner_passport_citizenship, indian_railways, railway_property_unlawful_possession, indian_telegraph, telegraph_wire_unlawful_possession, telegraph_cinematograph, cable_television_networks_regulation, essential_commodities, prevention_food_adulteration, food_safety_standards, macoca_control_organised_crimes, other_regulatory_enforcement_gambling, other_regulatory_enforcement_electricity, antiques_art_treasures, representation_people, bonded_labour_system_abolition_sc, bonded_labour_system_abolition_st, bonded_labour_system_abolition_others, prevention_insults_national_honour, defacement_public_property, transplantation_human_organs, other_regulatory_enforcement_transgender, rights_disabilities, prevention_cruelty_animals, mental_health, motor_vehicle, city_town_police, other_state_local, other_sll_crimes

</details>

<details><summary>All 76 variables: Districtwise SLL crimes 2024 Onwards</summary>

year, registration_circles, dowry_prohibition, immoral_traffic_prevention, protection_women_domestic_violence, indecent_representation_women_prohibition, protection_children_sexual_offences, juvenile_justice_care_protection_children, prohibition_child_marriage, pre_natal_diagnostic_techniques_reg_prev, child_labour_prohibition_regulation, medical_termination_pregnancy, sc_st_prevention_atrocities_scs, sc_st_prevention_atrocities_sts, protection_civil_rights_scs, protection_civil_rights_sts, prevention_damage_public_property, unlawful_activities, official_secrets, legal_licensed_arms, illegal_unlicensed_arms, other_arms, arms_explosive_explosives, explosive_substances, information_technology, copy_right, trade_marks, lotteries_regulation, chit_funds, negotiable_instruments, benami_transaction_prohibition, mines_minerals_development_regulation, prevention_corruption, liquor_narcotic_drugs_prohibition, liquor_narcotic_drugs_excise, possession_drugs_personal_consumption, possession_drugs_trafficking, forest_conservation, wildlife_protection, environmental_protection, air_water_prevention_control_pollution, cigarette_other_tobacco_products, noise_pollution, national_green_tribunal, registration_foreigners, foreigner_passport, foreigner_passport_emigration, foreigner_passport_citizenship, indian_railways, railway_property_unlawful_possession, indian_telegraph, telegraph_wire_unlawful_possession, telegraph_cinematograph, cable_television_networks_regulation, essential_commodities, prevention_food_adulteration, food_safety_standards, macoca_control_organised_crimes, other_regulatory_enforcement_gambling, other_regulatory_enforcement_electricity, antiques_art_treasures, representation_people, bonded_labour_system_abolition_sc, bonded_labour_system_abolition_st, bonded_labour_system_abolition_others, prevention_insults_national_honour, defacement_public_property, transplantation_human_organs, other_regulatory_enforcement_transgender, rights_disabilities, prevention_cruelty_animals, mental_health, motor_vehicle, city_town_police, other_state_local, other_sll_crimes

</details>

#### Suicides in India

The Suicides in India dataset package, published by the National Crime Records Bureau (NCRB) under its annual Accidental Deaths and Suicides in India (ADSI) reports, presents a comprehensive statistical overview of suicide patterns across the country.
*Source:* National Crime Records Bureau. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/suicides-in-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Suicides by Means Adopted | State | 2018 - 2024 | 36 states/UTs | 12,000 | 4: year, method_of_suicide, gender, number_of_deaths |
| Suicides by Profession Wise | State | 2018-2024 | 36 states/UTs | 18,108 | 4: year, profession, gender, number_of_deaths |
| Suicides by Marital Status | State | 2018 - 2024 | 36 states/UTs | 5,250 | 4: year, marital_status, gender, number_of_deaths |
| Suicides by Educational Status | State | 2018 - 2024 | 36 states/UTs | 6,750 | 4: year, educational_status, gender, number_of_deaths |
| Suicides by Economic Status | State | 2018 - 2024 | 36 states/UTs | 3,108 | 4: year, economic_status, gender, number_of_deaths |
| Suicides by Cause | State | 2018 - 2024 | 36 states/UTs | 22,500 | 4: year, cause, gender, number_of_deaths |
| Mass or Family Suicides | State | 2018 - 2024 | 36 states/UTs | 250 | 4: year, cases, married, un_married |
| Incidence and Rate of Suicides | State | 2018 - 2024 | 36 states/UTs | 249 | 4: year, number_of_suicides, percentage_share_in_total_suicides, projected_mid_year_population_in_lakh |

#### Traffic Accidents in India

The Traffic Accidents in India dataset package, published by the National Crime Records Bureau (NCRB) as part of its annual Accidental Deaths and Suicides in India (ADSI) reports, provides a comprehensive overview of road, trail and traffic-related accidents across all Indian states and union territories.
*Source:* National Crime Records Bureau. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/traffic-accidents-in-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Cases Reported, Persons Injured and Died | State | 2018 - 2024 | 36 states/UTs | 783 | 5: year, type_of_accident, cases, injured, died |
| Mode of Transport Wise Number of Persons Died in Road Accidents (2018 - 2020) | State | 2018 - 2020 | 36 states/UTs | 1,484 | 4: year, mode_of_transport, offenders, victims |
| Mode of Transport Wise Number of Persons Died in Road Accidents 2021 Onwards | State | 2021-2024 | 36 states/UTs | 1,728 | 4: year, mode_of_transport, injured, died |
| Month of Occurrence Wise Number of Traffic Accidents | State | 2018 - 2024 | 36 states/UTs | 8,964 | 4: year, accident_type, month, number_of_accidents |
| Time of Occurrence Wise Number of Traffic Accidents | State | 2018 - 2024 | 36 states/UTs | 5,976 | 5: year, accident_type, time, day_night, number_of_accidents |
| Road Classification Wise Number of Road Accidents, Injuries and Deaths | State | 2018 - 2024 | 36 states/UTs | 996 | 5: year, road_type, cases, injured, died |
| Cause Wise Distribution of Road Accidents and Unmanned Railway Crossing Accidents | State | 2018-2024 | 36 states/UTs | 3,735 | 5: year, cause, cases, injured, died |
| Place of Occurrence Wise Road Accident Deaths | State | 2018 - 2024 | 36 states/UTs | 11,205 | 4: year, place, gender, number_of_deaths |
| Classification of Railway Accidents | State | 2018 - 2024 | 36 states/UTs | 988 | 5: year, cause, cases, injured, died |
| Cause Wise Distribution of Railway Accidents | State | 2018 - 2024 | 36 states/UTs | 1,240 | 5: year, cause, cases, injured, died |

### Energy

#### Coal Usage in India

The "Coal Usage in India" package thoroughly explores coal's role within India, providing a yearly snapshot that informs on various aspects of coal consumption, production, and reserves. Designed to cater to analysts, policymakers, industry stakeholders, and researchers, this package encapsulates detailed datasets to paint a comprehensive picture of India's coal ecosystem.
*Source:* Ministry of Coal. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/coal-usage-in-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Coal Consumption Sector Wise | Other | 2006-2021 | — | 272 | 3: year, sector, quantity |
| Coal Consumption | State | 2006-2021 | 26 states/UTs | 3,086 | 3: year, sector, quantity |
| Coal Import | Other | 2006-2023 | — | 913 | 6: year, country, type, quantity, amount, price |
| Coal Reserves by Coal Type | State | 2006-2022 | 15 states/UTs | 406 | 3: year, type, quantity |
| Coal Reserves by Depth | State | 2006-2022 | 15 states/UTs | 1,436 | 4: year, depth, reserve_type, reserves |
| Coal Reserves by Field | State | 2006-2023 | 15 states/UTs | 2,629 | 4: year, coal_field, reserve_type, reserves |
| Coal Reserves | State | 2006-2023 | 21 states/UTs | 385 | 2: year, quantity |
| Domestic Coal Production | State | 2006-2023 | 16 states/UTs | 288 | 2: year, quantity |

#### Daily Coal Stocks

Coal Stocks data is taken from thermal power stations across India. The data is collected daily. It contains coal stock data by state, sector, and individual power station. The data field includes mode of transport, capacity, normative stocks, actual stocks, receipt, consumption, the criticalness of the plant, etc., for each power station.
*Source:* Ministry of Power. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/daily-coal-stocks>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Daily Coal Stocks | Power Station | 2018-2025 | 17 states/UTs | — | not previewable on the portal (download to inspect) |

#### Daily Non-Renewable Power Generation

Power Generation data is taken from nuclear, thermal and hydro power stations across india. The data is collected on daily basis. It contains generation data by state, sector, power station type, individual power station and unit level. The data field includes installed capacity, day's power generaiton target, actual generation etc. for each power station.
*Source:* Ministry of Power. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/daily-non-renewable-power-generation>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Daily Non-Renewable Power Generation | Power Station | 2017-2025 | 36 states/UTs | — | not previewable on the portal (download to inspect) |

#### Power

The Ministry of Power, India, is a governmental body responsible for the country's overall development, planning, and administration in the power sector. It oversees a vast array of functions, from power generation and transmission to policy formulation and technology development. One of its key objectives is to ensure reliable and uninterrupted power supply to all citizens.
*Source:* Ministry of Power. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/power>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Installed Capacity Statewise | State | 2017-2025 | 36 states/UTs | 9,654 | 10: date, region, sector, coal_cap, gas_cap, diesel_cap, lignite_cap, nuclear_cap, hydro_cap, res_cap |
| Daily Power Generation | Power Station | 2017-2024 | 36 states/UTs | 2,590,757 | 9: date, region, sector, station_type, power_station, power_station_unit, monitored_capacity, todays_gen_prgm, todays_gen_act |
| Energy Requirement and Availabililty | State | 2019-2023 | 36 states/UTs | 1,579 | 3: month, energy_requirement, energy_availability |
| Daily Coal Stocks | Power Station | 2018-2025 | 17 states/UTs | 362,035 | 19: date, power_station_name, sector, utility, mode_of_transport, capacity, daily_requirement, daily_receipt, daily_consumption, req_normative_stock, normative_stock_days, indigenous_stock … |
| Daily Power Outage | Power Station | 2017-2024 | 36 states/UTs | 2,664,042 | 12: date, region, sector, station_type, power_station, power_station_unit, outage_type, monitored_capacity, cap_under_outage, outage_date, expected_sync_date, remarks |
| Inter-State Generating Station(ISGS) Renewable Energy Generation | Power Station | 2019-2024 | 11 states/UTs | 200,234 | 9: date, region, solar_park, station, sector, owner, type, installed_capacity, actual_generation |
| State Control Renewable Energy Generation | State | 2019-2024 | 35 states/UTs | 61,845 | 6: date, region, wind_energy, solar_energy, other_renewable_energy, total_renewable_energy |
| Daily Renewable Energy Generation | State | 2019-2024 | 35 states/UTs | 67,014 | 6: date, region, wind_energy, solar_energy, other_renewable_energy, total_renewable_energy |
| Transmission Lines | Transmission Line | 2014-2025 | — | 2,340 | 7: date, transmission_line, circuit_type, sector, executing_agency, line_length, voltage_level |

<details><summary>All 19 variables: Daily Coal Stocks</summary>

date, power_station_name, sector, utility, mode_of_transport, capacity, daily_requirement, daily_receipt, daily_consumption, req_normative_stock, normative_stock_days, indigenous_stock, import_stock, total_stock, stock_days, plf_prcnt, actual_vs_normative_stock_prcnt, is_critical, remarks

</details>

### Rural Development

#### Mahatma Gandhi National Rural Employment Guarantee Act

The Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) dataset provides detailed information on the implementation of the MGNREGA program in India. The MGNREGA program is a flagship social welfare program of the Indian government that guarantees 100 days of employment to every rural household in the country, with a special focus on the poorest and most marginalized communities.
*Source:* Ministry of Rural Development. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/mahatma-gandhi-national-rural-employment-guarantee-act>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| MGNREGA | Gram Panchayat | 2014-2025 | — | — | not previewable on the portal (download to inspect) |

#### Pradhan Mantri Fasal Bima Yojana (PMFBY)

The Pradhan Mantri Fasal Bima Yojana (PMFBY) is a crop insurance scheme launched by the Government of India in 2016. It provides insurance coverage to farmers against crop losses resulting from natural calamities, pests, and diseases. The scheme mandates a uniform premium rate for farmers across the country. PMFBY aims to offer timely insurance payouts to farmers facing crop damages.
*Source:* Ministry of Agriculture & Farmers Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pradhan-mantri-fasal-bima-yojana-pmfby>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| State Level PMFBY | State | 2018-2022 | 22 states/UTs | 286 | 24: year, season, scheme, district_count, farmer_count, loanee, non_loanee, area_insured, sum_insured, farmer_share, goi_share, state_share … |
| PMFBY District Level | District | 2018-2022 | 26 states/UTs | 6,161 | 23: year, season, scheme, farmer_count, loanee, non_loanee, area_insured, sum_insured, farmer_share, goi_share, state_share, male … |

<details><summary>All 24 variables: State Level PMFBY</summary>

year, season, scheme, district_count, farmer_count, loanee, non_loanee, area_insured, sum_insured, farmer_share, goi_share, state_share, male, female, transgender, sc, st, obc, gen, marginal, small, other, iu_count, gross_premium

</details>

<details><summary>All 23 variables: PMFBY District Level</summary>

year, season, scheme, farmer_count, loanee, non_loanee, area_insured, sum_insured, farmer_share, goi_share, state_share, male, female, transgender, sc, st, obc, gen, marginal, small, other, iu_count, gross_premium

</details>

#### Road Connectivity-PMGSY

"The dataset provides comprehensive financial and physical progress information for all road projects that are being implemented under the Pradhan Mantri Gram Sadak Yojana (PMSGY) in India. PMSGY is a government-led initiative aimed at connecting all unconnected habitations in rural areas with all-weather roads, which is critical to the socio-economic development of rural India.
*Source:* Ministry of Rural Development. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/road-connectivity-pmgsy>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Road Connectivity-PMGSY | Road | 1960-2025 | 30 states/UTs, 673 districts, 5,172 sub-districts | — | not previewable on the portal (download to inspect) |

#### Swachh Bharat Mission - Grameen

The Swachh Bharat Mission – Grameen (SBM-G) dataset package is a collection of village-level administrative datasets that track rural sanitation infrastructure, ODF Plus implementation, waste management practices, and programme verification across India.
*Source:* Swachh Bharat Mission. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/swachh-bharat-mission-grameen>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Village Profile | Village | — | 34 states/UTs, 753 districts, 7,116 sub-districts, 254,054 panchayats, 570,290 villages | 574,101 | 16: is_lgd_exact_mapping, vil_assessment_completed, vil_with_swm, vil_with_lwm, vil_with_min_litter, vil_with_min_stagnant_water, first_verified_model, second_verified_model, video_url_model, gp_res_cert, odf_plus_cert_model, odf_plus_vil_status … |
| Liquid Waste Management - Household | Village | — | 34 states/UTs, 753 districts, 7,116 sub-districts, 253,538 panchayats, 568,413 villages | 2,860,635 | 6: is_lgd_exact_mapping, asset, sbm, mnerga, mopr, hhs_covered_per |
| Liquid Waste Management | Village | — | 34 states/UTs, 753 districts, 7,116 sub-districts, 253,633 panchayats, 568,681 villages | 1,717,341 | 7: is_lgd_exact_mapping, asset, sbm, mnerga, mopr, shared_other_vil, hhs_covered_per |
| Solid Waste Management | Village | — | 34 states/UTs, 753 districts, 7,116 sub-districts, 254,116 panchayats, 570,485 villages | 2,871,305 | 7: is_lgd_exact_mapping, asset, sbm, mnerga, mopr, shared_other_vil, hhs_covered_per |
| Solid Waste Management - Household | Village | — | 34 states/UTs, 753 districts, 7,116 sub-districts, 253,900 panchayats, 569,940 villages | 2,294,618 | 6: is_lgd_exact_mapping, asset, sbm, mnerga, mopr, hhs_covered_per |

<details><summary>All 16 variables: Village Profile</summary>

is_lgd_exact_mapping, vil_assessment_completed, vil_with_swm, vil_with_lwm, vil_with_min_litter, vil_with_min_stagnant_water, first_verified_model, second_verified_model, video_url_model, gp_res_cert, odf_plus_cert_model, odf_plus_vil_status, community_sanitary_complex, ihhl_phase_1, ihhl_phase_2, total_ihhl

</details>

### Transportation

#### Airports Authority of India

This package contains three monthly airport traffic resources for India: Aircraft Movements, Passenger Movements, and Aircraft Freight. Together, the resources cover key measures of airport activity and are organised by state, airport, airport type, and airport category.
*Source:* Airports Authority of India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/airports-authority-of-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Aircraft Movements | Airport | 2017-2026 | 36 states/UTs | 18,305 | 5: date, airport_type, airport_category, airport_name, aircraft_movement |
| Aircraft Freights | Airport | 2017-2026 | 36 states/UTs | 18,299 | 5: date, airport_type, airport_category, airport_name, freight |
| Airport Passenger Traffic | Airport | 2017-2026 | 36 states/UTs | 18,301 | 5: date, airport_type, airport_category, airport_name, passengers |

#### Maritime Trade

The "Cargo Traffic Handled at Major and Non-Major Ports" dataset, presented by the Ministry of Ports, Shipping and Waterways, chronicles the volume of cargo managed at India's significant maritime points. Organized by year and individual states, each identified by a distinct code, the dataset distinctly quantifies cargo volumes for both major and non-major ports.
*Source:* Ministry of Ports, Shipping and Waterways. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/maritime-trade>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Cargo Traffic Handled at Major and Non-Major Ports | State | 2013-2022 | 12 states/UTs | 119 | 3: year, major_ports_cargo, non_major_ports_cargo |

#### Railway Statistics

The dataset includes information about railway networks in various states or union territories. It provides details such as the year of measurement, the name of the state or union territory, the LGD (Local Government Directory) code, aggregate route length, and the total length of railway tracks.
*Source:* Indian Railways. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/railway-statistics>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Railway Networks | State | 2012-2022 | 31 states/UTs | 307 | 3: year, route_length, total_track |

#### Vehicle Registrations

Vaahan is the official digital platform of the Ministry of Road Transport & Highways, Government of India, dedicated to maintaining a comprehensive national vehicle registry. The platform centralizes data pertaining to registered vehicles across India.
*Source:* Ministry of Road Transport and Highways. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/vehicle-registrations>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| VAHAN Vehicle Registrations by Norm | Regional Transport Office | 2019-2024 | 34 states/UTs | 342,023 | 6: date, office_name, office_code, type, category, registrations |
| VAHAN Vehicle Registrations by Maker | Regional Transport Office | 2019-2024 | 34 states/UTs | 2,791,564 | 6: date, office_name, office_code, type, category, registrations |
| VAHAN Vehicle Registrations by Fuel Type | Regional Transport Office | 2019-2024 | 34 states/UTs | 418,372 | 6: date, office_name, office_code, type, category, registrations |
| VAHAN Vehicle Registrations by Vehicle Category | Regional Transport Office | 2019-2024 | 34 states/UTs | 584,267 | 6: date, office_name, office_code, type, category, registrations |
| VAHAN Vehicle Registrations by Vehicle Class | Regional Transport Office | 2019-2024 | 34 states/UTs | 857,760 | 6: date, office_name, office_code, type, category, registrations |

### Animal Husbandry and Fisheries

#### Livestock Products

The "State/UT wise Production of Major Livestock Products" dataset, curated by the Department of Animal Husbandry and Dairying, offers a comprehensive overview of livestock product outputs across the various states and union territories of India.
*Source:* Department of Animal Husbandry and Dairying. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/livestock-products>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| State/UT wise Production of Major Livestock Products | State | 2019-2021 | 37 states/UTs | 74 | 5: year, milk, egg, meat, wool |

#### Pashu Aadhaar

Pashu Aadhaar is compiled from the Bharat Pashudhan portal, where livestock are registered using a unique 12-digit Pashu Aadhaar identification number. State and district authorities record registrations digitally, and these are consolidated into the national database maintained by NDDB under NDLM.
*Source:* National Dairy Development Board. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pashu-aadhaar>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Pashu Aadhaar Registrations | District | 2001-2026 | 36 states/UTs, 769 districts | 40,330 | 5: year, type, species_name, male_count, female_count |

### Education

#### UDISE

The Unified District Information System for Education (UDISE) is an initiative by the Government of India to collate and manage data related to the education sector at the school level.
*Source:* Ministry of Education. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/udise>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Basic Details of Schools | Point | 1701-2021 | 35 states/UTs, 669 districts, 4,579 sub-districts | 1,372,195 | 36: cluster_name, pincode, ward, school_name, udise_school_code, school_category, school_type, management, year_of_establishment, longitude, latitude, status … |
| State-wise School Education Indicators (2018-19 to 2022-23) | State | 2018-2022 | 37 states/UTs | 182 | 128: year, total_schools, govt_schools, govt_aided_schools, total_teachers, govt_teachers, govt_aided_teachers, ptr_primary, ptr_upper_primary, ptr_secondary, ptr_higher_secondary, enrolment_all_management_total … |
| State-wise School Education Indicators by NEP Stage 2023 Onwards | State | 2023-2025 | 36 states/UTs | 108 | 120: year, total_schools, govt_schools, govt_aided_schools, total_teachers, govt_teachers, govt_aided_teachers, ptr_foundational, ptr_preparatory, ptr_middle, ptr_secondary, enrolment_all_management_total … |

<details><summary>All 36 variables: Basic Details of Schools</summary>

cluster_name, pincode, ward, school_name, udise_school_code, school_category, school_type, management, year_of_establishment, longitude, latitude, status, location_type, class_from, class_to, aff_board_sec, aff_board_h_sec, pre_primary, class_rooms, other_rooms, total_teachers, pre_primary_students, i_students, ii_students, iii_students, iv_students, v_students, vi_students, vii_students, viii_students, ix_students, x_students, xi_students, xii_students, class_students, class_with_pre_primary_students

</details>

<details><summary>All 128 variables: State-wise School Education Indicators (2018-19 to 2022-23)</summary>

year, total_schools, govt_schools, govt_aided_schools, total_teachers, govt_teachers, govt_aided_teachers, ptr_primary, ptr_upper_primary, ptr_secondary, ptr_higher_secondary, enrolment_all_management_total, enrolment_all_management_pre_primary, enrolment_all_management_primary_1_to_5, enrolment_all_management_upper_primary_6_to_8, enrolment_all_management_secondary_9_to_10, enrolment_all_mgmt_higher_secondary_11_to_12, enrolment_govt_total, enrolment_govt_pre_primary, enrolment_govt_primary_1_to_5, enrolment_govt_upper_primary_6_to_8, enrolment_govt_secondary_9_to_10, enrolment_govt_higher_secondary_11_to_12, enrolment_govt_aided_total, enrolment_govt_aided_pre_primary, enrolment_govt_aided_primary_1_to_5, enrolment_govt_aided_upper_primary_6_to_8, enrolment_govt_aided_secondary_9_to_10, enrolment_govt_aided_higher_secondary_11_to_12, enrolment_cwsn_primary_1_to_5, enrolment_cwsn_upper_primary_6_to_8, enrolment_cwsn_secondary_9_to_10, enrolment_cwsn_higher_secondary_11_to_12, ger_1_to_5, ger_6_to_8, ger_9_to_10, ger_11_to_12, ner_1_to_5, ner_6_to_8, ner_9_to_10, ner_11_to_12, aner_1_to_5, aner_6_to_8, aner_9_to_10, aser_6_to_10, aser_11_to_13, aser_14_15, aser_16_17, gpi_ger_1_to_5, gpi_ger_6_to_8, gpi_ger_9_to_10, gpi_ger_11_to_12, promotion_rate_1_to_5, promotion_rate_6_to_8, promotion_rate_9_to_10, repetition_rate_1_to_5, repetition_rate_6_to_8, repetition_rate_9_to_10, dropout_rate_1_to_5, dropout_rate_6_to_8, dropout_rate_9_to_10, transition_rate_5_to_6, transition_rate_8_to_9, transition_rate_10_to_11, retention_rate_1_to_5, retention_rate_1_to_8, retention_rate_1_to_10, retention_rate_1_to_12, electricity_available_all_management, electricity_available_govt, electricity_available_govt_aided, electricity_functional_all_management, electricity_functional_govt, electricity_functional_govt_aided, drinking_water_available_all_management, drinking_water_available_govt, drinking_water_available_govt_aided, drinking_water_functional_all_management, drinking_water_functional_govt, drinking_water_functional_govt_aided, toilet_boys_available_all_management, toilet_boys_available_govt, toilet_boys_available_govt_aided, toilet_boys_functional_all_management, toilet_boys_functional_govt, toilet_boys_functional_govt_aided, toilet_girls_available_all_management, toilet_girls_available_govt, toilet_girls_available_govt_aided, toilet_girls_functional_all_management, toilet_girls_functional_govt, toilet_girls_functional_govt_aided, toilet_total_available_all_management, toilet_total_available_govt, toilet_total_available_govt_aided, toilet_total_functional_all_management, toilet_total_functional_govt, toilet_total_functional_govt_aided, handwash_available_all_management, handwash_available_govt, handwash_available_govt_aided, library_available_all_management, library_available_govt, library_available_govt_aided, medical_checkup_all_management, medical_checkup_govt, medical_checkup_govt_aided, computer_available_all_management, computer_available_govt, computer_available_govt_aided, computer_functional_all_management, computer_functional_govt, computer_functional_govt_aided, internet_available_all_management, internet_available_govt, internet_available_govt_aided, cwsn_toilet_available_all_management, cwsn_toilet_available_govt, cwsn_toilet_available_govt_aided, cwsn_toilet_functional_all_management, cwsn_toilet_functional_govt, cwsn_toilet_functional_govt_aided, ramps_cwsn_all_management, ramps_cwsn_govt, ramps_cwsn_govt_aided, ramps_handrails_cwsn_all_management, ramps_handrails_cwsn_govt, ramps_handrails_cwsn_govt_aided

</details>

<details><summary>All 120 variables: State-wise School Education Indicators by NEP Stage 2023 Onwards</summary>

year, total_schools, govt_schools, govt_aided_schools, total_teachers, govt_teachers, govt_aided_teachers, ptr_foundational, ptr_preparatory, ptr_middle, ptr_secondary, enrolment_all_management_total, enrolment_all_management_foundational, enrolment_all_management_preparatory, enrolment_all_management_middle, enrolment_all_management_secondary, enrolment_govt_total, enrolment_govt_foundational, enrolment_govt_preparatory, enrolment_govt_middle, enrolment_govt_secondary, enrolment_govt_aided_total, enrolment_govt_aided_foundational, enrolment_govt_aided_preparatory, enrolment_govt_aided_middle, enrolment_govt_aided_secondary, enrolment_cwsn_foundational, enrolment_cwsn_preparatory, enrolment_cwsn_middle, enrolment_cwsn_secondary, ger_foundational, ger_preparatory, ger_middle, ger_secondary, ner_foundational, ner_preparatory, ner_middle, ner_secondary, aner_foundational, aner_preparatory, aner_middle, aner_secondary, aser_foundational, aser_preparatory, aser_middle, aser_secondary, gpi_ger_foundational, gpi_ger_preparatory, gpi_ger_middle, gpi_ger_secondary, dropout_rate_preparatory, dropout_rate_middle, dropout_rate_secondary, transition_rate_foundational_to_preparatory, transition_rate_preparatory_to_middle, transition_rate_middle_to_secondary, retention_rate_foundational, retention_rate_preparatory, retention_rate_middle, retention_rate_secondary, electricity_available_all_management, electricity_available_govt, electricity_available_govt_aided, electricity_functional_all_management, electricity_functional_govt, electricity_functional_govt_aided, drinking_water_available_all_management, drinking_water_available_govt, drinking_water_available_govt_aided, drinking_water_functional_all_management, drinking_water_functional_govt, drinking_water_functional_govt_aided, toilet_boys_available_all_management, toilet_boys_available_govt, toilet_boys_available_govt_aided, toilet_boys_functional_all_management, toilet_boys_functional_govt, toilet_boys_functional_govt_aided, toilet_girls_available_all_management, toilet_girls_available_govt, toilet_girls_available_govt_aided, toilet_girls_functional_all_management, toilet_girls_functional_govt, toilet_girls_functional_govt_aided, toilet_total_available_all_management, toilet_total_available_govt, toilet_total_available_govt_aided, toilet_total_functional_all_management, toilet_total_functional_govt, toilet_total_functional_govt_aided, handwash_available_all_management, handwash_available_govt, handwash_available_govt_aided, library_available_all_management, library_available_govt, library_available_govt_aided, medical_checkup_all_management, medical_checkup_govt, medical_checkup_govt_aided, computer_available_all_management, computer_available_govt, computer_available_govt_aided, computer_functional_all_management, computer_functional_govt, computer_functional_govt_aided, internet_available_all_management, internet_available_govt, internet_available_govt_aided, cwsn_toilet_available_all_management, cwsn_toilet_available_govt, cwsn_toilet_available_govt_aided, cwsn_toilet_functional_all_management, cwsn_toilet_functional_govt, cwsn_toilet_functional_govt_aided, ramps_cwsn_all_management, ramps_cwsn_govt, ramps_cwsn_govt_aided, ramps_handrails_cwsn_all_management, ramps_handrails_cwsn_govt, ramps_handrails_cwsn_govt_aided

</details>

#### UDISE

The Unified District Information System for Education (UDISE) is a comprehensive database of schools in India, encompassing over 1.5 million schools, 9.6 million teachers, and 264 million children.
*Source:* Ministry of Education. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/udise-2023>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| UDISE | School | Cross-section | 35 states/UTs, 669 districts, 4,579 sub-districts | — | not previewable on the portal (download to inspect) |

### Elections

#### Elections in India

The "Elections in India" package provides detailed information about various elections held in India, including both the Lok Sabha General Elections and Assembly Elections at the candidate level. This datasets is sourced from the Election Commission of India and other official governmental bodies.
*Source:* Election Commission of India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/elections-in-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Assembly Elections Data at Candidate Level | Assembly Constituency | 2009-2021 | 32 states/UTs, 654 districts | 122,559 | 21: year, month, assembly_no, ac_name, ac_type, candidate_name, sex, age, candidate_type, party, position, ac_total_candidates … |
| Loksabha General Elections at Candidate Level | Parliamentary Constituency | 2009-2019 | 37 states/UTs | 26,114 | 17: year, month, pc_code, pc_name, pc_type, candidate_name, candidate_type, sex, party, votes, position, valid_votes … |

<details><summary>All 21 variables: Assembly Elections Data at Candidate Level</summary>

year, month, assembly_no, ac_name, ac_type, candidate_name, sex, age, candidate_type, party, position, ac_total_candidates, total_electors, total_votes, total_valid_votes, vote_share_percentage, margin, margin_percentage, turnout_percentage, poll_no, delimit_id

</details>

<details><summary>All 17 variables: Loksabha General Elections at Candidate Level</summary>

year, month, pc_code, pc_name, pc_type, candidate_name, candidate_type, sex, party, votes, position, valid_votes, total_electors, turnout_percentage, vote_share_percentage, margin, margin_percentage

</details>

#### Loksabha General Election Results

The Loksabha General Election Results package is a curated collection of datasets covering multiple dimensions of India’s Lok Sabha elections across election years.
*Source:* Election Commission of India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/loksabha-general-election-results>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Constituency Wise Data Summary (2019, 2024) | Parliamentary Constituency | 2019 - 2024 | 36 states/UTs | 1,085 | 80: year, pc_name, pc_code, majority_caste, nominated_candidates_men, nominated_candidates_women, nominated_candidates_third_gender, nominated_candidates_total, nomination_rejected_candidates_men, nomination_rejected_candidates_women, nomination_rejected_candidates_third_gender, nomination_rejected_candidates_total … |
| Constituency Wise Detailed Results (2004, 2009, 2014) | Parliamentary Constituency | 2004 - 2014 | 35 states/UTs | 21,859 | 13: year, pc_name, total_electors, candidate_name, gender, age, category, party_name, party_symbol, votes_secured_general, votes_secured_postal, pct_votes_of_total_electors … |
| Constituency Wise Detailed Results (2019, 2024) | Parliamentary Constituency | 2019 - 2024 | 38 states/UTs | 17,498 | 17: year, pc_name, pc_code, total_electors, candidate_name, gender, age, category, party_name, party_symbol, total_votes_polled, valid_votes … |
| Constituency Wise Repoll Election Data (Historical) | Parliamentary Constituency | 2004 - 2014 | 25 states/UTs | 417 | 4: year, pc_name, repoll_date, no_of_repoll_stations |
| Constituency Wise Repoll Election Data (Recent) | Parliamentary Constituency | 2019 - 2024 | 23 states/UTs | 84 | 5: year, pc_name, pc_code, repoll_date, no_of_repoll_stations |
| Constituency Wise Data Summary (2004, 2009, 2014) | Parliamentary Constituency | 2004 - 2014 | 36 states/UTs | 1,629 | 76: year, pc_name, nominated_candidates_men, nominated_candidates_women, nominated_candidates_third_gender, nominated_candidates_total, nomination_rejected_candidates_men, nomination_rejected_candidates_women, nomination_rejected_candidates_third_gender, nomination_rejected_candidates_total, withdrawn_candidates_men, withdrawn_candidates_women … |

<details><summary>All 80 variables: Constituency Wise Data Summary (2019, 2024)</summary>

year, pc_name, pc_code, majority_caste, nominated_candidates_men, nominated_candidates_women, nominated_candidates_third_gender, nominated_candidates_total, nomination_rejected_candidates_men, nomination_rejected_candidates_women, nomination_rejected_candidates_third_gender, nomination_rejected_candidates_total, withdrawn_candidates_men, withdrawn_candidates_women, withdrawn_candidates_third_gender, withdrawn_candidates_total, contested_candidates_men, contested_candidates_women, contested_candidates_third_gender, contested_candidates_total, forfeited_deposit_candidates_men, forfeited_deposit_candidates_women, forfeited_deposit_candidates_third_gender, forfeited_deposit_candidates_total, general_electors_men, general_electors_women, general_electors_third_gender, general_electors_total, overseas_electors_men, overseas_electors_women, overseas_electors_third_gender, overseas_electors_total, service_electors_men, service_electors_women, service_electors_third_gender, service_electors_total, total_electors_men, total_electors_women, total_electors_third_gender, total_electors_total, general_voters_men, general_voters_women, general_voters_third_gender, general_voters_total, overseas_voters_men, overseas_voters_women, overseas_voters_third_gender, overseas_voters_total, total_voters_men, total_voters_women, total_voters_third_gender, total_voters_total, postal_voters, proxy_voters, votes_rejected_other_reason, polling_per_total, postal_votes_counted, postal_votes_deducted, valid_postal_votes, test_votes_polled_on_evm, total_deducted_votes_from_evm, votes_not_counted_from_cu, tendered_votes, total_votes_polled_on_evm, total_valid_votes_polled_on_evm, total_valid_votes_polled, nota_votes_including_postal, no_of_polling_stations, avg_electors_per_polling_station, repoll_conducted, polling_date, counting_date, result_declaration_date, winner_votes, winner_party, winner_candidate, runner_up_votes, runner_up_party, runner_up_candidate, margin_votes

</details>

<details><summary>All 13 variables: Constituency Wise Detailed Results (2004, 2009, 2014)</summary>

year, pc_name, total_electors, candidate_name, gender, age, category, party_name, party_symbol, votes_secured_general, votes_secured_postal, pct_votes_of_total_electors, pct_votes_of_total_polled

</details>

<details><summary>All 17 variables: Constituency Wise Detailed Results (2019, 2024)</summary>

year, pc_name, pc_code, total_electors, candidate_name, gender, age, category, party_name, party_symbol, total_votes_polled, valid_votes, votes_secured_general, votes_secured_postal, pct_votes_over_constituency_electors, pct_votes_over_votes_polled, pct_votes_over_valid_votes

</details>

<details><summary>All 76 variables: Constituency Wise Data Summary (2004, 2009, 2014)</summary>

year, pc_name, nominated_candidates_men, nominated_candidates_women, nominated_candidates_third_gender, nominated_candidates_total, nomination_rejected_candidates_men, nomination_rejected_candidates_women, nomination_rejected_candidates_third_gender, nomination_rejected_candidates_total, withdrawn_candidates_men, withdrawn_candidates_women, withdrawn_candidates_third_gender, withdrawn_candidates_total, contested_candidates_men, contested_candidates_women, contested_candidates_third_gender, contested_candidates_total, forfeited_deposit_candidates_men, forfeited_deposit_candidates_women, forfeited_deposit_candidates_third_gender, forfeited_deposit_candidates_total, general_electors_men, general_electors_women, general_electors_third_gender, general_electors_total, overseas_electors_men, overseas_electors_women, overseas_electors_third_gender, overseas_electors_total, service_electors_men, service_electors_women, service_electors_total, total_electors_men, total_electors_women, total_electors_third_gender, total_electors_total, general_voters_men, general_voters_women, general_voters_third_gender, general_voters_total, overseas_voters_men, overseas_voters_women, overseas_voters_third_gender, overseas_voters_total, postal_voters, proxy_voters, votes_rejected_other_reason, polling_per_men, polling_per_women, polling_per_total, total_voters, postal_votes_counted, postal_votes_deducted, valid_postal_votes, test_votes_polled_on_evm, votes_not_retrieved_from_evm, total_deducted_votes_from_evm, tendered_votes, total_votes_polled_on_evm, total_valid_votes_polled_on_evm, total_valid_votes_polled, nota_votes_including_postal, no_of_polling_stations, avg_electors_per_polling_station, repoll_conducted, polling_date, counting_date, result_declaration_date, winner_votes, winner_party, winner_candidate, runner_up_votes, runner_up_party, runner_up_candidate, margin_votes

</details>

### Forestry and Wildlife

#### CAMPA

The eGreenWatch portal, associated with the Compensatory Afforestation Fund Management and Planning Authority (CAMPA), serves as a comprehensive data repository on afforestation efforts in India. The portal offers detailed data on forest land areas that have been diverted for non-forest purposes and the subsequent compensatory afforestation projects.
*Source:* Ministry of Environment, Forest and Climate Change. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/campa>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Asset/Site-specific Non Plantations Work-site | State | 1885-2028 | 24 states/UTs | 70,472 | 12: forest_division, forest_range, asset_site, work_site_asset_code, site_area, work_initiation_year, asset_nature, forest_land_type, major_work_category, updated_on, updated_by, non_plantations_work_sites_gps_id |
| Other Plantation(Non-CA) Work-sites | State | nan | 28 states/UTs | 44,370 | 10: forest_division, forest_range, other_plantation_non_ca_site, work_site_code, area, forest_land_type, forestry_details, updated_on, updated_by, other_plantation_work_gps_id |
| CA Land Management | State | 1899-2022 | 31 states/UTs | 19,545 | 10: forest_division, forest_range, fca_project, fca_project_year, site_name, area_diverted, land_type, updated_on, updated_by, ca_land_gps_id |
| Diverted Land | State | 1899-2022 | 30 states/UTs | 12,227 | 10: division, range, fca_project, fca_project_year, site_name, area_diverted, land_type, updated_on, updated_by, diverted_land_gps_id |
| Plantation Works | State | 1980-2023 | 30 states/UTs | 56,290 | 11: forest_division, forest_range, work_site, site_nature, plantation_work, plantation_area_in_ha, start_year, duration_in_years, updated_on, updated_by, plantation_work_gps_id |

#### Wildlife and Protected Areas

The Environment Information System (ENVIS) Centre on Wildlife & Protected Areas is a pivotal initiative by India, dedicated to the collection, collation, and dissemination of information concerning the nation's diverse wildlife and their designated conservation zones.
*Source:* Ministry of Environment, Forest and Climate Change. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/wildlife-and-protected-areas>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Indian Conservation Reserves | State | 1992-2022 | 14 states/UTs | 105 | 3: year, protected_area_name, area |
| Indian Community Reserves | State | 2007-2021 | 9 states/UTs | 220 | 3: year, protected_area_name, area |

### Health

#### Health Management Information System (HMIS)

The Health Management Information System (HMIS) dataset provides comprehensive health-related information at various levels of healthcare administration in India. It covers data points related to healthcare services, diseases, maternal and child health, immunization, hospital admissions, and more.
*Source:* Ministry of Health & Family Welfare. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/health-management-information-system-hmis>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Major Health Indicators Sub-district Level | Sub District | 2017-18, 2019-20 | 36 states/UTs, 739 districts, 4,493 sub-districts | 547,336 | 288: date, sector, abortion_spontaneous, allopathic_outpatient_attendance, ayush_outpatient_attendance, blood_units_family_don, boys_reg_afhc, child_9_11m_je1, child_9_11m_meas1, child_9_11m_mr1, child_bcg, child_dpt1 … |

<details><summary>All 288 variables: Major Health Indicators Sub-district Level</summary>

date, sector, abortion_spontaneous, allopathic_outpatient_attendance, ayush_outpatient_attendance, blood_units_family_don, boys_reg_afhc, child_9_11m_je1, child_9_11m_meas1, child_9_11m_mr1, child_bcg, child_dpt1, child_dpt2, child_dpt3, child_dpt_boost1, child_hepb0, child_hepb1, child_hepb2, child_hepb3, child_ipv1, child_ipv2, child_je1, child_meas1, child_gt16m_meas2, child_mmr1, child_mr1, child_16_24m_mmr2, child_opv1, child_opv2, child_opv3, child_opv0, child_opv_boost, child_penta1, child_penta2, child_penta3, child_rota1, child_rota2, child_rota3, child_typhoid, child_vita1, child_vita5, child_vita9, child_vitk1, child_afp, child_asthma, child_diarr, child_diarr_ip, child_diphtheria, child_malaria, child_measles, child_pertussis, child_pneumonia, child_sepsis, child_sam, child_tet_neon, child_tb, child_admit_uri, child_9_11m_full_imm_f, child_9_11m_full_imm_m, child_gt10_tt10, child_gt16_tt16, child_gt5_dpt5_boost2, comp_f_ster, comp_m_ster, csec_night, death_f_ster, death_m_ster, dengue_elisa_pos, dengue_rdt_pos, emer_cardiac, emer_burn, emer_cva, emer_ob_comp, emer_snakebite, emer_trauma_acc_poison, fail_f_ster, fail_m_ster, f_nonanc_hiv_pos, f_nonanc_hiv_test, girls_reg_afhc, imm_sess_held, imm_sess_plan, inf_death_4w_asphyx, inf_death_4w_other, inf_death_4w_sepsis, inf_death_24h, antara_dose1, antara_dose4plus, antara_dose2, antara_dose3, ip_asthma_copd_resp, inpatient_deaths_female, inpatient_deaths_male, inpatient_dengue, inpatient_diarrhea_with_dehydration, inpatient_female_adults, inpatient_female_children18yrs, inpatient_head_count_at_midnight, inpatient_hepatitis, inpatient_malaria, inpatient_male_adults, inpatient_male_children18yrs, inpatient_pyrexia_of_unknown_origin_puo, inpatient_tuberculosis, inpatient_typhoid, kala_azar_positive_cases, kala_azar_rdt_tests_conducted, live_birth_female, live_birth_male, major_surg_nonobgyn, mal_pf_micro_pos, mal_pv_micro_pos, mal_pf_rdt_pos, mal_pv_rdt_pos, m_hiv_pos, m_hiv_test, mtp_gt12w, mtp_upto12w, new_htn_detect_pw, new_rtisti_f, new_rtisti_m, admit_nbsu, adol_death_acc_burn, adol_death_bite_sting, adol_death_cancer, adol_death_unknown, adol_death_diarr, adol_death_htn_hd, adol_death_hiv, adol_death_acute_dis, adol_death_chronic_dis, adol_death_neuro_stroke, adol_death_fever, adol_death_resp_inf, adol_death_suicide, adol_death_tb, vhnd_uhnd_awc_uphc, baby_cong_syph_dx, baby_cong_syph_tx, blood_tx_done, blood_units_issued, aefi_abscess, aefi_death, aefi_other, preg_ob_comp, centchroman_strips, child_death_1_5y_diarr, child_death_1_5y_fever, child_death_1_5y_measles, child_death_1_5y_other, child_death_1_5y_pneum, child_12_59m_alb, child_6_59m_ifa_8_10d, child_admit_nrc, child_nrc_wt_gain, child_gt16m_je, cop_cycles_dist, preg_comp_blood_tx, comp_iucd_ins, condom_pcs_dist, death_aes, death_dengue, death_je, death_kalaazar, death_mal_pf, death_mal_pv, death_emer_dept, death_sncu, dots_success, eclampsia_deliv_mgd, ecp_given, f_nonanc_syph_pos, f_nonanc_syph_test, hb_tests, home_deliv_non_sba, home_deliv_sba, imm_sess_asha, inf_death_1_12m_diarr, inf_death_1_12m_fever, inf_death_1_12m_measles, inf_death_1_12m_other, inf_death_1_12m_pneum, inst_deliv_csec, int_iucd_ins, int_minilap, iucd_removals, lab_tests_done, lap_ster_excl_pa, lama_cases, m_syph_pos, m_syph_test, mat_death_abort, mat_death_bleed, mat_death_fever, mat_death_ob_lab, mat_death_unknown, mat_death_htn_fits, mother_cal360_pp, mother_ifa180_pp, nb_sncu_asha_ref, nb_bf_1hr, nb_lt2_5kg, nb_hbnc6_inst, nb_hbnc7_home, nb_weighed_birth, nsv_done, dots_ongoing_reg, pa_ster_7d, pa_iucd_12d, postop_ssi, pp_ster_7d, ppiucd_48h, preterm_nb, ptk_used, pw_hiv_screen, pw_syph_test, pw_syph_pos, pw_ifa180, pw_cal360, pw_anc_steroids, pw_gdm_insulin, pw_alb_1trim, pw_misoprostol_home, pw_tt1, pw_tt2, pw_tt_boost, pw_hb7_10_9, pw_hb_lt7, pw_severe_anemia_tx, pw_4plus_anc, pw_ogtt_test, pw_hb4plus_test, pw_gdm_pos, pw_syph_poc_test, rks_meetings, suw_child_hc_0_5y, pw_syph_tx, women_pa_mtp_contra, op_major_ga_sa, op_minor_local, pw_syph_pos_above, major_gyn_hyst, boys_clin_serv, boys_counsel, girls_clin_serv, girls_counsel, screen_pos_above, hiv_conf_ictc, new_pw_htn_inst, anc_1trim_12w, hb_test_lt7, inst_deliv_48h_disch, outborn_female, outborn_male, outpatient_acute_heart_diseases, outpatient_dental, outpatient_diabetes, outpatient_epilepsy, outpatient_hypertension, outpatient_mental_illness, outpatient_oncology, outpatient_ophthalmic_related, outpatient_stroke_paralysis, mera_aspatal_score, emer_pat_reg, pa_mtp_comp_id, pa_mtp_comp_tx, pkdl_cases, usg_tests, xray_tests, mal_rdt_done, rtisti_tx_f, rtisti_tx_m, sncu_inborn_f, sncu_inborn_m, stillbirths, drug_stockout_rate, je_tests, je_pos, mal_smears_exam, csec_total, fb_mdr_done, blood_units_issued_yr, pw_anc_reg, widal_pos, widal_test, pp_check_48h_14d, pp_check_48h_home

</details>

#### National Family Health Survey (NFHS)

The NFHS package brings together district-level and state-level datasets from the National Family Health Survey (NFHS), conducted under the Ministry of Health and Family Welfare with the International Institute for Population Sciences (IIPS) as the nodal agency.
*Source:* Ministry of Health & Family Welfare. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/national-family-health-survey-nfhs>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| District Level NFHS | District | 2015-16, 2019-21, 2023-24 | 36 states/UTs, 724 districts | 1,995 | 124: year, women_15_19_anaemic, women_15_49_anaemic, family_planning_any_method, family_planning_any_modern_method, family_planning_any_traditional_method, delivery_out_of_pocket_expenditure, births_skilled_personnel, births_c_section, private_births_c_section, public_births_c_section, men_high_blood_sugar_141_160 … |
| State Level NFHS | State | 2015-16, 2019-21, 2023-24 (NFHS-4, NFHS-5, NFHS-6) | 36 states/UTs | 249 | 147: year, residence, adolescent_fertility_rate, women_15_19_anaemic, women_15_49_anaemic, family_planning_any_method, family_planning_any_modern_method, family_planning_any_traditional_method, delivery_out_of_pocket_expenditure, births_skilled_personnel, births_c_section, private_births_c_section … |

<details><summary>All 124 variables: District Level NFHS</summary>

year, women_15_19_anaemic, women_15_49_anaemic, family_planning_any_method, family_planning_any_modern_method, family_planning_any_traditional_method, delivery_out_of_pocket_expenditure, births_skilled_personnel, births_c_section, private_births_c_section, public_births_c_section, men_high_blood_sugar_141_160, women_high_blood_sugar_141_160, men_high_blood_sugar_140plus, women_high_blood_sugar_140plus, men_very_high_blood_sugar_160plus, women_very_high_blood_sugar_160plus, breastfed_children_6_23m_adequate_diet, children_12_23m_fully_vaccinated, children_12_23m_fully_vaccinated_card, children_12_23m_penta_dpt3, children_12_23m_hepb3, children_12_23m_pentavalent3, children_12_23m_polio3, children_12_23m_rotavirus3, children_12_23m_bcg, children_12_23m_any_vaccine, children_12_23m_hepb_birth, children_12_23m_mcv1, children_12_23m_vaccines_private, children_12_23m_vaccines_public, children_2_4_preschool, children_24_35m_mcv2, children_age5_preprimary, children_6_59m_anaemic, children_6_8m_solid_food_breastmilk, children_9_35m_vitamin_a, home_birth_checkup_24h, under5_overweight, under5_severely_wasted, under5_stunted, under5_underweight, under5_wasted, children_breastfed_within_1h, under5_birth_registered, under6m_currently_breastfeeding, under6m_breastfeeding_water_milk, under6m_exclusive_breastfeeding, children_postnatal_care_2days, children_diarrhoea_treated, children_diarrhoea_ors, children_diarrhoea_zinc, children_fever_respiratory_infection_treated, family_planning_condom, family_planning_users_told_side_effects, deaths_3yr_registered, men_elevated_bp_140plus, women_elevated_bp_140plus, women_breast_cancer_screened, women_cervical_cancer_screened, women_oral_cancer_screened, women_6plus_ever_school, family_planning_female_sterilization, family_planning_health_worker_talked_nonusers, home_births_skilled_personnel, households_clean_cooking_fuel, households_iodized_salt, households_women_own_house_land, households_health_insurance, households_bank_account, family_planning_iud_postpartum_iud, family_planning_injectables, institutional_births, institutional_births_public, family_planning_male_sterilization, men_15plus_alcohol, men_15plus_tobacco, men_ever_used_internet, men_10plus_schooling, men_mildly_elevated_bp, women_mildly_elevated_bp, men_moderately_severely_elevated_bp, women_moderately_severely_elevated_bp, mothers_iron_folic_acid_100plus_days, mothers_iron_folic_acid_180plus_days, mothers_anc_first_trimester, mothers_any_anc, mothers_anc_4plus_visits, mothers_postnatal_care_2days, mothers_birth_tetanus_protected, nonbreastfed_children_6_23m_adequate_diet, nonpreg_women_15_49_anaemic, family_planning_pill, population_60plus, population_under_15, population_under_5, population_improved_sanitation, population_improved_water, population_electricity, preg_women_15_49_anaemic, children_diarrhoea, children_respiratory_infection_symptoms, pregnancies_mother_child_protection_card, sex_ratio_birth, sex_ratio_total, threeplus_births_5yr, children_6_23m_adequate_diet, family_planning_unmet_need_total, family_planning_unmet_need_limiting, family_planning_unmet_need_spacing, women_15plus_alcohol, women_15plus_tobacco, women_15_19_mother_or_pregnant, women_15_24_menstrual_hygiene, women_20_24_married_before18, men_25_29_married_before21, women_use_bank_account, women_use_mobile_phone, women_literate, women_bmi_25plus, women_ever_used_internet, women_waist_hip_high_risk, women_bmi_under18_5, women_10plus_schooling

</details>

<details><summary>All 147 variables: State Level NFHS</summary>

year, residence, adolescent_fertility_rate, women_15_19_anaemic, women_15_49_anaemic, family_planning_any_method, family_planning_any_modern_method, family_planning_any_traditional_method, delivery_out_of_pocket_expenditure, births_skilled_personnel, births_c_section, private_births_c_section, public_births_c_section, men_high_blood_sugar_141_160, women_high_blood_sugar_141_160, men_high_blood_sugar_140plus, women_high_blood_sugar_140plus, men_very_high_blood_sugar_160plus, women_very_high_blood_sugar_160plus, breastfed_children_6_23m_adequate_diet, children_12_23m_fully_vaccinated, children_12_23m_fully_vaccinated_card, children_12_23m_penta_dpt3, children_12_23m_hepb3, children_12_23m_pentavalent3, children_12_23m_polio3, children_12_23m_rotavirus3, children_12_23m_bcg, children_12_23m_any_vaccine, children_12_23m_hepb_birth, children_12_23m_mcv1, children_12_23m_vaccines_private, children_12_23m_vaccines_public, children_2_4_preschool, children_24_35m_mcv2, children_age5_preprimary, children_6_59m_anaemic, children_6_8m_solid_food_breastmilk, children_9_35m_vitamin_a, home_birth_checkup_24h, under5_overweight, under5_severely_wasted, under5_stunted, under5_underweight, under5_wasted, children_breastfed_within_1h, under5_birth_registered, under6m_currently_breastfeeding, under6m_breastfeeding_water_milk, under6m_exclusive_breastfeeding, children_postnatal_care_2days, children_diarrhoea_treated, children_diarrhoea_ors, children_diarrhoea_zinc, children_fever_respiratory_infection_treated, family_planning_condom, family_planning_users_told_side_effects, married_women_3_household_decisions, deaths_3yr_registered, men_elevated_bp_140plus, women_elevated_bp_140plus, women_breast_cancer_screened, women_cervical_cancer_screened, men_oral_cancer_screened, women_oral_cancer_screened, women_18_49_spousal_violence, women_18_49_pregnancy_physical_violence, women_6plus_ever_school, family_planning_female_sterilization, family_planning_health_worker_talked_nonusers, home_births_skilled_personnel, households_clean_cooking_fuel, households_iodized_salt, households_women_own_house_land, households_health_insurance, households_bank_account, family_planning_iud_postpartum_iud, infant_mortality_rate, family_planning_injectables, institutional_births, institutional_births_public, family_planning_male_sterilization, men_15plus_alcohol, men_15plus_tobacco, men_15_19_anaemic, men_15_49_anaemic, men_25_29_married_before21, men_literate, men_bmi_25plus, men_hiv_comprehensive_knowledge, men_ever_used_internet, men_waist_hip_high_risk, men_hiv_condom_knowledge, men_bmi_under18_5, men_10plus_schooling, men_mildly_elevated_bp, women_mildly_elevated_bp, men_moderately_severely_elevated_bp, women_moderately_severely_elevated_bp, mothers_iron_folic_acid_100plus_days, mothers_iron_folic_acid_180plus_days, mothers_anc_first_trimester, mothers_any_anc, mothers_anc_4plus_visits, mothers_postnatal_care_2days, mothers_birth_tetanus_protected, neonatal_mortality_rate, nonbreastfed_children_6_23m_adequate_diet, nonpreg_women_15_49_anaemic, family_planning_pill, population_60plus, population_under_15, population_under_5, population_improved_sanitation, population_improved_water, population_electricity, preg_women_15_49_anaemic, children_diarrhoea, children_severe_diarrhoea, children_respiratory_infection_symptoms, pregnancies_mother_child_protection_card, sex_ratio_birth, sex_ratio_total, children_6_23m_adequate_diet, total_fertility_rate, family_planning_unmet_need_total, under5_mortality_rate, family_planning_unmet_need_limiting, family_planning_unmet_need_spacing, women_15plus_alcohol, women_15plus_tobacco, women_15_19_mother_or_pregnant, women_15_24_menstrual_hygiene, women_20_24_married_before18, women_use_bank_account, women_use_mobile_phone, women_own_house_land, women_literate, women_bmi_25plus, women_hiv_comprehensive_knowledge, women_ever_used_internet, women_waist_hip_high_risk, women_hiv_condom_knowledge, women_worked_paid_cash, women_bmi_under18_5, women_10plus_schooling, women_18_29_sexual_violence

</details>

### Banking

#### Bank Outlets and ATM

The dataset provides a snapshot of the banking infrastructure in India, including both active and inactive branches and ATMs. It provides comprehensive details about bank outlets and ATMs across different regions in India. It includes location information, bank details, and operational status, helping to understand the spread and accessibility of banking services in the country.
*Source:* Reserve Bank of India. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/bank-outlets-and-atm-s>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Bank Outlets and ATM | Outlets | Cross-section | 34 states/UTs, 753 districts, 5,989 sub-districts | — | not previewable on the portal (download to inspect) |

### General

#### LGD Codes

The Local Government Directory (LGD) codes serve as a standardized system of identification for administrative divisions and entities within India, including states, districts, blocks, and villages. Managed and maintained by the central government, these unique codes ensure uniformity and ease of reference across various governmental databases and systems.
*Source:* Ministry of Panchayati Raj. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/lgd-codes>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Block LGD Codes | Block | nan | 745 districts | 7,245 | 0:  |
| Gram Panchayat LGD Codes | Gram Panchayat | 2023 | 252,049 panchayats | 252,049 | 0:  |
| Villages LGD Codes | Village | 2023 | 35 states/UTs, 760 districts, 664,395 villages | 690,499 | 3: local_body_name, local_body_type, local_body_code |
| Sub District LGD Codes | Sub District | 2023 | 764 districts | 7,077 | 2: census_2001_sub_district_code, census_2011_sub_district_code |
| District LGD Codes | District | 2023 | 766 districts | 765 | 2: census_2001_district_code, census_2011_district_code |
| State LGD Codes | State | 2023 | 38 states/UTs | 38 | 2: census_2001_state_code, census_2011_state_code |

### Government Schemes

#### Pradhan Mantri Awaas Yojana - Gramin

The dataset provides an in-depth view of the Pradhan Mantri Awaas Yojana - Gramin (PMAY-G), illustrating the scheme's progress and impact at the granular level of Gram Panchayats. It includes a multi-year record of houses sanctioned and completed, with detailed breakdowns by social categories to facilitate nuanced policy assessment and socio-economic analyses.
*Source:* Ministry of Rural Development. *Licence:* License not specified. *Portal page:* <https://ckandev.indiadataportal.com/dataset/pradhan-mantri-awaas-yojana-gramin>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Pradhan Mantri Awaas Yojana - Gramin | Gram Panchayat | 2014-2025 | — | — | not previewable on the portal (download to inspect) |

### Infrastructure

#### MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act)

This package brings together Gram Panchayat-level datasets on the implementation of the Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) across India, drawn from the programme’s Management Information System, where the information is reported annually by the Ministry of Rural Development.
*Source:* Ministry of Rural Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/mgnrega-mahatma-gandhi-national-rural-employment-guarantee-act>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Category-wise Workers | Gram Panchayat | 2014-2015 to 2025-2026 | 34 states/UTs, 744 districts, 7,211 sub-districts, 262,922 panchayats | 3,207,680 | 20: year, applied_jobcards, issued_jobcards, active_jobcards, sc_active_workers, st_active_workers, others_active_workers, women_active_workers, sc_registered_workers, st_registered_workers, others_registered_workers, women_registered_workers … |
| Employment Generated | Gram Panchayat | 2014-2015 to 2025-2026 | 34 states/UTs, 744 districts, 7,211 sub-districts, 262,922 panchayats | 3,207,563 | 21: year, reg_hh, reg_pers, del_jobcards_hh, del_jobcards_pers, incl_jobcards_hh, incl_jobcards_pers, cumul_hh_jobcards_sc, cumul_hh_jobcards_sts, cumul_hh_jobcards_others, emp_demand_hh, emp_demand_pers … |
| Women Joint Accounts | Gram Panchayat | 2014-2015 to 2025-2026 | 34 states/UTs, 744 districts, 7,211 sub-districts, 262,922 panchayats | 3,207,565 | 5: year, join_acc_women, total_acc_women, women_benef_workers_with_acc, active_women_benef_workers_with_acc |
| Work Structure-wise Physical, Financial and Mandays Progress | Gram Panchayat | 2020-2021 to 2025-2026 | 34 states/UTs, 742 districts, 7,149 sub-districts, 259,777 panchayats | 16,403,302 | 6: year, work_type, work_category, completed_work, expenditure_lakhs, mandays |

<details><summary>All 20 variables: Category-wise Workers</summary>

year, applied_jobcards, issued_jobcards, active_jobcards, sc_active_workers, st_active_workers, others_active_workers, women_active_workers, sc_registered_workers, st_registered_workers, others_registered_workers, women_registered_workers, ippe_sc_registered_workers, ippe_st_registered_workers, ippe_others_registered_workers, ippe_women_registered_workers, nrlm_sc_registered_workers, nrlm_st_registered_workers, nrlm_others_registered_workers, nrlm_women_registered_workers

</details>

<details><summary>All 21 variables: Employment Generated</summary>

year, reg_hh, reg_pers, del_jobcards_hh, del_jobcards_pers, incl_jobcards_hh, incl_jobcards_pers, cumul_hh_jobcards_sc, cumul_hh_jobcards_sts, cumul_hh_jobcards_others, emp_demand_hh, emp_demand_pers, emp_offer_hh, emp_offer_pers, emp_avail_hh, emp_avail_pers, emp_avail_central_persondays, emp_avail_states_persondays, fam_completed_100_days, land_reform_benef_hh, disabled_benef_indiv

</details>

### National Sample Survey

#### Periodic Labour Force Survey (PLFS)

Periodic Labour Force Survey (PLFS) conducted by the Ministry of Statistics and Programme Implementation. The survey aims to provide comprehensive data on the labor force and demographic characteristics of the population.
*Source:* Ministry of Statistics and Programme Implementation. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/periodic-labour-force-survey-plfs>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Periodic Labour Force Survey (PLFS) | Sate | 2018-2019 | 36 states/UTs | 648 | 169: year, sector, gender, gen_edu_not_lit, gen_edu_primary, gen_edu_middle, gen_edu_secondary, gen_edu_higher_secondary, gen_edu_dip_cert, gen_edu_grad, gen_edu_post_grad_above, gen_edu_secondary_above … |
| Persons Surveyed | State | 2018-2023 | 22 states/UTs | 529 | 22: year, quarter, num_blocks_surveyed, households, males_age_0_4_years, females_age_0_4_years, persons_age_0_4_years, males_age_5_14_years, females_age_5_14_years, persons_age_5_14_years, males_age_15_29_years, females_age_15_29_years … |
| Unemployment Rate (UR) | State | 2018-2024 | 22 states/UTs | 4,761 | 5: year, quarter, age_group, gender, value |
| Worker Population Ratio (WPR) | State | 2018-2024 | 22 states/UTs | 5,175 | 5: year, quarter, age_group, gender, value |
| Labour Force Participation Rate (LFPR) | State | 2018-2024 | 22 states/UTs | 5,175 | 5: year, quarter, age_group, gender, value |
| Distribution of persons working sector wise | State | 2018-2024 | 22 states/UTs | 1,591 | 6: year, quarter, gender, agriculture_sector, secondary_sector, tertiary_sector |

<details><summary>All 169 variables: Periodic Labour Force Survey (PLFS)</summary>

year, sector, gender, gen_edu_not_lit, gen_edu_primary, gen_edu_middle, gen_edu_secondary, gen_edu_higher_secondary, gen_edu_dip_cert, gen_edu_grad, gen_edu_post_grad_above, gen_edu_secondary_above, usual_self_own_account, usual_self_helper, usual_self_all, usual_wage_salary, usual_casual_labour, lfpr_not_lit, lfpr_primary, lfpr_middle, lfpr_secondary, lfpr_higher_secondary, lfpr_dip_cert, lfpr_grad, lfpr_post_grad, lfpr_secondary_above, wpr_not_lit, wpr_primary, wpr_middle, wpr_secondary, wpr_higher_secondary, wpr_dip_cert, wpr_grad, wpr_post_grad, wpr_secondary_above, ur_not_lit, ur_primary, ur_middle, ur_secondary, ur_higher_secondary, ur_dip_cert, ur_grad, ur_post_grad, ur_secondary_above, indus_agri_forest_fish, indus_mining_quarry, indus_manufac, indus_elec_gas_ac_supply, indus_water_sewer_waste_manage, indus_cons, indus_wholesale_retail_repair, indus_transport_stor, indus_acco_food, indus_infor_comm, indus_finan_insurance, indus_real_estate, indus_prof_scientific_tech, indus_admin_support_services, indus_pub_admin_defence, indus_edu, indus_human_social_work, indus_art_entertain_rec, indus_oth_service, indus_hhs_as_employers, indus_extraterritorial_org, lfpr_usual_mpce_0_10, lfpr_usual_mpce_10_20, lfpr_usual_mpce_20_30, lfpr_usual_mpce_30_40, lfpr_usual_mpce_40_50, lfpr_usual_mpce_50_60, lfpr_usual_mpce_60_70, lfpr_usual_mpce_70_80, lfpr_usual_mpce_80_90, lfpr_usual_mpce_90_100, lfpr_usual_mpce_all, wpr_usual_mpce_0_10, wpr_usual_mpce_10_20, wpr_usual_mpce_20_30, wpr_usual_mpce_30_40, wpr_usual_mpce_40_50, wpr_usual_mpce_50_60, wpr_usual_mpce_60_70, wpr_usual_mpce_70_80, wpr_usual_mpce_80_90, wpr_usual_mpce_90_100, wpr_usual_mpce_all, ur_usual_mpce_0_10, ur_usual_mpce_10_20, ur_usual_mpce_20_30, ur_usual_mpce_30_40, ur_usual_mpce_40_50, ur_usual_mpce_50_60, ur_usual_mpce_60_70, ur_usual_mpce_70_80, ur_usual_mpce_80_90, ur_usual_mpce_90_100, ur_usual_mpce_all, cws_self_own_account, cws_self_helper, cws_self_all, cws_wage_salary, cws_casual_labour, enterprise_proprietary_partner, enterprise_govt_local_public, enterprise_autonomous, enterpirse_pub_pvt_ltd, enterprise_cooeprative, enterprise_trust_nonprofit, enterprise_emp_hhs, enterprise_oth, wage_salary_july_sep, wage_salary_oct_dec, wage_salary_jan_march, wage_salary_apr_june, wage_casual_july_sep, wage_casual_oct_dec, wage_casual_jan_march, wage_casual_apr_june, earning_self_july_sep, earning_self_oct_dec, earning_self_jan_march, earning_self_apr_june, lfpr_cws_15_above, wpr_cws_15_above, lfpr_usual_age_15_29, lfpr_usual_age_15_59, lfpr_usual_age_15_above, lfpr_usual_all, wpr_usual_age_15_29, wpr_usual_age_15_59, wpr_usual_age_15_above, wpr_usual_all, ur_usual_age_15_29, ur_usual_age_15_59, ur_usual_age_15_above, ur_usual_all, hrs_cws_july_sep_0_12, hrs_cws_july_sep_12_24, hrs_cws_july_sep_24_36, hrs_cws_july_sep_36_48, hrs_cws_july_sep_48_60, hrs_cws_july_sep_60_72, hrs_cws_july_sep_72_84, hrs_cws_july_sep_84above, hrs_cws_oct_dec_0_12, hrs_cws_oct_dec_12_24, hrs_cws_oct_dec_24_36, hrs_cws_oct_dec_36_48, hrs_cws_oct_dec_48_60, hrs_cws_oct_dec_60_72, hrs_cws_oct_dec_72_84, hrs_cws_oct_dec_84above, hrs_cws_jan_march_0_12, hrs_cws_jan_march_12_24, hrs_cws_jan_march_24_36, hrs_cws_jan_march_36_48, hrs_cws_jan_march_48_60, hrs_cws_jan_march_60_72, hrs_cws_jan_march_72_84, hrs_cws_jan_march_84above, hrs_cws_apr_june_0_12, hrs_cws_apr_june_12_24, hrs_cws_apr_june_24_36, hrs_cws_apr_june_36_48, hrs_cws_apr_june_48_60, hrs_cws_apr_june_60_72, hrs_cws_apr_june_72_84, hrs_cws_apr_june_84above

</details>

<details><summary>All 22 variables: Persons Surveyed</summary>

year, quarter, num_blocks_surveyed, households, males_age_0_4_years, females_age_0_4_years, persons_age_0_4_years, males_age_5_14_years, females_age_5_14_years, persons_age_5_14_years, males_age_15_29_years, females_age_15_29_years, persons_age_15_29_years, males_age_15_59_years, females_age_15_59_years, persons_age_15_59_years, males_age_15_above_years, females_age_15_above_years, persons_age_15_above_years, males_all_ages, females_all_ages, persons_all_ages

</details>

### Nutrition

#### Poshan Tracker

The Poshan Tracker, initiated by the Ministry of Women and Child Development, is a digital tool designed to monitor and evaluate the nutritional interventions and outcomes under the Poshan Abhiyaan, India's flagship program to combat malnutrition. It facilitates real-time tracking and monitoring of the nutritional status, growth, and development of women and children across the country.
*Source:* Ministry of Women and Child Development. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/poshan-tracker>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Poshan Statistics | District | 2023-2026 | 36 states/UTs, 780 districts | 28,258 | 58: date, project, sector, anganwadi_centers, anganwadi_workers, anganwadi_helpers, aadhar_verified_beneficiaries, eligible_beneficiaries, health_id_created, awc_infra_drink_water_src, awc_infra_func_toilets, awc_infra_own_building … |

<details><summary>All 58 variables: Poshan Statistics</summary>

date, project, sector, anganwadi_centers, anganwadi_workers, anganwadi_helpers, aadhar_verified_beneficiaries, eligible_beneficiaries, health_id_created, awc_infra_drink_water_src, awc_infra_func_toilets, awc_infra_own_building, awc_did_not_open, awc_open_atleast_1_day, awc_opened_less_than_15_days, awc_open_atleast_15_days, awc_open_atleast_21_days, awc_open_atleast_25_days, adolescent_girls, children_0_6_months, children_0_2_years, children_3_6_years, children_6_months_3_years, children_measured_0_5_years, children_measured_0_6_years, children_attend_awc_atleast_21_days, children_attend_awc_atleast_25_days, children_3_6_years_non_school_going, children_3_6_years_school_going, hcm_given_1_6_days, hcm_given_7_14_days, hcm_given_15_20_days, hcm_given_atleast_1_day, hcm_given_atleast_15_days, hcm_given_atleast_21_days, hcm_given_atleast_25_days, lactating_mothers, pregnant_women, pregnant_women_and_lactating_mother, obese_or_overweight, severely_moderately_underweight, severely_or_moderately_stunted, wasting_sam_or_mam, thr_given_atleast_1_day, thr_given_atleast_21_days, thr_given_atleast_25_days, awc_mini, awc_regular, awc_rural, awc_urban, awc_total, awc_tribal, awc_tribal_rural, awc_tribal_urban, janman_rural, janman_urban, awc_rural_pvtg, awc_urban_pvtg

</details>

### Others

#### Khelo India

The "Khelo India Medal Tally" dataset, managed by the Ministry of Youth Affairs, presents a detailed record of the performance of various states in the Khelo India games, a flagship initiative to foster sports culture in India. For each participating state, identified by its name and code, the dataset lists the number of gold, silver, and bronze medals won in different sports annually.
*Source:* Ministry of Youth Affairs. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/khelo-india>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Khelo India Medal Tally | State | 2020-21 | 37 states/UTs | 1,091 | 6: year, sport, gold, silver, bronze, total |

### Science and Technology

#### Unique Identification Authority of India(UIDAI)

The Unique Identification Authority of India(UIDAI) provides detailed insights into the Aadhaar saturation levels across various regions of India. It tracks the extent of Aadhaar enrollment and coverage, highlighting the progress and penetration of the Aadhaar program.
*Source:* Ministry of Electronics & Information Technology. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/unique-identification-authority-of-indiauidai>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Aadhaar Saturation Report | State | 2022 | 36 states/UTs | 108 | 4: date, age_bucket, population, num_of_aadhar_assigned |

### Social Welfare

#### Corporate Social Responsibility (CSR)

In India, Corporate Social Responsibility (CSR) has gained significant momentum, especially after the introduction of legal mandates. The Companies Act of 2013 made it obligatory for certain firms, based on net worth, turnover, or profitability criteria, to spend at least 2% of their average net profits from the preceding three years on CSR activities.
*Source:* Ministry of Corporate Affairs, Government of India. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/corporate-social-responsibility-csr>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| CSR Projects: Social Sector Wise Aggregated Expenditure | District | 2014-2020 | 35 states/UTs, 490 districts | 8,489 | 4: year, development_sector, project_outlay_amount_in_lakhs, amount_spent_in_lakhs |
| CSR Projects By Companies | District | 2014-2020 | 35 states/UTs, 490 districts | 36,664 | 12: year, csr_project_name, development_sector, company_name, cin, company_class, company_type, roc, company_category, listing_status, project_outlay_amount_in_lakhs, amount_spent_in_lakhs |

### Surveys

#### Handloom Census

The Handloom Census is a specialized survey undertaken to understand the intricacies of India's handloom sector, which boasts a rich heritage and provides livelihood to millions. This census captures data on the number of weavers, their socio-economic conditions, types of looms in use, patterns of production, and market dynamics.
*Source:* Ministry of Textile. *Licence:* Open Data Commons Attribution License. *Portal page:* <https://ckandev.indiadataportal.com/dataset/handloom-census>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Handloom Household LoomType and Weaving Patterns | State | 2019-2020 | 36 states/UTs | 72 | 22: year, residence_type, hh_with_loom, hh_without_loom, hh_pitloom_dobby_jacquard, hh_other_pitlooms, hh_frameloom_dobby_jacquard, hh_other_framelooms, hh_loin_looms, hh_other_looms, non_commercial_handloom_hh, hh_handloom_occ_income … |
| Non Household Production, Material Usage And Sales Channels | State | 2019-2020 | 36 states/UTs | 72 | 61: year, residence_type, company_non_hh, coop_society_non_hh, govt_corp_non_hh, producer_group_non_hh, other_entity_non_hh, pitloom_dobby_jacquard_non_hh, frameloom_dobby_jacquard_non_hh, other_frameloom_non_hh, loinloom_non_hh, other_loom_non_hh … |
| State Wise Demographic Distribution Of Allied And Handloom Workers | State | 2019-2020 | 36 states/UTs | 144 | 31: year, typ_residence, worker_type, hindu, muslim, jain, sikh, christian, buddhist, zoroastrian, other_religion, sc_workers … |
| Handloom Households Demographics, Yarn And Dye Preferences, Sourcing And Sales | State | 2019-2020 | 36 states/UTs | 72 | 93: year, type_residence, total_hh, male_weavers, male_allied_weavers, female_weavers, female_allied_weavers, transg_weaver, transg_allied_weaver, hh_antodaya_card, hh_no_anotadaya_card, kacha_house … |

<details><summary>All 22 variables: Handloom Household LoomType and Weaving Patterns</summary>

year, residence_type, hh_with_loom, hh_without_loom, hh_pitloom_dobby_jacquard, hh_other_pitlooms, hh_frameloom_dobby_jacquard, hh_other_framelooms, hh_loin_looms, hh_other_looms, non_commercial_handloom_hh, hh_handloom_occ_income, hh_handloom_domestic_commercial, hh_weaving_dhoti_sarong_lungi_angavastram, hh_weaving_saree, hh_weaving_dress_material_suiting_shirting, hh_weaving_towel_napkin_duster_gamcha, hh_weaving_bedsheet_furnishings_blanket, hh_weaving_shawls_mekhla_chadder, hh_weaving_durries_rugs_mats, hh_weaving_others, avg_fabric_prod_per_weaver_day

</details>

<details><summary>All 61 variables: Non Household Production, Material Usage And Sales Channels</summary>

year, residence_type, company_non_hh, coop_society_non_hh, govt_corp_non_hh, producer_group_non_hh, other_entity_non_hh, pitloom_dobby_jacquard_non_hh, frameloom_dobby_jacquard_non_hh, other_frameloom_non_hh, loinloom_non_hh, other_loom_non_hh, dhoti_sarong_lungi_angavastram_non_hh, saree_prod_non_hh, dress_material_prod_non_hh, towel_napkin_duster_gamcha_non_hh, bedsheet_furnishing_blanket_non_hh, shawls_mekhla_chadder_stole_non_hh, durries_rugs_mats_non_hh, other_fabric_prod_non_hh, cotton_1_20_non_hh, cotton_21_40_non_hh, cotton_41_80_non_hh, cotton_above_80_non_hh, viscose_blends_non_hh, muga_silk_non_hh, eri_silk_non_hh, mulberry_silk_non_hh, tussar_silk_non_hh, linen_non_hh, wool_non_hh, acrylic_wool_non_hh, polyester_blends_non_hh, jute_non_hh, zari_non_hh, other_yarn_non_hh, open_market_hank_yarn_non_hh, master_weaver_hank_yarn_non_hh, coop_society_hank_yarn_non_hh, nhdc_hank_yarn_non_hh, kvic_kvib_hank_yarn_non_hh, other_hank_yarn_non_hh, open_market_dyes_chem_non_hh, master_weaver_dyes_chem_non_hh, coop_society_dyes_chem_non_hh, nhdc_dyes_chem_non_hh, kvic_kvib_dyes_chem_non_hh, other_dyes_chem_non_hh, open_market_dyed_yarn_non_hh, master_weaver_dyed_yarn_non_hh, coop_society_dyed_yarn_non_hh, nhdc_dyed_yarn_non_hh, kvic_kvib_dyed_yarn_non_hh, other_dyed_yarn_non_hh, local_market_sales_non_hh, master_weaver_sales_non_hh, coop_society_sales_non_hh, fair_exhibition_sales_non_hh, export_sales_non_hh, ecommerce_sales_non_hh, other_source_sales_non_hh

</details>

<details><summary>All 31 variables: State Wise Demographic Distribution Of Allied And Handloom Workers</summary>

year, typ_residence, worker_type, hindu, muslim, jain, sikh, christian, buddhist, zoroastrian, other_religion, sc_workers, st_workers, obc_workers, no_schooling, edu_below_primary, edu_primary, edu_middle, edu_high_or_secondary, edu_higher_secondary, edu_grad_above, have_bank_acct, having_aadhar, part_time_worker, full_time_worker, independent_worker, wrk_under_master_weaver, wrk_undr_khadi_vlg_indust_cmsn_boards, wrk_undr_state_handloom_develp_corp, working_days, avg_working_days

</details>

<details><summary>All 93 variables: Handloom Households Demographics, Yarn And Dye Preferences, Sourcing And Sales</summary>

year, type_residence, total_hh, male_weavers, male_allied_weavers, female_weavers, female_allied_weavers, transg_weaver, transg_allied_weaver, hh_antodaya_card, hh_no_anotadaya_card, kacha_house, semi_pucca_house, pucca_house, own_residency, rent_residency, other_residency, income_less_5000, income_btw_5001_and_10000, income_btw_10001_15000, income_btw_15001_20000, income_btw_20001_25000, income_btw_25001_50000, income_btw_50000_100000, income_above_100000, income_less_5000_hl_related, income_btw_5001_10000_hl_related, income_btw_10001_15000_hl_related, income_btw_15001_20000_hl_related, income_btw_20001_25000_hl_related, income_btw_25001_50000_hl_related, income_btw_50001_100000_hl_related, income_above_100000_hl_related, debt_due_to_hl, debt_due_to_other_purposes, debt_due_to_hl_and_other_purposes, loan_from_cooperative_societies, loan_from_commercial_banks, loan_from_friends_or_relatives, loan_from_govt, loan_from_master_weaver, loan_from_money_lender, loan_from_other_sources, loan_from_shg, avg_hh_size, yarn_cotton_1_20, yarn_cotton_21_40, yarn_cotton_41_80, yarn_cotton_above_80, yarn_viscose_blends, yarn_muga_silk, yarn_eric_silk, yarn_mulberry_silk, yarn_tussar_silk, yarn_linen, yarn_wool, yarn_acrylic_wool, yarn_polyester_blends, yarn_jute, yarn_zari, other_yarns, input_hank_yarn_open_market, input_hank_yarn_master_weavers_group, input_hank_yarn_cooperative_society, input_hank_yarn_nat_handloom_dev_corp, input_hank_yarn_khadi_vill_indus_cmsn_or_board, input_other_types_of_hank_yarn, source_dyes_chemicals_open_market, source_dyes_chemicals_master_weavers_group, source_dyes_chemicals_cooperative_society, source_dyes_chemicals_nat_handloom_dev_corp, source_dyes_chemicals_khadi_vill_indus_cmsn, source_dyes_chemicals_other_types, input_dyed_yarn_open_market, input_dyed_yarn_master_weavers_group, input_dyed_yarn_cooperative_society, input_dyed_yarn_nat_or_state_handloom_dev_corp, input_dyed_yarn_khadi_vill_indus_cmsn, input_dyed_yarn_other_types_of_dyed_yarn, using_azo_free_dye, using_natural_dye, using_other_type_of_dye, using_dye_of_any_type, sales_local_market, sales_master_weaver_group, sales_cooperative_society, sales_organized_fairs_or_exhibition, sales_export, sales_ecommerce, sales_other_sources, members_cooperative_society, members_shg_or_joint_liability_group, hl_hh_members_of_producer_company

</details>

### Water

#### Groundwater Level

Telemetric Data, Groundwater Monitoring, Hydrology, Water Resources, Environmental Sensing, Real-Time Data, India-WRIS, Aquifer Health, Water Level Measurement, Automated Monitoring
*Source:* Ministry of Jal Shakti. *Licence:* not stated. *Portal page:* <https://ckandev.indiadataportal.com/dataset/groundwater-level>

| File | Level | Years | Coverage | Rows | Variables |
|---|---|---|---|---|---|
| Groundwater Level Collected Manually | Point | 1976-2025 | — | 2,397,271 | 21: station_name, station_code, station_type, station_status, data_acquisition_mode, agency_name, agency_id, well_type, well_aquifer_type, latitude, longitude, date_of_establishment … |
| Groundwater Level Collected Telemetric | Point | 1987-2025 | — | 29,210,237 | 21: station_name, station_code, station_type, station_status, data_acquisition_mode, agency_name, agency_id, well_type, well_aquifer_type, latitude, longitude, date_of_establishment … |

<details><summary>All 21 variables: Groundwater Level Collected Manually</summary>

station_name, station_code, station_type, station_status, data_acquisition_mode, agency_name, agency_id, well_type, well_aquifer_type, latitude, longitude, date_of_establishment, data_available_from, discharge_data_available, discharge, well_depth, date, time, data_type_code, data_type_description, data_value

</details>

<details><summary>All 21 variables: Groundwater Level Collected Telemetric</summary>

station_name, station_code, station_type, station_status, data_acquisition_mode, agency_name, agency_id, well_type, well_aquifer_type, latitude, longitude, date_of_establishment, data_available_from, discharge_data_available, discharge, well_depth, date, time, data_type_code, data_type_description, data_value

</details>

