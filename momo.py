import requests
from bs4 import BeautifulSoup
url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=43pfh4052&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType"
headers = {'User-Agent': 'Googlebot', 'From': 'EMAIL'}

r = requests.get(url, headers = headers, allow_redirects = False)

#print(r.status_code)
#print(r.history)
#print(r.url)

#soup = BeautifulSoup(r.text, 'html.parser')