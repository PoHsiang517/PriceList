import requests
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = 'https://shopee.tw/search?keyword=43pfh4052'
headers = {'User-Agent': 'Googlebot', 'From': 'EMAIL'}
r = requests.get(url, headers = headers, allow_redirects = False)
#print(r.status_code)
#print(r.history)
#print(r.url)

soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
#print(len(items))

contents = soup.find_all("div", class_="_1NoI8_ _2gr36I")
prices = soup.find_all("span", class_="_341bF0")
all_items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
links = [i.find('a').get('href') for i in all_items]

for c, p, l in zip(contents, prices, links):
    print(c.contents[0])
    print(p.contents[0])
    print('https://shopee.tw/'+l)
    print('*---------------------------------*')