
firstName = input("Enter first name : ")
numberOfSteps = float(input( "Enter number of steps : "))
eachStepBurnedCalories =0.25


#process phase
totalburnedcalories = numberOfSteps * eachStepBurnedCalories

#output process
print("First name", firstName )
print("Total calories burned : {:.2f}".format(totalburnedcalories))