import pandas as pd
import numpy as np

# DataFrame:

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

df = pd.DataFrame(data)

##dublicates
dup = df[df.duplicated()]#dup = df[df.duplicated(keep="first")]
print(dup)
dup2 = df[df.duplicated(keep= "last")]
print(dup2)
df= df.drop_duplicates()
print(df)

##invalid values(making changes using condition : lemda function)
df["Salary"]=df["Salary"].apply(lambda x:x/10 if x>60000 else x)
print("\n",df)
df["Name"]= df["Name"].replace({"Alice":"Alice_John","Eve":"Eve Charl"},inplace=True)
#spliting name 
df[["First name","Last name"]]=df["Name"].str.split(r" |_",expand=True)
print(df)

#using function for changing 
def multiply_age(x):
    return 2*x
df["Age"]=df["Age"].apply(multiply_age)
print("\n",df)
df["Age"]=df["Age"].apply(lambda x:x/2)
print("\n",df)

##if we had two different datasheet and we have to combine them 
##then there are two methods 1.joins 2.merges
##joins are 4 types :left , right , outer , inner

# Joins and Merges

department_info = {
    "Department": ["HR", "IT", "Finance"],
    "Location": ["New York", "San Francisco", "Chicago"],
    "Manager": ["Laura", "Steve", "Nina"]
}

df2 = pd.DataFrame(department_info)
df3 = pd.concat([df,df2])
print("\n\n",df3)
#for combining column wise 
df4 = pd.concat([df,df2],axis =1)
print("\n\n",df4)
#for not getting repeated feature use merge
df5 = pd.merge(df,df2, on="Department")
print(df5)

##how to read or bring a data on platform
 
# for google collab you should write
# data = pd.read_csv("data.csv") , if you are using any downloaded app
#then give the path of the file in place of "data.csv"
#if there is any object dtype , then to change it in valid panda format
#data['date']=pd.to_datetime(data['date'])
 