import torch

from PyTorch_2.CIFAR10.CIFAR10_Net_1 import net
from PyTorch_2.CIFAR10.CIFAR_10 import testloader
from PyTorch_2.CIFAR10.CIFAR_10 import classes

# 数据集中预测各分类的精确度

class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))

with torch.no_grad():
    for data in testloader:
       images, labels = data
       outputs = net(images)
       _, predicted = torch.max(outputs, 1)
       c = (predicted == labels).squeeze()
       for i in range(4):
           label = labels[i]
           class_correct[label] += c[i].item()
           class_total[label] += 1

for i in range(10):
    print('Accuracy of %5s : %2d %%' % (
     classes[i], 100 * class_correct[i] / class_total[i]))