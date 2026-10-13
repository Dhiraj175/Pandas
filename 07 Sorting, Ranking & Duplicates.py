import pandas as pd
import numpy as np
## Sorting by Values: sort_values()
# df.sort_values(by='column_name', ascending=True, na_position='last')

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 92, 85, 78, np.nan],
    'Age': [25, 22, 23, 22, 29]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by="Score",ascending=False)
print(sorted_df)

## Sorting by Multiple Columns
mult_sort = df.sort_values(by=["Score","Age"],ascending=[False,True])
print(mult_sort)

restored_df = sorted_df.sort_index()
print(restored_df.index)


## Ranking: rank()
marks = pd.Series([90,100,90,80,70,90])
print(marks.rank(method="average",ascending=False))  # 90 ties at 2 3 4 - avg 3 next start at 5
print(marks.rank(method="min",ascending=False))  # 90 ties at 2 3 4 - taken min 2 next at 5
print(marks.rank(method="max",ascending=False))  # 90 ties at 2 3 4 - taken min 4 next at 5
print(marks.rank(method="first",ascending=False)) # Ranks assigned in order they appear in the array.
print(marks.rank(method="dense",ascending=False))




## Finding and Removing Duplicates
# duplicated()
# Returns a boolean Series denoting duplicate rows.

# keep='first' (default): Mark duplicates as True except for the first occurrence.
# keep='last': Mark duplicates as True except for the last occurrence.
# keep=False: Mark ALL duplicates as True (even the first one).
data = {'user_id': [1, 2, 2, 3, 1], 'action': ['click', 'view', 'view', 'click', 'click']}
df_dup = pd.DataFrame(data)
print(df_dup.duplicated())

# drop_duplicates()
clean_df = df_dup.drop_duplicates(keep="last")
print(clean_df)



## Unique Values and Frequencies
# unique(): Returns a NumPy array of unique values in order of appearance.
# nunique(): Returns the count of unique values.
# value_counts(): Extremely useful! Returns a Series containing counts of unique values.
colors = pd.Series(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(colors.unique())
print(colors.nunique())
print(colors.value_counts())
print(colors.value_counts(normalize=True))



# ============================================================================
# Practice
# ============================================================================

# Exercise 1:
df = pd.DataFrame({
    "X":np.random.randint(10,100,size=20),
    "Y": np.random.choice(["Car","Bike","Mobile","Laptop"],size=20)
})
# Sort df by column 'X' ascending.
print(df.sort_values("X",ascending=False))
print(df["X"].sort_values(ascending=False))

# Get the unique values of df['Y']
print(df["Y"].unique())
print(df["Y"].value_counts())

print(df["X"].sort_values(ascending=False).index)



# Exercise 2:
# Given a DataFrame of 1000 cars with columns ['Make', 'Model', 'Price']:
make = np.random.choice(['Toyota', 'Honda', 'Ford', 'Hyundai', 'Nissan',
             'BMW', 'Mercedes', 'Audi', 'Kia', 'Volkswagen'],size=1000)
model = np.random.choice(['Corolla', 'Civic', 'Focus', 'Elantra', 'Sentra',
              '3 Series', 'C-Class', 'A4', 'Forte', 'Jetta'],size=1000)
price = np.random.randint(5000,100000,size=1000)*100

cars= pd.DataFrame({
    "Make": make,
    "Model": model,
    "Price": price
})
print(cars)

# 1. Find the top 3 most expensive cars.
Expensive_cars = cars.sort_values("Price",ascending=False)
print(Expensive_cars[:3])

# 2. Find the number of unique 'Make's.
print(cars["Make"].nunique())

# 3. Get the percentage of cars that are of Make 'Toyota'.
print((cars["Make"]=="Toyota").value_counts(normalize=True))
print((cars["Make"]== "Toyota").mean()*100)
print(cars["Make"].value_counts(normalize=True)["Toyota"])


# exercise 3:
# DataFrame of model predictions with columns ['user_id', 'prob_click']
user_id = np.random.randint(100,150,size=200)
prob_click = np.random.random(size=200)
prediction = pd.DataFrame({
    "user_id": user_id,
    "prob_click": prob_click
})

# 1. Assign a rank to each user based on prob_click (highest prob = rank 1), using dense ranking.
prediction["rank"] = prediction["prob_click"].rank(method="dense",ascending=False).astype("int")
top_5 = prediction[prediction["rank"]<=5]
print(top_5.sort_values("rank",ascending=True))

# 2. Remove any duplicate user_ids, keeping the one with the highest prob_click.
sorted_prob_click = prediction.sort_values("prob_click",ascending=False)
duplicate_removed = sorted_prob_click.drop_duplicates(keep="first",subset=["user_id"])
print(duplicate_removed.shape)


# Exercise 4:
# You have a dataset of student test submissions. Sometimes students double-click submit, creating duplicate records.
# Columns: ['student_id', 'timestamp', 'score']
student_id = np.random.randint(1,75,size=100)
timestamp = (pd.to_datetime("2026-10-13")+ pd.to_timedelta(np.random.randint(0,24*60,size= 100),unit="m"))
score = np.random.randint(20,100,size= 100)

test = pd.DataFrame({
    "student_id": student_id,
    "timestamp": timestamp,
    "score": score
})

# 1. Sort the DataFrame by student_id and timestamp (both ascending).
test = test.sort_values(by=["student_id","timestamp"])

# 2. Drop duplicate submissions per student, keeping ONLY the last submission (most recent).
test = test.drop_duplicates(subset=["student_id"],keep="last")

# 3. Add a column class_rank based on their final score (highest score = rank 1, handle ties with 'min')
test["class_rank"] = test["score"].rank(method="min",ascending=False).astype("int")
print(test)

# 4. Find the most common score in the class.
common_scores = test["score"].value_counts().head(1)
print(common_scores)

common_scores = test["score"].mode()[0]
print(common_scores)

common_scores = test["score"].value_counts().idxmax()
print(common_scores)


## Mini Project 
# "The Sales Leaderboard"
# Generate a dummy DataFrame of 50 sales reps. Each has a region and sales_amount.
employee_id = range(1,51)
region= np.random.choice([ "Africa","Europe","Asia-Pacific","North America","South America","Middle East"],size=50)
sales_amount = np.random.randint(10000,500000,size=50)
sales = pd.DataFrame({
    "employee_id": employee_id,
    "region":region,
    "sales_amount": sales_amount
})

# 1. Check for and remove any exact duplicate rows.
print(sales.duplicated().sum()) # no duplicate

# 2. Rank the sales reps globally (across all regions).
sales["rank"] = sales["sales_amount"].rank(ascending=False,method="dense").astype(int)

# 3. Find which region has the highest number of reps (using value_counts).
highest_reps_region = sales.value_counts(subset=["region"]).idxmax()
print(highest_reps_region)

# 4. Sort the DataFrame so the top rep overall is at row index 0.
sales = sales.sort_values(by=["sales_amount"],ascending=False).reset_index(drop=True)
print(sales)