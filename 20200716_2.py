import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('20190510.png') 
#這邊的順序是 BGR 不是 RGB
#前面兩個是照片大小設定
img[273:333,100:160] = 127

#擷取區塊
# aa = img[:,:]
# img[273:333,100:160] = aa
img[:,:,2] = 0

# img[:,:,0] = 0 #b設為0
# img[:,:,1] = 0 #g的通道都是0
#所以剩下紅色通道,所以圖片會紅通通的


print(img)

cv2.imshow('myimg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()