import torch

from PyTorch_2.CIFAR10.CIFAR10_Net_1 import net
from PyTorch_2.CIFAR10.CIFAR_10 import testloader
from PyTorch_2.CIFAR10.CIFAR_10 import classes

# 从测试集中显示一张图像来预测
dataiter = iter(testloader)
images, labels = dataiter.next()

outputs = net(images)

# 不加_,返回的是一行中最大的数
# 加_,返回一行中最大数的位置
_, predicted = torch.max(outputs, 1)
print('Predicted: ', ' '.join('%5s' % classes[predicted[j]] for j in range(4)))