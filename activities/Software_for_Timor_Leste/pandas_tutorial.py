import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Welcome to an Exhaustive Review of Pandas!")
print("-------------------------------------------")

# Importing the CSV file from the last lesson
print("\nImporting the CSV file:")
df = pd.read_csv("example.csv")
print(df)

# Pandas Series: creation and basic operations
print("\nPandas Series:")
print("--------------")

# Creating a Pandas Series
series = pd.Series([1, 2, 3, 4, 5])
print("Creating a Pandas Series:")
print(series)

# Accessing elements of a Series
print("\nAccessing elements of a Series:")
print("Element at index 2:", series[2])

# Basic operations on a Series
print("\nBasic operations on a Series:")
print("Addition:", series + 2)
print("Multiplication:", series * 3)
print("Exponentiation:", series ** 2)

# Pandas DataFrames: creation and basic operations
print("\nPandas DataFrames:")
print("------------------")

# Creating a Pandas DataFrame
data = {
    "Name": ["John", "Alice", "Bob", "Claire"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Tokyo"]
}
df = pd.DataFrame(data)
print("Creating a Pandas DataFrame:")
print(df)

# Accessing columns of a DataFrame
print("\nAccessing columns of a DataFrame:")
print("Name column:")
print(df["Name"])

# Accessing rows of a DataFrame using iloc
print("\nAccessing rows of a DataFrame using iloc:")
print("Row at index 1:")
print(df.iloc[1])

# Basic operations on a DataFrame
print("\nBasic operations on a DataFrame:")
print("Adding a new column:")
df["Country"] = ["USA", "UK", "France", "Japan"]
print(df)

print("Dropping a column:")
df = df.drop("City", axis=1)
print(df)

print("Filtering rows based on a condition:")
filtered_df = df[df["Age"] > 30]
print(filtered_df)

# Data analysis with Pandas
print("\nData analysis with Pandas:")
print("--------------------------")

# Loading a dataset
print("Loading a dataset:")
titanic_df = pd.read_csv("titanic.csv")
print("Head of the Titanic dataset:")
print(titanic_df.head())

# Exploring the dataset
print("\nExploring the dataset:")
print("Shape of the dataset:", titanic_df.shape)
print("Columns in the dataset:", titanic_df.columns)
print("Data types of the columns:")
print(titanic_df.dtypes)

# Handling missing values
print("\nHandling missing values:")
print("Number of missing values in each column:")
print(titanic_df.isnull().sum())

print("Filling missing values with mean:")
titanic_df["Age"].fillna(titanic_df["Age"].mean(), inplace=True)
print(titanic_df.isnull().sum())

# Data visualization with Pandas
print("\nData visualization with Pandas:")
print("-------------------------------")

# Bar plot
print("Bar plot of passenger class counts:")
titanic_df["Pclass"].value_counts().plot(kind="bar")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.title("Passenger Class Counts")
plt.show()

# Histogram
print("Histogram of passenger ages:")
titanic_df["Age"].plot(kind="hist", bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Passenger Age Distribution")
plt.show()

# Scatter plot
print("Scatter plot of fare vs. age:")
titanic_df.plot(kind="scatter", x="Fare", y="Age")
plt.xlabel("Fare")
plt.ylabel("Age")
plt.title("Fare vs. Age")
plt.show()

# Data manipulation with Pandas
print("\nData manipulation with Pandas:")
print("------------------------------")

# Grouping and aggregating data
print("Average age by passenger class:")
print(titanic_df.groupby("Pclass")["Age"].mean())

print("Survival rate by passenger class:")
print(titanic_df.groupby("Pclass")["Survived"].mean())

# Merging and joining DataFrames
print("\nMerging and joining DataFrames:")
print("--------------------------------")

# Creating sample DataFrames
df1 = pd.DataFrame({
    "key": ["A", "B", "C", "D"],
    "value1": [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    "key": ["B", "D", "E", "F"],
    "value2": [5, 6, 7, 8]
})

print("DataFrame 1:")
print(df1)

print("DataFrame 2:")
print(df2)

# Inner join
print("Inner join of the DataFrames:")
merged_df = pd.merge(df1, df2, on="key", how="inner")
print(merged_df)

# Outer join
print("Outer join of the DataFrames:")
merged_df = pd.merge(df1, df2, on="key", how="outer")
print(merged_df)

# Time series analysis with Pandas
print("\nTime series analysis with Pandas:")
print("---------------------------------")

# Creating a sample time series DataFrame
dates = pd.date_range("20210101", periods=5)
ts_df = pd.DataFrame(np.random.randn(5, 2), index=dates, columns=["A", "B"])
print("Time series DataFrame:")
print(ts_df)

# Resampling time series data
print("Resampling time series data:")
print(ts_df.resample("D").mean())

# Rolling window calculations
print("Rolling window calculations:")
print(ts_df.rolling(window=2).mean())

# Advanced Pandas operations
print("\nAdvanced Pandas operations:")
print("---------------------------")

# Applying functions to DataFrames
print("Applying a function to a DataFrame:")

def square(x):
    return x ** 2

print(df.apply(square))

# Pivot tables
print("Creating a pivot table:")
pivot_df = titanic_df.pivot_table(index="Pclass", columns="Sex", values="Survived", aggfunc=np.mean)
print(pivot_df)

# Melting DataFrames
print("Melting a DataFrame:")
melted_df = pd.melt(pivot_df.reset_index(), id_vars=["Pclass"], value_vars=["female", "male"])
print(melted_df)

# Pandas and data science
print("\nPandas and data science:")
print("------------------------")

print("Pandas is a powerful library for data manipulation and analysis in Python.")
print("It provides data structures like Series and DataFrame for efficient data handling.")
print("Pandas allows data loading, cleaning, transformation, and visualization.")
print("It integrates well with other data science libraries like NumPy, Matplotlib, and Scikit-learn.")
print("Pandas is widely used in data science tasks such as data preprocessing, exploratory data analysis, and feature engineering.")

print("\nThank you for exploring Pandas with us!")