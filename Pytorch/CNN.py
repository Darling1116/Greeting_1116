import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt


# MNIST手写数据

EPOCH = 1  # train the training data n times,to save time,we just train 1 epoch
BATCH_SIZE = 50
LR = 0.01  # learning rate
DOWNLOAD_MNIST = False

# torchvision包是服务于pytorch深度学习框架的,用来生成图片,视频数据集,和一些流行的模型类和预训练模型.
train_data = torchvision.datasets.MNIST(  # 从网上下载数据
    root='D:/PycharmProjects/pythonProject1/PyTorch/mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),  # transform时，会把图片中（0-255）的值压缩到数据的（0-1）中
    download=DOWNLOAD_MNIST
)

'''
# plot one example
print(train_data.train_data.size())
print(train_data.train_labels.size())
plt.imshow(train_data.train_data[0].numpy(), cmap='gray')
plt.title('%i' % train_data.train_labels[0])
plt.show()
'''

train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)

test_data = torchvision.datasets.MNIST(root='D:/PycharmProjects/pythonProject1/PyTorch/mnist', train=False)
# train=False意味着提取出来的不是train data,而是test data
test_x = Variable(torch.unsqueeze(test_data.test_data, dim=1), volatile=True).type(torch.FloatTensor)[:1000]/255.
# 出来的值仍然在（0-255）之间，/255.表示手动压缩
test_y = test_data.test_labels[:1000]
# 先只取前2000个值



# 创建CNN模型:对于黑白的图片，CNN的输入是一个1x28x28的二维神经元；对于RGB格式的图片来说，CNN的输入是一个3x28x28的三维神经元
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(  # conv1为卷积层
            nn.Conv2d(
                # ->(1, 28, 28):1为channel的维度，28,28为宽和高
                in_channels=1,  # 图片的高度为1
                out_channels=16,  # 16个filter，16个特征
                kernel_size=5,  # filter的长和宽都是5x5的像素
                stride=1,  # 每隔多少步跳一下
                padding=2,  # 边缘填充 if stride=1, padding=(kernel_size-1)/2
            ),  # ->(16, 28, 28)
            nn.ReLU(),  # 激励函数 ->(16, 28, 28)
            nn.MaxPool2d(kernel_size=2),  # 池化层 ->(16, 14, 14)
        )

        self.conv2 = nn.Sequential(  # ->(16, 14, 14)
            nn.Conv2d(16, 32, 5, 1, 2),  # ->(32, 14, 14)
            nn.ReLU(),  # ->(32, 14, 14)
            nn.MaxPool2d(2)  # ->(32, 7, 7)
        )

        self.out = nn.Linear(32*7*7, 10)  # 展平成2维数据

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # (batch, 32*7*7)
        output = self.out(x)
        return output

cnn = CNN()
#print(cnn)


# 训练
optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)  # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted

#training and testing
for epoch in range(EPOCH):
    for step, (x, y) in enumerate(train_loader):
        b_x = Variable(x)  # batch x
        b_y = Variable(y)  # batch y

        output = cnn(b_x)  # cnn output
        loss = loss_func(output, b_y)  # cross entropy loss
        optimizer.zero_grad()  # clear gradient for this training step
        loss.backward()  # backpropagation, compute gradients
        optimizer.step()

        if step % 50 == 0:  # 每50步看一下训练效果
            test_output = cnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.squeeze()
            accuracy = sum(pred_y == test_y) / (test_y.size(0))
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.item(), '|test accuracy: %.2f' % accuracy)


# print 10 prediction from test data
test_output = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')
