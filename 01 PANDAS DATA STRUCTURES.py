import pandas as pd
import numpy as np

# Pandas has two fundamental data structures: Series and dataframe

# ________________________________________________________________________
# 1. Series 
# ________________________________________________________________________

marks = pd.Series([40,79,96,64,34])   # automatically assigned an index: 0, 1, 2, 3 (called RangeIndex)

# with custom index
marks = pd.Series([40,79,96,64,34],index= ["PK","AK","DK","GK","SK"])
print(marks)

# from dict
marks = pd.Series({"Pk":40,"AK":79,"DK":96,"GK":34})  #  keys become the index, the values become the data.
print(marks)

# from numpy array
np_arr = np.array([40,79,96,64,34])
marks = pd.Series(np_arr,index=["PK","AK","DK","GK","SK"])
print(marks.values)
print(marks.index)
print(marks.dtype)
print(marks.shape)
print(marks.ndim)
print(marks.size)

# NumPy vs Series — Side by Side
# NumPy
np_marks = np.array([85, 92, 67, 78])
print(np_marks[0])          # 85 — positional access only
print(np_marks.dtype)       # int64
print(np_marks.shape)       # (4,)

# Pandas Series
pd_marks = pd.Series([85, 92, 67, 78], index=["Arjun", "Bhavna", "Chirag", "Diya"])
print(pd_marks["Arjun"])    # 85 — label-based access!
print(pd_marks.iloc[0])     # 85 — positional access also works
print(pd_marks.dtype)       # int64
print(pd_marks.shape)       # (4,)
# Key difference: With NumPy you access by position. With Pandas you can access by label OR position.


## Accessing Elements in a Series
print(pd_marks["Arjun"])
print(pd_marks[["Arjun","Diya","Bhavna"]])
print(pd_marks.iloc[1])
print(pd_marks.iloc[:2]) # like numpy 2 excluded 
print(pd_marks.loc["Arjun":"Diya"])  # include diya



# ________________________________________________________________________
# 2. DataFrame: The 2D Labeled Table
# ________________________________________________________________________

# A DataFrame is a two-dimensional labeled data structure — like a spreadsheet, SQL table, or a dictionary of Series.
# Every column in a DataFrame is a Series.


## Creating a DataFrame
# From dict of list
data = {
    "name" : ["DK","AK","PK"],
    "age" : [25,20,24],
    "result" : ["Pass","Pass","Fail"],
    "salary" : [30000,20000,18000]
}
df = pd.DataFrame(data, index= ["I", "II","III"])
print(df.columns)
print(df.index)
print(df.values)
print(df.dtypes)

print(df["name"]) # for column
print(df.loc["I"]) # row
print(df.iloc[1]) # row

print(f"Sample: {df.shape[0]}")  # sample rows
print(f"Feature: {df.shape[1]}")  # feature column

# index alignment
# s1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
# s2 = pd.Series([100, 200, 300], index=["b", "c", "d"])
# print(s1+s2)




## Inspecting a DataFrame: 
data = {
    "name": ["Arjun", "Bhavna", "Chirag", "Diya", "Esha",
             "Farhan", "Gauri", "Harsh", "Isha", "Jay"],
    "age": [20, 22, 19, 21, 23, 20, 22, 24, 19, 21],
    "marks": [85, 92, 67, 78, 95, 55, 88, 72, 91, 60],
    "city": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi",
             "Mumbai", "Bangalore", "Delhi", "Mumbai", "Bangalore"],
    "passed": [True, True, False, True, True,
               False, True, True, True, False]
}

df = pd.DataFrame(data)

# head() — See the First Few Rows
print(df.head()) # first 5 default
print(df.head(2))  # first 2 rows

# Tail () -- last few rows
print(df.tail())  # last 5 default
print(df.tail(2)) # last 2 rows

# sample() — See Random Rows
print(df.sample(3))

# complete overview 
print(df.info())

# describe() — Statistical Summary   -- only shows numeric columns by default. Text/object columns are excluded.
print(df.describe())
print(df.describe(include="all"))




# =====================================================================
## Practice
# =====================================================================

# Exercise 1: Create a Series of 5 temperatures: 32.5, 28.1, 35.0, 30.2, 27.8
temp = pd.Series([32.5,28.1,35,30.2,27.8])
print(temp.shape)  # 5,0 & dtype is float64

