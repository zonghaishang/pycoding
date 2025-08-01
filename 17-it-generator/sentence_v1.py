import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return 'Sequence(%s)' % reprlib.repr(self.text)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration()
        _word = self.words[self.index]
        self.index += 1
        return _word


s = Sentence('"The time has come," the Walrus said,')
for word in s:
    print(word)
