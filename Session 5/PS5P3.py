#input phase
numberofbooks = float(input("Enter the numbers of books:  "))
costperbook = float(input("Enter cost per book:  "))

ordertotal = (numberofbooks * costperbook)
if ordertotal > 50:
    sPfees = 0.0
else:
    sPfees = 25.0
total = ordertotal + sPfees
print(" The total is $ " + str(total))
print(" The shipping fees is $ " + str(sPfees))
