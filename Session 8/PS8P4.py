f = open("data4.txt", "r")

#initialize counters and sums to 0
c = 0.0
totp_ex = 0.0

#get first data line
item = str(f.readline().rstrip('\n'))

while item !="":
    qty = float(f.readline())
    price = float(f.readline())

    ep = qty*price
    #sum and count . in the loop
    totp_ex = totp_ex + ep
    c = c + 1

    #display a line of data
    print ("Item is:           ", item)
    print("Quantity is:        ", qty)
    print("price is:           ", price)
    print("Extended Price is:  ", ep)

    #get next data
    item = str(f.readline().rstrip('\n'))
