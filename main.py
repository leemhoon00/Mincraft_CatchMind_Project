import cv2
import camera
import numpy as np
from mcpi.minecraft import Minecraft
import Draw_Screen as ds
from mcpi import entity
from mcpi import event
import GUI as g

mc = Minecraft.create()

test = ds.RGBBlock(mc)
test.setPaint128Location() #한번만 실행,도화지 그릴위치와 주변 환경정리
test.setPixLocation() #이미 맵이 완성되었으면 위치만 잡아주기

g.Show_Textbox()#채팅창 띄우기

pix = camera.capture()
test.print2DtoBlocks(pix) #128X128PIX데이터(RGB) 입력시 프린터
