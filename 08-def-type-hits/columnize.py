from collections.abc import Sequence


def columnize(seq: Sequence[str], num_columns: int = 0) \
        -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(seq) ** 0.5)
        print(len(seq) ** 0.5, num_columns)
    num_rows, reminder = divmod(len(seq), num_columns)
    num_rows += bool(reminder)
    return [tuple(seq[i::num_columns]) for i in range(num_rows)]


animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
table = columnize(animals)
print(table)

for row in table:
    print(''.join(f'{word:10}' for word in row))
