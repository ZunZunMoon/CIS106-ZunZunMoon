def discount(qty, price, discrate):
  total = (qty * price)
  discamt = discrate * total
  discprice = total - discamt

  return discamt, discprice




qty = float(input("Enter the quantity "))
price = float(input("Enter the unit price $ "))
discrate = float(input("Enter the discount rate % "))
discamt, discprice = discount(qty, price, discrate)

print("This is your quantity", qty)
print("The unit price $ ", price)
print("This is your siscounted amount $ ", discamt)
print("THisis your discounted price $ ", discprice)
