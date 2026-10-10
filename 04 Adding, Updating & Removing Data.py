import pandas as pd
import numpy as np
import random
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df["Total"] = df["A"]+ df["B"]
print(df)

## The assign() Method
# .assign() allows to create new columns in a chainable way. It returns a new DataFrame and leaves the original unchanged
new_df = df.assign(D = df["A"]**2)  # return new dataframe
print(new_df)

## Updating Existing Values
# Updating via .loc
df.loc[0] = 90
df.loc[1,"B"] = 105

# Conditional Assignment
df.loc[df["A"]<75,"B"] = 0  # If A < 75, set B to 0
print(df)

## Conditional Column Creation
# np.where for 2 outcomes
df["status"] = np.where(df["Total"]>10,"High","Low")
print(df)

# np.select() for multiple conditions
conditions = [
    df["Total"] > 50,
    df["Total"] > 5,
]
choices = [
    "High",
    "Medium",
]
df["Category"] = np.select(conditions,choices,default="Low")
print(df)


## Rename columns and rows
df = df.rename(columns={"A":"Alpha","B":"Beta"})
df = df.rename(index= {0:"Row1"})
print(df)

## Removing Data
# drop()  --- Returns a NEW DataFrame (unless inplace=True).
# df_drop_row = df.drop("Row1")
df_drop_row = df.drop(["Row1",2],axis=0) # Axis = 0 for rows
print(df_drop_row)

# df_drop_cloumn = df.drop(["Alpha"],axis=1,inplace= True)
df_drop_cloumn = df.drop(["Alpha"],axis=1)
print(df_drop_cloumn)

## pop() -- Removes a column from the DataFrame and returns it as a Series.
# Modify or new? Modifies the original DataFrame IN PLACE.
popped_col = df.pop("Alpha")
print(f"\n{popped_col}")
print(df)


## Managing the Index
df = df.set_index("Beta")
print(df)
df = df.reset_index()
print(df)



# ============================================================================
#Practice
# ============================================================================

# Exercise 1:  Create a DataFrame with columns 'Price' and 'Qty'. Add a 'Revenue' column (Price * Qty)
df = pd.DataFrame({
    "Price": [random.randint(1000,10000) for _ in range(10)],
    "Quantity": [random.randint(1,20) for _ in range(10)]
})
df["Revenue"] = df["Price"] + df["Quantity"]
print(df)

new_df = df.assign(Revenue = df["Price"] + df["Quantity"])
print(new_df)
print(df)


# Exercise 2: Use np.where to add a 'Discount' column: True if Qty > 10, False otherwise
df["Discount"] = np.where(df["Quantity"]>10,True,False)
print(df)


# Exercise 3 : cap the 'Quantity' column at 15. Any Discount with >5 bedrooms should be set to 5 using .loc. Then drop the 'discount' column.
df.loc[df["Quantity"]>15,"Quantity"]= 15
df = df.drop("Discount",axis=1)
print(df)


# Exercise 4: 
# Do this using method chaining if possible (using assign, drop, rename, set_index).
df = pd.DataFrame({
    "col1": [random.randint(150,350) for _ in range(100,105)],
    "ID": range(100,105),
    "Temp": [round(random.random()*100,2) for _ in range(100,105)]
})

# 1. Rename 'Col1' to 'Feature1'.
df = df.rename(columns={"col1":"Feature1"})

# 2. Set 'ID' column as the index.
df = df.set_index('ID')

# 3. Drop 'Temp' column.
dropped_temp = df.drop("Temp",axis=1)
print(dropped_temp)

# 4. Add 'Normalized' column = 'Feature1' / 100.
new_df = df.assign(Normalized = df["Feature1"]/100)
print(new_df)
print(df)


# Mini Project 
df = pd.DataFrame({
    "User": [
        "Alice", "Bob", "Charlie", "David", "Eva",
        " Frank ", "Grace", "Henry", "Ivy", "Jack",
        "alice", "Bob", "Kevin", "Luna", "Mike",
        "Nina", "Oscar", "Pam", "Quinn", "Rachel"
    ],
    "Age": [
        25, 30, None, 28, 22,
        35, -5, 150, 29, 31,
        25, 30, 27, None, 33,
        26, " 40 ", "twenty-eight", 29, None
    ],
    "Salary": [
        50000, "60,000", 55000, "$58000", 45000,
        70000, 52000, 80000, None, 65000,
        50000, "60,000", 54000, 47000, "not available",
        51000, 90000, 62000, "$75,000", 58000
    ],
    "JoinDate": [
        "2023-01-15", "15/02/2022", "2021-03-20", "04-10-2020", "2023/05/18",
        "18-Jun-2021", "2022-07-30", "2021-08-15", "09/09/2020", None,
        "2023-01-15", "15/02/2022", "2020/11/25", "March 12 2021", "2022-12-01",
        "2023.04.10", "2021-01-05", "2020-06-18", "07/14/2022", "2023-08-20"
    ]
})

df["Age"] = pd.to_numeric(df["Age"],errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"],errors="coerce")
# 1.  Drop the 'User' column (not useful for ML).
df = df.drop("User",axis=1)

# 2. Create 'Age_Group': <25='Young', 25-50='Adult', >50='Senior' (use np.select).
conditions = [
    df["Age"]>= 50,
    df["Age"] >= 25,
]
choices = [
    "Senior",
    "Adult"
]
df["Age_Group"] = np.select(conditions,choices,default="Young")
print(df)

# 3. If Salary is missing, set it to the median salary using conditional assignment.
median_sal = np.nanmedian(df["Salary"])  # both are correct
median_sal = df["Salary"].median()
df.loc[df["Salary"].isna(),"Salary"] = median_sal
print(df)


