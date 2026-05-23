import numpy as np

##arithmatic operations 

arr = np.array([1,2,3,4])
brr = np.array([2,5,6,7])
#addition
print("THE ADDITION IS ",arr+brr)
#substraction
print("\n THE SUBSTRACTION IS ",brr-arr)
#multiplication
print(arr*brr)
#division(it is normal division, give floating values)
print(brr/arr)
#division(values in integer)
print(brr//arr)
#modulus for remainder
print(brr%arr)
#exponent(power)remember one array is used
print(arr**3)

##universal function
##This are one array functions 

#square root
crr = np.sqrt(arr)
print(crr)
#exponential(e^x where x is any integer)
print(np.exp(arr))
crr2 = np.exp([2,3,4])
print(crr2)
#sine functions
angles = np.array([0,np.pi/2,np.pi])
print(np.sin(angles))

##Indexing and slicing

a = np.array([2,3,4,5,6])
#negative indexing
print(a[-1])
b = a[-1:-4:-1]#6-> -1, 5-> -2 ,4-> -3, and so on
print(b)
#skipping one one element
new_a= a[::2]
print(new_a)
#multidimentional slicing
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
new_arr2 = arr2[0:2 ,0:3]
print("multidimentional array ",new_arr2)
print(arr2[1: ,1:])
#np.take->build in function to perform indexing and slicing
ind = [0,2]
print("THE 0TH AND 2TH INDEX ELEMENTS ARE",np.take(a,ind))

##ITERATION(using nditer())

#for numpy arrays we can't use for loop
err = np.array([[1,2],[3,4]])
for x in np.nditer(err):
 print(x, end=" ")#instead of curly braces it relies on blankspace
#ndenumerate--> both index+value
for i,x in np.ndenumerate(err):
    print("THE",i,"th ELEMENT IS",x)
    
##VIEWS AND COPYS 

err2=np.array([1,2,3,4,5])
v = err2[1:]  #view
v[2]=300
print(err2)
c = err2[1:].copy()# copy
c[1]=800
print(err2) #no change

##transpose of matrix

trr=np.array([[1,2,3],[4,5,6]])
new_trr=np.transpose(trr)
print("THE TRANSPOSE MATRIX IS ",new_trr)
#swapaxes--> swap two specific axes in a matrix
srr = np.array([[[10,20,30],[23,45,56]]])
print(srr.shape)
swap = np.swapaxes(srr,0,1)
print(swap)
print(swap.shape)