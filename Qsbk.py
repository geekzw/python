# -*- coding: utf-8 -*-
import requests
import os
import re
import shutil
import urllib

#抓糗事百科趣图
page = 1
url = 'http://www.qiushibaike.com/pic/page/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
filePath = os.path.join(os.path.abspath('.'),'image1')

if(os.path.exists(filePath)):
    # os.rmdir(filePath)
    shutil.rmtree(filePath)
os.mkdir(filePath)
print (filePath)
def getPage(url,page):
    url = url+str(page)
    response = requests.get(url,headers=headers)
    return response.text

def getImagePath(htmlPage):
    reg = 'src="(.+?\.jpg)" alt'
    regg = re.compile(reg)
    imageUrl = re.findall(regg,htmlPage)
    # for i in range(len(imageUrl)):
    #     print imageUrl[i]
    return imageUrl

def downloadImage(images,page):
    index = 1;
    for url in images:
        ii = str(page)+str(index)
        urllib.request.urlretrieve(url,filePath+'/'+ii+'.jpg')
        index+=1
for i in range(1,35):
    print (i);
    page = getPage(url,i)
    imagePath = getImagePath(page)
    downloadImage(imagePath,i)