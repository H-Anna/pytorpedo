
from ship import *

'''A-J betűkhöz'''
from string import ascii_uppercase

BOARD_UPPER_BOUND = 10
BOARD_LOWER_BOUND = 0

ABC = ascii_uppercase[BOARD_LOWER_BOUND:BOARD_UPPER_BOUND]


class Player:
	'''Adattagok:
	__board = {} 	dictionary ; Kulcs: A-J, érték: lista 0-9. Azokat a mezőket tárolja, amelyekre még lehet lőni
	__ships = [] 	list ; 5 db hajó. Ha egy hajó elsüllyed, kiveszi a listából. Ha üres a lista, vége a játéknak.
	'''
	
	'''Ellenőrzi, létezik-e ez a cella'''
	def isCellInputCorrect(self, cell):
		return (cell[0] in ABC) and (int(cell[1:]) in range(BOARD_LOWER_BOUND, BOARD_UPPER_BOUND))

	
	def __init__(self, name):
		self.__name = name
		self.__board = {}
		self.__ships = []
		for letter in list(ABC):
			'''Új oszlopot hoz létre'''
			self.__board[letter] = []
			for n in range(BOARD_LOWER_BOUND,BOARD_UPPER_BOUND):
				'''Új sort hoz létre'''
				self.__board[letter].append(n)
	
	
	def getName(self):
		return self.__name
	
	def getShips(self):
		return self.__ships
	
	def printShips(self):
		print("A hajók helyzete:")
		for x in self.__ships:
			x.printRange()
	
	def getBoard(self):
		return self.__board
	
	
	def addShip(self, length):
		newship = Ship(length)
		self.__ships.append(newship)
		return newship
	
	'''Hajó letételekor ne indexeljünk a játéktéren kívül'''
	def stayWithinBounds(self, head, length, horizontal):
		tmp = 0
		'''Ha a hajó vízszintes, akkor az oszlopokat kell vizsgálni; ha függőleges, akkor a sorokat'''
		if horizontal:
			tmp = list(ABC).index(head[0])
		else:
			tmp = int(head[1:])
		
		if (tmp + length-1) > BOARD_UPPER_BOUND - 1: return -1
		else: return 1
	
	
	'''Megnézi, hogy van-e az adott cellán hajó, ha igen, visszatér vele'''
	def checkCellForShip(self, cell):
		for s in self.__ships:
			if cell in s.getRange():
				return s
		return None
	
	
	'''Megjelöli az adott cellát, tehát kiveszi a lehetséges cellák közül'''
	def markCellOnBoard(self, cell):
		self.__board[cell[0]].remove(int(cell[1:]))
	
	
	'''Meg van-e jelölve már az adott cella?'''
	def isCellUnmarkedOnBoard(self, cell):
		return (int(cell[1:]) in self.__board[cell[0]])
	
	
	def setShipLocation(self, ship, head, horizontal = False, omit_print = False):
		if not(self.isCellInputCorrect(head)):
			print("Hiba: Nem megfelelő input")
			return False
	
		'''A hajó celláit tartalmazó lista'''
		temp = []
		
		'''A betű'''
		ltr = head[0]
		'''A betű helye az ABC-ben'''
		ltr_place = list(ABC).index(head[0])
		'''A szám'''
		num = int(head[1:])
		
		'''Alaphelyzetben a program a "head" cellát úgy veszi, mintha a bal szélső/legészakibb cella lenne.
		(Pl. ha a head B2, és a hajó vízszintes, akkor a hajó cellái: B2, C2, D2...)
		Ha így a hajó kilógna a pályáról, akkor a program megfordítja az irányát.
		(Ha a head J5, és a hajó vízszintes, akkor a cellák: J5, I5, H5...)
		A correction egy szorzó, ami segít a programnak eldönteni, merre iteráljon.'''
		correction = self.stayWithinBounds(head, ship.getLength(), horizontal)
		
		'''Vízszintes iterálás a betűkön ; Függőleges iterálás a számokon'''
		if horizontal:
			for idx in range(ltr_place, ltr_place + (ship.getLength() * correction), correction):
				cell = ABC[idx] + str(num)
				temp.append(cell)
		else:
			for n in range(num, num + (ship.getLength() * correction), correction):
				cell = ltr + str(n)
				temp.append(cell)
		
		'''Található-e a megadott tartományban másik hajó?'''
		anothership = False
		for c in temp:
			if self.checkCellForShip(c) != None:
				anothership = True
				break
		
		'''Ha igen, akkor nem lehet oda letenni új hajót.'''
		if anothership:
			if not(omit_print): print("!! A cellák valamelyikében már van hajó, próbált újra.")
		else:
			'''Cellák beállítása'''
			ship.setRange(temp)
		
		'''Ha van másik hajó -> a hajó elhelyezése sikertelen (return False)'''
		return not(anothership)
	

	'''Ha nincs több hajó a listában, akkor vége a játéknak'''
	def checkEndCondition():
		if len(self.__ships) == 0:
			print("A(z) " + self.__name + " nevű játékos elsüllyedt.")
			return True
		else:
			print(self.__name + " játékosnak " + str(len(self.__ships)) + " hajója van még vízen.")
			return False

	
	'''Megvizsgálja a torpedózott cellát'''
	def checkForHit(self, cell):
		
		if not(self.isCellInputCorrect(cell)):
			print("Hiba: Nem megfelelő input")
			return False
	
		'''Ha erre a cellára még nem lőttek'''
		if self.isCellUnmarkedOnBoard(cell):
			self.markCellOnBoard(cell)
			s = self.checkCellForShip(cell)
			
			if s == None: print("Nem talált...")
			else:
				s.removeFromRange(cell)
				print("Talált!")
				if len(s.getRange()) == 0:
					self.__ships.remove(s)
					del s
			
			return True
		else:
			'''Ha erre a cellára már lőttek'''
			print("Ez a cella már ismert.")
			return False