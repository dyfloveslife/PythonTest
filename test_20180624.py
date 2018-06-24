# raise Exception('Hi')

# try:
#     raise NameError('Hi')
# except NameError:
#     print('An exception flew by')
#     raise

# try:
#     raise KeyboardInterrupt
# except:
#     print('This i except home')
# finally:
#     print('Goodbye,World')
#
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is ", result)
#     finally:
#         print("finally")
#
#
# # divide(2, 1)
# # divide(2, 0)
# divide("2", "1")
#
# for line in open("1.txt"):
#     print(line, end="")

# with open("1.txt") as f:
#     for line in f:
#         print(line, end="")


'''
 在Python中，当引用一个变量的时候，对这个变量的搜索是按:
 - 本地作用域(Local)；
 - 嵌套作用域(Enclosing function locals)；
 - 全局作用域(Global)；
 - 内置作用域(builtins模块)
 以上顺序来进行的，即所谓的LEGB规则。
然而当在一个函数内部为一个变量赋值时，并不是按照上面所说LEGB规则来首先找到变量，之后为该变量赋值。
在Python中，在函数中为一个变量赋值时，有下面这样一条规则:
“当在函数中给一个变量名赋值是(而不是在一个表达式中对其进行引用)，
Python总是创建或改变本地作用域的变量名，
除非它已经在那个函数中被声明为全局变量.”
'''

'''
global关键字主要作用是声明变量的作用域。
global语句可以用来指明某个特定的变量位于全局作用域并且应该在那里重新绑定
如果想为一个在函数外的变量重新赋值，并且这个变量会作用于许多函数中时，就需要告诉python这个变量的作用域是全局变量。
此时用global语句就可以变成这个任务.
首先：python使用的变量，在默认情况下一定是用局部变量。
其次：python如果想使用作用域之外的全局变量，则需要加global前缀。

'''

# a = 5
# def test():
#     '加了global，在函数内部是可以改变外面的全局变量'
#     global a
#     a = 1
#     print("In test function:", a)
# test()
# # 由于在函数中加了global，所以在函数内部成功修改了全局变量的数值
# # 此时全局变量被重新定义为1
# print("In global:", a)
# def fun():
#     return a
# fun()
# print(a)


'''
nonlocal语句表示否定当前命名空间的作用域，寻找父函数的作用域并绑定对象。
使用nonlocal关键字可以在一个嵌套的函数中修改嵌套作用域中的变量.
'''


def func():
    count = 1
    def foo():
        count = 12
    foo()
    print(count)
func()
'''
  上面的程序中，在嵌套的foo函数中，对变量count赋值，同样会创建一个新的变量，而非使用count = 1语句中的count;
  如果要修改嵌套作用域中的count，就要使用nonlocal关键字了.
'''


def func():
    count = 1
    def foo():
        nonlocal count
        count = 12
    foo()
    print(count)
func()

# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
# scope_test()
# print("In global scope:", spam)
'''从9.3开始'''
