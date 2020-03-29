'''Képernyő törlése'''

from player import *

import random
import os

CHAR_OF_SHIP = "H"
CHAR_OF_SEA = "S"
CHAR_OF_MARK = "X"



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
				head = random.choice(ABC) + str(random.choice(BOARDRANGE))
				hori = random.choice([True, False])
			else:
				head = input("A(z) " + str(length) + " hosszú hajó helye: ").upper()
				hori = (input("Vízszintes (V) vagy függőleges (F) a hajó? : ") == "V")
			if player.setShipLocation(tmpship, head, hori, rnd): break
	
	player.printShips()
	return player


def makeTurn(turn_player, enemy_player):

	print("----   " + turn_player.getName() + " játékos köre:   ----")
	print()
	'''Input: cella'''
	cell = ""
	while 1:
		cell = input("Írd be azt a cellát, amire lősz: ").upper()
		print()
		if enemy_player.checkForHit(cell): break
	
	if enemy_player.checkEndCondition(): return turn_player
	
	input("(A folytatáshoz nyomj meg egy billentyűt...)")
	
	return None

def printLegend():
	print()
	print(CHAR_OF_SEA + " = tenger")
	print(CHAR_OF_SHIP + " = hajó")
	print(CHAR_OF_MARK + " = torpedózott cella")
	print()



def printBoard(player, print_enemy):
	
	name = player.getName()
	brd = player.getBoard()
	shps = player.getShips()
	
	
	print("----   " + name + " TÁBLÁJA   ----")
	print()
	
	row = "    "
	for ltr in ABC:
		row += ltr + "  "
	print(row)
	
	for num in BOARDRANGE:
		row = str(num) + "   "
		
		for ltr in ABC:
			char = ""
			if print_enemy: char = getCharFromEnemyBoard(ltr, num, brd, shps)
			else: char = getCharFromBoard(ltr, num, brd, shps)
			
			row += char + "  "
		print(row)
	
	print()


def getCharFromBoard(ltr, num, board, ships):	
	if num in board[ltr]:		#ha a cella benne van a táblában akkor vagy üres, vagy van rajta hajó
		cell = ltr + str(num)
		
		for s in ships:
			if cell in s.getRange():
				return CHAR_OF_SHIP
		
		return CHAR_OF_SEA
	#ha nincs benn a táblában, akkor már lőttek rá
	return CHAR_OF_MARK
	

def getCharFromEnemyBoard(ltr, num, board, ships):
	#ha a cella NINCS a táblában, akkor lőttünk már rá, de nem biztos hogy hajó
	if num not in board[ltr]:		
		cell = ltr + str(num)
		
		for s in ships:
			if cell in s.getUnrange():
				return CHAR_OF_SHIP
		
		return CHAR_OF_MARK
	return CHAR_OF_SEA
