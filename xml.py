'''import xml.etree.ElementTree as ET
tree = ET.parse('academy.xml')
root = tree.getroot()

row = root.findall("row")

cityName = [x.findtext("SIGUN_NM") for x in row]
cityDong = [x.findtext("EMD_NM") for x in row]

print(cityName)
print(cityDong)'''

import requests
url = 'https://openapi.gg.go.kr/TninsttInstutM'