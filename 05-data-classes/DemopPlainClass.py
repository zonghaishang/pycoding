class PlainClass:
    a: int
    b: float = 1.1
    c = "Hello World!"


print(PlainClass.__annotations__)

print(PlainClass.c)
print(PlainClass.b)
print(PlainClass.a)