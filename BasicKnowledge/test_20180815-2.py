'''
# g = lambda x: 2 * x + 1
# print(g(100))
'''

'''
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein',
                 'Arthus C. Clarke', 'Frank Herbert']

# help(scifi_authors.sort)
scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)
'''

# import math
# from functools import reduce

'''
radii = [1, 3, 4, 5, 6, 77, 8]


def area(r):
    return math.pi * (r ** 2)


print(list(map(area, radii)))
'''

'''
temps = [('Berlin', 29), ('Cairo', 30), ('Buenos Aires', 1),
         ('Los Angeles', 26), ('Tokoy', 27), ('China', 30)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
print(list(map(c_to_f, temps)))
'''

'''
import statistics

data = [1.3, 4.3, 65, 0.1, -0.4]
# avg = statistics.mean(data)
# print(list(filter(lambda x: x > avg, data)))

multiplier = lambda x, y: x * y
print(reduce(multiplier, data))
'''

'''
planets = [('Caorl', 23, 182), ('Jack', 25, 180), ('Tom', 21, 179)]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)
'''