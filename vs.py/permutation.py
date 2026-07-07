import itertools as itr
col=eval(input("Enter the list"))
for ch in itr.permutations(col,3):
    print(ch)