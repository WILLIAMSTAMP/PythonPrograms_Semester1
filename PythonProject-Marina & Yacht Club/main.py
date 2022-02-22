
EVEN_SITE_FEE = 80.00
ODD_SITE_FEE = 120.00
ALT_MEM_COST = 5
WK_CLEAN_SVC_COST = 50.00
V_SURVEIL_SVC_COST = 35.00
STD_MON_DUES = 75.00
EXEC_MON_DUES = 150.00
PROC_FEE = 59.99
CNCL_FEE = .6
TAX = .15
# IF STATEMENTS / MEMBER TYPE
E = "Executive"
S = "Standard"
# IF STATEMENTS / Yes | No
Y = "Yes"
N = "No"
SiteNum = int(input("Enter the Site Number (1-100):  "))
MemName = input("Enter the Member Name:  ").title()
StAdd = input("Enter the Street Address:  ").title()
City = input("Enter the City: ").title()
Prov = input("Enter the Province:  ").title()
PostCode = input("Enter the Postal Code:  ").title()
PhNum = input("Enter the Phone Number:  ")
CellNum = input("Enter the Cell Number:  ")
MEMTYPE = str(input("Enter the Membership Type (E = Executive / S = Standard):  ")).title()
NumAltMem = int(input("Enter the Number of Family / Guests Members:  "))
WkCleanSvc = str(input("Would you like weekly Cleaning services?:  (Y/N)  ")).title()
VSurvailSvc = str(input("Would you like video surveillance ?  (Y/N):  ")).title()
MemTypeCost = 0
if MEMTYPE == "E":
    MemTypeCost = EXEC_MON_DUES
elif MEMTYPE == "S":
    MemTypeCost = STD_MON_DUES
MembershipDsp = 0
if MEMTYPE == "E":
    MembershipDsp = "Executive"
if MEMTYPE == "S":
    MembershipDsp = "Standard"
# Calculations
# SiteNumFee
SiteNumCost = 0
if SiteNum % 2 == 0:
    SiteNumCost = EVEN_SITE_FEE
elif SiteNum % 2 == 1:
    SiteNumCost = ODD_SITE_FEE
# Family & Guests
AltMemTotal = (NumAltMem * ALT_MEM_COST)
# Weekly Cleaning Service Fee
WkCleanSvcDsp = 0
if WkCleanSvc == "Y":
    WkCleanSvc = WK_CLEAN_SVC_COST
    WkCleanSvcDsp = "Yes"
elif WkCleanSvc == "N":
    WkCleanSvc = 0
    WkCleanSvcDsp = "No"
# Surveillance Fee
VSurvailSvcDsp = 0
if VSurvailSvc == "Y":
    VSurvailSvc = V_SURVEIL_SVC_COST
    VSurvailSvcDsp = "yes"
elif VSurvailSvc == "N":
    VSurvailSvc = 0
    VSurvailSvcDsp = "No"

# Site Charge + Guests
SiteChrg = (AltMemTotal + SiteNumCost)
# Extra Charges
ExtraChrg = WkCleanSvc + VSurvailSvc
# SubTotal
SubTotal = SiteChrg + ExtraChrg
# Taxes
SalesTax = SubTotal * .15
# Total Monthly Charges
TotalMonChgs = SiteChrg + ExtraChrg + SalesTax
TotalMonFees = TotalMonChgs + MemTypeCost
TotalYearFee = TotalMonFees * 12
MonthlyPay = (TotalYearFee + PROC_FEE) / 12
CNCL_FEE_Dsp = TotalYearFee * CNCL_FEE
print()
print("     St. John's Marina & Yacht Club")
print("         Yearly Member Reciept")
print("_________________________________________")
print()
print("Client Name and Address:")
print()
print(MemName.title())
print(StAdd)
print("{:>1},{:>1},{:>1} ".title().format(City.title(), Prov.upper(), PostCode.upper()))
print()
print("Phone:", PhNum, "(H)")
print("      ", CellNum, "(C)")
print()
print("Site #: {:>3}   Membership Type: {:>2}".format(SiteNum, MembershipDsp))
print()
print("Alternate members:{:>22}".format(NumAltMem))
print("Weekly site cleaning:{:>19}".format(WkCleanSvcDsp))
print("Video surveillance:{:>21}".format(VSurvailSvcDsp))
print()
print("Site Charges: {:>26,.2f}".format(SiteChrg))
print("Extra Charges: {:>25,.2f}".format(ExtraChrg))
print("                            ------------")
print("Subtotal: {:>30,.2f}".format(SubTotal))
print("Sales Tax(HST): {:>24,.2f}".format(SalesTax))
print("                            ------------")
print("Total Monthly Charges: {:>17,.2f} ".format(TotalMonChgs))
print("Monthly Dues: {:>26,.2f}".format(MemTypeCost))
print("                            ------------")
print("Total Monthly Fee: {:>21,.2f}".format(TotalMonFees))
print("Total Yearly Fee: {:>22,.2f}".format(TotalYearFee))
print()
print("Monthly payment: {:>23,.2f}".format(MonthlyPay))
print("_________________________________________")
print("Issued: 2021-01-31")
print("HST Reg No: 123-45-6789-1011-1213")
print()
print("Cancellation Fee: {:>22,.2f}".format(CNCL_FEE_Dsp))
