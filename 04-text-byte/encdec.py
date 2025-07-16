s = 'café'
print(len(s))

b = s.encode("utf-8")
print(b)

print(b.decode('utf-8'))

cafe = bytes(s, encoding='utf-8')
print(cafe)

print(cafe[0])
print(cafe[1:])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])