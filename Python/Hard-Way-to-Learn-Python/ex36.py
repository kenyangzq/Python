from sys import exit

live = 100
spell = 100
challenge = 1


def room_gold():
	print "Welcome to room_gold. This room is full of gold."
	print "How many kilogram of gold do you want to take?"

	next = raw_input("> ")
	amount = int(next)

	if amount > 100:
		dead("How dare you?!")
	else:
		print "You are not greedy."
		leave()

def room_danger(room):
	if room == "start":
		print "Welcome, my brave warrior."
		print "You have to go thorough several challenge before you find the treasure!"
		print "Whenever you finish one challenge, you can rest and fix yourself in rest rooms."
		
	if challenge == 1:
		status()

		print "Now here is your first challenge:"
		print "There is a huge robot inside the room. It suddenly comes alive!!"
		print "Do you want to fight against him?"

		answer = raw_input("YES or NO?  ")

		if answer == "YES":
			fight("robot")
		elif answer == "NO":
			print "You coward bastard!"
			dead("You don't have the courage to fight!")
		else:
			print "What are you saying?? Try again, young man."
			next = raw_input("> ")
			room_danger("restroom")

	elif challenge == 2:
		print "Now here is your second challenge:"
		print "A huge tiger appear! It is very dangerous!"
		
		next = raw_input("> ")

		print "It runs toward you. You have no choice but fight!"

		next = raw_input("> ")
		fight("tiger")


def fight(enemy):
	print "You are fighting against a huge %r." % enemy

	if enemy == "robot":
		print "You win the battle after a long fight!"
		print "But you are injured."
		global live
		global spell
		live = 60
		spell = 50
		status()

		print "Now you are going to the rest room and take some rest."
		print "Press RETURN to confirm."
		confirm = raw_input("> ")

		restroom()

	elif enemy == "tiger":
		print "This tiger is so strong!"

		next = raw_input("> ")

		print "But you finally win!"
		print "You win the entrance to gold room!"

		next = raw_input("> ")
		room_gold()



def restroom():
	print "How many hours do you want to rest?"
	print "(You gain 10 live and 10 spell per hour rest.)"

	time = int(raw_input("> "))

	if time > 6:
		print "You rest for too long. The danger has come and you are not aware."
		dead("You are not prepared for the sudden danger.")
	
	for i in range(0,time):	
		global live
		global spell
		live += 10
		spell += 10

	print "After %d hours of rest, you become much healthier." % time
	status()


	print "Now is time to face your second challenge!"
	global challenge
	challenge += 1

	print "Press RETURN if you are ready!"
	confirm = raw_input("> ")

	room_danger("restroom")





def status():
	print "Here is your status:"
	print "Your live is %d and you spell is %d." % (live, spell)



def leave():
	print "Because you make the right decision, you finally leave the room safely."


def dead(reason):
	print reason
	print "You are kicked out of the building."
	exit(1)


def start():
	print "You are in a huge building!"
	print "Do you want to start a great adventure?"
	print "Press RETURN to start. Press CTRL-C to exit."

	confirm = raw_input("> ")


	room_danger("start")




start()


