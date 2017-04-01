import requests
import mysql.connector
import re

import Db
import FileUtil
from bs4 import BeautifulSoup

#抓小说内容
URL = 'http://www.xxbiquge.com'
path = '/Users/gzw/Documents/workspace/python/'

class Article:

    def __init__(self):
        self.name = ''
        self.url = ''
        self.category = ''
        self.image = ''
        self.author = ''
        self.updatetime = ''
        self.status = ''
        self.news = ''
        self.description = ''
        self.path = ''


class Chapter:
    def __init__(self):
        self.articleid = ''
        self.name = ''
        self.url = ''
        self.path = ''

class ArticleServer:
    conn = mysql.connector.connect(host='localhost',port = Db.prot,user='root', password='root', database='xiaoshuo')
    cur = conn.cursor()
    session = requests.Session()
    response = ''
    soup = ''

    def getArticle(self,url):
        self.url = url
        self.response = self.session.get(self.url)
        self.response.encoding = 'utf8'
        self.soup = BeautifulSoup(self.response.text,'html.parser')

        article = Article()
        article.url = self.url
        top = self.soup.find('div',class_='box_con')
        #类别
        category = top.find('a',href=re.compile('.*?.html'))
        article.category = category.text

        #图片
        article.image = top.img.get('src')

        #main
        info = self.soup.find('div',id='info')
        article.name = info.h1.text
        list = info.find_all('p')
        author = list[0].text
        article.author = str(author).split('：')[1]
        #状态暂时略过
        status = list[1].text
        article.status = (str(status).split('：')[1]).split(',')[0]
        #更新时间
        update = list[2].text
        article.update = str(update).split('：')[1]

        news = list[3].text
        article.news = str(news).split('：')[1]

        description = self.soup.find('div',id='intro').p.text
        article.description = description

        self.cur.execute('select * from articlemain where name=%s',[article.name])
        result = self.cur.fetchone()
        dirName = str(self.url).split('/')[3]
        article.path = FileUtil.mkdir(dirName)
        if(result == None):
            print(article.name+'---------------------save to db')
            self.cur.execute('insert into articlemain(name,url,image,author,updatetime,news,description,category,path,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[article.name,article.url,article.image,article.author,article.update,article.news,article.description,article.category,article.path,article.status] )
            self.conn.commit()
        else:
            print(article.name+'---------------------已存在')


        self.cur.execute('select id from articlemain where name=%s',[article.name])
        result2 = self.cur.fetchone();
        if(result2 == None):
            print('查询小说信息失败')
            return
        self.getChapter(str(result2[0]),article.path,article.name)
        self.cur.execute('update hot set isload=%s where name=%s',['1',article.name])
        self.conn.commit()

    def getChapter(self,id,prePath,articlename):

        chapter = Chapter()
        chapter.articleid = id;
        list = self.soup.find('div',id='list').find_all('dd')
        index = 1;
        print('加载中')
        for item in list:
            chapter.articleid = id;
            url = item.a.get('href')
            name = item.a.text
            chapter.url = URL+url
            chapter.name = name
            content = self.getContent(chapter.url)
            print('before')
            self.cur.execute('select name from chapter where name=%s',[chapter.name])
            print('after')
            result = self.cur.fetchone()
            if(result == None):
                print(articlename+'-------'+chapter.name+'-------------------写入db')
                path = FileUtil.mkfile(prePath,str(index)+'.txt',content)
                chapter.path = path
                self.cur.execute('insert into chapter(name,articleid,url,path) values(%s,%s,%s,%s)',[chapter.name,chapter.articleid,chapter.url,chapter.path])
            else:
                print(articlename+'-------'+chapter.name+'-------------------已存在')

            if(index%500 == 0):
                print("commit")
                self.conn.commit()

            index+=1
        print("commit")
        self.conn.commit()
        print('finish')

    def getContent(self,url):
        text = self.session.get(url)
        text.encoding = 'utf8'
        soup = BeautifulSoup(text.text,'html.parser')
        content = soup.find('div',id='content').text
        return str(content).lstrip()







