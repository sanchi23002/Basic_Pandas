import pandas as pd 
 
s =pd.Series([10,20,30,40,50])
print("THE SERIES IS\n",s)
print(s.dtype)
print(s.index)
print(s.values)
print(s.shape)
#giving a name 
s.name = "numbers"
print(s)
#indexing
print(f"\nthe third element of the series is {s[2]}")
print(f"the 1st,third values are{s[0:3:2]}")
#fetching indexes(iloc)
print(f"{s.iloc[2]}\n{s.iloc[[0,1,2,3]]}")
#row indexing
ind = ["apple","banana","grapes","orange","strawberry"]
s.index = ind
print(s)
#we cant use iloc for strings but can for numerical indexes
#for strings we use loc
print(f"THE NUMBER OF APPLES IS {s["apple"]}")
print(f"THE NUMBER OF BANANA ARE {s.loc["banana"]} ")
#in level based indexing your start as well as stop value both are included
print("THE FIRST THREE ELEMENT OF THE ARRAY IS",s["apple":"grapes"])
#dictionary formation
fruit_protein ={
    "apple" : 2.0,
    "banana" :3.0,
    "guava" : 2.5,
    "kiwi" :1.1,
    "mango" : 0.8
}
s2= pd.Series(fruit_protein,name = "protein")
print(s2)

##conditional selection
s3=s2[s2>1]
print(s3)

##logical operator (and , or and not)
s4=s2[(s2>=2)&(s2<3)]#similarly for or operation we need |
print(s4)
s5=s2[s2!=1.1]
print(s5)
#not gretter than 
s6=s2[~(s2>1)]
print(s6)

##modifying a series 
s2["mango"]=0.6
print(s2.loc["mango"])

