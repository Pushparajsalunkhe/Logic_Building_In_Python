import random as ran 
Num=ran.randint(0,100)
count=5
while count>=1:
    Guess=int(input("Enter Guess Number: "))
    if Guess==Num:
        print("!...Congrats,You Have Win...!")
        break
    elif Guess>Num:
        print("You Are Above The Number")
    else:
        print("You Are Below The Number")
    count-=1
else:
    print("!...Game Is Over...!")