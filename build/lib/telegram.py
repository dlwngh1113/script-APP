from teller import *
from tkinter import *
from tkinter.font import *
import tkinter.ttk
import telepot

BotID = '1135207639:AAFLPlKeeWRMvAHv95tWfJjl_9cetDkV9FY'
UserID = '1062661278'


class TelegramFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=12)
        telegramLabel = Label(frame, text='TELEGRAM', font=self.Labelfont, bg='light cyan')
        telegramLabel.place(x=0, y=270)

        self.image = PhotoImage(file="telegram.png")
        self.initButton(frame)

    def initButton(self, frame):
        self.telegramButton = Button(frame, width=70, height=70, image=self.image, command=self.startTelegram)
        self.telegramButton.place(x=10, y=300)

    def startTelegram(self):
        start()
        pass
