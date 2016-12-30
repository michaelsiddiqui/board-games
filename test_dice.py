# trying out test-driven code development
# this module is meant to contain tests that I expect the classes
# written in 'dice.py' should pass

import unittest
from collections import Counter

from dice import SingleDie
from dice import DiceRoller


class TestSingleDieMethods(unittest.TestCase):
    """TestCase class containing unit tests for the SingleDie methods

    Starting with four tests:
    i. if a SingleDie object is initialized with no arguments we get an object
        with expected attributes;
        num_sices == 6, face_value gets first roll value
    ii. can roll an initialized object and inspect the face value for
        expected output when not default initialization
    iii. can generate a list of values from many rolls and expect to see all
        values in range and no single value getting 'an unreasonable'
        number of outcomes in the list
    iv. get a reasonable error when I initialize with an unreasonable initial
        condition set
    """
    def test_default_initialization(self):
        """Test that when I initialize with no args I get a SingleDie object
        with the expected attributes
        """
        test_die = SingleDie()
        self.assertEqual(type(test_die), type(SingleDie()))
        self.assertEqual(test_die.num_sides, 6)
        self.assertTrue(1 <= test_die.face_value <= 6)

    def test_initialized_with_face_value_greater_than_six(self):
        """Test attributes are correct when initialized with greater than 6

        as the num_sides argument
        """
        test_die = SingleDie(num_sides=12)
        self.assertEqual(type(test_die), type(SingleDie()))
        self.assertEqual(test_die.num_sides, 12)
        self.assertTrue(1 <= test_die.face_value <= 12)

    def test_many_rolls_creates_distribution(self):
        """A list populated by a series of rolls should have expected values

        specifically that across 400 rolls, every number hits once
        no number is >= 250 rolls; no number is <= 10 rolls
        """
        test_die = SingleDie()
        roll_series = [test_die.roll() for i in range(400)]
        roll_counter = Counter(roll_series)
        roll_coverage = [i for i in roll_counter.keys()]
        roll_maximum = max([i for i in roll_counter.values()])
        roll_minimum = min([i for i in roll_counter.values()])
        self.assertEqual(roll_coverage, range(1, 7))
        self.assertTrue(roll_maximum < 250)
        self.assertTrue(roll_minimum > 10)

    def test_initiation_with_zero_faces_raises_value_error(self):
        """SingleDie object cannot be initiated with zero faces

        expect method to raise a value error
        """
        with self.assertRaises(ValueError) as context:
            SingleDie(0)


class TestDiceRollerMethods(unittest.TestCase):
    """TestCase class containing unit tests for the DiceRoller methods

    Starting with four tests:
    i. if a DiceRoller object is initialized with no arguments we get an object
        with expected attributes;
        num_dice == 2; dice_value gets first roll value
    ii. can roll an initialized object and inspect the dice value for
        expected output when not default initialization
    iii. can generate a list of values from many rolls and expect to see all
        values in range and no single value getting 'an unreasonable'
        number of outcomes in the list
    iv. get a reasonable error when I initialize with an unreasonable initial
        condition set
    """
    def test_default_initialization(self):
        """Test when initialized with no args I get a DiceRoller object
        with the expected attributes
        """
        test_dice_roll = DiceRoller()
        dice = test_dice_roll.dice
        num_dice = len(dice)
        dice_sides = [die.num_sides for die in dice]
        self.assertEqual(type(test_dice_roll), type(DiceRoller()))
        self.assertEqual(test_dice_roll.num_sides, 6)
        self.assertEqual(dice_sides, [6, 6])
        self.assertEqual(num_dice, 2)
        self.assertEqual(test_dice_roll.num_dice, 2)
        self.assertTrue(2 <= test_dice_roll.roll_value <= 12)

    def test_initialized_with_greater_than_default_values(self):
        """Test attributes when initialized with greater than default values

        num_sides and num_values greater than 6 and 2, respectively
        """
        test_dice_roll = DiceRoller(num_sides=12, num_dice=4)
        dice = test_dice_roll.dice
        num_dice = len(dice)
        dice_sides = [die.num_sides for die in dice]
        self.assertEqual(type(test_dice_roll), type(DiceRoller()))
        self.assertEqual(test_dice_roll.num_sides, 12)
        self.assertEqual(dice_sides, [12, 12, 12, 12])
        self.assertEqual(num_dice, 4)
        self.assertEqual(test_dice_roll.num_dice, 4)
        self.assertTrue(4 <= test_dice_roll.roll_value <= 48)

    def test_many_rolls_creates_distribution(self):
        """A list populated by a series of rolls should have expected values

        specifically that across 2000 rolls, every number hits once
        no number is >= 700 rolls; no number is <= 20 rolls
        most frequent roll is 7, least frequent is 2 or 12
        """
        test_dice_roll = DiceRoller()
        roll_series = [test_dice_roll.roll() for i in range(2000)]
        roll_counter = Counter(roll_series)
        roll_coverage = [i for i in roll_counter.keys()]
        roll_maximum = max([i for i in roll_counter.values()])
        roll_minimum = min([i for i in roll_counter.values()])
        roll_most_common = roll_counter.most_common(1)
        roll_negative_counter = Counter(
            {face: -1 * freq for face, freq in roll_counter.iteritems()}
        )
        roll_least_common = roll_negative_counter.most_common(2)
        least_common_values = sorted([v[0] for v in roll_least_common])
        self.assertEqual(roll_coverage, range(2, 13))
        self.assertTrue(roll_maximum < 700)
        self.assertTrue(roll_minimum > 20)
        self.assertEqual(roll_most_common[0][0], 7)
        self.assertEqual(least_common_values, [2, 12])

    # TO-DO: write last error-checking test