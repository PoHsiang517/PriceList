from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import sqlite3
from selenium import webdriver
import json
import requests


#商品查詢

def productsearch(main):
	global momosearch
	global pchomesearch
	global yahoosearch
	global shpsearch
	global itemname

    str(main)
    momo = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword="
    momosearch = momo+main
    pchome = "http://ecshweb.pchome.com.tw/search/v3.3/all/results?q="
    pchomesearch = pchome+main
    yahoo = "https://tw.search.mall.yahoo.com/search/mall/product?p="
    yahoosearch = yahoo+main
    shp1 = "https://shopee.tw/search/?keyword="
    shp2 = "&sortBy=sales"
    shpsearch = shp1+main+shp2
    print("momo購物網")
    print(momosearch)
    momoinfo()
    print("Pchome24H購物")
    print(pchomesearch)
    pchomeinfo()
    print("yahoo超級商城")
    print(yahoosearch)
    yahooinfo()
    print("蝦皮拍賣")
    print(shpsearch)
    shpinfo()

    