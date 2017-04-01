# coding=utf-8
import requests
import json
import re
import FileUtil
from bs4 import BeautifulSoup

URL = 'http://www.xxbiquge.com'

class Chapter:
    def __init__(self):
        self.articleid = ''
        self.name = ''
        self.url = ''
        self.path = ''

dirName = str('http://www.xxbiquge.com/20_20331/').split('/')
print(dirName)

print(1000 %500)


session = requests.Session()
def getChapter(url,prePath):

    response = session.get(url)
    chapter = Chapter()
    soup = BeautifulSoup(response.text,'html.parser')
    list = soup.find('div',id='list').find_all('dd')
    index = 1;
    print('加载中')
    for item in list:
        print(index)
        chapter.articleid = id;
        url = item.a.get('href')
        name = item.a.text
        chapter.url = URL+url
        chapter.name = name
        content = getContent(chapter.url)
        path = FileUtil.mkfile(prePath,str(index)+'.txt',content)
        chapter.path = path
        index+=1
    print("commit")
    print('finish')

def getContent(url):
    text = session.get(url)
    text.encoding = 'utf8'
    soup = BeautifulSoup(text.text,'html.parser')
    content = soup.find('div',id='content').text
    return str(content).lstrip()

getChapter('http://www.xxbiquge.com/9_9187/','/Users/gzw/Documents/workspace/python/9_9187')