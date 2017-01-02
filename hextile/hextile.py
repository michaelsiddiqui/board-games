# see if I can model up a simple game
# resources are earned upon particular dice rolls
# according to arrangements of tiles and their values
# on a HextileBoard


from base_models.board import Board
from base_models.dice import DiceRoller
from base_models.tiles import Tile
from base_models.cards import Card
from base_models.utils import list_type_check


class HextileBoard(Board):
    """
    """
    def __init__(self, **kwargs):
        super(HextileBoard, self).__init__(**kwargs)


class Hextile(Tile):
    """
    """
    def __init__(self, num_edges=6, rank=0, value=0):
        super(Hextile, self).__init__(rank=rank, value=value)
        self.num_edges = num_edges


class TurnManager(object):
    """
    """
    def __init__(self, board, players=[]):
        self.board = board
        self.players = []
        if players:
            player_list_check = list_type_check(players, Player, error=True)
            self.players.extend([obj for obj in players])


class Player(object):
    """
    """
    def__init__(self, name='player', position=1):
        self.name = name
        self.position = position

