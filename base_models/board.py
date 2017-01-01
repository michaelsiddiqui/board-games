# board module for Board class
# The Board class is intended to model the 'game board'
# or generic playing surface for games included in the project
# for a given point of play (during or between a 'turn')
# the Board object should be able to fully assess the current state
# of the game objects shared between the players
# (the entire 'state' of the 'turn' not inclusive of
# the objects within a certain players 'hand'). Some examples:
# i. for poker the board would be the community cards;
# ii.for craps the board would be the various betting lines
#   with the bets laid on;
# iii.for Monopoly it would be the physical board with player tokens,
#   property improvements, the chance and community chest decks;
# iv. for Codenames this would be the word tiles, and the agent cards
#   (either covering the tiles or in an off-tile deck);
# v. for Settlers this would be the hexagonal tiles with built structures
#   and numbered tokens, as well as the played Development cards, and the
#   Development card deck;
# etc. for other games to elaborate as reasonable

from cards import DeckOfCards
from tiles import Tile


class Board(object):
    """Base class for Board objects board_game project

    Models the playing surface of a given board game
    Board type objects contain the following attributes:
        spaces: type list, default empty, to be populated with integers,
            strings, or nested list; this will denote an empty surface for
            tiles or cards to be placed
        tiles: collection of tiles, to be placed in spaces or to be held in
            reserve
        decks: type list of DeckOfCards, empty when not relevant or has
            n decks of playing cards
        tokens: type list, to be populated with a concept of tokens to
            be determined later -- want the concept of tokens to be able to
            mean improvements or buildings or chips
        score: to be worked out --  this will be None for early development

    Additional attributes may be added later.
    """
    def __init__(self, spaces=[], tiles=[], decks=[], tokens=[], score=None):
        self.spaces = spaces
        self.tiles = []

        # idea: is there a way to make a reusable util function to check
        #       a list for containing the constrained object type?
        #       may be reusing this functionality more
        if tiles:
            tiles_type_check = all([isinstance(obj, Tile) for obj in tiles])
            if not tiles_type_check:
                raise TypeError("Expect list to only contain Tile objects")
            else:
                self.tiles.extend([obj for obj in tiles])

        self.decks = []

        # idea: is there a way to make a reusable util function to check
        #       a list for containing the constrained object type?
        #       may be reusing this functionality more
        if decks:
            deck_check = all([isinstance(obj, DeckOfCards) for obj in decks])
            if not deck_check:
                raise TypeError("Expect list to only contain Tile objects")
            else:
                self.decks.extend([obj for obj in decks])

        self.tokens = tokens
        self.score = score