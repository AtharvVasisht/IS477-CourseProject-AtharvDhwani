# Housing Affordability and Income Trends Across Major U.S. Metropolitan Areas

## Contributors
- **Atharv Vasisht**
- **Dhwani Patel**

---

## Summary (Project Description, Motivation, Research Question, Findings)

This project examines the relationship between housing market trends and personal income growth across the 100 largest US metropolitan areas by integrating housing data from Zillow (2000-2025) with personal income statistics from the U.S. Bureau of Economic Analysis (BEA). 

**Motivation:** The US housing market has experienced significant valuation increases over the past 25 years, ranging from strong domestic net migration, low interest rates, rising income inequality, and increased costs for housing materials. To study the trend of housing prices nationwide, and more specifically understand the nuances of housing price changes across various US metropolitan areas over the past 25 years, we have decided to examine how exactly housing prices have changed, what patterns have emerged, and how homebuyers in 2025 can conceptualize this data to make adequate lifestyle/investment decisions. 

Macroeconomic trends have largely shaped housing price fluctuations in recent decades, with certain regions/metropolitan areas experiencing fast housing price appreciations (such as those in the West and South), while other regions experiencing sluggish growth due to net out migration, local industry trends, and broad nation-wide patterns that have rippled throughout housing markets. However, the purpose of this research is less about solely identifying which metros have appreciated most and which haven't, but is rather more about understanding the *why* behind these trends, and more importantly, determining the implication this has on homeowners and buyers in terms of purchasing power. Although it is relatively well known that the US middle class has shrunk in recent decades due slow wage growth and skyrocketing asset prices, the extent of disparity is something we would also like to study during this analysis. 

**Research Question:** More specifically, we want to understand, in today's housing market, how does an American's income in a given metropolitan area compare to the current housing prices in the market, the level of housing price appreciation that market has experienced (along with long-term growth expectations), and the metropolitan area's affordability (house price-to-income ratio) when compared to other metropolitan areas. Our specific research questions have revolved around the following areas: 

1. Which American metropolitan areas have seen the largest housing market appreciations since the year 2000, and given these trends, which housing markets make the most sense for Americans to invest in real estate? 
2. Which housing markets are currently trading at a "discount" and which ones are 
"oversaturated" and bound for a correction?
3. How can everyday Americans maximize their incomes to identify homes/housing markets that provide the best value in terms of present day affordability (House price-to-Income ratio) and long-term growth potential (based on historic growth rates)?

**Project Design & Process:** This project was intentionally designed by both Dhwani and I in a comprehensive process that enabled us to deliver relevant insights that would bring us closer to answer these research questions. Additionally, all stages of this project was structured with the intent to maximize structural data handling. All stages of this data lifecycle are represented within the repository, including ethical data acquisition, storage and organization, data quality assessment, cleaning, integration, analysis, workflow automation, and ultimate reproducibility. 

Feedback received during earlier milestones (MS1, MS2, & MS3) have enabled us to refine and confirm the validity of our project scope, dataset selection, and analytical direction. As a result, no substantive changes were made to our project design after the interim review. Our efforts have primarily focused on ensuring adequate, accurate, and complete data integration between both datasets (Zillow & BEA), followed by adequate analysis and workflow automation initiatives. As we've continued to iterate on project direction, our efforts have been accompanied by continuously improving documentation and reproducibility.

