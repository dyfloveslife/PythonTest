# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
# print(reduce(fn, map(char2num,'13579')))

# def normalize(name):
#     return name[:1].upper() + name[1:].lower()
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
#
#
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_dibisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_dibisible(n), it)
#
#
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# print(sorted([1, 2, 5, -7, 1, -1], key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# def by_name(t):
#     return t[0]
#
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print(L2)


# def by_score(t):
#     return t[1]
#
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_score, reverse=True)
# print(L2)


# def now():
#     print('123')
#
# now()

# a = int('12345', 16)
# print(a)

# __author__ = 'Carol'
#
# import sys
#
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello,world!')
#     elif len(args == 2):
#         print('Hello,%s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__ == '__main__':
#     test()

# class Studnet(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s:%s' % (self.name, self.score))
#
#
# bart = Studnet('Bart Simpson', 59)
# lisa = Studnet('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()


# class Person(object):
##    这里就是初始化你将要创建的实例的属性
# def __init__(self, hight, weight, age):
#     self.hight = hight
#     self.weight = weight
#     self.age = age
#
##    定义你将要创建的实例所有用的技能
# def paoniu(self):
#     print('你拥有泡妞的技能')
#
# def eat(self):
#     print('you can eat')
#
#
##开始创建实例
# zhangsan = Person(170, 50, 1)
# lisi = Person(175, 100, 30)
#
##你的实例开始使用它的技能
# zhangsan.paoniu()
# lisi.eat()
# fpath = r'F:\system.txt'
#
# with open(fpath, 'r') as f:
#     print(f.read())


# import os
# print(os.name)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))

# from datetime import datetime
# now = datetime.now()
# print(now)
# print(type(datetime))
# dt = datetime(2018, 7, 3, 23, 59)
# print(dt)

# from PIL import Image

# im = Image.open('test.jpg')
# w, h = im.size
# print('Original image size:%sx%s' % (w, h))
# im.thumbnail((w // 2, h // 2))
# print('Resize image to:%sx%s' % (w // 2, h // 2))
# im.save('thumbnail.jpg')
# assert isinstance(im, Image.Image)
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')

# im = Image.open('test.jpg')
# print(im.format, im.size, im.mode)
# im.show()


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
word_font = ImageFont.truetype('arial.ttf', 35)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=word_font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
