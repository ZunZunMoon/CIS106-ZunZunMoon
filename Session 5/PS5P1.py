
qty = float(input("Enter quantity:  "))

if qty >= 1000:
    unitprice = 3.00
else:
    unitprice = 5.00
extprice = qty * unitprice
tax = extprice * 7/100
total = extprice + tax

print("Quantity Ordered" + str(qty))
print("Unit Price $ " + str(unitprice))
print("Extended Price is $ " + str(extprice))
print("Tax is $  " + str(tax))
print("Total Order $ " + str(total))
