import numpy as np
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

class MyDataset(Dataset):
    def __init__(self):
        txt_data = np.loadtxt('D:/PycharmProjects/pythonProject1/1/landmarks1.txt', delimiter=' ')
        '''
        self._x = txt_data[:, 0]  # x取第一列（下标从0开始）
        self._y = txt_data[:, 1]  # y取第二列
        '''
        self.x = torch.from_numpy(txt_data[:, 0])
        self.y = torch.from_numpy(txt_data[:, 1])
        self.len = len(txt_data)

    def __getitem__(self, item):
        return self.x[item], self.y[item]

    def __len__(self):
        return self.len


dataset = MyDataset()
print('type: ', type(dataset))
print('len: ', len(dataset))
'''
first = next(iter(data))
print(first)
print(type(first[0]))
print(type(first[1]))
'''

loader = DataLoader(dataset, batch_size=10, shuffle=True, drop_last=False, num_workers=0)
for epoch in range(2):  # 把数据整体训练2次
    for step, (batch_x, batch_y) in enumerate(loader):
        # training.....
        print('Epoch: ', epoch, '| step: ', step, '| batch x: ', batch_x.numpy(), '| batch y: ', batch_y.numpy())



