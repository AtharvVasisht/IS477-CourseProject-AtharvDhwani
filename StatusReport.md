# Overview

Overall, we have made significant progress with the project plan and feel that we are in a good position approaching the final milestone of submitting our project. 

---

## 1. Update on Project Tasks (Relative to Project Plan)

Here, you can find the progress made on each of the tasks described in the original project plan and how that relates back to the artifacts in the repository. 

### Data Lifecycle 

In terms of the data lifecycle, we have a very clear, written narrative of the lifecycle from acquisition through analysis, ethics and reproducibility, which can be found in the project plan text. The lifecycle itself includes how we will move from the raw Zillow and BEA data to cleaned and integrated datasets, which will lead to analysis and visualization. At this point, the lifecycle has been defined conceptually and serves as a guiding point to how we have structured the repository and early scripts, but we have not yet implemented a full end-to-end workflow. 

### Ethical Data Handling (Module 2)

In terms of the ethical data handling task which corresponds to module 2, we began to operationalize the ethical data handling plans we had laid out. The raw Zillow and BEA files are stored under data/raw/ to keep the original data separate from any cleaned versions. As described in the project plan, we are keeping our use of the data within non-commercial, academic purposes by using the official Zillow and BEA sources. We also do recognize the Zillow usage constraints, such as not using the data for business purposes and not bulk-exposing property-level details. Therefore, we have planned to design our analysis and visualizations to stay within that criteria. 

### Data Collection and Acquisition (Module 3)

The next step we want to discuss is the data collection and acquisition step that mainly aligns with Module 3. The Zillow acquisition is implemented in src/data_acquisition/zillow_acquire.py. The script loads the raw Zillow file (data/raw/Zillow_Housing_Data.csv), and filters the dataset to include only the top 100 largest metropolitan cities by SizeRank align with the US national average row. The code uses head(102) because the first row is the column headers and the second row is the national average. Essentially, the rationale behind only retaining the largest 100 metro areas was that our research focuses on regions where most US residents live and where affordability trends have the most impact. 

The BEA acquisition is implemented in. So the original BEA file is provided in Excel format (BEA_PersonalIncome_Data.xlsx), we had to convert it to a CSV file (BEA_PersonalIncome_Data_converted.csv) for easier processing. The acquisition script loads both versions and performs a structural comparison by checking whether the excel_df.shape == csv_df.shape. By doing this comparison, we were able to confirm that the conversion did preserve all the rows and columns and no metadata was altered during format transformation. Both acquisition scripts also print descriptive confirmation messages and store their resulting dataframes in memory for the cleaning step. The raw files are also preserved in data/raw/ for provenance and traceability. 

### Storage and Organization (Modules 4–5)

Following data collection and acquisition we have storage and organization, associated with modules 4 and 5. We have set up a very clear repository structure that helps support our data lifecycle that was originally outlined in the project plan. Raw data is stored under data/raw/, and we have a data/processed/ directory reserved for cleaned and integrated outputs. Code is also organized under src/, which includes separate subdirectories such as src/data_acquisition/, src/data_cleaning/ and src/data_integration/. We also have a requirements.txt file, which includes pandas, numpy, openpyxl, fuzzywuzzy, and scipy, so that the software environment is essentially reproducible. This specific structure is meant to directly support the storage, organization and reproducibility goals found in Modules 4-5 in the course itself and help separate raw data, processing scripts, and output artifacts. 

---

## 3. Data Cleaning (Module 10)

Next we will focus on data cleaning from module 10, which has been a significant portion of our progress. It has been focused on handling missing values, resolving semantic inconsistencies between datasets and aligning schemas across data sources. This work has been implemented in the following two scripts: zillow_cleaning.py and bea_cleaning.py. 

### 3.1 Zillow Data Cleaning

The Zillow cleaning script is saved as "zillow_cleaning.py" and begins by importing zillow_df directly from the acquisition script. Before modifying the data, we used a shared helper function (examine_data()), to inspect the dataframe’s shape, column names, datatypes and null value counts. 

**Handling Null Values in Monthly Time-Series Columns**

