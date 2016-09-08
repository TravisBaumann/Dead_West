import sys
import textwrap
from Run_Game import *

 # I need to add a save and load function along with using 0 to break the game. last thing I need to do is learn to lower the amount of health I have 

WELCOME_SPLASH = (""" The marshall has taken you into custody. Usually you are met with a warning.... A slap on the wrist, but this time he's taking it seriously. He says you've got to learn how to behave sometime if you're going to be taking care of your wife (and his daughter), Miriam. He's asked you to stay in a holding cell overnight so you can own up to your mistakes, but this day will be no normal day.You have been waiting in your cell with a raving lunatic for the last 12 hours.
You Decide to get some sleep.
You awaken to the sound of the marshall hootin' and hollerin' about some crazy folk in the city.
He says they 'been eating people.
The marshall inserts his lock into the cell door to let you out when suddenly the crazy man runs at him and bites him in the throat.
The marshall is luck enough to fire off a shot at the assailant which hits him in the skull and kills 'em dead. """)
ACTIONS = ( "1: SHOOT", "2: STAB", )

def ERROR_CHECKING(choice):
	print("\nYou entered \'{}', an invalid option".format(choice))
	#print("\nYou must choose either \'1' or \'0'")
	OptionsList()

class DisplayArt():
	def __init__(self, LevelNumber=0, gameOn=True):
		self.LevelNumber = 0
		self.gameOn = True

	def titleArt(self):
		os.system("clear")
		print("    ___               _   __    __          _   ")
		print("   /   \___  __ _  __| | / / /\ \ \___  ___| |_ ")
		print("  / /\ / _ \/ _` |/ _` | \ \/  \/ / _ \/ __| __|")
		print(" / /_//  __/ (_| | (_| |  \  /\  /  __/\__ \ |_ ")
		print("/___,' \___|\__,_|\__,_|   \/  \/ \___||___/\__|")
                                                


	def YouLose(self):
		print("Maybe Next Time, Partner")
	def wannaPlay(self):
		print("\n", textwrap.fill(WELCOME_SPLASH, width=70))
		print("\nPress any key to leave and find your beloved.") 
		print("...OR...")
		print("Press \'0' to: Exit Authentic Western Simulator")

	def stage_display(self, LevelNumber):	
		if LevelNumber == 0:
			LevelNumber += 1
			y = input("\nMaking your way home is necessary if you ever want to see Miriam again.")
			x = input("You have alerted an enemy")
			print("\nYou thank the Marshall, grab your weapons and walk out the door")


			return (LevelNumber, self.gameOn)

		elif LevelNumber == 1:
			LevelNumber += 1
			print("\nKeep moving!")
			return (LevelNumber, self.gameOn)

		elif LevelNumber == 2:
			LevelNumber += 1
			print("\nKeep Moving!")
			return (LevelNumber, self.gameOn)

		else: 
			LevelNumber += 1
			self.gameOn = False
			return (LevelNumber, self.gameOn)
			gameEnd()

class Player():
	
	def loseHealth(self):
		self.health -= 2
		return self.health
	def __init__(self, health=5, score=0, extra=0):
		self.health = 5
		self.score = 0
		self.extra = 0

	def GainScore(self):
		self.score += 1
		return self.score

	def displayHealth(self):
		print("\n")
		print("You have {} health".format(self.health))
		return self.health

	def loseHealth(self):
		self.health -= 2
		return self.health

class Monster():
	def __init__(self):
		self.monsterName = ""

	def outlaw(self): 
		self.monsterName = "outlaw"

		print("\n")
		description1 = """\n You are faced by an outlaw, taking advantage of the panic in the city. He sees the knife at your side and pulls one out from his pocket. "I'll be taking your wallet!" He says. """
		
		print("\n")
		print(textwrap.fill(description1))
		

		return self.monsterName

	def zombies(self): 
		self.monsterName = "zombies"
		
		print("\n")
		description = """ You have come to realize that your cellmate was not a madman, he was.... infected?
							now these people are attacking the normal folk of the city.
								NOT ON MY WATCH! """
		print("\n")
		print(textwrap.fill(description))
		
		return self.monsterName

	def zombie_outlaw(self): 
		self.monsterName = "zombie outlaw"
		
		print("\n")
		description = """ Whoah hold on there nellie. I thought the enemies could be outlaws OR Zombies... not both. """
		print("\n")
		print(textwrap.fill(description))
		
		return self.monsterName


