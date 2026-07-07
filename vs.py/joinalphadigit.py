s=input("Enter the string")
alpha=''
digit=''
for ch in s:
    if ch.isalpha():
        alpha+=ch
    else:
        digit+=ch
print(alpha)
print(digit)

out=''.join(sorted(alpha)+sorted(digit))
print(out)