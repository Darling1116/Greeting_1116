import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

#分类的数据点
n_data = torch.ones(100, 2)
x0 = torch.normal(2*n_data, 1)
y0 = torch.zeros(100)
x1 = torch.normal(-2*n_data, 1)
y1 = torch.ones(100)
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)  # x合并在一起当做数据
y = torch.cat((y0, y1), ).type(torch.LongTensor)  # y合并在一起当做标签

x, y = Variable(x), Variable(y)  # 让x，y都放在Variable里面让它去学习

#method 1
class Net(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x

net = Net(2, 10, 2)  #参数含义依次是：2个特征，10个神经元，2个输出特征
print(net)



#method 2:快速搭建神经网络
net2 = torch.nn.Sequential(
    torch.nn.Linear(2, 10),
    torch.nn.ReLU(),  # 中间加一层激励函数
    torch.nn.Linear(10, 2),
)
print(net2)



'''
#可视化
plt.ion()
plt.show()
#优化神经网络
optimizer = torch.optim.SGD(net.parameters(), lr=0.002)  #lr为分类效果，数值越小，分类效果越慢
loss_func = torch.nn.CrossEntropyLoss()  # 用于分类问题：输出概率

for t in range(100):
    out = net(x)
    loss = loss_func(out, y)  # 计算误差：预测值一定在前

    optimizer.zero_grad()  # 优化梯度圈，降为0
    loss.backward()
    optimizer.step()

    if t % 2 == 0:
        plt.cla()
        prediction = torch.max(F.softmax(out), 1)[1]
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0)
        accuracy = sum(pred_y ==target_y)/200
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)


plt.ioff()
plt.show()

'''