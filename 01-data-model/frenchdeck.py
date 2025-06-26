import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._Cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._Cards)

    def __getitem__(self, item):
        return self._Cards[item]

    def __setitem__(self, key, value):
        self._Cards[key] = value


if __name__ == '__main__':
    deck = FrenchDeck()
    print(Card(rank='A', suit='spades'))
    print('length:', len(deck))
    print('deck 0:', deck[0])
    print('random check:', random.choice(deck))
    print('before>>')
    for card in deck:
        print(card)
    print('after>>')
    random.shuffle(deck)
    for card in deck:
        print(card)
    print('sort------')
    for card in sorted(deck, key=spades_high):
        print(card)

