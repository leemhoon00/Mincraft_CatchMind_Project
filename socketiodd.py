# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:42:08 2022

@author: Administrator
"""
import socketio

sio = socketio.Client()
sio.connect('http://ec2-54-249-31-97.ap-northeast-1.compute.amazonaws.com:3000') #서버 연결

@sio.on('answerCheck')#정답 체크하는 이벤트
def checkAnswer(data):
    if(data == 1):
        print("아쉽지만 늦었습니다.")
    elif(data == 2):
        print("정답이 등록되지않았습니다.")
    else:
        print("오답입니다.")

@sio.on('answerWinner')#우승자가 나올시 메시지 출력 이벤트
def winner(data):
    print(data + "가 정답을 맞췄습니다.")

sio.emit('setAnswer','개구리')#정답 등록
sio.emit('answerCheck',{'player' : 'kyungil','answer':'개구'})#정답 체크 양식 answer는 정답 player는 닉네임
sio.emit('answerCheck',{'player' : 'kyung','answer':'개구리'})
sio.emit('answerCheck',{'player' : 'kyungil','answer':'개구리'})

text = input("입력:")#바로 disconnect되지않도록 막아주는거
sio.disconnect()#프로그램 종료시에 실행하여 서버분리
