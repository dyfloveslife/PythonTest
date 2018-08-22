import sys


class Dog:

    def __del__(self):
        print('-----over------')


dog1 = Dog()
dog2 = dog1  # dog1和dog2都指向Dog对象

del dog1  # 删除dog1引用，这时Dog对象还存在，不会调用__del__
del dog2  # 删除dog2引用，这时Dog对象就不存在了，python会自动调用__del__方法
print('===============')
'''
像上面的情况，如果只删除了一个引用dog1或dog2，那么在最后程序结束之后，系统也会自动调用__del__方法
也就是说，如果在程序结束时，有些对象还存在，那么python解释器会自动调用__del__方法完成清理工作
'''
print(sys.getrefcount(dog1))  # 获取对象引用计数的个数