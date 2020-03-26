'''#!/usr/bin/env python3'''

from player import *
from ship import *

print("****Új játék****")


'''Ellenőrzi, létezik-e ez a cella'''
def isCellInputCorrect(cell):
	return (cell[0] in ABC) and (int(cell[1:]) in range(BOARD_LOWER_BOUND, BOARD_UPPER_BOUND))


def setUpPlayerShips(player, random):
	for length in range(1,6):
		if random:
			
			'''Random input'''
		else:
		tmpship = player.addShip(length)
		head = ""
		while (head == "") or (isCellInputCorrect(head) and !player.setShipLocation(head)):	'''Egyelőre feltételezzük hogy az input megfelelő'''
			head = input("A(z) " + length + " hosszú hajó helye: ")


red_player = Player(input("Üdvözöllek a játékban! A neved: "))
char = input("Szeretnéd, ha véletlenszerűen lennének elhelyezve a hajóid? (I/N): ")
setUpPlayerShips(red_player, (char == "I"))
