#input process
purchasepricepershare = float(input("Enter purchase price per share : "))
thecurrentstockprice = float(input("Enter the current stock price : "))
qtyofstock = float(input("Enter the qty of stock : "))

#process phase
thevalueofthestock = (thecurrentstockprice - purchasepricepershare) * qtyofstock

#output phase
print("The value of the stock price is ", thevalueofthestock)