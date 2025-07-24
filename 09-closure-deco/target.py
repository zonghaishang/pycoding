def deco(func):
    def inner():
        print("running inner()")
        func()

    # print("running inner()")

    return inner


@deco
def target():
    print("running target()")


print(target(), target)
print(target(), target)
