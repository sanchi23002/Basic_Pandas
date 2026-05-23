import numpy as np
 
##aggregate function (works on one array)

arr = np.array([10,20,30])
print(np.sum(arr))
print("THE MEAN OF THE ARRAY IS ",np.mean(arr))
print("THE MEDIAN OF THE ARRAY ",np.median(arr))
print("THE STANDARD DEVIATION OF THE ARRAY IS ",np.std(arr))
print("THE VARIENCE OF THE ARRAY IS ",np.var(arr))
print("THE MINIMUM VALUE OF ARRAY IS ",np.min(arr))
print("THE MAXIMUM NUMBER OF THE ARRAY IS ",np.max(arr))
#for column and row wise sum use axis
#axis=0 column wise sum
#axis = 1 row wise sum
brr = np.array([[11,34,56],[1,2,3]])
print("column wise sum",np.sum(brr,axis=0)) 
print("row wise sum",np.sum(brr,axis=1)) 

##cumulative operations

crr = np.array([1,4,6,7])
#cumsum-->(1,(1+4),(1+4+6),(1+4+6+7))
print("THE CUMULATIVE SUM OF ARRAY IS ",np.cumsum(crr))
print("THE CUMULATIVE MULTIPLICATION IS ",np.cumprod(crr))
#THE POSITINS OF NONZERO ELEMENTS
print("THE NONZERO ELEMENT'S POSITION OF THE ARRAY IS ",np.nonzero(crr))

##CONDITIONAL BASED CHOICES

result = np.where(crr<6,"low","high")#where
print(result)
#argwhere--> row column position of 2D arrays
crr2 = np.array([[1,20,3],[5,2,9]])
result2 = np.argwhere(crr2>4)
print(result2)
#to get number between two specific number
#LOGICAL AND
mask = np.logical_and(crr>=1,crr<=6)
print(mask)
result3 = crr[mask]
print(result3)
#LOGICAL OR
mask2 = np.logical_or(crr2>6,crr2<=1)
print(mask2)
result4 = crr2[mask2]
print(result4)

##BRODCASTING
#SCALER QUANTITY ACTUALLY 1D ARRAY
image = np.array([[239,43],[290,301]])
brightness = image + 50
print(brightness)

##vectorized function

#np.vectorize()->convert a regular function to be applied in array
def square(X):
 return X*X
sq = np.vectorize(square)
print("THE SQUARE OF ELEMENTS IN ARRAY ",sq(arr))

##FINDING MISSING VALUES

a = np.array([1,3,np.nan,7])#np.nan->null(not a number)
#similarly np.inf and -np.inf is used for + or - infinite
#np.isnan,np.isinf,np.isfinite these are used to detect
#any null value, infinitevalue or finite value
print(np.isnan(a))
print(np.isinf(a))
print(np.isfinite(a))
#if we want to check null and infinite value together 
#we can use logical and 
mask5=np.logical_or(np.isnan(a),np.isinf(a))
b=a[mask5]
print("THE FALSE VALUES ARE ")
print(mask5)
print(b)
#TO CHANGE + INFINITY BY LARGEST REAL NUMBER 
# Same for negative infinity 
# null values are replaced with zeros
new_a= np.nan_to_num(a);
print(new_a)