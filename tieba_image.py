import threading,re,time,requests
from bs4 import BeautifulSoup

task = []
Name = []
n=0


def download(threadname,tieba):
    while len(task) > 0:
        global n
        jpg = requests.get(task.pop()).content
        with open(tieba+'/'+str(Name.pop())+'.jpg','wb') as f:
            f.write(jpg)
        print ("%s" % (threadname)+'剩余：'+str(len(task)))
        
def run(url,tieba):
    startime = time.time()
    r = requests.get(url).text
    for i in re.findall('https://imgsa.baidu.com/forum/.*?jpg',str(r)):
        name = i.split('/')[-1]
        Name.append(name)
        task.append('https://imgsrc.baidu.com/forum/pic/item/'+name)

    for ii in range(6):
        ii = str(ii)
        thread1 = threading.Thread(target=download,args=('线程'+ii,tieba))
        thread1.start()
    thread1.join()  
    print('任务完成，耗时：%s' %(time.time()-startime))
    
if __name__ == "__main__":
    url = input('网址： ')
    run(url,'temp')
