# another instance of test-driven development
# here I am testing the implementation cards and deck classes
# both written into the cards.py module in this project
# the intention is that cards are a base class to a future tiles class
# which will enable the construction of flexible playing boards later

import unittest

from cards import Card
from cards import DeckOfCards

class TestCardMethods(unittest.TestCase):
    """TestCase class containing unit tests for the Card methods

    Starting with four tests:
    i. if a Card object is initialized with no arguments we get an object
        with expected attributes;
        default attribues are: {'rank' : 0, 'value' : 0}
    ii. can initialize Card object and inspect the rank and value for
        expected output when not default initialization
    iii. get a reasonable error when I initialize with an unreasonable initial
        condition set
    """
    def test_default_initialization(self):
        """Test that when I initialize with no args I get a Card object
        with the expected attributes
        """
        test_card = Card()
        self.assertEqual(test_card.rank, 0)
        self.assertEqual(test_card.value, 0)
        self.assertEqual(test_card.__dict__, {'rank' : 0, 'value' : 0})
