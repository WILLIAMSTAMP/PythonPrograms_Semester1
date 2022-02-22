# Payroll Formula - Widgets.Inc
# Written by: William Stamp

# Employee Inputs
EmployeeName = input("Enter Employees Name:  ")

# Wicgets Produced Each Day
MONHOURS = float(input("Enter Hours Worked Monday  "))
WPMON = int(input("Enter Widgets Produced Monday:  "))
TUEHOURS = float(input("Enter Hours Worked Tuesday:  "))
WPTUE = int(input("Enter Widgets Produced Tuesday:  "))
WEDHOURS = float(input("Enter Hours Worked Wednesday:  "))
WPWED = int(input("Enter Widgets Produced Wednesday:  "))
THUHOURS = float(input("Enter Hours Worked Thursday:  "))
WPTHU = int(input("Enter Widgets Produced Thursday:  "))
FRIHOURS = float(input("Enter Hours Worked Friday:  "))
WPFRI = int(input("Enter Widgets Produced Friday:  "))
# Constants
INCOME_TAX = 0.21
CPP = 0.0494
EI = 0.0106
UNION_DUES = 15.00
COMMISSION_RATE = 0.35
REG_PAY_RATE = 17.50
INC_CPP_EI = 0.2701
# Calculations
# Total Hours Worked
TotalHoursWorked = MONHOURS + TUEHOURS + WEDHOURS + THUHOURS + FRIHOURS
# Calculate Regular Pay
RegularPay = REG_PAY_RATE * TotalHoursWorked
# Calculate Total Widgets Produced
TWP = int(WPMON + WPTUE + WPWED + WPTHU + WPFRI)
# Calculate Commission From Widgets Produced
CommEarned = (COMMISSION_RATE * TWP)
# Calculate Gross Bi-Weekly Pay
GrossPay = RegularPay + CommEarned
# Calculate Deductions
Deduct = (float(INC_CPP_EI) * float(GrossPay)) - int(15.00)
DeductDsp = "${:,.2f}".format(Deduct)
# Display
Invoice = 123
Date = "18-01-2022"
Address = "25 Simms Street"
Address2 = "St.John's, NL."
Address3 = "A1B2A9"
print("Hours Worked Monday:", MONHOURS)
# Calculate Net Pay
NetPay = (GrossPay - Deduct)
NetPayDisp = "${:,.2f}".format(NetPay)
# Display
print()
print(" "*29,  "GADGETS .INC")
print(" "*27, "108 Topsail Road")
print(" "*29, "709-555-5555")
print("Invoice#:{:<9}                                              Date:{:<5}".format(Invoice, Date))
print("--------------------------------------------------------------------------------")
print(EmployeeName)
print(Address)
print(Address2)
print(Address3)
print()
print("Hours Worked Monday:    {:<5}             Widgets Produced:   {:<5} ".format(MONHOURS, WPMON))
print("Hours Worked Tuesday:   {:<5}             Widgets Produced:   {:<5} ".format(TUEHOURS, WPTUE))
print("Hours Worked Wednesday: {:<5}             Widgets Produced:   {:<5} ".format(WEDHOURS, WPWED))
print("Hours Worked Thursday:  {:<5}             Widgets Produced:   {:<5} ".format(THUHOURS, WPTHU))
print("Hours Worked Friday:    {:<5}             Widgets Produced:   {:<5} ".format(FRIHOURS, WPFRI))
print("---------------------------------------------------------------------------------")
print("Total Hours Reported:  ", TotalHoursWorked, "                  Regular Pay:   ${:,.2f}".format(RegularPay))
print("Total Widgets Produced:", TWP,  "Commission Earned:  ${:>20,.2f}  ".format(CommEarned))
print("                                                    Total :   ${:,.2f}".format(GrossPay))
print("Deductions")
print("--------------------------------")
print("Union Dues:  -$15.00")
print("Income Tax:  -21%")
print("CPP:         -4.95%")
print("EI:          -1.6%")
print("--------------------------------")
print("Gross Earnings:         ${:,.2f}".format(GrossPay))
print("Total Deductions:       {:<5}                     NetPay:   {:<9}".format(DeductDsp, NetPayDisp))
