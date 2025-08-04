import itertools

print(list(itertools.groupby('LLLLAAGGG')))

for key, group in itertools.groupby('LLLLAAGGG'):
    print(key, ' -> ', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

print('max:', max([1, 2, 6, 4, 5, 5]))
