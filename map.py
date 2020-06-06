from xml import *
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
        mapLabel = Label(frame, text='지도', font=self.Labelfont)
        mapLabel.place(x=15, y=25)

        # 검색 할 라벨 생성
        self.initEntry(frame)
        # 네이버 지도 연결해서 위치 보여주는 버튼
        self.initButton(frame)

    def initEntry(self, frame):
        self.mapEntry = Entry(frame, width=15, font=self.Labelfont)
        self.mapEntry.place(x=100, y=25)

    def initButton(self, frame):
        self.mapButton = Button(frame, text='열기', width=4, height=1, relief='raised',
                                font=Font(family='italic', size=15, weight='bold'), command=self.connectMap)
        self.mapButton.place(x=100, y=25)

    def connectMap(self):
        # url과 검색 옵션 설정
        '''url = 'https://openapi.naver.com/v1/search/local.xml'
        option = '&display=3&sort=count'
        query = 'query=' + urllib.parse.quote(self.mapEntry.get())
        url_query = url + query + option

        request = urllib.request.Request(url_query)
        request.add_header('X-Naver_Client-Id', client_id)
        request.add_header('X-Naver_Client-Secret', client_secret)'''
        # 지도 url 열기
        url = 'https://search.naver.com/search.naver'
        option = '?sm=top_hty&fbm=1&ie=utf8&'
        query = 'query=' + urllib.parse.quote(self.mapEntry.get())

        url_query = url+option+query
        webbrowser.open_new(url_query)
        pass
