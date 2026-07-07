import time
a=eval(input("Enter the list1:"))
b=eval(input('Enter the list2:'))
s=time.time()
out=[]
for i in a:
    if i in b:
        out.append(i)
c=time.time()
d=c-s
print(out)
print(d)



out=[i for i in a if i in b]
print(out)