age=int(input("Enter the Age"))
if(age<18):
    print("Child")
elif(age<65):
    print("Adult")
elif(age<120):
    print("Senior citizen")
else:
    print("invalid age")