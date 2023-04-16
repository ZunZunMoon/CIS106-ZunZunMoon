def compcost(gallons):
    costoftrip = gallons * 2.5
    
    return costoftrip

def compmpg(miles, gallons):
    mpg = miles / gallons
    
    return mpg

# Main
city = input("Enter destination city;  ")
miles = float(input("Enter how many miles travelled:  "))
gallons = float(input("Enter how many gallons:  "))
mpg = compmpg(miles, gallons)
costoftrip = compcost(gallons)
print("destination city " + city)
print("miles per gallon " + str(mpg))
print("Cost of gas used on the trip " + str(costoftrip))
