import torch

from PyTorch_2.CIFAR10.CIFAR10_Net_1 import net
from PyTorch_2.CIFAR10.CIFAR_10 import testloader

# 看网络在整个数据集上的表现
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))

# 随机预测的准确率为10%，该神经网络预测的准确率为56%