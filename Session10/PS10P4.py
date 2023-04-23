def b_average (score1, score2, score3, handi):
  sum = score1 + score2 + score3
  average = (sum / 3)
  haverage = (sum + handi) / 3
  return average,haverage



lastname = str(input("Enter bowlers last name "))
score1 = float(input("Enter your score1 "))
score2 = float(input("Enter your score2 "))
score3 = float(input("Enter your score3 "))
handi = float(input("What is your handicap "))
average,haverage = b_average(score1,score2, score3,handi)
print("Your last name ", lastname)
print("Your score average is  ", format(float(average), '10,.2f'))
print("Your handicap", format(float(haverage), '10,.2f'))
                    