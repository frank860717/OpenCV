import cv2
import numpy as np
# 以单通道灰度图像读入
# img = cv2.imread('20190510.png', 0)
# shape 多接收了color,imread即可輸入彩色通道
img = cv2.imread('20190510.png')
# 添加color 即可輸出彩色旋轉,
# 图像的大小可以通过其shape属性来获取，shape返回的是一个tuple元组，
# 第一个元素表示图像的高度，
# 第二个表示图像的宽度，
# 第三个表示像素的通道数。
rows, cols, color = img.shape
# 这里的第一个参数為旋轉中心，第二个為旋轉角度，第三个為旋轉後縮放的因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.6)
# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (cols, rows))
while(1):
    cv2.imshow('src', img)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
