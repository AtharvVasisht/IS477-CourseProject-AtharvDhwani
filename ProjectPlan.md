# US Housing Market Valuations & Affordability Analysis
## By Atharv Vasisht & Dhwani Patel

### Overview ###
The US housing market has experienced significant valuation increases over the past 25 years, ranging from strong domestic net migration, low interest rates, rising income inequality, and increased costs for housing materials. To study the trend of housing prices nationwide, and more specifically understand the nuances of housing price changes across various US metropolitan areas over the past 25 years, we have decided to examine how exactly housing prices have changed, what patterns have emerged, and how homebuyers in 2025 can conceptualize this data to make adequate lifestyle/investment decisions. 

Macroeconomic trends have largely shaped housing price fluctuations in recent decades, with certain regions/metropolitan areas experiencing fast housing price appreciations (such as those in the West and South), while other regions experiencing sluggish growth due to net out migration, local industry trends, and broad nation-wide patterns that have rippled throughout housing markets. However, the purpose of this research is less about solely identifying which metros have appreciated most and which haven't, but is rather more about understanding the *why* behind these trends, and more importantly, determining the implication this has on homeowners and buyers in terms of purchasing power. Although it is relatively well known that the US middle class has shrunk in recent decades due slow wage growth and skyrocketing asset prices, the extent of disparity is something we would also like to study during this analysis. *More specifically, we want to understand, in today's housing market, how does an American's income in a given metropolitan area compare to the current housing prices in the market, the level of housing price appreciation that market has experienced (along with long-term growth expectations), and the metropolitan area's affordability (house price-to-income ratio) when compared to other metropolitan areas.*

The overarching goal of this project is to (a) identify the patterns associated with the national real estate market, and (b) provide reasoning behind practical advice Americans may follow to best leverage the existing state of the real estate market while also being aware of potential future patterns in emergence. 

### Research Questions ###
To delve deeper into the trends and goals identified above, we have the following questions we would like to answer throughout the course of this analysis and proposal:

1. Which American metropolitan areas have seen the largest housing market appreciations since the year 2000, and given these trends, which housing markets make the most sense for Americans to invest in real estate? 
2. Which housing markets are currently trading at a "discount" and which ones are 
"oversaturated" and bound for a correction?
3. How can everyday Americans maximize their incomes to identify homes/housing markets that provide the best value in terms of present day affordability (House price-to-Income ratio) and long-term growth potential (based on historic growth rates)?

These research questions have provided us with guidance and clarity as we have continuosly identified, iterated upon, and began utilizing datasets for analysis. 

### Team ###
While both team members (Atharv and Dhwani) aim at fulfilling and collaborating on all responsibilities, we aim at distributing responsibilities in a way that enable both members to perform to their strengths, and effectively handle specific workflows related to the project. Both members will focus on ensuring success in all aspects of the data lifecycle management; ensuring quality control from ethical data handling, storage and organization, data cleaning/integration, quality/assessment, and most importantly, reproducibility. Throughout this data lifecycle process, Atharv's main focus will revolve around ensuring adequate/ethical data handling, data cleaning, and integration between both datasets to ensure a streamlined ability for machine learning, visualization, and analysis. Meanwhile, Dhwani will prioritize tracking technical documentation, data visualization, and proper extraction for metrics, key conclusions, and takeaways. By strategically allocating "focus areas" and specific responsibilities, while having goals such as "biweekly progress checks" meant to faciliate strong collaboration, we, as a team, aim to ensure for successful data ingestion for analysis.

Through this collaboration, we aim at providing a conclusive final synthesis and report, showcasing the details of this project and the significance our analysis has on homeowners and buyers across the US. Additionally, our analysis aims at drawing upon key data ethics, reproducibility, privacy, and purpose principles to ensure our project meets proper code of conduct. 

1. Atharv Vasisht – Technical Analysis & Data Infrastructure

**Goals:**

Develop a robust data pipeline to integrate, clean, and analyze large-scale datasets from Zillow and the BEA.

Apply reproducible data management principles to ensure the entire project workflow can be replicated accurately.

