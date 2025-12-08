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
unadjusted_bea = unadjusted_bea.rename(columns={unadjusted_bea.columns[0]: "RegionName"})

# create a list of cities in the zillow_cleaned data to compare against the BEA data
zillow_cities = zillow_cleaned["RegionName"].tolist()
# this check indicates that zillow_cities exists as a list of stirngs in an array
#print(zillow_cities)
# create a similar list for BEA cities 
bea_cities = unadjusted_bea["RegionName"].tolist()
# check if bea_cities exists as a list of string as well
print(bea_cities)
# iterate through these cities 
'''
BEA cities are formatted in the same way as zillow cities in terms of "City, State", however, 
they use full metropolitan area names rather than just city names. For example, if Zillow uses
"Los Angeles, CA" to represent the LA metro area, BEA uses "Los Angeles-Long Beach-Anaheim, CA".
Thus, it wouldn't make sense to do a fuzzy match, but rather to see if the zillow city name exists
WITHIN the BEA metropolitan area name. To ensure cities like Portland, OR and Portland, ME aren't being mixed up,
we can check if the zillow city name exists within the BEA metropolitan area name, and if the states match as well. 
'''

# split bea regionname into city and state
bea_split = unadjusted_bea["RegionName"].str.split(",", n=1, expand=True)
unadjusted_bea["BEA_Metro"] = bea_split[0].str.strip()
unadjusted_bea["BEA_State"] = bea_split[1].str.strip()

# split zillow regionname in a similar way
z_split = zillow_cleaned["RegionName"].str.split(",", n=1, expand=True)
zillow_cleaned["Zillow_City"] = z_split[0].str.strip()
zillow_cleaned["Zillow_State"] = z_split[1].str.strip()

# create an empty list to store the matched bea cities
matched_bea = []

# iterate through the zillow cities and find if they exist in bea metro 
for i, row in zillow_cleaned.iterrows():
    z_city = row["Zillow_City"]
    z_state = row["Zillow_State"]

    # identify BEA metros with the same state and where the zillow city name exists within the BEA metro name
    # This handles cases like "Los Angeles, CA" matching "Los Angeles-Long Beach-Anaheim, CA"
    matches = (unadjusted_bea["BEA_State"].str.contains(z_state, regex=False)) & (unadjusted_bea["BEA_Metro"].str.contains(z_city, regex=False))
    
    # count the number of matches (matches.sum() counts True values in boolean Series)
    num_matches = matches.sum()

    # exception for the united states
    if z_city == "United States":
        matched_bea.append({
            "ZillowRegionName": row["RegionName"],
            "BEARegionName": "United States",
            "SizeRank": row["SizeRank"]
        })
    else:
        # if not the united states, continue with the matching process
        pass
    
    # if exactly one match, append it
    if num_matches == 1:
        matched_bea.append({
            "ZillowRegionName": row["RegionName"],
            "BEARegionName": unadjusted_bea.loc[matches.idxmax(), "RegionName"],
            "SizeRank": row["SizeRank"]
        })
    elif num_matches > 1:
        # if multiple matches, print a warning and use the first one
        #print(z_city, z_state)
        matched_bea.append({
            "ZillowRegionName": row["RegionName"],
            "BEARegionName": unadjusted_bea.loc[matches.idxmax(), "RegionName"],
            "SizeRank": row["SizeRank"]
        })
    else:
        # else, we still append and can drop it later 
        # we should print a warning in case this happens
        #print(z_city, z_state)
        matched_bea.append({
            "ZillowRegionName": row["RegionName"],
            "BEARegionName": "No Match",
            "SizeRank": row["SizeRank"]
        })

# remove edge case of united states "no match"
matched_bea = [item for item in matched_bea if item["BEARegionName"] != "No Match"]
# converted the matched_bea from a list to a dataframe
df_matches = pd.DataFrame(matched_bea)
print(df_matches)

# see which of these cities are perfectly matched, have multiple matches, or no matches
perfect_matches = df_matches[df_matches["BEARegionName"] == df_matches["ZillowRegionName"]]
multiple_matches = df_matches[df_matches["BEARegionName"] != df_matches["ZillowRegionName"]]
no_matches = df_matches[df_matches["BEARegionName"] == "No Match"]

#print(f"Number of perfect matches: {len(perfect_matches)}")
#print(f"Number of multiple matches: {len(multiple_matches)}")
#print(f"Number of no matches: {len(no_matches)}")



# when we include both perfect matches and multiple matches, every city/metro area is matched in the csv
# thus, we have conducted a successful match 
# now, we must "stitch" the information in the bea dataset back with the relevant city that is matched to it

# conduct a simple merge to ensure the new cleaned df is both sizeranked, correlates with zillow, and includes all relevant BEA data 
# this will make integratin very very easy
# this includes 2021, 2022, 2023, % change in income (2022-2023), and income rank in US (from BEA data)
# this can all be appended to the df_matches df

# conduct the merge by ensuring column names are same
bea_for_merge = unadjusted_bea.rename(columns={"RegionName": "BEARegionName"})

# conduct the merge
bea_merged = df_matches.merge(
    bea_for_merge,
    on="BEARegionName",
    how="left"
)

bea_ordered = bea_merged.sort_values("SizeRank").reset_index(drop=True)
# conduct some last minute cleaning manually to fix the column names during the merge
# drop repeating columns: BEA_Metro, BEA_State, rank percetage change in US
bea_ordered = bea_ordered.drop(columns=["BEA_Metro", "BEA_State"])
bea_ordered = bea_ordered.drop(columns=["--.1"], errors="ignore")

# there are currently irrelevant "Metropolitan portion" values in the column headers, this needs to be renamed to actual column names
# to do this, we will first rename the columns 
bea_ordered = bea_ordered.rename(columns={
    "66,663": "2021",
    "68,517": "2022",
    "72,275": "2023",
    "2.8": "% change (2021-2022)",
    "5.5": "% change (2022-2023)",
    "--": "Income Rank in US"
})

# now that we have columns renamed, we need to fill the null values for the US as well with the original values from teh BEA_PersonalIncome_Data_converted.csv file
# this can be done manually since its only a few rows
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "2021"] = 64460
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "2022"] = 66244
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "2023"] = 69810
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "% change (2021-2022)"] = 2.8
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "% change (2022-2023)"] = 5.4
bea_ordered.loc[bea_ordered["ZillowRegionName"] == "United States", "Income Rank in US"] = "--"

# save the dataframe to a csv in the data/processed folder
bea_ordered.to_csv(Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "bea_cleaned.csv", index=False)

# bea_cleaned.csv is now effectively reordered, cleaned, and complete
# dhwani and I have run a sanity check to ensure all values match the original BEA data that can be found in the data/raw/BEA_PersonalIncome_Data_converted.csv file
# now that we have this file, we have effectively completed the heavy lifting of the integration process

