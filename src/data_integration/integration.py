'''
The goal of this script is to integrate both the zillow_cleaned.csv and bea_cleaned.csv into one single dataframe and csv. 
Although we will not always be using the integrated dataset (sometimes, we many solely analyze the zillow data, and sometimes only the BEA data),
an integrated dataset will be helpful when trying to find patters or correlations between the two datasets. Because we already utilized matching
with the Zillow dataset in the bea_cleaning.py script, we can utilize a simple merge on the Zillow region name column in both zillow_cleaned.csv
and bea_cleaned.csv to create the single integrated dataset. We can then save this integrated dataset to data/integrated/integrated_dataset.csv
'''

# imports (added to requirements.txt)
import pandas as pd
import numpy as np
from pathlib import Path
import sys 

# load zillow_cleaned.csv and bea_cleaned.csv
zillow_cleaned_path = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "zillow_cleaned.csv"
bea_cleaned_path = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "bea_cleaned.csv"
zillow_cleaned = pd.read_csv(zillow_cleaned_path)
bea_cleaned = pd.read_csv(bea_cleaned_path)

# integrate the two datasets by mergining the zillow region name in both dataframes
integrated_df = zillow_cleaned.merge(bea_cleaned, left_on="RegionName", right_on="ZillowRegionName", how="left")

# drop the redundant column: ZillowRegionName
integrated_df = integrated_df.drop(columns=["ZillowRegionName"])

# save the integrated dataframe to a csv in the data/integrated folder
integrated_df.to_csv(Path(__file__).resolve().parent.parent.parent / "data" / "integrated" / "integrated_dataset.csv", index=False)

# check for shape and null values
print(integrated_df.shape)
print(integrated_df.isnull().sum())
# find what the null value is
print(integrated_df[integrated_df.isnull().any(axis=1)])

# there is only one null value, but this isn't even a real null value as it is the United States national average (which doesn't have a state name - therefore a NaN) - this is expected and will not disrupt anything in our analysis
# therefore, the integration is now complete - although we may not use this dataset for ALL our analysis, it will be useful when identifying patterns and correlations
# the integrated dataset is in the data/integrated folder and has the BEA data after the Zillow data at the end of the dataframe

