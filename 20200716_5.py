import cv2
import numpy as np
from matplotlib import pyplot as plt

# img=cv2.imread('20190510.png')
img3=cv2.imread('20190510.png')
print("這是原本的:",img3)
cv2.imshow('dst2', img3)
# cvtColor 顏色空間轉換
imgChange =cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
print("這是轉換後的:",imgChange)
# print(img_color)

# cv2.namedWindow("dst",0)
# cv2.resize(img3,(100,100))

cv2.imshow('dst', imgChange)
cv2.waitKey(0)
cv2.destroyAllWindow()

