import numpy as np

'''
array = np.array([[1, 2, 3], [2, 3, 4]])  # 把列表转化为矩阵
print(array)
print('number of dim:', array.ndim)   # 维数
print('shape:', array.shape)  # 行列数
print('size:', array.size)  # 元素个数
'''

'''
a1 = np.array([2, 23, 4], dtype=np.int64)  # 定义元素的数据形式
print(a1.dtype)
a2 = np.array([2, 23, 4], dtype=np.float32)
print(a2.dtype)

b1 = np.zeros((3, 4))
print(b1)
b2 = np.ones((3, 4), dtype=np.int64)
print(b2)

c1 = np.arange(10, 20, 2)  # 定义起始位10，终止为20（不包括20），步长为2的数列
print(c1)
c2 = np.arange(12).reshape((3, 4))  # 随机生成12个数，定义为3行4列的矩阵
print(c2)
c3 = np.linspace(1, 10, 5)  # 定义一个5段的数列
print(c3)
'''

'''
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(b)
print(b < 3)  # 返回值为TRUE或FALSE

#c = b**2
c = 10*np.sin(a)
print(c)
'''

'''
a = np.array([[1, 1], [2, 2]])
b = np.arange(4).reshape((2, 2))
print(a, b)

c = a*b
print(c)  # 相应位置的元素逐个想乘

c_dot = np.dot(a, b)  # 笛卡尔积
# c_dot = a.dot(b)
print(c_dot)
'''

'''
a = np.random.random((2, 4))
print(a)
print(np.sum(a, axis=1))  # 按行求和
print(np.min(a))
print(np.max(a))
'''

'''
A = np.arange(2, 14).reshape((3, 4))
print(A)
print(A[2])
print(A[2][1])
print(np.argmin(A))  # 返回最小值的索引
print(np.argmax(A))
print(np.mean(A))  # 返回A的平均值
print(np.median(A))  # 返回A的中位数
print(np.diff(A))  # 返回每两个元素之间的差
print(np.nonzero(A))  # 输出A中元素的行数和列数
print((np.transpose(A)))  # 输出矩阵的反向（转置矩阵）
print(np.clip(A, 5, 9))  # 规定A中最小值为5，最大值为9
print(A[:, 1])  # 打印第一列的所有数
print(A[1, 1:3])  # 打印第一行从1到3列的数（左闭右开）

for row in A:
    print(row)  # 默认按行迭代

for column in A.T:
    print(column)  # 按列迭代

for item in A.flat:
    print(item)  # 得到每一个元素
'''

A = np.array([1, 1, 1])  # A为序列
B = np.array([2, 2, 2])

C1 = np.vstack((A, B))  # 上下合并
D1 = np.hstack((A, B))  # 左右合并
#print(A.shape, C1.shape, D1.shape)

E = np.array([2, 2, 2])[:, np.newaxis]  # 给行加维度
print(E)
F = np.array([2, 2, 2])[np.newaxis, :]  # 给列加维度
print(F)

print(np.vsplit(E, 3))  # 按行分割矩阵
print(np.hsplit(F, 3))  # 按列分割矩阵

'''
a = np.arange(4)
print(a)

b = a.copy()
c = a
d = b
a[0] = 11
print(a, b, c, d)
'''