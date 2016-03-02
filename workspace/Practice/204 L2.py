
date = raw_input("Enter a date in MM/DD/YYYY format > ")
month, day, year = date.split('/')
Months = ["Jan", "Feb", "Mar", "Apr", "May"]
month = Months[int(month)-1]
print month + " " + day + "," + year


