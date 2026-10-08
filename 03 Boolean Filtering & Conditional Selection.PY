import pandas as pd
import numpy as np
import random

data = {
    "User_id": range(100,106),
    "User_name": ["AK","BK","DK","DK","SK","AK"],
    "Nabourhood":[ "Downtown", "Suburb", "Riverside", "Hilltop",
        "City Center", "Beachside"],
    "Price": [102800,54000,34000,76000,79900,24507]
}
house = pd.DataFrame(data)
# and &
print(house[(house["Price"]>50000) & (house["User_name"]=="AK")])  # parantheses is imp  and bit wise operand & | ~ 

# Or |
print(house[(house["Price"]<50000) | (house["User_name"]=="DK")])

# Not ~
print(house[~(house["User_name"]=="AK")])


# Isin()
print(house[(house["User_name"].isin(["AK","DK"]))])
print(house[(house["Nabourhood"].isin(["Suburb","Riverside"]))])

# Between()
print(house[house["Price"].between(40000,80000)])


# query()
print(house.query("Price > 50000 and User_name =='DK'"))


# String-based filters (.str)
print()
print(house[house["User_name"].str.contains("A")])


# Filtering Missing Values: isna() and notna()
print(house[house["Price"].isna()])


## np.where() with DataFrames
# np.where(condition, x, y) returns elements chosen from x or y depending on condition.
house["category"] = np.where(house["Price"]>50000, "high","low")
print(house["category"])



#============================================================================
## Practice
#============================================================================

# Exercise 1: Create a DataFrame with columns 'ID', 'Score'. Filter to keep only rows where Score >= 50.
df = pd.DataFrame({
    "ID":range(100,110),
    "Score":[random.randint(25,80) for _ in range(10)]
})
mask = df["Score"]>50
print(df[mask])

# Exercise 2: Use multiple conditions: Filter where Score is between 50 and 80, AND ID is even.
mask =(df["Score"].between(50,80) ) & (df["ID"]%2 ==0)
print(df[mask])


# Exercise 3: Load a mock Titanic dataset. Find all female passengers older than 30 who survived.
data = {
    "ID": range(1,101),
    "Survived": [random.choice(["Yes","No"]) for _ in range(100)],
    "Gender": [random.choice(["Male","Female"]) for _ in range(100)],
    "Age": [random.randint(21,60) for _ in range(100)],
    "Ticket_no": range(1000,1100)
}
titanic = pd.DataFrame(data)
# survied_female_over30 = (titanic["Age"]>30) & (titanic["Gender"] == "Female") & (titanic["Survived"]=="Yes") 
survied_female_over30 = titanic.query("Age > 30 and Gender =='Female' and Survived == 'Yes'")   # with query
print(survied_female_over30)


# Exercise 4:
# Combine .loc, .isin, string methods, and ~.
# Find all rows where the 'Status' is NOT in ['Failed', 'Cancelled'], and 'Description' contains the word 'Error', returning only the 'ID' and 'Description' columns.
data = {
    "ID": range(101,200),
    "Status": [random.choice(["Passed","Failed","Cancelled"]) for _ in range(101,200)],
    "Description": [random.choice(["I Passed error","Enjoyed Travel lover raigad","cooking Error Happy","sad error completed","successfully hero error","I am DK"])for _ in range(101,200)]
}
df = pd.DataFrame(data)
print(df)
# mask = df.query("Status != 'Failed' and Status != 'Cancelled' and Description.str.contains('error')")[["ID","Description"]] 
print(df.loc[~(df["Status"].isin(['Failed','Cancelled'])) & df["Description"].str.contains('error'),["ID","Description"]])


## Mini project
# Goal: Clean a messy user dataset for a machine learning model.
# Data: Columns ['UserID', 'Age', 'Email', 'Income'].
# Tasks:
# 1. Remove users with Age < 18 or Age > 100.
# 2. Keep only users who have a valid email (contains '@').
# 3. Fill 'Income' status as 'High' if Income > 100k, else 'Standard' using np.where.
# 4. Drop rows with missing 'Income'.

