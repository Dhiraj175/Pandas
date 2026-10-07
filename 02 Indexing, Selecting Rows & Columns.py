import pandas as pd
import random
import datetime 
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90.5, 88.0, 95.2]
},index=["S1","S2","S3"])

## Selecting a single column
ages = df["Age"]  # To select a single column, use bracket notation [] with the column name as a string.
print(ages)
print(type(ages))

## Selecting Multiple Columns
student_score = df[["Name","Score"]]
print(student_score)
print(student_score.dtypes)
print(student_score.shape)
print(type(student_score))


## Selecting row
print(df.loc["S1"])  # label based  
print(df.loc[["S1","S3"]])
print(df.iloc[0])    # integer position based 
print(df.iloc[[1,2]]) 


## Slicing 
print(df.iloc[0:2]) #2 excluded 
print(df.iloc[0:2,1:]) # row and column slicing 
print(df.loc["S1":"S3"])  # S3 include


# Scalar Access: .at[] and .iat[]
# If only need a single specific value (a scalar), .at and .iat are much faster than .loc and .iloc.
print(df.at["S1","Score"])
print(df.iat[1,0]) 


## Boolean indexing
mask = df["Score"]> 90
print(mask)
passed = df.loc[mask]
print(passed)



# ===================================================================
## Practice
# ===================================================================

# Exercise 1 : Given a DataFrame of housing prices, use .loc to filter for houses where price > 500000 and select only the "neighborhood" and "price" columns.
data = {
    "User_id": range(100,106),
    "User_name": ["AK","BK","CK","DK","EK","KK"],
    "Nabourhood":[ "Downtown", "Suburb", "Riverside", "Hilltop",
        "City Center", "Beachside"],
    "Price": [102800,54000,34000,46000,79900,49598]
}
house = pd.DataFrame(data)
mask = house["Price"] > 50000
print(house[["Price","Nabourhood"]][mask])


result = house.loc[house["Price"]>50000, ["Price","Nabourhood"]]
print(result)


# Exercise 2: You have a DataFrame X_train with 1000 rows. Use .iloc to split it into X_train_fold1 (first 800 rows) and X_val_fold1 (last 200 rows).
df = pd.DataFrame({
    "Train_no": range(1,1001),
    "Price": [random.randint(100,500) for _ in range(1000)]
})
X_train_fold1 = df[:800]
X_val_fold1 = df[-200:]
print(X_val_fold1)


## Exercise 2: You have a DataFrame transactions with columns: ['TransactionID', 'Amount', 'Location', 'Is_Fraud'].
# Your index consists of unique dates: e.g., "2023-01-01" to "2023-12-31".
data = {
    "TransactionID": range(1000,1365),
    "Amount": [random.randint(100,100)*500 for _ in range(365)],
    "Location":[random.choice(["Jalgaon","jamod","Pune","mumbai","solapur","satara","akola","buldana","washim","raigad","Nashik","Thane","SN","Yavatmal","Nagpur","Amravti"]) for j in range(365)] ,
    "Is_Fraud": [random.choice([True,False]) for i in range(365)]
}
transactions = pd.DataFrame(data,index=[pd.date_range(start="2023-01-01",end="2023-12-31")])

# Task 1: Using .loc, extract all columns for dates from "2023-06-01" to "2023-06-30".
second_half = transactions.loc["2023-06-01":"2023-06-30"]
print(second_half)

# Task 2: From that subset, filter rows where Amount > 10000.
print(second_half.loc[second_half["Amount"]> 10000])

