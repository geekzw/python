import requests
import re

from pip._vendor.distlib.compat import raw_input

#模拟登录github并抓取所有项目
class Github:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.session = requests.Session()#获取session
        self.url_login_page = 'https://github.com/login'
        self.url_login_action = 'https://github.com/session'
        self.headers = {#header可以抓包看,一般变化都不带,除非有header特殊验证的
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection':'keep-alive',
            'Host':'github.com',
            'Referer':'https://github.com/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }

    def login(self):
        form = {#登录表单,浏览器审查元素可以查看到表单都需要哪些数据,抓包也可以看到,注意隐藏的token字段
            'utf8':'✓',
            'authenticity_token':self.getToken(),
            'login':self.username,
            'password':self.password
        }
        response = self.session.post(self.url_login_action,data=form,headers=self.headers)
        print(response.status_code)
        return response.text

    def getToken(self):
        html = self.session.get(self.url_login_page,headers=self.headers)
        string = 'name="authenticity_token".*?value="(.*?)"'
        zz = re.compile(string,re.S)
        result = re.search(zz,html.text)
        return result.group(1).strip()

    def getPro(self):
        page = self.login();
        fragment = '<li class="public source">.*?</li>'
        zFragment = re.compile(fragment,re.S)
        fragmentResult = re.findall(zFragment,page)

        for f in fragmentResult:
            self.getItem(f)
        return

    def getItem(self,fragment):
        stringUrl = '<a.*?class="mini-repo-list-item css-truncate".*?href="(.*?)".*?<span class="repo">(.*?)</span>'
        zStringUrl = re.compile(stringUrl,re.S)
        allProUrl = re.search(zStringUrl,fragment)
        print(allProUrl.group(2)+"    https://github.com/"+allProUrl.group(1))


print("Github账号登录")
username = raw_input("用户名:")
password = raw_input("密码:")
print("加载中...")
git = Github(username,password)
git.getPro()



