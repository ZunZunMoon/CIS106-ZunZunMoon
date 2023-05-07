#define the object
class Student:
  
#use pass to leave empty for now
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + ',' + last + '@harpercollege.com' 
    #self.rate = 0.00
  


  def comptutionOwed(dcode, credithrs):
    if dcode == "I":
        tution = float(credithrs) * float(250)
    else:
        tution = float(credithrs) * float(500)
    return tution

  def bonus(self,rate):
    b = float(rate) * float (self.pay)
    return b

   
#main - execution begins here
#  instantiate the object
stud1 = Student('ZunZun', 'Moon', 2500.00)

#use the object
#object syntax is object.method
print(stud1.email)
print(stud1.first)
print(stud1.last)
print(stud1.pay)
print(stud1.bonus(0.10))
print(stud1.bonus(0.20))
