
from string import ascii_uppercase '''A-J betűkhöz'''

BOARD_UPPER_BOUND = 10
BOARD_LOWER_BOUND = 0

ABC = ascii_uppercase[BOARD_LOWER_BOUND:BOARD_UPPER_BOUND]


class Player:
	'''Adattagok:
	board = {} 	dictionary ; Kulcs: A-J, érték: lista 0-9, ha egy mezőre már lőttek, akkor azt ki kell venni a listából
	ships = [] 	list ; 5 db hajó. Ha egy hajó elsüllyed, kiveszi a listából. Ha üres a lista, vége a játéknak.
	'''
	
	def __init__(self, name):
		self.name = name
		board = {}
		ships = []
		for letter in list(ABC):
			board[letter] = []				'''Új oszlopot hoz létre'''
			for n in range(BOARD_LOWER_BOUND,BOARD_UPPER_BOUND):
				board[letter].append(n)		'''Új sort hoz létre'''
	
	
	def addShip(length):
		newship = Ship(length)
		ships.append(newship)
		return newship
	
	
	def stayWithinBounds(head, length, horizontal): '''Hajó letételekor ne indexeljünk a játéktéren kívül'''
		tmp = 0
		if horizontal:		'''Ha a hajó vízszintes, akkor az oszlopokat kell vizsgálni'''
			tmp = list(ABC).index(head[0])
		else:				'''Ha a hajó függőleges, akkor a sorokat'''
			tmp = int(head[1:])
		
		if (tmp + length-1) > BOARD_UPPER_BOUND - 1:
			return -1
		else:
			return 1
	
	
	'''Megnézi, hogy van-e az adott cellán hajó, ha igen, visszatér vele'''
	def checkCellForShip(cell):
		for s in ships:
			if cell in s.getRange():
				return s
		return None
	
	
	def setShipLocation(ship, head, horizontal = False):
		temp = [] '''A hajó celláit tartalmazó lista'''
	
		ltr = head[0] '''A betű'''
		ltr_place = list(ABC).index(head[0]) '''A betű helye az ABC-ben'''
		num = int(head[1:]) '''A szám'''
		
		'''Alaphelyzetben a program a "head" cellát úgy veszi, mintha a bal szélső/legészakibb cella lenne.
		(Pl. ha a head B2, és a hajó vízszintes, akkor a hajó cellái: B2, C2, D2...)
		Ha így a hajó kilógna a pályáról, akkor a program megfordítja az irányát.
		(Ha a head J5, és a hajó vízszintes, akkor a cellák: J5, I5, H5...)
		A correction egy szorzó, ami segít a programnak eldönteni, merre iteráljon.'''
		correction = stayWithinBounds(head, ship.getLength(), horizontal)
		
		if horizontal: '''Vízszintes iterálás a betűkön'''
			for idx in range(ltr_place, ltr_place + (ship.getLength() * correction), correction):
				cell = ABC[idx] + string(num)
				temp.append(cell)
		else:			'''Függőleges iterálás a számokon'''
			for n in range(num, num + (ship.getLength() * correction), correction):
				cell = ltr + string(n)
				temp.append(cell)
		
		'''Található-e a megadott tartományban másik hajó?'''
		anothership = False
		for c in temp:
			if checkCellForShip(c) != None:
				anothership = True
				break
		
		'''Ha igen, akkor nem lehet oda letenni új hajót.'''
		if anothership:
			print("!! A cellák valamelyikében már van hajó, próbált újra.")
		else:
			ship.setRange(temp)		'''Cellák beállítása'''
		return !anothership 		'''Ha van másik hajó -> a hajó elhelyezése sikertelen (return False)'''
	
	
'''
	def getShipWithLength(length):
		for s in ships:
			if s.getLength == length:
				return s
		return null
'''
	
	'''Megjelöli az adott cellát, tehát kiveszi a lehetséges cellák közül'''
	def markCellOnBoard(cell):
		board[cell[0]].remove(int(cell[1:]))
	
	
	'''Meg van-e jelölve már az adott cella?'''
	def isCellUnmarkedOnBoard(cell):
		return (int(cell[1:]) in board[cell[0]])
	
	
	'''Ha nincs több hajó a listában, akkor vége a játéknak'''
	def checkEndCondition():
		if len(ships) == 0:
			print("JÁTÉK VÉGE - A(z) " + name + " nevű játékos elsüllyedt.")
		else:
			print(name + " játékosnak " + len(ships) + " hajója van még vízen.")

	
	'''Megvizsgálja a torpedózott cellát'''
	def checkForHit(cell):
		if isCellUnmarkedOnBoard(cell):
			markCellOnBoard(cell)
			s = checkCellForShip(cell)
			if s == None:
				print("Nem talált...")
			else:
				s.removeFromRange(cell)
				print("Talált!")
				if len(s.getRange()) == 0:
					ships.remove(s)
					del s
					checkEndCondition()