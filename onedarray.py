import numpy as np
a=[]
b=int(input("Enter the size :"))
for i in range(b):
    val=int(input("Enter the number :"))
    a.append(val)
    arr=np.array(a)
print(arr)
arr1=arr[2:4]
print(arr1)
arr2=arr[1:7]
print(arr2)
print(arr[0:7])
