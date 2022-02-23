
# Honest Harry Used Cars - Sales Program
# Written by: William Stamp
# Date: Feb 13 2022
import datetime
from datetime import date
# Constants
HST = .15
LicFee_75 = 75.00
LicFee_165 = 165.00
TransFee_Rate = 0.01
TransFee_LxRate = 0.016
Fin_Fee = float(39.99)
date_format = "%Y-%m-%d"

# User Inputs
while True:
    try:
        Inv_Date = input("Enter the date of the sales invoice (YYYY-MM-DD): ")
        Inv_Date = datetime.datetime.strptime(Inv_Date, "%Y-%m-%d")
    except:
        print("Date of the sales invoice is not a valid format - please re-enter.")
    else:
        break

while True:
    try:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ_ abcdefghijklmnopqrstuvwxyz-' ")
        CusFName = input("Please enter your first name: ").title()
    except:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    if CusFName == "":
        print("Name cannot be blank - Please enter your name. ")
    elif set(CusFName).issubset(allowed_char) == False:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break

while True:
    try:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
        CusLName = input("Please enter your last name: ").title()
    except:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    if CusLName == "":
        print("Name cannot be blank - Please enter your name. ")
    elif set(CusLName).issubset(allowed_char) == False:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break

while True:
    try:
        allowed_char = set("1234567890-")
        PhNum = input("Please enter your phone number including the area code. -(Digits only/No spaces):")
    except:
        print("Phone number contains invalid characters - Please try again. ")
    if PhNum == "":
        print("Phone Number Cannot be blank - Please enter your phone number. ")
    if PhNum.isdigit() == False:
        print("Phone number contains invalid characters - Please try again. ")
    if len(PhNum) != 10:
        print("Home Phone number must include area code and should be 10 digits - please try again. ")
    else:
        break

while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz,0123456789-.'")
    StAdd = input("Enter your street address: ").title()
    if StAdd == "":
        print("Street address cannot be blank - Please try again. ")
    elif set(StAdd).issubset(allowed_char) == False:
        print("Street address contains invalid characters - Please try again. ")
    else:
        break

while True:
    try:
        allowed_char = set(("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'"))
        City = input("Enter the City:").title()
    except:
        print("City name contains invalid characters - Please re-enter. ")
    if City == "":
        print("City name cannot be blank. Please re-enter. ")
    elif set(City).issubset(allowed_char) == False:
        print("City name contains invalid characters - Please re-enter. ")
    else:
        break

while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
    Prov = input("Please enter name of province: ")
    if set(Prov).issubset(allowed_char) == False:
        print("Province name contains invalid characters - Please try again. ")
    elif Prov == "":
        print("Province name cannot be blank - Please enter Province name. ")
    else:
        break

while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890")
    PostCode = input("Please enter your postal code  (A1A1A1): ").capitalize()
    if set(PostCode).issubset(allowed_char) == False:
        print("Postal Code contains invalid characters - Please Re-enter.")
    elif PostCode == "":
        print("Postal code cannot be blank - Please enter postal code. ")
    else:
        break

while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890")
    LicPlate = input("Enter the licence plate number (LLL000): ").capitalize()
    if set(LicPlate).issubset(allowed_char) == False:
        print("Licence plate number Contains invalid characters - Please re-enter. ")
    elif LicPlate == "":
        print("Licence plate number cannot be blank - Please re-enter.")
    elif len(LicPlate) != 6:
        print("Licence plate must be 6 characters - Please re-enter.")
    elif not LicPlate[0:3].isalpha():
        print("Licence plate number must start with 3 letters - Please re-enter.")
    elif not LicPlate[3:6].isdigit():
        print("Licence plate number must end with 3 numbers - Please re-enter.")
    else:
        break

while True:
    try:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.,-")
        VehicleMake = input("Enter the make of the vehicle.  Examples -(Honda, Dodge, Toyota, etc.): ")
    except:
        print("Vehicle make contains invalid characters - Please re-enter vehicle year:")
    if set(VehicleMake).issubset(allowed_char) == False:
        print("Vehicle make contains invalid characters - Please re-enter vehicle year:")
    if VehicleMake == "":
        print("Vehicle make cannot be empty - Please enter the vehicle make.")
    else:
        break

