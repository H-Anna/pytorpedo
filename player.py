
from string import ascii_uppercase '''A-J betűkhöz'''

BOARD_UPPER_BOUND = 10
BOARD_LOWER_BOUND = 0

ABC = ascii_uppercase[BOARD_LOWER_BOUND:BOARD_UPPER_BOUND]


class Player:
	'''Adattagok:
	__board = {} 	dictionary ; Kulcs: A-J, érték: lista 0-9. Azokat a mezőket tárolja, amelyekre még lehet lőni
	__ships = [] 	list ; 5 db hajó. Ha egy hajó elsüllyed, kiveszi a listából. Ha üres a lista, vége a játéknak.
	'''
	
	'''Ellenőrzi, létezik-e ez a cella'''
	def isCellInputCorrect(cell):
		return (cell[0] in ABC) and (int(cell[1:]) in range(BOARD_LOWER_BOUND, BOARD_UPPER_BOUND))

	
	def __init__(self, name):
		__name = name
		__board = {}
		__ships = []
		for letter in list(ABC):
			__board[letter] = []				'''Új oszlopot hoz létre'''
			for n in range(BOARD_LOWER_BOUND,BOARD_UPPER_BOUND):
				__board[letter].append(n)		'''Új sort hoz létre'''
	
	
	def getName():
		return __name
	
	def getShips():
		return __ships
	
	def printShips():
		print("A hajók helyzete:")
		for x in __ships:
			x.printRange()
	
	def getBoard():
		return __board
	
	
	def addShip(length):
		newship = Ship(length)
		__ships.append(newship)
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
		for s in __ships:
			if cell in s.getRange():
				return s
		return None
	
	
	def setShipLocation(ship, head, horizontal = False, omit_print = False):
		if !isCellInputCorrect(head):
			print("Hiba: Nem megfelelő input")
			return False
	
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
			if !omit_print print("!! A cellák valamelyikében már van hajó, próbált újra.")
		else:
			ship.setRange(temp)		'''Cellák beállítása'''
			
		return !anothership 		'''Ha van másik hajó -> a hajó elhelyezése sikertelen (return False)'''
	
	
	'''Megjelöli az adott cellát, tehát kiveszi a lehetséges cellák közül'''
	def markCellOnBoard(cell):
		__board[cell[0]].remove(int(cell[1:]))
	
	
	'''Meg van-e jelölve már az adott cella?'''
	def isCellUnmarkedOnBoard(cell):
		return (int(cell[1:]) in __board[cell[0]])
	
	
	'''Ha nincs több hajó a listában, akkor vége a játéknak'''
	def checkEndCondition():
		if len(__ships) == 0:
			print("A(z) " + __name + " nevű játékos elsüllyedt.")
			return True
		else:
			print(__name + " játékosnak " + len(__ships) + " hajója van még vízen.")
			return False

	
	'''Megvizsgálja a torpedózott cellát'''
	def checkForHit(cell):
		
		if !isCellInputCorrect(cell):
			print("Hiba: Nem megfelelő input")
			return False

		if isCellUnmarkedOnBoard(cell): '''Ha erre a cellára még nem lőttek'''
			markCellOnBoard(cell)
			s = checkCellForShip(cell)
			if s == None:
				print("Nem talált...")
			else:
				s.removeFromRange(cell)
				print("Talált!")
				if len(s.getRange()) == 0:
					__ships.remove(s)
					del s
					'''checkEndCondition()'''
			return True
		else:						'''Ha erre a cellára már lőttek'''
			print("Ez a cella már ismert.")
			return False