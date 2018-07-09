# list = [5, 4, 4, 3, 1]
# total = 0
# i = 0
# while i < len(list) and list[i] > 0:
#     total += list[i]
#     i += 1
# print(total)
# list = [5, 4, 4, 3, 1, -1, -4, -6]
# total = 0
# for element in list:
#     if element <= 0:
#         break
#     total += element
# print(total)
# list = [5, 4, 4, 3, 1, -1, -4, -6]
#
# total = 0
# i = 0
# while True:
#     total += list[i]
#     i += 1
#     if list[i] <= 0:
#         break
# print(total)

# a = ['banana', 'apple', 'republic']
# for i in range(len(a)):
#     for j in range(i + 1):
#         i = 0 -> j = 0
#         i = 1 -> j = 0, 1
#         i = 2 -> j = 0, 1, 2
# print(a[i])
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
# print(j)
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
def c_greater_than_d_plus_e(c, d, e):
    return c > d + e


print(c_greater_than_d_plus_e(3, 1, 1, ))
print(c_greater_than_d_plus_e(2, 1, 1))
