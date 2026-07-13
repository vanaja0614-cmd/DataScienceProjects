# Telecom Customer Churn Data Preparation & Exploratory Data Analysis

## Project Objective

The objective of this project is to prepare the Telecom Customer Churn dataset for machine learning by performing data cleaning, feature engineering, and exploratory data analysis (EDA). The project aims to understand customer behavior and identify the major factors influencing customer churn.

---

## Dataset Overview

* Dataset: Telecom Customer Churn Dataset
* Records: Approximately 7,000 customers
* Features include:

  * Customer demographics
  * Internet services
  * Phone services
  * Contract information
  * Billing details
  * Customer churn status

---

## Project Workflow

### 1. Data Understanding

* Loaded the dataset using Pandas.
* Explored dataset structure using `info()` and `describe()`.
* Checked data types and missing values.
* Identified blank spaces and inconsistent values.

### 2. Data Cleaning

* Replaced blank values with NaN.
* Converted `TotalCharges` to numeric format.
* Removed or handled missing values.
* Verified data consistency.

### 3. Feature Engineering

Created several useful features:

* TenureGroup
* AvgMonthlySpend
* Binary encoding for Yes/No columns
* One-Hot Encoding for categorical variables

### 4. Exploratory Data Analysis

Performed:

* Customer churn distribution
* Contract type vs Churn
* Correlation Heatmap
* Monthly Charges vs Churn
* Additional statistical analysis

---

## Key Insights

1. Customers with month-to-month contracts have the highest churn rate.
2. Long-term customers are more likely to remain with the company.
3. Higher monthly charges are associated with increased churn.
4. Customers on two-year contracts have the lowest churn.
5. Contract type and tenure are among the strongest predictors of customer churn.

---

## Deliverables

* Cleaned dataset (`telecom_churn_cleaned.csv`)
* Jupyter Notebook
* Visualizations
* Feature-engineered dataset
* Summary report

---

## Conclusion

The dataset was successfully cleaned and transformed into a machine-learning-ready format. Exploratory analysis revealed several business insights that can help telecom companies improve customer retention and reduce churn.
