import pandas as pd
import numpy as np

##dataframe

# DataFrame:

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}
df= pd.DataFrame(data)
print(df)
print(df.head(2))#print first two rows
print(df.tail(2))#print last two rows

##loc and iloc
print(df.iloc[0:3:2])
print(df.loc[0:3:2,["Age","Department"]])
print(df[["Age","Department"]])#for multiple column use 2 bracket
#column reoval {axis = 1}, row removal {axis = 0}
df_new= df.drop("Age", axis =1)
print(df_new)
#to replace from raw data (given)
#df_new2 = df.drop("Department",axis =1, inplace=True)
#print("\n\n\n")
#print(df_new2)
#print("\n\n")
#print(df)#new data will be changed 
print(df.shape)# (row,column) = (samples, features)

#information about data
print("\n the information about the data")
print(df.info())
#for getting information calculation on numerical datatype
print("\n",df.describe())

##brodcasting
df["Salary"] += 5000
print(df["Salary"])

##renaming column
new = df.rename(columns = {"Department":"dept"},inplace = True)
print(df)