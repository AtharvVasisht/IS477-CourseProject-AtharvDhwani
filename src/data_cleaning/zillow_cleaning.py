''' The goal of this script is to clean the zillow data after it has been acquired in the zillow_acquire.py script.
Cleaning the data will include examining the existing data, cleaning null values, and saving th cleaned data to the data/processed folder.
'''

# imports (added to requirements.txt)
import pandas as pd
import numpy as np
from pathlib import Path
import sys 
import scipy.stats as stats

# Load zillow_df from zillow_acquire.py
# Add the data acquisition directory to the path to allow importing zillow_acquire
sys.path.append(str(Path(__file__).resolve().parent.parent / "data_acquisition"))
import zillow_acquire

zillow_df = zillow_acquire.zillow_df

# Before we conduct the cleaning process, we need to examine the data and check for null values
def examine_data(df):
    print(f"shape: {df.shape}")
    print(f"cols:{df.columns}")
    print(f"dtypes: {df.dtypes}")
    print(f"null vals: {df.isnull().sum()}")
    print(f"number of null values: {df.isnull().sum().sum()}")

# execute function
examine_data(zillow_df)

# many cities have null values for home values at certain months, due to the fact that Zillow may not have collected data for those months.
# we need to fill these null values in for proper analysis moving forward.
''' 
The Zillow data is structured in the following way:
1. each row represents a city that is identified by the RegionName column
2. the metadata columns are RegionID, SizeRank (how big city is), RegionType (type of city), and StateName
3. date columns are all formatteed in YYYY-MM-DD format and represents the home value for that city at the end of the specific month 

Filling null values will require us to iterate through the time-series columns for each city, identify cities and their months 
with missing vlaues, and fill them in based on the first valid index of the column series. 
'''

def fill_null(zillow_df):
    # Get all the date columns in the dataframe
    # check if the date columns are in the correct format and contain '-' and if so ensure they are in the correct order
    date_cols_sorted = [col for col in zillow_df.columns if isinstance(col, str) and '-' in col]

    # For each row in the dataframe
    for idx in zillow_df.index:
        # Get the price series for this row
        price_data = zillow_df.loc[idx, date_cols_sorted]
        
        # Find the first valid index that isnt a null value
        first_valid_idx = price_data.first_valid_index()
        
        if first_valid_idx is not None:
            # Get the numeric index of the first valid column
            first_valid_col_idx = date_cols_sorted.index(first_valid_idx)
            
            # Forward fill all values before the first valid index
            if first_valid_col_idx > 0:
                zillow_df.loc[idx, date_cols_sorted[:first_valid_col_idx]] = price_data[first_valid_idx]
            
            # Forward fill any remaining NaN values using ffill()
            zillow_df.loc[idx, date_cols_sorted] = zillow_df.loc[idx, date_cols_sorted].ffill()
    
    return zillow_df

# execute function
cleaned_zillow = fill_null(zillow_df)

# save as csv in proper directory
cleaned_zillow.to_csv(Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "zillow_cleaned.csv", index=False)

# examine the cleaned data utilizing the same examine_data function from above
examine_data(cleaned_zillow)

''' The data is completely clean and there are no null values remaining - the only technical null value 
that exists is the "Statname" column for the United States as a whole. This null value makes sense 
and will not disrupt our analysis as the United States is the national average and thus will not have 
a state name associated with it.
'''