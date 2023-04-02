counter = 0
totalex1 = 0
print("Do you want to compute your avarage score (yes or no)")
response = input("Enter yes or no ")
while response == "yes":
    counter = counter + 1
    print("Enter student last name ")
    lname = input()
    print("Enter exam score 1 ")
    score1 = float(input())
    print("Enter exam score 2")
    score2 = float(input())
    avg = (score1 + score2) / 2
    totalex1 = totalex1 + score1
    print("Student " + lname + " has avarage of  " + str(avg))
    print("Do ou want to compute your avarage score (yes or no)")
    response = input()
print("Total number of students " + str(counter))
avgex1 = totalex1 / counter
print("Average Exam score 1 is " + str(avgex1))
