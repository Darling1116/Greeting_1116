import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# 1. 生成随机数据：正负数据各50个
data = pd.read_csv('D:/PycharmProjects/pythonProject1/numpy&pandas/data.csv')
# X1 = np.random.rand(50, 2)
# X2 = np.random.rand(50, 2)*(-1)
X = data.iloc[:,:2].values
Y = data.iloc[:,2].values
# print('X:',X)
# print('Y:',Y)

# 2. 特征标准化处理：标准差归一化
# 均值
u = np.mean(X, axis=0)
# 方差
v = np.std(X, axis=0)
# 标准化输入
X = (X - u) / v
# print(X)
# X加上偏置项
X = np.hstack((np.ones((X.shape[0],1)), X))

# 3. 权重初始化
# w = np.random.randn(3,1)  # 随机生成一个1行3列的数组
# print(w)
w = np.array([[-0.04841753],[-0.71738979],[ 1.0517744 ]])

x1 = -2;
x2 = 2;

# 4. 更新权重: 迭代更新训练
for i in range(100):
    # 直线初始化
    y1 = -1 / w[2] * (w[0] * 1 + w[1] * x1)  # 直线第一个坐标（x1，y1）
    y2 = -1 / w[2] * (w[0] * 1 + w[1] * x2)  # 直线第二个坐标（x2，y2）

    s = np.dot(X, w)
    y_pred = np.ones_like(Y)
    loc_n = np.where(s < 0)[0]
    y_pred[loc_n] = -1
    num_fault = len(np.where(Y != y_pred)[0])
    print('第%2d次更新...分类错误的点的个数:%2d;' % (i, num_fault))
    if num_fault == 0:
        break
    else:
        t = np.where(Y != y_pred)[0][0]
        w += Y[t] * X[t, :].reshape((3,1))
        plt.scatter(X[:50, 1], X[:50, 2], color='yellow', marker='o')
        plt.scatter(X[50:, 1], X[50:, 2], color='blue', marker='x')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot([x1, x2], [y1, y2], 'r')
        plt.show()


# 显示最后一次更新迭代的结果
plt.scatter(X[:50, 1], X[:50, 2], color='yellow', marker='o')
plt.scatter(X[50:, 1], X[50:, 2], color='blue', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot([x1, x2], [y1, y2], 'r')
plt.show()