while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 abcdefghijklmnopqrstuvwxyz,'.-")
    VehicleModel = input("Enter the vehicle model. Examples -(Accord, Ram 1500, 4Runner etc.): ").title()
    if VehicleModel == "":
        print("Vehicle model cannot be blank - Please re-enter. ")
    elif set(VehicleMake).issubset(allowed_char) == False:
        print("Vehicle make contains invalid characters - Please re-enter. ")
    else:
        break

while True:
    allowed_char = set("1234567890")
    VehicleYear = input("Enter the manufacture year of the vehicle  -(YYYY): ")
    if VehicleYear == "":
        print("Vehicle year cannot be blank - Please enter the vehicle year: ")
    elif VehicleYear < "1900" or VehicleYear > "2023":
        print("Please enter a valid year: ")
    elif VehicleYear.isdigit() == False:
        print("Vehicle year contains invalid characters - Please re-enter vehicle year:")
    else:
        break

while True:
    try:
        allowed_char = set("1234567890.")
        SellPrice = float(input("Enter the sell price of the vehicle   ($99999.99): "))
        SellPrice = str(SellPrice)
    except:
        print("Sell Price is invalid")
    if float(SellPrice) > 50000.00:
        print("Sell Price cannot exceed $50,000.00 - Please re-enter the sell amount.")
    elif set(SellPrice).issubset(allowed_char) == False:
        print("Sell price contains invalid characters - Please re-enter the sell price. ")
    elif SellPrice == "":
        print("Sell price cannot be blank - Please re-enter.")
    else:
        break
SellPrice = float(SellPrice)

while True:
    try:
        allowed_char = set("1234567890.")
        TradeIn = float(input("Enter the Trade-In value of the vehicle   ($99999.99). "))
        TradeIn = str(TradeIn)
    except:
        print("Trade-In value is invalid - Please re-enter. ")
    if float(TradeIn) > 50000.00:
        print("Trade-In value cannot exceed $50,000.00 - Please re-enter the Trade-In value. ")
    elif set(TradeIn).issubset(allowed_char) == False:
        print("Trade-In value contains invalid characters - Please re-enter the Trade-In value. ")
    elif TradeIn == "":
        print("Trade-In value cannot be blank - Please re-enter. ")
    else:
        break
TradeIn = float(TradeIn)

