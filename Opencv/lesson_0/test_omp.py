import math
import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# ---定义OMP算法---
# 定义y=Dx,x为稀疏系数，即y在D上的分解系数
def cs_omp(y, D, K):
    residual = y  # 初始化残差:r = y - D * Lp
    (M,N) = D.shape  # M为行数，N为列数
    index = np.zeros(N, dtype=int)
    for i in range(N):  # 第i列被选中就是1，未选中就是-1
        index[i] = -1
    Xrec = np.zeros((N, 1))
    for j in range(K):  # K为迭代次数
        # np.fabs()函数：求各元素的绝对值
        w = np.fabs(np.dot(D.T, residual))  # 1.计算D对y的贡献量:w = ^DT * y
        pos = np.argmax(w)  # 2.获取最大贡献量系数对应的位置
        index[pos] = 1  # 对应的位置取1
        # 3.最小二乘法计算Xrec: Dnew用D[:, index>=0]表示来实现, +Dnew用D_new表示
        D_new = np.linalg.pinv(D[:, index >= 0])  # 先把最大贡献量所在的向量基加入到+Dnew中
        Lp = np.dot(D_new, y)  # Lp = +Dnew * y
        residual = y - np.dot(D[:, index >= 0], Lp)  # 4.更新残差:r=y-Dnew*Lp
    Xrec[index >= 0] = Lp  # 把Lp的值加入到在Xrec所对应的行值中
    Candidate = np.where(index >= 0)  # 获取所有选中的列
    return Xrec, Candidate  # 返回重建的Xrec及其所选中的列



# 读取图像:使用灰色度图像
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/lesson_0/lena.jpg', 0)
# img = Image.open('D:/PycharmProjects/pythonProject1/Opencv 4.5/lesson_0/lena.jpg').convert('L')
# plt.imshow(img, cmap='gray')
# # 根据图像的深度，imshow函数会自动对其显示灰度值进行缩放
# plt.show()

# ---生成稀疏基DCT矩阵---DCT矩阵量化之后才是系数矩阵
mat_dct_1d = np.zeros((256, 256))
v = range(256)  # 生成从0到255(不包含256)，从0开始
for k in range(0, 256):  # k从0到255(不包含256)，左闭右开
    dct_1d = np.cos(np.dot(v, k*math.pi/256))
    if k > 0:
        dct_1d = dct_1d - np.mean(dct_1d)
    mat_dct_1d[:, k] = dct_1d / np.linalg.norm(dct_1d)  # 默认为求矩阵二范数:矩阵整体元素平方和开根号，不会保留矩阵二维特性

# ---生成高斯随机观测矩阵---
# sampleRate = 0.7  # 采样率
N = 256
M = 128
K = 50
img = np.array(img)  # 使图像变成numpy类型的array
D = np.random.randn(M, N)/np.sqrt(M)
# 随机测量
img_cs_1d = np.dot(D, img)

# ---重建---
sparse_rec_1d = np.zeros((256, 256))   # 初始化稀疏系数矩阵
Theta_1d = np.dot(D, mat_dct_1d)   # 测量矩阵 x 稀疏基DCT矩阵
for i in range(N):
    if i % 32 == 0:
        print('正在重建图像的第',i,'列...')
    y = np.reshape(img_cs_1d[:, i], (M, 1))
    Xrec, Candidate = cs_omp(y, Theta_1d, K)  # 利用OMP算法计算稀疏系数X
    X_pre = np.reshape(Xrec, (N))
    sparse_rec_1d[:, i] = X_pre

img_rec = np.dot(mat_dct_1d, sparse_rec_1d)  # 稀疏系数 x 稀疏基DCT矩阵
# 显示重建后的图片
img_pre = Image.fromarray(img_rec)  # 实现array到image的转换

plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Image')
plt.subplot(1,2,2),plt.imshow(img_pre,cmap = 'gray')
plt.title('Image_pre')
# plt.imshow(img_pre, cmap='gray')
error = np.linalg.norm(img_rec-img)/np.linalg.norm(img)
print('K is 50, error is ', error)
plt.show()