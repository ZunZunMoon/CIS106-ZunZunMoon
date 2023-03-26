nOtickets = int(input("Enter number of tickets:   "))
if nOtickets >= 25:
    ppticket = 50
else:
    if nOtickets >= 10:
        ppticket = 60
    else:
        if nOtickets >= 5:
            ppticket = 70
        else:
            ppticket = 75
totalC = nOtickets * ppticket
print("The numberof tickets :    " + str(nOtickets))
print("The price per ticket :$   " + str(ppticket))
print("The total cost :$  " + str(totalC))
