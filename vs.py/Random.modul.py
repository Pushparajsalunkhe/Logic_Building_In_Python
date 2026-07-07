import random as ran
for i in range(5):
    print(ran.randint(100000,999999))


print("-"*30)
for j in range(5):
    print(ran.randint(0,9),
          ran.randint(0,9),
          ran.randint(0,9),
          ran.randint(0,9),
          ran.randint(0,9),
          ran.randint(0,9),sep=""
          )