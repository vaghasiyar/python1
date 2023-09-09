unit = int(input("Enter the consumed units: "))

if unit <= 100:
    bill = 50 + (unit * 0.60)
elif unit>100 and unit<300:
    bill = 50 + 60 + ((unit - 100) * 0.80)
elif unit>300:
    bill = 50 + 60 + 160 + ((unit - 300) * 0.90)
if bill > 300:
    charge = (bill - 300) * 0.15
    surcharge = bill + charge
    print("Electricity Bill:", surcharge)
else:
    print("Electricity Bill:", bill)
