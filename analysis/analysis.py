import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)
from pathlib import Path

# Get the project root directory (one level up from analysis/)
project_root = Path(__file__).parent.parent
df = pd.read_csv(project_root / "data" / "integrated" / "integrated_dataset.csv")

# BEA numeric columns
for column in ["2021", "2022", "2023"]:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .replace({"--": np.nan})
            .astype(float)
        )


# Date columns from Zillow dataset
date_columns = [c for c in df.columns if len(c) >= 4 and c[:4].isdigit()]
date_columns_sort = sorted(date_columns)

early_column= date_columns_sort[0]      # earliest monthly ZHVI 
recent_column= date_columns_sort[-1]       # most recent ZHVI

# Latest ZHVI 
df["LatestZHVI"] = df[recent_column]

# Appreciation formula
df["appreciation_percentage"] = (df[recent_column] - df[early_column]) / df[early_column] * 100

# SizeRank_x to SizeRank
# Ignore SizeRank_y
if "SizeRank_x" in df.columns:
    df["SizeRank"] = df["SizeRank_x"]

# Drop USA aggregate row 
df = df[df["SizeRank"] > 0].copy()

# Affordability Ratio formula
df["AffordabilityRatio"] = df["LatestZHVI"] / df["2023"]


# Appreciation Analysis using the Appreciation Percentage 

#  Top and bottom appreciating metro areas function

def appreciation_ranking(df):
    columns = ["RegionName", "StateName", "appreciation_percentage", "LatestZHVI"]
    rank_appreciation = df[columns].sort_values("appreciation_percentage", ascending=False)
    top_ranked_appreciation = rank_appreciation.head(10).reset_index(drop=True)
    bottom_ranked_appreciation = rank_appreciation.tail(10).reset_index(drop=True)
    return top_ranked_appreciation, bottom_ranked_appreciation

top_appreciation, bottom_appreciation = appreciation_ranking(df)
top_appreciation.to_csv("analysis/output/top10_appreciation.csv", index=False)
bottom_appreciation.to_csv("analysis/output/bottom10_appreciation.csv", index=False)

#printing the output for analysis 
print("Top 10 Metro Areas by Appreciation Percent")
print(top_appreciation)

print("\n")
print("Bottom 10 Metro Areas by Appreciation Percent")
print(bottom_appreciation)

# Affordability Analysis using the Affordability Ratio

# Affordability Ranking Function - ranks the metro areas by top and bottom affordability using the affordability ratio
def affordability_ranking(df):
    columns = ["RegionName", "StateName", "LatestZHVI", "2023", "AffordabilityRatio"]
    ranking_affordability = df[columns].sort_values("AffordabilityRatio", ascending=True)
    top_ranking_metros = ranking_affordability.head(10).copy()    # most affordable
    bottom_ranking_metros = ranking_affordability.tail(10).copy()  # least affordable

    # Metro column
    top_ranking_metros["Metro"] = top_ranking_metros["RegionName"] + ", " + top_ranking_metros["StateName"]
    bottom_ranking_metros["Metro"] = (bottom_ranking_metros["RegionName"] + ", " + bottom_ranking_metros["StateName"])
    return top_ranking_metros, bottom_ranking_metros

top_affordability_metro, bottom_affordability_metro = affordability_ranking(df)
top_affordability_metro.to_csv("analysis/output/top10_affordability.csv", index=False)
bottom_affordability_metro.to_csv("analysis/output/bottom10_affordability.csv", index=False)

#printing the output for analysis 
print("\n")
print("Top 10 Most Affordable Metros")
print(top_affordability_metro[["Metro", "LatestZHVI", "2023", "AffordabilityRatio"]])

print("\n")
print("Top 10 Least Affordable Metros")
print(bottom_affordability_metro[["Metro", "LatestZHVI", "2023", "AffordabilityRatio"]])


# Visuals for Affordability - using a bar plot to visualize the 10 top and bottom metro areas based on affordability from the ratio calculated earlier

def affordability_plot(top_affordability, bottom_affordability):

    # Most Affordable (10)
    plt.figure(figsize=(11, 6))
    plt.barh(top_affordability["Metro"], top_affordability["AffordabilityRatio"])
    plt.xlabel("Affordability Ratio")
    plt.title("Top 10 Most Affordable Metros")
    plt.gca().invert_yaxis() #highest at the top
    #plt.savefig("analysis/output/top10_most_affordable.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Least Affordable (10)
    plt.figure(figsize=(11, 6))
    plt.barh(bottom_affordability["Metro"], bottom_affordability["AffordabilityRatio"])
    plt.xlabel("Affordability Ratio")
    plt.title("Top 10 Least Affordable Metros")
    plt.gca().invert_yaxis() #lowest at the top
    plt.savefig("analysis/output/top10_least_affordable.png", dpi=300, bbox_inches="tight")
    plt.show()

