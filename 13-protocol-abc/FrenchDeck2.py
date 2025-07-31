import random
from collections import abc, namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __delitem__(self, key):
        del self._cards[key]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def insert(self, index, value):
        self._cards.insert(index, value)


if __name__ == '__main__':
    f = FrenchDeck2()
    print(f)
    random.shuffle(f)
    print(f)
