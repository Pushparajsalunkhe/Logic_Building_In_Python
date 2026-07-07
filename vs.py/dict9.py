d=eval(input("Enter the dict{}:"))
k=eval(input("Enter the key"))
if k in d:
    v=d.pop(k)
    print(f"{k}:{v} is removed")
    print(d)
else:
    print(f"{k} is not present in the dict")
    