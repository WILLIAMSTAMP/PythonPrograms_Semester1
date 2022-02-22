import datetime
RegRate = 85.00
HighSeasonRate = 105.00
HighSeasonMsg = "(High Season Rate applied)"
print()
print("The Hotel Reservation Program")
print()
while True:
    try:
        ArriveDate = input("Enter the arrival date:    (YYYY-MM-DD): ")
        ArriveDate = datetime.datetime.strptime(ArriveDate, "%Y-%m-%d")
    except:
        print("Arrival format is not a valid format - Please re-enter. ")
    else:
        break
while True:
    try:
        DepartDate = input("Enter the departure date:  (YYYY-MM-DD): ")
        DepartDate = datetime.datetime.strptime(DepartDate, "%Y-%m-%d")
    except:
        print("Date of departure is not a valid format - Please re-enter. ")
    else:
        if DepartDate <= ArriveDate:
            print("Departure date cannot be before arrival date - Please re-enter. ")
        else:
            break

HSStart = datetime.datetime(2022, 7, 1)
HSEnd = datetime.datetime(2022, 8, 31)

if int(ArriveDate >= HSStart and DepartDate <= HSEnd):
    NightlyRate = HighSeasonRate
else:
    NightlyRate = RegRate
TotalNights = (DepartDate - ArriveDate).days
TotalPrice = TotalNights * NightlyRate
TotalPriceDsp = " ${:,.2f}".format(TotalPrice)
ArriveDateDsp = "{:%B" " %d, %Y}".format(ArriveDate)
DepartDateDsp = "{:%B" " %d, %Y}".format(DepartDate)
print()
print("Arrival Date:     {:>5}".format(ArriveDateDsp))
print("Departure Date:   {:>3}".format(DepartDateDsp))
if NightlyRate == HighSeasonRate:
    print("Nightly Rate:     ${:>5,.2f} {:>5}".format(NightlyRate, HighSeasonMsg))
else:
    print("Nightly Rate:    {:>5} ".format(NightlyRate))
print("Total Nights: {:>5}".format(TotalNights))
print("Total price:     {:>5}".format(TotalPriceDsp))
print()
while True:
    Continue = input("Continue (Y/N): ").upper()
    if Continue == "N":
        break
print("Thank you for using The Hotel Reservation Program. Bye Bye.")
