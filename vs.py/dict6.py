#print key but value is same value==user_value
d=eval(input("Enter the dict{}:"))
value=eval(input("Enter the value:"))
if value in d.values():
    for k,v in d.items():
        if v==value:
            print(k,end="\t")
else:
    print(f"{value} is not present")
