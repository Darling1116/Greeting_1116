import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

#回归的数据点
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # 把一维的数据变成二位的数据
y = x.pow(2) + 0.2*torch.rand(x.size())

x, y = Variable(x), Variable(y)

#plt.scatter(x.data.numpy(), y.data.numpy())
#plt.show()

class Net(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x

net = Net(1, 10, 1)
print(net)

#可视化
plt.ion()
plt.show()
#优化神经网络
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  # 使用SGD的方法优化神经网络（optimizer为优化器）
loss_func = torch.nn.MSELoss()

for t in range(100):
    prediction = net(x)
    loss = loss_func(prediction, y)  # 预测值一定在前
    optimizer.zero_grad()  # 优化梯度圈，降为0
    loss.backward()
    optimizer.step()

    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), y.data.numpy(), 'r-', lw=4)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.item(), fontdict={'size': 15, 'color': 'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()