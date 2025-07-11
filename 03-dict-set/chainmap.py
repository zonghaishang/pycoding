from collections import ChainMap

d1 = {1:2}
d2 = {3:4}
d = ChainMap(d1, d2)


print(d.get(1), d.get(3), d.get(5))