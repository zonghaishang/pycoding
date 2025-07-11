
from collections.abc import Mapping, MutableMapping

mydict = {}

print('isinstance(mydict, Mapping)', isinstance(mydict, Mapping))
print('isinstance(mydict, MutableMapping)', isinstance(mydict, MutableMapping))

tt = (1,2,(3,4))
print(hash(tt))


test = [1,2,3,4,5,6]
dd: dict = mydict.fromkeys(test, -1)
print(mydict)
print(dd)

r=dd.__getitem__(1)
print('dd.__getitem__(1)', r)

r=dd.get(7, 7)
print('dd.get(7, __default=7)', r)

dd.update({1:2, 3:4})
print(dd)

