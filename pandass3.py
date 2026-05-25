import pandas as pd
import numpy as np

# DataFrame:

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

df =pd.DataFrame(data)
print(df)
## searching unique element in any column
print(df["Department"].unique())
#to know how many people in that department
print(df["Department"].value_counts())

#creating new column
df["promoted salary"] = df["Salary"]*10
print("\n\n")
print(df)

##DATA CLEANING

#checking number of null values
print(df.isnull().sum())
#if any values in any row is null then drop it 
print(df.dropna(how="any"))#print(df.dropna())works same
#if all the values of the ropw is null, then drop it 
print("\n\n")
print(df.dropna(how="all"))
 #filling all the null data by 0
print("\n")
print(df.fillna(0))
#replacing age with mean salary with median
data2=df.fillna(df["Age"].mean())#you can use inplace = true
print("\n",data2)
data3=df.fillna(df["Salary"].median())
print(f"\n{data3}")

# for filling there is two methods 1.forward fill 2.backward fill

print("\n")
print(df["Age"].ffill())
print("\n")
print(df["Salary"].bfill())
df["Name"]=df["Name"].replace("Charlie","Rose",inplace = True)
print("\n",df)
