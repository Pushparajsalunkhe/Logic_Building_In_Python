s1=input("Enter the string1:")
s2=input("Enter the string2:")
if set(s1 ) <= set(s2):
    print(f"All chars of '{s1} apperes in '{s2}")
else:
    print(f"All chars of '{s1} does not apperes in'{s2}")