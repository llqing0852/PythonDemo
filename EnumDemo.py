from enum import Enum, unique
import time
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Tuh = 4
    Fri = 5
    Sat = 6

@unique
class Gender(Enum):
    Male = 0
    Femail = 1

class Student(object):
    def __init__(self,name,gender):
        self._name = name
        self._gender = gender
    def __call__(self):
        print('My name is %s, I a\'m %s' %(self._name,self._gender.name))

#装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if(__name__ == '__main__'):
    #s = Student('Harry',Gender.Male)
    #s()
    now()