import itertools
import collections.abc

f = filter(lambda x: x < 3, itertools.count(1, .5))
print(isinstance(f, collections.abc.Iterable))
print(isinstance(itertools.count(1, .5), collections.abc.Iterable))

# for i in itertools.count(1, 10):
#     print(i)

# print(list(filter(lambda x: x < 3.0, itertools.count(1, 10))))
print(list(filter(lambda x: x < 3, range(1, 4))))
