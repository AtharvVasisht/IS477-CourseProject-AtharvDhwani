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

# first, we need to rename the BEA columns to match zillow_cleaned data in case we want to merge them 
unadjused_bea = unadjusted_bea.rename(columns={unadjusted_bea.columns[0]: "RegionName"})

# create a list of cities in the zillow_cleaned data to compare against the BEA data
zillow_cities = zillow_cleaned["RegionName"].tolist()

# this check indicates that zillow_cities exists as a list of stirngs in an array
print(zillow_cities)

# now, we need to iterate through the BEA region name column and find the closest fuzzy
# match between city name and our zillow_cities list
# bea cities use a similar format of "City, State" to zillow, so fuzzy matching will
# be enough

# create empty list to store the matched BEA cities
matched_bea = []

# iterate through bea citeis and find the closest fuzzy match
for city in unadjusted_bea["RegionName"]:
    # conduct a fuzzy match
    matched_city = process.extractOne(city, zillow_cities, scorer = fuzz.ratio)

    # create a similarity score threshold of 80% to filter out any matches that are clearly incorrect (e.g. Portland, OR vs Portland, ME)
    


