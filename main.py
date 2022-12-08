import cv2
import camera
import numpy as np
from mcpi.minecraft import Minecraft
import Draw_Screen as ds
from mcpi import entity
from mcpi import event

mc = Minecraft.create()

chatEvents = mc.events.pollChatPosts()
print(chatEvents)

# pix = camera.capture()

# test = ds.RGBBlock(mc)
# test.setPaint128Location() #한번만 실행,도화지 그릴위치와 주변 환경정리
# test.setPixLocation() #이미 맵이 완성되었으면 위치만 잡아주기

# test.print2DtoBlocks(pix) #128X128PIX데이터(RGB) 입력시 프린터