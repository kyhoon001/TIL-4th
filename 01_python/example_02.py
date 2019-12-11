import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# webbrowser.open('www.google.co.kr')
# webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')

# res = requests.get('http://naver.com')
# print(res.status_code)

url = 'https://www.naver.com/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
now = datetime.now()
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
print(f'{now}기준 실시간 검색어')
# for name in search:
#     print(name.text)

for i, name in enumerate(search):
    print(f'{i+1}위: {name.text}')

