import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create outputs folder
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\n========== Dataset Information ==========\n")
print(df.info())

print("\n========== Statistical Summary ==========\n")
print(df.describe(include='all'))

# -----------------------------
# Data Cleaning
# -----------------------------

# Replace blank spaces with NaN
df.replace(" ", np.nan, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Remove missing values
df.dropna(inplace=True)

# -----------------------------
# Feature Engineering
# -----------------------------

# Create TenureGroup
bins = [0, 12, 24, 36, 48, 60, 72]
labels = ["0-12", "13-24", "25-36", "37-48", "49-60", "61-72"]

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Average Monthly Spend
df["AvgMonthlySpend"] = df["TotalCharges"] / df["tenure"]

# Avoid division by zero
df["AvgMonthlySpend"] = df["AvgMonthlySpend"].replace([np.inf, -np.inf], np.nan)
df["AvgMonthlySpend"] = df["AvgMonthlySpend"].fillna(df["MonthlyCharges"])

# Binary Encoding
binary_columns = [
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
    "Churn"
]

for col in binary_columns:
    if col in df.columns:
        df[col] = df[col].map({"Yes": 1, "No": 0})

# One-Hot Encoding
categorical_columns = ["Contract", "InternetService"]

existing_columns = [c for c in categorical_columns if c in df.columns]

df = pd.get_dummies(
    df,
    columns=existing_columns,
    drop_first=True
)

# -----------------------------
# Correlation
# -----------------------------
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# -----------------------------
# Countplot
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Count")
plt.tight_layout()
plt.savefig("outputs/churn_countplot.png")
plt.close()

# -----------------------------
# Contract vs Churn
# -----------------------------
contract_columns = [c for c in df.columns if c.startswith("Contract_")]

if contract_columns:
    contract = contract_columns[0]

    plt.figure(figsize=(6, 4))
    sns.barplot(x=contract, y="Churn", data=df)
    plt.title("Contract vs Churn")
    plt.tight_layout()
    plt.savefig("outputs/contract_vs_churn.png")
    plt.close()

# -----------------------------
# Monthly Charges Boxplot
# -----------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges by Churn")
plt.tight_layout()
plt.savefig("outputs/monthlycharges_boxplot.png")
plt.close()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("cleaned_telecom_churn.csv", index=False)

print("\n======================================")
print("Project Completed Successfully!")
print("======================================")

print("\nGenerated Files:")
print("1. cleaned_telecom_churn.csv")
print("2. outputs/churn_countplot.png")
print("3. outputs/contract_vs_churn.png")
print("4. outputs/correlation_heatmap.png")
print("5. outputs/monthlycharges_boxplot.png")