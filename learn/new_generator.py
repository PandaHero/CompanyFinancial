# 生成器
# a = (x for x in range(100))
# print(next(a))

def fib(time):
    n = 0
    a, b = 0, 1
    while n < time:
        yield b
        a, b = b, a + b
        n += 1


c=fib(5)
next(c)


