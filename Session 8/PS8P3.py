f = open("data3.txt","r")
totalBonus = 0
c = 0
lname = f.readline()
while lname !="":
  salary = f.readline()
  print()
  print("Employee Last Name: ", lname)
  print("Employee salary: $", format(float(salary), '10,.2f'))
  bonus = float(salary) * 0.10
  print ("Employee Bonus: $  ", format(float(bonus), '10,.2f'))
  totalBonus = totalBonus + bonus
  c = c + 1
  lname = f.readline()
f.close()
avgBonus = totalBonus/ c
print(" ")
print("Average Bonus: $  ", format(float(avgBonus),'10.2f'))