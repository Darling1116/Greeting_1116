import timeit

import cv2 as cv
import time

# 检查是否启用了优化
print(cv.useOptimized())

# 关闭它
cv.setUseOptimized(False)
print(cv.useOptimized())
