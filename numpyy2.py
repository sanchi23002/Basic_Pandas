import numpy as np

#as numpy is c function, so in array it store onetype data
arr = np.array([1,2,3,4])
brr = np.array([1,2,3.14,4])
crr = np.array(["sanchi",43,4.34])
print(arr)
print(brr)
print(crr)
print(type(crr))
print(arr.dtype)# it shows datatype

#for typecasting of datatype we use 
arr2 = np.array([2.3,4.5,2,1], dtype=int)
print(arr2)
#for loading typecasted value in a new array,use astype
new_brr = brr.astype(int)
print(new_brr)

brr2 = np.array([[2,3],[3,4]])
print(brr2.ndim) #3D aspect
print(brr2.shape) #(row,column)
print(brr2.size)#no. of elements
print(brr2.itemsize) # size of bit of one element

#reshape (we can reshape any dimentional array just give
#new dimension)
crr2 = np.array([1,2,3,4,5,6,7,8,9,11,12,23])
new_crr = crr2.reshape(3,4)
print(new_crr)
new_crr2= new_crr.reshape(2,6)
print(new_crr2)
#ravel is the opposite of reshape(any dimension to one dimension)
#same work is done by flatten
#the diff is ravel effect real array, but flatten does not
new_crr3=new_crr2.ravel()
print(new_crr3)
new_crr3[0]=100
print(new_crr2)# first element is 100
new_crr4=new_crr2.flatten()
new_crr4[0]=500
print(new_crr2)#no change



