import re
import urllib

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

    def getString(string):
        botton = str.split(string,'?')#xscj_gc.aspx   xh=13223227&xm=关郑委&gnmkdm=N121605
        ss = str.split(botton[1],'&')#xh=13223227  xm=关郑委  gnmkdm=N121605
        s1 = str.split(ss[1],'=')#xm  关郑委
        path = botton[0]+'?'
        path+=s1[0]+'='
        path+=urllib.request.quote(s1[1])+'&'
        path+=ss[0]+'&'
        path+=ss[2]
        return path
