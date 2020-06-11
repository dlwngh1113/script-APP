from tkinter import *
from tkinter.font import *
import tkinter.ttk
import smtplib
from email.mime.text import MIMEText

WIDTH = 480
HEIGHT = 160


class MailFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)
        mailLabel = Label(frame, text='MAIL', font=self.Labelfont, bg='light cyan')
        mailLabel.place(x=13, y=50)

        self.Gmail = smtplib.SMTP('smtp.gmail.com', 587)
        self.Gmail.starttls()
        self.Gmail.login('jaewon990905@gmail.com', 'wamgdzzpvtknsvjl')

        self.image = PhotoImage(file="gmail.png")
        self.initButton(frame)

    def initButton(self, frame):
        self.mailButton = Button(frame, width=70, height=55, image=self.image, command=self.initWindow)
        self.mailButton.place(x=10, y=90)

    def initWindow(self):
        self.mailWindow = Tk()
        self.mailWindow.title("이메일 보내기")
        self.mailWindow.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.mailWindow.resizable(False, False)

        self.initFrame(self.mailWindow)
        self.initEntry(self.mailWindow)
        self.makeButton(self.mailWindow)

        self.mailWindow.mainloop()

    def initEntry(self, frame):
        mailLabel = Label(frame, text='보낼 사람', font=self.Labelfont, bg='light green')
        mailLabel.place(x=10, y=50)
        self.mailEntry = Entry(frame, width=30, font=self.Labelfont)
        self.mailEntry.place(x=120, y=50)

    def initFrame(self, frame):
        self.mailFrame = Frame(frame, width=WIDTH, height=HEIGHT, bg='light green')
        self.mailFrame.place(x=0, y=0)

    def makeButton(self, frame):
        self.sendButton = Button(frame, text='전송', width=4, height=1, relief='raised', bg='light cyan',
                                 font=Font(family='italic', size=15, weight='bold'), command=self.send)
        self.sendButton.place(x=200, y=100)

    def send(self):
        mailId = self.mailEntry.get()
        msg = MIMEText('학원/교습소 정보')
        msg['Subject'] = '정보를 입력하세요'

        self.Gmail.sendmail("jaewon990905@gmail.com", mailId, msg.as_string())
        self.Gmail.quit()
        self.mailWindow.destroy()


