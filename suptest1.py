unit=int(input("enter the unit"))
total=charge=amt=0
if unit<=50:
    amt=unit*0.50
elif unit<=150:
    amt=25+(unit-50)*0.75
elif unit<=250:
    amt=100+(unit-150)*1.20
else:
    amt=220+(unit-250)*1.50
    charge=amt*20/100
    total=amt*charge
print("your total electricity bill is",total)
