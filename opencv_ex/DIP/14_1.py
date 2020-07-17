import cv2
import numpy as np

img = cv2.imread('20190510.png')
# 方法一 设置缩放比例
# Resizecv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# 它的参数输入却是 宽×高×颜色通道。
# interpolation	說明:
# INTER_NEAREST	最近鄰插值
# INTER_LINEAR	雙線性插值（預設）
# INTER_AREA	使用像素區域關係進行重採樣。它可能是圖像抽取的首選方法，因為它會產生無雲紋理(波紋)的結果。 但是當圖像縮放時，它類似於INTER_NEAREST方法。
# INTER_CUBIC	4x4像素鄰域的雙三次插值
# INTER_LANCZOS4	8x8像素鄰域的Lanczos插值
dst1 = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)

# 方法二 直接设置输出尺寸
height, width = img.shape[:2]  # 获得原尺寸
dst2 = cv2.resize(img, (int(0.5*width), int(0.5*height)),
                  interpolation=cv2.INTER_CUBIC)  # 输出尺寸必须为整型
while(1):
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
