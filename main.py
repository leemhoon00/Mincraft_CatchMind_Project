import numpy as np
import cv2

img = cv2.imread('lenna.PNG')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # color to gray

ret, dst = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY) # 임계값 127을 기준으로 이진화

dst = cv2.resize(dst,(128,128)) # 128 by 128로 다운샘플링 - 이 과정에서 0 또는 255 였던 필셀값이 중간값으로 평균화됨

ret, dst = cv2.threshold(dst, 127,255,cv2.THRESH_BINARY) # 임계값 127을 기준으로 이진화 한번 더 해줌

print('이미지 사이즈 : {}'.format(dst.shape))
print(dst)
cv2.imshow("binary",dst)
cv2.waitKey(0)