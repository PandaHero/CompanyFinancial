# 对无参数的函数进行修饰
def func1(funcName):
    print("----func----")

    def func_in():
        print("----func_in----1----")
        funcName()
        print("----func_in----2----")

    return func_in


@func1
def test():
    print("----test----")


test()
print("*" * 10)


# 对有参数的函数进行修饰
def func2(funcName):
    def func2_in(*args, **kwargs):
        funcName(*args, **kwargs)

    return func2_in


@func2
def test2(name, *args, sex="girl"):
    print(name, sex, *args)


test2("haha", 1, 2, 3, 4, sex="boy")
print("*" * 10)


# 对有返回值的函数进行装饰
def func3(funcName):
    def func1_in():
        ret = funcName()  # 保存返回来的haha
        return ret  # 返回保存值

    return func1_in


@func3
def test3():
    return "hello world"


ret = test3()
print("test3 return value is %s" % ret)
print("*" * 10)


# 通用装饰器
def func4(funcName):
    def func4_in(*args, **kwargs):
        ret = funcName(*args, **kwargs)
        return ret

    return func4_in


@func4
def test4():
    return "haha"



num1=[1,2,3,4]

def test5():
    num = 200
    x = num + 100
    locals()[x] = 200
    # globals()[num1].append(5)



test5()
# print(num1)

print(test4())
