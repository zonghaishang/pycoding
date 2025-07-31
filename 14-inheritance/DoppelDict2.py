import collections


class DoppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


d = DoppelDict(one=1)
d['two'] = 2
print(d)
