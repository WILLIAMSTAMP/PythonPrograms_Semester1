# A program for The Gym to calculate the membership costs for new family memberships.
# Written by: William Stamp
# Date Written: Jan 13, 2022
# Define program constants.
FIRST_MEM_COST = 125.00
ALT_MEM_COST = 75.00
HST_RATE = .15
CANCEL_RATE = .60
# Gather required data from the user.
MemNum = input("Enter the membership number: ")
MemName = input("Enter the member name: ")
StAdd = input("Enter the member street address: ")
PhoneNum = input("Enter the member phone number: ")
NumMembers = int(input("Enter the number of family members: "))
# Perform required calculations.
MemCost = FIRST_MEM_COST + (NumMembers - 1) * ALT_MEM_COST
HST = MemCost * HST_RATE
TotMemCost = MemCost + HST
CancelFee = (MemCost * 3) * CANCEL_RATE
# Display output results for the user.
print()
print("Membership number:        ", MemNum)
print("Member name:              ", MemName)
print("Member street address:    ", StAdd)
print("Member phone number:      ", PhoneNum)
print("Number of family members: ", NumMembers)
print()
print("Membership cost:          $", (round(MemCost, 2)))
print("Sales tax (HST):          $", (round(HST), 2))
print("Total membership cost:    $", (round(TotMemCost, 2)))
print("Cancellation fee:         $", (round(CancelFee), 2))