The Zillow dataset contains monthly home value estimates for each metropolitan area, however we noticed that many cities have missing values in certain months due to gaps in Zillow’s internal reporting or periods where Zillow did not have sufficient data. These missing values appear exclusively in the time-series portion of the dataset. 

To address this, we implemented a forward-filling approach within the fill_null() function. For each city, this script identifies the first valid or non-null monthly value and assigns this value to any earlier months that were missing. It then applies .ffill() on the remaining time-series columns to fill nulls with. These null value fills ensure that data is complete, and mostly accurate, while ensuring that we are able to still analyze long-term trends relevant to providing meaningful conclusions during the latter portions of this project.

This approach was taken because the ZHCI metric is a continuous, monotonic and relatively smooth economic indicator for housing market trends. Missing earlier values occur because Zillow did not track the metro during those months, not because the values don’t exist. Using the earliest known value as a proxy for earlier missing periods is consistent with the discussions in class on mechanistic missingness and forward-imputation in monotonic time-series. Also, forward-filling preserves temporal continuity and avoids artificial value drops, preventing discrepancies in downstream affordability or appreciation calculations. 

**Restricting Scope to Top 100 Metros**

We also described how Zillow is already sorted by SizeRank and how we retained only the top 100 metro areas along with the national average. This choice was made to improve interpretability and to reduce the noise from small, maybe less representative markets. Essentially, the rationale behind only retaining the largest 100 metro areas was that our research focuses on regions where most US residents live and where affordability trends have the most impact. 

**Output and Validation**

After forward-filling, the cleaned dataframe is saved as data/processed/zillow_cleaned.csv. Next we ran examine_data() again to confirm that no null values remain, besides the expected StateName = NaN for the United States national row. 

### 3.2 BEA Data Cleaning

The BEA cleaning script is saved as src/data_cleaning/bea_cleaning.py, and addresses a different challenge of semantic heterogeneity. While Zillow stores city names in “RegionName” and states in “StateName”, BES does it differently by storing the entire metro identifier as a single string in the format “City, State”. Also, BEA orders cities alphabetically rather than by population size. 

**Attribute Parsing and Schema Alignment**

To better align BEA’s schema with Zillow’s, we split the “RegionName” column into two separate attributes: 

```
unadjusted_bea["City"] = unadjusted_bea["RegionName"].str.split(",").str[0]
unadjusted_bea["State"] = unadjusted_bea["RegionName"].str.split(",").str[1]
```

This helped eliminate the structural ambiguity and allows for direct comparison to Zillow’s “RegionName” field. 

**Fuzzy Matching and Levenshtein Distance for City Alignment**

The datasets do not use identical naming convention, and therefore using direct string matching would exclude valid matches. To address this issue, we used the fuzzywuzzy library with the Levenshtein distance scorer (fuzz.ratio) to perform approximate string matching: 

```
closest_match = process.extractOne(city, unadjusted_bea["City"], scorer=fuzz.ratio)
```

We applied an 80% similarity threshold, which means that only matches that met or exceeded this similarity score were retained. This helps us balance inclusiveness with accuracy and prevents false positives. 

**Filtering BEA to Match Zillow’s Top 100 Metros**

After we obtained the list of fuzzy-matched cities, we filtered the BEA dataset to include only the metros present in Zillow’s top 100. This helps us ensure that both datasets represent the same locations and eliminate unnecessary rows of data. 

**Output and Validation**

Finally, we used examine_data() again to confirm that no null values were added during the cleaning process and saved the cleaned dataset as data/processed/bea_cleaned.csv.

---

## 4. Extraction & Enrichment (Module 6 – Partially Completed)

We realize that full metric extraction will occur after dataset integration, however we have still implemented foundational enrichment components. First, we created the city/state parsing logic needed to align BEA and Zillow naming conventions. Also, we implemented fuzzy matching to address the semantic heterogeneity between Zillow and BEA. Finally, we developed a reusable examine_data() function to support data quality checks throughout the cleaning and integration phase. 

All these components will serve us during the integration and analysis stage to build metrics such as house price-to-income ratios and metro level appreciation rates. 

---

## 5. Current Status & Next Steps

### Immediate Next Steps (Modules 7–9)

