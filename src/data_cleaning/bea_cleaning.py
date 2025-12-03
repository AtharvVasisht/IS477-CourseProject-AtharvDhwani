''' The BEA data which was originally downloaded as an excel file, was already converted to a csv file in the 
acquisition part of our project. When examining the csv converted file, we already identified that there were
no null values present in the data - in other words, the data is already clean. This script will do a few things: it will first 
organize this csv into sizerank to match the zillow data (based on Zillow's 2024 metropolitan area size rankings), and then it will be stored as a cleaned csv to the data/processed folder.
'''

# imports (added to requirements.txt)
import pandas as pd
import numpy as np
from pathlib import Path
import sys 
from fuzzywuzzy import process, fuzz

# Load bea_csv from raw/BEA_PersonalIncome_Data_converted.csv
bea_csv = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "BEA_PersonalIncome_Data_converted.csv"
unadjusted_bea = pd.read_csv(bea_csv, skiprows = 5) # skipping the unnecessary header rows at the top of the file

# Load zillow_cleaned data to match cities
zillow_cleaned_path = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "zillow_cleaned.csv"
zillow_cleaned = pd.read_csv(zillow_cleaned_path)

# we must standardize column names to make sure there's no breakge in our organization function below
unadjusted_bea.columns = unadjusted_bea.columns.str.strip()
zillow_cleaned.columns = zillow_cleaned.columns.str.strip()

# utilize the zillow_cleaned data to organize the bea into only necessary cities by size rank
def organize_bea(unadjusted_bea, zillow_cleaned):
    # we first need to store the zillow_cleaned and get the cities within "RegionName" column into a list to iterate through
    zillow_cities = zillow_cleaned["RegionName"].tolist()

    # now, we need to iterate through the zillow_cities list and find the closest fuzzy match between the city name and the unadjusted_bea["RegionName"] column
    # BEA uses a similar "City, State" format as Zillow, so we don't need to worry about splitting the city and state names apart and can just focus on finding approximate matches
    # logic for reorganizing the bea data to match the zillow data: 
    # itereate through zillow_data

    '''
    # now we need to temporarily split the unadjusted_bea into city and state (right now the format is "City, State")
    unadjusted_bea["City"] = unadjusted_bea["RegionName"].str.split(",").str[0]
    unadjusted_bea["State"] = unadjusted_bea["RegionName"].str.split(",").str[1]

    # now that we have adjusted the format to allow for easier matches, we need to conduct an approximate match between zillow_cities and unadjusted_bea["City"]
    # utilize fuzzy matching to find the closest match between city names
    # utilize levenshtein distance to find closest match as discussed in class
    matched_bea_cities = []
    
    for city in zillow_cities:
        closest_match = process.extractOne(city, unadjusted_bea["City"], scorer=fuzz.ratio)
        if closest_match and closest_match[1] > 80:  # threshold of 80% similarity
            matched_bea_cities.append(closest_match[0])
    
    # now we need to filter the unadjusted_bea dataframe to only include the cities that are in the matched_bea_cities list
    adjusted_bea = unadjusted_bea[unadjusted_bea["City"].isin(matched_bea_cities)].copy()
    '''
    return adjusted_bea

# execute this function and store the result into bea_df
bea_df = organize_bea(unadjusted_bea, zillow_cleaned)

# Before we save the data, we need to examine the data and check for null values
# this is the same function we used in the zillow cleaning script
def examine_data(df):
    print(f"shape: {df.shape}")
    print(f"cols:{df.columns}")
    print(f"dtypes: {df.dtypes}")
    print(f"null vals: {df.isnull().sum()}")
    print(f"number of null values: {df.isnull().sum().sum()}")

# utilize the examine_data function to double check for null values in this data
examine_data(bea_df)

# save the csv to the data/processed directory within this project
bea_df.to_csv(Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "bea_cleaned.csv", index=False)

