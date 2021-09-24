import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt

torch.manual_seed(1)

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2*torch.rand(x.size())
x, y = Variable(x), Variable(y)


def save():
    net = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),  # 中间加一层激励函数
        torch.nn.Linear(10, 1),
    )
    # 优化神经网络:训练参数
    optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
    loss_func = torch.nn.MSELoss()

    for t in range(100):
        prediction = net(x)
        loss = loss_func(prediction, y)  # 预测值一定在前
        optimizer.zero_grad()  # 优化梯度圈，降为0
        loss.backward()
        optimizer.step()

    torch.save(net, 'net.pkl')  # 保存整个神经网络
    torch.save(net.state_dict(), 'net_params.pkl')  # 只保存神经网络中的参数
    #plot result
    plt.figure(1, figsize=(8, 3))  # 定义一个画框
    plt.subplot(131)  #排列位置
    plt.title('Net1:save')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=2)



def restore_net():
    net2 = torch.load('net.pkl')
    prediction = net2(x)
    plt.subplot(132)
    plt.title('Net2:restore_net')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=2)



# 提取参数：要先建立神经网络的模型
def restore_params():
    net3 = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),  # 中间加一层激励函数
        torch.nn.Linear(10, 1),
    )
    net3.load_state_dict(torch.load('net_params.pkl'))
    prediction = net3(x)
    plt.subplot(133)
    plt.title('Net3:restore_params')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=2)
    plt.show()



save()
restore_net()
restore_params()






