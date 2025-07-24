def deco(func):
    def inner():
        print("running inner()")
        r = func()
        return r

    # print("running inner()")

    return inner


@deco
def target():
    print("running target()")


print(target(), target)
print(target(), target)
