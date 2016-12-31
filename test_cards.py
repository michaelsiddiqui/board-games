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

    Starting with three tests:
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
        self.assertEqual(test_card.__dict__, {'rank': 0, 'value': 0})
        self.assertEqual(type(test_card), type(Card()))

    def test_non_default_initialization(self):
        """Test that I can initialize a Card object with args

        will get expected attributes when I inspect them
        """
        initial_attributes = {
            'rank': 2,
            'value': 11
        }
        test_card = Card(**initial_attributes)
        self.assertEqual(test_card.rank, 2)
        self.assertEqual(test_card.value, 11)
        self.assertEqual(test_card.__dict__, initial_attributes)

    def test_non_allowed_initialization(self):
        """Test that I get a reasonable error when Card is improperly created

        """
        initial_attributes = {
            'rank': 2,
            'value': 11,
            'extra_arg': 'nonsense'
        }
        with self.assertRaises(TypeError) as context:
            Card(**initial_attributes)


class TestDeckOfCardsMethods(unittest.TestCase):
    """TestCase class containing unit tests for the DeckOfCards methods

    Initial test cases, one per method plus tests for attributes
    and initialization error:
    i. Test default initialization and expected attributes
    ii. Test default initialization plus add_card
    iii. Test initialization with list of Card objects, show attributes
    iv. Test add_card with list initialization
    v. Test deal_card with list initialization
    vi. Test 'bottom' add with list initialization
    vii. Test 'bottom' deal with list initialization
    viii. Test improper initialization (non-Cards in list)
    xi. Test deal_card from empty deck
    x. Three card deck shuffled many times has expected outcome
    xi. Shuffling a deck with many cards results in a new list
    """
    def setUp(self):
        self.card_to_add = Card(rank=2, value=11)
        list_card_attributes = [
            {'rank': 1, 'value': 1},
            {'rank': 3, 'value': 4},
            {'rank': 4, 'value': 9}
        ]
        self.card_init_list = [
            Card(**init_dict) for init_dict in list_card_attributes
        ]
        self.bad_init_list = self.card_init_list + ['nonsense']
        self.large_shuffle_init_list = [
            Card(rank=1, value=i) for i in range(1, 1001)
        ]

    def tearDown(self):
        self.card_to_add = None
        self.card_init_list = []

    def test_default_initialization(self):
        """Test default initialization and expected attributes
        """
        test_deck = DeckOfCards()
        self.assertEqual(test_deck.card_list, [])
        self.assertEqual(test_deck.cards_left, 0)
        with self.assertRaises(IndexError) as context:
            test_deck.show_bottom()
        with self.assertRaises(IndexError) as context:
            test_deck.show_top()

    def test_default_init_plus_add_card(self):
        """Test default initialization and add_card() has expected attributes
        """
        test_deck = DeckOfCards()
        test_deck.add_card(self.card_to_add)
        self.assertEqual(test_deck.card_list, [self.card_to_add])
        self.assertEqual(test_deck.cards_left, 1)
        self.assertEqual(test_deck.show_top(), {'rank': 2, 'value': 11})
        self.assertEqual(test_deck.show_bottom(), test_deck.show_top())

    def test_initialization_with_card_list(self):
        """Test initialization with list of Card objects, show attributes
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)
        self.assertEqual(test_deck.card_list, self.card_init_list)
        self.assertEqual(test_deck.cards_left, 3)
        self.assertEqual(test_deck.show_top(), {'rank': 1, 'value': 1})
        self.assertEqual(test_deck.show_bottom(), {'rank': 4, 'value': 9})

    def test_add_card_to_populated_deck(self):
        """Test add_card with list initialization
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)
        to_add = self.card_to_add
        test_deck.add_card(to_add)
        self.assertEqual(test_deck.card_list, [to_add] + self.card_init_list)
        self.assertEqual(test_deck.cards_left, 4)
        self.assertEqual(test_deck.show_top(), {'rank': 2, 'value': 11})
        self.assertEqual(test_deck.show_bottom(), {'rank': 4, 'value': 9})

    def test_deal_card_from_populated_deck(self):
        """Test deal_card with list initialization
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)
        dealt_card = test_deck.deal_card()
        expected_list = self.card_init_list[1:]
        self.assertEqual(test_deck.card_list, expected_list)
        self.assertEqual(test_deck.cards_left, 2)
        self.assertEqual(test_deck.show_top(), {'rank': 3, 'value': 4})
        self.assertEqual(dealt_card.__dict__, {'rank': 1, 'value': 1})
        self.assertEqual(test_deck.show_bottom(), {'rank': 4, 'value': 9})

    def test_bottom_add_card_to_populated_deck(self):
        """Test 'bottom' add with list initialization
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)
        to_add = self.card_to_add
        test_deck.add_card(to_add, bottom_add=True)
        self.assertEqual(test_deck.card_list, self.card_init_list + [to_add])
        self.assertEqual(test_deck.cards_left, 4)
        self.assertEqual(test_deck.show_top(), {'rank': 1, 'value': 1})
        self.assertEqual(test_deck.show_bottom(), {'rank': 2, 'value': 11})

    def test_bottom_deal_card_from_populated_deck(self):
        """Test 'bottom' deal with list initialization
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)
        dealt_card = test_deck.deal_card(bottom_deal=True)
        expected_list = self.card_init_list[:-1]
        self.assertEqual(test_deck.card_list, expected_list)
        self.assertEqual(test_deck.cards_left, 2)
        self.assertEqual(test_deck.show_top(), {'rank': 1, 'value': 1})
        self.assertEqual(dealt_card.__dict__, {'rank': 4, 'value': 9})
        self.assertEqual(test_deck.show_bottom(), {'rank': 3, 'value': 4})

    def test_intialization_with_non_card_in_list(self):
        """Test improper initialization (non-Cards in list)
        """
        with self.assertRaises(TypeError) as context:
            test_deck = DeckOfCards(card_list=self.bad_init_list)

    def test_deal_from_empty_deck(self):
        """Test deal_card from empty deck
        """
        test_deck = DeckOfCards()
        self.assertEqual(test_deck.card_list, [])
        self.assertEqual(test_deck.cards_left, 0)
        dealt_card = test_deck.deal_card()
        self.assertFalse(dealt_card)

    def test_shuffling_short_deck_many_times(self):
        """Three card deck shuffled many times has expected outcome
        """
        test_deck = DeckOfCards(card_list=self.card_init_list)

        # make an empty array of nine by nine
        # count as follows: first row counts positions of first card
        #   first column +1 when in top of deck, second +1 in middle of deck
        #   and so on, expect that over 10000 shuffles each value in array
        #   will be close to 3000, going to assert that the average of all
        #   values is between 2700 and 3300 to start
        location_count_array = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        for i in range(10000):
            test_deck.shuffle()
            value_list = [card.value for card in test_deck.card_list]
            n = 0
            for value in value_list:
                if value == 1:
                    location_count_array[0][n] += 1
                elif value == 4:
                    location_count_array[1][n] += 1
                elif value == 9:
                    location_count_array[2][n] += 1
                n += 1
        minimum_count = min([min(row) for row in location_count_array])
        maximum_count = max([max(row) for row in location_count_array])
        self.assertTrue(minimum_count > 3100)
        self.assertTrue(maximum_count < 3500)

    def test_shuffling_large_deck_creates_new_list(self):
        """Shuffling a deck with many cards results in a new list
        """
        init_values = [card.value for card in self.large_shuffle_init_list]
        test_deck = DeckOfCards(card_list=self.large_shuffle_init_list)
        test_deck.shuffle()
        final_values = [card.value for card in test_deck.card_list]
        self.assertNotEqual(init_values, final_values)