**Data Integration**

Now that we have completed the cleaning, the next stage will be to merge zillow_cleaned.csv and bea_cleaned.csv on the shared “City” and “State” identifiers. This unified dataset will help us with the affordability analysis, where Zillow will provided a long time series (2000-2024) and BEA provides recent annual incomes (2021-2023). The overlapping years (2021-2023) will be used for affordability analysis, while Zillow’s historical data will be used for long term appreciation analysis. This integration is 95% complete and analysis will be conducted beginning very soon.

**Data Quality Assessment**

After actual integration, we will evaluate the correctness of the fuzzy matching, the completeness of overlapping time periods, outliers in price-to-income ratios and consistency between the datasets. This will align with module 9 on data quality and verification. 

### Remaining Work (Modules 11–15)

**Workflow Automation**

Looking ahead for the final submission to address workflow automation, we will build a reproducible script that connects the acquisitions, cleaning and integration steps into one executable workflow. 

**Documentation, Metadata & Reproducibility**

In order to do this we want to produce a README describing the setup and execution, data dictionaries for Zillow and BEA, metadata files detailing transformations, and clear descriptions of all assumptions and limitations. 

**Analysis Phase**

As part of our analysis phase we will calculate the following after integration is complete:
- Housing affordability ratios
- Long-run appreciation metrics
- Metro-level comparisons
- Visualizations to address our research questions about appreciation, affordability, and investment potential

We did not make any changes to our plan, as based on feedback from Milestone 2, we were on track to achieving the initial goals we had set for this project.

---

## 6. Technical Achievements

In terms of our technical achievements, we have thus far completed cleaning of both Zillow and BEA datasets. We have also addressed schema and semantic heterogeneity, along with implementing forward-fill for time-series null values. Additionally, we used fuzzy and Levenshtein matching  to align metro names and established a reproducible, modular Python pipeline. 

---

## 7. Challenges Addressed

We have addressed the challenges of missing temporal values in Zillow’s monthly data and dealt with mismatched city naming formats between datasets. We have also limited BEA to top 100 metros through approximate matching and ensured that both datasets are prepared for integration.

---

## 8. Overall Project Status

In conclusion, the overall project is on track as we had initially planned. The data acquisition and cleaning are complete. The repository structure is organized and we are positioned to begin dataset integration and analysis in the following weeks. 

---

## 9. Updated Project Timeline 

| Task                                                         | Status                                    |
|--------------------------------------------------------------|-------------------------------------------|
| <span style="color:green">Data lifecycle: Dhwani (Completed)</span> | <span style="color:green">Done</span>                  |
| <span style="color:green">Ethical data handling (cf. Module 2): Atharv (Completed)</span> | <span style="color:green">Done</span>  |
| <span style="color:green">Data collection and acquisition (cf. Module 3): Dhwani (Completed)</span> | <span style="color:green">Done</span>  |
| <span style="color:green">Storage and organization (cf. Modules 4-5): Atharv (Completed)</span> | <span style="color:green">Done</span>  |
| <span style="color:orange">Extraction and enrichment (cf. Module 6): Dhwani (In Progress)</span> | <span style="color:orange">In Progress</span> |
| <span style="color:orange">Data integration (cf. Module 7-8): Atharv (In Progress, complete by 11/15)</span> | <span style="color:orange">In Progress</span> |
| <span style="color:orange">Data quality (cf. Module 9): Dhwani (In Progress, complete by 11/17)</span> | <span style="color:orange">In Progress</span> |
| <span style="color:green">Data cleaning (cf. Module 10): Atharv (Completed)</span> | <span style="color:green">Done</span>  |
| <span style="color:red">Workflow automation and provenance (cf. Module 11-12): Dhwani & Atharv (Complete by 11/20)</span> | <span style="color:red">To Do</span> |
| <span style="color:red">Reproducibility and transparency (cf. Module 13): Dhwani & Atharv (Complete by 11/27)</span> | <span style="color:red">To Do</span> |
| <span style="color:red">Metadata and data documentation (cf. Module 15): Dhwani & Atharv (Complete by 12/2)</span> | <span style="color:red">To Do</span> |