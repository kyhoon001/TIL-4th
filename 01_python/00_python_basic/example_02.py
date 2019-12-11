import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#1. webbrowser 열기
webbrowser.open('https://www.google.com')
webbrowser.open_new('https://www.naver.com')
webbrowser.open_new_tab('https://www.daum.net')

#2. 웹 정보 가져오기
res = requests.get('https://www.naver.com')
print(res)
print(res.text)
print(res.status_code)

#3. 원하는 정보만 선택하여 출력하기(코스피, 환율 등)
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)
print(f'오늘의 코스피 지수는 {kospi.text}입니다.')

url2 = 'https://finance.naver.com/marketindex/'
response = requests.get(url2).text
soup = BeautifulSoup(response, 'html.parser')
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(exchange.text)
print(f'오늘의 환율 지수는 {exchange.text}입니다.')

#4. 네이버 실시간 검색어 출력하기
url = 'https://www.naver.com/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
now = datetime.now()
words = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
print(f'{now}기준 실시간 검색어')
# for word in words:
#     print(word.text)

for i, word in enumerate(words):
    print(f'{i+1}위: {word.text}')

