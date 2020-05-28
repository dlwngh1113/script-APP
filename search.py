from xml import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk


class SearchFrame:
    def __init__(self, frame):
        self.font = Font(family='italic', weight='bold', slant='roman')
        cityLabel = Label(frame, text='시/군', font=self.font)
        cityLabel.place(x=30, y=25)
        values = [str(i) for i in range(10)]
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)
        cityCombo.configure(state='readonly')
        cityCombo.place(x=100, y=30)
        cityCombo.set('목록 선택')

        jobLabel = Label(frame, text='업종', font=self.font)
        jobLabel.place(x=30, y=80)
        values = [str(i) for i in range(10)]
        cityCombo = tkinter.ttk.Combobox(frame, values=values, height=5)
        cityCombo.configure(state='readonly')
        cityCombo.place(x=100, y=85)
        cityCombo.set('목록 선택')

        resultLabel = Label(frame, text='학원 및 교습소 명', font=self.font)
        resultLabel.place(x=30, y=150)

    def search(self):
        pass


