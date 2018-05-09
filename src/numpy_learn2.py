# # #
# # # a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # b = [4, 5, 6]
# # # c = [sum(num) for num in a]
# # # d = list(map(sum, a))
# # # print(c)
# # # print(d)
# # # dic_1 = {1: 2, 2: 3, 3: 4, 4: 5}
# # # print(dic_1.items())
# # # a = [i for i in range(1, 100, 2)]
# # # b = [j for j in range(0, 100, 2)]
# # # dic_2 = {}
# # # for i in range(len(a)):
# # #     dic_2[a[i]] = b[i]+1
# # # print(dic_2)
# # # print(sorted(dic_2))
# # #
import numpy as np

#
# #
# # a = np.arange(15).reshape(3, 5)
# # print(a)
# # # 多维数组的秩
# # print(a.ndim)
# # print(a.shape)
# # print(a.size)
# # print(a.dtype)
# # print(a.itemsize)
# # print(a.data)
# # # 显式指定创建数组元素类型
# # b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
# # print(b)
# # # 特殊数组
# # c = np.zeros((3, 4))
# # d = np.ones((3, 4))
# # e = np.eye(3)
# # f = np.empty((3, 4))
# # print(c, d, e, f)
# # # 创建一个数列
# # print(np.arange(1, 10, 1))
# # c = np.array([[4, 5, 6], [7, 8, 9]], dtype=int)
# # print(b - c)
# # print(b * c)
# # # 矩阵乘法
# # print(np.dot(np.transpose(b), c))
# # print(np.exp(b), np.sqrt(b))
# # print(b, c)
# # print(np.add(b, c))
# # print(b[0:3, 1])
# # print(b[0:2, :])
# # print(b[...])
# # print([element for element in b.flat])
# # b.shape = (3, 2)
# # print(b, np.transpose(b))
# # print(b.ravel())
# # c = b.view()
# # print(c is b)
# # print(c.base is b)
# # c[0, 1] = 100
# # print(b)
# # d = b[0:1]
# # print(d)
# # d[:] = 99
# # print(b, c, d)
# # a = np.arange(12) ** 2
# # i = np.array([1, 1, 3, 4, 8])
# # print(a[i])
# # # 创建数组
# # array1 = np.array([[1, 2, 3], [4, 5, 6]])
# # array2 = np.array([1, 2, 3], dtype=np.int32)
# # array3 = np.arange(10, 30, 5)  # array([10,15,20,25])
# # array4 = np.linspace(1, 2, 9)  # linespace接收想要的元素数量
# # array5 = np.arange(15).reshape(3, 5)
# # array6 = np.arange(5)  # [0,1,2,3,4]
# # array8 = np.random.random(5) * 10
# # print(array8)
# # # 数组运算
# # array7 = np.array([5, 6, 7, 8, 9])
# # print(array7 - array6)
# # print(array7 + array6)
# # print(np.sin(array7))
# # array8 += array7
# # print(array8)
# # # array7 += array8
# # # print(array7)
# # a = np.arange(12).reshape(3, 4)
# # print(a.sum())
# # print(a.min())
# # print(a.max())
# # print(np.sum(a))
# # print(np.max(a))
# # print(np.min(a))
# # print(a.sum(axis=0))
# # print(a.max(axis=0))
# # print(np.max(a, axis=1))
# # print(a.cumsum(axis=0))  # 按照行累计求和
# # print(np.sum(a, axis=0))
# # print(np.cumsum(a, axis=0))
# # # 切片
# # print(a[2, 3])
# # print(a[1:2])
# # print(a[1:2, :])
# # for row in a:
# #     print(row)
# # for element in a.flat:
# #     print(element)
# # # 更改数组形状，但是不更改原始数组
# # print(a.ravel())
# # print(a.reshape(4, 3))
# # print(a.T)
# # print(a.reshape(4, -1))  # -1自动计算其它维度
# # # 更改原始数组
# # print("-----------")
# # a.resize(4, 3)
# # print(a)
# # # 数组的堆叠
# # print(np.vstack((a, a)))
# # print(np.hstack((a, a)))
# # # 数组的切割
# # print(np.vsplit(a, 2))
# # print(np.hsplit(a, 3))
# # print(a)
# # print(a.shape)
# # b = a[1, :]
# # print(b)
# # print(b.reshape(3, ))
# # c = np.arange(60).reshape(3, 4, 5)
# # print(c)
# # a = np.arange(3)
# # print(a, a.shape[0])
# # b = np.arange(3).reshape(3, 1)
# # print(b, b.shape[0])
# # print(id(a))
# # c = np.zeros((3, 2))
# # d = np.arange(3).reshape(3, 1)
# # print(c + d)
# a = np.arange(4).reshape(2, 2)
# b = np.array([[1, 1], [1, 2]])
# c = np.array([[2, 1], [3, 3]])
# # print(np.linalg.inv(a))
# print(a.transpose())
# d = np.array([[1, 2, 3], [4, 5, 6], [7, 9, 8]])
# print(np.linalg.inv(d))
# # 生成随机数组
e = np.random.randn(2, 3)
print(e)
# 创建n纬数组
array1 = np.arange(10).reshape(2, 5)
array2 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
zero1 = np.zeros(10)
zero2 = np.zeros((2, 5))
empty1 = np.empty(10)
empty2 = np.empty((2, 5))
one1 = np.ones(10)
print(array1, array2, zero1, zero2, empty1, empty2,one1)
float_array = array2.astype(np.float64)
print(float_array)
# 布尔索引
name = np.array(["haha", "haha1", "haha2", "haha3"])
random_array = np.random.randn(4, 3)
print(random_array[name == "haha"])
print(np.arange(10).reshape(2, 5))
print(array1.mean(), array1.std(), array1.sum(axis=0), np.sum(array1, axis=0))
# array1=np.arange(6).reshape(3,2)
# array2=np.arange(3).reshape(3,1)
# print(array1+array2,array1*array2)
print(np.dot(array1,np.ones(5)))
print(np.round(array1.dot(np.linalg.inv(array1)),2))
