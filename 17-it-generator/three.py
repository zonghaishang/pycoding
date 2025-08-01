import itertools

g = itertools.takewhile(lambda x: x < 3, itertools.count(1, .5))

while True:
    print(next(g))
