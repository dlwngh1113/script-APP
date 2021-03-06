from tkinter import *
from tkinter.font import *
import tkinter.ttk
# api에 사용할 모듈
import urllib.request
# 웹 브라우저 열기에 사용할 모듈
import webbrowser

client_id = '3rzrKUftiMZU0SeyQ2ED'
client_secret = 'NtYskSEN1D'


class MapFrame:
    def __init__(self, frame):
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=20)
        mapLabel = Label(frame, text='지도', font=self.Labelfont, bg='light green')
        mapLabel.place(x=0, y=25)

        # 검색 할 라벨 생성
        self.initEntry(frame)
        # 네이버 지도 연결해서 위치 보여주는 버튼
        self.initButton(frame)

    def initEntry(self, frame):
        self.mapEntry = Entry(frame, width=15, font=self.Labelfont)
        self.mapEntry.place(x=75, y=25)

    def initButton(self, frame):
        self.mapButton = Button(frame, text='열기', width=4, height=1, relief='raised', bg='light cyan',
                                font=Font(family='italic', size=15, weight='bold'), command=self.connectMap)

        self.mapButton.place(x=325, y=25)

    def connectMap(self):
        # 지도 url 열기
        url = 'https://map.naver.com/'
        option = '?sm=top_hty&fbm=1&ie=utf8&'
        if self.mapEntry.get() == '':
            return False
        query = 'query=' + urllib.parse.quote(self.mapEntry.get())

        url_query = url+option+query
        webbrowser.open_new(url_query)
        pass
