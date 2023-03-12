#input process
totalcostforameal = float(input("Enter the total cost for a meal : "))

#process phase
tips = [15/100, 18/100, 20/100]

#output process
for tip in tips:
  print("Total:\t%.2f" % (totalcostforameal))
  print("Tip:\t%.2f" % (totalcostforameal * tip))
  print("Total with Tip:\t%.2f" % ((totalcostforameal * tip) + totalcostforameal))
  print("\n\n")