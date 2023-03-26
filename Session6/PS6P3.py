
principleamount = float(input("Enter principle amount : $  "))
yearstomaturity = input("enter the years to maturity :  ")
if yearstomaturity == "5" and principleamount > 100000.00:
    interestrate = 0.06
else:
    if yearstomaturity == "10" and principleamount > 50000.00:
        interestrate = 0.05
    else:
        if yearstomaturity == "5" and principleamount > 50000.00:
            interestrate = 0.04
        else:
            interestrate = 0.02
fYinterestamount = principleamount * interestrate
print("The principle amount is $    " + str(principleamount))
print("The interest rate is     " + str(interestrate))
print("The interest amount for first year is    " + str(fYinterestamount))
