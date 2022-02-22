# NL Power Company
# Written by: William Stamp on Jan 27 2021

COST_UNDER_100 = .073
COST_OVER_100 = .069
EARLY_PAY_DIS_500 = .03
EARLY_PAY_DIS_PLUS = .01
HST = .15

# Input Data
CusName = input("Enter the customers name:  ")
StAdd = input("Enter the street address:  ")
LastMeterReading = int(input("Enter The last meter reading:  "))
CurMeterReading = int(input("Enter the current meter reading:  "))

# Calculations
# Monthly Charge + Discount + HST
MonthlyKWH = CurMeterReading - LastMeterReading
if MonthlyKWH <= 100:
    Charges = (MonthlyKWH * COST_UNDER_100) * 10
else:
    Charges = (MonthlyKWH * COST_OVER_100) * 10

# Discount
if Charges > 500:
    Discount = EARLY_PAY_DIS_500 * Charges
else:
    Discount = EARLY_PAY_DIS_PLUS * Charges
# SubTotal
SubTotal = Charges - float(Discount)


# Taxes
Taxes = SubTotal * HST
TotalCharges = SubTotal + Taxes

print("Customers Name:  ", CusName)
print("Street address:  ", StAdd)
print()
print("Total KWH used:  ", MonthlyKWH)
print("Usage Charges:     ${:>5,.2f}".format(Charges))
print("Discount:         -${:>5,.2f}".format(Discount))
print("SubTotal:          ${:>5,.2f}".format(SubTotal))
print("HST:               ${:>4,.2f}".format(Taxes))
print()
print("Your Bill:         ${:>5,.2f}".format(TotalCharges))
