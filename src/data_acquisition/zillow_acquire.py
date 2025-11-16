''' The Zillow data was originally downloaded from the Zillow website directily as a csv file.
Therefore, we do not need to compare any format changes but must load the data proper to ensure for cleaning moving forward.
'''

# imports (added to requirements.txt)
import pandas as pd
import numpy as np
from pathlib import Path

# Step 1: Define and Load files from the data/raw folder
csv_file = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "Zillow_Housing_Data.csv"
# only consider top 100 metros by population (first 100 rows) to streamline analysis and reduce computational complexity
zillow_df = pd.read_csv(csv_file).head(102) # the 1st row is the header, and the 2nd row is the United States as a whole, so we need to add 1 to the head count

print("Zillow data loaded successfully")
print(f"The shape of the Zillow data is {zillow_df.shape}")
print(f"The columns of the Zillow data are {zillow_df.columns}")

# zillow data is successfully loaded and can now be cleaned in the data_cleaning folder