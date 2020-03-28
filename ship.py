
'''Meg lehet változtatni a hajók hosszát, illetve ezáltal a számukat. Alapértelmezetten 1-5 hosszú hajók vannak.'''
SHIPLENGTH_LOWER_BOUND = 1
SHIPLENGTH_UPPER_BOUND = 6

class Ship:

	'''Adattagok:
		length: hajó hossza
		range: hajót tartalmazó cellák listája, eleinte üres, a játékos tölti fel a Player osztályon keresztül
	'''
	
	def __init__(self, leng):
		__length = leng
		__range = []
	
	def __del__(self):
		print("A(z) " + __length + ". számú hajó elsüllyedt!")
	
	def getLength():
		return __length
	
	def getRange():
		return __range
	
	def setRange(r):
		__range = r
	
	def removeFromRange(cell):
		__range.remove(cell)
	
	def printRange():
		str = ""
		for x in __range:
			str += x + "  "
		print(str)