import requests
import re
import mysql.connector
from bs4 import BeautifulSoup
import Tool
import os

URL = 'http://www.xxbiquge.com'
path = '/Users/gzw/Documents/workspace/python/test.txt'
conn = mysql.connector.connect(host='localhost',port = 32768,user='root', password='root', database='xiaoshuo')
cur = conn.cursor()
session = requests.Session()
response = session.get("http://www.xxbiquge.com/20_20331/")
response.encoding = 'utf8'
soup = BeautifulSoup(response.text,'html.parser')
content = soup.find('div',id='list')
# print(content)
chapter1 = content.a.get('href')

while(chapter1!='/20_20331'):
    url = URL+chapter1
    text = session.get(url)
    text.encoding = 'utf8'
    soup = BeautifulSoup(text.text,'html.parser')
    chapter1 = soup.find('a',text='下一章').get('href')
    print(next)
    title = soup.find('div',class_='bookname').h1.text
    print(title)

    content = soup.find('div',id='content').text
    print(content)
    with open(path,'a') as f:
        f.write(title+'\n')
        f.write(content+'\n')











