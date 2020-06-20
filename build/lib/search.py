from tkinter import *
from tkinter.font import *
import tkinter.ttk
import requests
from bs4 import BeautifulSoup
import urllib

open_api_key = '28c84783ab7249d9b2251c0bb4bc525b'
url = 'https://openapi.gg.go.kr/TninsttInstutM?KEY='


class SearchFrame:
    def __init__(self, frame):
        self.Combofont = Font(family='italic', weight='bold', slant='roman', size=14)
        self.Labelfont = Font(family='italic', weight='bold', slant='roman', size=18)

        # 시/군 라벨 생성, 위치 지정
        Label(frame, text='시/군', font=self.Labelfont, bg='light green').place(x=15, y=25)
        #행정구역 더 추가해야함
        cities = ['고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시',
                  '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '여주시',
                  '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시',
                  '가평군', '양평군', '연천군']
        self.cityCombo = tkinter.ttk.Combobox(frame, values=cities, height=5, font=self.Combofont)
        self.cityCombo.configure(state='readonly')
        self.cityCombo.place(x=90, y=30)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.cityCombo.set('목록 선택')

        # 업종 라벨 생성, 위치 지정
        Label(frame, text='업종', font=self.Labelfont, bg='light green').place(x=15, y=80)
        #업종
        industries = ['교습소', '평생직업교육학원', '학교교과교습학원']
        self.industryCombo = tkinter.ttk.Combobox(frame, values=industries, height=3, font=self.Combofont)
        self.industryCombo.configure(state='readonly')
        self.industryCombo.place(x=90, y=85)
        frame.option_add('*TCombobox*Listbox.font', self.Combofont)
        self.industryCombo.set('목록 선택')

        # 검색 버튼 생성, 위치 지정
        Button(frame, text='검색', width=4, height=1, relief='raised', bd=4, font=self.Labelfont,
                             command=self.search, bg='light cyan').place(x=350, y=60)


        # 라벨 생성, 위치 지정
        Label(frame, text='학원 및 교습소 명', font=self.Labelfont, bg='light green').place(x=15, y=160)

        #학원 리스트 박스
        self.academyListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.academyListBox.place(x=15, y=230)

        #sample
        notebook = tkinter.ttk.Notebook(frame, width=50, height=20)

        #북마크 화살표 이미지
        self.leftArrow = PhotoImage(file="left_arrow.png")
        self.rightArrow = PhotoImage(file="right_arrow.png")

        #북마크 라벨
        Label(frame, text='북마크', font=self.Labelfont, bg='light green').place(x=450, y=160)

        # 북마크 버튼
        Button(frame, width=40, height=65, image=self.leftArrow, command=self.moveToList).place(x=387, y=400)
        Button(frame, width=40, height=65, image=self.rightArrow, command=self.moveToBook).place(x=387, y=300)

        #북마크 리스트 박스
        self.bookmarkListBox = Listbox(frame, selectmode='extended', width=50, height=20)
        self.bookmarkListBox.place(x=450, y=230)

    def moveToBook(self):
        selection = self.academyListBox.curselection()

        for i in range(len(selection)):
            self.bookmarkListBox.insert(i, self.academyListBox.get(selection[i]))
        pass

    def getBookMark(self):
        lst = []
        for i in range(self.bookmarkListBox.size()):
            lst.append(self.bookmarkListBox.get(i))
        return lst

    def moveToList(self):
        selection = self.bookmarkListBox.curselection()
        self.bookmarkListBox.delete(selection[0], selection[len(selection)-1])
        pass

    def search(self):
        self.academyListBox.delete(0, self.academyListBox.size())
        SIGUN_NM = urllib.parse.quote(self.cityCombo.get())
        INDUTYPE = urllib.parse.quote(self.industryCombo.get())
        params = '&SIGUN_NM=' + SIGUN_NM + '&INDUTYPE_DIV_NM=' + INDUTYPE
        open_url = url + open_api_key + params

        '''1        SIGUN_NM                    시군명
            2       SIGUN_CD                    시군코드
            3       EMD_NM                      구 / 읍면동명
            4       INDUTYPE_DIV_NM             업종구분명
            5       FACLT_NM                    시설명
            6       REPRSNTV_NM                 대표자명
            7       CRSE_CLASS_NM               교습과정명
            8       TELNO                       전화번호
            9       REFINE_ZIP_CD               소재지우편번호
            10      REFINE_LOTNO_ADDR           소재지지번주소
            11      REFINE_ROADNM_ADDR          소재지도로명주소
            12      REFINE_WGS84_LAT            WGS84위도
            13      REFINE_WGS84_LOGT           WGS84경도'''

        req = requests.get(open_url)
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        academies = soup.find_all('faclt_nm')
        telephones = soup.find_all('telno')

        academyList = [x.text for x in academies]
        phoneList = [x.text for x in telephones]
        for x in range(len(academyList)):
            academy = academyList[x]
            phone = phoneList[x]
            self.academyListBox.insert(x, academy + '  ' + phone)