import torch

x = torch.rand(3, requires_grad=True)
print(x)
y = x * 2
print(y)
#y.data.norm()就是对张量y每个元素先进行平方，然后对它们求和，最后取平方根
#计算的结果就是所谓的L2范数或欧几里德范数
while y.data.norm() < 1000:
    y = y * 2
print(y)  # 此时y不是一个标量:标量就是一个数

#求在v=[0.1, 1.0, 0.0001]处的梯度
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)


print(x.requires_grad)
print((x ** 2).requires_grad)
#通过将代码包裹在with torch.no_grad()，来停止对跟踪历史中的.requires_grad=True的张量自动求导
with torch.no_grad():
    print((x ** 2).requires_grad)