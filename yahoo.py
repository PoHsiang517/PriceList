import requests
from bs4 import BeautifulSoup


url = "https://tw.buy.yahoo.com/search/product?p=YS-826DW"
headers = {'User-Agent': 'Googlebot'}
r = requests.get(url, headers = headers, allow_redirects = False)

soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all("span", class_="BaseGridItem__content___3LORP")
#print(len(items))

contents = soup.find_all("span", class_="BaseGridItem__title___2HWui")
prices = soup.find_all("em", class_="BaseGridItem__price___31jkj")
#all_items = soup.find_all("a", class_="BaseGridItem__content___3LORP")
#links = [i.find('a').get('href') for i in all_items]

for c, p in zip(contents, prices):
    print(c.contents[0])
    print(p.contents[0])
    print('*---------------------------------*')