Provide the analytical foundation to link macroeconomic patterns to housing affordability trends.

**Responsibilities:**

**Ethical Data Handling (Module 2):** Ensure that all datasets (Zillow, BEA) comply with usage and licensing terms; verify data reproducibility and citation standards.

**Storage & Organization (Modules 4–5):** Establish a well-documented, version-controlled file structure in GitHub for storing raw, processed, and cleaned data.

**Data Integration (Modules 7–8):** Combine housing valuation and income datasets to create metro-level affordability indices and growth metrics.

**Data Cleaning (Module 10):** Handle missing values, normalize variables across years, and validate statistical consistency between data sources.

**Technical Documentation (Module 13 & 15):** Maintain clear metadata, data dictionary, and processing logs for full transparency.

**Workflow Collaboration:** Work with Dhwani to automate reproducibility scripts and ensure all analyses are trackable in the final deliverable.

2. Dhwani Patel – Data Acquisition & Quality Assurance

**Goals:**

Collect and validate all primary datasets while ensuring adherence to ethical, reproducible data practices.

Oversee data enrichment and validation to guarantee data accuracy, consistency, and contextual relevance.

Support analytical interpretation of findings by ensuring reliable data quality and documentation.

**Responsibilities:**

**Data Lifecycle Management:** Outline and monitor each phase from acquisition to analysis, ensuring data completeness.

**Data Collection & Acquisition (Module 3):** Extract Zillow ZHVI and BEA income data directly from official sources, verifying download integrity and schema.

**Extraction & Enrichment (Module 6)**: Derive additional metrics (growth rates, affordability ratios) and annotate data with contextual metadata.

**Data Quality Assessment (Module 9):** Conduct consistency checks, identify outliers, and validate inter-year continuity for time-series data.

**Workflow Automation & Provenance (Modules 11–12):** Collaborate on version control and automated data updates using reproducible scripts.

**Reproducibility & Transparency (Modules 13 & 15):** Contribute to final documentation detailing data lineage, methodology, and ethical considerations.

3. Joint Responsibilities (Atharv & Dhwani)

**Weekly Progress Coordination**: Meet twice a week (Tuesday and Thursday) to align progress, track deliverables, and update interim status reports.

**Final Synthesis**: Co-author final analytical insights, visualizations, and recommendations for homebuyers and policymakers.

**Reproducibility & Presentation**: Ensure the final submission includes clear code, references, and transparent methodological explanation for reproducibility.

### Datasets ###
1. Zillow Housing Data: https://www.zillow.com/research/data/
    • **Description**: This dataset (CSV) is pulled directly from Zillow itself. Because Zillow pulls data on an annual basis from its listings, real estate data, and satelite imaging tools, it is effectively a direct source that is straight from the root. This makes it much more accurate and compliant from a data ethics and reproducibility standpoint as opposed to retrieving data from third-party sources such as Kaggle. On Zillow's website, we are particularly using the *Zillow Home Values Index (ZHVI)* for US Metro areas. The dataset is "available as a smoothed, seasonally adjusted measure and as a raw measure" according to the website. Additionally, Zillow permits the usage of this data for personal use as long as it isn't used for business purposes. The following description below is Zillow's exact terms for its data (csv file) and or API.

        You agree to the following terms, only with respect to the Property Details API:

            • You may not use the Zillow Data to provide a service for other businesses.
            • You must use commercially reasonable efforts to prevent the Zillow Data from being downloaded in bulk or otherwise scraped. Such efforts include “spider traps,” “C.A.P.T.C.H.A.,” velocity checks, source IP analysis, or other methods that are as effective.
            • You may present data on no more than 20 individual properties at a time to any given user (e.g., per Web page).

