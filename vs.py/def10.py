def count_up_low(n):
    up=low=0
    for i in n:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1

    return up,low

a=input("Enter the string")
w,y=count_up_low(a)
print(f"count of upper {w}")
print(f"count of lower {y}")
