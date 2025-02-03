hours = int(input("How many kilowatt hours were used?\n"))

if hours <= 1000:
    price = hours * 0.07633
    print ("Amount owed is: $", price)
    if price <=100:
        print (":)")
else:
    price = (hours - 1000) * 0.09259 + (1000 * 0.07633)
    print ("Amount owed is: $", price)
    if price <=100:
        print (":)")
    else:
        print (":(")

print ("Ava Iannone")