import numpy as np

##concatenation

arr = np.array([1,3])
brr = np.array([5,8])
crr = np.concatenate((arr,brr))
print(crr)

##STACK

arr1=np.array([[23,45,56],[78,88,66]])
arr2=np.array([[22,33,44],[1,3,5]])
# vertical stack
vstk = np.vstack((arr1,arr2))
print(vstk)
#horizontal stack
hstk = np.hstack((arr1,arr2))
print(hstk)
#stack(axis->0,hstack) , (axis->1,vstack)
print(np.stack((arr1,arr2),axis=1))

##spliting of array 

srr = np.split(hstk,2)#it split rows(always in equal part)
print(srr)
#similarly there was vsplit and hsplit(you can try)

##REPEATING (any dimension to 1 dimension result)

rrr = np.repeat(arr1,2)
print(rrr)
ttt = np.tile(arr1,2)#tile(dimension will bew same)
print(ttt)
