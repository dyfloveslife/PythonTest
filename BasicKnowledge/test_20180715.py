# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))
# a.insert(2, -1)
# print(a)
# print(a.index(333))
# a.remove(333)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# stack = [3, 4, 5]
# stack.append(6)
# print(stack)
# stack.append(7)
# print(stack)
# print('===============')
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

# from collections import deque
#
# queue = deque(['Carol', 'Jack', 'Tom'])
# queue.append('Terry')
# queue.append('Michael')
# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)

# a = [x * x for x in range(1, 11) if x % 2 == 0]
# print(a)

# a = [m + n for m in 'ABC' for n in 'abc']
# print(a)
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# a = [[row[i] for row in matrix] for i in range(4)]
# print(a)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# a = {x: x * 2 for x in range(5)}
# print(a)

# person = {'name': 'Carol', 'age': 20, 'gender': 'male'}
# for k, v in person.items():
#     print(k, v)

# for i, v in enumerate(['Carol', 'Jack', 'Mike']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['Carol', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your %s? It is %s.' % (q, a))
#     print('What is your {0}? It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# # for i in sorted(set(basket)):
# #     print(i)

# a = [x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if x < 3]

# for x in range(1, 5):
#     if x > 2:
#         for y in range(1, 4):
#             if x < 3:
#                 x * y
#
# import sys
#
# print(dir(sys))

