import requests
import mysql.connector
import re

import Db
import FileUtil
from bs4 import BeautifulSoup

URL = 'http://www.xxbiquge.com'
conn = mysql.connector.connect(host='localhost',port = Db.prot,user='root', password='root', database='xiaoshuo')
cur = conn.cursor()
session = requests.Session()

class Article:
    url = ''
    name = ''
    category = ''



def getCategoryArticle(categoryname,url):
    response = session.get(url)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text,'html.parser')
    left = soup.find('div',class_='l')
    right = soup.find('div',class_='r')
    leftList = left.find_all('span',class_='s2')
    rightList = right.find_all('a')

    for item in leftList:
        article = Article()
        article.category = categoryname
        article.name = item.a.text
        article.url = URL+item.a.get('href')

        save(article)
        # print(article.name+"  "+article.url)

    for item in rightList:
        article = Article()
        article.category = categoryname
        article.name = item.text
        article.url = URL+item.get('href')
        save(article)
        # print(article.name+"  "+article.url)
    conn.commit()
def save(article):
    cur.execute('select name from normal where name=%s',[article.name])
    result = cur.fetchone()
    if(result == None):
        print(article.name+'--------'+article.name+'-----------------save to db')
        cur.execute('insert into normal(name,url,category) values(%s,%s,%s)',[article.name,article.url,article.category])
    else:
        print(article.category+'--------'+article.name+'-----------------已存在')

def getNormalResource():
    cur.execute('select name,url from category')
    result = cur.fetchall();
    if(result!=None):
        for item in result:
            if(str(item[0])=='排行榜单'):
                continue
            elif(str(item[0])!='完本小说'):
                getCategoryArticle(item[0],item[1])

#---------------start-----------------------------

# getCategoryArticle('玄幻奇幻','http://www.xxbiquge.com/xclass/1/1.html')