More information on the project description, research questions, and data considerations can be found in the root directory of this repository under ProjectPlan.md (link: https://github.com/AtharvVasisht/IS477-CourseProject-AtharvDhwani/blob/main/ProjectPlan.md).

**Findings (Summarized):** Type here...

## Data Profile

**1. Zillow Housing Data: https://www.zillow.com/research/data/** 

**Source:** Zillow Research
**Format:** CSV
**Access Method:** Direct Download
**Coverage:** Metropolitan areas and U.S. national aggregate data

    • Description: This dataset (CSV) is pulled directly from Zillow itself. Because Zillow pulls data on an annual basis from its listings, real estate data, and satelite imaging tools, it is effectively a direct source that is straight from the root. This makes it much more accurate and compliant from a data ethics and reproducibility standpoint as opposed to retrieving data from third-party sources such as Kaggle. On Zillow's website, we are particularly using the *Zillow Home Values Index (ZHVI)* for US Metro areas. The dataset is "available as a smoothed, seasonally adjusted measure and as a raw measure" according to the website. Additionally, Zillow permits the usage of this data for personal use as long as it isn't used for business purposes. The following description below is Zillow's exact terms for its data (csv file) and or API.

        You agree to the following terms, only with respect to the Property Details API:

            • You may not use the Zillow Data to provide a service for other businesses.
            • You must use commercially reasonable efforts to prevent the Zillow Data from being downloaded in bulk or otherwise scraped. Such efforts include “spider traps,” “C.A.P.T.C.H.A.,” velocity checks, source IP analysis, or other methods that are as effective.
            • You may present data on no more than 20 individual properties at a time to any given user (e.g., per Web page).

**Ethical and Legal Constraints:** Because we are utilizing this Zillow data solely for educational purposes (non-commercial), we remain in compliance from a data usability standpoint. Additionally, the dataset contains no personally identifiable metadata and reports values at an aggregated metropolitan area level, which is generic. This ensures that no privacy or confidentiality constraints are being violated. Overall, we remain in compliance with all data ethics and reproducibility standards. 

**2. US Department of Commerce - Bureau of Economic Analysis (BEA): https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas**

**Source:** U.S. Bureau of Economic Analysis
**Format:** Excel (converted to CSV during /src/acquisition)
**Access Method:** Federal open data
**Coverage:** Metropolitan areas and U.S. national aggregate data

    • Description: We will particularly be utilizing the "Metropolitan Area Table" within this link, which focuses on per capita personal income across all US metropolitan areas. This metric will allow us to understand how personal income compares to home prices across various metropolitan areas, allowing us to evaluate more than home prices themselves but rather home affordability in metropolitan areas. Similar to Zillow, this dataset is collected by the Department of Commerce itself, making it a reliable direct source as opposed to a third-party source. This ensures for successful reproducibility and will enable us to ensure that we are properly abiding by license agreements, terms of use, etc. The BEA clearly states that the data in the site are aimed to be accessible for everyone, and doesn't have any specific guidelines on how the data may be used for an individual/personal standpoint within its policies (https://www.bea.gov/about/policies-and-information). 

**Ethical and Legal Constraints:** BEA data is part of the U.S. federal statistical system and is therefore openly licensed for reuse, as stated above. Additionally, because there is no personally identifiable metadata, no privacy or confidentiality constraints apply for this project beyond proper attribution, which is done throughout all project plans, files, and stats reports. 

Dataset considerations are explained adequately in the root directory under "StatusReport.md" (link: https://github.com/AtharvVasisht/IS477-CourseProject-AtharvDhwani/blob/main/StatusReport.md) for further information on ethical and legal considerations taken into account while acquiring, cleaning, and integrating data.

## Data Quality

We ensured that data quality was assessed independently and wholistically for both datasets throughout the data acquisition and cleaning process, and well-prior to integration. Throughout our process, data quality remained essential to integration, and was re-evaluated iteratively throughout the project and revisited after each main processing stages. Our approach aligns directly with the practices highlighted in Module 9 of this course, with particular emphasis on systematic data inspection (leveraging file paths, print statements, and other practices to "see" the data at all cleaning phases), documentation of assumptions throughout the process, and validation that data integrity is maintained throughout all steps of acquisition, cleaning, and integration. We additionally created and utilized helper functions, such as examine_data() to return null values, shape misconfigurations, and any integrity checks at all steps of our process. Below, is a description of our data quality assessment for both sources, with additional information to be found throughout the comments and code of these files.

### Zillow Data Quality Assessment

The Zillow cleaning script is saved as "zillow_cleaning.py" and begins by importing zillow_df directly from the acquisition script. Before modifying the data, we used a shared helper function (examine_data()), to inspect the dataframe’s shape, column names, datatypes and null value counts. 

**Handling Null Values in Monthly Time-Series Columns**

The Zillow dataset contains monthly home value estimates for each metropolitan area, however we noticed that many cities have missing values in certain months due to gaps in Zillow’s internal reporting or periods where Zillow did not have sufficient data. These missing values appear exclusively in the time-series portion of the dataset. 

To address this, we implemented a forward-filling approach within the fill_null() function. For each city, this script identifies the first valid or non-null monthly value and assigns this value to any earlier months that were missing. It then applies .ffill() on the remaining time-series columns to fill nulls with. These null value fills ensure that data is complete, and mostly accurate, while ensuring that we are able to still analyze long-term trends relevant to providing meaningful conclusions during the latter portions of this project.

This approach was taken because the ZHCI metric is a continuous, monotonic and relatively smooth economic indicator for housing market trends. Missing earlier values occur because Zillow did not track the metro during those months, not because the values don’t exist. Using the earliest known value as a proxy for earlier missing periods is consistent with the discussions in class on mechanistic missingness and forward-imputation in monotonic time-series. Also, forward-filling preserves temporal continuity and avoids artificial value drops, preventing discrepancies in downstream affordability or appreciation calculations. 

**Restricting Scope to Top 100 Metros**

We also described how Zillow is already sorted by SizeRank and how we retained only the top 100 metro areas along with the national average. This choice was made to improve interpretability and to reduce the noise from small, maybe less representative markets. Essentially, the rationale behind only retaining the largest 100 metro areas was that our research focuses on regions where most US residents live and where affordability trends have the most impact. 

**Output and Validation**

After forward-filling, the cleaned dataframe is saved as data/processed/zillow_cleaned.csv. Next we ran examine_data() again to confirm that no null values remain, besides the expected StateName = NaN for the United States national row. This validated that the cleaned zillow dataset maintained both integrity and completeness, while remaining accurate for further integration. 

### BEA Data Quality Assessment

The BEA personal income dataset initially exhibited strong structural quality. After we converted the data from its original format (Excel) to CSV during the data acquisition phase (src/data_acquisition/bea_acquire.py), we identified that no rows or columns were lost by comparing the dataframe and shapes of both formats. This inspection was necessary to ensure that the format transfer didn't impact data integrity in any sort of manner. Additionally, we immediately tested the dataset for null values utilizing the Pandas library and idenfitied no null values in the income fields for relevant analysis. This made the data, from a quality standpoint, suitable for further integration.

However, when examining the csv dataset initally, the primary data quality issue we immediately recognized was **semantic rather than structural**. In other words, while the BEA data was complete, its metadata with regards to metropolitan identifiers (metro names: city, state formatting) differed from Zillow's naming conventions. An example of this can be seen in the data/raw datasets, in which BEA represents metropolitan regions using full metro area names (e.g. "Los Angeles-Long Beach-Anaheim, CA") rather than city-level identifiers that are used in Zillow. The reason this data quality issue is semantic, rather than structural, is due to the fact that despite these naming convention differences, both datasets are referring to the same metropolitan statistical areas. Another data quality issue revolved around the fact that BEA data is **ordered alphabetically rather than by population size**, unlike Zillow, which is conducted in a size-rank format. 

Although we had briefly touched upon these issues in the interim status report (StatusReport.md), these data quality issues were addressed and remediated after that report. To fix these semantic/sizerank issues, we implemented a detailed cleaning and alignment process that can be found in src/data_cleaning/bea_cleaning.py. While we initially thought that the most optimal way of matching the order and names of BEA and Zillow data would be through conducting a fuzzy match, after some trial and error, we identified that utilizing metropolitan identifiers by parsing and matching component attributes (city and state) for all 100 largest metropolitan areas proved much more efficient, reliable, and accurate - allowing us to maintain integrity when cleaning the BEA data's semantic and structural differences. 

To conduct this procedure, we condeucted the following steps. (1) Split the Zillow RegionName column into both city and state lists. (2) Iterate through the zillow city, state columnns, and identify if there were zero, one, or multiple matches with BEA names. A match was identified in cases where zillow city names appeared within the BEA metropolitan area string, while enforcing state-level consistency as well. This can be see through lines 61-107 of bea_cleaning.py file. When conducting this alignment, we ensured that the matches in the newly reorganized BEA dataset contained both the original metropolitan area metadata as well as the zillow city match metadata - this allowed us to easily perform a left_join via python in the integration phase while easily maintaining data completeness and integrity.

After alignment, we performed validation checks to ensure that all of Zillow's top 100 metros were handled and matched to teh corresponding BEA record. We also had to specificallly and manually handle the US national aggregate data, which didn't have a "State" name - for this special case, we explicitly filled income values for 2021-2023, as this was the easiest way to ensure data accuracy for the few US aggregate columns. 

Now that we handled the US aggregate, we conducted one final inspection of the cleaned BEA dataset to ensure (1) it was in the same sizerank order as zillow, included both the Zillow RegionName and BEA metropolitan area metadata tags for integration joins, and correctly handled exceptions such as the US aggregate data while dropping irrelevant columns to our specific analysis (metro vs non-metro comparison columns in BEA). Throughout this process, data quality was preserved via continuous monitoring of null value handling, data reordering, and semantic matching in a manner that was both efficient and optimized. 

### Integrated Dataset Quality Assessment

Following the individual dataset, we performed integration within src/data_integration/integration.py. This integration was straightforward due to our data quality and preservation efforts in the acquisition and cleaning steps of our data handling, as we simply had to combine both datasets via a dataframe merge in pandas as seen in line 22:

integrated_df = zillow_cleaned.merge(bea_cleaned, left_on="RegionName", right_on="ZillowRegionName", how="left")

We conducted a final round of data quality checks after completing the integration. These checks confirmed that all metropolitan areas were successfully integrated and that the merged dataset preserved both housing and income attributes as expected. We expected only one null value after conducting the integration (the state identifier for the US Aggregate data), and after conducting this quality check, that was the only null value that appeared. This sole null value was expected and does not affect analysis or reproducibility in any manner, showcasing that all our data quality precautions throughout acquisition, cleaning, and integration were successful. 

Overall, the data quality checks conducted iteratively across all stages confirmed that the datasets were complete, internally consistent, and accurate. This subsequently made our data suitable for downstream analysis as we proceded into data analysis, visualization, and workflow automation moving forward.

## Findings 

Through our analysis, we were able to gain many measurable insights to answer our original research questions. We investigated housing trends across U.S. metropolitan areas using integrated data from Zillow and the Bureau of Economic Analysis (BEA). 

**1. Which metros have seen the largest housing appreciations since 2000, and which markets make the most sense for real estate investment?**
We calculated the appreciation as a percent change between the earliest and latest ZHVI values for each metro, which created a long-run appreciation ranking. The top ones were overwhelming in the California and Florida metros, specifically: 
- San Jose, CA
- San Diego, CA
- Los Angeles, CA
- Riverside, CA
- Miami, FL

The metros have experienced long term value increases, sometimes exceeding 250-300% appreciation. The  rapid economic expansion , population influx and constrained supply of housing are some factors that can explain this trend. 
On the other hand, slower-growth metro areas like Chicago, Detroit and Cleveland have had significantly lower appreciation, which can mean weaker demand and stagnant economic conditions. 
When thinking about investment, although the top-appreciating metros are demonstrating historical strength, they are also very expensive and have affordability ratios that do exceed sustainable levels. The Investment Score that we also calculated revealed that not all high-appreciation metros are good current investment targets.

**2. Which housing markets are trading at a “discount,” and which appear oversaturated or overvalued?**
In order to answer this question, we calculated the Affordability Ratio to evaluate the current value relative to the local economic conditions. The lower ratios indicate that “discount” markets are more affordable relative to income, whereas higher ratios may explain that markets are overpriced. 
Most Affordable (Discount) Markets
Some of the more affordable markets included: 
- Pittsburgh, PA
- Toledo, OH
- Oklahoma City, OK
- St. Louis, MO
- Little Rock, AR

These metros have ratios from about 2-4, which means that home values remain within a reasonable multiple of the local incomes, and can also be considered undervalued relatively. 
Least Affordable (Oversaturated) Markets
Some of the more oversaturated markets included: 
- San Jose, CA
- Modesto, CA
- Stockton, CA
- Provo, UT
- Ogden, UT
  
These ratios exceed 10-12, which indicates disconnects between income and the housing cost. These metros may actually be at higher risk of corrections, if macroeconomic conditions become more rigid. 

**3. How can everyday Americans maximize their incomes to find metros with both strong affordability and long-term growth potential?**
In order to answer our third research question, we were able to calculate an Investment Score, which normalized both the appreciation and affordability metrics, giving them equal weights (0.5). This helped us create a balance between historic price appreciation and current affordability from the 2 datasets. 
Top Investment Score Metros
The top Investment Score metros included:
- Miami, FL
- Syracuse, NY
- Tampa, FL
- Buffalo, NY
- Knoxville, TN
  
These metros are ranked well here because they offer strong appreciation, reasonable affordability and sustainable fundamentals. 
This makes these metros attractive for first-time homebuyers and middle-income households who want both immediate sense of affordability and the potential to build long term wealth.

**Scatterplot Insight**

We have also included a scatterplot, visualizing appreciation against affordability and Investment Score as a color map to reveal some clusters. This revealed high-priced coastal metros scored lower because affordability was too constrained. Also, low appreciation Rust Belt metros scored lower. There was also a middle cluster, including Southeastern and Northeastern secondary metros that produced the optimal combination of growth and accessibility. 

**Extended Finding**

We also tried to extend our analysis by using a logistic regression to classify metros as HighGrowth or LowGrowth and through this we achieved approximately 86% test accuracy, balanced precision and recall, and an interpretable confusion matrix. 
Some of the key predictors included home value levels, income levels and affordability ratios. This shows us the housing market growth patterns are systematic and predictable, not just random. So Americans can use simple economic indicators like income, home value trends and affordability to make better informed decisions on where to buy. 

## Future Work

In this project, we successfully integrated two large public datasets to evaluate long-run housing appreciation, affordability and investment potential across 100 top US metropolitan areas. The analysis did provide strong insights into the data, but we also learned some lessons about the process that provide us with future improvements and extension.

One lesson that we learned was related to data acquisition and automation. Our workflow does include scripts for acquiring and cleaning both Zillow and BEA data, but our current version downloads fixed snapshots of the datasets. Naturally, the next step here would be to convert the scripts into parameterized modules so that it can automatically pull the most recent monthly ZHVI updates and annual BEA income reports, to stay truly up to date. An automated scheduling pipeline, would help make the project a continual tool that can adapt to the market data. We would also combine this with Snakemake workflow to allow the future versions of the analysis to re-run end to end as well. 

Additionally, another area for future improvement deal with more complex data integration. Our current dataset aligns with the metros across the sources using region names, which can have a level of ambiguity or mismatches attached with it due to naming inconsistencies. In order to approach this more robustly, we would map each metro to their unique geographic identifiers, also known as the CBSA codes, which would better incorporate with other data that can further develop our understanding of how demographic and economic factors affect appreciation. Also, we can add data about rental prices, building permits, inventory level and migration to create an even more holistic model.

Furthermore, we can also extend our predictive modeling component. Our logistic classification model for this did perform well with about 86% accuracy, but it did also rely on a small feature set. In the future, we can consider additional models like Random Forests, Gradient Boosted Trees or even neural networks to better understand nonlinear relationships that drive market growth. We can also improve generalization across different economic cycles by adding more indicators such as interest rates, inflation and unemployment. 
We also have opportunities to expand in the investment scoring analysis that we conducted. THe current score does weigh both appreciation and affordability equally, but it is also important to realize that different buyers, investors and policymakers all have different views about these components. In the future, we can develop more customized scoring for profiles that may need emphasis on affordability over appreciation. Another very important metric to consider is risk, which can include volatility of appreciation, what the changes of housing crashes are and these would allow the Investment Score metric to also include the downside risk. 

Finally, we also want to improve the reproducibility and user accessibility of the project as a future consideration. Although the repository already includes thorough documentation and a working analysis pipeline, we would like to create a web dashboard that would allow users to actually explore affordability and appreciation trends for these US metro areas more interactively. The utility and reach of the analysis would be deepened through a reproducible software tool and if the results show consistent, valuable performance, this would also be a consumer-friendly platform for Americans making these decisions, provided the right data ethics and handling is still utilized. 

Overall, this project did create a strong foundational understanding in the intersection of housing appreciation, income and affordability. In the future there are a lot of possibilities to expand this foundation in a multitude of ways. 


## Reproducing

In this section, we provide a complete set of instructions for anyone to reproduce the results from start to finish of our project. Our workflow has data acquisition scripts, cleaning scripts, integration and final analysis scripts. 

**1. Clone the Repository**

Step 1: It is required to clone the repository and the code below can help you do just that. 
```
git clone https://github.com/<your-github>/IS477-CourseProject-AtharvDhwani.git
cd IS477-CourseProject-AtharvDhwani
```
**2. Create and Activate a Python Environment**

Step 2: You need to create an activate a Python environment and for that we recommend using conda:
```
conda create -n housing python=3.10
conda activate housing
pip install -r requirements.txt
```
This essentially installs all required packages, including NumPy, Pandas, Matplotlib, and scikit-learn.

**3. Download Required Input Data from Box**

Step 3: Due to the fact that some data files cannot be redistributed through GitHub due to restrictions, all the required input files and all output visualizations from our pipeline are stored in the following Box folder:

BOX LINK HERE: https://uofi.box.com/s/y45nblwcwhqjb1leidqyezjgxqw18ori

Inside this Box folder you will find:
```
input_data/
zillow_raw.csv
bea_income_raw.csv
output_data/
integrated_dataset.csv (final merged dataset used in analysis)
All generated figures (PNG)
Intermediate cleaned datasets
Where to place the Box files locally
```
After downloading the Box folder:

Withing the project root, create a data folder, that has 3 other folders within it: raw, processed, and integrated. In the raw file, place the Zillow & BEA raw files. In the processed folder place the cleaned data files. In the integrated folder, place the "integrated_dataset.csv". Also all the output visuals and csv files should be stored in analysis/output path folder. In the analysis folder itself, you should put the analysis.py script.

Your folder structure should match the layout already shown in the repository itself.

**4. Run the Full Analysis Pipeline**

Step 4: The final analysis script is placed in:
```analysis/analysis.py```

In order to  run it:
```python analysis/analysis.py```

This will do multiple actions, including, loading the integrated dataset, computing appreciation percentages, computing affordability ratios, ranking metros by affordability and appreciation, computing the investment score, running the logistic classification model, printing out evaluation metrics, generating all figures. 

**5. Run Individual Workflow Steps**

Step 5: Additionally, you can also replicate the workflow if you would like with the following steps: 
```
src/data_acquisition/bea_acquire.py
src/data_acquisition/zillow_acquire.py
src/data_cleaning/bea_cleaning.py
src/data_cleaning/zillow_cleaning.py
src/data_integration/integration.py
analysis/analysis.py
```

Each of these scripts does have comments about the inputs and outputs. 

**6. Software Dependencies**

Step 6: In order to create the same environment, you can use the dependencies listed out in:
```requirements.txt```

**7. Licenses and Terms of Use**

Step 7: Everyone must abide by the terms of use and licenses. 

For the Zillow ZHVI data, public, non-commercial academic use is allowed and redistribution of the raw files is not allowed. For the BEA Income Data, it is federal open data, so redistribution is allowed with attribution. Finally, our processed dataset is stored in Box and not GitHub to comply with Zillow’s restrictions. 


## References 

* Zillow Research Data: https://www.zillow.com/research/data/
* U.S. Bureau of Economic Analysis (BEA): https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas
* Project Libraries Used: requirements.txt 
