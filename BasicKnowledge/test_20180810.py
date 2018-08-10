# s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
# for x in s:
#     print(x[0] + ':', x[1])


# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for x in L:
#     if x in s:
#         s.remove(x)
#     else:
#         s.add(x)
#
# print(s)

# L = []
# x = 1
# while x <= 100:
#     L.append(x * x)
#     x += 1
#
# print(sum(L))

# L = range(1, 101)
# print(sum([i * i for i in L]))

# def firstCharUpper(s):
#     return s[0].upper() + s[1:]
#
#
# print(firstCharUpper('hello'))
# print(firstCharUpper('sunday'))
# print(firstCharUpper('september'))

# for x in range(1, 101):
#     if x % 7 == 0:
#         print(x)

# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in zip(range(1, len(L)), L):
#     print(index, '-', name)
# sum = 0
# d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
# for x in d.values():
#     sum += x
# print(sum / len(d))
# d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
# sum = 0.0
# for k, v in d.items():
#     sum += v
#     print(k, ':', v)
#
# print('average:', sum / len(d))

# print([x * (x + 1) for x in range(1, 100, 2)])

# import math
#
#
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(25, 9, math.sqrt))

# def f(x):
#     return x * x
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(map(f, list1)))
# print(list(map(lambda x: x * x, list1)))

