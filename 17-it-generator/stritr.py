s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

print(' ' * 10)

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
