n = int(input())
name1 = input()
name2 = input()
name3 = input()

def move(n, a, b, c):
    if n == 1:
        print("%s->%s" % (a, c))
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(n, name1, name2, name3)