2. US Department of Commerce - Bureau of Economic Analysis (BEA): https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas
    • We will particularly be utilizing the "Metropolitan Area Table" within this link, which focuses on per capita personal income across all US metropolitan areas. This metric will allow us to understand how personal income compares to home prices across various metropolitan areas, allowing us to evaluate more than home prices themselves but rather home affordability in metropolitan areas. Similar to Zillow, this dataset is collected by the Department of Commerce itself, making it a reliable direct source as opposed to a third-party source. This ensures for successful reproducibility and will enable us to ensure that we are properly abiding by license agreements, terms of use, etc. The BEA clearly states that the data in the site are aimed to be accessible for everyone, and doesn't have any specific guidelines on how the data may be used for an individual/personal standpoint within its policies (https://www.bea.gov/about/policies-and-information). 

### Project Timeline ###
For the project timeline, even though we have delegated tasks to an extent, we plan on working together for each of these requirements. The individual responsible for the requirement will be responsible for submitting and refining the final product we submit to make sure the responsibility is shared. We will approach this project timeline with the same cadence as we have class. So we will aim to complete 2 tasks each week, one on Tuesday and one on Thursday. The Interim Status Report will also be worked on every week to update the progress of the project for that week by Friday. This means that we will complete the project in approximately 5 weeks, putting us at Nov, 14th. We will keep the week of November 17th to make final changes and polish the final product before Fall Break. Given this timeline, we will have the week of December 3 to make any changes and adjust for any delays if we experience any. 

    •    Data lifecycle: Dhwani 

    •    Ethical data handling (cf. Module 2): Atharv 

    •    Data collection and acquisition (cf. Module 3): Dhwani 

    •    Storage and organization (cf. Modules 4-5): Atharv

    •    Extraction and enrichment (cf. Module 6): Dhwani 

    •    Data integration (cf. Module 7-8): Atharv

    •    Data quality (cf. Module 9): Dhwani

    •    Data cleaning (cf. Module 10): Atharv 

    •    Workflow automation and provenance (cf. Module 11-12): Dhwani & Atharv

    •    Reproducibility and transparency (cf. Module 13):  Dhwani & Atharv

    •    Metadata and data documentation (cf. Module 15): Dhwani & Atharv

### Constraints & Gaps ###
While the data sources we have picked are as wholistic, accurate, and direct as possible, there are some constraints that must be considered when conducting analysis on our data.

1. Data Availability: While zillow and BEA both have relatively complete, standardized, and normalized data, there are some metropolitan areas that have inconsistent, incomplete, or null data that must be properly handled via imputation, pandas null handling, mean reversion, etc. Additionally, BEA provides income data in recent years but doesn't have data trailing back to 2000 - this is a constraint we must consider when conducting our analysis.
2. Data Normalization & Usage Limits: We must ensure that data is normalized between both data sources - although they do seem to be normalized at first glance, we must ensure that both are expressed in similar terms. For example, if the zillow data is expressed in nominal USD (not adjusted for inflation) and the BEA data is expressed in real USD (inflation adjusted), this could cause problems in analysis accuracy. We must ensure we are understanding the fine prints of how this data is collected. Additionally, as per the terms of conditions, we must ensure make sure that our analysis is being used for academic purposes only, with non-commercial intent.
3. Time Constraints: Given we have less than 2 months to complete this project, we must identify optimal ways to conduct predictive analytics - ensuring that they are wholistically representing data while also feasible to conduct in the given time. We must utilize proper research practices while also acknolwedging that we are time-bound when creating models that are both plausible and accurate.
4. Visualization Gaps: While we do aim to use tools within python, excel, SQL, HTML, or PowerBi, we will need input in coming weeks on how to visualize data for our given subject matter. These visualizations will be crucial in aiding our overall analysis in terms of both accuracy and ease of interpretation for us and our audience respectively.

### Next Steps ###
With these considerations in mind, we aim to begin conducting our analysis by examining our datasets. This includes conducting exploratory data analysis and ensuring that we are understanding the fine prints regarding how the Zillow and BEA data were collected, in what standards they were normalized, and what these conditions mean for our analysis moving forward. Additionally, a crucial first step will involve conducting ethical assessments on the usability of this data and its future reproducibiility, along with ensuring proper handling of the aforementioned constraints to allow for wholistic data representation. These next steps will be conducted in accordance with the best practices described in IS 477 coursework and beyond. 
