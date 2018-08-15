'''
# low efficiency
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


for n in range(1, 11):
    print(n, ':', fib(n))
'''

'''
fib_cache = {}


def fib(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)

    fib_cache[n] = value
    return value

for n in range(1, 10):
    print(n, ':', fib(n))
'''

'''
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib(n):
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


for n in range(1, 500):
    print(n, ':', fib(n))
'''

'''
import random


def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return x, y


for i in range(25):
    walk = random_walk(10)
    print(walk, 'Distance from home = ', abs(walk[0]) + abs(walk[1]))
'''

import datetime


class User:
    """A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user information"""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        name_pieces = full_name.split(' ')  # 名片
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2018, 8, 15)
        year = int(self.birthday[0:4])
        month = int(self.birthday[4:6])
        day = int(self.birthday[6:8])
        dob = datetime.date(year, month, day)  # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

# help(User)

# user = User('Dave Bowman', 19950305)
# print(user.name)
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)
user = User('Dave Bowman', '19950305')
print(user.age())