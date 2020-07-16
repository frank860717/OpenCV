import cv2
import numpy as np
from matplotlib import pyplot as plt

#IMREAD_GRAYSCALE可將輸入的圖片變更為灰階
img=cv2.imread('20200627_jole.png',cv2.IMREAD_GRAYSCALE)
# img_color=cv2.imread('20200627_jole.png')
img2=cv2.imread('20190510.png')
img3=cv2.imread('10.png')
img4=cv2.imread('1.png')

print(img)
# print(img_color)

# # 輸出圖片視窗
# cv2.imshow('myimg',img)
# cv2.imshow('myimg2',img2)
# # 等待按鍵(鍵盤),否則一執行完圖片視窗就會關掉
# #waitKey 0 代表無限期等待
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#將灰階圖儲存
cv2.imwrite('grayJole.png',img)

#matplotlib是繪圖庫
#camp 使用灰階
#interpolation 內差值,做放大縮小
# plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()

#兩張圖混和
#必須要相同大小
#addWeighted 修改透明度
dst=cv2.addWeighted(img4,0.7,img3,0.3,0)
cv2.namedWindow("dst",0)
#resize 調整影像大小用
cv2.resize(img4,(100,100))
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()