n=int(input("enter the number"))
x=1
y=1
for i in range(n):
    t=x/y
    print(t,end="\t")
    x+=1
    y*=2
