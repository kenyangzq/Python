# import argument variables from the system
from sys import argv

# unpack the argument variable
script, filename  = argv

# assign txt the file of the name filename
txt = open(filename)
line1 = txt.readline()

print line1

print "Here's your file %r:" % filename
# print the file out
print txt.read()

txt.close()


# prompt the user for the next file's name
file_again = raw_input("I will ask you the file name again\n> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()


