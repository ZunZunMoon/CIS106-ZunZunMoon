# input phase
lname = input("Enter your last name:  ")
nofdependents = float(input("Enter the number of dependents:  "))
gIncome = float(input("Enter your gross income :  "))

adjgross = float(gIncome)- 12000.00 * float(nofdependents)

if adjgross > 50000.0:
    tax = gIncome * 0.20
else:
    tax = gIncome * 0.10

if tax < 0:
    tax = 100.00

print("The last name is " + lname)
print("The gross income is " + str(gIncome))
print("The number of dependents is " + str(nofdependents))
print("The adjusted gross income is " + str(adjgross))
print("The income tax is $ " + str(tax))