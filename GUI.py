from tkinter import *

class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def callback(self, event):
        print(self.name.get())

    def initUI(self):
        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.name = StringVar()

        textbox = Entry(self,textvariable=self.name)
        textbox.grid(column=0,row=0)
        textbox.place(x=0,y=0,relwidth=0.5,relx=0.25)
        textbox.bind('<Return>',self.callback)

    def centerWindow(self):
        w = self.master.winfo_screenwidth()
        h = 20

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        # y = (sh - h)/6
        y=0
        self.master.geometry('%dx%d+%d+%d' % (w,h,x,y))

def Show_Textbox():
    root = Tk()
    ex = Example()
    root.mainloop()

