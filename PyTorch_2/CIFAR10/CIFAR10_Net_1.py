import torch
import torch.nn as nn
import torch.nn.functional as F

import torch.optim as optim

from PyTorch_2.CIFAR10.CIFAR_10 import trainloader

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# 定义一个卷积神经网络，并修改它为3通道的图片
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)  # 第一个参数表示图片为3通道的图片
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
# net.to(device)  将它们的参数和缓冲器转换为CUDA张量

# 定义一个损失函数和优化器:
# 使用分类交叉熵Cross-Entropy作为损失函数
# 使用动量SGD做优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)  # momentum：动量因子（默认：0）


# 要在数据迭代器上循环传给网络和优化器输入
# 通过训练数据集对网络进行了2次训练
for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs
        inputs, labels = data
        # 在每一个步骤向GPU发送输入和目标
        # inputs, labels = inputs.to(device), labels.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:
            # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
print('Finished Training')