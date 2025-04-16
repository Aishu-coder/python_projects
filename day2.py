print("Welcome to tip calculator")
bill= float(input("what is the total bill?"))
tip= int(input("how much tip would you like to give ? 10 or 15 0r 12 ?"))
percentage= bill*float((tip/100))
totalbill=bill+percentage
people=int(input("how many people to split the bill ?"))
billforeach=round(totalbill/people,2)

print(f"each person should pay:{billforeach}")