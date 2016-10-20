import random
import unittest


class DeckOfCard():

    def __init__(self, suits=None, values=None):
        '''
        Create new deck of cards with suits and values
        if suit or value is None, create deck with default ones
        '''
        if suits is None:
            self.suits = ('clubs', 'diamonds', 'hearts', 'spades')
        else:
            self.suits = suits
        if values is None:
            self.values = {'A': 14,
                           'K': 13,
                           'Q': 12,
                           'J': 11,
                           '10': 10,
                           '9': 9,
                           '8': 8,
                           '7': 7,
                           '6': 6,
                           '5': 5,
                           '4': 4,
                           '3': 3,
                           '2': 2
                           }
        else:
            self.values = values

        self.generate(self.suits, self.values.keys())

    def generate(self, suits_list, values_list):
        '''
        Generate a deck of card - list of dicts
        List - deck
        Dict - card
        Dict have 2 keys - value and suit
        '''
        deck_list = []
        for suit in suits_list:
            for value in values_list:
                card_dict = {}
                card_dict['suit'] = suit
                card_dict['value'] = value
                deck_list.append(card_dict)
        self.deck = deck_list

    def random_card(self):
        return random.choice(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def compare(self, card_1, card_2):
        '''
        Compare 2 cards with value name
        Value for compare get is self.values
        '''
        value_1 = self.values[card_1['value']]
        value_2 = self.values[card_2['value']]
        if value_1 > value_2:
            return card_1
        elif value_1 < value_2:
            return card_2
        else:
            return 'Cards equally'

    def check_card_index(self, card):
        return self.deck.index(card)


class DeckOfCardTestCase(unittest.TestCase):

    def setUp(self):
        '''
        Crete new deck with default suits and values
        '''
        self.test_deck = DeckOfCard()

    def test_generate(self):
        '''
        Check count of cards in deck
        '''
        count_cards = len(self.test_deck.suits)*len(self.test_deck.values)
        self.assertEqual(count_cards, len(self.test_deck.deck))

    def test_shuffle(self):
        '''
        Test shufle of deck
        '''
        check_deck = self.test_deck.deck[:]
        self.test_deck.shuffle()
        self.assertEqual(len(check_deck), len(self.test_deck.deck))
        self.assertFalse(check_deck == self.test_deck)

    def test_check_index(self):
        '''
        Get fifth card id deck and check they index in deck
        '''
        card = self.test_deck.deck[5]
        index = self.test_deck.check_card_index(card)
        self.assertEqual(index, 5)

    def test_random_card(self):
        card = self.test_deck.random_card()
        index = self.test_deck.check_card_index(card)
        self.assertEqual(card, self.test_deck.deck[index])

    def test_compare(self):
        card_1 = {'value': '4', 'suit': 'spades'}
        card_2 = {'value': '9', 'suit': 'spades'}
        self.assertEqual(self.test_deck.compare(card_1, card_2), card_2)

    def test_sort_deck_suit(self):
        '''
        Create new deck with only diamonds suit
        and check other suit in deck
        '''
        suit_deck = DeckOfCard(suits=('diamonds',))
        check_other_suit = False
        for card in suit_deck.deck:
            if card['suit'] != 'diamonds':
                check_other_suit = True
        count_cards = len(suit_deck.suits)*len(suit_deck.values)
        self.assertEqual(count_cards, len(suit_deck.deck))
        self.assertFalse(check_other_suit)

    def test_sort_deck_value(self):
        '''
        Create new deck with only 'A' value
        and check other value in deck
        '''
        value_deck = DeckOfCard(values={'A': 14})
        check_other_values = False
        for card in value_deck.deck:
            if card['value'] != 'A':
                check_other_values = True
        count_cards = len(value_deck.suits)*len(value_deck.values)
        self.assertEqual(count_cards, len(value_deck.deck))
        self.assertFalse(check_other_values)


if __name__ == '__main__':
    unittest.main()
