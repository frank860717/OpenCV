import numpy as np
import cv2



# 選擇第1隻攝影機
cap = cv2.VideoCapture(0)

while(True):
# 從攝影機擷取一張影像
# 一個frame都是一個圖檔
 ret, frame = cap.read()

# Our operations on the frame come here
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#  顯示圖片
 cv2.imshow('frame',frame)
#  若按下 q 鍵則離開迴圈
 if cv2.waitKey(1) & 0xFF == ord('q'):
    #按下q之後,直接將最後一個frame寫入jpg檔
    cv2.imwrite('test2.jpg',frame)
    break

# 釋放攝影機
cap.release()
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()