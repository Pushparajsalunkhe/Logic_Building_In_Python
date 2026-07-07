a=eval(input("Enter the first number"))
b=eval(input("Enter the second number"))
c=eval(input("Enter the third number"))
if(a>b):
    if(a>c):
        print(f"largest ={a}")
    else:
        print(f"largest ={c}")
else:
    if(b>c):
        print(f"largest ={b}")
    else:
        print(f"largest ={c}")