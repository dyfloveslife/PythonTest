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

# L = list(range(1, 11, 2))
# print(L)
'''列表生成式'''

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
# g = (x * x for x in range(1, 10, 2))  # generator
# for n in g:
#     print(n, end=' ')


# 打印小于100的斐波那契数列
# def fib1(n):
#     a, b = 1, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print('done')


# 打印斐波那契数列的前100个数
# def fib2(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b, end=' ')
#         a, b = b, a + b
#         n += 1
#     print('done')
#
#
# fib1(100)
# fib2(100)


# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield 3
#     print('step3')
#     yield 5
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# for n in fib(6):
#     print(n)

# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return L
#
# for n in fab(5):
#     print(n)

'''
yield 的作用就是把一个函数变成一个 generator，
带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield。
'''
'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，
生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
每次中断都会通过 yield 返回当前的迭代值。
'''


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# print(fib(10))
