import itertools
import operator

sample = []

print(list(itertools.accumulate(sample)))

print(enumerate('albatroz', 1))
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
print(' ' * 20)
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))
