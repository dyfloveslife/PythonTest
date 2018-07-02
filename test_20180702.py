'''
打印杨辉三角的实现步骤：
1、yield N：函数遇到yield返回N=[1]
2、N.append(0)：给N添加一个元素，此时N=[1，0]
3、range(len(N))=[0,1]
4、N = [N[i-1]+N[i] for i in [0,1]]
5、N = [N[0-1]+N[0] , N[1-1]+N[1]]
6、N = [0+1 , 1+0] = [1,1]
'''
# def triangles():
#     N = [1]
#     while True:
#         yield N
#         N.append(0)
#         N = [N[i - 1] + N[i] for i in range(len(N))]
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

'''
可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance()判断一个对象是否是Iterable对象
'''
# from collections import Iterable
# print(isinstance([], Iterable))
# print(isinstance({},Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))
'''
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''

# print(x for x in range(10))
# print([x for x in range(10)])
# print(abs(-10))
# print(abs)
# x = abs
# print(x)

# f = abs
# print(f(-10))
'''高阶函数->传入函数'''