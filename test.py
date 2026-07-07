import itertools as itr 
word=input('Enter the string')
for ch in itr.permutations(word):
    print(''.join(ch))