# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
if count < 1:
    print("Count must be a positive integer")
    exit()
cicle = 0
while cicle < count:
    l = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        l.append(tag.get('href', None))
    obj = l[position-1]
    url = obj
    print("Retrieving: ", url)
    cicle+=1
    
'''
复盘：
BeautifulSoup(html, 'html.parser') 返回值是一个dict
get(key, default= None) 返回value

l: list 每次循环，需要更新，所以在循环内声明。
'''