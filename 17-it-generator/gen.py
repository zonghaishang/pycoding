def gen_abc():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


for c in gen_abc():
    print('--->', c)
