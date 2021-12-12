from __future__ import print_function
import torch

x1 = torch.rand(3, 3)
print(x1)

#索引操作:输出第一列所有元素的操作
print(x1[:, 1])


#使用torch.view改变一个tensor的大小或者形状
x = torch.randn(4, 4)
y = x.view(16)  # 这里16表示16行
#你如果不确定想要reshape成几行，但是肯定要reshape成4列
z = x.view(-1, 2)  # 这里-1表示一个不确定的数
print(x)
print(y)
print(z)
print(x.size())
print(y.size())
print(z.size())


#使用.item()获得该tensor值的value
x2 = torch.randn(1)
print(x2)
print(x2.item())