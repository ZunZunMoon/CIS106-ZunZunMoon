name = input("Enter your name :  ")
costofApp = float(input("Enter the cost of appliance:  "))

if costofApp > 1000:
    costofWat = costofApp * 0.1
else:
    costofWat = costofApp * 0.05
total = costofApp + costofWat
print("Enter your name " + name)
print("The cost of warrantee is " + str(costofWat))
print("The total is $ " + str(total))
