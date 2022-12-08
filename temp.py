from tkinter import *

class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        textbox = Entry(self, width=100)
        textbox.grid(column=0,row=3)

    def centerWindow(self):
        w = 290
        h = 50

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/6
        self.master.geometry('%dx%d+%d+%d' % (w,h,x,y))

def main():
    root = Tk()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    main()