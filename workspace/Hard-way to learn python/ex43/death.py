from random import randint
from sys import exit

class Death(object):
	"""This is the file containing the death ending."""

	def __init__(self, junk):
		self.number = randint(0,5)

	def get_number(self):
		return self.number

	def death(self):
		comment = [ "You died, you loser.",
					"You know what? You have been kicked out.",
					"Yoo, loser. Welcome to the death end.",
					"Poor young man, you are dead.",
					"Congratulation, my friend! You died! Good job!"]		

		print comment[self.get_number()-1]


	def run(self):
		self.death()
		exit(0)
