import HotResource
import NormalResource
import Category
import ArticleMain
import threadpool
import threading


articleMain = ArticleMain.ArticleServer()
articleServier = ArticleMain.ArticleServer()
hotResource = HotResource.HotResource()
task_pool=threadpool.ThreadPool(10)#8是线程池中线程的个数
request_list=[]#存放任务列表

#-------------------获取类别---------------------------
Category.getCategory()

#-------------------获取hot资源---------------------------
hotResource.getHot()

#-------------------获取normal资源---------------------------
NormalResource.getNormalResource()

#-------------------hot区---------------------------

articleServier.cur.execute('select url,isload,id from hot')
result = articleServier.cur.fetchall()
paramers_list = []
for item in result:
    if(str(item[1]) == '0'):
        paramers_list.append(item[0])
        # articleServier.getArticle()


request_list=threadpool.makeRequests(articleServier.getArticle,paramers_list)
[task_pool.putRequest(req) for req in request_list]
task_pool.wait()
print('hot all finish')

#-------------------普通区---------------------------
articleServier.cur.execute('select url,isload,id from normal')
result = articleServier.cur.fetchall()
paramers_list = []
index = 0
for item in result:
    if(str(item[1]) == '0'):
        index+=1
        articleServier.getArticle(item[0])

# request_list=threadpool.makeRequests(articleServier.getArticle,paramers_list)
# [task_pool.putRequest(req) for req in request_list]
# task_pool.wait()

print('normal all finish')

