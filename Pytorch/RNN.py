import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# MNIST手写数据

EPOCH = 1  # train the training data n times,to save time,we just train 1 epoch
BATCH_SIZE = 64
LR = 0.01  # learning rate
TIME_STEP = 28  # rnn input size/ image height
INPUT_SIZE = 28  # rnn input size/ image wigth
DOWNLOAD_MNIST = False

#获取训练集数据
train_data = dsets.MNIST(
    root='D:/PycharmProjects/pythonProject1/PyTorch/mnist',
    train=True,
    transform=transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)
#把train_data变成train_loader，以loader的形式来进行批训练
train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)

test_data = dsets.MNIST(root='D:/PycharmProjects/pythonProject1/PyTorch/mnist', train=False,
                        transform=transforms.ToTensor())
test_x = Variable(test_data.test_data, volatile=True).type(torch.FloatTensor)[:2000]/255.
test_y = test_data.test_labels.numpy().squeeze()[:2000]


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(
            input_size=INPUT_SIZE,
            hidden_size=64,
            num_layers=1,
            batch_first=True,
        )
        self.out = nn.Linear(64, 10)

    def forward(self, x):
        r_out, (h_n, h_c), = self.rnn(x, None)  # x (batch, time_size, input_size)
        out = self.out(r_out[:, -1, :])  # (batch, time_size, input_size)
        return out

rnn = RNN()
print(rnn)

optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)  # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted

for epoch in range(EPOCH):
    for step, (x, y) in enumerate(train_loader):
        b_x = Variable(x.view(-1, 28, 28))  # reshape x to (batch, time_size, input_size)
        b_y = Variable(y)
        output = rnn(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0:
            test_output = rnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
            accuracy = sum(pred_y == test_y) / test_y.size
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.item(), '|test accuracy: %.2f' % accuracy)#


test_output = rnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
print(pred_y, 'prediction number')
print(test_y[:10], 'real number')
