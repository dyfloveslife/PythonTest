# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))

# import sys
# list = [1, 2, 3, 4]
# it = iter(list)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# import sys
#
#
# def fib(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fib(10)
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# def hello():
#     print('Hello World!')
#
# hello()

# def area(width, height):
#     return width * height
#
#
# def print_hello(name):
#     print('Hello', name)
#
#
# print_hello('Carol')
# w = 1
# h = 2
# print('width =', w, 'height =', h, 'area =', area(w, h))
# def print_me(str):
#     print(str)
#
# print_me('Hello World')

# list = [1, 2, 3, 4]
# list[2] = 5
# print(list)
# def change_int(a):
#     a = 10
#
#
# b = 2
# change_int(b)
# print(b)
# def change_me(mylist):
#     mylist.append([1, 2, 3, 4])
#     print('函数内取值：', mylist)
#     return
#
#
# mylist = [10, 20, 30]
# change_me(mylist)
# print('函数外取值：', mylist)
# 定义函数
# def print_me(str):
#     print(str)
#
#
# 调用函数
# print_me(str='Hello World!')

# def print_info(name, age=30):
#     print('名字：', name)
#     print('年龄：', age)
#     return
#
# print_info(age=50, name='Jack')
# print('============')
# print_info(name='Carol')
# def print_info(arg1, *vartuple):
#     print('输出：')
#     print(arg1)
#     for i in vartuple:
#         print(i)
#     return
#
# print_info(10)
# print_info('hello', 10, 20, 30, 'world')

# def print_info(arg1, **vardict):
#     print('输出：')
#     print(arg1)
#     print(vardict)
#
#
# print_info(1, a=2, b=3)

# def f(a, b, *, c):
#     return a + b + c
#
#
# print(f(1, 2, 3))
# print(f(1, 2, c=3))
# sum = lambda arg1, arg2, var1: arg1 + arg2 * 2
# print('相加后的值为：', sum(10, 20, 2))
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print('函数内：', total)
#     return total
#
#
# total = sum(10, 20)
# print('函数外：', total)

# x = int(2.9)  # 内建作用域
# g_count = 0  # 全局作用域
#
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域

# if True:
#     msg = 'HelloWorld'
#     print(msg)
#
# print(msg)

# def test():
#     msg_inner = 'HelloWorld'
#     print(msg_inner)
#
# print(msg_inner)

# total = 0
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print('函数内是局部变量：', total)
#     return total
#
# sum(10, 20)
# print('函数外是全局变量：', total)
# num = 1
#
# def fun():
#     global num
#     print(num)
#     num = 123
#     print(num)
#
# fun()

# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num = 20
#         print(num)
#
#     inner()
#     print(num)
#
#
# outer()

# def outer():
#     count = 1
#
#     def inner():
#         nonlocal count
#         count = 12
#
#     inner()
#     print(count)
#
#
# outer()

# a = 10
# def test(a):
#     a = a + 1
#     print(a)
#
# test(a)

# sum = lambda x=0, y=0: x ** 1 + y ** 2
# print(sum(y=2, x=3))
# print(sum(3))
# print(sum(y=2))
a = int(3.5)
print(a)