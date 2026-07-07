s=eval(input("Enter the list"))
out={}
for a in s:
    k,v=a.values()
    if k in out:
        out[k]+=v
    else:
        out[k]=v
print(out)