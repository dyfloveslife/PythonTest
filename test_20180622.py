'''元组是不可变的
    列表是可变的
'''
# t = 12345, 54321, 'Hello!'
# print(t[0])
# print(t)
# u = t, (1, 2, 3, 4, 5)
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

'''构造包含0个或1个元素的元组'''
# empty = ()
# singleton1 = 'Hello'
# singleton2 = 'Hello',
# print(len(empty))
# print(len(singleton1))
# print(len(singleton2))
# print(singleton1)
# print(singleton2)

'''集合:集合中的元素不会重复且没有顺序
其中符号：^ 表示对称差集，表示元素在a或b中，但不会同时出现在二者中）
'''

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# a = 'orange' in basket
# b = 'crabgrass' in basket
# print(a)
# print(b)

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print('a-b:', a - b)
# print('a|b:', a | b)
# print('a&b', a & b)
# print('a^b:', a ^ b)

# 推导式
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# extend和append的区别
# a = ['a', 'hello', 123]
# b = ('522', 'sad')
# a.extend(b)
# a.append(b)
# print(a)

'''字典，无序的键:值对集合，要求是键必须是唯一的'''
# print(tel)
# print(tel['jack'])
# tel= {'jack': 7000, 'sape': 4139}
# tel['guido'] = 4127
# del tel['sape']
# tel['irv'] = 4128
# print(tel)
# a = list(tel.keys())
# b = sorted(tel.keys())
# c = 'guido' in tel
# d = 'jack' not in tel
# print(a, b, c, d)

# a = dict([('sape', 100), ('guido', 200), ('jack', 300)])
# print(a)
# b = {x: x ** 2 for x in (2, 4, 6)}
# print(b)

# a = dict(sape=4139, guido=4127, jack=4098)
# print(a)

'''当循环遍历字典时，用items()方法提取键和值'''
# knights = {'gallahad': 100, 'robin': 200}
# for k, v in knights.items():
#     print(k, v)

'''当遍历一个序列时，用enumerate()方法可以同时得到位置索引和对应的值'''
# for i, v in enumerate(['a', 'b', 'c']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

'''sorted()对序列进行排序'''
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(set(basket)):
#     print(i)


'''raw_data原始数据，filtered_data过滤后的数据
NaN，Not a Number,不是数，既不是无穷大也不是无穷小。
'''
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

'''从5.7开始'''
