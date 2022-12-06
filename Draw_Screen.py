# -*- coding: utf-8 -*-
import numpy as np
#from mcpi.minecraft import Minecraft

#self.mc = Minecraft.create()

class RGBBlock:
    def __init__(self,mc):
        self.RGB = np.empty((0,3),int)
        self.block = np.empty((0,2),int)
        self.activeBlock()
        self.mc = mc
    
    def add(self,r1,g1,b1,blockID,blockData):
        self.RGB = np.append(self.RGB,np.array([[r1,g1,b1]]),axis=0)
        self.block = np.append(self.block,np.array([[blockID,blockData]]),axis=0)
        
    def add2(self,r1,g1,b1,r2,g2,b2,blockID,blockData):
        self.RGB = np.append(self.RGB,np.array([[r1,g1,b1],[r2,g2,b2]]),axis=0)
        self.block = np.append(self.block,np.tile([blockID,blockData],reps=[2,1]),axis=0)
        
    def add3(self,r1,g1,b1,r2,g2,b2,r3,g3,b3,blockID,blockData):
        self.RGB = np.append(self.RGB,np.array([[r1,g1,b1],[r2,g2,b2],[r3,g3,b3]]),axis=0)
        self.block = np.append(self.block,np.tile([blockID,blockData],reps=[3,1]),axis=0)
        
    def add4(self,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4,blockID,blockData):
        self.RGB = np.append(self.RGB,np.array([[r1,g1,b1],[r2,g2,b2],[r3,g3,b3],[r4,g4,b4]]),axis=0)
        self.block = np.append(self.block,np.tile([blockID,blockData],reps=[4,1]),axis=0)
        
    def activeBlock(self):
        self.add4(116,116,116,127,127,127,131,131,131,131,131,132, 1, 0) #stone
        self.add4(136,98,69,133,96,66,113,79,54,150,108,74, 3, 0) #dirt
        self.add2(169,169,169,143,143,143, 4, 0) #coddle stone
        self.add4(164,132,80,163,131,79,188,152,98,159,132,77, 5, 0) #OAK_WOOD_PLANK
        #self.add3(219,212,160,218,210,159,208,202,146, 12, 0) #SAND
        #self.add3(128,125,123,134,121,124,106,99,96, 13, 0) #GRAVEL
        self.add4(106,83,49,111,87,52,110,89,56,110,85,51, 17, 0) #OAK_WOOD
        #self.add4(209,207,202,225,224,220,221,220,215,212,210,205, 17, 2) #BIRCH WOOD
        self.add4(34,77,146,31,65,141,31,68,139,29,61,135, 22, 0) #LAPIS BLOCK
        self.add4(218,205,158,217,204,156,217,204,156,216,203,155, 24, 0) #SAND STONE
        self.add4(248,238,80,251,242,92,249,239,73,255,244,70, 41, 0) #GOLD BLOCK
        self.add2(239,239,239,230,230,230, 42, 0) #IRON BLOCK
        self.add4(146,100,87,147,100,87,147,101,88,148,101,88, 45, 2) #BRICK
        self.add4(21,19,31,20,18,29,21,19,30,20,18,30, 49, 0) #OBBISIDIAN
        self.add2(162,236,232,117,225,220, 57, 0) #DIAMOND BLOCK
        self.add4(243,252,252,238,255,255,240,251,251,242,251,251, 80, 0) #SNOW BLOCK
        self.add4(118,61,59,108,50,49,182,107,107,136,79,79, 87, 2) #NETHERRACK
        self.add4(150,122,74,144,120,72,149,123,72,133,109,62, 89, 0) #GLOW STONE
        self.add2(238,236,229,236,233,226,155, 2) #QUARTZ BLOCK
       #19 -75
        self.add2(232,231,231,200,200,200, 35, 0) #WOOL WHITE
        self.add2(221,119,52,235,132,62, 35, 1) #WOOL ORANGE
        self.add2(166,70,180,187,61,198, 35, 2) #WOOL MAGENTA
        self.add2(202,230,253,89,128,208, 35, 3) #WOOL LIGHT BLUE
        self.add2(214,200,42,182,169,24, 35, 4) #WOOL YELLOW
        self.add2(66,180,58,49,161,40, 35, 5) #WOOL LIME
        self.add2(210,128,158,205,92,122, 35, 6) #WOOL PINK
        self.add2(61,61,61,68,68,68, 35, 7) #WOOL GRAY
        self.add(162,168,168, 35, 8) #WOOL LIGHT GRAY
        self.add2(49,116,143,41,121,154, 35, 9) #WOOL CYAN
        self.add2(130,62,188,119,46,183, 35, 10) #WOOL PURPLE
        self.add2(43,53,133,37,49,146, 35,11) #WOOL BLUE
        self.add(76,48,30, 35, 12) #WOOL BROWN
        self.add2(55,72,28,162,197,69, 35, 13) #WOOL GREEN
        self.add2(157,56,51,188,52,47, 35, 14) #WOOL RED
        self.add(23,19,19, 35, 15) #WOOL BLACK
        self.add(159,165,177, 82, 0) #CLAY
        #self.add(150,152,37, 103, 0) #MELON
        
    def find_near(self,value):
        array = np.asarray(self.RGB)
        array = np.abs(array - value)
        array = array.sum(axis=1)
        return array.argmin()
    
    
    def setPaintLocation(self):#64x64
        self.x = 0
        self.y = 0
        self.z = 0
        self.mc.setBlocks(self.x-64,self.y+64,self.z+64,self.x,self.y,self.z,0,0)#주변공간 밀기
        self.mc.setBlocks(self.x+1,self.y,self.z,self.x+1,self.y+64,self.z+64,35,0)#게임시작 테이블 설치 앞면
        self.mc.setBlocks(self.x-65,self.y,self.z,self.x-65,self.y+64,self.z+64,35,15)#게임시작 테이블 설치 뒷면
        self.mc.setBlocks(self.x,self.y,self.z+65,self.x-65,self.y+64,self.z+65,35,15)#게임시작 테이블 설치 오른쪽면
        self.mc.setBlocks(self.x,self.y,self.z-1,self.x-65,self.y+64,self.z-1,35,15)#게임시작 테이블 설치 왼쪽면
        self.mc.setBlocks(self.x,self.y-1,self.z,self.x-65,self.y-1,self.z+64,35,15)#게임시작 테이블 설치 플레이어 바닥면
        self.mc.player.setPos(self.x-32,self.y,self.z+32)#중앙으로 플레이어 이동
        self.y = 63
        
    # 주변환경 정리 후 플레이어 위치이동
    def setPaint128Location(self):#128x128
        self.x = 0
        self.y = 0
        self.z = -64
        self.mc.setBlocks(self.x-110,self.y-64,self.z+128,self.x,self.y+64,self.z,0,0)#주변공간 밀기
        self.mc.setBlocks(self.x+1,self.y+64,self.z,self.x+1,self.y-64,self.z+128,35,0)#게임시작 테이블 설치 앞면
        self.mc.setBlocks(self.x-110,self.y+64,self.z,self.x-110,self.y-64,self.z+128,35,15)#게임시작 테이블 설치 뒷면
        self.mc.setBlocks(self.x,self.y+64,self.z+129,self.x-110,self.y-64,self.z+129,35,15)#게임시작 테이블 설치 오른쪽면
        self.mc.setBlocks(self.x,self.y+64,self.z-1,self.x-110,self.y-64,self.z-1,35,15)#게임시작 테이블 설치 왼쪽면
        self.mc.setBlocks(self.x-100,self.y-1,self.z+54,self.x-110,self.y-1,self.z+74,35,15)#게임시작 테이블 설치 플레이어 바닥면
        self.mc.player.setPos(self.x-103,self.y,self.z+64)#중앙으로 플레이어 이동
        self.y = 63
    
    # 그림그릴 위치 잡아주기
    def setPixLocation(self):
        self.x = 0
        self.y = 63
        self.z = -64
        
    def printBlock(self,x,y,z,c):
        self.mc.setBlock(x,y,z,self.block[c,0],self.block[c,1])
        
    def print2DtoBlocks(self,pix):
        for i in range(len(pix)):
            for j in range(len(pix)):
                blockrgb = self.find_near(pix[i,j])
                self.printBlock(self.x,self.y-i,self.z+j,blockrgb)