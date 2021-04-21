from sys import exit

# Welcome to the main code of TowerOfKnowledge game 
# Just have fun playing it GoodLuck!

print('\n\nThis game is inspired from the game-book "LA TOUR AUX 100 MENACES" authored by '
	'Jean-Luc BIZIEN and Didier GRAFFET'

	'\n\tYou are Elric, a youg boy who is always isolated in the basement of the house of '
	'his grandparents. There, seated in the half-light, you love paging through old books.'
	'This afternoon, you discovered an worn-out work, with a brown leather cover orned with'
	' gold. It\'s without doubt a collection of old tales!' 
	'\n\tWrapped up in your favourite blanket, you opened the thick volume and you dive '
	'immediately in the pages.'
	'\n\tSuddenly, you sense a powerful blow, a violent light blinds you and... you aspired'
	' in a magic world!'
	'\n\tRemember in any case, there is no going back!'
	'Good Luck!'

)

def start():
	n = int(input('Choose a number.'))

	for i in range(n):
		print(f"\t*{i+1}-This game is cool!")

	print('The tower of knowledge! A titan tower and you are going forward it. At a glance '
		'you see 3 entrances: one at the ground floor, the second just above it, the third '
		'is a window more higher.'
		'What will choose ?'
	)
	
	choice = input("> ")

	#just run the if statement according to the user choice!!
	if "1" in choice or "first" in choice or "one" in choice:
		print("You have chosen the first door.")
		page_18() 
	elif "2" in choice or "second" in choice or "two" in choice:
		print("You have chosen the second door.")
		page_30()
	elif "3" in choice or "third" in choice or "three" in choice:
		print("You have chosen the third door.")
		page_22()
	else:
		print("This is not a valid choice.")
		start()


def page_18():
	print('Here you are inside the tower. This journey is like a distress call, you need to '
		'save the guardien of dreams. The mold has already began devouring pages. '

		'Here is the message of the guardien of dreams : I AM THE GUARDIEN OF DREAMS, I AM '
		'FOREVER WATCHING THE TALES. I LIKE POETRY AND GOOD STORIES, BUT THE MOLD QUEEN IS '
		'EATING ME. IF I\'AM GONE, THE TALES ARE TOO. WOULD HELP ME ?'
	)
	
	choice = input('> ')

	if 'y' in choice:
		print('Use the magic spray in top of the table to eliminate all the mold.'
			'\nCome on, you can do it!'
			'\nAlmost there! You got it!'
			'\nThank you very much!'
			'\nI thank you on the behalf of all the tales.'
			)
		page_30()
	elif 'n' in choice:
		print('Why?\nWe really need your help!')
		page_18()
	elif 'w' in choice or 'c' in choice:
		print('You are climbing from the window to get to the 3rd door.')
		page_22()
	else:
		print('This is not an answer!')
		print('You can always climb from the window to reach the third door.')
		page_18()


def page_22():
	print('You see the horrifying gargoyles that watching the tower. After seeing thinly, you '
		'discover that only one is alive. You can either ask it to take you in his back or you'
		' can continue climbing or your own. \nWhat are you going to do ?'
		)

	choice = input('> ')

	if 'take' in choice or 'back' in choice or 'ask' in choice:
		print('WOOHOOO, that is amazing !!!')
		print('The gargoyle refuse to take you higher, end of the trip.')
		#exo_36()
	elif 'continue' in choice or 'climb' in choice:
		print("It's very dangerous!\nBut you're lucky! You just arrived!")
		#exo_34()
	else:
		print('There no going back! You to choose on of the 2 alternatives!')
		page_22()


def page_30():
	print('Here you are in the presence of the master of writings! The old man has some troubles finding '
		'his eyeglasses. Can you read this text for him? If not, there is also a door at your left and a '
		'window at your right.\nTheManuscript'
		'\nthankyouforhelpingmeredingthismanuscriptactuallyicanreadwithoutglassesijustwantedtomakesureyo'
		'uareoursavioryoutakethestairstokeepgoinginthesearchofthemoldqueenandthankyouagain!'
		)

	choice = input("> ")

	if 'stairs' in choice or 'y' in choice:
		page_44()
	elif 'door' in choice or 'left' in choice:
		print('You\'re taking the door at your left.')
		page_42()
	elif 'window' in choice or 'right' in choice:
		print('You\'re taking the window.')
		page_34()
	else:
		print('This is not a valid choice!')
		page_30()


