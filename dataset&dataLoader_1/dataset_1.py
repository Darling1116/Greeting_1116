import numpy as np
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class MyDataset(Dataset):
    def __init__(self):
        txt_data = np.loadtxt('D:/PycharmProjects/pythonProject1/dataset&dataLoader/sample_data.txt', delimiter=',')
        self._x = txt_data[:, 0]  # x取前两列
        self._y = txt_data[:, 1]  # y取第三列
        '''
        self._x = torch.from_numpy(txt_data[:, :2])
        self._y = torch.from_numpy(txt_data[:, 2])
        '''
        self._len = len(txt_data)
    
    def __getitem__(self, item):
        return self._x[item], self._y[item]

    def __len__(self):
        return self._len


data = MyDataset()
print('data_len: ', len(data))

first = next(iter(data))  # data是一个iterable可迭代的类
print('fiest:', first)  # 取第一行的元素

print('type(first[0]): ', type(first[0]))
print('type(first[1]): ', type(first[1]))


dataloader = DataLoader(data, batch_size=3, shuffle=True, drop_last=True, num_workers=0)
# shuffle为是否打乱sample的顺序；drop_last为是否保留最后不能batch的数据
# dataLoader里面数据的类型是tensor
n = 0  # 用来标记迭代的次数
for data_val, label_val in dataloader:
    print('x:', data_val, 'y:', label_val)
    n += 1
    print('iterration: ', n)