users_data = {
    "UserID": [
        "U001","U002","U003","U004","U005","U006","U007","U008","U009","U010",
        "U011","U012","U013","U014","U015","U016","U017","U018","U019","U020",
        "U021","U022","U023","U024","U025","U026","U027","U028","U029","U030",
        "U031","U032","U033","U034","U035","U036","U037","U038","U039","U040",
        "U041","U042","U043","U044","U045","U010","U047","U048","U049","U050",
        "U051","U052","U053","U054","U055","U056","U057","U058","U059","U060",
        "U061","U062","U063","U064","U065","U066","U067","U068","U069","U070",
        "U071","U072","U073","U074","U025","U076","U077","U078","U079","U080",
        "U081","U082","U083","U084","U085","U086","U087","U088","U089","U090",
        "U091","U092","U093","U094","U095","U096","U097","U098","U099","U100"
    ],

    "Age": [
        25,31,None,-5,120,"Thirty",29,41,35,28,
        22,45,19,54,None,27,24,39,150,33,
        30,26,"",37,42,29,34,23,21,"Unknown",
        32,44,18,57,66,None,28,35,-2,40,
        23,25,38,52,29,31,27,24,200,36,
        42,None,39,45,34,22,"NA",48,26,55,
        33,21,29,41,37,24,20,None,63,58,
        44,19,31,35,46,28,39,40,-10,51,
        32,27,"",23,36,65,43,34,25,47,
        30,22,38,29,41,33,None,50,26,37
    ],

    "Email": [
        "john@gmail.com","emma@yahoo.com","mike@","david@gmail.com","sara@example.com",
        "alex@gmail","", "tom@mail.com","harry@example.com","ivy@test.com",
        "user11@gmail.com","user12@yahoo.com","user13gmail.com","user14@gmail.com","user15@gmail.com",
        "user16@yahoo.com","user17@hotmail.com","user18@example.com","user19@gmail.com","user20@",
        "user21@gmail.com","user22@yahoo.com","user23@gmail.com","user24@example.com","duplicate@gmail.com",
        None,"user27@gmail.com","user28@yahoo.com","user29gmail.com","",
        "user31@gmail.com","user32@yahoo.com","user33@hotmail.com","user34@gmail.com","invalid",
        "user36@gmail.com","user37@yahoo.com","","user39@gmail.com","user40@example.com",
        "user41@gmail.com",None,"user43@yahoo.com","user44gmail.com","user45@example.com",
        "user46@gmail.com","user47@yahoo.com","bademail","user49@gmail.com","user50@hotmail.com",
        "user51@gmail.com","user52@yahoo.com","user53@example.com","user54@gmail.com","",
        "user56@gmail.com","user57gmail.com","user58@yahoo.com","user59@gmail.com","user60@",
        "user61@gmail.com","user62@example.com",None,"user64@gmail.com","user65@yahoo.com",
        "user66@hotmail.com","invalid@mail","user68@gmail.com","user69@gmail.com","",
        "user71@example.com","user72@gmail.com","user73@yahoo.com","user74gmail.com","user75@gmail.com",
        "user76@hotmail.com","user77@gmail.com",None,"user79@gmail.com","user80@example.com",
        "user81@gmail.com","user82@yahoo.com","","user84@gmail.com","user85gmail.com",
        "user86@hotmail.com","user87@gmail.com","user88@example.com","user89@","user90@gmail.com",
        "user91@gmail.com","user92@yahoo.com","user93@example.com",None,"user95@gmail.com",
        "user96@gmail.com","user97gmail.com","user98@example.com","user99@yahoo.com","user100@gmail.com"
    ],

    "Income": [
        45000,62000,55000,30000,None,70000,52000,-10000,"85000",48000,
        35000,78000,24000,95000,45000,"",64000,72000,55000,49000,
        51000,47000,39000,68000,88000,43000,61000,37000,32000,None,
        54000,82000,29000,102000,15000,58000,76000,-5000,63000,81000,
        42000,None,74000,56000,69000,87000,45000,52000,"N/A",60000,
        71000,38000,47000,79000,54000,66000,None,91000,32000,43000,
        58000,61000,72000,83000,-12000,37000,45000,98000,120000,55000,
        47000,63000,"Unknown",71000,68000,51000,49000,None,87000,62000,
        45000,39000,-3000,58000,76000,85000,91000,47000,66000,52000,
        43000,75000,None,54000,68000,59000,35000,81000,47000,62000
    ]
}
df = pd.DataFrame(users_data)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Income"] = pd.to_numeric(df["Income"],errors="coerce")
# 1. Remove users with Age < 18 or Age > 100.
clean_df = df[df["Age"].between(18,100)]

# 2. Keep only users who have a valid email (contains '@').
clean_df = clean_df[clean_df["Email"].str.contains('@')]

# 3. Fill 'Income' status as 'High' if Income > 50k, else 'Standard' using np.where.
clean_df["Income_status"] = np.where(clean_df["Income"]> 50000, "High","Standard")

# 4. Drop rows with missing 'Income'.
clean_df = clean_df[clean_df["Income"].notna()]
print(clean_df)