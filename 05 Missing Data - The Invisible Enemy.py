import pandas as pd
import numpy as np

# isna()/isnull(), Notna()/notnull() 
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 'b', 'c', 'd'],
    'C': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print(df.isna())  # true if na
print(df.notna())  # isnull


# Counting and Quantifying Missing Values
print(df.isna().sum())
# print(df.info())

# Counting Total Missing Values in the Entire DataFrame
print(df.isna().sum().sum())

# Calculating the Percentage of Missing Values
print(df.isna().mean()*100)



## Dropping Missing Data: dropna()
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# how: 'any' drops the row/col if any NA values are present. 'all' drops it only if all values are NA. (Default: 'any')
# thresh: Require that many non-NA values. e.g., thresh=3 means "keep the row if it has at least 3 non-missing values".
# subset: Only look for NA values in specific columns (when axis=0) or rows (when axis=1).

dropped_na = df.dropna()
print(dropped_na)

df.loc[4] = [np.nan,np.nan,None]
dropped_na = df.dropna(how="all")  # Drop rows only if ALL values are missing
print(dropped_na)
 
dropped_na= df.dropna(subset="A") #  Drop rows only if they have a missing value in column 'A'.
print(dropped_na)
# Use it when the number of missing values is extremely small (e.g., < 1% of the dataset) and dropping them won't significantly reduce your dataset size or introduce bias.



## Filling Missing Data: fillna()
# df.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
# Filling with a Scalar Value
print(df.fillna(0))  # fill All nan with 0
df["A"] = df['A'].fillna(10)   # fill a specific column
print(df)


# Filling with a Dictionary
fill_values = {"A":100, "B":"Unknown","C":-1}
print(df.fillna(value=fill_values))



# forwardfill ffill() and backwardfill bfill()
# In time-series data, if a value is missing, it often makes sense to carry the last known value forward (ffill), or the next known value backward (bfill).
time_data = pd.Series([10, np.nan, np.nan, 40, 50])
# print(time_data.ffill()) # privious value
print(time_data.bfill())  # after value


## Statistical Imputation (Mean, Median, Mode)
age = pd.Series([25, 30, None, 28, 22,
        35, -5, 150, 29, 31,
        25, 30, 27, None, 33,
        26, " 40 ", "twenty-eight", 29, None])
age = pd.to_numeric(age,errors="coerce")

# print(age.fillna(age.mean()))  # mean imputation
print(age.fillna(age.median()))  # median imputation

df = pd.DataFrame({
    "category" :["Food", "Travel", "Food", None, "Shopping", "Travel",
        "Food", "Health", None, "Shopping", "Education",
        "Food", "Travel", "Bills", "Health", "Food",
        "Entertainment", "Travel", pd.NA, "Shopping"],
    "age": [25, 30, None, 28, 22,
        35, -5, 150, 29, 31,
        25, 30, 27, None, 33,
        26, " 40 ", "twenty-eight", 29, None]
})
#  Mode Imputation (for categories)
print(df["category"].fillna(df['category'].mode()[0])) # mode() returns a Series, so we take index [0]


##  Group-Based Imputation
people = pd.DataFrame({
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Height': [180, 165, np.nan, 160, 175, np.nan]
})
mean_height = people.groupby("Gender")["Height"].transform("mean")
print(mean_height)
people["Height"] = people["Height"].fillna(mean_height)
print(people)


##  Interpolation -- Interpolation is a mathematical method of estimating unknown values that fall between known values. It is exceptionally powerful for time-series data.
# df['column'].interpolate(method='linear')
ts = pd.Series([0, np.nan, np.nan, 30])
print(ts.interpolate(method="linear"))




#================================================================
# Practice
#================================================================

#Level 1: Basic
s = pd.Series([10, np.nan, 20, np.nan, 30])
# 1. How many missing values are there?
print(s.isna().sum())
# 2. Fill the missing values with the number 99.
s = s.fillna(99)
print(s)



# Exercise 2:
df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'B'], 'Value': [10, np.nan, 100, np.nan, 300]})
# Fill the missing values using group-based mean imputation (mean of their respective Category).
mean_value = df.groupby("Category")["Value"].transform("mean")
df["Value"] = df["Value"].fillna(mean_value)
print(df)



## Exercise 3:
sales = pd.DataFrame({
    'Day': pd.date_range(start='2023-01-01', periods=10),
    'Store_A': [100, 110, np.nan, np.nan, 150, 160, np.nan, 180, 190, 200],
    'Store_B': [500, np.nan, 520, 530, np.nan, 550, 560, 570, 580, np.nan]
})
# 1. Print the percentage of missing data per store.
print(sales.isna().mean()*100)

# 2. For Store A, the missing data represents consecutive days the store was closed for renovations. Fill these using linear interpolation.
sales["Store_A"] = sales["Store_A"].interpolate(method="linear")
print(sales)

# 3. For Store B, the missing data is random errors. Fill these by carrying the previous day's sales forward (ffill).
sales["Store_B"] = sales["Store_B"].ffill()
print(sales)




## 
sensor_data = pd.DataFrame({
    'Timestamp': pd.date_range('2025-01-01', periods=12, freq='h'),'Temp_Celsius': [22.5, 22.8, 23.1, np.nan, np.nan, np.nan, 24.2, 24.0, 23.8, 23.5, 23.2, 22.9],
    'Humidity': [78.0, 68.0, 47.0, 60.0, np.nan, 78.0, 58.0, np.nan, 50.0, 50.0, np.nan, 75.0]
    })

#  Visualize the missing data
# print(sensor_data.info())
print(sensor_data.isna().sum())
print(sensor_data.isna().mean()*100)

# Drop any rows where BOTH Temp and Humidity are missing.
dropped_row = sensor_data.dropna(how="all",subset=["Temp_Celsius","Humidity"])
print(dropped_row)

# Impute Temp_Celsius using linear interpolation.
sensor_data["Temp_Celsius"] = sensor_data["Temp_Celsius"].interpolate(method="linear")
print(sensor_data)

# Impute Humidity using the overall median.
sensor_data["Humidity"] = sensor_data["Humidity"].fillna(sensor_data["Humidity"].median())
print(sensor_data)