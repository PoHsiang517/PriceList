import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
#改用行動版網頁即可抓到MOMO搜尋出的商品
#url = "https://m.momoshop.com.tw/search.momo?searchKeyword=43pfh4052&couponSeq=&searchType=1&cateLevel=-1&ent=k&_imgSH=fourCardStyle"
url = "https://m.momoshop.com.tw/search.momo?searchKeyword=%E8%97%8D%E7%89%99%E8%80%B3%E6%A9%9F&couponSeq=&searchType=1&cateLevel=-1&ent=k&_imgSH=fourCardStyle"
headers = {'User-Agent':ua.chrome}
r = requests.get(url, headers = headers)

#print(r.status_code)
#print(r.history)
#print(r.url)

soup = BeautifulSoup(r.text, 'html.parser')

contents = soup.find_all("li", class_="goodsItemLi") #改抓 li列出所有商品
items = soup.find_all("p", class_="prdName")
discount = soup.find_all("p", class_="prdEvent") #撈不到 /滿n件現折xxx/
#print(discount)
prices = soup.find_all("b", class_="price")

for c, i, p in zip(contents, items, prices):
	print(i.contents[0].strip())
	print(p.contents[0])

