import numpy as np
import cv2

# Create a black image RGB都是0的圖
img=np.zeros((512,512,3), np.uint8)
#改成紅色(255 全紅)
img[:,:,2] = 175 

# Draw a diagonal blue line with thickness of 5 px

#img為要畫線的圖片名稱
#(0,0)=(x1, y1)
#(512,400)=(x2, y2)
#(255,255,0)為線條顏色(GBR或RGB，取決於是否使用cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#10 為線條粗細度
cv2.line(img,(0,0),(512,400),(255,255,0),10)
#畫正方形
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# cv2.line()畫直線
# cv2.circle()畫圓
# cv2.rectangle()畫矩形
# cv2.ellipse()畫橢圓
# cv2.polylines()畫多邊形
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello',(10,500), font,4,(255,255,255),2)

cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindow()