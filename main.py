from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
from search import *
from map import *

frameHeight = 580
WIDTH = 960
HEIGHT = 640


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("학원 교습소 검색 프로그램")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(False, False)

        #왼쪽 상단 APP글자 띄우기
        APP = Font(family='bauhaus 93', size=40, slant='italic')
        nameTag = Label(self.window, text='APP', font=APP, width=4)
        nameTag.grid(row=0, column=0, sticky='w')

        #왼쪽의 학원 교습소 위치 검색 프레임
        self.searchFrame = Frame(self.window, width=WIDTH, height=frameHeight, bg='light gray')
        self.searchFrame.place(x=0, y=60)
        SearchFrame(self.searchFrame)

        #중간의 지도 보여주는 프레임
        self.mapFrame = Frame(self.window, width=WIDTH / 2 - 60, height=frameHeight - 80, bg='magenta')
        self.mapFrame.place(x=450, y=130)
        MapFrame(self.mapFrame)

        #오른쪽의 텔레그램, 메일 보내는 아이콘 위치하는 프레임
        self.funcFrame = Frame(self.window, width=70, height=frameHeight - 50, bg='cyan')
        self.funcFrame.place(x=880, y=100)

        #나중에 지워줘야 하는 프레임(검색 프레임에 합쳐야함)
        self.resultFrame = Frame(self.window, width=WIDTH / 2 - 50, height=frameHeight / 2 + 60, bg='green')
        self.resultFrame.place(x=10, y=280)

        self.window.mainloop()
        pass


MainGUI()