def page_44():
	print('Here you are in the room of the master coppyist, he is having some problems sorting the pages '
		'of an ancient roman book. If you help him he is ready to open the door in the back for you, if '
		'you do not want to waste time you can use the window at you right.\n'
		'Here is the numbers of the pages of the book :\n\t(1)---M\n\t(2)---IV\n\t(3)---X\n\t(4)---VI\n\t'
		'(5)---I\n\t(6)---XX\n(Write your answer like this :123456)'
		)

	choice = input('> ')

	if '524361' in choice:
		print("Perfectly done!\n")
		page_42()
	elif 'window' in choice or 'use' in choice:
		page_34()
	else:
		print('Wrong answer! You can always take the window!')
		page_44()


def page_34():
	print('Your energy is done, you lose control and you fall!\nEND OF THE GAME!')
	exit(0)


def page_42():
	print('Here you are in the core of the tower in the main big library. You have two choices: the door '
		'in the end of the corridor or a small window on your left. What would you choose?'
		)

	choice = input("> ")

	if 'door' in choice:
		print("After a long march, here is the door!\n")
		page_36()
	elif 'window' in choice:
		page_10()
	else:
		print("Not a choice!")
		page_42()

def page_36():
	print('You are in a room that is deserted, there is nothing here but 2 doors one red, the other is '
		'blue. What would you choose')

	choice = input("> ")

	if 'red' in choice:
		print("Opening the red door!\n")
		page_8()
	elif 'blue' in choice:
		print("Opening the blue door!\n")
		page_20()
	else:
		print("Not a choice!")
		page_36()


def page_8():
	print('You are in the middle of the jungle, the trees are very long and they mask the moon light, you '
		'can distinguish a door in a old house at the back, and a hole in the ground. What route will you '
		'take?'
		)

	choice = input('> ')

	if 'door' in choice:
		page_28()
	elif 'hole' in choice:
		page_24()
	else: 
		print('Not a valid choice!')
		page_8()


def page_28():
	print('You are finally in front of the mold queen who is trying to demolish all books and the tower. '
		'You have to stop her! But how? Think!\n\n There many solutions: you can escape the fight by taki'
		'ng the window, or begin a direct fight, or you can read the wizard book in thr ground to defeat '
		'her! \nWhat would you choose?'
		)

	choice = input("> ")

	if 'escape' in choice or 'window' in choice:
		page_34()
	elif 'direct' in choice or 'fight' in choice:
		print("She is more powerful than she seems! \nOH! NO! SHE EATS YOU HEAD OFF!")
		print("End of the game!")
		exit(0)
	elif 'wizard' in choice or 'book' in choice:
		print("Hurry up ! You have to find the right magic formula to beat her!")
		print("Here it is, say out loud with doing gestures with your bare hands:")
		print("'Klaatu barada nikto'")
		print("'Sim Sala Bsim'")
		print("'Treguna Mekoides Trecorum Statis Deee'")
		print("CLAP YOUR HANDS!")
		print('\nNice work! She is vanishing!')
		print('A door is now opening for you.')
		page_38()
	else:
		print('Not a choice!')
		page_28()


def page_38():
	print('You are finally in the automn garden. But there  is a lot of ravens here, they are clouding '
		'the whole room. What would you do? Say to them to leave, or take a window and escape. '
		)	

	choice = input("> ")

	if 'clarck' in choice:
		print('Well said! \nYou know very well the raven language!')
		page_32()
	elif 'escape' in choice or 'window' in choice:
		page_16()
	else:
		print("That's not raven language!\nHint: 'clarck', 'clarck'!")
		page_38()