class Calculations():
	def __init__(self, character_roll=0, enemy_roll=0, gameOn=True, monster_type=3, extra=0, monsterName="enemies"):
		self.character_roll = 0
		self.enemy_roll = 0
		self.gameOn = True
		self.monster_type = 3
		self.extra = 0
		self.monsterName = "enemies"

	def randomRoll(self, monster_type, choice):
		if (monster_type == 0 and choice == "1"):
			self.extra = 25
			print("\nYour extra is: +{}".format(self.extra))
		elif (monster_type == 1 and choice == "2"):
			self.extra = 25
			print("\nYour extra is: +{}".format(self.extra))

		self.character_roll = (randint(1,100) + self.extra)
		print("\nYour roll was: {}".format(self.character_roll))

		self.enemy_roll = randint(1,99)
		print("\nThe {}' roll was: {}".format(self.monsterName, self.enemy_roll))

		return self.character_roll, self.enemy_roll

	def compareBids(self, character_roll, enemy_roll):
		if character_roll >= enemy_roll:
			print("You beat 'em!")
			x = input("Press any key to continue.")
			return True
	
		else:
			print("\nWhoah, I never knew they hit that hard!")
			z = input("You Lost. Miriam is probably a zombie now.")	

			gameOn = False
			return gameOn

	def MakeEnemy(self, monster):
		self.monster_type = randint(0,2)

# this sets up the random selection of the enemy
		if self.monster_type == 0:
			monsterName = monster.outlaw()
			return monsterName, self.monster_type
		elif self.monster_type == 1:
			monsterName = monster.zombie_outlaw()
			return monsterName, self.monster_type
		else:
			monsterName = monster.zombies()
			return monsterName, self.monster_type

def OptionsList():
	print("\n")
	print("\nThere are only two actions for a cowboy.... shoot, or stab............ or gamble:")
	print("\nPress 0 Quit Authentic Wester MMORPG.")

	for act in ACTIONS:
		print(act)
	
	choice = input("> Enter a number: ")
	
	if choice == "0":
		gameEnd()
	
	elif choice == "1":
		print("You Shoot!")
		return choice

	elif choice == "2":
		print("You Stab!")
		return choice
	
	else:
		ERROR_CHECKING(choice)

def gameEnd():
	gameOn = False
	sys.exit

def game(): #runs first from main()
	LevelNumber = 0

	splash = DisplayArt()
	splash.titleArt()
	splash.wannaPlay()
	continueOption = input("> ")

	if continueOption == "0":
		gameOn = gameEnd()
		gamePlay(gameOn, LevelNumber)
	else:
		gameOn = True
		gamePlay(gameOn, LevelNumber)

def gamePlay(gameOn, LevelNumber):
	stage = DisplayArt()
	calcs = Calculations()
	monster = Monster()

	while LevelNumber < 3:
		if gameOn == True:

			LevelNumber, gameOn = stage.stage_display(LevelNumber)

			player = Player()
			health = player.displayHealth()

			monsterName, monster_type = calcs.MakeEnemy(monster)

			choice = OptionsList()
			character_roll, enemy_roll = calcs.randomRoll(monster_type, choice)

			gameOn = calcs.compareBids(character_roll, enemy_roll)
			if LevelNumber == 3:
				print("\nYou have made it back to Miriam! she's sad he dad is now a zombie..... but she can keep him as a pet now")
				print("Thanks for playing.")
			

		else:
			print("\nYou'll get 'em next time, kid")
			break

