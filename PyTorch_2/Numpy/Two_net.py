import numpy as np

#---实现的两层神经网络的模型---

# N是批量大小;
# D_in是输入维度;
# 49/5000 H是隐藏的维度;
# D_out是输出维度
N, D_in, H, D_out = 64, 1000, 100, 10

# 创建随机输入和输出数据
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# 随机初始化权重
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # 前向传播: 计算预测值y
    # h = w1∗X+b1
    # a = max(0,h)
    # y_hat = w2∗a+b2
    h = x.dot(w1)  # 矩阵乘法计算: 数据*权重
    h_relu = np.maximum(h, 0)  # np.maximum(X, Y): 将X与Y逐位比较取其大者
    y_pred = h_relu.dot(w2)
    # print(y_pred)

    # 计算损失loss: square平方损失函数
    loss = np.square(y_pred - y).sum()
    # print(t, loss)

    # 反向传播，计算w1和w2对loss的梯度??????
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # 更新权重: w -= a * grad_w
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
    print("w1: ", w1)
    print("w2: ", w2)
