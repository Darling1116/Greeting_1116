from __future__ import print_function
import torch

x = torch.rand(5, 3)
print(x)
y = torch.rand(5, 3)
print(y)

#加法操作1
print(x + y)

#加法操作2:使用add函数
print(torch.add(x, y))

#加法操作3:提供一个输出tensor作为参数
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

#加法操作4:adds x to y
y.add_(x)
#这里张量y发生了改变，任何使张量会发生变化的操作都有一个前缀_
print(y)
