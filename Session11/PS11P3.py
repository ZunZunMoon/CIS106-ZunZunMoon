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
lname=["Adams", "Baker", "Smith", "Davis  ", "Michaels", "Ted", "Bob", "Steve", "Kevin", "Calin"]
scores = [1000.00, 800.00, 900.00, 850.00, 950.00, 980.00, 880.00, 920.00, 990.00, 750.00]



lname3 = []
scores = []


loadarrays(lname3,scores)
darrays(lname3, scores)