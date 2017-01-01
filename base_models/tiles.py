# module to contain Tile class as an extension of the Card class
# naively Tiles just have shape therefore will just add attribute 'edges'

from cards import Card


class Tile(Card):
    """Tile class extends Card class with an attribute num_edges

    """
    def __init__(self, num_edges=4, rank=0, value=0):
        super(Tile, self).__init__(rank=rank, value=value)
        self.num_edges = num_edges
