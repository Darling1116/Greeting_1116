import numpy as np
import torch
from numpy.random import sample
from skimage import transform


class Rescale(object):
 # ---将图像缩放到给定大小---
 # Args:
 # output_size（tuple或int）：所需的输出大小。
 # 如果是元组，则输出为与output_size匹配;
 # 如果是int，则匹配较小的图像边缘到output_size保持纵横比相同。

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, sample):
        image, landmarks = sample['image'], sample['landmarks']
        h, w = image.shape[:2]
        if isinstance(self.output_size, int):
            if h > w:
                new_h, new_w = self.output_size * h / w, self.output_size
            else:
                new_h, new_w = self.output_size, self.output_size * w / h
        else:
            new_h, new_w = self.output_size

        new_h, new_w = int(new_h), int(new_w)
        img = transform.resize(image, (new_h, new_w))

        # h and w are swapped for landmarks because for images,
        # x and y axes are axis 1 and 0 respectively
        landmarks = landmarks * [new_w / w, new_h / h]
        return {'image': img, 'landmarks': landmarks}


class RandomCrop(object):
 # ---随机裁剪样本中的图像:用于数据增强---
 # Args:
 # output_size（tuple或int）：所需的输出大小。 如果是int，方形裁剪。

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size


    def __call__(self, sample):
        image, landmarks = sample['image'], sample['landmarks']

        h, w = image.shape[:2]
        new_h, new_w = self.output_size

        top = np.random.randint(0, h - new_h)
        left = np.random.randint(0, w - new_w)

        image = image[top: top + new_h, left: left + new_w]
        landmarks = landmarks - [left, top]

        return {'image': image, 'landmarks': landmarks}


class ToTensor(object):
# 将样本中的numpy图像转为torch图像（需要交换轴axes）

    def __call__(self, sample):
        image, landmarks = sample['image'], sample['landmarks']
    # 交换颜色轴因为
    # numpy包的图片是: H * W * C
    # torch包的图片是: C * H * W
        image = image.transpose((2, 0, 1))
        return {'image': torch.from_numpy(image), 'landmarks': torch.from_numpy(landmarks)}

