marks=eval(input("Enter the Marks"))
if(marks<40):
    print("Fail:Better Luck Next Time")
elif(marks<50):
    print("Pass Class")
elif(marks<60):
    print("Second Class")
elif(marks<80):
    print("First Class")
elif(marks<=100):
    print("Distinction")
else:
    print("Invalid Marks")