while True:
    try:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,-.'")
        SalesPerson = input("Enter the salespersons name: ").title()
    except:
        print("Salespersons name cannot contain invalid characters - Please re-enter your name. ")
    if SalesPerson == "":
        print("Salespersons name cannot be blank - Please enter your name. ")
    elif set(SalesPerson).issubset(allowed_char) == False:
        print("Salespersons name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break

while True:
    allowed_char = set("1234567890")
    CCardNum = input("Please enter the credit card number  (9999-9999-9999-9999): ")
    if len(CCardNum) > 16 or len(CCardNum) < 16:
        print("Credit card number must be 16 digits long - Please re-enter. ")
    elif not set(CCardNum).issubset(allowed_char):
        print("Credit card number contains invalid characters - Please re-enter. ")
    else:
        break

print("# Years          # Payments          # Financing Fee          Total Price         Monthly Payment")
print("--------------------------------------------------------------------------------------------------")

for Years in range(1, 5):
    New_Price = float(SellPrice) - float(TradeIn)
    Payments = 12 * Years
    FinanceFee = Years * Fin_Fee
    New_Price += FinanceFee
    Mon_Pay = New_Price / Payments
    Fin_FeeDsp = "${:,.2f}".format(Fin_Fee * Years)
    New_PriceDsp = "${:,.2f}".format(New_Price)
    Mon_PayDsp = "${:,.2f}".format(Mon_Pay)
    print("{:>5} {:>17} {:>23}   {:>22}   {:>18}".format(Years, Payments, Fin_FeeDsp, New_PriceDsp, Mon_PayDsp))
while True:
    print()
    Choice = int(input("Enter the payment schedule you want to follow  (1-4):"))
    print()
    if Choice == Choice:
        Years = Choice
        New_Price = SellPrice - TradeIn
        Payments = 12 * Choice
        FinanceFee = Years * Fin_Fee
        New_Price += FinanceFee
        Mon_Pay = New_Price / Payments
        Fin_FeeDsp = "${:,.2f}".format(Fin_Fee * Choice)
        New_PriceDsp = "${:,.2f}".format(New_Price)
        Mon_PayDsp = "${:,.2f}".format(Mon_Pay)
    if SellPrice <= 5000.00:
        LicFee = LicFee_75
    elif SellPrice > 5000.00:
        LicFee = LicFee_165
    if SellPrice <= 20000.00:
        Trans_Fee = TransFee_Rate * SellPrice
    elif SellPrice > 20000.00:
        Trans_Fee = TransFee_LxRate * SellPrice
    else:
        break
    break

TradeInDsp = "${:,.2f}".format(TradeIn)
Mon_PayDsp = New_Price / Payments
PaymentsDsp = 12 * Choice
Taxes = SellPrice * HST
Trans_FeeDsp = "${:,.2f}".format(Trans_Fee)
LicFeeDsp = "${:,.2f}".format(LicFee)
PriceAfterTradeDsp = "${:,.2f}".format(SellPrice - TradeIn)
Mon_PayDsp = "${:,.2f}".format(New_Price / Payments)
SellPriceDsp = "${:.2f}".format(SellPrice)
ReceiptDsp = f"{CusFName.upper()[0]}{CusLName.upper()[0]}-{LicPlate.upper()[0:3]}-{PhNum[0:4]}"
TaxesDsp = "${:.2f}".format(SellPrice * HST)
Tot_Sales_Cost = SellPrice - TradeIn + LicFee + Taxes + Trans_Fee
Tot_Sales_CostDsp = "${:,.2f}".format(Tot_Sales_Cost)
today = date.today()
InvoiceDatePlus10Dsp = InvoiceDate + datetime.timedelta(days=10)

# Customers Display
print("        Honest Harry Car Sales  ")
print("       Used Car Sale and Receipt ")
print()
print("Invoice Date:", InvoiceDate.strftime("%b %d, %Y "))
print("Receipt No:", ReceiptDsp.upper())
print()
print("Sales Person:", SalesPerson.title())
print("Sold to: ")
print("    "f"{CusFName.upper()[0]}.", CusLName.title())
print("   ", StAdd.title())
print("   ", City.title(), ",", f"{Prov.upper()[0]}"f"{Prov.upper()[8]}", ",", PostCode.upper())
print()
print("Car Details: ")
print("          ", VehicleYear, VehicleMake.upper(), VehicleModel.upper())
print("-----------------------------------------")
print("Sale Price:", "{:>29}".format(SellPriceDsp))
print("Trade Allowance: ", "{:>23}".format(TradeInDsp))
print("Price after Trade: ", "{:>21}".format(PriceAfterTradeDsp))
print("                              -----------")
print("HST:",      "{:>36}".format(TaxesDsp))
print("Licence Fee:  {:>27}".format(LicFeeDsp))
print("Transfer Fee:  {:>26}".format(Trans_FeeDsp))
print("                              -----------")
print("Total Sales Cost: {:>23}".format(Tot_Sales_CostDsp))
print("-----------------------------------------")
print("Terms: {:>2}              Total Payments:{:>3}".format(Choice, PaymentsDsp))
print("Monthly Payment: {:>24}".format(Mon_PayDsp))
print("First Payment Date: {:>21}".format(InvoiceDatePlus10Dsp.strftime("%d-%b-%y")))
print()
print("         Honest Harry Car Sales  ")
print("   Best Used cars at the best price ! ")
