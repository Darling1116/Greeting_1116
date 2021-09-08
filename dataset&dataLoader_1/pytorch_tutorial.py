import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
from sklearn.linear_model import LinearRegression
import numpy as np
import math

from torch.autograd import Variable
import torch.nn.functional as F



class mydataSet(Dataset):
    def __init__(self):
        # data loading
        xy = np.loadtxt('D:/PycharmProjects/pythonProject1/1/landmarks1.txt', delimiter=' ', dtype=np.float32, skiprows=1)
        self.x = torch.from_numpy(xy[:, 0])
        self.y = torch.from_numpy(xy[:, 1])
        self.n_samples = xy.shape[0]


    def __getitem__(self, item):
        # dataset(0)
        return self.x[item], self.y[item]

    def __len__(self):
        # len(dataset)
        return self.n_samples

dataset = mydataSet()
print('dataset.n_samples:', dataset.n_samples)
'''
first_data = dataset[0]
val, labels = first_data
print(val, labels)
'''
# 训练集dataloader,想到于train_loader
dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, drop_last=False, num_workers=0)

'''
dataiter = iter(dataloader)
data = dataiter.next()
vals, labels = data
print(vals, labels)
'''


# training loop
print('-----training loop-----')
num_epochs = 3  # 迭代三次
total_samples = len(dataset)
n_iterations = math.ceil(total_samples/4)
print('total_samples:', total_samples, '\nn_iterations:', n_iterations)

for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(dataloader):
        # forward backward, update
        if (i+1)%5 == 0:
            print(f'epoch {epoch+1}/{num_epochs}, step {i*1}/{n_iterations}, inputs {inputs.shape}')










