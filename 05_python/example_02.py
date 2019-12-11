import webbrowser
import requests
from bs4 import BeautifulSoup

# webbrowser.open('www.google.co.kr')
# webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')

# res = requests.get('http://naver.com')
# print(res.status_code)

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)