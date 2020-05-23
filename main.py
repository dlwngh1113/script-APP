from tkinter import *
from tkinter.font import *


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry('1080x720')

        APP = Font(family='맑은 고딕', size=20)
        nameTag = Label(self.window, text='APP', font=APP)
        nameTag.place(x=0, y=0)

        self.leftFrame = Frame(self.window, width=540, height=700, bg='black')
        self.leftFrame.pack(side=LEFT)
        self.rightFrame = Frame(self.window, width=540, height=700, bg='white')
        self.rightFrame.pack(side=RIGHT)

        self.window.mainloop()
        pass


MainGUI()
