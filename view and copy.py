import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
arr1=arr[1:8].view()
arr1[:]=0
print(arr)
arr2=np.array([1,2,3,4,5,6,7,8,9])
arr3=arr2[1:8].copy()
arr3[:]=0
print(arr2)

