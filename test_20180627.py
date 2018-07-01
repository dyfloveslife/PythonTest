# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# # person('Tom', 20)
# # person('Bob', 25, city='Beijing')
# # person('Adam', 35, gender='M', job='Eigineer')
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# # person('Jack', 24, city=extra['city'], job=extra['job'])
# person('Jack', 24, **extra)

# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=12345)

# 符号*后面的参数被视为命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# person('Jack', 35, city='Beijing', job='Engineer')

'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数。
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b = ', b, 'c =', c, 'args =', args, 'kw =', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
#
# # f1(1, 2)
# # f1(1, 2, c=3)
# # f1(1, 2, 3, 'a', 'b')
# # f1(1, 2, 3, 'a', 'b', x=99)
# # f2(1, 2, d=99, ext=None)
#
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)

# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)  # 把每一步的乘积传入到递归函数中
#
# print(fact(5))

'''
1.先将A柱的n-1个盘子移到B柱；
2.再将A柱的最后一个盘子移到C柱；
3.最后将B柱的n-1个盘子移到C柱。
'''
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
#
#
# move(3, 'A', 'B', 'C')

'''切片'''
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r = []
# n = 5
# for i in range(n):
#     r.append(L[i])
# print(r)
# print(L[0:3])  # 不包括索引3
# print(L[1:3])
# print(L[-5:-2])
# L = list(range(0, 110, 10))
# print(L)
# print(L[:])
#
# L = (0, 1, 2, 3, 4, 5)
# print(L[1:3])
# print(L[:2])
# print(L[2:])
# print(L)
# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s
# print(trim('hello   '))
# print(trim('  hello'))
# print(trim('  hello  world   '))

# L = ['a', 'b', 'c', 'd', 'e', 'f']
# print(L[:1])  # 不包括索引1的数
# print(L[1:])
# print(L[-1:])
# print(L[:-1])
'''迭代'''