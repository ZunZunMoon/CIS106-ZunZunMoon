response = input("Do you want to calculate interest (Yes or No)")

while response == "yes":

  p = float(input("Enter principle amount "))
  i = float(input("Enter interest rate "))

  totint = 0.0
  print("Year", "Beg Bal", "End Bal")
  for count in range (1, 6, 1):
    intamt = p * i
    totint = totint + intamt
    endbal = p + intamt
    print(count,"  ", p , "  ", endbal)
    p = endbal
  response = input("Do you want to calculate interest(yes or No)")

print("total interest earned", totint)



