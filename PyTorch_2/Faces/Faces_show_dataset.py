from matplotlib import pyplot as plt

import Faces_dataset
from PyTorch_2.Faces.Faces_show_landmarks import show_landmarks

face_dataset = Faces_dataset.FaceLandmarksDataset(csv_file='F:/faces/face_landmarks.csv', root_dir='F:/faces/')

fig = plt.figure()

for i in range(len(face_dataset)):
    sample = face_dataset[i]
    print(i, sample['image'].shape, sample['landmarks'].shape)
    # plt.subplot（ijn）形式,其中ij是行列数,n是第几个图,比如（221）则是一个有四个图，该图位于第一个
    ax = plt.subplot(1, 4, i + 1)
    plt.tight_layout()
    ax.set_title('Sample #{}'.format(i))  # {}表示i的值
    ax.axis('off')  # 关闭坐标轴
    show_landmarks(**sample)

    if i == 3:
        plt.show()
        break