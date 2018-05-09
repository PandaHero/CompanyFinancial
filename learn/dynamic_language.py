from types import MethodType


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self, speed):
        print(speed)

    # 给类添加静态方法
    @staticmethod
    def test():
        print("----staticMethod----")

    @classmethod
    def test2(cls):
        print("----classMethod----")


# 给实例添加方法
def eat(self):
    print(self.name + "正在吃东西")


s = Student("haha", 12)
s2 = Student("heihei", 20)
# 动态给实例添加属性
s.sex = "boy"
# 动态给类添加属性
Student.id = 1
# 给实例动态添加方法
s.eat = MethodType(eat, s)
s2.eat = MethodType(eat, s2)
s.eat()
s2.eat()
