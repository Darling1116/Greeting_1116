import torch

#---用自定义nn.Module的子类构建两层网络---

class TwoLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
    # 在构造函数中，我们实例化了两个nn.Linear模块，并将它们作为成员变量!!!!!!
        super(TwoLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
    # 在前向传播的函数中，我们接收一个输入的张量，也必须返回一个输出张量;
    # 我们可以使用构造函数中定义的模块以及张量上的任意的（可微分的）操作。
        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)
        return y_pred


N, D_in, H, D_out = 64, 1000, 100, 10

x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

# 通过实例化上面定义的类来构建我们的模型
model = TwoLayerNet(D_in, H, D_out)

# 构造损失函数和优化器:这里使用SGD优化方法
# SGD构造函数中对model.parameters()的调用,将包含模型的一部分;
# 即两个nn.Linear模块的可学习参数。
loss_fn = torch.nn.MSELoss(reduction='sum')


# ---优化器基本使用方法:建立优化器实例，循环---
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
for t in range(500):
    # 前向传播计算预测值y，计算并输出loss
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    print(t, loss.item())

    # 清零梯度，反向传播，更新权重
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
