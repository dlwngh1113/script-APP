from xml import *
from tkinter import *
from tkinter.font import *
from tkinter.ttk import *


class SearchFrame:
    def __init__(self, frame):
        self.font = Font(family='italic', slant='italic')
        cityLabel = Label(frame, text='시/군', font=self.font, bg='gray')
        cityLabel.place(x=30, y=30)
        cityCombo = Combobox()
        pass
