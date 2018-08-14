# import json
#
# '''
# json_file = open("f:/Python_test/BasicKnowledge/movie_1.txt", 'r', encoding='utf-8')
# moive = json.load(json_file)
# json_file.close()
#
# print(moive)
# print(json.dumps(moive, ensure_ascii=False))
# print(moive['title'])
# print(moive['actors'])
# print(moive['release_year'])
# value = """
#     {"title": "Tron: Legacy",
#     "composer": "Daft Puck",
#     "release_year" : 2010,
#     "budget": 170000000,
#     "actors": null,
#     "won_oscar": false
#     }"""
#
# tron = json.loads(value)
# print(tron)
# '''
# moive2 = {}
# moive2['title'] = 'Minority Report'
# moive2['director'] = 'Steven Spielberg'
# moive2['composer'] = 'John Williams'
# moive2['actors'] = ['Tom Cruise', 'Colin Farrell',
#                     'Samantha Morton', 'Max von Sydow']
# moive2['is_awesom'] = True
# moive2['budget'] = 102000000
# moive2['cinematographer'] = 'Janusz Kami\u0144ski'
#
# file2 = open('f:/Python_test/BasicKnowledge/movie_2.txt', 'w', encoding='utf-8')
# json.dump(moive2, file2, ensure_ascii=False)
# file2.close()

# import datetime

# launch_date = datetime.date(2018, 8, 14)
# launch_time = datetime.time(16, 39, 1)
# launch_datetime = datetime.datetime(2018, 8, 14, 16, 39, 2)

# print(launch_date)
# print(launch_time)
# print(launch_datetime)
# print(launch_time.hour)
# print(launch_time.minute)
# print(launch_time.second)

# now = datetime.datetime.today()
# print(now)
# print(now.microsecond)

# moon_landing = '7/20/1969'
# moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m/%d/%Y')
# print(moon_landing_datetime)
# print(type(moon_landing_datetime))

# print(dir())
#
#
# def f():
#     pass
#
#
# f
# print(dir())
# print(f)

# import math
#
#
# def volume(r):
#     '''Return volume of something'''
#     v = (4.0 / 3.0) * math.pi * r ** 3
#     return v
#
#
# print(volume(2))
# help(volume)

# post2 = dict(message='SS Cotopaxi', language='English')
# post2['user_id'] = 209
# post2['datetime'] = '20180814'
# # print(help(post2.get))
# # loc = post2.get('location', None)  # 当 location 也就是 key 不在 post2 中时,返回 None
# for key in post2.keys():
#     value = post2[key]
#     print(key, '=', value)
#
# for key, value in post2.items():
#     print(key, '=', value)


# Display 10 random numbers from interval [0, 1)
import random

# print(dir(random))
# print(help(random.random))

'''
for i in range(10):
    print(random.random())
'''

'''
# Generate random numbers from interval [3, 7)
def my_random():
    """
    1.Call random(): in[0, 1)
    2.Scale number(multiply by 4): in [0, 4)
    3.Shift number(add 3): in [3, 7)
    4.return
    """
    return 4 * random.random() + 3

for i in range(10):
    print(my_random())
'''

'''
# 随机函数可用于构建定制的随机数生成器
for i in range(10):
    print(random.uniform(3, 7))
'''

'''
for i in range(10):
    print(random.normalvariate(0, 9))
'''

'''
for i in range(20):
    print(random.randint(1, 6))  # Return random integer
'''

''''
outcomes = ['Jack', 'Tom', 'Carol']
for i in range(10):
    print(random.choice(outcomes))  # Return element from a list
'''

