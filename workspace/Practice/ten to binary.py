# y = input("Enter a number in ten > ")

y = 846 ## enter whatever number you want to transfer into binary
print y%2

result = ""
while y != 0:
	result = str(y%2) + result
	y = y/2

print (result)