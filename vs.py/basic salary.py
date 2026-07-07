basic=eval(input("Enter The Salary"))
if(basic<1500):
    hra=basic*0.10
    da=basic*0.25
else:
    hra=500
    da=basic*0.50
gross=basic+hra+da
print(f"Gross salary={gross}")