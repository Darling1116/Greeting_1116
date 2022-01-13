from matplotlib import pyplot as plt
from torchvision import transforms
from PyTorch_2.Faces import Faces_dataset
from PyTorch_2.Faces.Faces_show_landmarks import show_landmarks
from PyTorch_2.Faces.models.Transform import Rescale, RandomCrop

# 调用torchvision.transforms.Compose实现图片大小、数据格式转换
# 把图像的短边调整为256
scale = Rescale(256)
# 随机裁剪为224大小的正方形
crop = RandomCrop(128)
composed = transforms.Compose([Rescale(256), RandomCrop(224)])


# ---在一个样本上应用上述的每个变换---
plt.figure()
face_dataset = Faces_dataset.FaceLandmarksDataset(csv_file='F:/faces/face_landmarks.csv', root_dir='F:/faces/')
sample = face_dataset[39]

for i, tsform in enumerate([scale, crop, composed]):
    transformed_sample = tsform(sample)
    ax = plt.subplot(1, 3, i + 1)  # 在一个图上排列3个子图
    plt.tight_layout()
    ax.set_title(type(tsform).__name__)
    show_landmarks(**transformed_sample)

plt.show()