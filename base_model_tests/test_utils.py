# test functions and classes in the utils module

import unittest

from base_models.utils import list_type_check
from base_models.cards import Card


class TestListTypeCheck(unittest.TestCase):
    """Test three usage options for list_type_check_function

    i. list with all items of accepted class; returns True
    ii. list with a non-accepted item; returns False
    iii. list with a non-accepted item and error=True; raises TypeError
    """
    def setUp(self):
        """Initialize objects for later test methods
        """
        list_card_attributes = [
            {'rank': 1, 'value': 1},
            {'rank': 3, 'value': 4},
            {'rank': 4, 'value': 9}
        ]
        self.card_list_correct = [
            Card(**init_dict) for init_dict in list_card_attributes
        ]
        self.card_list_incorrect = self.card_list_correct + ['nonsense']

    def test_correct_list_check(self):
        """Test check on a list with all expected classes
        """
        check_boolean = list_type_check(self.card_list_correct, Card)
        self.assertTrue(check_boolean)

    def test_incorrect_list_check(self):
        """Test check on a list with a non accepted class included
        """
        check_boolean = list_type_check(self.card_list_incorrect, Card)
        self.assertFalse(check_boolean)

    def test_incorrect_list_with_error(self):
        """Test check on incorrect list when error=True
        """
        with self.assertRaises(TypeError) as context:
            list_type_check(self.card_list_incorrect, Card, error=True)
