import cv2
import numpy as np
from matplotlib import pyplot as plt


img3 = cv2.imread('10.png')
img4 = cv2.imread('1.png')


dst = cv2.addWeighted(img4, 0.7, img3, 0.3, 0)
cv2.namedWindow("dst", 0)
# resize 調整影像大小用
cv2.resize(img4, (100, 100))
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
