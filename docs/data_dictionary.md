# Data Dictionary For The Integrated Zillow & BEA Dataset

## In Conformance with DCAT/Schema.org 

The purpose of this document is to state all specific metadata for the integrated dataset (Zillow + BEA) utilized during this project and analysis. 

## Project 
**Housing Affordability and Income Trends Across Major U.S. Metropolitan Areas**

**Creators:**
* Atharv Vasisht
* Dhwani Patel

## 1. Dataset Overview

**Name:** integrated_dataset.csv
**Path:** data/integrated/integrated_dataset.csv

**Description:** This integrated dataset combines Zillow housing data with the BEA income data, creating one unified dataset for exploratory data analysis. The provided information below is aimed at explaining all relevant metadata and coverage related to both datasets and their integration. More information regarding the integration itself can be found within relevant integration folders, status updates, and the README.md file.

**Time Horizon of Datasets:**
* Zillow ZHVI (monthly data): 2000-2025
* BEA income (annual): 2021-2023

**Geographic Coverage:** Both are for United States metropolitan statistical areas (MSAs), and the overall US national aggregate. This is represented in the integrated dataset as well.

**Data Sources:**
* Zillow Research (Zillow Home Value Index - ZHVI)
* U.S. Bureau of Economic Analysis (Per capita personal income)

## 2. Identifier Fields

### RegionID
**Description:** ID of metropolitan area in integer format

### RegionName
**Description:** Name of the metropolitan area in "City, State" format

### RegionType
**Description:** all "msa" (metropolitan area)

### StateName
**Description:** Name of state for msa area

### DateTime columns
**Description:** monthly columns from 2000-2025 for zillow data 

### BEARegionName
**Description:** Name of metropolitan area as stated in BEA data - string format

### RegionName
**Description:** Name of the metropolitan area in "City, State" format

### Sizerank
**Description:** Zillow metropolitan size rank based on population and market size.

### 2021, 2022, 2023 Columns
**Description:** Annual per capita income data by year from BEA

### "Income Rank Change Columns
**Description:** % change in income by year by metropolitan area for both date ranges