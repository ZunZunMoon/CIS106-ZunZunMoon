def displyarrays(lname):
    for i in range (0,10,1):
      print(lname[i])

    print("Another Display using for loops")
    for x in range (2,10,1):
      print (lname[x])

    for j in lname:
      print(j)

def rdisplay(lname):
    for i in range(9,-1,-1):
      print(lname[i])

    print(lname)
    lname.reverse()
    print(lname)
lname=["Adams", "Baker", "Smith", "Davis  ", "Michaels", "Ted", "Bob", "Steve", "Kevin", "Calin"]

displyarrays(lname)
print("reverse order")
rdisplay(lname)