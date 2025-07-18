from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
]

for m in sorted(metro_data, key=itemgetter(1)):
    print(m)

print('-' * 20)

cc = itemgetter(1, 0)
for m in metro_data:
    print(cc(m))
