# here cards and deck classes are defined
# both are written into the cards.py module in this project
# the intention is that cards are a base class to a future tiles class
# which will enable the construction of flexible playing boards later
from collections import deque
import random

from utils import list_type_check

class Card(object):
    """Base class for all card or tile objects in board_game project

    base attributes are only 'rank' and 'value'
    default values initialize to 0 for both attributes
    """
    def __init__(self, rank=0, value=0):
        self.rank = rank
        self.value = value


class DeckOfCards(object):
    """Base class for all collections of card objects

    models a collection of card objects
    default initialization is an empty list

    Description of intended methods:
    i. add_card: add a card object to the deck, default to 'top add'
    ii. deal_card: deal a card from the deck, default to 'top deal'
    iii. shuffle: reorder the list randomly
    iv. show_top: print the attributes of the first card as dict
    v. show_bottom: print the attributes of the last card as dict

    Intended attributes:
    i. card_list: list of cards
    ii. cards_left: list the length of the card list


    Need to make a choice on 'top' versus 'bottom' convention:
        For the purposes here the 'top' of the deck will be card_list[0]
        the bottom will be card_list[n] where n is the list length
        default is 'top add' and 'top deal', in other words LIFO
        keyword option to specify other choice

    TO-DO: is there a way to use the deque class to optimize performance?
    """
    def __init__(self, card_list=[]):
        self.card_list = []
        if card_list:
            type_check = list_type_check(card_list, Card, error=True)
            self.card_list.extend([card for card in card_list])

        # update the cards_left count
        self.cards_left = len(self.card_list)

    def show_top(self):
        """print the attributes of the first card as dict
        """
        return self.card_list[0].__dict__

    def show_bottom(self):
        """print the attributes of the last card as dict
        """
        return self.card_list[self.cards_left - 1].__dict__

    def shuffle(self):
        """reorder the card_list randomly
        """
        # print statement below for earlier debugging
        # print 'shuffling the deck'
        random.shuffle(self.card_list)

    def deal_card(self, bottom_deal=False):
        """deal a card from the deck, default to 'top deal'
        """
        if self.cards_left < 1:
            return None
        elif self.cards_left == 1 or bottom_deal:
            dealt_card = self.card_list.pop()
            self.cards_left = len(self.card_list)
            return dealt_card
        else:
            dealt_card = self.card_list.pop(0)
            self.cards_left = len(self.card_list)
            return dealt_card

    def add_card(self, card_to_add, bottom_add=False):
        """add a card object to the deck, default to 'top add'
        """
        if not isinstance(card_to_add, Card):
            raise TypeError("Can only add Card objects to Deck")

        if self.cards_left < 1 or bottom_add:
            self.card_list.append(card_to_add)
        else:
            self.card_list.insert(0, card_to_add)

        # update the cards_left count
        self.cards_left = len(self.card_list)
