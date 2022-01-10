from __future__ import print_function, division
import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import pandas as pd  # 用于更容易地进行csv解析
from skimage import io, transform  # 用于图像的IO和变换

# 忽略警告
import warnings
warnings.filterwarnings("ignore")

# python可视化库matplotlib的显示模式默认为阻塞（block）模式
# 使用plt.ion()使matplotlib的显示模式转换为交互（interactive）模式
# plt.ion()  # interactive mode


# csv:逗号分隔值,其文件以纯文本形式存储表格数据（数字和文本）
# 将csv中的标注点数据读入（N，2）数组中，其中N是特征点的数量
landmarks_frame = pd.read_csv('F:/faces/face_landmarks.csv')
n = 65
img_name = landmarks_frame.iloc[n, 0]
# landmarks = landmarks_frame.iloc[n, 1:].as_matrix()
landmarks = landmarks_frame.iloc[n, 1:].values
landmarks = landmarks.astype('float').reshape(-1, 2)  #???

print('Image name: {}'.format(img_name))
print('Landmarks shape: {}'.format(landmarks.shape))
print('First 4 Landmarks: {}'.format(landmarks[:4]))


#---展示这张图片和它对应的标注点---
def show_landmarks(image, landmarks):
    plt.imshow(image)
    # 绘制散点图，landmarks[:,0]表示的是X的坐标，landmarks[:,1]表示的是y的坐标 ???
    plt.scatter(landmarks[:, 0], landmarks[:, 1], s=10, marker='.', c='r')
    plt.pause(0.001)  # pause a bit so that plots are updated

plt.figure()
show_landmarks(io.imread(os.path.join('F:/faces/', img_name)), landmarks)
plt.show()