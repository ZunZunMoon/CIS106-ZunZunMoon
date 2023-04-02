nooforders = 0
sumofdiscamt = 0
print("Do you want to calculate total order with discount? (yes or no)")
response = input()
while response == "yes":
    qty = float(input("Enter the quantity "))
    price = float(input("Enter the price "))
    extPrice = qty * price
    if extPrice > 10000.0:
        discamt = extPrice * 0.25
    else:
        discamt = extPrice * 0.1
    totalorder = extPrice - discamt
    sumofdiscamt = sumofdiscamt + discamt
    nooforders = nooforders + 1
    print("Extended price is $  " + str(extPrice))
    print("Discount amount $  " + str(discamt))
    print("Total order amount $  " + str(totalorder))
    print("Do you want to calculate total order with discount? (yes or no)")
    response = input()
print("Total Discount Given $  " + str(sumofdiscamt))
print("Number of orders entered   " + str(nooforders))
avgdiscamt = sumofdiscamt / nooforders
print("Average Discount Given $  " + str(avgdiscamt))
