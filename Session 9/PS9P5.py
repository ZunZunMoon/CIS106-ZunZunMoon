def comptotal(credithrs, payrate):
    totalpay = credithrs * payrate
    
    return totalpay

def comptutionOwed(dcode, credithrs):
    if dcode == "I":
        payrate = 250
    else:
        payrate = 550
    
    return payrate

# Main
lname = input("Enter student last name: ")
credithrs = float(input("Enter how many credits hours: "))
dcode = input("Enter district code of I or O: ")
payrate = comptutionOwed(dcode, credithrs)
totalpay = comptotal(credithrs, payrate)
print("Student last name  " + lname)
print("The total tution owed  " + str(totalpay))
