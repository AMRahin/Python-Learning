print("Welcome to the bill calculator")
totalbill=(float(input("What was your total bill?")))
percentagetip=(float(input("How much tip do you like to give?")))
splitbill=(int(input("How many people to split the bill?")))
tip=(percentagetip/100)
billwithtip=(totalbill*tip)+totalbill
billperperson=(billwithtip/splitbill)
finalbill=round(billperperson,2)
if(splitbill==1 or splitbill==0):
    print(f"your total bill:{billwithtip:.2f}")
else:
    print(f"Each person should pay:{finalbill:.2f}")


