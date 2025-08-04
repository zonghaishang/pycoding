from collections.abc import Generator


def average() -> Generator[float, float, None]:
    total = 0.0
    count = 0.0
    avg = 0.0
    while True:
        term = yield avg
        total += term
        count = count + 1
        avg = total / count


g = average()
next(g)

print(g.send(10))
print(g.send(30))

print(g.close())
