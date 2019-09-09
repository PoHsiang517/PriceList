import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
url = 'http://www.doubleround.com.tw/v2/Search?q=43pfh4052&shopId=5210'
headers = {'User-Agent': ua.random, 'From': 'EMAIL'}
r = requests.get(url, headers = headers, allow_redirects = False)
#print(r.status_code)
#print(r.history)
#print(r.url)

soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all("h3", class_="cabinet-instruction blind-instruction")
print(soup)
#無法抓到文字部分資料