#plots the affordability metros, both top 10 and bottom 10 
affordability_plot(top_affordability_metro, bottom_affordability_metro)



# Investment Score
# Uses both appreication and affordability (normalizes it before)

# Investment score function 
def investment_score(df):

    # Normalize the long run appreciation percentage
    min, max = df["appreciation_percentage"].min(), df["appreciation_percentage"].max()
    df["AppreciationNorm"] = (df["appreciation_percentage"] - min) / (max - min)

    # Normalize the affordability ratio
    minimum_ratio, maximum_ratio = df["AffordabilityRatio"].min(), df["AffordabilityRatio"].max()
    df["AffordabilityNorm"] = (
        maximum_ratio - df["AffordabilityRatio"]) / (maximum_ratio - minimum_ratio)

    # Put equal weight on both appreication and affordability (can be changed depending on analysis needs, but chose 50% to incorporate both metrics)
    df["InvestmentScore"] = 0.5*df["AppreciationNorm"] + 0.5*df["AffordabilityNorm"]
    return df


df_invest = investment_score(df)

# Ranking by the calculated investment score 
investment_rank = df_invest.sort_values("InvestmentScore", ascending=False)
investment_rank.to_csv("analysis/output/investment_score_ranking.csv", index=False)

print("\nTop 10 Metros by Investment Score")
print(
    investment_rank[
        ["RegionName","StateName","appreciation_percentage","AffordabilityRatio","InvestmentScore",]].head(10)
)


# Visual for Investment Score - Uses 3 dimensions (affordabiility, appreciation & investment) to answer research question 

def investment_plot(df_invest):
    # Use colormap for Investment Score and plot appreciation vs affordability 
    plt.figure(figsize=(12, 7))
    scatter = plt.scatter(
        df_invest["appreciation_percentage"],
        df_invest["AffordabilityRatio"],
        c=df_invest["InvestmentScore"],
    )
    plt.xlabel("Appreciation Percent")
    plt.ylabel("Affordability Ratio")
    plt.title("Metros by Appreciation, Affordability, & Investment Score")
    cbar = plt.colorbar(scatter)
    cbar.set_label("Investment Score")
    plt.savefig("analysis/output/investment_scatter.png", dpi=300, bbox_inches="tight")
    plt.show()

investment_plot(df_invest)


# Classification Model 
# Uses binary labels of 1 for HighGrowth and 0 for LowGrowth metros 

def run_classification(classification_df):

    # Binary, 1 is above-median appreciation and 0 is below-median
    median = classification_df["appreciation_percentage"].median()
    classification_df["HighGrowth"] = (classification_df["appreciation_percentage"] >= median).astype(int)

    # Features
    feature_cols = ["SizeRank","LatestZHVI","2021","2022","2023","AffordabilityRatio",]

    X = classification_df[feature_cols].astype(float)
    y = classification_df["HighGrowth"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=40, stratify=y
    )

    classification_model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("logreg", LogisticRegression(max_iter=1000)),
        ]
    )

# Fit model to train data and predict model on test data 
    classification_model.fit(X_train, y_train)
    y_pred = classification_model.predict(X_test)


# Calculating various metrics that answer research questions 

    results_text = []
    results_text.append("Classification: HighGrowth (1) vs LowGrowth (0)\n")
    results_text.append(f"Accuracy on Test Set: {accuracy_score(y_test, y_pred)}\n\n")
    results_text.append("Classification Report:\n")
    results_text.append(classification_report(y_test, y_pred))
    results_text.append("\nConfusion Matrix:\n")
    results_text.append(str(confusion_matrix(y_test, y_pred)))

    with open("analysis/output/classification_results.txt", "w") as f:
        f.writelines(results_text)

    # Still print to console
    print("".join(results_text))

   # print("\nClassification: HighGrowth (1) vs LowGrowth (0)")
    #print(f"Accuracy on Test Set: {accuracy_score(y_test, y_pred)}")
    #print("\nClassification Report:")
    #print(classification_report(y_test, y_pred))
    #print("Confusion Matrix:")
    #print(confusion_matrix(y_test, y_pred))

    return classification_model, feature_cols


classification_model, clf_features = run_classification(df_invest)

