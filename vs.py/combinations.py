import itertools as itr 
col=eval(input("enter the list"))
for ch in itr.combinations(col,2):
    print(ch)