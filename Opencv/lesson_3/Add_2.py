import cv2 as cv


# 加载两张图片
img1 = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color2.jpg')
img2 = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')

# 我想把logo放在左上角，所以我创建了ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]


# 现在创建logo的掩码，并同时创建其相反掩码
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 把img2图像转换为灰度图像
# 隔离图像上像素的边缘，下面函数将大于10像素的值置为0,小于的置为255!!!
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)  # mask为掩膜
# 在cv2.thresh(src, thresh, maxval, type)中，type=cv.THRESH_BINARY为阈值的类型
# 1.cv2.THRESH_BINARY表示阈值的二值化操作，大于阈值使用maxval表示，小于阈值使用0表示
# 2.cv2.THRESH_BINARY_INV表示阈值的二值化翻转操作，大于阈值的使用0表示，小于阈值的使用最大值表示
# 3.cv2.THRESH_TRUNC表示进行截断操作，大于阈值的使用阈值表示，小于阈值的不变
# 4.cv2.THRESH_TOZERO表示进行化零操作，大于阈值的不变，小于阈值的使用0表示
# 5.cv2.THRESH_TOZERO_INV表示进行化零操作的翻转，大于阈值的使用0表示，小于阈值的不变
mask_inv = cv.bitwise_not(mask)  # 按位非操作


# 现在将ROI中logo的区域涂黑
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
# 仅从logo图像中提取logo区域
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# 将logo放入ROI并修改主图像
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()