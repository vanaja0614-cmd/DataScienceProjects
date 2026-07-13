import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# # Load Dataset
df = pd.read_csv("netflix_titles.csv")

# # print("="*50)
# print("First 5 Rows")
# print("="*50)
# print(df.head())

# print("\nDataset Shape:", df.shape)

# print("\nColumns")
# print(df.columns)
print(df.info())

print(df.describe(include="all"))

print(df.isnull().sum())

# Convert date column
df["date_added"] = pd.to_datetime(
    df["date_added"].astype(str).str.strip(),
    errors="coerce",
    format="mixed"
)

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")

print("\nMissing Values After Cleaning")
print(df.isnull().sum())
# Release Decade
df["release_decade"] = (df["release_year"] // 10) * 10

# Movie Flag
df["is_movie"] = df["type"].apply(lambda x: 1 if x == "Movie" else 0)

# Content Type
df["content_type"] = df["type"]

df.to_csv("cleaned_netflix.csv", index=False)

print("\nCleaned dataset saved successfully.")
plt.figure(figsize=(6,6))
df["type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.savefig("outputs/movie_vs_tvshow.png")
plt.close()
plt.figure(figsize=(12,6))
df["release_year"].value_counts().sort_index().plot()
plt.title("Content Released Per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.savefig("outputs/content_per_year.png")
plt.close()
genres = df["listed_in"].str.split(", ").explode()

plt.figure(figsize=(10,6))
genres.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.savefig("outputs/top_genres.png")
plt.close()
countries = df["country"].str.split(", ").explode()

plt.figure(figsize=(10,6))
countries.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("outputs/top_countries.png")
plt.close()
plt.figure(figsize=(6,4))
sns.heatmap(df[["release_year", "is_movie"]].corr(),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.close()
print("\nGenerated Files:")
print("1. cleaned_netflix.csv")
print("2. outputs/movie_vs_tvshow.png")
print("3. outputs/content_per_year.png")
print("4. outputs/top_genres.png")
print("5. outputs/top_countries.png")
print("6. outputs/correlation_heatmap.png")