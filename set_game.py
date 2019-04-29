NUMBERS = [1,2,3]
SYMBOLS = ['DIAMOND','SQUIGGLE','OVAL']
SHADINGS = ['STRIPPED','SOLID', 'OPEN']
COLORS = ['RED','GREEN','PURPLE']

class Card:
	def __init__(self, number, symbol, shading, color):
		if any([
			number not in NUMBERS,
			symbol not in SYMBOLS,
			shading not in SHADINGS,
			color not in COLORS
		]):
			raise ValueError('Неправильные параметры карты')
	
		self.number = number
		self.symbol = symbol
		self.shading = shading
		self.color = color

	def __repr__(self):
		return f'{self.number} || {self.symbol} || {self.shading} || {self.color}'

def check_set(cards):
	valid_len = (1,len(cards))
	len_set = lambda x: len(set(x)) in valid_len
	return any([
		len_set([card.number for card in cards]),
		len_set([card.symbol for card in cards]),
		len_set([card.shading for card in cards]),
		len_set([card.color for card in cards]),
		])