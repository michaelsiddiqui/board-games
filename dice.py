# module to contain class that models a single die of variable sides
# and a class that use multiple dice to model random rolls

from random import randint


class SingleDie(object):
    """Models a single die with a variable number of sides

    Initialization default set to six sides
    Automatically 'rolled' upon initialization
    """
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.face_value = 0
        self.roll()

    def roll(self):
        """Rolls the SingleDie

        Args:
            self: the class instance object SingleDie

        Returns:
            face_value: a random integer between one and num_sides
        """
        self.face_value = randint(1, self.num_sides)
        return self.face_value


class DiceRoller(object):
    """Models a container for multiple dice

    This class is used to represent rolling multiple dice all at one time
    """
    def __init__(self, num_sides=6, num_dice=2):
        self.num_sides = num_sides
        self.num_dice = num_dice
        self.dice = [
            SingleDie(num_sides=num_sides) for i in range(num_dice)
        ]
        self.roll_value = 0
        self.roll()

    def roll(self):
        """Rolls the DiceRoller

        Args:
            self: the class instance object SingleDie

        Returns:
            face_value: a random integer between num_dice
                and num_dice * num_sides
        """
        self.roll_value = sum([die.roll() for die in self.dice])
        return self.roll_value
        