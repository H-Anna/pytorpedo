
'''Meg lehet változtatni a hajók hosszát, illetve ezáltal a számukat. Alapértelmezetten 1-5 hosszú hajók vannak.'''
SHIPLENGTH_LOWER_BOUND = 1
SHIPLENGTH_UPPER_BOUND = 6

class Ship:

	'''Adattagok:
		length: hajó hossza
		range: hajót tartalmazó cellák listája, eleinte üres, a játékos tölti fel a Player osztályon keresztül
	'''
	
	def __init__(self, leng):
		self.__length = leng
		self.__range = []
	
	def sinking(self):
		print("A(z) " + str(self.__length) + ". számú hajó elsüllyedt!")
	
	def getLength(self):
		return self.__length
	
	def getRange(self):
		return self.__range
	
	def setRange(self, r):
		self.__range = r
	
	def removeFromRange(self, cell):
		self.__range.remove(cell)
	
	def printRange(self):
		str = ""
		for x in self.__range:
			str += x + "  "
		print(str)