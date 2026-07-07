import numpy as np
#input form the user
arr=[]
a=int(input("Enter the size :"))
for i in range(a):
    val=int(input("Enter the number :"))
    arr.append(val)
    b=np.array(arr)
print(b)
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
c=np.eye(3)
print(c)
d=np.ones(2)
print(d)
e=np.zeros(2)
print(e)
p=np.random.randint(1,100,9)
print(p)


