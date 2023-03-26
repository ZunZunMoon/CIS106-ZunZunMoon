lname = input("Enter last name :   ")
salary = float(input("Enter salary :   "))
joblevel = int(input(" Enter joblevel :   "))
if joblevel >= 10:
    bonusrate = 0.25
else:
    if joblevel >= 5:
        bonusrate = 0.2
    else:
        bonusrate = 0.1
bonus = salary * bonusrate
print("Employee last name :   " + lname)
print("The bonus amount :  " + str(bonus))