def page_32():
	print('Your now in front of the guardian hydra, she thinks that you are the mold queen and want to'
		'destroy you. The proof she wants is you say a word of the magic spell you  used to beat the true'
		' mold queen!'
		)

	choice = input("> ")

	if choice in "Klaatu barada nikto Sim Sala Bsim Treguna Mekoides Trecorum Statis Deee":
		print('Nice play!')
		print('We\'ve arrived to the end of the journey!')
		print('You are now back to the basement!')
		exit(0)
	else:
		print('Bad choice!')
		print('The hydra devoured you!')
		print('You lost! GAME OVER!')
		exit(0)


def page_40():
	print('Now you are in this tiny room with a big monstreous raven in the back! There a window at '
		'your right and a small door at your left. What would you choose the door, the window or affront'
		'the raven beast? ACT FAST !'
		)

	choice = input("> ")

	if 'door' in choice:
		page_28()
	elif 'window' in choice:
		page_14()
	else: 
		print("Bad Luck!")
		print("Game Over.")
		exit(0)


def page_24():
	print('You are now in a white room, it is empty, there only one ladder in the back, you can use '
		'it to climb up or down. And there is a little door in the ground. It is up to you.'
		)
	
	choice = input("> ")

	if 'up' in choice:
		page_20()
	elif 'down' in choice:
		page_8()
	elif 'ground' in choice or 'door' in choice :
		page_12()
	else:
		print("I don't know what you mean!")
		page_24()

def page_10():
	print('Here are you in the room of the guardian of wrintings. On his desk there is a letter.'
		'\nHere is what it says : §§ EPYT MORF ENO OT ENIN §§ '
	)

	choice = input("> ")

	if choice == "123456789":
		print("You have decrypted the message. Nice done!")
		page_24()
	else:
		print("Bad choice!")
		print("The journey ends here!")
		exit(0)


def page_26():
	print('While you are going down, you see a little door. You have to choose to enter or continue.')

	choice = input("> ")

	if 'door' in choice:
		page_24()
	else:
		print('Oh, you fell down!')
		print('Game Over!')
		exit(0)


def page_20():
	print("Here you are in the guests room: Damp, dirty, blue-gray bricks held the cold inside the room "
		"as if it were collecting it. A single dancing light, projected from the last dying candle, flic"
		"kerd across the walls, moving to an unseen rhythm. The lone window, high on the outside wall, "
		"allowed only one tiny gleam of moonlight in to pronounce the time of the day. Scratches in the "
		"stone and rusty chains hung with eerie decoration as reminder of the passt. Thick white spider "
		"webs flowed across the room, shimmering in the candle light, and a lone live victim struggled "
		"in the wind. Wrapped thightly in silk threads. Rats squealed and padded across the hard floor, "
		"their nails scraping the ground as they scattered away from the crystal webs as if in fear they "
		"would be caught too!\nThere is 2 doors one on the left, the other in the right, and there is a "
		"secret passage."
		)

	choice = input("Your choice ?\n> ")

	if 'right' in choice:
		page_44()
	elif "left" in choice:
		page_24()
	elif 'secret' in choice or 'passage' in choice:
		page_30()
	else:
		print("Not a choice!")
		page_20()


def page_12():
	print("This is a room with two doors: one black, and one white, and a little window.")

	choice = input("> ")

	if "white" in choice:
		page_40()
	elif "black" in choice:
		page_38()
	elif 'window' in choice:
		page_16()
	else:
		page_12()


def page_14():
	print("Here in the top of the tower, you find the tribe of lost childrens. They are just like you. "
		"But they refuse to get back to the tower. They have developped a strategy to leave the tower. "
		"They need just one more member to go!"
		)
	print('Would join them and leave, or you would rather stay?')

	choice = input('> ')

	if 'join' in choice:
		print("You are back to the basement when all began!")
		exit(0)
	elif 'stay' in choice:
		print("They wont leave you stay, they take you with them as a prisonner!")
		print("Game over!")
		exit(0)
	else:
		print('What\'s that?')
		page_14()


def page_16():
	print('Here you are in the embarkation point. You have to choose between the three ships: the blue, '
		'the orange, or the  green.'
		)

	choice = input('> ')

	if 'blue' in choice:
		page_14()
	elif 'orange' in choice:
		page_40()
	elif 'green' in choice:
		page_26()
	else:
		print('Choose one of the tree ships!')
		page_16()

start()
