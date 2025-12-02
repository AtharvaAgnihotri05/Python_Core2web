x = 10

def fun():
    x = 20
    def inner():
        nonlocal x
        x += 5
        print("Inner x:", x)
    print(x)
    return inner

ref = fun()
ref()
print("Outer x:", x)

