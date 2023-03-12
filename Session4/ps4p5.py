#input process
fixedCost = float(input("Enter fixed costs : "))
pricePerUnit = float(input("Enter price per unit : "))
costPerUnit = float(input("Enter cost per unit : "))

#process phase
breakEvenPoint = fixedCost / (pricePerUnit - costPerUnit)
print("Break even point : %d" % (breakEvenPoint))
