# Date
print("Enter The Game Date  (yyyy-mm-dd) : XXXXXXXXXX")
Year = input("Enter a year:  ")
Month = input("Enter a month:  ")
Day = input('Enter a day:  ')
Opp_Name = input("Enter Opponents Name:  ")
Date = ("on {:>0}/{:>0}/{:>0}".format(Year, Month, Day))

# QB_Stats_Inputs
Num_Pass_Att = int(input('Enter The Number Of Pass Attempts:   '))
Num_Pass_Comp = int(input('Enter The Number of Pass Completions: '))
Total_Pass_Yrds = int(input('Enter The Total Of Passing Yards:  '))
Num_Touchdowns = int(input('Enter The Number of Touchdowns:  '))
Num_IntCP = int(input('Enter The Number of Intercepts:  '))
print()

# Rushing Stats
Rush_Att = int(input('Enter The Number of Rushing Attempts:  '))
Total_Rush_Yards = int(input('Enter The Total Rushing Yards:  '))
Rush_Touchdowns = int(input('Enter The Rushing Touchdowns:  '))

# Calculations QB Rating
Pass_Comp_Perc = float(Num_Pass_Comp/Num_Pass_Att) * 100
Yards_per_Pass = float(Num_Pass_Comp/Total_Pass_Yrds)
# QB Rating
Score1 = (Num_Pass_Comp/Num_Pass_Att)
Score1_Rating = (Score1 - 0.3)/0.2
Score2 = (Total_Pass_Yrds/Num_Pass_Att)
Score2_Rating = (Score2 - 3)/4
Score3 = (Num_Touchdowns/Num_Pass_Att)
Score3_Rating = Score3/0.05
Score4 = (Num_IntCP/Num_Pass_Att)
Score4_Rating = (Score4 - 0.095) / 0.04
QB_Score = (Score2_Rating + Score2_Rating + Score3_Rating) * 100
QB_Rating = QB_Score / 6
# Running Back Rating
RBScore1 = float(Total_Rush_Yards/Rush_Att)
RBScore2 = float(Rush_Touchdowns/Rush_Att) * 100
print(Rush_Touchdowns)
print()
print("Game Statistics Program")
print()
print("Game Statistics Vs {:>3}".format(Opp_Name), "{:>12}".format(Date))
print("----------------------------------------------------------------")
print("Quarterback Statistics")
print()
print("Number Of Pass Attempts:  {:>3}       Pass Completion %:     {:<2,.0f}%".format(Num_Pass_Att, Pass_Comp_Perc))
print("Number of Completitions:  ", Num_Pass_Comp)
print("Total Passing Yards:      {:>3}       Yards Per Pass:       {:<2,.2f}".format(Total_Pass_Yrds, Yards_per_Pass * 100))
print("Number of Touchdowns:      ", Num_Touchdowns)
print("Number of Intercepts:     {:>3}     Quarterback Rating:    {:<2.f}".format(Num_IntCP, QB_Rating))
print()
print("Number of rushing AAtts:   {:>2}       Avg Yards Per Rush:    {:<2.1f} ".format(Rush_Att, RBScore1))
print("Total Rushing Yards:   {:>6}   ".format(Total_Rush_Yards))
print("Number of Rushing TD,s:    {:>2}       TD Efficiency:        {:<2.2f}%  ".format(Rush_Touchdowns, RBScore2))
