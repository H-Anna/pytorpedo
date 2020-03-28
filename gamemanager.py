'''Képernyő törlése'''

import player
import ship

import os

def clearScreen():
	os.system('cls' if os.name=='nt' else 'clear')

'''Játékosok beállítása'''
def setUpPlayers(player):
	
	name = input("Üdvözöllek a játékban! A neved: ")
	player = Player(name)
	char = input("Szeretnéd, ha véletlenszerűen lennének elhelyezve a hajóid? (I/N): ")
	setUpPlayerShips(player, (char == "I"))
	
	input("(A folytatáshoz nyomj meg egy billentyűt...)")
	clearScreen()


'''Hajók felállítása'''
def setUpPlayerShips(player, random):
	for length in range(1,6):
		tmpship = player.addShip(length)
		head = ""
		hori = False
		
		while !player.setShipLocation(tmpship, head, hori):
			if random:
				ltr_r = choice(ABC)
				num_r = choice(range(BOARD_LOWER_BOUND,BOARD_UPPER_BOUND))
				hori = choice([True, False])
			else:
				head = input("A(z) " + length + " hosszú hajó helye: ")
				hori = input()
	
	player.printShips()


def makeTurn(turn_player, enemy_player):

	clearScreen()

	print("----   " + turn_player.getName() + " játékos köre:   ----")
	
	'''Input: cella'''
	cell = ""
	while !enemy_player.checkForHit(cell):
		cell = input("Írd be azt a cellát, amire lősz: ")
	
	if enemy_player.checkEndCondition():
		return turn_player
	
	input("(A folytatáshoz nyomj meg egy billentyűt...)")
	
	return None
