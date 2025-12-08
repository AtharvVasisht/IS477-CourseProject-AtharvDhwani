# Snakefile

rule all:
    input:
        "data/integrated/integrated_dataset.csv",
        "analysis/output/top10_appreciation.csv",
        "analysis/output/bottom10_appreciation.csv",
        "analysis/output/top10_affordability.csv",
        "analysis/output/bottom10_affordability.csv",
        "analysis/output/investment_score_ranking.csv",
        "analysis/output/top10_most_affordable.png",
        "analysis/output/top10_least_affordable.png",
        "analysis/output/investment_scatter.png"



# 1. Acquire Zillow data

rule acquire_zillow:
    output:
        "data/raw/Zillow_Housing_Data.csv"
    shell:
        "python src/data_acquisition/zillow_acquire.py"


# 2. Acquire BEA data

rule acquire_bea:
    output:
        "data/raw/BEA_PersonalIncome_Data_converted.csv"
    shell:
        "python src/data_acquisition/bea_acquire.py"



# 3. Clean Zillow data

rule clean_zillow:
    input:
        "data/raw/Zillow_Housing_Data.csv"
    output:
        "data/processed/zillow_cleaned.csv"
    shell:
        "python src/data_cleaning/zillow_cleaning.py"



# 4. Clean BEA data

rule clean_bea:
    input:
        "data/raw/BEA_PersonalIncome_Data_converted.csv"
    output:
        "data/processed/bea_cleaned.csv"
    shell:
        "python src/data_cleaning/bea_cleaning.py"



# 5. Integrate cleaned Zillow + BEA

rule integrate:
    input:
        zillow="data/processed/zillow_cleaned.csv",
        bea="data/processed/bea_cleaned.csv"
    output:
        "data/integrated/integrated_dataset.csv"
    shell:
        "python src/data_integration/integration.py"



# 6. Run final analysis (tables, plots, ML)

rule analysis:
    input:
        "data/integrated/integrated_dataset.csv"
    output:
        "results/analysis_log.txt"
    shell:
        "python analysis/analysis.py > {output}"


rule run_analysis:
    input:
        "data/integrated/integrated_dataset.csv"
    output:
        "analysis/output/top10_appreciation.csv",
        "analysis/output/bottom10_appreciation.csv",
        "analysis/output/top10_affordability.csv",
        "analysis/output/bottom10_affordability.csv",
        "analysis/output/investment_score_ranking.csv",
        "analysis/output/top10_most_affordable.png",
        "analysis/output/top10_least_affordable.png",
        "analysis/output/investment_scatter.png"
    shell:
        "python analysis/analysis.py"


