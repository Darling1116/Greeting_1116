from __future__ import print_function
import torch

#构造一个5x3的矩阵，不初始化
x1 = torch.empty(5, 3)
print(x1)

#构造一个5x3的矩阵，随机初始化:该张量由区间[0,1)上均匀分布的随机数填充
x2 = torch.rand(5, 3)
print(x2)

#构造一个5x3的全为0的矩阵，而且数据类型为long
x3 = torch.zeros(5, 3, dtype=torch.long)
print(x3)

#构造一个张量，直接使用数据
x4 = torch.tensor([5.5, 3])
print(x4)
print(x4.size())

#创建一个tensor基于已经存在的tensor(这里x1已经存在)
x1 = x1.new_ones(5, 3, dtype=torch.double)
print(x1)

x1 = torch.randn_like(x1, dtype=torch.float)
print(x1)

#输出张量x1的大小
print(x1.size())

