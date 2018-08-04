import copy

a = [1, 2, [3, 4]]
b = a.copy()
print(b)
print(id(a[0]), id(b[0]))
print(id(a[2][0]), id(b[2][0]))
print(id(a), id(b))