d=eval(input("Enter the dict {}"))
k=eval(input("Enter the key"))
if k in d:
    print(f"{k} is present with values {d[k]}")
else:
    print(f"{k} is not present in dictionary")