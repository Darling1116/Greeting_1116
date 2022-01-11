from __future__ import print_function, division
import os
import numpy as np
from torch.utils.data import Dataset
import pandas as pd  # 用于更容易地进行csv解析
from skimage import io, transform  # 用于图像的IO和变换

# ---建立人脸标记数据集---
class FaceLandmarksDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
    # csv_file（string）:带注释的csv文件的路径
    # root_dir（string）:包含所有图像的目录
    # transform（callable, optional）：一个样本上的可用的可选变换
        self.landmarks_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    # __len__ 实现len(dataset),返还数据集的尺寸
    def __len__(self):
        return len(self.landmarks_frame)

    # __getitem__ 用来获取一些索引数据
    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.landmarks_frame.iloc[idx, 0])
        image = io.imread(img_name)
        landmarks = self.landmarks_frame.iloc[idx, 1:]
        landmarks = np.array([landmarks])
        landmarks = landmarks.astype('float').reshape(-1, 2)
        sample = {'image': image, 'landmarks': landmarks}

        if self.transform:
            sample = self.transform(sample)

        return sample