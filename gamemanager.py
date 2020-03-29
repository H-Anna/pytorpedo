'''Képernyő törlése'''

from player import *

import random
import os

def clearScreen():
	os.system('cls' if os.name=='nt' else 'clear')

'''Játékosok beállítása'''
def setUpPlayers(player):
	
	name = input("Üdvözöllek a játékban! A neved: ")
	player = Player(name)
	mychoice = (input("Szeretnéd, ha véletlenszerűen lennének elhelyezve a hajóid? (I/N): ") == "I")
	player = setUpPlayerShips(player, mychoice)
	
	input("(A folytatáshoz nyomj meg egy billentyűt...)")
	clearScreen()
	return player


'''Hajók felállítása'''
def setUpPlayerShips(player, rnd):
	for length in range(1,6):
		tmpship = player.addShip(length)
		head = ""
		hori = False
		
		while 1:
			if rnd:
				head = random.choice(ABC) + str(random.choice(range(BOARD_LOWER_BOUND,BOARD_UPPER_BOUND)))
				hori = random.choice([True, False])
			else:
				head = input("A(z) " + str(length) + " hosszú hajó helye: ").upper()
				hori = (input("Vízszintes (V) vagy függőleges (F) a hajó? : ") == "V")
			if player.setShipLocation(tmpship, head, hori, rnd): break
	
	player.printShips()
	return player


def makeTurn(turn_player, enemy_player):

	clearScreen()

	print("----   " + turn_player.getName() + " játékos köre:   ----")
	
	'''Input: cella'''
	cell = ""
	while 1:
		cell = input("Írd be azt a cellát, amire lősz: ").upper()
		if enemy_player.checkForHit(cell): break
	
	if enemy_player.checkEndCondition(): return turn_player
	
	input("(A folytatáshoz nyomj meg egy billentyűt...)")
	
	return None
