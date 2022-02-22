# Edsel Rentals
# Written by: William Stamp
# Date Written: Jan 15, 2022
# Constants
DAILY_RENTAL_RATE = int(35)
RATE_PER_KLM = float(.10)
HST_RATE = 1.15

# User Input
UserName = input("Enter Your Name: ")
PhoneNum = input("Enter Your Phone Number: ")
NumDaysRented = int(input("Enter The Number Of Days Rented "))
StartKms = float(input("Enter The Odometer Kms to nearest klm of the vehicle at PICKUP "))
EndKms = float(input("Enter the odometer Kms to nearest Klm of the vehicle at DROP OFF "))

# Calculate Total Daily Vehicle Rental Rate
DailyVehicleRentalRate = DAILY_RENTAL_RATE * NumDaysRented
# Calculate Total Kms
TotalKms = EndKms - StartKms
# Calculate Total Klm Cost
TotalKlmCost = TotalKms * RATE_PER_KLM
# Total Cost Before Taxes
TotalCostBeforeTaxes = NumDaysRented * DAILY_RENTAL_RATE + TotalKlmCost
# Total Cost After Taxes
TotalCostAfterTaxes = TotalCostBeforeTaxes * HST_RATE

# Display Custom Info
print()
print("Customer:     ", UserName)
print("Phone Number: ", PhoneNum)
print()
print("Standard Daily Rate = $35/Day ", "$", DailyVehicleRentalRate)
print("Rental Period/Days: ", NumDaysRented)
print()
print("Rate/Klm: $0.10/Klm")
print("Kilometers Traveled:", format(TotalKms, ".0f"))
print("Total Kilometer Cost:", "$", format(TotalKlmCost,".2f"))
print()
print("Total Before Taxes: ", "$", format(TotalCostBeforeTaxes,".2f" ))
print("HST: 15%")
print()
print("Your Total:  ", "$" , format(TotalCostAfterTaxes,".2f" ))
