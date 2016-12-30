# here cards and deck classes are defined
# both are written into the cards.py module in this project
# the intention is that cards are a base class to a future tiles class
# which will enable the construction of flexible playing boards later


class Card(object):
	"""Base class for all card or tile objects in board_game project

	base attributes are only 'rank' and 'value'
	default values initialize to 0 for both attributes
	"""
	def __init__(self, rank=0, value=0):
		self.rank = 0
		self.value = 0


class DeckOfCards(object):
	"""
	"""
	pass