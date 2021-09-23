import torch
import numpy as np


'''
#pytorch是神经网络界的numpy
print(torch.__version__)
'''

'''
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()

print(
    '\nnumpy', np_data,
    '\ntorch', torch_data,
    '\ntensor2array', tensor2array,
)
'''

#abs
'''
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)
print(
    '\ndata:', data,
    '\nabs',
    '\nnumpy: ', np.abs(data),
    '\ntorch: ', torch.abs(tensor),
    '\nsin',
    '\nnumpy: ', np.sin(data),
    '\ntorch: ', torch.sin(tensor),
    '\nmean',
    '\nnumpy: ', np.mean(data),
    '\ntorch: ', torch.mean(tensor),
)
'''
print('torch version: ', torch.__version__)
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)
#data = np.array(data)
print(
    'data: ', data,
    '\nnumpy: ', np.matmul(data, data),  # 两个矩阵相乘
    '\ntorch: ', torch.mm(tensor, tensor),

)