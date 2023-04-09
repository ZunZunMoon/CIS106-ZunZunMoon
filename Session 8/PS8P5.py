f = open("data5.txt","r")

c = 0
totaltution = 0.0

#get first prt of the data

lastname = str(f.readline().rstrip('\n'))

while lastname != "": # detect end of file
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())

  if dcode == "I":
    costpercredit = 250.00
  else:
    costpercredit = 500.00

  tution = costpercredit * credits
  c = c + 1
  totaltution = totaltution + tution

  print("Student:  ", lastname)
  print("credits taken:  ", credits)
  print("Tution Owed  ", tution)
  print("")
  
  latname = str(f.readline().rstrip('\n'))

f.close()

print("Number od students  ", c)
print("Total Tution Owed  ", totaltution)
