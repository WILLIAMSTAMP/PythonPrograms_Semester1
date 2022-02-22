# Constants
import datetime
ExtraLiab = 75.00
ExtraPers = 90.00
ContentIns = 110.00
HST = 0.15
# User Data
while True:
    try:
        PolicyDate = input("Please enter the date:  (YYYY-MM-DD): ")
        PolicyDate = datetime.datetime.strptime(PolicyDate, "%Y-%m-%d")
    except:
        print("Date format is not a valid format - Please re-enter. ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
    CusFName = input("Please enter your name: ").title
    if CusFName == "":
        print("Name cannot be blank - Please enter your name. ")
    elif set(CusFName).issubset(allowed_char) == False:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
    CusLName = input("Please enter your name: ").title
    if CusLName == "":
        print("Name cannot be blank - Please enter your name. ")
    elif set(CusLName).issubset(allowed_char) == False:
        print("Customers name cannot contain invalid characters - Please re-enter your name. ")
    else:
        break
while True:
    HPhNum = input("Please enter your home phone number (___-___-____): ")
    if HPhNum.isdigit() == False:
        print("")
    elif len(HPhNum) != 10:
        print("Home Phone number must include area code and should be 10 digits - please try again: ")
    else:
        break
while True:
    CPhNum = input("Please enter your Cell phone number (___-___-____): ")
    if CPhNum.isdigit() == False:
        print("")
    elif len(CPhNum) != 10:
        print("Cell Phone number must include area code and should be 10 digits - please try again: ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz,0123456789-'")
    StAdd = input("Enter your street address: ").title
    if StAdd == "":
        print("Street address cannot be blank - Please try again. ")
    elif set(StAdd).issubset(allowed_char) == False:
        print("Street address contains invalid characters - Please try again. ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXWYZ abcdefghijklmnopqrstuvwxyz")
    City = input("Please enter the City:").title
    if City == "":
        print("City name cannot be blank - Please enter the city name.")
    elif set(City).issubset(allowed_char) == False:
        print("City name contains invalid characters - Please try again. ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-' ")
    Prov = ("Please enter name of province: ")
    if Prov == "":
        print("Province name cannot be blank - Please enter Province name. ")
    elif set(Prov).issubset(allowed_char) == False:
        print("Province name contains invalid characters - Please try again. ")
    else:
        break
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890")
    PostCode = input("Please enter your postal code  (A1A1A1): ").capitalize()
    if PostCode == "":
        print("Postal code cannot be blank - Please enter postal code. ")
    elif set(PostCode).issubset(allowed_char) == False:
        print("Postal Code contains invalid characters - Please Re-enter.")
    else:
        break
while True:
    PolicyStat = input("Are you starting a new policy or renewing a policy?  (N = New / R = Renew): ").capitalize()
    if PolicyStat == "R":
        PolicyStat = "Policy Renewal"
    elif PolicyStat == ("N"):
        PolicyStat = "New Policy"
    else:
        break
while True:
    PolicyType = input("What type(s) of coverage are you looking for?  (H = Home / A = Auto / B = Both):")
    allowed_char = set("ABH")
    if set(PolicyType).issubset(allowed_char) == False:
        print("Invalid input - What type(s) of coverage are you looking for?  (H = Home / A = Auto / B = Both): ")
    elif PolicyType == "":
            print("Policy Type cannot be blank - Please make a selection - (H = Home / A = Auto / B = Both):")
    elif PolicyType == "H":
        PolicyType = PolicyTypeH
    elif PolicyType == "A":
        PolicyType = PolicyTypeA
    elif PolicyType == "B":
        PolicyType = PolicyTypeB
    else:
        break








