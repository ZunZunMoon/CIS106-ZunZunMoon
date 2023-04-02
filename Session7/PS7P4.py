sumofgrosspay = 0.0
noofemployees = 0
print("Enter response? (yes or no)")
var_continue = input()
while var_continue == "yes":
    print("Enter last name ")
    lname = input()
    print("Enter hours worked")
    hrs = float(input())
    print("Enter hourly rate ")
    rate = float(input())
    if hrs >= 40:
        grosspay = 40 * rate + (hrs - 40) * 1.5 * rate
    else:
        grosspay = rate * hrs
    print("Gross pay =  " + str(grosspay))
    sumofgrosspay = sumofgrosspay + grosspay
    noofemployees = noofemployees + 1
    print("Enter response? (yes or no)")
    var_continue = input()
avggrosspay = sumofgrosspay / noofemployees
print("Sum of all gross pay is $  " + str(sumofgrosspay))
print("Number of employees is " + str(noofemployees))
print("Average gross pay is $ " + str(avggrosspay))