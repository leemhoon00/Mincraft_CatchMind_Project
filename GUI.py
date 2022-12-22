from tkinter import *
import socketio

sio = socketio.Client()

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        sio.connect('http://ec2-54-249-31-97.ap-northeast-1.compute.amazonaws.com:3000')#서버 연결

    def callback(self, event):
        args = self.name.get().split()
        if(args[0] == '/setAnswer'):
            print('정답 등록완료')
            sio.emit('setAnswer', args[1])
        elif(args[0] == '/setPlayername'):  
            print('player이름 등록완료')
            self.playerName = args[1]
        else:
            sio.emit('answerCheck',{'player' : self.playerName,'answer':args[0]})
        self.textbox.delete(0, END)
        
    def initUI(self):
        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.name = StringVar()

        self.textbox = Entry(self,textvariable=self.name)
        self.textbox.grid(column=0,row=0)
        self.textbox.place(x=0,y=0,relwidth=0.5,relx=0.25)
        self.textbox.bind('<Return>',self.callback)

    def centerWindow(self):
        w = self.master.winfo_screenwidth()
        h = 20

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        # y = (sh - h)/6
        y=0
        self.master.geometry('%dx%d+%d+%d' % (w,h,x,y))
        

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
    
    def __del__(self):
        sio.disconnect()#프로그램 종료시에 실행하여 서버분리
    
def Show_Textbox():
    root = Tk()
    ex = Example()
    root.mainloop()
        


