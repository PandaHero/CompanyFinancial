# class Test(object):
#     def __init__(self):
#         # 私有化属性(方法),禁止导入，但是类对象或者子类可以访问
#         self._name = "jack"
#         # 避免与子类中的属性命名冲突，无法再外部直接访问(通过名字重整可以访问)
#         self.__age = 100
#         self.sex = "boy"
#
#     def get_age(self):
#         print("-------getterAge-------")
#         return self.__age
#
#     def set_age(self, new_age):
#         print("-------setterAge-------")
#         self.__age = new_age
#
#     def get_name(self):
#         print("-------getterName-------")
#         return self._name
#
#     def set_name(self, new_name):
#         print("-------setterName-------")
#         self._name = new_name
#
#     @property
#     def sex(self):
#         return self.sex
#
#     @sex.setter
#     def sex(self, new_sex):
#         if isinstance(new_sex, str):
#             self.sex = new_sex
#         else:
#             print("sex is not str")
#
#     # age = property(get_age, set_ag e)
#     # name = property(get_name, set_name)
#
#
# t = Test()
# # print(t._name)
# # print(t._Test__age)
# # t.name = "haha"
# # t.age = 50
# # print(t.name, t.age)
# t.sex = "girl"
# print(t.sex)
class Test(object):
    def __init__(self):
        self._age = 10

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


t = Test()
t.age = 100
print(t.age)