# Exercise 2: Create a Series with custom index:
temp = pd.Series([32.5,28.1,35,30.2,27.8],index=["I","II","III","IV","V"])
print(temp)


# Exercise 3: Create DataFrame from a dictionary:
data = {
    "Product": ["Laptop","TV","Smartphone"],
    "Price": [56000,48000,35000],
    "Quantity": [4,2,12]
}
items = pd.DataFrame(data)
print(items.shape) #  3,3
print(items.dtypes) # str,int64,int64
print(items.ndim) # 2D

# Exercise 4: given DataFrame, what will each command return?
df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [90, 85, 75, 95]
})

# a) df.shape
print(df.shape) # 4,2

# b) df.size
print(df.size) # 8

# c) df.ndim
print(df.ndim) # 2

# d) type(df["score"])
print(type(df["score"]))

# e) type(df[["score"]])
print(type(df[["score"]]))

# f) df["score"].dtype
print(df["score"].dtypes) # int64



# Exercise 6: Given this Series:

s = pd.Series([10, 20, 30], index=["x", "y", "z"])

# - s.values → ?
print(s.values) # 10,20,30

# - s.index → ?
print(s.index) # x,y,z

# - s.dtype → ?
print(s.dtype) # int64

# - type(s.values) → ?
print(type(s.values)) 
print(type(s.index)) 


# Exercise 7: Two Series are added:

s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["c", "b", "a"])
print(s1+s2) # 31,22,13


print(items.describe())

# Exercise 8: Create a DataFrame representing 5 employees - 
data = {
    "Emp_ID": [101,102,103,104,105],
    "Name": ["DK","AK","PK","SK","KK"],
    "Department": ["BD","Sale","IT","Non IT","CA"],
    "Salary": [45000,15000,46000,35400,24000],
    "Is_actice": [True,True,False,True,False]
}
emp = pd.DataFrame(data)
# 1. Print info() and explain each line of output
print(emp.info())

# 2. Print describe() and explain what it shows and what it does NOT show
print(emp.describe())

# 3. Print the shape and explain what rows and columns represent
print(emp.shape)

# 4. Extract the "salary" column — what type is it? Series or DataFrame?
print(emp["Salary"])
print(type(emp["Salary"]))

# 5. Convert the salary column to a NumPy array
sal_np = emp["Salary"].to_numpy()
print(sal_np)
print(type(sal_np))



## Exercise 9:
student_data = {
    "Name" : ["Dhiraj","Prashant","Anand","Yash","Daksh","Bhavesh","Sagar","Pooja"],
    "Age": [25,26,20,18,30,27,36,22],
    "Math_score": [99,64,34,87,86,74,58,91],
    "Sci_score": [97,64,74,89,81,67,83,49],
    "City": ["Jalgaon","Jamod","Pune","Mumbai","Nashik","Amravti","Nagpur","Akola"]
}
student = pd.DataFrame(student_data,index=["R001","R002","R003","R004","R005","R006","R007","R008"])
print(student.head(3))
print(student.tail(2))
print(student.sample(4))
print(student.shape)
print(student.info())
print(student.describe(include="all"))
math_numpy = student["Math_score"].to_numpy()
print(math_numpy)



##  Exercise 
df = pd.DataFrame({
    "study_hours": [2, 5, 1, 8, 3, 7, 4, 6, 2, 9],
    "attendance_pct": [60, 90, 40, 95, 70, 85, 75, 80, 55, 98],
    "marks": [45, 85, 30, 95, 55, 80, 65, 75, 40, 99],
    "passed": [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
})

# 1. How many samples are there?
print(df.shape[0])

# 2. How many features are there?
print(df.shape[1])


# 3. Which column is the target variable (what would we predict)?  ----- passed 
# 4. What are the input features? ---- study hours and attendence 

# 5. What is the dtype of the target? Is this a classification or regression problem?
print(df["passed"].dtype)

# 6. Run describe() — what is the average marks? What is the min and max study_hours?
print(df.describe())

# 7. Convert only the input features to a NumPy array. What shape is it?
study_hours_numpy = df[["study_hours","attendance_pct"]].to_numpy()
print(study_hours_numpy.shape)
# 8. Convert the target to a NumPy array. What shape is it?