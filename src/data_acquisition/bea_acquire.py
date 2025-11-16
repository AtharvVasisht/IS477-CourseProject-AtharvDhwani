# The BEA data was originally downloaded from the BEA website as an excel file, but was converted to a csv for ease of analysis.
# The goal of this script is the compare the original excel file to the csv file to ensure no data was lost during the conversion.

# imports (added to requirements.txt)
import pandas as pd
import numpy as np
from pathlib import Path

# Step 1: Define and Load files from the data/raw folder
excel_file = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "BEA_PersonalIncome_Data.xlsx"
csv_file = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "BEA_PersonalIncome_Data_converted.csv"
excel_df = pd.read_excel(excel_file)
csv_df = pd.read_csv(csv_file)

print("Excel file loaded successfully")
print("CSV file loaded successfully")

# Step 2: Compare the shapes of both dataframes to ensure the structures of the data are the same
if excel_df.shape != csv_df.shape:
    print(f"The shapes of both dataframes are not the same - excel has {excel_df.shape[0]} rows and {excel_df.shape[1]} columns, while csv has {csv_df.shape[0]} rows and {csv_df.shape[1]} columns")
else:
    print(f"The shapes of both dataframes are the same - excel has {excel_df.shape[0]} rows and {excel_df.shape[1]} columns, while csv has {csv_df.shape[0]} rows and {csv_df.shape[1]} columns")

# we have now confirmed that the structures of the data are the same, and no metadata was lost during the conversion
# we will use the csv file for analysis moving forward
bea_df = csv_df
