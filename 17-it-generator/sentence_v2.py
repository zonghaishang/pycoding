import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for _word in self.words:
            yield _word

    def __repr__(self):
        return 'Sequence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
for word in s:
    print(word)
