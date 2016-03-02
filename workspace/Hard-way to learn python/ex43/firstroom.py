from random import randint


class First(object):
	"""This is the first room of challenge."""

	def __init__(self, live):
		self.live = live
		self.xxx = 1000

	def get_live(self):
		return self.live

	def get_xxx(self):
		return self.xxx

	def challenge(self):
		print "There is a huge xxx."
		print "It runs to you!"
		print "Fight against him, my warrior!"

	def welcome(self):
		print "This is the first room!"
		print "You will face unknown challenge."
		print "If you are ready, press ENTER."
		raw_input("> ")

	def show(self):
		print "You now have %d live." % self.get_live()
		print "The huge xxx has %d health." % self.get_xxx()

	def run(self):

		self.welcome()

		print "A huge xxx is approaching!"

		while self.get_xxx() > 0:
			

			self.show()

			print "What are you going to do?"
			print "A. Use your fist to hit it hard!"
			print "B. Hit it with all your strength."
			
			action = raw_input("> ")

			if action == "A":
				self.live = self.live * 0.95 - randint(0, 10)
				hit = randint(50, 100)
				damage = hit + self.xxx * 0.1 
				self.xxx = self.xxx - damage
				
				if hit > 90:
					print "You hit the weakness of the xxx, causing %d damages!" % damage
					print "It bleed badly!"
					print "Causing extra 100 damage!"
					self.xxx -= 100
				else:
					print "You hit it pretty hard!"
					print "Causing %d damage!" % damage
					

				raw_input("> ")

			elif action == "B":
				self.live = self.live * 0.8 - randint(0, 10)
				hit = self.xxx * 0.35 + randint(20, 60)
				self.xxx = self.xxx - hit
				print "Your strong hit causes %d damage to xxx." % hit
				print "You hit it with a huge strength, but it also hurds you on the arm!"
				print "You may not hit it as hard as this one!"
				raw_input("> ")
			else:
				print "Please try again."

			if self.get_live() <= 0:
				print "You use all your strength but unfortunately the xxx is too strong."
				return 'death'

		print "WOW! You finally defeat the huge monster."
		print "You can proceed now, my warrior."

		raw_input("> ")


		return ["Restroom", self.live]










