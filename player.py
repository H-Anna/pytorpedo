
from string import ascii_uppercase '''A-J betűkhöz'''

class Player:
	'''Adattagok:
	board = {} 	dictionary ; Kulcs: A-J, érték: lista 0-9, ha egy mezőre már lőttek, akkor azt ki kell venni a listából
	ships = [] 	list ; 5 db hajó. Ha egy hajó elsüllyed, kiveszi a listából. Ha üres a lista, vége a játéknak.
	'''
	
	def __init__(self):
		board = {}
		ships = []
		for letter in list(abc):
			for n in range(0,10):
				board[letter] = n		'''Feltölti a boardot'''
	
	def addShip(length, head, horizontal = False):
		newship = Ship(length)
		ships.append(newship)
		return newship
	
	def setShipLocation(ship, head, horizontal):
		temp = [head]
	
		if length > 1:
			ltr = head[0]
			ltr_place = list(ascii_uppercase).index(head[0]) '''A betű helye az ABC-ben'''
			num = int(head[1])
			
			if horizontal:
				
			else:
				for n in range(num+1, num+ship.getLength()):
					cell = ltr + string(n)
					temp.append(cell)
		
		range = temp

	
	def getShipWithLength(length):
		for s in ships:
			if s.getLength == length:
				return s
		return null
	
	def checkForHit(cell):
		if int(cell[1]) in board[cell[0]]:
			board[cell[0]].remove(int(cell[1]))
			return "hit"
		else
			return "not in list"
	
	def checkCellForShip(cell):
		for s in ships:
			if cell in s.range:
				return True
		return False
