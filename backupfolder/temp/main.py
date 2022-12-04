import Draw_Screen as ds
import numpy as np
import cv2
from mcpi import minecraft

mc = minecraft.Minecraft.create()

img = cv2.imread('../lenna.PNG')
#cv2.imshow('dddd',img)
#cv2.waitKey(0)
dst = cv2.resize(img, dsize=(128,128), interpolation=cv2.INTER_AREA)

cv2.imshow('dddd',dst)
cv2.waitKey(0)
# dst = cv2.resize(img,(128,128))

#cv2.imshow("binary",dst)

# test = ds.RGBBlock()
# test.setPaint128Location()#한번만 실행,도화지 그릴위치와 주변 환경정리
# test.setPixLocation()#이미 맵이 완성되었으면 위치만 잡아주기


#test.print2DtoBlocks(pix)#128X128PIX데이터(RGB) 입력시 프린터 
