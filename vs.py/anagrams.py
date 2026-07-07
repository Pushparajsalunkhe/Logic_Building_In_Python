import random as ran
s='word'
a=list(s)
b=[]
while True:
    ran.shuffle(a)
    w=''.join(a)
    if w not in b:
        b.append(w)
        if len(b)==5:
            break
for w in b:
    print(w)