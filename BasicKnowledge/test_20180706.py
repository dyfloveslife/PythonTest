# var1 = 10
# var2 = var3 = 10.1
# var4, var5, var6 = 5, 6, 'hello'
# print(var1, var2, var3, var4, var5, var6)
# a, b, c, d = 1, 3.14, True, 1 + 2j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a = 100
# result = isinstance(a, int)
# print(result)

# print('1 + 2 =', 1 + 2)
# print('2 - 1 =', 2 - 1)
# print('1 * 2 =', 1 * 2)
# print('13 / 5 =', 13 / 5)
# print('13 // 5 =', 13 // 5)
# print('13 % 5 =', 13 % 5)
# print('2 ** 3 =', 2 ** 3)

# var = 123
# isinstance(var, int)  # 输出True
# isinstance(var, str)  # 输出False
# isinstance(var, string)  # 报错

# list1 = [0, 1, 2, 'a', 'abc']
# list2 = ['def', 3, 4]
# print('1.', list1)  # 输出完整的列表
# print('2.', list1[:])  # 输出完整的列表
# print('3.', list1[0])  # 输出列表中第一个元素
# print('4.', list1[-1])  # 输出列表中最后一个元素
# print('5.', list1[1:3])  # 输出列表中第二个到第三个元素，因为有冒号，所以不包括右侧
# print('6.', list1[:-1])  # 输出列表中除了最后一个元素以外的所有元素，同样的，因为有冒号，所以不包括右侧
# print('7.', list1 + list2)  # 将列表进行连接

# list = [1, 2, 3, 4, 5]
# list[0] = 'number'  # 这里将数字1改为了number
# list[2:4] = [100, 200]  # 这里进行了切片操作
# print(list)


# tuple1 = (1, 2, 'abc', 3.14, 'def')
# tuple2 = (4, 5, 'ghi')
# print(tuple1)  # 输出tuple1元组全部元素
# print(tuple1[0])  # 输出tuple1元组第一个元素
# print(tuple1[1:3])  # 输出tuple1元组第二个到第三个元素,因为有冒号，所以不包括右侧右侧
# print(tuple1[2:])  # 输出tuple1元组从第三个开始的所有元素
# print(tuple1 * 2)  # 输出两遍tuple1元组
# print(tuple1 + tuple2)  # 连接元组

# set1 = {1, 2, 2, 3, 'a', 'a', 'b', 'c'}
# print(set1)
#
# 进行成员测试
# if 'a' in set1:
#     print('a 在集合中')
# else:
#     print('a 不在集合中')
#
# 进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a - b)  # 差集，输出在a中，但不在b中的元素
# print(a | b)  # 并集
# print(a & b)  # 交集
# print(a ^ b)  # a和b不同时存在的元素

# dic1 = {'name': 'Carol', 'gender': 'male', 'age': 18}
# print(dic1)
# print(dic1['name'])
# print(dic1.keys())
# print(dic1.values())


list1 = [0, 1, 2, 'a', 'abc']
list2 = ['def', 3, 4]
print(list1)  # 输出完整的列表
print(list1[:])  # 输出完整的列表
print(list1[0])  # 输出列表中第一个元素
print(list1[-1])  # 输出列表中最后一个元素
print(list1[1:3])  # 输出列表中第二个到第三个元素，因为有冒号，所以不包括右侧
print(list1[:-1])  # 输出列表中除了最后一个元素以外的所有元素，同样的，因为有冒号，所以不包括右侧
print(list1 + list2)  # 将列表进行连接
print(list1[1::2])  # 注意这个写法，它表示[索引:索引:步长]，即每隔2个元素去一次元素