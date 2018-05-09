# def wrap(func):
#     def inner():
#         print("正在验证权限...")
#         if True:
#             func()
#         else:
#             print("没有权限")
#
#     return inner
#
#
# # test1=wrap(test1)
# @wrap
# def test1():
#     print("----1----")
#     return 1
#
#
# # test2=wrap(test2)
# @wrap
# def test2():
#     print("----2----")
#     return 2
#
#
# t1 = test1()
# t2 = test2()
# print(t1, t2)


def test_1(func):
    print("get in decorator 1")

    def wrap():
        print("get in inner 1")
        return '<b>' + func() + "</b>"

    return wrap


def test_2(func):
    print("get in decorator 2")

    def wrap():
        print("get in inner 2")
        return '<i>' + func() + "</i>"

    return wrap


# 只要解释器执行到该行代码，则自动装饰，没有等到调用该方法的时候才开始装饰
# t=test_1(test_3)
@test_1
@test_2
def test_3():
    print("get in test_3")
    return "hello world"


if __name__ == '__main__':
    # 调用test_3方法前，已经装饰完毕
    t = test_3()
    print(t)
