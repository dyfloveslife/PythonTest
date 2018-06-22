# for w in words:
#     print(w, len(w))
# words = ['cat', 'windows', 'defenestrate']
# # for w in words[:]:
# #     if len(w) > 6:
# #         words.insert(0, w)
# # print(words)
# 输出5到9内的数字
# for i in range(5, 10):
#     print(i)
# 输出0到9内，以3为步进值的数字
# for i in range(0, 10, 3):
#     print(i)
# 输出-10到-100内，以20为步进值的数字
# for i in range(-10, -100, -20):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# b = len(a)  # b=5
# for i in range(b):
#     print(i, a[i])
# print(list(enumerate(a, start=1)))
# num = list(range(5, 10))
# print(num)
# for i in range(0, 10):
#     print(i, end=' ')
# print('over')


# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n += 1
# print('end')
'''
对于for嵌套，之前理解错了，
应该是从第一个列表中每次取出一个，
再从第二个列表中也每次取出一个，
然后组合成一个新的列表，
新列表中包含所有组合.
计算过程如下：
2%2=0,N
3%2=3,Y
4%2=0,N
5%2=1,5%3=2,5%4=1,Y
6%2=0,N
7%2=1,7%3=1,7%4=3,7%5=2,7%6=1,Y
看下面的例子
'''
# list1 = ['a', 'b', 'c', 'd']
# list2 = [1, 2]
# new_list = []
# for i in list1:
#     for j in list2:
#         new_list.append([i, j])
# print(new_list)

# for i in range(2, 7):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, 'is a prime number.')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print('Found an even number', num)
#         continue
#         print('Found a number', num)

'''
从4.5 pass语句开始看
'''