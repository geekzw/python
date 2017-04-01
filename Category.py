import requests
import mysql.connector
import re

import Db
import FileUtil
from bs4 import BeautifulSoup

#抓小说类别
URL = 'http://www.xxbiquge.com'

def getCategory():
    conn = mysql.connector.connect(host='localhost',port = Db.prot,user='root', password='root', database='xiaoshuo')
    cur = conn.cursor()
    session = requests.Session()
    response = session.get(URL)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text,'html.parser')
    nav = soup.find('div',class_='nav')
    list = nav.find_all('a')
    for item in list:
        if(item.text!='首页' and item.text!='临时书架' and item.text!='永久书架'):
            name = item.text
            url = URL+item.get('href')
            cur.execute('select name from category where name=%s',[name])
            result = cur.fetchone()
            if(result == None):
                print(name +'--------------save to db')
                cur.execute('insert into category(name,url) values(%s,%s)',[name,url])
    conn.commit()
# getCategory()