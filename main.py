
from gamemanager import *

'''ÚJ JÁTÉK'''

clearScreen()

print("----   ÚJ JÁTÉK   ----")

red_player = None
blue_player = None

print("----   1. JÁTÉKOS   ----")
red_player = setUpPlayers(red_player)

print("----   2. JÁTÉKOS   ----")
blue_player = setUpPlayers(blue_player)

winner = None
'''Lehetetlen hogy döntetlen legyen de hibakeresés céljából most az lesz.'''

print("----   JÁTÉK INDUL   ----")

print("Kellemes időtöltést!")
input("(A folytatáshoz nyomj meg egy billentyűt...)")


'''KÖRÖK'''
while 1:

	'''TODO konzol grafika'''
	winner = makeTurn(red_player, blue_player)
	if winner != None: break
	
	'''TODO konzol grafika'''
	winner = makeTurn(blue_player, red_player)
	if winner != None: break


'''VÉGE'''

#clearScreen()

print("----   JÁTÉK VÉGE   ----")
'''TODO konzol grafika'''
print("A nyertes: " + winner.getName())

