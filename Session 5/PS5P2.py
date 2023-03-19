
item = input("Enter A or B for item :  ")
qty = float(input("Enter quantity :  "))

if item == "A":
    unprice = 10.0
else:
    unprice = 20.0
extprice = qty * unprice

print("The item is " + item)
print("The unit price is $ " + str(unprice))
print("The extened price is $ " + str(extprice))
