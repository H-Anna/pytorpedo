'''#!/usr/bin/env python3'''

from player import *
from ship import *

abc = ascii_uppercase[0:10]

'''DELETE?'''
def stringToCell(dict, str):
	return dict[str[0]][int(str[1])]



print("****Új játék****")

player = Player()
for length in range(1,6):
	tmpship = player.addShip(length)
	tmpship.setShipLocation
