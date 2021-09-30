import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
# 假设variable为神经网络中的一个结点
variable = Variable(tensor, requires_grad=True)  # requires_grad是否反向传播
print(tensor)
print(variable)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)
print(t_out)
print(v_out)

v_out.backward()
print(variable)
print(variable.grad)
print(variable.data)
print(variable.data.numpy(0))
