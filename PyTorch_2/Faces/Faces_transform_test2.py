from matplotlib import pyplot as plt
from torch.utils.data import DataLoader
from torchvision import transforms, utils

from PyTorch_2.Faces import Faces_dataset
from PyTorch_2.Faces.models.Transform import Rescale, RandomCrop, ToTensor

# ---在数据集上应用组合变换---
transformed_dataset = Faces_dataset.\
    FaceLandmarksDataset(csv_file='F:/faces/face_landmarks.csv',
                         root_dir='F:/faces/',
                         transform=transforms.Compose(
                             [Rescale(256), RandomCrop(224), ToTensor()]))

# 对所创建的数据集执行同样的操作
# for i in range(len(transformed_dataset)):
#     sample = transformed_dataset[i]
#     print(i, sample['image'].size(), sample['landmarks'].size())
#     if i == 3:
#         break

# 数据加载器DataLoader的辅助功能：批量处理数据 && 打乱数据
# DataLoader能够为我们自动生成一个多线程的迭代器
# shuffle参数：是否打乱数据
dataloader = DataLoader(transformed_dataset, batch_size=4, shuffle=True)

def show_landmarks_batch(sample_batched):
    # Show image with landmarks for a batch of samples.
    images_batch, landmarks_batch = sample_batched['image'], sample_batched['landmarks']
    batch_size = len(images_batch)
    im_size = images_batch.size(2)
    grid_border_size = 2

    grid = utils.make_grid(images_batch)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))

    for i in range(batch_size):
        plt.scatter(landmarks_batch[i, :, 0].numpy() + i * im_size + (i + 1) * grid_border_size,
                    landmarks_batch[i, :, 1].numpy() + grid_border_size, s=10, marker='.', c='r')
        plt.title('Batch from dataloader')

for i_batch, sample_batched in enumerate(dataloader):
    print(i_batch, sample_batched['image'].size(), sample_batched['landmarks'].size())

    # 观察第3批次并停止
    if i_batch == 2:
        plt.figure()
        show_landmarks_batch(sample_batched)
        plt.axis('off')  # 关闭坐标轴
        plt.ioff()  # 让界面停留下来
        plt.show()
        break
