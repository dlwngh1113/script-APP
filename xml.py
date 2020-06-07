'''import xml.etree.ElementTree as ET
tree = ET.parse('academy.xml')
root = tree.getroot()

row = root.findall("row")

cityName = [x.findtext("SIGUN_NM") for x in row]
cityDong = [x.findtext("EMD_NM") for x in row]

print(cityName)
print(cityDong)'''

import requests
from bs4 import BeautifulSoup
import urllib

open_api_key = '28c84783ab7249d9b2251c0bb4bc525b'
SIGUN_NM = urllib.parse.quote(input())
params = '&SIGUN_NM='+SIGUN_NM
url = 'https://openapi.gg.go.kr/TninsttInstutM?KEY='
open_url = url + open_api_key + params

req = requests.get(open_url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
values = soup.find_all('faclt_nm')
print([x.text for x in values][:5])