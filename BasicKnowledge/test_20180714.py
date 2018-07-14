x = int(3.3)

x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()

outer()



x = int(3.3)

x = 0
def outer():
    x = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()


x = int(3.3)
x = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()

x = int(3.3)
g = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()