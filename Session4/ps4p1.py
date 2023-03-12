#input process
firstexamscore = float(input("Enter first exam score : "))
secondexamscore = float(input("Enter secondexam score : "))

#process phase
totalexamscore = firstexamscore * 60/100 + secondexamscore * 40/100

#output phase
print("Total exam score =", totalexamscore)