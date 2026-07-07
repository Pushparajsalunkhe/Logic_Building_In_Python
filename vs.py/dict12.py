import operator as op
a=eval(input("enter the dict"))
s=sorted(a.items(),key=op.itemgetter(1),reverse=True) 
for k,v in s[:3]:
    print(k,v)