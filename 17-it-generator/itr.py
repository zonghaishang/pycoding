import itertools
import operator

sample = []

print(list(itertools.accumulate(sample)))

print(enumerate('albatroz', 1))
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
