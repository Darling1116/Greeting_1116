import torch
import torchvision
import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# CIFAR-10中图片的尺寸为 32×32 ，数据集中一共有 50000 张训练圄片和 10000 张测试图片。
# 与MNIST数据集中目比，CIFAR-10具有以下不同点：
# CIFAR-10 是3通道的彩色RGB图像，而MNIST是灰度图像。
# CIFAR-10 的图片尺寸为32×32， 而MNIST的图片尺寸为28×28，比MNIST稍大。
# 相比于手写字符，CIFAR-10含有的是现实世界中真实的物体，不仅噪声很大，而且物体的比例、特征都不尽相同，这为识别带来很大困难。
# 直接的线性模型如Softmax在CIFAR-10上表现得很差。


# ToTensor()将每一个数值归一化到[0,1]
# transforms.Normalize()作用就是先将输入归一化到(0,1)
# 再使用公式"(x-mean)/std"，将每个元素分布到(-1,1)
# std=(0.5, 0.5, 0.5), mean=(0.5, 0.5, 0.5)
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='F:/data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=0)

testset = torchvision.datasets.CIFAR10(root='F:/data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=0)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


# functions to show an image
# img的格式为（channels,imagesize,imagesize）
# plt.imshow在实际输入的是（imagesize,imagesize,channels）
# np.transpose(t,(2,0,1)) 0,1,2代表了原始位置，通过调节0，1，2的位置，来调节数组维数变换
def imshow(img):
    img = img/2+0.5  # unnormalize 反归一化:先乘以0.5，再加0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

# get some random training images
dataiter = iter(trainloader)
images, labels = dataiter.next()  # batch_size=4

# show images
imshow(torchvision.utils.make_grid(images))

# print labels
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))