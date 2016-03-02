




x = raw_input("Please enter the amount > ")
x = 100 - int(x)
quarter = 0
dime = 0
nickel = 0
while x > 25:
	x = x - 25
	quarter += 1
while x > 10:
	x = x - 10
	dime += 1
while x > 0:
	x = x - 5
	nickel += 1

print "Your change is %d quarters, %d dimes and %d nickels" % (quarter, dime, nickel)