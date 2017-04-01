# coding=utf-8

import requests
import re

headers = {
    'Accept':'application/json, text/javascript, */*;q=0.01',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'napi.uc.cn',
    'Origin':'http://qiqu.uc.cn',
    'Referer':'http://qiqu.uc.cn/?uc_param_str=frpfvedncpssntnwbipreime',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

form = {
    '_app_id':'hottopic',
    '_size':'1',
    '_fetch':'1',
    '_select':'_pos'
}

url = 'http://napi.uc.cn/3/classes/topic/lists/topic_list?_app_id=hottopic&_size=1&_fetch=1&_select=_pos'
session = requests.Session()
session.get()
