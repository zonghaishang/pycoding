fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=lambda fruit: fruit[::-1]))

for obj in [abs, str, "Hi!"]:
    print(obj, callable(obj))
