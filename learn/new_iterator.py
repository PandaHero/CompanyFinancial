from collections import Iterator
from collections import Iterable
from collections import Generator

# 判断是否是迭代器
# print(isinstance(100, Iterator))
a = (x for x in range(100))
print(type(a))
print(isinstance(a, Iterator))  # True
# 判断是否是生成器
print(isinstance(a, Generator))  # True
b = [x for x in range(100)]
print(isinstance(b, Iterator))  # False
# 判断是否为迭代对象
print(isinstance(a, Iterable))  # True
print(isinstance([], Iterable))  # True
# 判断是否是迭代器
print(isinstance(iter([1, 2, 3, 4]), Iterator))  # True
