s=input("Enter the sting")
b={}.fromkeys(s,0)
for k in b:
    b[k]=s.count(k)


out=''
for k,v in b.items():
    out=out+k+str(v)


print(out)