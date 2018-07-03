# 可以级联比较
# a, b, c = 1, 2, 3
# print(a < b == c)
'''
not 优先级最高，or 优先级最低
所以 A and not B or C 等效于 (A and (not B)) or C
'''
# string1, string2, string3 = 'Tom', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)

# a = (1, 2, 3) < (1, 2, 4)
# b = 'ABC' < 'C' < 'Pascal' < 'Python'
# print(a)
# print(b)

'''导入模块'''
# import fibo
#
# fibo.fib(1000)
# print(fibo.fib2(100))
# print(fibo.__name__)

# from fibo import fib, fib2
# from fibo import *
#
# fib(500)

# import sys
#
# sys.ps1 = 'C>'
# print(sys.ps1)

# import fibo, sys
#
# print(dir(fibo))
# print(dir(sys))

# a = [1, 2, 3, 4, 5]
# import fibo
#
# fib = fibo.fib
# print(dir())

s = 'Hello,World!'
# str(s)
# repr(s)
# print(str(s))
# print(repr(s))

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '.'
# print(s)

# hello = 'hello,world\n'
# hellos = repr(hello)
# print(hellos)

# result = repr((x, y, ('spam', 'eggs')))
# print(result)


'''
其中，rjust返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。
如果指定的长度小于字符串的长度则返回原字符串
'''
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x * x * x).rjust(4))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

'''zfill方法返回指定长度的字符串，原字符串右对齐，前面填充0'''

# str = "this is string example....wow!!!"
# print(str.zfill(40))

# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(20))

# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))
# print('This {food} is {adjective}.'.format(
#     food='spam', adjective='absolutely horrible'
# ))
# print(f'This {"spam"} is {"absolutely horrible"}.')

# print('The story of {0},{1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# contents = 'eels'
# print('My hovercraft is full of {}.'.format(contents))
# print('My hovercraft is full of {!r}.'.format(contents))

import math

# print('The value of PI is approximately {0:.3f}.'.format(math.pi))

''' 字典的items函数以列表返回可遍历的(键,值)元组数组。'''
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print('{0:10}--->{1:10d}'.format(name, phone))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack:{0[Jack]:d};Sjoerd:{0[Sjoerd]:d};'
#       'Dca:{0[Dcab]:d}'.format(table))

# table = {'Tom': 4127, 'Jack': 4098, 'Carol': 8637678}
# print('Jack:{Jack:d};Tom:{Tom:d};Carol:{Carol:d}'.format(**table))

# import math

# print('The value of PI is a approximately %1.3f' % math.pi)

'''从7.2开始'''
# f = open(r'F:\Python_test\1.txt', 'r')
# print(f.readline())
# for line in f:
#     print(line, end='')
# f = open('1.txt', 'w')
# print(f.write('This is a test\n'))

# f = open('1.txt', 'w')
# value = ('the answer', 42)
# s = str(value)
# print(f.write(s))

# f = open('1.txt', 'rb+')
# f.write(b'0123456789abcdef')
# a = f.seek(-3, 2)
# print(f.read(1))
# f.close()
# f.read()

# f = open('1.txt', 'rb+')
# with open('1.txt', 'r') as f:
#     read_data = f.read()
# f.close()
# print(f)

# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Oops!That was no valid number.Try angin...")
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS err:{0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
'''异常处理'''


# try:
#     1 / 1
# except Exception as e:
#     print("0不能被除")
# else:
#     print("没有异常")
# finally:
#     print("最后总是要执行我")


# def try_exception(num):
#     try:
#         return int(num)
#     except ValueError as arg:
#         # print("This {0} is not a number".format(arg))
#         print(arg, "is not a number.")
#     else:
#         print("This is a number.")
# try_exception('xxx')

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#     x, y = inst.args
#     print('x =', x)
#     print('y =', y)

def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error.', err)

'''从8。4开始'''