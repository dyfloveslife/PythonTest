# list = [5, 4, 4, 3, 1]
# total = 0
# i = 0
# while i < len(list) and list[i] > 0:
#     total += list[i]
#     i += 1
# print(total)
# given_list = [5, 4, 4, 3, 1, -2, -3, -5]
# total = 0
# for element in given_list:
#     if element <= 0:
#         break
#     total += element
# print(total)
# list = [5, 4, 4, 3, 1, -1, -4, -6]
#

# given_list = [5, 4, 4, 3, 1, -2, -3, -5]
# total = 0
# i = 0
# while True:
#     total += given_list[i]
#     i += 1
#     if given_list[i] <= 0:
#         break
# print(total)

# a = ['banana', 'apple', 'microsoft']
# for i in range(len(a)):
#     for j in range(i + 1):
#         #  i = 0 -> j = 0
#         # i = 1 -> j = 0, 1
#         # i = 2 -> j = 0, 1, 2
#         print(a[i])
# total = 0
# for i in range(1, 100):
# if i % 3 == 0:
#     total += i
# elif i % 5 == 0:
#     total += i
# if i % 3 == 0 or i % 5 == 0:
#     total += i
# print(total)
# given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total = 0
# j = len(given_list) - 1
# while given_list[j] < 0:
#     total += given_list[j]
#     j -= 1
# print(total)

# d = {'Tom': 20, 'Jack': 23, 'George': 50}
# for k, v in d.items():
#     print('key:', k)
#     print('value:', v)
#     print(' ')
# class Robot:
#     def __init__(self, n, c, w):
#         self.name = n
#         self.color = c
#         self.weight = w
#
#     def introduce_self(self):
#         print('My name is ' + self.name)
#
#
# class Person:
#     def __init__(self, n, p, i):
#         self.name = n
#         self.personality = p
#         self.is_sitting = i
#
#     def sit_down(self):
#         self.is_sitting = True
#
#     def stand_up(self):
#         self.is_sitting = False
#
#
# r1 = Robot('Tom', 'red', 20)
# r2 = Robot('Jack', 'blue', 30)
#
# p1 = Person('Alice', 'aggressive', False)
# p2 = Person('Luca', 'talkative', True)
#
# p1.robot_owned = r2
# p2.robot_owned = r1
#
# p1.robot_owned.introduce_self()
# p2.robot_owned.introduce_self()

# def are_you_sad(is_rainy, has_umbrella):
#     if is_rainy == True and has_umbrella == False:
#         return True
#     else:
#         return False

# def are_you_sad(is_rainy, has_umbrella):
#     return is_rainy and not has_umbrella
#
#
# print(are_you_sad(True, False))
# print(are_you_sad(True, True))
# def c_greater_than_d_plus_e(c, d, e):
#     return c > d + e
#
#
# print(c_greater_than_d_plus_e(3, 1, 1, ))
# print(c_greater_than_d_plus_e(2, 1, 1))

# a = 1
# b = 2
# if a < b:
#     print('a is less than b')
# else:
#     print('a is not less than b')
# print('outside the if block')

# c = 20
# d = 8
# if c < d:
#     print('c is less than d')
# elif c == d:
#     print('c is equal to d')
# elif c > d + 10:
#     print('c is greater than d by more than 10')
# else:
#     print('c is greater than f')

# e = 9
# f = 8
# if e < f:
#     print('e is less than f')
# else:
#     if e == f:
#         print('e is equal to f')
#     else:
#         print('e is greater than f')
# a = ['banana', 'apple', 'microsoft']
# for element in a:
#     print(element)
# b = [20, 10, 5]
# total = 0
# for e in b:
#     total += e
# print(total)

# a = list(range(1, 5))
# print(a)

# for i in range(1, 10, 2):
#     print(i)

# a = list(range(1, 5))
# print(a)

# total = 0
# for i in range(1, 5):
#     total += i
# print(total)

# total = 0
# for i in range(1, 8):
#     if i % 3 == 0:
#         total += i
# print(total)
# total = 0
# j = 1
# while j < 5:
#     total += j
#     j += 1
# print(total)

# given_list = [5, 4, 4, 3, 1, -2, -3, -5]
# total = 0
# i = 0
# while i < len(given_list) and given_list[i] > 0:
#     total += given_list[i]
#     i += 1
# print(total)


for letter in 'Hello abc':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)
