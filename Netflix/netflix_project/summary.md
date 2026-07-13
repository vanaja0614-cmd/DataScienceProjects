# Netflix Titles Dataset - Exploratory Data Analysis

## Project Objective

The purpose of this project is to analyze the Netflix Titles dataset to discover content trends, identify popular countries and genres, and understand how Netflix's content library has evolved over time.

---

## Dataset Overview

* Dataset: Netflix Titles Dataset
* Records: Approximately 9,000 titles
* Features include:

  * Movie/TV Show
  * Director
  * Cast
  * Country
  * Release Year
  * Date Added
  * Rating
  * Genre
  * Duration

---

## Project Workflow

### 1. Data Cleaning

* Converted `date_added` into datetime format.
* Filled missing values in:

  * Director
  * Cast
  * Country
* Checked for duplicate records.

### 2. Feature Engineering

Created new features:

* Release Decade
* Year Added
* Content Type
* Movie Indicator
* Top Producing Countries

### 3. Exploratory Data Analysis

Generated visualizations including:

* Movie vs TV Show distribution
* Content released per year
* Top genres
* Country-wise content distribution
* Heatmap analysis

---

## Key Insights

1. Movies represent the majority of Netflix's content library.
2. Netflix experienced significant growth after 2015.
3. The United States contributes the highest number of titles.
4. Drama and International Movies are among the most popular genres.
5. TV Shows have steadily increased over recent years.

---

## Trend Prediction

A simple trend analysis suggests continued growth in Netflix content over the next two years based on historical release patterns.

---

## Deliverables

* Cleaned dataset (`netflix_cleaned.csv`)
* Jupyter Notebook
* Multiple visualizations
* Insight report
* Trend prediction

---

## Conclusion

This project demonstrates how data cleaning, feature engineering, and visualization techniques can be used to uncover meaningful business insights from entertainment data. The analysis provides a better understanding of Netflix's global content distribution and growth patterns.
