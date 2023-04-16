def compgross(hours, payrate):
    if hours > 40:
        grosspay = (hours - 40) * payrate * 1.5 + 40 * payrate
    else:
        grosspay = hours * payrate
    
    return grosspay

def comppay(jobcode, hours):
    if jobcode == "A":
        payrate = 30
    else:
        if jobcode == "L":
            payrate = 25
        else:
            payrate = 50
    
    return payrate

# Main
lname = input("Enter last name: ")
jobcode = input("Enter job code A or L or J: ")
hours = float(input("Enter how many hours worked: "))
payrate = comppay(jobcode, hours)
grosspay = compgross(hours, payrate)
print("Employee last name   " + lname)
print("Employee gross pay is $  " + str(grosspay))