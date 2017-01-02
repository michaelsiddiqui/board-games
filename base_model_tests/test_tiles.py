# simple tests here just default initialization
# and non-default initialization

import unittest

from base_models.tiles import Tile


class TestTileMethods(unittest.TestCase):
    """TestCase class containing unit tests for the Tile methods

    Starting with three tests:
    i. if a Tile object is initialized with no arguments we get an object
        with expected attributes;
        default attribues are: {'rank': 0, 'value': 0, 'num_edges': 4}
    ii. can initialize Tile object and inspect the rank and value for
        expected output when not default initialization
    iii. get a reasonable error when I initialize with an unreasonable initial
        condition set
    """
    def test_default_initialization(self):
        """Test that when I initialize with no args I get a Tile object
        with the expected attributes
        """
        test_tile = Tile()
        expected_dict = {
            'rank': 0, 'value': 0, 'num_edges': 4
        }
        self.assertEqual(test_tile.rank, 0)
        self.assertEqual(test_tile.value, 0)
        self.assertEqual(test_tile.__dict__, expected_dict)
        self.assertTrue(isinstance(test_tile, Tile))

    def test_non_default_initialization(self):
        """Test that I can initialize a Tile object with args

        will get expected attributes when I inspect them
        """
        initial_attributes = {
            'rank': 2,
            'value': 11,
            'num_edges': 6
        }
        test_tile = Tile(**initial_attributes)
        self.assertEqual(test_tile.rank, 2)
        self.assertEqual(test_tile.value, 11)
        self.assertEqual(test_tile.__dict__, initial_attributes)

    def test_non_allowed_initialization(self):
        """Test that I get a reasonable error when Tile is improperly created

        """
        initial_attributes = {
            'rank': 2,
            'value': 11,
            'num_edges': 6,
            'extra_arg': 'nonsense'
        }
        with self.assertRaises(TypeError) as context:
            Tile(**initial_attributes)
