import requests
import mysql.connector
from bs4 import BeautifulSoup
import Db



#获取hot区资源
class Info:
    def __init__(self,category):
        self.name = ''
        self.category = category
        self.url = ''

class HotResource:
    conn = mysql.connector.connect(host='localhost',port = Db.prot,user='root', password='root', database='xiaoshuo')
    cur = conn.cursor()
    session = requests.Session()
    response = session.get("http://www.xxbiquge.com/")
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text,'html.parser')

    def insert(self,info):
        self.cur.execute('select name from hot where name=%s',[info.name])
        result = self.cur.fetchone()
        if(result == None):
            print('热门----------------'+info.name+'------------save to db')
            self.cur.execute('insert into hot(name,url,category) values(%s,%s,%s)',[info.name,info.url,info.category])
        else:
            print('热门----------------'+info.name+'------------已存在')


    def getHot(self):
        hot = self.soup.find('div',id='hotcontent')
        normal = self.soup.find_all('div',class_='novelslist')
        new = self.soup.find('div',id='newscontent')

        left = hot.find('div',class_='l')
        right = hot.find('div',class_='r')

        left_items = left.find_all('div',class_='item')
        right_items = hot.find_all('li')

        #hot区,左侧数据
        for litem in left_items:
            info = Info('热门')
            info.name = litem.dt.a.text
            info.url = 'http://www.xxbiquge.com'+litem.dt.a.get('href')
            self.insert(info)
        self.conn.commit()
        #hot区,右侧数据
        for ritem in right_items:
            info = Info('热门')
            info.url = 'http://www.xxbiquge.com'+ritem.a.get('href')
            info.name = ritem.a.text
            self.insert(info)
        self.conn.commit()















