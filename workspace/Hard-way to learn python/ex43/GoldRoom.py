class GoldRoom(object):

	def __init__(self, gold):
		self.gold = 0

	def get_gold(self, more):
		self.gold += more
		return self.gold

	def show_gold(self):
		return self.gold

	def welcome(self):
		print "Welcome to Gold Room!"
		print "You must have gone through several huge challenges."
		print "Now it's the time to get your rewards, treasures!!"
		print "But remember one thing: Those greedy will suffer!"
		raw_input("> ")

	def collect_gold(self):
		print "In the center of the room, you find a huge amount of gold."
		amount = 0
		while amount != "q":
			print "Now you have %d kilogram of gold." % self.get_gold(int(amount))
			print "What amount of gold do you want to get?"
			print "Enter q to leave."
			amount = raw_input("> ")

			

	def run(self):
		self.welcome()
		self.collect_gold()
		if self.show_gold() > 200:
			print "You are too greedy!!!!!!!!"
			print "The guardian of the room wakes up and hit you hard!"
			return ["Death", 0]
		return ["Leave", 0]

