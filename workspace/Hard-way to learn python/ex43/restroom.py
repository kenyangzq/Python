
from random import randint
from death import Death

class Restroom(object):
	"""This is the place where warriors can take some rest and recover!"""
	
	def __init__(self, live):
		self.live = live

	def intro(self):
		print "This is the room where warriors get some rest and get recovered."
		print "But be careful. Don't waste too much time here. "
		print "There may be unknown danger if you stay too long!"
		print "Maybe 5 days is a limit..."
		raw_input("> ")



	def rest(self):
		count = 0
		while count < 6:
			print "Now you have %d live." % self.live
			print "Do you want to take some rest?"
			print "Enter Yes or No."
			choice = raw_input("> ")
			if choice == "Yes":
				count += 1
				self.live = self.live * 1.1 + randint(0, 20)
				if self.live > 120:
					self.live = 120
				print "You take a good rest!"
				raw_input("> ")
			elif choice == "No":
				return ["GoldRoom", self.live]
			else:
				print "I don't understand."
				raw_input("> ")

		print "Young man, you are afraid of future challenge!"
		return ["Death", 0]

	def run(self):
		self.intro()
		return self.rest()
		








