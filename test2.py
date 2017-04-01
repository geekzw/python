import threadpool
import threading
import time

class He:

    def hee(self,url):
        print('heheda')
def hello(x):
    time.sleep(10)
    print('hello')


t = threading.Thread(target=hello,args=('http://www.xxbiquge.com/67_67324/',))
t.start()

print('over')