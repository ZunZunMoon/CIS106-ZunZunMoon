def loadarrays(lname, score):
    f = open("myfile.txt", "r")
    for i in range (0,10,1):
      ln = f.readline()
      ln = ln.rstrip("\n")
      lname.append(ln)
      s = f.readline()
      s.rstrip("\n")
      score.append(s)
    f.close
def darrays(lname3, scores):
    for i in range (0,10,1):
      print(lname3[i], "has score of", scores[i])
def hilow(lname, scores):
  hisoc = 0.0
  hisub = 0
  losoc = 999999.99
  losub = 0
  for i in range(0,5,1):
      if scores[i] > hisoc:
        hisoc = scores[i]
        hisub = i
      elif scores[i] < losoc:
        losoc = scores[i]
        losub = i

  print (lname[hisub], "has higest score of", scores[hisub])
  print(lname[losub], "has lowet score of", scores[losub])



def displyarrays(lname, scores):
    for i in range (0,10,1):
      print(lname[i], "has score of", scores[i])

    print("Another Display using for loops")
    for x in range (2,10,1):
      print (lname[x])
  
    for j in lname:
      print(j)

def rdisplay(lname):
    for i in range(9,-1,-1):
      print(lname[i])

    print(lname)
    lname2 = lname[::-1]
    print(lname2)
    lname.reverse()
    print(lname)
def searchname(lname3, scores, slname):
  foundsub = -1
  for i in range (0,10,1):
    if lname3[i] == slname:
      foundsub = i

  if foundsub == -1:
      print(slname,"not in the list")
  else:
      print(lname3[foundsub], "has score of ", scores[foundsub])

lname=["Adams", "Baker", "Smith", "Davis  ", "Michaels", "Ted", "Bob", "Steve", "Kevin", "Calin"]
scores = [1000.00, 800.00, 900.00, 850.00, 950.00, 980.00, 880.00, 920.00, 990.00, 750.00]




lname3= []
score = []

loadarrays(lname3, scores)
darrays(lname3,scores)
hilow(lname, scores)

response = input("Do you want to serch for a last name (y or N)")
while response == "Y":
  slname = input("Enter the name to search for ")
  searchname(lname3, scores, slname)
  response = input("Do you want to search for a last name (Y or N)")