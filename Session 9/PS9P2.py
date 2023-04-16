def compavg(hits, atbats):
    bavg = hits / atbats
    
    return bavg

# Main
lname = input("Enter last name:  ")
hits = float(input("Enter hits:   "))
atbats = float(input("Enter at bats:  "))
bavg = compavg(hits, atbats)
print("Player: " + lname)
print("Batting Average " + str(bavg))

