import random as ran 
import string
alpha=string.ascii_letters
digit=string.digits
password=''
for i in range (6):
    if i in (1,3,5):
        password=password+ran.choice(alpha)
    else:
        password=password+ran.choice(digit)

print(password)