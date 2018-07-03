# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))
#
#
# def concat(*args, sep="/"):
#     return sep.join(args)
#
#
# print(concat("earth", "mars", "venus"))

# a = list(range(3, 6))
# print(a)

# args = [3, 7]
# a = list(range(*args))
# print(a)


# def parrot(voltage=1000, state=1, action=2):
#     print("--This parrot wouldn't", action, end=" ")
#     print("is you put", voltage, "volts through it.", end=" ")
#     print("E's", state, "!")
#
#
# d = {"voltage": "four million"}
# parrot(**d)

# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(42)
# print(f(0))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), ]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# def my_function():
#     '''Do nithing,but document it.
#
#     No,really, it doesn't do anyting.
#     And also a line.
#     '''
#     pass
#
#
# print(my_function.__doc__)

# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
#
#
# print(f('spam'))
#
#
# '''从5.数据结构开始看'''
#
# '''返回x出现的次数'''
# # print(a.count(333), a.count(66.25), a.count('x'))
# '''在第i个位置插入元素x'''
# # a.insert(2, -1)
# '''在列表末尾添加一个元素'''
# # a.append(333)
#
# '''删除列表中第一个值为 x 的元素'''
# # a.remove(333)
#
# '''元素按位置反转'''
# # a.reverse()
#
# '''对列表中的项进行排序'''
# # a.sort()
#
# '''删除列表中给定位置的元素并返回它。
#     如果没有给定位置，a.pop()将会删除并返回
#     列表中的最后一个元素。需要print(a.pop())
# '''
# # a = [66.25, 3331, 333, 1, 1234.5]
#
# '''append()进栈，pop()出栈'''
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# stack.pop()
# stack.pop()
# stack.pop()
# # print(stack.pop())
# print(stack)


# '''入队/出队的Demo'''
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Tom")
# queue.pop()
# print(queue)
'''从5.1.3开始看'''
