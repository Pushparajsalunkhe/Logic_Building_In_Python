a=[10,4.5,'python',True,56,21]
n=0
i=0
while i< len(a):
    n=i-len(a)
    print(i,a[i],type(a[i]),n)
    i+=1