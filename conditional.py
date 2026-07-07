import numpy as np
arr=np.arange(1,16)
print(arr)
b=arr1=arr>10
print(arr1)
print(arr[b])
arr2=(arr%2==0)
print(arr[arr2])
arr[arr%2==0]=0
print(arr)
