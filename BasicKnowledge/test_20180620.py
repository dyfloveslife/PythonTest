# squares = []
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)

# squares = list(map(lambda x: x ** 2, range(10)))
# squares = [x ** 2 for x in range(10)]
# print(squares)

# a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)
'''abs函数返回绝对值'''
# vec = [-4, -2, 0, 2, 4]
# a = [abs(x) for x in vec]
# print(a)
'''strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。'''

# freshfruit = [' banana', 'loganberry', 'passion fruit ']
# a = [weapon.strip() for weapon in freshfruit]
# print(a)
# a = [(x, x ** 2) for x in range(6)]
# print(a)

# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for elem in vec for num in elem])

from math import pi

'''round(x[,n]) 方法返回浮点数x的四舍五入值。

'''
# a = [str(round(pi, i)) for i in range(1, 7)]
# print(a)

# matrix 矩阵
# row   行
'''实现将3行4列转置成4行3列'''
# a = [[row[i] for row in matrix] for i in range(4)]
# print(a)

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# print(transposed)
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# a = list(zip(*matrix))
# print(a)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# del a[2:4]
# # del a[:]
# # del a
# a.append(32)
# print(a)

'''从5.3开始看'''