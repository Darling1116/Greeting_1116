import cv2
import numpy as np
import numpy.linalg as lg
import math

def get_matri_new_plus(A):
    '''
    求A矩阵的伪逆
    :param A: 输入矩阵
    :return A_new: 求解的伪逆矩阵
    '''
    A_new = A.T.dot(A)
    if A_new.ndim < 2:
        A_new = 1 / A_new
        A_new = A_new * A.T
    else:
        A_new = lg.inv(A_new)
        A_new = A_new.dot(A.T)
    return A_new

def get_A_ba(A):
    '''
    求解A_ba，也就是矩阵列向量单位化
    :param A: 输入矩阵
    :return A_new: 返回列向量单位后的矩阵
    '''
    A_new = A.T
    for row in range(A_new.shape[0]):
        norm2 = lg.norm(A_new[row], ord=2)           # 求向量的2范数
        A_new[row] /= norm2                          # 单位化
    return A_new


def find_pos_VecInMatrix(A, v):
    '''
    求解某个向量在矩阵中的相应行位置
    :param A: 输入矩阵
    :param v: 输入向量
    :return pos: 位置
    '''
    A_rownum = A.shape[0]                           # 矩阵行的数量
    for pos in range(A_rownum):
        if (v == A[pos]).all():                       # 判断向量v和矩阵中的某一行是否相等
            return pos


def cs_omp(s, mat):
    '''
    压缩感知主体算法
    :param s: 待重构向量
    :param mat: 重构矩阵
    :param N: 重构向量的长度
    :return: 重构完成的向量
    '''
    global N, K
    m = math.floor(3*(s.shape[0])/4)                # 算法迭代次数(m>=K)
    hat_y = np.zeros(N)                             # 待重构的谱域(变换域)向量
    Aug_t = None                                    # 增量矩阵(初始值为空矩阵)
    r_n = s                                         # 残差值

    T_tran = mat.T
    A_ba = T_tran.copy()                            # 初始化A矩阵
    A_ba1 = A_ba                                    # 复制
    pos_selected_v = []
    for times in range(m):
        w = A_ba.dot(r_n)                           # 求各列向量和残差的投影系数
        pos = np.argmax(abs(w))                     # 最大投影系数所对应的位置
        b_k = A_ba[pos]
        A_ba = np.delete(A_ba, pos, axis=0)         # 选中的列删除
        pos1 = find_pos_VecInMatrix(A_ba1, b_k)
        pos_selected_v.append(pos1)                 # 纪录最大投影系数的位置
        if Aug_t is None:                          # 将最大贡献向量（未单位化的）加入Aug_t矩阵
            Aug_t = T_tran[pos1]
        else:
            Aug_t = np.c_[Aug_t, T_tran[pos1]]
        A_new_plus = get_matri_new_plus(Aug_t)
        aug_y = A_new_plus.dot(s)                   # 解最小二乘解
        r_n = s - Aug_t.dot(aug_y)                  # 求残差

    for item in range(m):                          # 重构的谱域向量
        pos = pos_selected_v[item]
        x_r = aug_y[item]
        try:
            hat_y[pos] = x_r
        except np.ComplexWarning:
            pass

    hat_x = mat_dct_1d.T.dot(hat_y)                 # 做逆傅里叶变换重构得到时域信号
    return hat_x



# ---生成稀疏基DCT矩阵---
mat_dct_1d = np.zeros((256,256))
v = range(256)
for k in range(0,256):
    dct_1d = np.cos(np.dot(v, k*math.pi/256))
    if k > 0:
        dct_1d = dct_1d-np.mean(dct_1d)
    mat_dct_1d[:, k] = dct_1d/np.linalg.norm(dct_1d)   # 默认为求矩阵二范数:矩阵整体元素平方和开根号，不会保留矩阵二维特性


# ---生成高斯随机观测矩阵---
N = 256                                             # 向量长度
sampleRate = 0.75                                   # 采样率，也就是256长度的向量只采样64个
im = cv2.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/lesson_0/lena.jpg')                        # 读取图像
im = cv2.resize(im, (N, N))                         # 将图像修改成256X256的大小，这么做主要是方便计算

Phi=np.random.randn(int(sampleRate*N), N)           # 生成高斯随机采样矩阵
s = Phi.dot(im)                                     # 获得线性测量，s其实就是我们要采样的数据

P = Phi.dot(mat_dct_1d.T)    # 恢复矩阵(测量矩阵*正交反变换矩阵)


# ---重建---
restruct_im = np.zeros([256, 256, 3])               # 重构的图像
# 对每一个通道的每一列进行重构向量，并写入图像
for x in range(256):
    for y in range(3):
        restruct_s = cs_omp(s[:, x].T[y], P)        # 重构向量
        restruct_im[x].T[y] = restruct_s            # 将重构的向量写入图像

restruct_im = np.array(restruct_im, dtype=np.uint8)  # 这里一定要将矩阵的数据形式转换为uint8,不然图片无法正常显示

cv2.imshow('im_re', restruct_im)
cv2.imshow('im_ss', im)
cv2.waitKey(0)
