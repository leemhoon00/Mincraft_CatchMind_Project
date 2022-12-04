import numpy as np
import cv2
import Draw_Screen as ds
from mcpi import minecraft

mc = minecraft.Minecraft.create()

img = cv2.imread('lenna.PNG')
dst = cv2.resize(img, dsize=(128,128), interpolation=cv2.INTER_AREA)

# cv2.imshow('dddd',dst)
# cv2.waitKey(0)

test = ds.RGBBlock()
test.setPaint128Location()#한번만 실행,도화지 그릴위치와 주변 환경정리
test.setPixLocation()#이미 맵이 완성되었으면 위치만 잡아주기

pix = np.array(dst)
test.print2DtoBlocks(pix)#128X128PIX데이터(RGB) 입력시 프린터 
