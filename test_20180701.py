'''三种迭代方式'''
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:  # 迭代key
#     print(key, end='')
# for value in d.values():  # 迭代value
#     print(value, end='')
# for k, v in d.items():  # 迭代key和value
#     print(k, v)

# for ch in 'abc':
#     print(ch)

'''如何判断一个对象是否是迭代对象？'''
# from collections import Iterable

# print(isinstance('abc', Iterable))  #判断str是否可以迭代
# print(isinstance(123, Iterable))  #判断整数是否可以迭代
# print(isinstance([4, 5, 6], Iterable))  #判断list是否可以迭代

'''利用enumerate函数把一个list变成（索引-元素）对'''

# for i, n in enumerate(['a', 'b', 'c']):
#     print(i,n)

# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     max = L[0]
#     min = L[0]
#     for i in L:
#         if max < i:
#             max = i
#         elif min > i:
#             min = i
#     return (min, max)
#
#
# list = [3, 4, -1.6, 6, 12, 5, 6, 1, 10]
# print(findMinAndMax(list))

'''列表生成式'''
# L = list(range(1, 11, 2))
# print(L)

# list = [x * x for x in range(1, 11) if x % 2 == 0]
# print(list)
# list = [m + n for m in 'ABC' for n in 'XYZ']
# print(list)
# import os
# list = [d for d in os.listdir('.')]
# print(list)

# d = {'X': 'A', 'Y': 'B', 'Z': 'C'}
# list = [k + '=' + v for k, v in d.items()]
# print(list)

# L1 = ['Hello', 'World', 'IBM', 'Apple', 18]
# L2 = [s.upper() for s in L1 if isinstance(s, str)]
# print(L2)

'''一边循环一边计算的机制，称为生成器：generator'''
# L = [x * x for x in range(10)]  #list
# print(L)
g = (x * x for x in range(10))  # generator
for n in g:
    print(n,end=' ')