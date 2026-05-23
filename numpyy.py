import numpy as np
arr = np.array([1,2,3])
print(arr.ndim)# dimension of a array
#ploting number from any range we use arange 
range = np.arange(1,10)#1,2,3,4,5,6,7,8,9
print(range)
#for skipping one number do 
range2 = np.arange(1,10, 2)# start , stop, step
print(range2)
#for getting equal diition number between two number
brr = np.linspace(0,1, 10)#start , stop,number of vaiues
print(brr)
#for getting power of 10 in equal division
crr = np.logspace(1,3,3)
print(crr)
# np.zeros -> an array full of zeros
arr3 = np.zeros(5)
print(arr3)

#for creating 2D array numpy is really good
arr4 = np.zeros([2,3])# 2 rows , 3 coloums
print(arr4)
#similarly if we want to initialize array with 1 
arr5 = np.ones([3,4])# 3 rows , 4 coloums
print(arr5)
# we can create any initialize with any number 
new_arr2 = np.full(10,2)#we can use floating point also here
print(new_arr2)
new_arr3 = np.full([3,4],3)#2D array
print(new_arr3)

err = np.empty([2,3])# for uninitialized array
print(err)
# for getting random floating  points in between 0 and 1
# as border are predefined , we just have to give dimensions
#it is diff from other 2D array  {([]) is wrong here}
err2 = np.random.rand(3,4)
print(err2)
#np.random.randn()->random float from standardnormal distribution
# normal diatribution means avg =0 , standard deviation=1
err3 = np.random.randn(2,3)
print(err3)
#to get random integer point in your defined range
err4 = np.random.randint(1,60,4)#start,stop,dimention
print(err4)
err5 = np.random.randint(1,60,[2,3])
print(err5)

