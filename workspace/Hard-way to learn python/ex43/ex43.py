from GoldRoom import GoldRoom
from firstroom import First
from restroom import Restroom
from death import Death
from leave import leave

key = {'GoldRoom': GoldRoom, 'Death':Death, 'Leave':leave, 'First':First, 'Restroom':Restroom}


def intro():
	print "Open your eyes!"
	raw_input("> ")
	print "You wake up in a strange room with silver on all the walls."
	print "There is dim light in the center. You try to find out where this is."
	raw_input("> ")
	print "There is nothing but a huge door in front of you."
	print "Seems like you have the only choice!"
	print "Go, and open the gate my warrior!"
	raw_input("> ")
	print "Try to survive!"
	raw_input("> ")


def play(key, start):
	a = key[start](100)
	while True:
		next = a.run()
		a = key[next[0]](next[1])


intro()
play(key, 'First')




