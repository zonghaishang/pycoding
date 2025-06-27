
import typing

ll:typing.TypeAlias = list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.insert(0,99)
lst.append(88)
lst.extend([100, 101])
print(lst)
print('-'*20)
symbols = '$¢£¥€¤'
arr = [ord(n) for n in symbols]
print(arr)
print('-'*20)
arr = (ord(n) for n in symbols)
print(list(arr))

print('-'*20)
print(ll([1,2,3]))