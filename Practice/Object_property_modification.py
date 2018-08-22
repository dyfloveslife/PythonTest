'''
class Dog:

    def __init__(self, new_name):
        self.name = new_name
        self.__age = 0  # 私有属性在类外部无法直接进行访问

    def set_age(self, new_age):
        if 0 < new_age < 100:
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age


# 对象属性直接修改
dog = Dog('小白')
# dog.age = -10
# print(dog.age)

# 对象方法修改
dog.set_age(-10)
age = dog.get_age()
print(age)

dog.__age = 100
print(dog.__age)
'''

'''
class Message:
    @staticmethod
    # 定义私有方法
    def __send_message():
        print('正在发送短信...')

    # 定义公有方法
    def send_message(self, new_money):
        if new_money > 0:
            self.__send_message()
        else:
            print('余额不足，请先充值...')


msg = Message()
msg.send_message(10)
# msg.send_message(-4)
'''

'''
# 调用被重写的父类方法

class Animal:
    def eat(self):
        print('--eat--')

    def sleep(self):
        print('--sleep--')

    def run(self):
        print('--run--')


class Dog(Animal):
    def bark(self):
        print('--bark--')


class TomDog(Dog):
    def fly(self):
        print('--fly--')

    def bark(self):
        print('--violent bark--')

        # 第一种调用被重写的父类方法
        # Dog.bark(self)

        # 第二种
        super().bark()

tom_dog = TomDog()
tom_dog.fly()
tom_dog.bark()
tom_dog.eat()
'''

'''
class A:
    """
    如果调用的是 继承父类中的公有方法，
    则可以在这个公有方法中访问父类中的私有属性；
    但是，如果在子类中实现了一个公有方法，
    则这个方法不能够调用继承父类中的私有方法和私有属性
    """
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print('--test1--')

    def __test2(self):
        print('--test2--')

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)

b = B()
b.test1()
# b.__test2()  #不可调用
# print(b.num1)
# print(b.__num2)  # 不可调用

# b.test3()
b.test4()  # 不可调用
'''

# 多态
'''
class Dog(object):
    def print_self(self):
        print('This is a dog')

class Tom_dog(Dog):
    def print_self(self):
        print('This is a Tom_dog')

# 函数
def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Tom_dog()
introduce(dog1)
introduce(dog2)
'''

'''
class Tool(object):
    # 类属性
    num = 0

    # 实例方法
    def __init__(self, new_name):
        # 实例属性
        self.name = new_name
        # Tool.num += 1

tool1 = Tool('123131321')
tool2 = Tool('asc')
print(Tool.num)
'''


class Game(object):
    # 类属性
    num = 0

    # 实例方法
    def __init__(self):
        # 实例属性
        self.name = 'Carol'

    # 类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 静态方法
    @staticmethod
    def print_menu():
        print('==========')


game = Game()

Game.add_num()  # 可通过类的名字调用类方法
game.add_num()  # 也可通过类的实例对象调用类方法

print(Game.num)

Game.print_menu()  # 可通过类的名字调用静态方法
game.print_menu()  # 也可通过实例对象调用静态方法