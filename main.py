from tkinter import *
from tkinter.font import *
from search import *

frameHeight = 580
WIDTH = 960
HEIGHT = 640


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(False, False)

        APP = Font(family='italic', size=40, slant='italic')
        nameTag = Label(self.window, text='APP', font=APP)
        nameTag.grid(row=0, column=0)

        self.searchFrame = Frame(self.window, width=WIDTH / 2 - 30, height=frameHeight, relief=GROOVE, bg='lightgray')
        #self.searchFrame.place(x=0, y=HEIGHT - frameHeight)
        self.searchFrame.grid(row=1, column=0)
        SearchFrame(self.searchFrame)

        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=frameHeight, bg='gray')
        self.mapFrame.grid(row=1, column=1)
        #self.mapFrame.place(x=WIDTH / 2 - 30, y=HEIGHT - frameHeight)

        self.funcFrame = Frame(self.window, width=90, height=frameHeight, bg='cyan')
        self.funcFrame.grid(row=1, column=2)
        #self.funcFrame.place(x=WIDTH - 90, y=HEIGHT - frameHeight)

        self.window.mainloop()
        pass


MainGUI()
