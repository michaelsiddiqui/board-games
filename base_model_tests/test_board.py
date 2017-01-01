# tests for the classes defined in the boards.py module

import unittest

from base_models.board import Board
from base_models.cards import DeckOfCards
from base_models.cards import Card
from base_models.tiles import Tile


class TestBoardMethods(unittest.TestCase):
    """TestCase class containing unit tests for the Board methods

    Starting with three tests:
    i. if a Board object is initialized with no arguments we get an object
        with expected attributes;
        default attribues are: {'rank': 0, 'value': 0, 'num_edges': 4}
    ii. can initialize Board object and inspect the rank and value for
        expected output when not default initialization
    iii. get a reasonable error when I initialize with an unreasonable initial
        condition set
    """
    def setUp(self):
        """Initialize objects for later test methods
        """
        self.test_tile = Tile(rank=2, value=11, num_edges=6)
        list_card_attributes = [
            {'rank': 1, 'value': 1},
            {'rank': 3, 'value': 4},
            {'rank': 4, 'value': 9}
        ]
        self.card_init_list = [
            Card(**init_dict) for init_dict in list_card_attributes
        ]
        self.test_deck = DeckOfCards(card_list=self.card_init_list)
        self.test_deck_list = [self.test_deck]
        self.test_tile_list = [self.test_tile]

    def test_default_initialization(self):
        """Test that when I initialize with no args I get a Board object
        with the expected attributes
        """
        test_board = Board()
        expected_dict = {
            'spaces': [],
            'tiles': [],
            'decks': [],
            'tokens': [],
            'score': None
        }
        self.assertEqual(test_board.spaces, [])
        self.assertEqual(test_board.tiles, [])
        self.assertEqual(test_board.decks, [])
        self.assertEqual(test_board.tokens, [])
        self.assertFalse(test_board.score)
        self.assertEqual(test_board.__dict__, expected_dict)
        self.assertTrue(isinstance(test_board, Board))

    def test_non_default_initialization(self):
        """Test that I can initialize a Board object with args

        will get expected attributes when I inspect them
        """
        initial_attributes = {
            'spaces': ['a', 'b', 'c'],
            'tiles': self.test_tile_list,
            'decks': self.test_deck_list,
            'tokens': [],
            'score': ["Player One Wins!"]
        }
        test_board = Board(**initial_attributes)
        self.assertEqual(test_board.spaces, ['a', 'b', 'c'])
        self.assertEqual(test_board.tiles, self.test_tile_list)
        self.assertEqual(test_board.decks, self.test_deck_list)
        self.assertEqual(test_board.tokens, [])
        self.assertEqual(test_board.score, ["Player One Wins!"])
        self.assertEqual(test_board.__dict__, initial_attributes)
        self.assertTrue(isinstance(test_board, Board))

    def test_non_allowed_initialization(self):
        """Test that I get a reasonable error when Board is improperly created

        """
        initial_attributes = {
            'spaces': ['a', 'b', 'c'],
            'tiles': self.test_tile_list,
            'decks': self.test_deck_list,
            'tokens': [],
            'extra_arg': 'nonsense'
        }
        with self.assertRaises(TypeError) as context:
            Tile(**initial_attributes)
