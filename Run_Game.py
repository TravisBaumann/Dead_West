import sys
import os
from random import randint
#from game import *
from DeadWest import *
"""
a text-based choose-your-own-adventure

to clear screen:
	import os
	os.system("clear")
"""

def main():
	print("\nPlease, just do me a little favor. I'm doing this because I want you to grow \'Okay....' or 0 for \'I'm selfish and refuse to appease you, stranger.")
	wannaPlay = input("> ")
	if wannaPlay != "0":
#STEP 1
		game()
	else:
		print("Since you were mean, im now exiting the game.")
		sys.exit

if __name__ == "__main__":
	main()